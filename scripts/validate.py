#!/usr/bin/env python3
"""Validate the static site's published HTML structure and local references."""

from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}

# HTML allows these elements to close implicitly when another element starts
# or ends. The validator handles those cases without requiring an HTML5 parser.
OPTIONAL_END_ELEMENTS = {
    "dd",
    "dt",
    "li",
    "optgroup",
    "option",
    "p",
    "rp",
    "rt",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
}

REFERENCE_ATTRIBUTES = {
    ("a", "href"),
    ("form", "action"),
    ("img", "src"),
    ("link", "href"),
    ("script", "src"),
    ("source", "src"),
    ("img", "srcset"),
    ("source", "srcset"),
}


class PageParser(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.errors: list[str] = []
        self.references: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.tags: set[str] = set()
        self.stack: list[str] = []
        self.has_doctype = False

    def error(self, message: str) -> None:
        self.errors.append(message)

    def handle_decl(self, decl: str) -> None:
        if decl.lower().startswith("doctype html"):
            self.has_doctype = True

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        self.tags.add(tag)
        attributes = {name.lower(): value for name, value in attrs}

        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.error(f"duplicate id #{element_id}")
            self.ids.add(element_id)

        for name, value in attrs:
            if (tag, name.lower()) in REFERENCE_ATTRIBUTES and value:
                self.references.append((value, name.lower()))

        if tag in VOID_ELEMENTS:
            return

        if self.stack and tag == self.stack[-1] and tag in OPTIONAL_END_ELEMENTS:
            self.stack.pop()
        self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID_ELEMENTS and self.stack and self.stack[-1] == tag.lower():
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in VOID_ELEMENTS:
            return
        if tag not in self.stack:
            self.error(f"unexpected closing tag </{tag}>")
            return

        if self.stack[-1] == tag:
            self.stack.pop()
            return

        match_index = len(self.stack) - 1 - self.stack[::-1].index(tag)
        dangling = self.stack[match_index + 1 :]
        if any(element not in OPTIONAL_END_ELEMENTS for element in dangling):
            self.error(f"mismatched closing tag </{tag}> (open: <{self.stack[-1]}>)")
            return
        del self.stack[match_index:]


def published_pages() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.html")
        if ".git" not in path.parts
        and "_partials" not in path.parts
        and path.name != "template.html"
    )


def is_external(value: str) -> bool:
    parsed = urlsplit(value)
    return value.startswith("//") or parsed.scheme in {
        "data",
        "http",
        "https",
        "mailto",
        "tel",
    }


def reference_candidates(value: str, attribute: str) -> list[str]:
    if attribute != "srcset":
        return [value.strip()]
    return [candidate.strip().split()[0] for candidate in value.split(",") if candidate.strip()]


def resolve_reference(page: Path, value: str) -> tuple[Path | None, str | None]:
    parsed = urlsplit(value)
    fragment = unquote(parsed.fragment) or None
    path = unquote(parsed.path)

    if not path:
        return page, fragment
    if path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = page.parent / path
    try:
        target = target.resolve()
        target.relative_to(ROOT.resolve())
    except ValueError:
        return None, fragment
    return target, fragment


def validate_reference(page: Path, value: str, attribute: str, page_ids: dict[Path, set[str]]) -> str | None:
    value = value.strip()
    if not value or value.startswith("#") and len(value) == 1 or is_external(value):
        return None

    target, fragment = resolve_reference(page, value)
    if target is None:
        return f"{attribute} escapes site root: {value}"
    if not target.exists():
        return f"missing local target: {value}"
    if fragment and target.suffix.lower() == ".html" and fragment not in page_ids.get(target, set()):
        return f"missing fragment #{fragment} in {value.split('#', 1)[0]}"
    return None


def main() -> int:
    pages = published_pages()
    page_ids: dict[Path, set[str]] = {}
    references: dict[Path, list[tuple[str, str]]] = {}
    errors: list[str] = []

    for page in pages:
        parser = PageParser(page)
        try:
            parser.feed(page.read_text(encoding="utf-8"))
            parser.close()
        except Exception as exc:  # HTMLParser is intentionally forgiving; surface unexpected failures.
            errors.append(f"{page.relative_to(ROOT)}: parser failed: {exc}")
            continue

        relative = page.relative_to(ROOT)
        source = page.read_text(encoding="utf-8")
        for marker, label in (
            ('<meta name="description"', "meta description"),
            ('<link rel="canonical"', "canonical URL"),
            ('property="og:image"', "Open Graph image"),
            ('name="twitter:card"', "Twitter card"),
            ('application/ld+json', "JSON-LD data"),
        ):
            if marker not in source:
                parser.error(f"missing {label}")
        if not parser.has_doctype:
            parser.error("missing <!doctype html>")
        for required in ("html", "head", "body", "title"):
            if required not in parser.tags:
                parser.error(f"missing <{required}>")
        if parser.stack:
            parser.error("unclosed tags: " + ", ".join(parser.stack))

        page_ids[page] = parser.ids
        references[page] = parser.references
        errors.extend(f"{relative}: {message}" for message in parser.errors)

        # Check paths during the first pass. Fragment IDs are checked below after
        # every page has been parsed.
        for raw_value, attribute in parser.references:
            for value in reference_candidates(raw_value, attribute):
                message = validate_reference(page, value, attribute, {})
                if message and not message.startswith("missing fragment"):
                    errors.append(f"{relative}: {message}")

    for page, page_references in references.items():
        for raw_value, attribute in page_references:
            for value in reference_candidates(raw_value, attribute):
                if not value or is_external(value):
                    continue
                target, fragment = resolve_reference(page, value)
                if target and fragment and target.suffix.lower() == ".html" and target.exists():
                    if fragment not in page_ids.get(target, set()):
                        errors.append(
                            f"{page.relative_to(ROOT)}: missing fragment #{fragment} in {value.split('#', 1)[0]}"
                        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s) across {len(pages)} pages.")
        return 1

    print(f"Validated {len(pages)} published HTML pages and their local references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

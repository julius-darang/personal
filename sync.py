#!/usr/bin/env python3
"""Sync _partials/ shared components into all HTML files.

Usage:  python sync.py

Each HTML file uses these marker comments around shared sections:
  <!--#nav--> ... <!--#/nav-->
  <!--#footer--> ... <!--#/footer-->

Variables like {{ROOT}} are resolved from a <!--#set --> block at the file's top:
  <!--#set
    ROOT=../
    ACTIVE_PROJECTS=class="active"
  -->
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS = ROOT / "_partials"

HTML_FILES = [
    "index.html",
    "pages/projects.html",
    "pages/writings.html",
    "proj/visayasgrid.html",
    "blogs/template.html",
    "blogs/modelling-the-philippine-grid.html",
    "blogs/how-i-built-the-visayas-grid.html",
    "blogs/my-first-llm-subscription.html",
    "blogs/visayas-grid-engineering.html",
    "blogs/how-to-build-the-life-you-want.html",
    "blogs/how-to-create-a-website.html",
]

SET_BLOCK_RE = re.compile(r"<!--#set(.*?)-->", re.DOTALL)
VAR_RE = re.compile(r"\{\{(\w+)\}\}")


def load_partial(name: str) -> str:
    path = PARTIALS / name
    return path.read_text(encoding="utf-8") if path.exists() else ""


def extract_vars(content: str) -> dict[str, str]:
    vars_ = {}
    for match in SET_BLOCK_RE.finditer(content):
        for line in match.group(1).strip().split("\n"):
            line = line.strip()
            if "=" in line:
                key, _, val = line.partition("=")
                vars_[key.strip()] = val.strip()
    return vars_


def resolve_vars(text: str, vars_: dict[str, str]) -> str:
    def replacer(m):
        return vars_.get(m.group(1), m.group(0))
    return VAR_RE.sub(replacer, text)


def sync_section(content: str, marker: str, partial_text: str) -> str:
    pattern = re.compile(
        rf"<!--#{marker}-->(.*?)<!--#/{marker}-->", re.DOTALL
    )
    replacement = f"<!--#{marker}-->\n{partial_text}<!--#/{marker}-->"
    if not pattern.search(content):
        print(f"  WARNING: <!--#{marker}--> markers not found")
        return content
    return pattern.sub(replacement, content)


def sync():
    for rel_path in HTML_FILES:
        filepath = ROOT / rel_path
        if not filepath.exists():
            print(f"  SKIP: {rel_path} (not found)")
            continue

        content = filepath.read_text(encoding="utf-8")
        vars_ = extract_vars(content)

        nav = resolve_vars(load_partial("nav.html"), vars_)
        footer = resolve_vars(load_partial("footer.html"), vars_)
        head = resolve_vars(load_partial("head.html"), vars_)

        content = sync_section(content, "nav", nav)
        content = sync_section(content, "footer", footer)
        if "<!--#head-->" in content:
            content = sync_section(content, "head", head)

        filepath.write_text(encoding="utf-8", data=content)
        print(f"  Synced: {rel_path}")


if __name__ == "__main__":
    sync()

#!/usr/bin/env python3
"""Lightweight static site builder.

Usage: python build.py

Each source HTML file can use:
  - `<!--#include file="_partials/foo.html" -->` to include partials
  - `{{VARIABLE_NAME}}` placeholders resolved from a `<!--#set var="NAME" value="..." -->` block

Variables can also span multiple lines. The `#set` block uses a simple key=value
format where the value continues until the next variable or end of comment.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS = ROOT / "_partials"

SOURCE_FILES = [
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

INCLUDE_RE = re.compile(r'<!--#include\s+file="([^"]+)"\s*-->')
SET_RE = re.compile(r'<!--#set\s+var="([^"]+)"\s+value="(.*?)"\s*-->', re.DOTALL)
VAR_RE = re.compile(r"\{\{(\w+)\}\}")


def resolve_includes(content: str) -> str:
    def replacer(match):
        path = match.group(1)
        inc_path = (PARTIALS / path).resolve()
        if not inc_path.exists():
            inc_path = (ROOT / path).resolve()
        if not inc_path.exists():
            print(f"  WARNING: include not found: {path}", file=sys.stderr)
            return f"<!-- MISSING INCLUDE: {path} -->"
        inc_content = inc_path.read_text(encoding="utf-8")
        return resolve_includes(inc_content)
    return INCLUDE_RE.sub(replacer, content)


def extract_vars(content: str) -> dict[str, str]:
    vars = {}
    for match in SET_RE.finditer(content):
        vars[match.group(1)] = match.group(2)
    return vars


def resolve_vars(content: str, vars: dict[str, str]) -> str:
    def replacer(match):
        name = match.group(1)
        if name in vars:
            return vars[name]
        print(f"  WARNING: undefined variable {name}", file=sys.stderr)
        return match.group(0)
    return VAR_RE.sub(replacer, content)


def build():
    for rel_path in SOURCE_FILES:
        src_path = ROOT / rel_path
        if not src_path.exists():
            print(f"  SKIP (not found): {rel_path}", file=sys.stderr)
            continue
        content = src_path.read_text(encoding="utf-8")
        vars = extract_vars(content)
        content = SET_RE.sub("", content)
        content = resolve_includes(content)
        content = resolve_vars(content, vars)
        src_path.write_text(encoding="utf-8", data=content)
        print(f"  Built: {rel_path}")


if __name__ == "__main__":
    build()

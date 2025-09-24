#!/usr/bin/env python3
"""
Reorder `{% tab web %}` to be the first tab inside each `{% tabs ... %} ... {% endtabs %}` block.

Changes:
- No backups. Writes in place.
- Recursively scans ./_docs and ./_includes.
- Detects any `{% tabs ... %}` block (e.g., `{% tabs %}`, `{% tabs local %}`).
- If a `{% tab web %}` (any case) exists and is not already first, move that entire tab section to the top.
- Case-insensitive for tags (`tabs`, `tab`, `endtabs`, `endtab`) and the tab name `web`.
- Dry-run via `--check` to preview changes.

Usage:
  python reorder_web_tab.py            # modify files in place
  python reorder_web_tab.py --check    # list files that would change
  python reorder_web_tab.py --ext .md .html .liquid .mdx  # limit to specific extensions
"""

import argparse
import os
import re
import sys
from typing import List, Tuple

RE_TABS_BLOCK = re.compile(
    r"(?P<open>\{%\s*tabs(?:\s+[^%}]*)?\s*%})(?P<body>.*?)(?P<close>\{%\s*endtabs\s*%})",
    re.IGNORECASE | re.DOTALL,
)

RE_SINGLE_TAB = re.compile(
    r"(?P<full>\{%\s*tab\s+(?P<name>.+?)\s*%}(?P<content>.*?)(?:\{%\s*endtab\s*%}))",
    re.IGNORECASE | re.DOTALL,
)

def normalize_tab_name(raw: str) -> str:
    s = raw.strip().strip('"\''"`")
    s = re.sub(r"\s+", " ", s)
    return s.lower()

def reorder_web_first_in_tabs_block(block_open: str, block_body: str, block_close: str) -> Tuple[str, bool]:
    parts: List[Tuple[str, str]] = []
    order: List[str] = []

    matches = list(RE_SINGLE_TAB.finditer(block_body))
    if not matches:
        return block_open + block_body + block_close, False

    for m in matches:
        full = m.group("full")
        name_raw = m.group("name")
        name_norm = normalize_tab_name(name_raw)
        parts.append((name_norm, full))
        order.append(name_norm)

    if "web" not in order:
        return block_open + block_body + block_close, False
    if order[0] == "web":
        return block_open + block_body + block_close, False

    web_sections = [full for (n, full) in parts if n == "web"]
    other_sections = [full for (n, full) in parts if n != "web"]

    placeholder = "\u0000TAB\u0000"
    body_with_placeholders = RE_SINGLE_TAB.sub(placeholder, block_body)

    reordered_sections = web_sections + other_sections
    out_body = body_with_placeholders
    for section in reordered_sections:
        out_body = out_body.replace(placeholder, section, 1)

    return block_open + out_body + block_close, True

def process_text(text: str) -> Tuple[str, bool]:
    out = []
    last_idx = 0
    changed_any = False

    for m in RE_TABS_BLOCK.finditer(text):
        out.append(text[last_idx:m.start()])
        open_tag = m.group("open")
        body = m.group("body")
        close_tag = m.group("close")

        new_block, changed = reorder_web_first_in_tabs_block(open_tag, body, close_tag)
        out.append(new_block)
        changed_any = changed_any or changed
        last_idx = m.end()

    out.append(text[last_idx:])
    return ("".join(out), changed_any)

def should_process_file(path: str, allowed_exts: List[str]) -> bool:
    if not allowed_exts:
        return True
    _, ext = os.path.splitext(path)
    return ext.lower() in {e.lower() for e in allowed_exts}

def iter_target_files(root_dirs: List[str], allowed_exts: List[str]) -> List[str]:
    files = []
    for root in root_dirs:
        if not os.path.isdir(root):
            continue
        for dirpath, _, filenames in os.walk(root):
            for fn in filenames:
                path = os.path.join(dirpath, fn)
                if should_process_file(path, allowed_exts):
                    files.append(path)
    return files

def main():
    parser = argparse.ArgumentParser(description="Move `{% tab web %}` to first within each `{% tabs %}` block. No backups.")
    parser.add_argument("--check", action="store_true", help="Dry run. Print files that would change.")
    parser.add_argument("--ext", nargs="*", default=[".md", ".markdown", ".mdx", ".html", ".liquid"],
                        help="File extensions to include. Empty list = all files.")
    parser.add_argument("--roots", nargs="*", default=["_docs", "_includes"],
                        help="Root directories to scan.")
    args = parser.parse_args()

    targets = iter_target_files(args.roots, args.ext)

    changed_files = []
    for path in targets:
        try:
            with open(path, "r", encoding="utf-8") as f:
                original = f.read()
        except (UnicodeDecodeError, OSError):
            continue

        new_text, changed = process_text(original)
        if not changed:
            continue

        changed_files.append(path)
        if not args.check:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)

    if args.check:
        if changed_files:
            print("Would modify:")
            for p in changed_files:
                print(f"  {p}")
            sys.exit(1)
        else:
            print("No changes needed.")
            sys.exit(0)
    else:
        if changed_files:
            print("Modified:")
            for p in changed_files:
                print(f"  {p}")
        else:
            print("No changes made.")

if __name__ == "__main__":
    main()

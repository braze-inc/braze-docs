#!/usr/bin/env python3
"""
Reorder `web` to be the first entry in tabs-like blocks.

Supported containers and entries:
- Tabs:    `{% tabs ... %}`     ... `{% endtabs %}`     with `{% tab NAME %}`     ... `{% endtab %}`
- Subtabs: `{% subtabs ... %}`  ... `{% endsubtabs %}`  with `{% subtab NAME %}`  ... `{% endsubtab %}`
- SDKTabs: `{% sdktabs ... %}`  ... `{% endsdktabs %}`  with `{% sdktab NAME %}`  ... `{% endsdktab %}`

Rules:
- If a `web` entry (any case) exists and is not already first, move that whole section to the top.
- Case-insensitive for tag names and the `web` label.
- Recursively scans ./_docs and ./_includes.
- Writes in place. No backups.
- `--check` to preview.

Usage:
  python reorder_web_tab.py
  python reorder_web_tab.py --check
  python reorder_web_tab.py --ext .md .html .liquid .mdx
"""

import argparse
import os
import re
import sys
from typing import List, Tuple

# ----- Block regexes -----
RE_TABS_BLOCK = re.compile(
    r"(?P<open>\{%\s*tabs(?:\s+[^%}]*)?\s*%})(?P<body>.*?)(?P<close>\{%\s*endtabs\s*%})",
    re.IGNORECASE | re.DOTALL,
)
RE_SUBTABS_BLOCK = re.compile(
    r"(?P<open>\{%\s*subtabs(?:\s+[^%}]*)?\s*%})(?P<body>.*?)(?P<close>\{%\s*endsubtabs\s*%})",
    re.IGNORECASE | re.DOTALL,
)
RE_SDKTABS_BLOCK = re.compile(
    r"(?P<open>\{%\s*sdktabs(?:\s+[^%}]*)?\s*%})(?P<body>.*?)(?P<close>\{%\s*endsdktabs\s*%})",
    re.IGNORECASE | re.DOTALL,
)

# ----- Entry regexes -----
RE_TAB_ENTRY = re.compile(
    r"(?P<full>\{%\s*tab\s+(?P<name>.+?)\s*%}(?P<content>.*?)(?:\{%\s*endtab\s*%}))",
    re.IGNORECASE | re.DOTALL,
)
RE_SUBTAB_ENTRY = re.compile(
    r"(?P<full>\{%\s*subtab\s+(?P<name>.+?)\s*%}(?P<content>.*?)(?:\{%\s*endsubtab\s*%}))",
    re.IGNORECASE | re.DOTALL,
)
RE_SDKTAB_ENTRY = re.compile(
    r"(?P<full>\{%\s*sdktab\s+(?P<name>.+?)\s*%}(?P<content>.*?)(?:\{%\s*endsdktab\s*%}))",
    re.IGNORECASE | re.DOTALL,
)

def normalize_label(raw: str) -> str:
    s = raw.strip().strip('"\''"`")
    s = re.sub(r"\s+", " ", s)
    return s.lower()

def reorder_first_in_block(block_open: str, block_body: str, block_close: str, entry_re: re.Pattern) -> Tuple[str, bool]:
    matches = list(entry_re.finditer(block_body))
    if not matches:
        return block_open + block_body + block_close, False

    names = [normalize_label(m.group("name")) for m in matches]
    if "web" not in names or names[0] == "web":
        return block_open + block_body + block_close, False

    parts = [(normalize_label(m.group("name")), m.group("full")) for m in matches]
    web_sections = [full for (n, full) in parts if n == "web"]
    other_sections = [full for (n, full) in parts if n != "web"]

    placeholder = "\u0000ENTRY\u0000"
    body_with_placeholders = entry_re.sub(placeholder, block_body)

    reordered_sections = web_sections + other_sections
    out_body = body_with_placeholders
    for section in reordered_sections:
        out_body = out_body.replace(placeholder, section, 1)

    return block_open + out_body + block_close, True

def process_with_block_regex(text: str, block_re: re.Pattern, entry_re: re.Pattern) -> Tuple[str, bool]:
    out = []
    last = 0
    changed_any = False
    for m in block_re.finditer(text):
        out.append(text[last:m.start()])
        open_tag, body, close_tag = m.group("open"), m.group("body"), m.group("close")
        new_block, changed = reorder_first_in_block(open_tag, body, close_tag, entry_re)
        out.append(new_block)
        changed_any = changed_any or changed
        last = m.end()
    out.append(text[last:])
    return "".join(out), changed_any

def process_text(text: str) -> Tuple[str, bool]:
    # Order: innermost styles first, but they are independent. This order is stable.
    t1, c1 = process_with_block_regex(text, RE_SUBTABS_BLOCK, RE_SUBTAB_ENTRY)
    t2, c2 = process_with_block_regex(t1,   RE_TABS_BLOCK,    RE_TAB_ENTRY)
    t3, c3 = process_with_block_regex(t2,   RE_SDKTABS_BLOCK, RE_SDKTAB_ENTRY)
    return t3, (c1 or c2 or c3)

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
    parser = argparse.ArgumentParser(description="Move `web` to first in tabs, subtabs, and sdktabs blocks. No backups.")
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

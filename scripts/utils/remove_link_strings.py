#!/usr/bin/env python3
"""
remove_link_strings.py
Strips optional "title" strings from Markdown links in the path supplied
(by default under the repo root) and prints a per‑run summary.
"""

import re
import subprocess
import sys
from pathlib import Path

# ── repo root ────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"],
        text=True
    ).strip()
)

# ── path argument ────────────────────────────────────────────────────────────
if len(sys.argv) < 2:
    print("Error: path required. Usage: ./remove_link_strings.py <dir_or_file>")
    sys.exit(1)

REL_PATH = Path(sys.argv[1].lstrip("/"))
SEARCH_PATH = PROJECT_ROOT / REL_PATH

# ── regexes ───────────────────────────────────────────────────────────────────
_inline = re.compile(
    r'(?<!!)\[([^\]]+?)\]\(\s*([^\s)]+?)(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))\s*\)'
)
_refdef = re.compile(
    r'^(\s*\[[^\]]+]:\s+\S+)(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))',
    re.MULTILINE,
)

def _strip_inline(m):
    return f'[{m.group(1)}]({m.group(2)})'

def clean(text: str) -> tuple[str, int]:
    text, n1 = _inline.subn(_strip_inline, text)
    text, n2 = _refdef.subn(r'\1', text)
    return text, n1 + n2

# ── iterate files ────────────────────────────────────────────────────────────
files = (
    [SEARCH_PATH]
    if SEARCH_PATH.is_file()
    else list(SEARCH_PATH.rglob("*.md"))
)

total_files = total_replacements = 0

for md in files:
    original = md.read_text(encoding="utf-8")
    updated, replacements = clean(original)
    if replacements:
        md.write_text(updated, encoding="utf-8")
        total_files += 1
        total_replacements += replacements

print(
    f"Total files updated: {total_files}"
    f"\nTotal strings removed: {total_replacements}"
)

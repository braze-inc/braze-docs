#!/usr/bin/env python3

# A simple utility script that removes strings from within Markdown links.
# It doesn't remove any links from image links or similar--only URLs.
#
# Usage: ./scripts/utils/remove_link_strings.py [FILE|DIRECTORY]
#
# Options:
#   FILE              Remove Markdown link strings in a single file.
#   DIRECTORY         Recursively remove Markdown link strings in a directory.

import re
import subprocess
import sys
from pathlib import Path

# Constants
PROJECT_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"],
        text=True
    ).strip()
)

# Return error if path isn't given.
if len(sys.argv) < 2:
    print("Error: path required. Usage: ./remove_link_strings.py <dir_or_file>")
    sys.exit(1)

REL_PATH = Path(sys.argv[1].lstrip("/"))
SEARCH_PATH = PROJECT_ROOT / REL_PATH

# Regex's for different Markdown link types.
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

# Recursively iterate through given files.
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

#!/usr/bin/env python3
"""
remove_link_strings.py
Strips optional "title" strings from Markdown links under _docs
and prints a per‑file summary plus a final total.
"""

import re
import subprocess
from pathlib import Path

# ── locate repo root and _docs ────────────────────────────────────────────────
PROJECT_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
)
SEARCH_DIR = PROJECT_ROOT / "_docs"

# ── regexes ───────────────────────────────────────────────────────────────────
_inline = re.compile(
    r'(?<!!)\[([^\]]+?)\]\(\s*([^\s)]+?)(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))\s*\)'
)
_refdef = re.compile(
    r'^(\s*\[[^\]]+]:\s+\S+)(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))',
    re.MULTILINE,
)

def _strip_inline(m):                     # keep link text + URL only
    return f'[{m.group(1)}]({m.group(2)})'

def clean(text: str) -> tuple[str, int]:
    """Return cleaned text + number of removals."""
    text, n1 = _inline.subn(_strip_inline, text)
    text, n2 = _refdef.subn(r'\1', text)
    return text, n1 + n2

# ── walk _docs ────────────────────────────────────────────────────────────────
total_files = total_replacements = 0

for md in SEARCH_DIR.rglob("*.md"):
    original = md.read_text(encoding="utf-8")
    updated, replacements = clean(original)
    if replacements:                         # file changed
        md.write_text(updated, encoding="utf-8")
        rel = md.relative_to(Path.cwd())
        total_files        += 1
        total_replacements += replacements

print(
    f"Total files updated: {total_files}"
    f"\nTotal strings removed: {total_replacements}"
)

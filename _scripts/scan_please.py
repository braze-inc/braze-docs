#!/usr/bin/env python3
"""
Scan documentation files for occurrences of the word 'please' (case-insensitive) outside of excluded regions.
Generates a CSV report at _reports/please-occurrences.csv with columns:
file_path,line_number,line_text

Heuristics:
- Process only .md and .html files under _docs.
- Exclude directories: _site, _build, _lang (localized), node_modules if present.
- Skip YAML front matter (between leading --- blocks).
- Skip fenced code blocks (triple backticks) and Liquid tags lines containing '{{' or '{%'.
- Skip inline code spans enclosed in single backticks when isolating matches (do not count 'please' inside them).
- Matches are whole-word: \b[Pp]lease\b

This is a read-only scanner; it does not modify files.
"""
import csv
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / '_docs'
REPORTS_DIR = ROOT / '_reports'
REPORTS_DIR.mkdir(exist_ok=True)
REPORT_PATH = REPORTS_DIR / 'please-occurrences.csv'

EXCLUDED_DIR_PARTS = {'_site', '_build', '_lang', 'node_modules'}
FILE_EXTS = {'.md', '.html'}
WORD_RE = re.compile(r'\b[Pp]lease\b')

# Inline code span pattern
INLINE_CODE_RE = re.compile(r'`[^`]*`')


def should_skip_dir(path: Path) -> bool:
    return any(part in EXCLUDED_DIR_PARTS for part in path.parts)


def scan_file(path: Path):
    rel_path = path.relative_to(ROOT)
    results = []
    try:
        text = path.read_text(encoding='utf-8')
    except Exception:
        return results

    lines = text.splitlines()
    in_front_matter = False
    front_matter_done = False
    in_code_fence = False

    for i, line in enumerate(lines, start=1):
        stripped = line.strip()
        # YAML front matter handling
        if i == 1 and stripped == '---':
            in_front_matter = True
            continue
        if in_front_matter:
            if stripped == '---':
                in_front_matter = False
                front_matter_done = True
            continue

        # Detect fenced code blocks
        if stripped.startswith('```'):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        # Skip Liquid lines entirely
        if '{{' in line or '{%' in line:
            continue

        # Temporarily remove inline code spans to avoid false positives inside them
        def _mask_inline(m):
            return ' ' * (m.end() - m.start())
        masked_line = INLINE_CODE_RE.sub(_mask_inline, line)

        if WORD_RE.search(masked_line):
            results.append((str(rel_path), i, line.rstrip()))
    return results


def main():
    all_results = []
    for root, dirs, files in os.walk(DOCS_DIR):
        root_path = Path(root)
        if should_skip_dir(root_path):
            continue
        for fname in files:
            if Path(fname).suffix in FILE_EXTS:
                fpath = root_path / fname
                all_results.extend(scan_file(fpath))

    # Write CSV
    with REPORT_PATH.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['file_path', 'line_number', 'line_text'])
        for row in all_results:
            writer.writerow(row)

    print(f"Scanned files complete. Matches: {len(all_results)}. Report: {REPORT_PATH}")


if __name__ == '__main__':
    main()

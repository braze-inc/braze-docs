#!/usr/bin/env python3
"""
Re-run present tense conversion (corrected casing) over _docs/_partners.
Rules (conservative):
 1. Phrase mappings (case-insensitive) e.g., "will be" -> "is".
 2. Start-of-phrase user-centric simplification: "You will <verb>" -> "You <verb>", preserving original casing of 'You/you'. Same for "We will".
 3. Keep code blocks, inline code, Liquid tags/variables, YAML front matter, and <code> segments untouched.
 4. Mid-sentence capitalization correction: change capital "You" to lowercase "you" when it appears in the middle of a sentence (preceded by a lowercase letter or digit without sentence-ending punctuation).
Outputs CSV report listing each replacement.
"""
from __future__ import annotations
import re
from pathlib import Path
from csv import writer

PARTNERS_DIR = Path('_docs/_partners')
REPORT_PATH = Path('_reports/present-tense-applied-partners-rerun.csv')

# Ordered specific phrase mappings (avoid over-aggressive changes)
PHRASE_MAPPINGS = [
    (r"\bwill continue to\b", "continues to"),
    (r"\bwill start\b", "starts"),
    (r"\bwill provide\b", "provides"),
    (r"\bwill send\b", "sends"),
    (r"\bwill receive\b", "receives"),
    (r"\bwill update\b", "updates"),
    (r"\bwill appear\b", "appears"),
    (r"\bwill be available\b", "is available"),
    (r"\bwill be created\b", "is created"),
    (r"\bwill be added\b", "is added"),
    (r"\bwill be removed\b", "is removed"),
    (r"\bwill be split into\b", "is split into"),
    (r"\bwill be re-sent\b", "is re-sent"),
]

GENERIC_MAPPINGS = [
    (r"\bwill be\b", "is"),
]

START_PATTERNS = [
    # Preserve original casing of pronoun
    (re.compile(r"\b([Yy]ou)\s+will\b"), lambda m: m.group(1)),
    (re.compile(r"\b(We|we)\s+will\b"), lambda m: m.group(1)),
]

# Mid-sentence capitalization fix: preceding char is lowercase letter/digit and not sentence boundary
MID_SENTENCE_YOU = re.compile(r"(?<![.!?]\s)(?<=\w) You\b")

PROTECT_PATTERNS = [
    re.compile(r"^---.*?^---", re.DOTALL | re.MULTILINE),  # YAML front matter
    re.compile(r"```.*?```", re.DOTALL),                  # fenced code blocks
    re.compile(r"`[^`]*`"),                               # inline code
    re.compile(r"\{%.*?%\}", re.DOTALL),                # Liquid tags
    re.compile(r"\{\{.*?\}\}", re.DOTALL),            # Liquid variables
    re.compile(r"<code>.*?</code>", re.DOTALL | re.IGNORECASE),
]

ReplacementRecord = tuple[str, int, str, str]

def find_protected_spans(text: str):
    spans = []
    for p in PROTECT_PATTERNS:
        for m in p.finditer(text):
            spans.append((m.start(), m.end()))
    spans.sort()
    merged = []
    for s, e in spans:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    return merged

def apply_regex_sequence(segment: str, base_offset: int, regex_pairs, case_insensitive=False):
    flags = re.IGNORECASE if case_insensitive else 0
    out = segment
    records: list[ReplacementRecord] = []
    for pat, repl in regex_pairs:
        pattern = re.compile(pat, flags)
        def _do(m):
            orig = m.group(0)
            replacement = repl
            records.append((orig, m.start()+base_offset, orig, replacement))
            return replacement
        out = pattern.sub(_do, out)
    return out, records

def apply_phrase_mappings(segment: str, base_offset: int):
    records: list[ReplacementRecord] = []
    s = segment
    def sub_fn(pat, replacement):
        nonlocal s, records
        regex = re.compile(pat, re.IGNORECASE)
        def _r(m):
            orig = m.group(0)
            records.append((orig, m.start()+base_offset, orig, replacement))
            return replacement
        s = regex.sub(_r, s)
    for pat, repl in PHRASE_MAPPINGS + GENERIC_MAPPINGS:
        sub_fn(pat, repl)
    return s, records

def apply_start_patterns(segment: str, base_offset: int):
    s = segment
    records: list[ReplacementRecord] = []
    for regex, repl_fn in START_PATTERNS:
        def _r(m):
            orig = m.group(0)
            replacement = repl_fn(m)
            # replacement returns pronoun only; keep trailing space if original had one after 'will'
            # original form 'You will' -> 'You'
            line_portion = replacement
            records.append((orig, m.start()+base_offset, orig, line_portion))
            return line_portion
        s = regex.sub(_r, s)
    return s, records

def apply_mid_sentence_fix(segment: str, base_offset: int):
    s = segment
    records: list[ReplacementRecord] = []
    def _r(m):
        orig = m.group(0)
        replacement = orig.replace('You', 'you', 1)
        records.append((orig, m.start()+base_offset, orig, replacement))
        return replacement
    s = MID_SENTENCE_YOU.sub(_r, s)
    return s, records

def process_text(text: str, path: Path):
    protected = find_protected_spans(text)
    idx = 0
    out_parts = []
    all_changes: list[tuple[int, str, str]] = []  # line, orig, repl
    for s, e in protected:
        if idx < s:
            seg = text[idx:s]
            new_seg, seg_changes = transform_unprotected(seg, base_offset=idx)
            out_parts.append(new_seg)
            all_changes.extend(seg_changes)
        out_parts.append(text[s:e])
        idx = e
    if idx < len(text):
        seg = text[idx:]
        new_seg, seg_changes = transform_unprotected(seg, base_offset=idx)
        out_parts.append(new_seg)
        all_changes.extend(seg_changes)
    new_text = ''.join(out_parts)
    # Convert offsets to line numbers & excerpt
    lines_up_to = lambda off: text[:off].count('\n') + 1
    records_for_csv = []
    for off, orig, repl in all_changes:
        ln = lines_up_to(off)
        excerpt = orig[:120]
        records_for_csv.append((str(path), ln, orig, repl))
    return new_text, records_for_csv

def transform_unprotected(segment: str, base_offset: int):
    # Order: phrase mappings -> start patterns -> mid-sentence fix
    working = segment
    all_changes = []
    working, recs = apply_phrase_mappings(working, base_offset)
    all_changes.extend([(pos, o, r) for (o, pos, _o2, r) in recs])
    working, recs = apply_start_patterns(working, base_offset)
    all_changes.extend([(pos, o, r) for (o, pos, _o2, r) in recs])
    working, recs = apply_mid_sentence_fix(working, base_offset)
    all_changes.extend([(pos, o, r) for (o, pos, _o2, r) in recs])
    return working, all_changes

def main():
    files = [p for p in PARTNERS_DIR.rglob('*') if p.suffix in {'.md', '.html'}]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    changed_files = set()
    for f in files:
        try:
            text = f.read_text(encoding='utf-8')
        except Exception:
            continue
        new_text, recs = process_text(text, f)
        if recs:
            if new_text != text:
                f.write_text(new_text, encoding='utf-8')
            rows.extend(recs)
            changed_files.add(f)
    with REPORT_PATH.open('w', encoding='utf-8', newline='') as csvf:
        w = writer(csvf)
        w.writerow(['file','line','original_excerpt','replacement','confidence'])
        for file, line, orig, repl in rows:
            w.writerow([file, line, orig, repl, 'rerun'])
    print(f"Rerun complete. Changes: {len(rows)} replacements across {len(changed_files)} files. Report: {REPORT_PATH}")

if __name__ == '__main__':
    main()

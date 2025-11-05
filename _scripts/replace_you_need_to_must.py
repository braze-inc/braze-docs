#!/usr/bin/env python3
"""Replace 'you need to' with 'you must' (case preserving) in _docs/_partners.
Skips: YAML front matter, fenced code blocks, inline code, Liquid tags/vars, <code> blocks.
Writes CSV report _reports/you-need-to-replacements.csv.
Conservative: only when followed by a lowercase letter (assumes verb phrase) to reduce semantic false positives.
"""
from __future__ import annotations
import re
from pathlib import Path
from csv import writer

PARTNERS = Path('_docs/_partners')
REPORT = Path('_reports/you-need-to-replacements.csv')

PROTECT = [
    re.compile(r'^---.*?^---', re.MULTILINE|re.DOTALL),
    re.compile(r'```.*?```', re.DOTALL),
    re.compile(r'`[^`]*`'),
    re.compile(r'\{%.*?%\}', re.DOTALL),
    re.compile(r'\{\{.*?\}\}', re.DOTALL),
    re.compile(r'<code>.*?</code>', re.DOTALL|re.IGNORECASE),
]

PATTERN = re.compile(r'\b([Yy]ou) need to (?=[a-z])')


def protected_spans(text:str):
    spans=[]
    for p in PROTECT:
        for m in p.finditer(text):
            spans.append((m.start(), m.end()))
    spans.sort()
    merged=[]
    for s,e in spans:
        if not merged or s>merged[-1][1]:
            merged.append([s,e])
        else:
            merged[-1][1]=max(merged[-1][1], e)
    return merged


def transform_segment(seg:str, base:int, changes:list):
    def repl(m:re.Match):
        pron = m.group(1)
        replacement = f"{pron} must "
        changes.append((base + m.start(), m.group(0), replacement))
        return replacement
    return PATTERN.sub(repl, seg)


def process(text:str):
    spans = protected_spans(text)
    out=[]; idx=0; changes=[]
    for s,e in spans:
        if idx<s:
            seg=text[idx:s]
            out.append(transform_segment(seg, idx, changes))
        out.append(text[s:e])
        idx=e
    if idx < len(text):
        seg=text[idx:]
        out.append(transform_segment(seg, idx, changes))
    new=''.join(out)
    return new, changes


def main():
    files=[p for p in PARTNERS.rglob('*') if p.suffix in {'.md','.html'}]
    rows=[]; modified=0
    for f in files:
        try:
            txt=f.read_text(encoding='utf-8')
        except Exception:
            continue
        new, changes = process(txt)
        if changes:
            f.write_text(new, encoding='utf-8')
            modified+=1
            # line numbers
            for off, orig, repl in changes:
                line = txt[:off].count('\n')+1
                rows.append([str(f), line, orig, repl, 'you-need-to'])
    REPORT.parent.mkdir(exist_ok=True)
    with REPORT.open('w', encoding='utf-8', newline='') as csvf:
        w=writer(csvf)
        w.writerow(['file','line','original','replacement','tag'])
        for r in rows:
            w.writerow(r)
    print(f"Replacements: {len(rows)} in {modified} files. Report: {REPORT}")

if __name__=='__main__':
    main()

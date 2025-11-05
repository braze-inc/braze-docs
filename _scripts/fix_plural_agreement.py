#!/usr/bin/env python3
"""Fix specific plural agreement issues introduced by tense replacement.
Currently targets:
  - 'dashboard reports and CSV reports is' -> 'dashboard reports and CSV reports are'
  - generic '\breports is\b' -> 'reports are' (but keeps preceding context)
Writes a CSV report of changes to _reports/plural-agreement-fixes.csv.
Skips protected spans (YAML front matter, code fences, inline code, Liquid, <code>)."""
from __future__ import annotations
import re
from pathlib import Path
from csv import writer

ROOT = Path('_docs/_partners')
REPORT = Path('_reports/plural-agreement-fixes.csv')

PROTECT = [
    re.compile(r'^---.*?^---', re.MULTILINE|re.DOTALL),
    re.compile(r'```.*?```', re.DOTALL),
    re.compile(r'`[^`]*`'),
    re.compile(r'\{%.*?%\}', re.DOTALL),
    re.compile(r'\{\{.*?\}\}', re.DOTALL),
    re.compile(r'<code>.*?</code>', re.DOTALL|re.IGNORECASE),
]

SPECIFIC = [
    (re.compile(r'dashboard reports and CSV reports is'), 'dashboard reports and CSV reports are'),
]
GENERIC = [
    (re.compile(r'\breports is\b'), 'reports are'),
]

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

def apply_patterns(segment:str, base:int, changes:list):
    s = segment
    def sub_all(patterns):
        nonlocal s
        for rgx, repl in patterns:
            def _r(m):
                orig=m.group(0)
                changes.append((base + m.start(), orig, repl))
                return repl
            s = rgx.sub(_r, s)
    sub_all(SPECIFIC)
    sub_all(GENERIC)
    return s

def process(text:str):
    spans=protected_spans(text)
    out=[]; idx=0; changes=[]
    for s,e in spans:
        if idx<s:
            seg=text[idx:s]
            out.append(apply_patterns(seg, idx, changes))
        out.append(text[s:e])
        idx=e
    if idx<len(text):
        seg=text[idx:]
        out.append(apply_patterns(seg, idx, changes))
    new=''.join(out)
    return new, changes

def main():
    REPORT.parent.mkdir(exist_ok=True)
    rows=[]; modified_files=0
    for f in ROOT.rglob('*'):
        if f.suffix not in {'.md','.html'}: continue
        try:
            text=f.read_text(encoding='utf-8')
        except Exception:
            continue
        new, changes = process(text)
        if changes:
            f.write_text(new, encoding='utf-8')
            modified_files+=1
            for off, orig, repl in changes:
                line = text[:off].count('\n')+1
                rows.append([str(f), line, orig, repl, 'plural-fix'])
    with REPORT.open('w', encoding='utf-8', newline='') as csvf:
        w=writer(csvf)
        w.writerow(['file','line','original','replacement','tag'])
        for r in rows:
            w.writerow(r)
    print(f"Plural fixes: {len(rows)} replacements in {modified_files} files. Report: {REPORT}")

if __name__=='__main__':
    main()

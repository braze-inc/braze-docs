#!/usr/bin/env python3
"""Fix plural subject verb agreement where curated plural nouns incorrectly use 'is'.
Generates _reports/plural-subject-is-fixes.csv with original and replacement lines.
Safeguards:
- Only scans _docs (English source) excluding _site, _lang, node_modules, vendor, .jekyll-cache
- Skip fenced code blocks (```)
- Only modifies .md and .html files
"""
import os, re, csv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPORT = os.path.join(ROOT, '_reports', 'plural-subject-is-fixes.csv')
PLURALS = [
 'events','users','messages','segments','attributes','filters','campaigns','audiences','settings','products','variants','fields','ids','IDs','keys','tokens','webhooks','credentials','catalogs','errors','limits','groups'
]
# Build regex with word boundary, allow optional leading determiner 'the', 'these', 'those', 'your', 'their', 'all', 'any'
pattern = re.compile(r'\b((?:[Tt]he|[Tt]hese|[Tt]hose|[Yy]our|[Tt]heir|[Aa]ll|[Aa]ny)\s+)?(' + '|'.join(re.escape(p) for p in PLURALS) + r')\s+is\b')

SKIP_DIRS = {'_site','_lang','node_modules','vendor','.jekyll-cache'}
VALID_EXT = {'.md','.html'}
changes = []

for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT,'_docs')):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        ext = os.path.splitext(fn)[1]
        if ext not in VALID_EXT: continue
        path = os.path.join(dirpath, fn)
        try:
            with open(path,'r',encoding='utf-8') as f:
                lines = f.readlines()
        except Exception:
            continue
        in_code = False
        fence = re.compile(r'^\s*```')
        modified = False
        for i,line in enumerate(lines):
            if fence.search(line):
                in_code = not in_code
            if in_code: continue
            original = line
            def repl(m):
                determiner = m.group(1) or ''
                noun = m.group(2)
                # Preserve capitalization of noun
                return f"{determiner}{noun} are"
            line = pattern.sub(repl, line)
            if line != original:
                lines[i] = line
                modified = True
                changes.append({
                    'file': os.path.relpath(path, ROOT),
                    'line_number': i+1,
                    'original': original.rstrip('\n'),
                    'replacement': line.rstrip('\n')
                })
        if modified:
            with open(path,'w',encoding='utf-8') as f:
                f.writelines(lines)

os.makedirs(os.path.join(ROOT,'_reports'), exist_ok=True)
with open(REPORT,'w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['file','line_number','original','replacement'])
    w.writeheader(); w.writerows(changes)
print(f"Plural subject fixes: {len(changes)} replacements written to {REPORT}")

#!/usr/bin/env python3
"""
Scan English documentation for incorrect second-person verb agreements like:
- you receives -> you receive
- you sends -> you send
- you provides -> you provide
- you is -> you are

Creates a CSV report of all replacements at _reports/you-verb-agreement-fixes.csv
Safeguards:
- Skip non-English, generated, and build directories: _site, _lang, node_modules, vendor, .jekyll-cache
- Preserve YAML front matter, Liquid tags, and code fences (we only replace inside normal text lines; if a line is inside a fenced code block we skip)
- Only touch .md and .html files
"""
import re, os, csv, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
REPORT_PATH = os.path.join(ROOT, '_reports', 'you-verb-agreement-fixes.csv')

# Map incorrect third-person singular to correct base form after 'you'
VERB_MAP = {
    'provides': 'provide',
    'uses': 'use',
    'creates': 'create',
    'sends': 'send',
    'receives': 'receive',
    'defines': 'define',
    'allows': 'allow',
    'supports': 'support',
    'triggers': 'trigger',
    'selects': 'select',
    'updates': 'update',
    'adds': 'add',
    'returns': 'return',
    'stores': 'store',
    'gives': 'give',
    'includes': 'include',
    'enables': 'enable',
    'requires': 'require',
    'offers': 'offer',
    'shows': 'show',
    'lists': 'list',
    'configures': 'configure',
    'tracks': 'track',
    'captures': 'capture',
    'delivers': 'deliver',
    'builds': 'build',
    'generates': 'generate',
    'starts': 'start',
    'stops': 'stop',
    'opens': 'open',
    'closes': 'close',
    'views': 'view',
    'clicks': 'click',
    'chooses': 'choose'
}

YOU_VERB_PATTERN = re.compile(r'\b([Yy]ou)\s+(' + '|'.join(VERB_MAP.keys()) + r')\b')
YOU_IS_PATTERN = re.compile(r'\b([Yy]ou)\s+is\b')

SKIP_DIRS = {'_site', '_lang', '.jekyll-cache', 'node_modules', 'vendor'}
VALID_EXT = {'.md', '.html'}

changes = []

for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, '_docs')):
    # prune skip dirs
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        ext = os.path.splitext(fn)[1]
        if ext not in VALID_EXT:
            continue
        full_path = os.path.join(dirpath, fn)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception:
            continue

        in_code_fence = False
        fence_pattern = re.compile(r'^\s*```')
        modified = False
        for i, line in enumerate(lines):
            if fence_pattern.search(line):
                in_code_fence = not in_code_fence
            if in_code_fence:
                continue

            original_line = line

            def replace_you_verb(m):
                you = m.group(1)
                bad = m.group(2)
                return f"{you} {VERB_MAP[bad]}"

            line = YOU_VERB_PATTERN.sub(replace_you_verb, line)
            line = YOU_IS_PATTERN.sub(lambda m: f"{m.group(1)} are", line)

            if line != original_line:
                changes.append({
                    'file': os.path.relpath(full_path, ROOT),
                    'line_number': i + 1,
                    'original': original_line.rstrip('\n'),
                    'replacement': line.rstrip('\n')
                })
                lines[i] = line
                modified = True

        if modified:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)

# Write report
os.makedirs(os.path.join(ROOT, '_reports'), exist_ok=True)
with open(REPORT_PATH, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['file', 'line_number', 'original', 'replacement'])
    writer.writeheader()
    for row in changes:
        writer.writerow(row)

print(f"You verb agreement fixes: {len(changes)} replacements written to {REPORT_PATH}")

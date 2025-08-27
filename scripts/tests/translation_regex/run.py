#!/usr/bin/env python3
"""
Wrap all regex matches with $$...$$ in a copy of test.md, then compare to pass.md.

- Source:   ./scripts/tests/translation_regex/test.md
- Expected: ./scripts/tests/translation_regex/pass.md
- Output:   ./scripts/temp/test.md
- Patterns: ./scripts/tests/translation_regex/regex.json

Run from anywhere:
  python3 ./scripts/tests/translation_regex/run.py
"""

import json
import re
import sys
from pathlib import Path
from typing import List, Tuple

# ---------- utilities ----------

def find_project_root(start: Path) -> Path:
    """Walk up to find the repo root (folder that contains 'scripts' or '.git')."""
    cur = start.resolve()
    for p in [cur] + list(cur.parents):
        if (p / "scripts").is_dir() or (p / ".git").is_dir():
            return p
    return cur

def load_patterns(path: Path):
    if not path.exists():
        print(f"missing regex json: {path}", file=sys.stderr)
        sys.exit(2)
    data = json.loads(path.read_text(encoding="utf-8"))
    ordered = sorted(data, key=lambda x: x.get("order", 10**9))
    return [(item.get("name", f"pattern_{i+1}"), item["regex"]) for i, item in enumerate(ordered)]

def collect_spans(text: str, patterns: List[Tuple[str, str]]) -> List[Tuple[int, int]]:
    """Collect all match spans from all patterns without modifying text."""
    spans: List[Tuple[int, int]] = []
    for name, pattern in patterns:
        try:
            rx = re.compile(pattern)
        except re.error as e:
            print(f"regex compile error in '{name}': {e}", file=sys.stderr)
            continue
        for m in rx.finditer(text):
            s, e = m.span()
            if s < e:
                spans.append((s, e))
    return spans

def merge_spans(spans: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Merge overlapping (not merely touching) spans to avoid double wrapping."""
    if not spans:
        return []
    spans.sort()
    merged = [spans[0]]
    for s, e in spans[1:]:
        ms, me = merged[-1]
        if s < me:  # overlap only
            merged[-1] = (ms, max(me, e))
        else:
            merged.append((s, e))
    return merged

def wrap_spans(text: str, spans: List[Tuple[int, int]]) -> str:
    """Insert $$ before and after each merged span."""
    if not spans:
        return text
    out = []
    last = 0
    for s, e in spans:
        out.append(text[last:s])
        out.append("$$")
        out.append(text[s:e])
        out.append("$$")
        last = e
    out.append(text[last:])
    return "".join(out)

# ---------- main ----------

def main():
    # Resolve paths
    this_file = Path(__file__).resolve()
    PROJECT_ROOT = find_project_root(this_file)
    TESTS_DIR = PROJECT_ROOT / "scripts" / "tests" / "translation_regex"
    TEMP_DIR = PROJECT_ROOT / "scripts" / "temp"

    REGEX_FILE = TESTS_DIR / "regex.json"
    SRC_FILE = TESTS_DIR / "test.md"
    PASS_FILE = TESTS_DIR / "pass.md"
    DST_FILE = TEMP_DIR / "test.md"

    # Validate inputs
    if not SRC_FILE.exists():
        print(f"missing source file: {SRC_FILE}", file=sys.stderr)
        sys.exit(2)
    if not PASS_FILE.exists():
        print(f"missing pass file: {PASS_FILE}", file=sys.stderr)
        sys.exit(2)

    patterns = load_patterns(REGEX_FILE)

    # Read, mark, write
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    src_text = SRC_FILE.read_text(encoding="utf-8")

    spans = collect_spans(src_text, patterns)
    merged = merge_spans(spans)
    out_text = wrap_spans(src_text, merged)

    DST_FILE.write_text(out_text, encoding="utf-8")

    # Compare
    expected = PASS_FILE.read_text(encoding="utf-8")
    if out_text == expected:
        print("test pass")
        sys.exit(0)

    print("test failed")
    out_lines = out_text.splitlines()
    exp_lines = expected.splitlines()
    max_len = max(len(out_lines), len(exp_lines))
    failed = []
    for i in range(max_len):
        got = out_lines[i] if i < len(out_lines) else ""
        exp = exp_lines[i] if i < len(exp_lines) else ""
        if got != exp:
            failed.append(i + 1)  # 1-based
    if failed:
        print("mismatched lines:", ", ".join(str(n) for n in failed))
    sys.exit(1)

if __name__ == "__main__":
    main()

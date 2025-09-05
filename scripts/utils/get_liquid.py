#!/usr/bin/env python3

# Generates a list of all the built-in and unique liquid we use in the
# '_docs' and '_includes' directories.

import re
import json
from pathlib import Path

# Resolve project root (script is expected in ./scripts/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Scan roots
ROOTS = [PROJECT_ROOT / "_docs", PROJECT_ROOT / "_includes"]

# Directories to skip (relative to project root)
skip_dirs = [
    "_docs/_docs_pages",
]

OUT_DIR = PROJECT_ROOT / "scripts" / "temp"
OUT_FILE = OUT_DIR / "liquid_refs.json"

# Liquid outputs and tags
LIQUID_PATTERNS = [
    re.compile(r"{{-?\s*.*?\s*-?}}"),   # {{ ... }}
    re.compile(r"{%-?\s*.*?\s*-?%}"),   # {% ... %}
]

# Fenced code blocks and inline code
FENCE_RE = re.compile(r"^\s*([`~]{3,})(.*)$")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

# Normalize:
# 1) "{% WORD anything %}" -> "{% WORD %}"
# 2) "{% WORD/anything %}" -> "{% WORD %}"
# Preserve optional trim hyphens: {%-, -%}
SIMPLE_TAG_NORMALIZER_RE = re.compile(
    r"^{%(-?)\s*([A-Za-z_][\w-]*)(?:\s+|/).*?(-?)%}$"
)

def strip_fenced_blocks(text: str) -> str:
    out_lines = []
    in_fence = False
    fence_marker = None
    for line in text.splitlines(keepends=False):
        if not in_fence:
            m = FENCE_RE.match(line)
            if m:
                in_fence = True
                fence_marker = m.group(1)
                continue
            out_lines.append(line)
        else:
            if line.strip().startswith(fence_marker):
                in_fence = False
                fence_marker = None
            continue
    return "\n".join(out_lines)

def remove_inline_code(text: str) -> str:
    return INLINE_CODE_RE.sub("", text)

def normalize_simple_tag(s: str) -> str:
    st = s.strip()
    m = SIMPLE_TAG_NORMALIZER_RE.match(st)
    if not m:
        return st
    left_hy, word, right_hy = m.groups()
    l = "-" if left_hy else ""
    r = "-" if right_hy else ""
    return f"{{%{l} {word} {r}%}}"

def find_liquid(text: str) -> list[str]:
    hits = []
    for pat in LIQUID_PATTERNS:
        hits.extend(pat.findall(text))
    return hits

def file_is_text(path: Path) -> bool:
    skip_exts = {
        ".png",".jpg",".jpeg",".gif",".webp",".svg",".pdf",
        ".zip",".gz",".tar",".tgz",".bz2",".7z",
        ".woff",".woff2",".ttf",".otf",
        ".mp4",".mov",".webm",".mp3",".wav",
    }
    return path.suffix.lower() not in skip_exts

def is_in_skip_dir(path: Path) -> bool:
    p = path.resolve()
    for rel in skip_dirs:
        base = (PROJECT_ROOT / rel).resolve()
        if base in p.parents:
            return True
    return False

def gather_files(roots: list[Path]) -> list[Path]:
    files = []
    for base in roots:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            if p.is_file() and file_is_text(p) and not is_in_skip_dir(p):
                files.append(p)
    return files

def main():
    uniques: set[str] = set()
    for f in gather_files(ROOTS):
        try:
            text = f.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        text_no_fences = strip_fenced_blocks(text)
        text_clean = remove_inline_code(text_no_fences)
        for hit in find_liquid(text_clean):
            uniques.add(normalize_simple_tag(hit))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_FILE.open("w", encoding="utf-8") as fh:
        json.dump(sorted(uniques), fh, ensure_ascii=False, indent=2)

    print(f"Wrote {OUT_FILE} with {len(uniques)} unique items.")

if __name__ == "__main__":
    main()

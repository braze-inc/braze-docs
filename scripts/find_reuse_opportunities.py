#!/usr/bin/env python3

"""
Scans _docs/ for markdown files and identifies duplicate and near-duplicate
text blocks that could be extracted into _includes/ files.

Usage:  python scripts/find_reuse_opportunities.py
Output: scripts/temp/reuse_report.md
"""

import re
import hashlib
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "_docs"
OUT_DIR = PROJECT_ROOT / "scripts" / "temp"
OUT_FILE = OUT_DIR / "reuse_report.md"

# --- Tuning knobs ---
MIN_BLOCK_LINES = 3
MIN_BLOCK_WORDS = 25
SIMILARITY_THRESHOLD = 0.75
SHINGLE_SIZE = 4
MAX_SHINGLE_FREQ = 25

# Fenced code block detection (mirrors get_liquid.py)
FENCE_RE = re.compile(r"^\s*([`~]{3,})")


# ── Text cleaning ────────────────────────────────────────────────────────────

def strip_front_matter(content: str) -> str:
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3 :]
    return content


def strip_fenced_blocks(text: str) -> str:
    out, in_fence, marker = [], False, None
    for line in text.splitlines():
        if not in_fence:
            m = FENCE_RE.match(line)
            if m:
                in_fence, marker = True, m.group(1)
                continue
            out.append(line)
        elif line.strip().startswith(marker):
            in_fence, marker = False, None
    return "\n".join(out)


def clean_content(content: str) -> str:
    content = re.sub(
        r"^[ \t]*\{%-?\s*(multi_lang_)?include\s+.*?-?%\}[ \t]*$",
        "",
        content,
        flags=re.MULTILINE,
    )
    content = re.sub(r"\{%.*?%\}", "", content)
    content = re.sub(r"\{\{.*?\}\}", "", content)
    content = re.sub(r"<[^>]+>", "", content)
    content = re.sub(r"!\[.*?\]\(.*?\)", "", content)
    content = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", content)
    return content


# ── Block extraction ─────────────────────────────────────────────────────────

def _is_table_block(lines: list[str]) -> bool:
    """True if the block is a Markdown table (most lines start with |)."""
    pipe_lines = sum(1 for l in lines if l.lstrip().startswith("|"))
    return pipe_lines > len(lines) / 2


def extract_blocks(content: str) -> list[str]:
    content = strip_front_matter(content)
    content = strip_fenced_blocks(content)
    content = clean_content(content)

    blocks = []
    for raw in re.split(r"\n\s*\n", content):
        lines = [l.strip() for l in raw.strip().splitlines() if l.strip()]
        while lines and lines[0].startswith("#"):
            lines.pop(0)
        if len(lines) < MIN_BLOCK_LINES:
            continue
        if _is_table_block(lines):
            continue
        text = "\n".join(lines)
        if len(text.split()) < MIN_BLOCK_WORDS:
            continue
        blocks.append(text)
    return blocks


# ── Hashing / shingling helpers ──────────────────────────────────────────────

def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def make_shingles(norm: str) -> set[tuple[str, ...]]:
    words = norm.split()
    if len(words) < SHINGLE_SIZE:
        return set()
    return {
        tuple(words[i : i + SHINGLE_SIZE])
        for i in range(len(words) - SHINGLE_SIZE + 1)
    }


# ── Union-Find for grouping near-duplicates ──────────────────────────────────

class UnionFind:
    def __init__(self):
        self._p: dict[int, int] = {}

    def find(self, x: int) -> int:
        self._p.setdefault(x, x)
        while self._p[x] != x:
            self._p[x] = self._p[self._p[x]]
            x = self._p[x]
        return x

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self._p[ra] = rb

    def groups(self) -> list[set[int]]:
        clusters: dict[int, set[int]] = defaultdict(set)
        for x in self._p:
            clusters[self.find(x)].add(x)
        return list(clusters.values())


# ── Core analysis ────────────────────────────────────────────────────────────

SKIP_DIRS = {"_hidden"}


def analyze():
    md_files = sorted(
        f for f in DOCS_DIR.rglob("*.md")
        if not any(part in SKIP_DIRS for part in f.relative_to(DOCS_DIR).parts)
    )
    print(f"Scanning {len(md_files)} markdown files in _docs/ ...")

    entries: list[dict] = []
    files_with_blocks = 0

    for md in md_files:
        try:
            content = md.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        blocks = extract_blocks(content)
        if not blocks:
            continue
        files_with_blocks += 1
        rel = str(md.relative_to(PROJECT_ROOT))
        for block in blocks:
            norm = normalize(block)
            entries.append(
                {
                    "idx": len(entries),
                    "file": rel,
                    "text": block,
                    "norm": norm,
                    "hash": hashlib.md5(norm.encode()).hexdigest(),
                    "shingles": make_shingles(norm),
                    "words": len(block.split()),
                }
            )

    print(f"Extracted {len(entries)} text blocks from {files_with_blocks} files")

    # ── Exact duplicates ─────────────────────────────────────────────────
    by_hash: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_hash[e["hash"]].append(e)

    exact_groups = []
    exact_indices: set[int] = set()
    for h, group in by_hash.items():
        files = set(e["file"] for e in group)
        if len(files) >= 2:
            exact_groups.append(group)
            exact_indices.update(e["idx"] for e in group)

    exact_groups.sort(
        key=lambda g: (len(set(e["file"] for e in g)), g[0]["words"]), reverse=True
    )
    print(f"Found {len(exact_groups)} exact duplicate groups")

    # ── Near duplicates (shingle-based candidate search → Jaccard) ───────
    shingle_idx: dict[tuple, set[int]] = defaultdict(set)
    for e in entries:
        for s in e["shingles"]:
            shingle_idx[s].add(e["idx"])

    pair_hits: dict[tuple[int, int], int] = defaultdict(int)
    for s, idxs in shingle_idx.items():
        if len(idxs) > MAX_SHINGLE_FREQ:
            continue
        members = list(idxs)
        for i in range(len(members)):
            for j in range(i + 1, len(members)):
                a, b = members[i], members[j]
                if entries[a]["file"] == entries[b]["file"]:
                    continue
                pair_hits[(min(a, b), max(a, b))] += 1

    uf = UnionFind()
    for (a, b), hits in pair_hits.items():
        if hits < 3:
            continue
        if entries[a]["hash"] == entries[b]["hash"]:
            continue
        sa, sb = entries[a]["shingles"], entries[b]["shingles"]
        if not sa or not sb:
            continue
        jaccard = len(sa & sb) / len(sa | sb)
        if jaccard >= SIMILARITY_THRESHOLD:
            uf.union(a, b)

    near_groups = []
    for group_idxs in uf.groups():
        group = [entries[i] for i in group_idxs]
        files = set(e["file"] for e in group)
        if len(files) >= 2:
            near_groups.append(group)

    near_groups.sort(
        key=lambda g: len(set(e["file"] for e in g)) * max(e["words"] for e in g),
        reverse=True,
    )
    print(f"Found {len(near_groups)} near-duplicate groups")

    return files_with_blocks, len(entries), exact_groups, near_groups


# ── Report generation ────────────────────────────────────────────────────────

def _savings(exact_groups, near_groups):
    ew = sum(
        g[0]["words"] * (len(set(e["file"] for e in g)) - 1) for g in exact_groups
    )
    nw = sum(
        int(sum(e["words"] for e in g) / len(g))
        * (len(set(e["file"] for e in g)) - 1)
        for g in near_groups
    )
    return ew, nw


def generate_report(total_files, total_blocks, exact_groups, near_groups):
    ew, nw = _savings(exact_groups, near_groups)
    lines: list[str] = []

    lines.append("# Content Reuse Opportunities\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Files scanned | {total_files} |")
    lines.append(f"| Text blocks analyzed | {total_blocks} |")
    lines.append(f"| Exact duplicate groups | {len(exact_groups)} |")
    lines.append(f"| Near-duplicate groups | {len(near_groups)} |")
    lines.append(f"| Est. words saved (exact) | ~{ew:,} |")
    lines.append(f"| Est. words saved (near) | ~{nw:,} |")
    lines.append(f"| **Total est. words saved** | **~{ew + nw:,}** |")
    lines.append("")
    lines.append(
        "> Extract each group into an `_includes/` file and replace the original"
    )
    lines.append(
        "> content with `{% multi_lang_include path/to/include.md %}`.\n"
    )
    lines.append("---\n")

    # ── Exact duplicates ─────────────────────────────────────────────────
    lines.append("## Exact Duplicates\n")
    for i, group in enumerate(exact_groups, 1):
        files = sorted(set(e["file"] for e in group))
        sample = group[0]
        lines.append(f"### Exact #{i} — {len(files)} files, ~{sample['words']} words\n")
        lines.append("**Found in:**\n")
        for f in files:
            lines.append(f"- `{f}`")
        lines.append("")
        lines.append("**Content:**\n")
        lines.append("````markdown")
        lines.append(sample["text"])
        lines.append("````\n")

    # ── Near duplicates ──────────────────────────────────────────────────
    lines.append("---\n")
    lines.append("## Near Duplicates\n")
    for i, group in enumerate(near_groups[:200], 1):
        files = sorted(set(e["file"] for e in group))
        avg_words = sum(e["words"] for e in group) // len(group)
        lines.append(
            f"### Near #{i} — {len(files)} files, ~{avg_words} words avg\n"
        )

        seen: dict[str, dict] = {}
        for e in group:
            h = e["hash"]
            if h not in seen:
                seen[h] = {"entry": e, "files": []}
            seen[h]["files"].append(e["file"])

        for vi, (h, variant) in enumerate(seen.items(), 1):
            vf = sorted(set(variant["files"]))
            label = chr(64 + vi)
            lines.append(
                f"**Variant {label}** ({len(vf)} file{'s' if len(vf) != 1 else ''}):\n"
            )
            for f in vf:
                lines.append(f"- `{f}`")
            lines.append("")
            lines.append("````markdown")
            lines.append(variant["entry"]["text"])
            lines.append("````\n")

    if len(near_groups) > 200:
        lines.append(f"\n*...and {len(near_groups) - 200} more groups omitted.*\n")

    return "\n".join(lines)


# ── Entrypoint ───────────────────────────────────────────────────────────────

def main():
    total_files, total_blocks, exact_groups, near_groups = analyze()
    report = generate_report(total_files, total_blocks, exact_groups, near_groups)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(report, encoding="utf-8")
    print(f"\nReport written to {OUT_FILE.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()

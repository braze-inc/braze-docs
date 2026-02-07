#!/usr/bin/env python3
"""
IA Restructure Visualization Toolkit

Generates current IA from the repo, parses proposed IA from revised_ia.md,
fuzzy-matches entries, and produces comparison artifacts.

Usage:
    python3 scripts/generate_ia_tree.py

Outputs to _ia_audit/:
    ia_current.yaml        - Current IA as nested YAML tree
    ia_current.csv         - Flat inventory of all current pages
    ia_overview_current.md - Mermaid diagram of current IA
    ia_proposed.yaml       - Proposed IA as nested YAML tree
    ia_migration.csv       - Migration tracker with current->proposed mappings
    ia_comparison.md       - Side-by-side Mermaid diagrams + change summary
    gap_report.md          - Unmatched/ambiguous entries for review
"""

import os
import re
import csv
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Tuple
from difflib import SequenceMatcher

try:
    import yaml
except ImportError:
    print("Error: PyYAML required. Install with: pip3 install pyyaml")
    sys.exit(1)


# ============================================================
# Data structures
# ============================================================

@dataclass
class PageInfo:
    """A page in the current IA."""
    path: str
    nav_title: str = ""
    article_title: str = ""
    page_order: float = 0
    hidden: bool = False
    config_only: bool = False


@dataclass
class TreeNode:
    """A node in the IA tree (current or proposed)."""
    title: str
    path: str = ""
    page_order: float = 0
    page_count: int = 0
    annotation: str = ""
    hidden: bool = False
    config_only: bool = False
    children: list = field(default_factory=list)

    def count_descendants(self):
        """Count total descendants including self (if not root/config-only)."""
        count = 1 if self.title else 0
        for child in self.children:
            count += child.count_descendants()
        self.page_count = count
        return count


# ============================================================
# Frontmatter parser
# ============================================================

def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file using PyYAML."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, FileNotFoundError):
        return {}

    if not content.startswith('---'):
        return {}

    end = content.find('\n---', 3)
    if end == -1:
        return {}

    fm_text = content[4:end]
    try:
        result = yaml.safe_load(fm_text)
        return result if isinstance(result, dict) else {}
    except yaml.YAMLError:
        return {}


# ============================================================
# Current IA: Walk the repo
# ============================================================

def walk_user_guide(root_dir):
    """Walk _docs/_user_guide/ and build current IA tree + flat page list."""
    user_guide_dir = os.path.join(root_dir, '_docs', '_user_guide')
    if not os.path.isdir(user_guide_dir):
        print(f"Error: {user_guide_dir} not found")
        sys.exit(1)

    all_pages = []
    tree = TreeNode(title="User Guide")

    def walk_dir(dir_path, parent_node, depth=0):
        """Recursively walk directory and build tree."""
        try:
            items = sorted(os.listdir(dir_path))
        except PermissionError:
            return

        md_files = []
        subdirs = []

        for item in items:
            full_path = os.path.join(dir_path, item)
            if os.path.isfile(full_path) and item.endswith('.md'):
                md_files.append(full_path)
            elif os.path.isdir(full_path) and not item.startswith('.'):
                subdirs.append(full_path)

        # Track which subdirs are matched to an .md file
        matched_subdirs = set()

        for fpath in md_files:
            fm = parse_frontmatter(fpath)
            rel_path = os.path.relpath(fpath, root_dir)
            basename_no_ext = os.path.splitext(os.path.basename(fpath))[0]

            nav_title = fm.get('nav_title', basename_no_ext.replace('_', ' ').title())
            article_title = fm.get('article_title', nav_title)
            page_order = fm.get('page_order', 999)
            hidden = fm.get('hidden', False)
            config_only = fm.get('config_only', False)

            # Coerce types
            if isinstance(page_order, str):
                try:
                    page_order = float(page_order)
                except ValueError:
                    page_order = 999
            if not isinstance(page_order, (int, float)):
                page_order = 999

            page = PageInfo(
                path=rel_path,
                nav_title=str(nav_title) if nav_title else basename_no_ext,
                article_title=str(article_title) if article_title else "",
                page_order=float(page_order),
                hidden=bool(hidden),
                config_only=bool(config_only),
            )
            all_pages.append(page)

            node = TreeNode(
                title=page.nav_title,
                path=rel_path,
                page_order=page.page_order,
                hidden=page.hidden,
                config_only=page.config_only,
            )

            # Check if this .md file has a corresponding subdirectory
            matching_subdir = os.path.join(dir_path, basename_no_ext)
            if matching_subdir in subdirs:
                walk_dir(matching_subdir, node, depth + 1)
                matched_subdirs.add(matching_subdir)

            parent_node.children.append(node)

        # Process remaining subdirectories (no matching .md file)
        for subdir in subdirs:
            if subdir in matched_subdirs:
                continue
            dirname = os.path.basename(subdir)
            node = TreeNode(
                title=dirname.replace('_', ' ').title(),
                path=os.path.relpath(subdir, root_dir),
                config_only=True,
            )
            walk_dir(subdir, node, depth + 1)
            if node.children:
                parent_node.children.append(node)

        # Sort children by page_order
        parent_node.children.sort(key=lambda n: n.page_order)

    walk_dir(user_guide_dir, tree)
    tree.count_descendants()

    return tree, all_pages


# ============================================================
# Proposed IA: Parse revised_ia.md
# ============================================================

# Keywords that indicate a parenthetical is an annotation, not part of the title
ANNOTATION_KEYWORDS = [
    'new article', 'new landing', 'new page',
    'combines', 'combine', 'combining',
    'renaming', 'rename',
    'remove', 'removing', 'delete',
    'updates ', 'update existing', 'update article', 'update landing', 'update ',
    'rewrite',
    'landing page is', 'landing page becomes', 'landing page describes',
    'landing page provides', 'landing page contains', 'landing page should',
    'becomes landing', 'becomes introduction',
    'fold', 'folding',
    'pull', 'pulling',
    'currently', 'current ',
    'should include', 'should be',
    'would consist', 'would be', 'would explain', 'would pull',
    'from:', 'From:',
    'includes content', 'includes tile',
    'will be',
    'waiting',
    'no changes',
    'overview of the channel', 'overview of the',
    'braze overview',
    'then remove',
    'divides into',
]


def extract_title_and_annotation(text):
    """Extract title and annotation from a proposed IA entry.

    Annotations are in parentheses and contain known keywords.
    E.g., "Email (landing page is an overview of the channel)" -> ("Email", "landing page is...")
    But "Custom app icon feature (iOS 10.3)" -> ("Custom app icon feature (iOS 10.3)", "")
    """
    # Find the first ( preceded by a space that starts an annotation
    for i, char in enumerate(text):
        if char == '(' and i > 0 and text[i - 1] == ' ':
            rest = text[i + 1:]
            rest_lower = rest.lower()
            if any(kw in rest_lower for kw in ANNOTATION_KEYWORDS):
                title = text[:i].strip()
                # Take everything after the ( as annotation, strip trailing ) chars
                annotation = rest.rstrip(')').strip()
                return title, annotation

    return text.strip(), ""


def parse_revised_ia(filepath):
    """Parse revised_ia.md indented list format into a tree."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    root = TreeNode(title="User Guide (Proposed)")
    stack = [(-1, root)]  # (indent_level, node)

    for line_num, raw_line in enumerate(lines, 1):
        stripped = raw_line.rstrip()
        if not stripped:
            continue

        # Count leading whitespace
        indent = len(raw_line) - len(raw_line.lstrip())

        # Check if this is a list item (starts with "- " after whitespace)
        trimmed = raw_line.lstrip()
        if not trimmed.startswith('- '):
            # Non-list line (e.g., "Related articles: API endpoints")
            # Attach as annotation to most recent node
            if stack and len(stack) > 1:
                parent_node = stack[-1][1]
                if parent_node.annotation:
                    parent_node.annotation += "; " + trimmed.strip()
                else:
                    parent_node.annotation = trimmed.strip()
            continue

        # Extract the content after "- " (handle extra spaces)
        item_text = re.sub(r'^-\s+', '', trimmed).strip()

        # Separate title from annotation
        title, annotation = extract_title_and_annotation(item_text)

        node = TreeNode(title=title, annotation=annotation)

        # Find parent based on indentation using stack
        while len(stack) > 1 and stack[-1][0] >= indent:
            stack.pop()

        parent = stack[-1][1]
        parent.children.append(node)
        stack.append((indent, node))

    # Count entries
    root.count_descendants()
    return root


# ============================================================
# Matching: Current <-> Proposed
# ============================================================

def normalize_title(title):
    """Normalize a title for comparison."""
    t = title.lower().strip()
    # Remove common prefixes/suffixes that vary
    t = re.sub(r'^(create|set up|about)\s+(a|an|the)\s+', '', t)
    return t


def title_similarity(a, b):
    """Compute similarity between two titles."""
    return SequenceMatcher(None, a.lower().strip(), b.lower().strip()).ratio()


def build_path_hints(path):
    """Extract section hints from a file path."""
    parts = path.replace('_docs/_user_guide/', '').replace('.md', '').split('/')
    return [p.replace('_', ' ').replace('-', ' ').lower() for p in parts]


def breadcrumb_overlap(proposed_parents, current_path_hints):
    """Score how well proposed breadcrumb matches current path."""
    score = 0
    for pp in proposed_parents:
        pp_norm = pp.lower().replace('-', ' ').replace('_', ' ')
        for ch in current_path_hints:
            if pp_norm in ch or ch in pp_norm:
                score += 1
                break
            # Also check partial overlap
            if title_similarity(pp_norm, ch) > 0.7:
                score += 0.5
                break
    return score


def flatten_proposed(node, depth=0, parents=None):
    """Flatten proposed tree into list of (node, depth, parent_titles)."""
    if parents is None:
        parents = []
    results = []
    if depth > 0:
        results.append((node, depth, list(parents)))
    child_parents = parents + ([node.title] if depth > 0 else [])
    for child in node.children:
        results.extend(flatten_proposed(child, depth + 1, child_parents))
    return results


def is_marked_new(annotation):
    """Check if an annotation indicates this is a new page."""
    if not annotation:
        return False
    ann_lower = annotation.lower()
    return bool(re.search(r'\bnew\s+(article|landing\s*page|page)\b', ann_lower))


def determine_change_type(annotation):
    """Determine the change type from an annotation."""
    if not annotation:
        return None
    ann_lower = annotation.lower()

    if re.search(r'\bnew\s+(article|landing\s*page|page)\b', ann_lower):
        return 'new'
    if any(kw in ann_lower for kw in ['combin', 'fold', 'merge', 'pull']):
        return 'merged'
    if any(kw in ann_lower for kw in ['rename', 'renaming']):
        return 'renamed'
    if any(kw in ann_lower for kw in ['remove', 'delete']):
        return 'removed'
    if any(kw in ann_lower for kw in ['update', 'rewrite']):
        return 'updated'
    return None


def infer_proposed_path(parents, title):
    """Infer a proposed file path from the hierarchy."""
    parts = []
    for p in parents:
        slug = p.lower().strip()
        slug = re.sub(r'[^a-z0-9\s]', '', slug)
        slug = re.sub(r'\s+', '_', slug)
        parts.append(slug)
    title_slug = title.lower().strip()
    title_slug = re.sub(r'[^a-z0-9\s]', '', title_slug)
    title_slug = re.sub(r'\s+', '_', title_slug)
    parts.append(title_slug)
    return '_docs/_user_guide/' + '/'.join(parts) + '.md'


def match_proposed_to_current(proposed_tree, all_pages):
    """Match proposed entries to current pages using title + context."""
    # Build lookup: normalized title -> list of pages
    title_to_pages: Dict[str, List[PageInfo]] = {}
    for page in all_pages:
        norm = page.nav_title.lower().strip()
        if norm not in title_to_pages:
            title_to_pages[norm] = []
        title_to_pages[norm].append(page)

    # Build path hints for each page
    path_hints = {page.path: build_path_hints(page.path) for page in all_pages}

    # Flatten proposed tree
    proposed_flat = flatten_proposed(proposed_tree)

    migrations = []
    matched_current_paths = set()
    unmatched_proposed = []

    for node, depth, parents in proposed_flat:
        proposed_section = ' > '.join(parents + [node.title])

        # Check if explicitly new
        if is_marked_new(node.annotation):
            migrations.append({
                'nav_title': node.title,
                'current_path': '',
                'proposed_section': proposed_section,
                'proposed_path': infer_proposed_path(parents, node.title),
                'change_type': 'new',
                'annotation': node.annotation,
            })
            continue

        # Try exact title match
        norm_title = node.title.lower().strip()
        candidates = title_to_pages.get(norm_title, [])

        # If no exact match, try fuzzy with lower threshold
        if not candidates:
            best_score = 0
            best_pages = []
            for page_title, pages in title_to_pages.items():
                score = title_similarity(norm_title, page_title)
                if score > 0.70 and score > best_score:
                    best_score = score
                    best_pages = pages
            candidates = best_pages

        # If still no match, try substring matching (e.g., "A/B testing" in
        # "Multivariate & A/B testing")
        if not candidates:
            for page_title, pages in title_to_pages.items():
                if norm_title in page_title or page_title in norm_title:
                    candidates = pages
                    break

        if not candidates:
            # Still no match - add to unmatched
            unmatched_proposed.append({
                'nav_title': node.title,
                'proposed_section': proposed_section,
                'annotation': node.annotation,
            })
            continue

        # Pick best candidate using breadcrumb context
        if len(candidates) == 1:
            best_page = candidates[0]
        else:
            # Score each candidate by breadcrumb overlap
            scored = []
            for page in candidates:
                hints = path_hints.get(page.path, [])
                proposed_parents_norm = [p.lower() for p in parents]
                score = breadcrumb_overlap(proposed_parents_norm, hints)
                # Bonus for already-matched (prefer unmatched)
                if page.path in matched_current_paths:
                    score -= 2
                scored.append((score, page))
            scored.sort(key=lambda x: -x[0])
            best_page = scored[0][1]

        # Determine change type
        change_type = determine_change_type(node.annotation)
        if not change_type:
            # Check if section changed by comparing path structures
            current_hints = path_hints.get(best_page.path, [])
            proposed_parents_norm = [p.lower().replace(' ', '_').replace('-', '_')
                                     for p in parents]
            # Simple heuristic: if the top-level section name changed, it's "moved"
            if current_hints and proposed_parents_norm:
                if current_hints[0] != proposed_parents_norm[0]:
                    change_type = 'moved'
                else:
                    change_type = 'unchanged'
            else:
                change_type = 'unchanged'

        matched_current_paths.add(best_page.path)
        migrations.append({
            'nav_title': node.title,
            'current_path': best_page.path,
            'proposed_section': proposed_section,
            'proposed_path': infer_proposed_path(parents, node.title),
            'change_type': change_type,
            'annotation': node.annotation,
        })

    # Find current pages not mentioned in proposed
    unmatched_current = []
    for page in all_pages:
        if page.path not in matched_current_paths:
            unmatched_current.append(page)

    return migrations, unmatched_proposed, unmatched_current


# ============================================================
# Output: YAML tree
# ============================================================

def tree_to_dict(node):
    """Convert TreeNode to a dict for YAML serialization."""
    d = {'nav_title': node.title}
    if node.path:
        d['path'] = node.path
    if node.page_order and node.page_order != 999:
        d['page_order'] = node.page_order
    if node.annotation:
        d['annotation'] = node.annotation
    if node.hidden:
        d['hidden'] = True
    if node.config_only:
        d['config_only'] = True
    if node.page_count:
        d['page_count'] = node.page_count
    if node.children:
        d['children'] = [tree_to_dict(c) for c in node.children]
    return d


def write_yaml_tree(tree, filepath):
    """Write tree as YAML file."""
    data = {
        '_meta': {
            'title': tree.title,
            'total_entries': tree.page_count,
            'generated_by': 'generate_ia_tree.py',
        },
        'sections': [tree_to_dict(c) for c in tree.children],
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=120)


# ============================================================
# Output: CSV files
# ============================================================

def write_current_csv(all_pages, filepath):
    """Write flat CSV of current pages."""
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'current_path', 'nav_title', 'article_title',
            'page_order', 'depth', 'parent_section', 'hidden', 'config_only'
        ])
        for page in sorted(all_pages, key=lambda p: p.path):
            parts = page.path.replace('_docs/_user_guide/', '').split('/')
            depth = len(parts) - 1
            parent = '/'.join(parts[:-1]) if len(parts) > 1 else ''
            writer.writerow([
                page.path, page.nav_title, page.article_title,
                page.page_order, depth, parent, page.hidden, page.config_only,
            ])


def write_migration_csv(migrations, filepath):
    """Write migration tracker CSV."""
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'nav_title', 'current_path', 'proposed_section',
            'proposed_path', 'change_type', 'annotation', 'status'
        ])
        for m in migrations:
            writer.writerow([
                m['nav_title'], m['current_path'], m['proposed_section'],
                m.get('proposed_path', ''), m['change_type'],
                m['annotation'], '',
            ])


# ============================================================
# Output: Mermaid diagrams
# ============================================================

def sanitize_mermaid_label(text):
    """Sanitize text for use in a Mermaid node label."""
    # Replace characters that break mermaid syntax
    text = text.replace('"', "'")
    text = text.replace('<', '')
    text = text.replace('>', '')
    text = text.replace('&', 'and')
    return text


def generate_mermaid(tree, max_depth=2):
    """Generate a Mermaid graph from a tree (top N levels)."""
    lines = []
    lines.append("```mermaid")
    lines.append("graph TD")

    counter = [0]

    def make_id():
        counter[0] += 1
        return f"N{counter[0]}"

    def add_node(node, parent_id, depth):
        if depth > max_depth:
            return
        if node.hidden:
            return

        nid = make_id()
        label = sanitize_mermaid_label(node.title)
        if node.page_count and node.children:
            label += f" ({node.page_count})"

        lines.append(f'    {nid}["{label}"]')
        if parent_id:
            lines.append(f'    {parent_id} --> {nid}')

        for child in node.children:
            if not child.hidden:
                add_node(child, nid, depth + 1)

    # Root node
    root_id = make_id()
    root_label = sanitize_mermaid_label(tree.title)
    if tree.page_count:
        root_label += f" ({tree.page_count})"
    lines.append(f'    {root_id}["{root_label}"]')

    for child in tree.children:
        if not child.hidden:
            add_node(child, root_id, 1)

    lines.append("```")
    return '\n'.join(lines)


def write_overview_md(tree, filepath, title="Current IA Overview"):
    """Write overview markdown with Mermaid diagram."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n")
        f.write(f"Total pages: {tree.page_count}\n\n")
        f.write(generate_mermaid(tree, max_depth=2))
        f.write('\n')


def write_comparison_md(current_tree, proposed_tree, migrations, filepath):
    """Write comparison markdown with Mermaid diagrams and stats."""
    lines = []
    lines.append("# IA Restructure: Current vs Proposed\n")

    # Change summary stats
    change_counts = {}
    for m in migrations:
        ct = m['change_type']
        change_counts[ct] = change_counts.get(ct, 0) + 1

    lines.append("## Change Summary\n")
    for ct in ['unchanged', 'moved', 'renamed', 'updated', 'merged', 'new', 'removed']:
        if ct in change_counts:
            lines.append(f"- **{ct.title()}**: {change_counts[ct]} pages")
    lines.append(f"- **Total tracked**: {len(migrations)} entries\n")

    # Top-level section comparison
    lines.append("## Top-Level Sections: Before and After\n")
    lines.append("### Current\n")
    for child in current_tree.children:
        if not child.hidden:
            lines.append(f"- **{child.title}** ({child.page_count} pages)")
    lines.append("")
    lines.append("### Proposed\n")
    for child in proposed_tree.children:
        lines.append(f"- **{child.title}** ({child.page_count} entries)")
    lines.append("")

    # Current IA diagram
    lines.append("## Current IA Diagram\n")
    lines.append(generate_mermaid(current_tree, max_depth=2))
    lines.append("")

    # Proposed IA diagram
    lines.append("## Proposed IA Diagram\n")
    lines.append(generate_mermaid(proposed_tree, max_depth=2))
    lines.append("")

    # Per-section detail for most-changed areas
    lines.append("## Section Detail: Most-Changed Areas\n")
    lines.append("The following sections have the most structural changes.\n")

    # Generate deeper diagrams for key proposed sections
    key_sections = ['Messaging', 'Channels', 'Data', 'Audience', 'Analytics', 'Administer']
    for section_name in key_sections:
        for child in proposed_tree.children:
            if child.title == section_name:
                lines.append(f"### Proposed: {section_name}\n")
                # Build a mini-tree for this section
                mini_tree = TreeNode(title=section_name, children=child.children)
                mini_tree.count_descendants()
                lines.append(generate_mermaid(mini_tree, max_depth=3))
                lines.append("")
                break

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


# ============================================================
# Output: Gap report
# ============================================================

def write_gap_report(unmatched_proposed, unmatched_current, migrations, filepath):
    """Write gap report for items needing review."""
    lines = []
    lines.append("# IA Migration Gap Report\n")
    lines.append("Items below need manual review.\n")

    # Section 1: Proposed entries with no match
    lines.append("## Proposed entries not matched to a current page\n")
    lines.append("These entries from `revised_ia.md` could not be matched to any existing page.")
    lines.append("They may be new articles (missing annotation), typos, or renamed pages.\n")

    if unmatched_proposed:
        for item in unmatched_proposed:
            lines.append(f"- **{item['nav_title']}** (in: {item['proposed_section']})")
            if item['annotation']:
                lines.append(f"  - Note: _{item['annotation']}_")
    else:
        lines.append("_None -- all proposed entries were matched or marked as new._\n")

    lines.append("")

    # Section 2: Current pages not in proposed
    lines.append("## Current pages not mentioned in proposed IA\n")
    lines.append('Per your note: "If child pages are not listed here, no changes are needed."')
    lines.append("These pages exist today but are not explicitly listed in `revised_ia.md`.")
    lines.append("They should remain with their parent section (which may itself be moving).\n")
    lines.append("Review to confirm none were accidentally omitted.\n")

    if unmatched_current:
        # Group by top-level section
        by_section: Dict[str, List[PageInfo]] = {}
        for page in unmatched_current:
            parts = page.path.replace('_docs/_user_guide/', '').split('/')
            section = parts[0] if parts else 'other'
            if section not in by_section:
                by_section[section] = []
            by_section[section].append(page)

        # Check which top-level sections are being moved/dissolved
        moved_sections = set()
        for m in migrations:
            if m['change_type'] in ('moved', 'updated', 'merged'):
                parts = m.get('current_path', '').replace('_docs/_user_guide/', '').split('/')
                if parts:
                    moved_sections.add(parts[0])

        for section in sorted(by_section.keys()):
            section_label = section.replace('_', ' ').replace('-', ' ').title()
            is_moving = section in moved_sections
            moving_note = " **(section is being restructured -- verify these pages)**" if is_moving else ""
            lines.append(f"### {section_label}{moving_note}\n")

            for page in sorted(by_section[section], key=lambda p: p.path):
                tags = []
                if page.hidden:
                    tags.append("hidden")
                if page.config_only:
                    tags.append("config_only")
                tag_str = f" ({', '.join(tags)})" if tags else ""
                lines.append(f"- `{page.path}`{tag_str}")
                lines.append(f"  - nav_title: {page.nav_title}")
            lines.append("")
    else:
        lines.append("_None -- all current pages were matched._\n")

    # Section 3: Pages matched to multiple candidates (potential mismatches)
    lines.append("## Potential mismatches to verify\n")
    lines.append("These entries were matched but may need verification (e.g., title matched")
    lines.append("but section context was ambiguous).\n")

    ambiguous = []
    for m in migrations:
        if m['current_path'] and m['change_type'] == 'moved':
            # Check if the proposed title differs significantly from nav_title
            ambiguous.append(m)

    if ambiguous:
        for m in ambiguous[:50]:  # Limit output
            lines.append(f"- **{m['nav_title']}**")
            lines.append(f"  - Current: `{m['current_path']}`")
            lines.append(f"  - Proposed: {m['proposed_section']}")
            if m['annotation']:
                lines.append(f"  - Note: _{m['annotation']}_")
    else:
        lines.append("_None._\n")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))


# ============================================================
# Main
# ============================================================

def main():
    # Determine repo root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)

    # Revised IA file path
    revised_ia_path = os.path.expanduser('~/revised_ia.md')
    if not os.path.isfile(revised_ia_path):
        revised_ia_path = os.path.join(repo_root, 'revised_ia.md')
    if not os.path.isfile(revised_ia_path):
        print("Warning: revised_ia.md not found. Only generating current IA outputs.")
        revised_ia_path = None

    # Output directory
    output_dir = os.path.join(repo_root, '_ia_audit')
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 60)
    print("IA Restructure Visualization Toolkit")
    print("=" * 60)

    # Step 1: Generate current IA
    print("\n[1/4] Walking _docs/_user_guide/ ...")
    current_tree, all_pages = walk_user_guide(repo_root)
    print(f"  Found {len(all_pages)} pages in {len(current_tree.children)} top-level sections")

    yaml_path = os.path.join(output_dir, 'ia_current.yaml')
    write_yaml_tree(current_tree, yaml_path)
    print(f"  Wrote {yaml_path}")

    csv_path = os.path.join(output_dir, 'ia_current.csv')
    write_current_csv(all_pages, csv_path)
    print(f"  Wrote {csv_path}")

    overview_path = os.path.join(output_dir, 'ia_overview_current.md')
    write_overview_md(current_tree, overview_path, "Current IA Overview")
    print(f"  Wrote {overview_path}")

    if not revised_ia_path:
        print("\nDone (current IA only).")
        return

    # Step 2: Parse proposed IA
    print(f"\n[2/4] Parsing {revised_ia_path} ...")
    proposed_tree = parse_revised_ia(revised_ia_path)
    proposed_flat = flatten_proposed(proposed_tree)
    print(f"  Found {len(proposed_flat)} entries in {len(proposed_tree.children)} top-level sections")

    proposed_yaml_path = os.path.join(output_dir, 'ia_proposed.yaml')
    write_yaml_tree(proposed_tree, proposed_yaml_path)
    print(f"  Wrote {proposed_yaml_path}")

    # Step 3: Match and diff
    print("\n[3/4] Matching proposed entries to current pages ...")
    migrations, unmatched_proposed, unmatched_current = match_proposed_to_current(
        proposed_tree, all_pages
    )

    matched_count = sum(1 for m in migrations if m['current_path'])
    new_count = sum(1 for m in migrations if m['change_type'] == 'new')
    print(f"  Matched: {matched_count} entries to current pages")
    print(f"  New pages: {new_count}")
    print(f"  Unmatched proposed: {len(unmatched_proposed)} (need review)")
    print(f"  Unmatched current: {len(unmatched_current)} pages (not in proposed)")

    # Step 4: Generate comparison artifacts
    print("\n[4/4] Generating comparison artifacts ...")

    migration_csv_path = os.path.join(output_dir, 'ia_migration.csv')
    write_migration_csv(migrations, migration_csv_path)
    print(f"  Wrote {migration_csv_path}")

    comparison_path = os.path.join(output_dir, 'ia_comparison.md')
    write_comparison_md(current_tree, proposed_tree, migrations, comparison_path)
    print(f"  Wrote {comparison_path}")

    gap_path = os.path.join(output_dir, 'gap_report.md')
    write_gap_report(unmatched_proposed, unmatched_current, migrations, gap_path)
    print(f"  Wrote {gap_path}")

    # Summary
    print("\n" + "=" * 60)
    print("Done! All outputs in _ia_audit/:")
    print("  ia_current.yaml        - Current IA tree")
    print("  ia_current.csv         - Flat page inventory")
    print("  ia_overview_current.md - Current IA Mermaid diagram")
    print("  ia_proposed.yaml       - Proposed IA tree")
    print("  ia_migration.csv       - Migration tracker")
    print("  ia_comparison.md       - Side-by-side comparison + diagrams")
    print("  gap_report.md          - Items needing review")
    print("=" * 60)

    # Quick change summary
    change_counts = {}
    for m in migrations:
        ct = m['change_type']
        change_counts[ct] = change_counts.get(ct, 0) + 1
    print("\nChange summary:")
    for ct in ['unchanged', 'moved', 'renamed', 'updated', 'merged', 'new', 'removed']:
        if ct in change_counts:
            print(f"  {ct:12s}: {change_counts[ct]}")
    print(f"  {'TOTAL':12s}: {len(migrations)}")


if __name__ == '__main__':
    main()

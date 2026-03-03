#!/usr/bin/env python3
"""
Auto-translate English Braze docs into all supported languages using Claude.

Usage:
    python auto_translate.py translate --changed-files changed_files.txt
    python auto_translate.py qc
    python auto_translate.py verify --max-attempts 3
    python auto_translate.py summary
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

def _get_anthropic_client():
    """Lazy-import Anthropic so commands like qc/summary work without the SDK."""
    try:
        from anthropic import Anthropic
    except ImportError:
        print("ERROR: Install the Anthropic SDK: pip install anthropic")
        sys.exit(1)
    return Anthropic()


LANGUAGES = {
    "fr":    {"config": "fr",    "dir": "fr_fr", "name": "French"},
    "ja":    {"config": "ja",    "dir": "ja",    "name": "Japanese"},
    "ko":    {"config": "ko",    "dir": "ko",    "name": "Korean"},
    "pt-br": {"config": "pt-br", "dir": "pt_br", "name": "Portuguese (Brazil)"},
    "es":    {"config": "es",    "dir": "es",    "name": "Spanish"},
    "de":    {"config": "de",    "dir": "de",    "name": "German"},
}

MODEL = os.environ.get("TRANSLATION_MODEL", "claude-opus-4-6")
MAX_TOKENS = int(os.environ.get("TRANSLATION_MAX_TOKENS", "65536"))
MAX_FILE_KB = int(os.environ.get("TRANSLATION_MAX_FILE_KB", "130"))
MAX_WORKERS = int(os.environ.get("TRANSLATION_WORKERS", "6"))
REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
RESULTS_FILE = REPO_ROOT / "translation_results.json"
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"
STYLEGUIDE_DIR = REPO_ROOT / "scripts" / "styleguides"
QC_RESULTS_FILE = REPO_ROOT / "qc_results.json"

NON_TRANSLATABLE_FM_KEYS = frozenset({
    "page_order", "layout", "page_type", "channel", "platform", "tool",
    "link", "image", "permalink", "hidden", "noindex", "config_only",
    "search_rank", "page_layout",
})

BRAZE_PRODUCT_NAMES = [
    "Content Cards", "Content Blocks", "Push Stories", "In-App Messages",
    "REST API", "News Feed", "Canvases", "Canvas", "Currents", "Campaigns",
    "Campaign", "Segments", "Segment", "Braze", "Liquid", "SDK", "API",
]

COMPLETENESS_MIN_RATIO = float(os.environ.get("QC_MIN_RATIO", "0.6"))
COMPLETENESS_MAX_RATIO = float(os.environ.get("QC_MAX_RATIO", "1.6"))
UNTRANSLATED_BLOCK_THRESHOLD = 200


def load_prompt():
    """Load the translation system prompt from scripts/translation_prompt.md."""
    return (REPO_ROOT / "scripts" / "translation_prompt.md").read_text()


def load_styleguide(lang_key):
    """Load the style guide for a language. Returns '' if not found."""
    sg_path = STYLEGUIDE_DIR / f"{lang_key}.md"
    if sg_path.exists():
        content = sg_path.read_text().strip()
        if content:
            return f"\n\n## Style guide for this language\n\n{content}"
    return ""


def load_glossary(lang_key):
    """Load the terminology glossary for a language. Returns {} if not found."""
    glossary_path = GLOSSARY_DIR / f"{lang_key}.json"
    if glossary_path.exists():
        return json.loads(glossary_path.read_text())
    return {}


def filter_glossary(glossary, text, max_terms=200):
    """Return only glossary entries whose English term appears in the text.

    Case-insensitive matching. Capped at max_terms to keep prompt size
    reasonable — prioritizes longer (more specific) terms first.
    """
    text_lower = text.lower()
    matches = {
        en: target
        for en, target in glossary.items()
        if en.lower() in text_lower
    }
    if len(matches) <= max_terms:
        return matches
    sorted_by_specificity = sorted(matches.items(), key=lambda x: -len(x[0]))
    return dict(sorted_by_specificity[:max_terms])


def format_glossary_for_prompt(glossary):
    """Format filtered glossary as a markdown table for the prompt."""
    if not glossary:
        return ""
    lines = [
        "\n## Approved terminology for this file\n",
        "Use these approved translations. If an English term maps to itself, keep it in English.\n",
        "| English | Translation |",
        "|---------|-------------|",
    ]
    for en, target in sorted(glossary.items(), key=lambda x: x[0].lower()):
        lines.append(f"| {en} | {target} |")
    return "\n".join(lines)


def strip_code_fences(text):
    """Strip wrapping code fences if the model adds them despite instructions."""
    stripped = text.strip()
    match = re.match(r"^```(?:\w*)\s*\n(.*)\n```\s*$", stripped, re.DOTALL)
    return match.group(1) if match else stripped


def call_claude(client, system_prompt, user_message, retries=3):
    """Call the Claude API via streaming with exponential-backoff retry."""
    for attempt in range(retries):
        try:
            text_chunks = []
            stop_reason = None
            with client.messages.stream(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                temperature=0,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            ) as stream:
                for text in stream.text_stream:
                    text_chunks.append(text)
                stop_reason = stream.get_final_message().stop_reason
            full_text = "".join(text_chunks)
            if stop_reason == "max_tokens":
                print(f"    WARNING: output truncated (hit {MAX_TOKENS} token limit). "
                      "Consider increasing TRANSLATION_MAX_TOKENS.")
            return strip_code_fences(full_text)
        except Exception as exc:
            if attempt < retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"    API error: {exc} — retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise


def translate_file(client, prompt, english_content, existing_translation, language_name, extra_context=""):
    """Translate a single English file into the target language."""
    system = prompt + extra_context

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## English source (translate this)\n\n{english_content}\n\n"

    if existing_translation:
        user_msg += (
            "## Existing translation (use as reference for terminology consistency)\n\n"
            f"{existing_translation}\n"
        )
    else:
        user_msg += "## Existing translation\nNone — this is a new file. Translate from scratch.\n"

    return call_claude(client, system, user_msg)


def fix_file(client, prompt, translated_content, build_error, language_name):
    """Send a translated file back to Claude to fix Jekyll build errors."""
    system = (
        prompt
        + "\n\n## ADDITIONAL CONTEXT: FIX MODE\n"
        "The file below failed the Jekyll build. Fix ONLY the structural or "
        "syntax issues that caused the failure. Preserve all translations. "
        "Return the complete fixed file and nothing else."
    )

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## Translated file (has build errors)\n\n{translated_content}\n\n"
    user_msg += f"## Jekyll build error output\n```\n{build_error}\n```\n"

    return call_claude(client, system, user_msg)


REVIEW_PROMPT = """\
You are a senior translation reviewer for Braze technical documentation. \
Your job is to review a machine-translated file and improve its quality.

Compare the translation against the English source and fix any issues:

1. **Accuracy**: Correct any mistranslations or meaning shifts.
2. **Naturalness**: Rephrase anything that reads as awkward or overly literal. \
The translation should read as if originally written in the target language.
3. **Terminology**: Ensure glossary terms are used correctly. Braze product names \
(Canvas, Currents, Content Cards, etc.) must stay in English.
4. **Preservation**: Verify that Liquid tags, code blocks, URLs, front matter keys, \
HTML tags, and markdown formatting are intact and unmodified.
5. **Style guide**: Follow all rules in the language-specific style guide appended \
below (gender conventions, register, terminology preferences, etc.).
6. **Consistency**: Ensure consistent terminology and tone throughout the file.

Return ONLY the improved translated file — no explanations, no code fences, \
no commentary. If the translation is already high quality, return it unchanged.\
"""


def review_file(client, english_content, translated_content, language_name, extra_context=""):
    """Second-pass review of a translation for quality improvement."""
    system = REVIEW_PROMPT + extra_context

    user_msg = f"## Target language\n{language_name}\n\n"
    user_msg += f"## English source\n\n{english_content}\n\n"
    user_msg += f"## Translation to review and improve\n\n{translated_content}\n"

    return call_claude(client, system, user_msg)



def translation_path(english_relative, lang_dir):
    """Map an English-relative path to its _lang/ counterpart."""
    return REPO_ROOT / "_lang" / lang_dir / english_relative


def load_results():
    if RESULTS_FILE.exists():
        return json.loads(RESULTS_FILE.read_text())
    return {"translated": [], "failed": []}


def save_results(results):
    RESULTS_FILE.write_text(json.dumps(results, indent=2))


# ---------------------------------------------------------------------------
# translate
# ---------------------------------------------------------------------------

def translate_one(client, prompt, fpath, relative, english_content,
                  lang_key, lang_info, glossary, styleguide):
    """Translate + review a single file into one language. Returns a result dict."""
    target = translation_path(relative, lang_info["dir"])
    existing = target.read_text() if target.exists() else None

    filtered = filter_glossary(glossary, english_content)
    glossary_section = format_glossary_for_prompt(filtered)
    extra_context = styleguide + glossary_section

    try:
        translated = translate_file(
            client, prompt, english_content, existing,
            lang_info["name"], extra_context,
        )
        translated = review_file(
            client, english_content, translated,
            lang_info["name"], extra_context,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(translated)
        return {
            "ok": True,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
        }
    except Exception as exc:
        return {
            "ok": False,
            "source": fpath,
            "target": str(target.relative_to(REPO_ROOT)),
            "lang": lang_key,
            "error": str(exc),
        }


def cmd_translate(args):
    """Translate changed English docs into every supported language."""
    changed_path = REPO_ROOT / args.changed_files
    if not changed_path.exists():
        print("No changed-files list found. Nothing to translate.")
        return

    all_files = [line.strip() for line in changed_path.read_text().splitlines() if line.strip()]
    md_files = [
        f for f in all_files
        if f.startswith("_docs/") and f.endswith(".md") and (REPO_ROOT / f).exists()
    ]

    if not md_files:
        print("No English .md files changed. Nothing to translate.")
        return

    skipped = []
    translatable = []
    for fpath in md_files:
        size_kb = (REPO_ROOT / fpath).stat().st_size / 1024
        if size_kb > MAX_FILE_KB:
            skipped.append({"source": fpath, "size_kb": round(size_kb)})
            print(f"  SKIP: {fpath} ({round(size_kb)} KB exceeds {MAX_FILE_KB} KB limit)")
        else:
            translatable.append(fpath)

    if not translatable:
        print("All changed files exceed the size limit. Nothing to translate.")
        results = load_results()
        results["skipped"] = skipped
        save_results(results)
        return

    total_tasks = len(translatable) * len(LANGUAGES)
    print(f"Translating {len(translatable)} file(s) into {len(LANGUAGES)} language(s) "
          f"({total_tasks} tasks, {MAX_WORKERS} workers)")
    if skipped:
        print(f"  ({len(skipped)} file(s) skipped — too large for single-pass translation)")
    print()

    client = _get_anthropic_client()
    prompt = load_prompt()
    results = load_results()
    results["skipped"] = results.get("skipped", []) + skipped
    glossaries = {lang: load_glossary(lang) for lang in LANGUAGES}
    styleguides = {lang: load_styleguide(lang) for lang in LANGUAGES}

    futures = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for fpath in translatable:
            relative = str(Path(fpath).relative_to("_docs"))
            english_content = (REPO_ROOT / fpath).read_text()

            for lang_key, lang_info in LANGUAGES.items():
                future = pool.submit(
                    translate_one, client, prompt, fpath, relative,
                    english_content, lang_key, lang_info,
                    glossaries[lang_key], styleguides[lang_key],
                )
                futures[future] = (relative, lang_info["name"])

        done_count = 0
        for future in as_completed(futures):
            done_count += 1
            relative, lang_name = futures[future]
            result = future.result()

            if result["ok"]:
                results["translated"].append({
                    "source": result["source"],
                    "target": result["target"],
                    "lang": result["lang"],
                })
                print(f"  [{done_count}/{total_tasks}] {relative} → {lang_name} done")
            else:
                results["failed"].append({
                    "source": result["source"],
                    "target": result["target"],
                    "lang": result["lang"],
                    "error": result["error"],
                })
                print(f"  [{done_count}/{total_tasks}] {relative} → {lang_name} "
                      f"FAILED ({result['error']})")

    save_results(results)
    ok = len(results["translated"])
    fail = len(results["failed"])
    print(f"\nTranslation complete: {ok} succeeded, {fail} failed")


# ---------------------------------------------------------------------------
# QC checks and repairs
# ---------------------------------------------------------------------------

def _extract_front_matter(content):
    """Extract YAML front matter and body from a markdown file."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1), content[match.end():]
    return None, content


def _extract_fm_block(fm_str, key):
    """Extract a full YAML block for a key (key line + indented continuation)."""
    lines = fm_str.split('\n')
    block_lines = []
    in_block = False
    for line in lines:
        if not in_block and re.match(rf'^{re.escape(key)}\s*:', line):
            in_block = True
            block_lines.append(line)
        elif in_block:
            if line and line[0] in (' ', '\t'):
                block_lines.append(line)
            else:
                break
    return '\n'.join(block_lines) if block_lines else None


def repair_front_matter(english_content, translated_content):
    """Ensure non-translatable front matter values match the English source."""
    en_fm, _ = _extract_front_matter(english_content)
    tr_fm, tr_body = _extract_front_matter(translated_content)

    if not en_fm or not tr_fm:
        return translated_content, []

    repairs = []
    repaired_fm = tr_fm

    for key in sorted(NON_TRANSLATABLE_FM_KEYS):
        en_block = _extract_fm_block(en_fm, key)
        tr_block = _extract_fm_block(repaired_fm, key)

        if en_block and tr_block and en_block != tr_block:
            repaired_fm = repaired_fm.replace(tr_block, en_block)
            repairs.append(f"front_matter:{key} — restored from English")
        elif en_block and not tr_block:
            repaired_fm = repaired_fm.rstrip() + '\n' + en_block
            repairs.append(f"front_matter:{key} — re-added missing key")

    if repairs:
        translated_content = f"---\n{repaired_fm}\n---\n{tr_body}"

    return translated_content, repairs


def _extract_code_blocks(content):
    """Extract fenced code blocks with positions."""
    pattern = re.compile(r'(^```[^\n]*\n)(.*?)(^```\s*$)', re.MULTILINE | re.DOTALL)
    return [
        (m.start(), m.end(), m.group(0), m.group(2))
        for m in pattern.finditer(content)
    ]


def repair_code_blocks(english_content, translated_content):
    """Replace translated code block contents with English originals."""
    en_blocks = _extract_code_blocks(english_content)
    tr_blocks = _extract_code_blocks(translated_content)

    if not en_blocks:
        return translated_content, []

    if len(en_blocks) != len(tr_blocks):
        return translated_content, [
            f"code_blocks — count mismatch (English: {len(en_blocks)}, "
            f"translated: {len(tr_blocks)}); skipped auto-repair"
        ]

    repairs = []
    repaired = translated_content
    for i in range(len(en_blocks) - 1, -1, -1):
        en_full = en_blocks[i][2]
        tr_full = tr_blocks[i][2]
        if en_full != tr_full:
            repaired = (
                repaired[:tr_blocks[i][0]] + en_full + repaired[tr_blocks[i][1]:]
            )
            repairs.append(f"code_block[{i}] — restored English content")

    return repaired, repairs


def _extract_md_link_urls(content):
    """Extract markdown link/image URLs in order."""
    return re.findall(r'\[(?:[^\]]*)\]\(([^)]+)\)', content)


def repair_urls(english_content, translated_content):
    """Ensure markdown link URLs match the English source."""
    en_urls = _extract_md_link_urls(english_content)
    tr_urls = _extract_md_link_urls(translated_content)

    if not en_urls:
        return translated_content, []

    if len(en_urls) != len(tr_urls):
        return translated_content, [
            f"urls — count mismatch (English: {len(en_urls)}, "
            f"translated: {len(tr_urls)}); skipped auto-repair"
        ]

    repairs = []
    repaired = translated_content
    for i, (en_url, tr_url) in enumerate(zip(en_urls, tr_urls)):
        if en_url != tr_url:
            repaired = repaired.replace(f"]({tr_url})", f"]({en_url})", 1)
            repairs.append(f"url[{i}] — restored '{en_url}'")

    return repaired, repairs


def check_liquid_tags(english_content, translated_content):
    """Check that Liquid tags are preserved between source and translation."""
    warnings = []

    en_exprs = set(re.findall(r'\{\{.*?\}\}', english_content))
    tr_exprs = set(re.findall(r'\{\{.*?\}\}', translated_content))
    for expr in sorted(en_exprs - tr_exprs):
        warnings.append(f"liquid_expr — missing: {expr}")

    en_tags = re.findall(r'\{%[-\s]*(.*?)[-\s]*%\}', english_content)
    tr_tags = re.findall(r'\{%[-\s]*(.*?)[-\s]*%\}', translated_content)

    def tag_name(t):
        return t.strip().split()[0] if t.strip() else ""

    en_counts = Counter(tag_name(t) for t in en_tags)
    tr_counts = Counter(tag_name(t) for t in tr_tags)

    for tag, count in en_counts.items():
        tr_count = tr_counts.get(tag, 0)
        if tr_count < count:
            warnings.append(
                f"liquid_tag — '{tag}' appears {count}x in English but "
                f"{tr_count}x in translation"
            )

    return warnings


def check_glossary_compliance(english_content, translated_content, lang_key):
    """Check that Braze product names are kept in English."""
    _, en_body = _extract_front_matter(english_content)
    _, tr_body = _extract_front_matter(translated_content)

    code_re = re.compile(r'```.*?```', re.DOTALL)
    en_clean = code_re.sub('', en_body)
    tr_clean = code_re.sub('', tr_body)

    warnings = []
    for name in BRAZE_PRODUCT_NAMES:
        en_count = en_clean.lower().count(name.lower())
        if en_count < 2:
            continue
        tr_count = tr_clean.lower().count(name.lower())
        if tr_count < en_count * 0.5:
            warnings.append(
                f"glossary — '{name}' appears {en_count}x in English but "
                f"only {tr_count}x in translation"
            )

    return warnings


def check_completeness(english_content, translated_content):
    """Flag translations whose length deviates significantly from the source."""
    en_len = len(english_content)
    if en_len == 0:
        return []

    ratio = len(translated_content) / en_len
    if ratio < COMPLETENESS_MIN_RATIO:
        return [
            f"completeness — translation is {ratio:.0%} of English length "
            f"(min threshold: {COMPLETENESS_MIN_RATIO:.0%}); possible truncation"
        ]
    if ratio > COMPLETENESS_MAX_RATIO:
        return [
            f"completeness — translation is {ratio:.0%} of English length "
            f"(max threshold: {COMPLETENESS_MAX_RATIO:.0%}); possible hallucination"
        ]
    return []


def check_untranslated(english_content, translated_content):
    """Detect large blocks of English prose left verbatim in the translation."""
    _, en_body = _extract_front_matter(english_content)
    _, tr_body = _extract_front_matter(translated_content)

    strip_patterns = [
        (re.compile(r'```.*?```', re.DOTALL), ''),
        (re.compile(r'\{[%{].*?[%}]\}'), ''),
        (re.compile(r'`[^`]+`'), ''),
        (re.compile(r'\]\([^)]+\)'), ''),
        (re.compile(r'https?://\S+'), ''),
    ]

    en_clean = en_body
    tr_clean = tr_body
    for pattern, repl in strip_patterns:
        en_clean = pattern.sub(repl, en_clean)
        tr_clean = pattern.sub(repl, tr_clean)

    warnings = []
    for para in re.split(r'\n\s*\n', en_clean):
        text = para.strip()
        if len(text) < UNTRANSLATED_BLOCK_THRESHOLD:
            continue
        if text in tr_clean:
            preview = text[:80].replace('\n', ' ')
            warnings.append(
                f"untranslated — {len(text)}-char English block found verbatim: "
                f"\"{preview}...\""
            )

    return warnings


def qc_check_file(english_path, translated_path, lang_key):
    """Run all QC checks on one file pair. Auto-repairs are written back."""
    english_content = Path(english_path).read_text()
    translated_content = Path(translated_path).read_text()

    findings = {
        "file": str(translated_path),
        "lang": lang_key,
        "repairs": [],
        "warnings": [],
    }

    translated_content, fm_repairs = repair_front_matter(
        english_content, translated_content
    )
    findings["repairs"].extend(fm_repairs)

    translated_content, cb_repairs = repair_code_blocks(
        english_content, translated_content
    )
    findings["repairs"].extend(cb_repairs)

    translated_content, url_repairs = repair_urls(
        english_content, translated_content
    )
    findings["repairs"].extend(url_repairs)

    if findings["repairs"]:
        Path(translated_path).write_text(translated_content)

    findings["warnings"].extend(
        check_liquid_tags(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_glossary_compliance(english_content, translated_content, lang_key)
    )
    findings["warnings"].extend(
        check_completeness(english_content, translated_content)
    )
    findings["warnings"].extend(
        check_untranslated(english_content, translated_content)
    )

    return findings


def cmd_qc(_args):
    """Run deterministic quality checks on all translated files."""
    results = load_results()
    translated = results.get("translated", [])

    if not translated:
        print("No translations to QC.")
        return

    print(f"Running QC checks on {len(translated)} translated file(s)...\n")

    all_findings = []
    repair_count = 0
    warning_count = 0

    for entry in translated:
        source_path = REPO_ROOT / entry["source"]
        target_path = REPO_ROOT / entry["target"]

        if not source_path.exists() or not target_path.exists():
            print(f"  Skipping {entry['target']} — file not found")
            continue

        findings = qc_check_file(source_path, target_path, entry["lang"])

        n_repairs = len(findings["repairs"])
        n_warnings = len(findings["warnings"])
        repair_count += n_repairs
        warning_count += n_warnings

        if n_repairs or n_warnings:
            all_findings.append(findings)
            parts = []
            if n_repairs:
                parts.append(f"{n_repairs} repaired")
            if n_warnings:
                parts.append(f"{n_warnings} warnings")
            print(f"  {entry['target']} — {', '.join(parts)}")
        else:
            print(f"  {entry['target']} — passed")

    qc_data = {
        "total_files": len(translated),
        "files_with_issues": len(all_findings),
        "total_repairs": repair_count,
        "total_warnings": warning_count,
        "findings": all_findings,
    }
    QC_RESULTS_FILE.write_text(json.dumps(qc_data, indent=2))

    print(f"\nQC complete: {len(translated)} files checked, "
          f"{repair_count} auto-repairs, {warning_count} warnings")


# ---------------------------------------------------------------------------
# verify  (build + fix loop)
# ---------------------------------------------------------------------------

def jekyll_build(lang_config_key):
    """Run a Jekyll build for one language; return (success, output)."""
    config = f"./_config.yml,./_lang/_config_{lang_config_key}.yml"
    result = subprocess.run(
        ["bundle", "exec", "jekyll", "build", "--config", config],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    return result.returncode == 0, result.stderr + "\n" + result.stdout


def extract_error_files(error_output, lang_dir):
    """Pull file paths from Jekyll error output that belong to a language dir."""
    pattern = rf"_lang/{re.escape(lang_dir)}/\S+\.md"
    return list(set(re.findall(pattern, error_output)))


def cmd_verify(args):
    """Build each translated language; auto-fix errors up to N times."""
    client = _get_anthropic_client()
    prompt = load_prompt()
    results = load_results()

    translated_langs = {t["lang"] for t in results.get("translated", [])}
    if not translated_langs:
        print("No translations to verify.")
        return

    build_results = {"passed": [], "fixed": [], "failed": []}

    for lang_key in sorted(translated_langs):
        lang_info = LANGUAGES[lang_key]

        for attempt in range(1, args.max_attempts + 1):
            print(f"\nBuilding {lang_info['name']} (attempt {attempt}/{args.max_attempts})...")
            ok, output = jekyll_build(lang_info["config"])

            if ok:
                bucket = "fixed" if attempt > 1 else "passed"
                build_results[bucket].append(lang_key)
                label = "fixed and passed" if attempt > 1 else "passed"
                print(f"  {lang_info['name']} build {label}")
                break

            print(f"  {lang_info['name']} build failed")

            if attempt == args.max_attempts:
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": output[-3000:],
                })
                print(f"  {lang_info['name']} still failing after {args.max_attempts} attempts")
                break

            error_files = extract_error_files(output, lang_info["dir"])
            if not error_files:
                print("  Could not identify failing file(s) from build output")
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": output[-3000:],
                })
                break

            for efile in error_files:
                epath = REPO_ROOT / efile
                if not epath.exists():
                    continue
                print(f"  Fixing {efile}...")
                try:
                    content = epath.read_text()
                    fixed = fix_file(client, prompt, content, output[-3000:], lang_info["name"])
                    epath.write_text(fixed)
                except Exception as exc:
                    print(f"  Fix attempt failed: {exc}")

    results["build_results"] = build_results
    save_results(results)

    print(f"\nBuild verification complete:")
    print(f"  Passed:        {len(build_results['passed'])}")
    print(f"  Fixed & passed: {len(build_results['fixed'])}")
    print(f"  Failed:        {len(build_results['failed'])}")


# ---------------------------------------------------------------------------
# summary  (generate PR body)
# ---------------------------------------------------------------------------

def cmd_summary(_args):
    """Write a markdown PR body from the translation results."""
    results = load_results()
    translated = results.get("translated", [])
    failed = results.get("failed", [])
    skipped = results.get("skipped", [])
    build = results.get("build_results", {})

    lines = ["## Auto-translation summary\n"]

    source_files = sorted(set(t["source"] for t in translated))
    lines.append(f"**Source files translated:** {len(source_files)}  ")
    lines.append(f"**Translation files created/updated:** {len(translated)}  ")
    if failed:
        lines.append(f"**Translation API failures:** {len(failed)}  ")
    if skipped:
        lines.append(f"**Files skipped (too large):** {len(skipped)}  ")
    lines.append("")

    if skipped:
        lines.append("### Skipped files (exceed size limit)\n")
        lines.append("These files are too large for single-pass LLM translation and "
                      "need manual translation or a chunked approach.\n")
        for item in sorted(skipped, key=lambda x: -x["size_kb"]):
            lines.append(f"- `{item['source']}` ({item['size_kb']} KB)")
        lines.append("")

    # Build verification table
    if build:
        lines.append("### Build verification\n")
        lines.append("| Language | Status |")
        lines.append("|----------|--------|")
        for lang in build.get("passed", []):
            lines.append(f"| {LANGUAGES[lang]['name']} | Passed |")
        for lang in build.get("fixed", []):
            lines.append(f"| {LANGUAGES[lang]['name']} | Fixed and passed |")
        for item in build.get("failed", []):
            lines.append(f"| {LANGUAGES[item['lang']]['name']} | Needs manual review |")
        lines.append("")

    # Failed builds — expandable details
    build_failures = build.get("failed", [])
    if build_failures:
        lines.append("### Build failures requiring review\n")
        for item in build_failures:
            name = LANGUAGES[item["lang"]]["name"]
            lines.append(f"<details><summary>{name}</summary>\n")
            lines.append(f"```\n{item.get('error', 'No error details available')}\n```\n")
            lines.append("</details>\n")

    # QC checks
    if QC_RESULTS_FILE.exists():
        qc = json.loads(QC_RESULTS_FILE.read_text())
        total_repairs = qc.get("total_repairs", 0)
        total_warnings = qc.get("total_warnings", 0)

        if total_repairs or total_warnings:
            lines.append("### Quality checks\n")

            lang_stats = {}
            for f in qc.get("findings", []):
                lang = f["lang"]
                if lang not in lang_stats:
                    lang_stats[lang] = {"repairs": 0, "warnings": 0, "details": []}
                lang_stats[lang]["repairs"] += len(f.get("repairs", []))
                lang_stats[lang]["warnings"] += len(f.get("warnings", []))
                for r in f.get("repairs", []):
                    lang_stats[lang]["details"].append(f"[repaired] {r}")
                for w in f.get("warnings", []):
                    lang_stats[lang]["details"].append(f"[warning] {w}")

            lines.append("| Language | Repairs | Warnings | Status |")
            lines.append("|----------|---------|----------|--------|")
            for lang_key in sorted(LANGUAGES):
                if lang_key not in lang_stats:
                    lines.append(
                        f"| {LANGUAGES[lang_key]['name']} | 0 | 0 | Passed |"
                    )
                    continue
                s = lang_stats[lang_key]
                if s["warnings"]:
                    status = "Needs review"
                elif s["repairs"]:
                    status = "Auto-repaired"
                else:
                    status = "Passed"
                lines.append(
                    f"| {LANGUAGES[lang_key]['name']} | {s['repairs']} | "
                    f"{s['warnings']} | {status} |"
                )
            lines.append("")

            for lang_key in sorted(lang_stats):
                s = lang_stats[lang_key]
                if not s["details"]:
                    continue
                name = LANGUAGES[lang_key]["name"]
                count = len(s["details"])
                lines.append(
                    f"<details><summary>{name} — {count} finding(s)</summary>\n"
                )
                for d in s["details"]:
                    lines.append(f"- {d}")
                lines.append("\n</details>\n")

    # Translated files grouped by source
    if translated:
        lines.append("### Files translated\n")
        by_source = {}
        for t in translated:
            by_source.setdefault(t["source"], []).append(t["lang"])
        for source in sorted(by_source):
            lang_names = ", ".join(
                LANGUAGES[l]["name"] for l in sorted(by_source[source])
            )
            lines.append(f"- `{source}` → {lang_names}")
        lines.append("")

    body = "\n".join(lines)
    (REPO_ROOT / "translation_pr_body.md").write_text(body)
    print(body)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Auto-translate Braze documentation")
    sub = parser.add_subparsers(dest="command", required=True)

    tp = sub.add_parser("translate", help="Translate changed English files")
    tp.add_argument(
        "--changed-files", default="changed_files.txt",
        help="Path to a newline-delimited list of changed English doc paths",
    )
    tp.set_defaults(func=cmd_translate)

    vp = sub.add_parser("verify", help="Build each language and auto-fix errors")
    vp.add_argument(
        "--max-attempts", type=int, default=3,
        help="Maximum fix-and-rebuild cycles per language (default: 3)",
    )
    vp.set_defaults(func=cmd_verify)

    qp = sub.add_parser("qc", help="Run deterministic quality checks on translations")
    qp.set_defaults(func=cmd_qc)

    sp = sub.add_parser("summary", help="Generate a PR body from translation results")
    sp.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Auto-translate English Braze docs into all supported languages using Claude.

Usage:
    python auto_translate.py translate --changed-files changed_files.txt
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
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: Install the Anthropic SDK: pip install anthropic")
    sys.exit(1)


LANGUAGES = {
    "fr":    {"config": "fr",    "dir": "fr_fr", "name": "French"},
    "ja":    {"config": "ja",    "dir": "ja",    "name": "Japanese"},
    "ko":    {"config": "ko",    "dir": "ko",    "name": "Korean"},
    "pt-br": {"config": "pt-br", "dir": "pt_br", "name": "Portuguese (Brazil)"},
    "es":    {"config": "es",    "dir": "es",    "name": "Spanish"},
    "de":    {"config": "de",    "dir": "de",    "name": "German"},
}

MODEL = os.environ.get("TRANSLATION_MODEL", "claude-opus-4-6")
MAX_TOKENS = 16384
MAX_WORKERS = int(os.environ.get("TRANSLATION_WORKERS", "6"))
REPO_ROOT = Path(os.environ.get("GITHUB_WORKSPACE", Path.cwd()))
RESULTS_FILE = REPO_ROOT / "translation_results.json"
GLOSSARY_DIR = REPO_ROOT / "scripts" / "glossaries"


def load_prompt():
    """Load the translation system prompt from scripts/translation_prompt.md."""
    return (REPO_ROOT / "scripts" / "translation_prompt.md").read_text()


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
    """Call the Claude API with exponential-backoff retry."""
    for attempt in range(retries):
        try:
            response = client.messages.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                temperature=0,
                system=system_prompt,
                messages=[{"role": "user", "content": user_message}],
            )
            return strip_code_fences(response.content[0].text)
        except Exception as exc:
            if attempt < retries - 1:
                wait = 2 ** (attempt + 1)
                print(f"    API error: {exc} — retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise


def translate_file(client, prompt, english_content, existing_translation, language_name, glossary_section=""):
    """Translate a single English file into the target language."""
    system = prompt + glossary_section

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
5. **Gender**: In Portuguese, "Braze" is feminine (a Braze, da Braze, para a Braze — \
never o Braze, do Braze, para o Braze). In French, Spanish, and German, follow the \
existing article conventions for the brand name.
6. **Consistency**: Ensure consistent terminology and tone throughout the file.

Return ONLY the improved translated file — no explanations, no code fences, \
no commentary. If the translation is already high quality, return it unchanged.\
"""


def review_file(client, english_content, translated_content, language_name, glossary_section=""):
    """Second-pass review of a translation for quality improvement."""
    system = REVIEW_PROMPT + glossary_section

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
                  lang_key, lang_info, glossary):
    """Translate + review a single file into one language. Returns a result dict."""
    target = translation_path(relative, lang_info["dir"])
    existing = target.read_text() if target.exists() else None

    filtered = filter_glossary(glossary, english_content)
    glossary_section = format_glossary_for_prompt(filtered)

    try:
        translated = translate_file(
            client, prompt, english_content, existing,
            lang_info["name"], glossary_section,
        )
        translated = review_file(
            client, english_content, translated,
            lang_info["name"], glossary_section,
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

    total_tasks = len(md_files) * len(LANGUAGES)
    print(f"Translating {len(md_files)} file(s) into {len(LANGUAGES)} language(s) "
          f"({total_tasks} tasks, {MAX_WORKERS} workers)\n")

    client = Anthropic()
    prompt = load_prompt()
    results = load_results()
    glossaries = {lang: load_glossary(lang) for lang in LANGUAGES}

    futures = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        for fpath in md_files:
            relative = str(Path(fpath).relative_to("_docs"))
            english_content = (REPO_ROOT / fpath).read_text()

            for lang_key, lang_info in LANGUAGES.items():
                future = pool.submit(
                    translate_one, client, prompt, fpath, relative,
                    english_content, lang_key, lang_info,
                    glossaries[lang_key],
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


def extract_error_lines(output):
    """Extract only error-relevant lines from Jekyll build output.

    Full build output can be huge; we filter to lines containing error
    indicators or file paths so the auto-fix prompt gets useful context
    instead of truncated asset-pipeline noise.
    """
    error_keywords = re.compile(
        r"error|Error|ERROR|warning|Liquid|Invalid|SyntaxError|"
        r"undefined|Could not|not found|YAML|frontmatter|"
        r"_lang/\S+\.md",
        re.IGNORECASE,
    )
    lines = [line for line in output.splitlines() if error_keywords.search(line)]
    extracted = "\n".join(lines)
    if extracted:
        return extracted[:8000]
    return output[-3000:]


def extract_error_files(error_output, lang_dir):
    """Pull file paths from Jekyll error output that belong to a language dir."""
    pattern = rf"_lang/{re.escape(lang_dir)}/\S+\.md"
    return list(set(re.findall(pattern, error_output)))


def cmd_verify(args):
    """Build each translated language; auto-fix errors up to N times."""
    client = Anthropic()
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

            error_context = extract_error_lines(output)

            if attempt == args.max_attempts:
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": error_context,
                })
                print(f"  {lang_info['name']} still failing after {args.max_attempts} attempts")
                break

            error_files = extract_error_files(output, lang_info["dir"])
            if not error_files:
                print("  Could not identify failing file(s) from build output")
                build_results["failed"].append({
                    "lang": lang_key,
                    "error": error_context,
                })
                break

            for efile in error_files:
                epath = REPO_ROOT / efile
                if not epath.exists():
                    continue
                print(f"  Fixing {efile}...")
                try:
                    content = epath.read_text()
                    fixed = fix_file(client, prompt, content, error_context, lang_info["name"])
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
    build = results.get("build_results", {})

    lines = ["## Auto-translation summary\n"]

    source_files = sorted(set(t["source"] for t in translated))
    lines.append(f"**Source files translated:** {len(source_files)}  ")
    lines.append(f"**Translation files created/updated:** {len(translated)}  ")
    if failed:
        lines.append(f"**Translation API failures:** {len(failed)}  ")
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

    sp = sub.add_parser("summary", help="Generate a PR body from translation results")
    sp.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

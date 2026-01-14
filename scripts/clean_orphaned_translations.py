#!/usr/bin/env python3

# This script finds and deletes all files that exist in one or more '_lang' 
# subdirectories that don't exist in the primary '_docs' directory. If no 
# argument is given, all languages are processed. To see the full list of 
# options, append '--help' to the script.
#
# Usage:  ./scripts/clean_orphaned_translations.py [LANGUAGE]

import os
import shutil
import sys
from pathlib import Path

# Base directories
docs_dir = Path("_docs")
lang_dirs = {
    "ja": Path("_lang/ja"),
    "de": Path("_lang/de"),
    "es": Path("_lang/es"),
    "fr": Path("_lang/fr_fr"),
    "ko": Path("_lang/ko"),
    "pt-br": Path("_lang/pt_br")
}

def get_all_files(directory):
    """Get all files in a directory recursively."""
    all_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), directory)
            all_files.append(rel_path)

    return all_files

help_text = f"""This script finds and deletes all files that exist in one or more '_lang' subdirectories
that don't exist in the primary '_docs' directory. It can be run against a single language or all languages.

USAGE:
  ./scripts/clean_orphaned_translations.py [LANGUAGE]

OPTIONS:
  [LANGUAGE]         Process the given language. If none, process all. Available languages:
                       {', '.join(lang_dirs.keys())}
  -h, --help         Show this help message"""

def main():
    # Get all files in the _docs directory
    docs_files = set(get_all_files(docs_dir))

    # Initialize a dictionary to track orphaned files by section for each language
    language_summaries = {}

    # Check if a specific language was specified via command line
    target_language = None
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ('--help', '-h'):
            print(help_text)
            sys.exit(0)
        else:
            target_language = arg
            if target_language not in lang_dirs:
                print(f"Error: Language '{target_language}' not supported. Available options: {', '.join(lang_dirs.keys())}")
                sys.exit(1)
            print(f"Processing only the {target_language} language directory.")
    else:
        print(f"Processing all language directories.")
 

    # Filter language directories if target_language is specified
    languages_to_process = {target_language: lang_dirs[target_language]} if target_language else lang_dirs

    # Set up log file
    LOG_PATH = Path("scripts/temp/cleaned_lang_files.log")
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Process languages and write per-file logs
    with LOG_PATH.open("w", encoding="utf-8") as log:
        for lang, lang_dir in languages_to_process.items():
            if not os.path.exists(lang_dir):
                print(f"Language directory {lang_dir} does not exist. Skipping.")
                continue

            lang_files = get_all_files(lang_dir)
            orphaned_files = []
            section_counts = {}

            for lang_file in lang_files:
                # Skip files in _includes directory
                if lang_file.startswith("_includes/"):
                    continue

                # Check if the file exists in _docs
                if lang_file not in docs_files:
                    orphaned_files.append(lang_file)
                    file_path = os.path.join(lang_dir, lang_file)
                    log.write(f"Orphaned file found: {file_path}\n")
                    os.remove(file_path)
                    log.write(f"Deleted: {file_path}\n")

                    # Track the section of the file
                    section = lang_file.split("/")[0] if "/" in lang_file else "root"
                    section_counts[section] = section_counts.get(section, 0) + 1

                    # Remove empty directories
                    dir_path = os.path.dirname(file_path)
                    while dir_path != lang_dir:
                        try:
                            if len(os.listdir(dir_path)) == 0:
                                os.rmdir(dir_path)
                                log.write(f"Removed empty directory: {dir_path}\n")
                            else:
                                break
                        except:
                            break
                        dir_path = os.path.dirname(dir_path)

            language_summaries[lang] = {
                "total": len(orphaned_files),
                "sections": section_counts
            }

    # Print summary by language
    print("\n===== SUMMARY OF CLEANED FILES =====")
    for lang, summary in language_summaries.items():
        print(f"\n{lang.upper()} - Total: {summary['total']} files cleaned")
        if summary['sections']:
            print("Files cleaned by section:")
            for section, count in sorted(summary['sections'].items(), key=lambda x: x[1], reverse=True):
                print(f"  - {section}: {count}")
        else:
            print("No files cleaned")

    print("\nTo see the full list of changes, go to:")
    print(f"  {LOG_PATH}")


if __name__ == "__main__":
    main()

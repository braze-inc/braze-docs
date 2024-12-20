#!/usr/bin/env python3

# Script for updating old links. Requires 'update_redirect_list.py'.

import os
import json
import re
import subprocess

# Get project root
ROOT_DIR = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()
DICT_FILE = os.path.join(ROOT_DIR, 'redirects.json')


def get_user_path():
    path = input("Please provide a file or directory path: ").strip()
    while not path:
        path = input("Please provide a file or directory path: ").strip()
    return path


def gather_files(path):
    # If directory, walk it recursively
    if os.path.isdir(path):
        files = []
        for root, dirs, filenames in os.walk(path):
            for fn in filenames:
                # You can add filters here if needed, e.g., only .md files
                files.append(os.path.join(root, fn))
        return files
    elif os.path.isfile(path):
        return [path]
    else:
        print("The provided path is neither a file nor a directory.")
        exit(1)


def load_redirects(json_file):
    if not os.path.exists(json_file):
        print(f"Error: '{json_file}' not found.")
        exit(1)
    with open(json_file, 'r') as f:
        data_dict = json.load(f)
    return data_dict


def replace_urls_in_file(filepath, redirects):
    # redirects: a list of tuples (new_url, [old_url1, old_url2, ...])
    # Each entry: { "new_url": ..., "old_urls": [...] }
    # We replace {{site.baseurl}}old_url with {{site.baseurl}}new_url for all old_urls
    if not os.path.isfile(filepath):
        return 0

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original_content = content

    # For each entry (new_url, old_urls):
    # if an entry has multiple old_urls, we must replace all old_urls with the single new_url.
    total_replacements = 0
    for entry_key, data in redirects.items():
        new_url = data["new_url"]
        old_urls = data["old_urls"]
        # Replace all occurrences of each old_url
        for old in old_urls:
            # Construct pattern to match ({{site.baseurl}}old_url)
            pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(old) + r"\)"
            count_before = len(re.findall(pattern, content))
            if count_before > 0:
                content = re.sub(pattern, "(" + "{{site.baseurl}}" + new_url + ")", content)
                total_replacements += count_before

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return total_replacements


def main():
    user_path = get_user_path()
    files = gather_files(user_path)
    redirects = load_redirects(DICT_FILE)

    # transforms redirects into a list/dict we already have.
    # no changes needed if we trust the "redirects.json" format as per previous steps.

    # Process each file
    total_global_replacements = 0
    for fp in files:
        replacements = replace_urls_in_file(fp, redirects)
        if replacements > 0:
            print(f"In file '{fp}', made {replacements} replacements.")
        total_global_replacements += replacements

    print(f"Total replacements made across all files: {total_global_replacements}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# Uses 'assets/js/broken_redirect_list.js' to determine the newest version of
# a link, then updates all 'OLD' links with the 'NEW' link for the given
# page or directory.
#
# Requires: 'update_redirect_list.py'
#
# Usage: ./bdocs ulinks [FILE|DIRECTORY]
#
# Options:
#   FILE              Updates old links in a single file.
#   DIRECTORY         Recursively updates old links in a directory.

import os
import json
import re
import sys

# Get project root
PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
REDIRECT_MATCHES = os.environ.get('REDIRECT_MATCHES')


def update_old_links(filepath, redirects):
    # redirects: { key: { "new_url": str, "old_urls": [str, ...] }, ... }
    # Replace ({{site.baseurl}}old_url) with ({{site.baseurl}}new_url)
    if not os.path.isfile(filepath):
        return 0

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original_content = content
    total_replacements = 0

    for entry_key, data in redirects.items():
        new_url = data["new_url"]
        old_urls = data["old_urls"]

        # Replace {{site.baseurl}} references
        for old in old_urls:
            if "#" in old:
                pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(old) + r"\)"
            else:
                old_noslash = old.rstrip('/')
                pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(old_noslash) + r"/?\)"
            count_before = len(re.findall(pattern, content))
            if count_before > 0:
                content = re.sub(pattern, "(" + "{{site.baseurl}}" + new_url + ")", content)
                total_replacements += count_before

        # Replace YAML front matter links (link: /docs...)
        for old in old_urls:
            if "#" in old:
                pattern = r'(link:\s*)' + re.escape('/docs' + old)
            else:
                old_noslash = old.rstrip('/')
                pattern = r'(link:\s*)' + re.escape('/docs' + old_noslash) + r'/?'
            count_before = len(re.findall(pattern, content))
            if count_before > 0:
                content = re.sub(pattern, r'\1' + '/docs' + new_url, content)
                total_replacements += count_before

    # If content changed, write the file back out
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return total_replacements


def get_redirect_matches(json_file):
    if not os.path.exists(json_file):
        print(f"Error: '{json_file}' not found.")
        exit(1)
    with open(json_file, 'r') as f:
        data_dict = json.load(f)
    return data_dict


# TODO: Move this to bdocs directly for easier reuse.
def process_directory(directory, redirects):
    total_global_replacements = 0
    for root, dirs, files in os.walk(directory):
        for fn in files:
            file_path = os.path.join(root, fn)
            replacements = update_old_links(file_path, redirects)
            if replacements > 0:
                # Print relative path from the given directory
                relative_path = os.path.relpath(file_path, start=directory)
                print(f"In '{relative_path}', made {replacements} replacements.")
            total_global_replacements += replacements
    return total_global_replacements


# TODO: Move this to bdocs directly for easier reuse.
def process_single_file(filepath, redirects):
    replacements = update_old_links(filepath, redirects)
    if replacements > 0:
        # When given a single file, just print the filename
        print(f"In '{os.path.basename(filepath)}', made {replacements} replacements.")
    return replacements


def main(path):
    redirects = get_redirect_matches(REDIRECT_MATCHES)

    if os.path.isdir(path):
        total_replacements = process_directory(path, redirects)
        print(f"Total replacements made across all files: {total_replacements}")
    elif os.path.isfile(path):
        total_replacements = process_single_file(path, redirects)
        print(f"Total replacements made: {total_replacements}")
    else:
        print(f"Invalid path: {path}. Please provide a valid directory or file.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_or_file>")
        sys.exit(1)
    user_path = sys.argv[1]
    user_path = os.path.abspath(user_path)
    main(user_path)

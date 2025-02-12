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

PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
REDIRECT_MATCHES = os.environ.get('REDIRECT_MATCHES')


# Load redirect data from the JSON file generated by './utils/merge_redirect_descendants.py'.
def get_redirect_matches(json_file):
    if not os.path.exists(json_file):
        print(f"Error: '{json_file}' not found.")
        sys.exit(1)
    with open(json_file, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    return data_dict


# Update all old links found in a given file
def update_old_links(filepath, redirects):
    if not os.path.isfile(filepath):
        return 0

    # Read file content
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original_content = content
    total_replacements = 0

    # Loop through each redirect entry
    for entry_key, data in redirects.items():
        new_url = adjust_url(data["new_url"])
        old_urls = data["old_urls"]

        # 1) Replace '{{site.baseurl}}' style links
        for old in old_urls:
            # If there's an anchor in old (e.g., #something), match exactly '({{site.baseurl}}/old#...)'.
            if "#" in old:
                pattern = (
                        r"\("
                        + re.escape("{{site.baseurl}}")
                        + re.escape(old)
                        + r"\)"
                )
            else:
                # Otherwise, match '({{site.baseurl}}/old_url/)' with an optional trailing slash.
                no_trailing_slash = old.rstrip('/')
                pattern = (
                        r"\("
                        + re.escape("{{site.baseurl}}")
                        + re.escape(no_trailing_slash)
                        + r"/?\)"
                )

            # Find all matches of the old pattern.
            found = len(re.findall(pattern, content))
            # Replace them with the new baseurl link if any found.
            if found > 0:
                content = re.sub(pattern, f"({{{{site.baseurl}}}}{new_url})", content)
                total_replacements += found

        # 2) Replace 'link:' references in YAML with updated '/docs' link.
        for old in old_urls:
            no_trailing_slash = old.rstrip('/')
            # If old has '#', build a pattern including that anchor.
            if "#" in old:
                # Capture leading spaces + 'link: /docs' + 'old_url' + optional slash/spaces + end of line.
                pattern = re.compile(
                    r"^([ \t]*)link:\s*/docs"
                    + re.escape(old)
                    + r"/?[ \t]*$",
                    flags=re.MULTILINE
                )
            else:
                # Otherwise, capture same but without the anchor.
                pattern = re.compile(
                    r"^([ \t]*)link:\s*/docs"
                    + re.escape(no_trailing_slash)
                    + r"/?[ \t]*$",
                    flags=re.MULTILINE
                )

            # Count matches of the old pattern.
            found = len(re.findall(pattern, content))
            # Replace them with the new link if any found.
            if found > 0:
                content = re.sub(pattern, rf"\1link: /docs{new_url}", content)
                total_replacements += found

    # If file content changed, write the updated content back.
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return total_replacements


# Adjust a URL by removing trailing slashes if it contains '#' or '?'
def adjust_url(url):
    if '#' in url or '?' in url:
        return url.rstrip('/')
    return url


# Function to recursively process all files in a given directory.
def process_directory(directory, redirects):
    total_global_replacements = 0
    for root, dirs, files in os.walk(directory):
        for fn in files:
            file_path = os.path.join(root, fn)
            replacements = update_old_links(file_path, redirects)
            if replacements > 0:
                # Convert the file path to a relative path from the current directory
                rel_path = os.path.relpath(file_path, start=os.getcwd())
                # Prepend './'
                print(f"Made {replacements} replacements in {rel_path}")
            total_global_replacements += replacements
    return total_global_replacements


# Function to process a single file.
def process_single_file(filepath, redirects):
    replacements = update_old_links(filepath, redirects)
    if replacements > 0:
        # Convert the file path to a relative path from the current directory
        rel_path = os.path.relpath(filepath, start=os.getcwd())
        # Prepend './'
        print(f"Made {replacements} replacements in {rel_path}")
    return replacements


# Main function handling file or directory updates
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
    user_path = os.path.abspath(sys.argv[1])
    main(user_path)

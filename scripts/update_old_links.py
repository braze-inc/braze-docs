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


def adjust_url(url):
    # If URL contains '#' or '?', remove any trailing slash if present
    if '#' in url or '?' in url:
        return url.rstrip('/')
    return url


def update_old_links(filepath, redirects):
    if not os.path.isfile(filepath):
        return 0

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original_content = content
    total_replacements = 0

    for entry_key, data in redirects.items():
        new_url = adjust_url(data["new_url"])
        old_urls = data["old_urls"]

        #
        # 1) Replace '{{site.baseurl}}' links in page
        #
        for old in old_urls:
            if "#" in old:
                pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(old) + r"\)"
            else:
                no_trailing_slash = old.rstrip('/')
                pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(no_trailing_slash) + r"/?\)"

            found = len(re.findall(pattern, content))
            if found > 0:
                content = re.sub(pattern, f"({{{{site.baseurl}}}}{new_url})", content)
                total_replacements += found

        #
        # 2) Replace 'link:' references in YAML with /docs + new_url
        #
        for old in old_urls:
            no_trailing_slash = old.rstrip('/')
            if "#" in old:
                # If there's a '#' in old, build the pattern with it.
                pattern = re.compile(
                    r"^([ \t]*)link:\s*/docs"  # Group 1: leading spaces + "link: /docs"
                    + re.escape(old)  # The old URL with '#'
                    + r"/?[ \t]*$",  # Optional slash, optional spaces, line end
                    flags=re.MULTILINE
                )
            else:
                # If no '#', use the no_trailing_slash version
                pattern = re.compile(
                    r"^([ \t]*)link:\s*/docs"  # Group 1: leading spaces + "link: /docs"
                    + re.escape(no_trailing_slash)
                    + r"/?[ \t]*$",  # Optional slash, optional spaces, line end
                    flags=re.MULTILINE
                )

            found = len(re.findall(pattern, content))
            if found > 0:
                # Replace with:
                #   \1 => the leading spaces captured by group 1
                #   then "link: /docs{new_url}"
                content = re.sub(pattern, rf"\1link: /docs{new_url}", content)
                total_replacements += found

    # If content changed, write the file back out
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return total_replacements


def get_redirect_matches(json_file):
    if not os.path.exists(json_file):
        print(f"Error: '{json_file}' not found.")
        sys.exit(1)
    with open(json_file, 'r', encoding='utf-8') as f:
        data_dict = json.load(f)
    return data_dict


def process_directory(directory, redirects):
    total_global_replacements = 0
    for root, dirs, files in os.walk(directory):
        for fn in files:
            file_path = os.path.join(root, fn)
            replacements = update_old_links(file_path, redirects)
            if replacements > 0:
                rel_path = os.path.relpath(file_path, start=directory)
                print(f"In '{rel_path}', made {replacements} replacements.")
            total_global_replacements += replacements
    return total_global_replacements


def process_single_file(filepath, redirects):
    replacements = update_old_links(filepath, redirects)
    if replacements > 0:
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
    user_path = os.path.abspath(sys.argv[1])
    main(user_path)

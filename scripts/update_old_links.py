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

    # 1) site.baseurl replacements in entire file
    for entry_key, data in redirects.items():
        new_url = adjust_url(data["new_url"])
        old_urls = data["old_urls"]

        for old in old_urls:
            if "#" in old:
                pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(old) + r"\)"
            else:
                old_noslash = old.rstrip('/')
                pattern = r"\(" + re.escape("{{site.baseurl}}") + re.escape(old_noslash) + r"/?\)"

            found = len(re.findall(pattern, content))
            if found > 0:
                content = re.sub(pattern, f"({{site.baseurl}}{new_url})", content)
                total_replacements += found

    # 2) YAML front matter lines: between first and second ---
    lines = content.split('\n')
    in_front_matter = False
    dash_count = 0

    for i in range(len(lines)):
        line = lines[i].rstrip('\r')

        if line.strip() == "---":
            dash_count += 1
            if dash_count == 2:
                break
            in_front_matter = True
            continue

        if in_front_matter and "link: /docs" in line:
            for entry_key, data in redirects.items():
                new_url = adjust_url(data["new_url"])
                old_urls = data["old_urls"]

                for old in old_urls:
                    # Skip anchor-based old URLs for YAML
                    if "#" in old:
                        continue

                    old_noslash = old.rstrip('/')
                    pattern = (
                            r'(^[ \t]*link:\s*)/docs'
                            + re.escape(old_noslash)
                            + r'(/|$)'
                    )

                    # If we detect the old URL in line, remove everything from ': /docs...'
                    # and replace with ': /docs' + the adjusted new_url
                    if re.search(pattern, lines[i]):
                        lines[i] = re.sub(
                            r':\s*/docs.*',
                            f': /docs{new_url}',
                            lines[i]
                        )
                        total_replacements += 1
                        break

    new_content = "\n".join(lines)
    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

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

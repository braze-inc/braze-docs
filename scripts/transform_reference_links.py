#!/usr/bin/env python3

# Transforms Markdown reference links to in-line links. Created because
# reference links cannot be placed inside Liquid {% tab %} tags.
#
# For more information, see:
# https://www.braze.com/docs/contributing/content_management/cross_referencing/
# 
# Usage: ./bdocs tlinks [FILE|DIRECTORY]
#
# Options:
#   FILE              Transform reference links in a single file.
#   DIRECTORY         Recursively transform reference links in a directory.

import os
import sys
import re


# Create a dictionary with all reference links at the bottom of the file.
def create_link_dictionary(file_path):
    link_dict = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Reverse the lines to start from the last line
    lines.reverse()

    # The pattern for reference links
    pattern = re.compile(r'\[(.*?)]:\s*(.*)')

    for line in lines:
        line = line.strip()

        match = pattern.match(line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            link_dict[key] = value
        elif line and not line.startswith('['):
            break

    return link_dict


# Use the dictionary to find and replace all references with the full link.
def replace_links(file_path, link_dict):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    dict_keys = list(link_dict.keys())

    for line in lines:
        for key in dict_keys:
            line = line.replace(f'][{key}]', f']({link_dict[key]})')

        updated_lines.append(line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)


# TODO: Move this to bdocs directly for easier reuse.
# Recursively convert links for all Markdown files in given directory.
def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                link_dict = create_link_dictionary(file_path)
                replace_links(file_path, link_dict)


# If arg == directory, convert links for all Markdown files in that directory.
# If arg == file, convert links for that Markdown file only.
def main(path):
    if os.path.isdir(path):
        process_directory(path)
    elif os.path.isfile(path) and path.endswith('.md'):
        link_dict = create_link_dictionary(path)
        replace_links(path, link_dict)
    else:
        print(f"Invalid path: {path}. Please provide a valid directory or a markdown file.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./bdocs ulinks <directory_or_file>")
    else:
        given_path = sys.argv[1]
        # Normalize the path to ensure correct traversal
        given_path = os.path.abspath(given_path)
        main(given_path)

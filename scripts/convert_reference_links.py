# This script converts Markdown reference links to in-line links.
# Created because reference links cannot be placed inside Liquid a {% tab %}.
#
# For more information, see:
# https://www.braze.com/docs/contributing/content_management/cross_referencing/
# 
# Usage: ./convert_reference_links [directory|file]

import os
import sys
import re


# For the current file, create a dictionary of reference links, where
# NUM is the key and STRING is the value in [NUM]: STRING
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


# Use the link dictionary to find and replace all reference links in the file.
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


def main(path):
    # If 'path' == directory:
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    link_dict = create_link_dictionary(file_path)
                    replace_links(file_path, link_dict)

    # If 'path' == Markdown file:
    elif os.path.isfile(path) and path.endswith('.md'):
        link_dict = create_link_dictionary(path)
        replace_links(path, link_dict)

    # If 'path' is invalid:
    else:
        print(f"Invalid path: {path}. \
              Please provide a valid directory or a markdown file.")


if __name__ == "__main__":
    given_path = sys.argv[1]
    main(given_path)

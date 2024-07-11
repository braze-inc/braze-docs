# This script converts Markdown reference links to in-line links.
# Created because reference links cannot be placed inside Liquid a {% tab %}.
#
# For more information, see:
# https://www.braze.com/docs/contributing/content_management/cross_referencing/
# 
# Usage: ./convert_reference_links [directory|file]


# TODO: Make sure it also converts reference-style links for image tags as well. It currently does not.

import os
import sys

def create_link_dictionary(file_path):
    link_dict = {}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Reverse the lines to start from the last line
    lines.reverse()

    for line in lines:
        line = line.strip()
        
        if line.startswith('[') and (line.find(']') != -1) and (('{{site.baseurl}}' in line) or ('http' in line) or ('www' in line)):
            start_index = line.find('[') + 1
            end_index = line.find(']')
            key = line[start_index:end_index]

            value = line[end_index + 2:].strip()
            link_dict[key] = value
        elif line and not line.startswith('['):
            break

    return link_dict

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

def process_file(file_path):
    link_dict = create_link_dictionary(file_path)
    replace_links(file_path, link_dict)

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 convert_reference_links.py [path/to/file/or/directory]")
        sys.exit(1)

    path = sys.argv[1]

    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        sys.exit(1)

    if os.path.isfile(path):
        process_file(path)
    elif os.path.isdir(path):
        process_directory(path)
    else:
        print(f"Error: Path '{path}' is neither a file nor a directory.")
        sys.exit(1)

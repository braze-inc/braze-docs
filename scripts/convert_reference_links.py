# This script converts Markdown reference links to in-line links.
# Created because reference links cannot be placed inside Liquid a {% tab %}.
#
# For more information, see:
# https://www.braze.com/docs/contributing/content_management/cross_referencing/
# 
# Usage: ./convert_reference_links [directory|file]


# TODO: Script can run recursively against explicitly hard-coded directory. 
#       Update the script to take arguments so you can specify a single file or directory.

import os

# Retrieve the environment variable
project_root = os.getenv('PROJECT_ROOT')

# Verify the environment variable is passed correctly
print("PROJECT_ROOT:", project_root)

def create_link_dictionary(file_path):
    link_dict = {}
    
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Reverse the lines to start from the last line
    lines.reverse()

    for line in lines:
        line = line.strip()
        
        if line.startswith('[') and (line.find(']') != -1) and (('{{site.baseurl}}' in line) or ('http' in line) or ('www' in line) or ('{% image_buster' in line)):
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

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                link_dict = create_link_dictionary(file_path)
                replace_links(file_path, link_dict)

# Define the directory to process
directory_path = os.path.join(project_root, '_docs', '_api')

# Process all files in the directory
process_directory(directory_path)

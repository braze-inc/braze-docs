# THIS IS THE OLD VERSION.
# This script can only run against a single file (defined in 'file_path').
# It can not take arguments, nor run recursively.
# 
# Usage: ./convert_reference_links [directory|file]

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

# Always run against PROJECT_ROOT/_docs/_api/api_limits.md
file_path = os.path.join(project_root, '_docs', '_api', 'basics.md')

# Create the link dictionary
link_dict = create_link_dictionary(file_path)

# Replace the links in the markdown file
replace_links(file_path, link_dict)

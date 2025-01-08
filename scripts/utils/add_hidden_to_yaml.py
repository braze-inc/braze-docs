#!/usr/bin/env python3

# This script can be used to add the 'hidden: true' parameter
# to all files in the current directory and its subdirectories.
# This is helpful if you need to hide an entire section from
# the left-side navigation.
#
# NOTE: You need to place this script directly in the directory
# you want to run it against. It doesn't take paths as arguments.

import os
import re

def process_yaml_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Track if we're in YAML front matter
    in_front_matter = False
    start_index = None
    end_index = None
    hidden_exists = False

    for i, line in enumerate(lines):
        # Check for start of YAML front matter
        if line.strip() == "---" and not in_front_matter:
            in_front_matter = True
            start_index = i
            continue

        # Check for end of YAML front matter
        if line.strip() == "---" and in_front_matter:
            end_index = i
            break

        # Check if 'hidden: true' already exists
        if in_front_matter and re.match(r'^hidden:\s*true', line.strip()):
            hidden_exists = True
            break

    # If 'hidden: true' doesn't exist, add it before the end ---
    if in_front_matter and not hidden_exists and end_index is not None:
        lines[end_index] = "hidden: true\n" + lines[end_index]

        # Write the updated content back to the file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(lines)

        print(f"Updated file: {filepath}")

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.yml', '.yaml')):  # Adjust extensions as needed
                filepath = os.path.join(root, file)
                process_yaml_file(filepath)

if __name__ == "__main__":
    current_directory = os.getcwd()
    process_directory(current_directory)

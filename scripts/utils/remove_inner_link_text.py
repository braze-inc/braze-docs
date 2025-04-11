#!/usr/bin/env python3

# Removes inner text from '{{site.baseurl}}' links. (Should mainly be run 
# through 'bdocs' as a sub-command).
#
# Usage: ./scripts/utils/remove_inner_link_text.py [FILE|DIRECTORY]
#
# Options:
#   FILE         Process a single file.
#   DIRECTORY    Process all files recursively.

import os
import re
import sys

def remove_inner_link_text(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    original_content = content

    # Remove inner text from links starting with '{{site.baseurl}}'.
    pattern_alt = re.compile(r'(\(\s*\{\{site\.baseurl\}\}[^)]+?)\s+"[^"]*"\s*(\))')
    content = re.sub(pattern_alt, r'\1\2', content)

    # Remove extra spaces before the closing parenthesis.
    content = re.sub(r'\s+\)', ')', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == '__main__':
    path = os.path.abspath(sys.argv[1])
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                remove_inner_link_text(os.path.join(root, file))
    else:
        remove_inner_link_text(path)

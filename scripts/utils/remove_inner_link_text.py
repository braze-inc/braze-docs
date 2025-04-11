#!/usr/bin/env python3

# Removes inner text from '{{site.baseurl}}' links.
#
# Usage: ./scripts/utils/remove_inner_link_text.py [FILE]
#
# Options:
#   FILE         Process a single file.

import os
import re

# If {{site.baseurl}} links has inner text, remove it.
def remove_inner_link_text(filepath):

    # Recursively check files.
    if not os.path.isfile(filepath):
        return 0

    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original_content = content

    # Remove the inner link text.
    pattern_alt = re.compile(r'(\(\s*\{\{site\.baseurl\}\}[^)]+?)\s+"[^"]*"\s*(\))')
    content = re.sub(pattern_alt, r'\1\2', content)

    # Remove extra spaces before the closing ')'.
    content = re.sub(r'\s+\)', ')', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return 0

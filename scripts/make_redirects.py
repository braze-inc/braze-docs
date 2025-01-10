#!/usr/bin/env python3

# DESCRIPTION
#
# Usage: ./bdocs credirects

import re
import subprocess

# Paths (assuming these are sourced or set elsewhere in your environment)
redirect_file = "./assets/js/broken_redirect_list.js"
project_root = "./"  # Adjust to your actual root if needed

# Using Git, get the list of files that have been renamed.
def get_changed_files():
    cmd = f"git diff -M --summary develop HEAD -- {project_root}_docs"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    # Filter lines that start with "rename" or " rename"
    changed_files = [line.strip() for line in result.stdout.splitlines() if line.startswith("rename") or line.startswith(" rename")]
    
    return changed_files

def create_redirect(line):
    # Strip "rename " and the trailing percentage
    line = line.split(" ", 1)[1]
    line = re.sub(r"\s\(\d+%\)$", "", line)

    # Extract the `{old => new}` part.
    brace_match = re.search(r"{([^}]+) => ([^}]+)}", line)
    if not brace_match:
        return None
    
    old_in_braces = brace_match.group(1)
    new_in_braces = brace_match.group(2)
    
    # Grab everything before and after the braces
    before_braces = line.split("{")[0]
    after_braces  = line.split("}")[1]  # everything after the closing brace

    # Build the leading path (before the '{')
    leading_path = before_braces.strip()
    
    # The trailing part after the '}' (e.g. "/catalogs.md")
    # (strip leading slash, if any)
    trailing_path = after_braces.strip()
    
    # Combine to form full old & new
    # old_in_braces, new_in_braces might still have .md in them
    # trailing_path might also have .md

    old_full_path = f"/{leading_path}{old_in_braces}{trailing_path}"
    new_full_path = f"/{leading_path}{new_in_braces}{trailing_path}"
    
    # Clean underscores and strip .md
    old_full_path = old_full_path.replace("/_", "/").replace(".md", "")
    new_full_path = new_full_path.replace("/_", "/").replace(".md", "")

    # Return the final redirect line
    return f"validurls['{old_full_path}'] = '{new_full_path}';"


def main():
    # Fetch changed files
    changed_files = get_changed_files()
    
    # Process each line and write to redirect file
    with open(redirect_file, 'a') as f:
        for line in changed_files:
            formatted_redirect = create_redirect(line)
            if formatted_redirect:
                f.write(formatted_redirect + "\n")
    
    print("Redirects added successfully!")

if __name__ == "__main__":
    main()

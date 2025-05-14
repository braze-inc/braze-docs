#!/usr/bin/env python3

# DESCRIPTION
#
# Usage: ./bdocs mredirects

import os
import re
import subprocess

# Global variables
PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
REDIRECT_FILE = os.environ.get('REDIRECT_FILE')

# Using Git, get the list of files that have been renamed.
def get_changed_files():
    cmd = f"git diff -M --summary develop HEAD -- {PROJECT_ROOT}_docs"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    changed_files = [line.strip() for line in result.stdout.splitlines() if line.startswith("rename") or line.startswith(" rename")]

    if not changed_files:
        print("Error: Git can't find any renamed files in this branch, so no redirects were created.")
        return []
    
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
    
    old_full_path = f"/{leading_path}{old_in_braces}{trailing_path}"
    new_full_path = f"/{leading_path}{new_in_braces}{trailing_path}"
    
    old_full_path = old_full_path.replace("/_", "/").replace(".md", "")
    new_full_path = new_full_path.replace("/_", "/").replace(".md", "")

    print("Redirects created successfully!")
    return f"validurls['{old_full_path}'] = '{new_full_path}';"


def main():
    changed_files = get_changed_files()
    
    with open(REDIRECT_FILE, 'a') as f:
        for line in changed_files:
            formatted_redirect = create_redirect(line)
            if formatted_redirect:
                f.write(formatted_redirect + "\n")

if __name__ == "__main__":
    main()

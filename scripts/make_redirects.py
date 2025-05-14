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
    cmd = f"git diff -M --summary develop HEAD -- {os.path.join(PROJECT_ROOT, '_docs')}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    changed_files = [line.strip() for line in result.stdout.splitlines() if line.startswith("rename") or line.startswith(" rename")]

    if not changed_files:
        print("Error: Git can't find any renamed files committed in this branch.\nNote that redirects are only created for renamed files if they're 'committed', not just 'added' to the branch.")
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
    
    # Combine to form full old & new
    # old_in_braces, new_in_braces might still have .md in them
    # trailing_path might also have .md
    old_full_path = f"/{leading_path}{old_in_braces}{trailing_path}"
    new_full_path = f"/{leading_path}{new_in_braces}{trailing_path}"
    
    # Clean underscores and strip .md
    old_full_path = old_full_path.replace("/_", "/").replace(".md", "")
    new_full_path = new_full_path.replace("/_", "/").replace(".md", "")

    print("Redirects created successfully!")
    return f"validurls['{old_full_path}'] = '{new_full_path}';"


# Remove duplicate lines while preserving blank lines
def remove_duplicates(lines):
    processed = []
    unique_lines = []
    blank_lines = 0

    for line in lines:
        if line.strip() == "":
            # count consecutive blank lines but don't append yet
            blank_lines += 1
            continue

        # if we just skipped one or more blanks, add exactly one
        if blank_lines:
            if not unique_lines or unique_lines[-1].strip() != "":
                unique_lines.append("\n")
            blank_lines = 0

        # keep only the first occurrence of each non-blank line
        if line not in processed:
            processed.append(line)
            unique_lines.append(line)

    return unique_lines


def main():
    changed_files = get_changed_files()
    
    with open(REDIRECT_FILE, 'r+') as f:
        lines = f.readlines()

        # Remove any existing placeholder comment
        lines = [l for l in lines if l.strip() != "// validurls['OLD'] = 'NEW';"]

        # Append any new redirects
        for line in changed_files:
            redirect_line = create_redirect(line)
            if redirect_line:
                lines.append(redirect_line + "\n")

        # Add blank line, placeholder, blank line at the end
        lines.append("\n// validurls['OLD'] = 'NEW';\n")

        # Remove duplicates
        unique_lines = remove_duplicates(lines)

        # Rewrite file
        f.seek(0)
        f.truncate()
        f.writelines(unique_lines)

if __name__ == "__main__":
    main()

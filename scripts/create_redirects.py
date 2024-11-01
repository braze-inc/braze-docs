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
    return [line.strip() for line in result.stdout.splitlines() if line.startswith("rename") or line.startswith(" rename")]

def create_redirect(line):
    # Remove everything up to and including the first space, but keep the initial underscore
    line = line.split(" ", 1)[1]

    # Remove any trailing `(NUM%)` from the line
    line = re.sub(r"\s\(\d+%\)$", "", line)

    # Get the relative paths for the old and new filenames
    line_separator = line.split("{")[0].strip()

    # Check if this is a directory rename (no `.md` in `{old => }/new.md` portion)
    if re.search(r"{([^{}]+) => }/[^\s]+\.md", line):
        # Directory-only rename handling
        old_path_part, new_filename = re.search(r"{([^{}]+) => }/(.+)", line).groups()
        
        # Construct the paths for old and new locations
        old_path = f"/{line_separator}{old_path_part}/{new_filename}"
        new_path = f"/{line_separator}{new_filename}"
    elif re.search(r"{(.+?) => (.+?)}", line):
        # Standard file rename handling with `{old => new}` pattern
        unformatted_old_path, unformatted_new_path = re.search(r"{(.+?) => (.+?)}", line).groups()
        old_path = f"/{line_separator}{unformatted_old_path}"
        new_path = f"/{line_separator}{unformatted_new_path}"
    else:
        return None

    # Remove leading underscores and .md extensions, and format paths
    old_path = old_path.replace("/_", "/").replace(".md", "")
    new_path = new_path.replace("/_", "/").replace(".md", "")

    # Convert paths to the redirect syntax: validurls['OLD'] = 'NEW';
    redirect = f"validurls['{old_path}'] = '{new_path}';"

    return redirect

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

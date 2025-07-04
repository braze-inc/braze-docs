#!/usr/bin/env python3

# Uses 'git diff' to track renamed files or directories, then creates redirects 
# in 'assets/js/broken_redirect_list.js'. Note that redirects are only created 
# for renamed files if they're 'committed', not just 'added' to the branch.
#
# Usage: ./bdocs mredirects

import os
import re
import subprocess

# Global variables
PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
REDIRECT_FILE = os.environ.get('REDIRECT_FILE')
LOG_PATH = os.path.join(PROJECT_ROOT, "scripts", "temp", "mredirect_logs")

# Uses Git to return a list of renamed files and directories in this format:
#   files:       rename _docs/_contributing/{bdocs.md => test.md} (100%)
#   directories: rename _docs/_contributing/{yaml => jekyll}/metadata.md (100%)
def get_renamed_files():
    cmd = f"git diff -M --summary develop HEAD -- {os.path.join(PROJECT_ROOT, '_docs')}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    changed_files = [line.strip() for line in result.stdout.splitlines() if line.startswith("rename") or line.startswith(" rename")]

    if not changed_files:
        print("Error: Git can't find any renamed files committed in this branch.\nNote that redirects are only created for renamed files if they're 'committed', not just 'added' to the branch.")
        return []
    
    return changed_files


# Adds unmatched lines to ./scripts/temp/mredirect_logs.
def log_unmatched(line):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a") as log_file:
        log_file.write(line + "\n")


# Creates redirects by cleaning up the list generated by 'get_renamed_files'.
def create_redirect(line):
    original_line = line.strip()

    # Remove 'rename ' and trailing percentage like '(98%)'
    line = line.split(" ", 1)[1]
    line = re.sub(r"\s\(\d+%\)$", "", line)

    # Extract {old => new}
    regex_group = re.search(r"{([^}]+) => ([^}]*)}", line)
    if not regex_group:
        log_unmatched(original_line)
        return None
    
    subgroup_old = regex_group.group(1)
    subgroup_new = regex_group.group(2)
    
    # Path before { }
    path = line.split("{")[0].strip()

    # Portion after }
    renamed_dir_file = line.split("}")[1].strip()
    
    # Build URLs
    url_old = f"/{path}{subgroup_old}{renamed_dir_file}".replace("/_", "/").replace(".md", "")
    url_new = f"/{path}{subgroup_new}{renamed_dir_file}".replace("/_", "/").replace(".md", "")

    return f"validurls['{url_old}'] = '{url_new}';"


# Remove duplicate lines while preserving single blank lines
def remove_duplicates(lines):
    unique_lines = []
    double_blank = False

    for line in lines:
        if line.strip() == "":          
            if not double_blank:         
                unique_lines.append(line)
                double_blank = True
        else:                           
            double_blank = False
            if line not in unique_lines:
                unique_lines.append(line)

    return unique_lines


def main():
    # Reset the log file each run
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "w"):
        pass

    changed_files = get_renamed_files()
    if not changed_files:
        return

    placeholder_comment = "// validurls['OLD'] = 'NEW';"
    redirects_created = False

    with open(REDIRECT_FILE, "r+") as f:
        original_lines = f.readlines()
        lines = [l for l in original_lines if l.strip() != placeholder_comment]

        # Build redirects, skip duplicates
        for line in changed_files:
            redirect_line = create_redirect(line)
            if redirect_line and (redirect_line + "\n") not in lines:
                lines.append(redirect_line + "\n")
                redirects_created = True

        if not redirects_created:
            print(
                "Error: Git can't find any renamed files committed in this branch.\n"
                "Note that redirects are only created for renamed files if they're "
                "'committed', not just 'added' to the branch."
            )
            return

        # Add placeholder and tidy file
        lines.append(f"\n{placeholder_comment}\n")
        unique_lines = remove_duplicates(lines)

        # Only write if content actually changed
        if unique_lines != original_lines:
            f.seek(0)
            f.truncate()
            f.writelines(unique_lines)
            print("Redirects created successfully!")
            if os.path.getsize(LOG_PATH) > 0:
                with open(LOG_PATH) as log_file:
                    print("\nHowever, some redirects will need to be created manually:\n")
                    print(log_file.read().rstrip())


if __name__ == "__main__":
    main()

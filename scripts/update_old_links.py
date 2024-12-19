#!/usr/bin/env python3

import os
import re
import subprocess

# Get the project root directory using git
def get_project_root():
    try:
        project_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], universal_newlines=True).strip()
        return project_root
    except subprocess.CalledProcessError:
        print("Error: Unable to determine the project root. Make sure you are inside a git repository.")
        exit(1)

# File paths (update these as necessary)
PROJECT_ROOT = get_project_root()  # Get the root of the project using Git
TEST_PAGE_PATH = os.path.join(PROJECT_ROOT, 'test_page.md')
REDIRECT_FILE = os.path.join(PROJECT_ROOT, 'assets/js/broken_redirect_list.js')  # Corrected path to the redirect file

# Function to read the redirect file and create a mapping of old and new links
def load_redirects():
    redirects = {}
    try:
        with open(REDIRECT_FILE, 'r') as file:
            for line in file:
                # Match the pattern and exclude the /docs part
                match = re.match(r"validurls\['/([^']+)' \] = '/([^']+)';", line.strip())
                if match:
                    old_url = match.group(1)  # This is the part after '/docs'
                    new_url = match.group(2)  # This is the new URL after '/docs'
                    redirects[old_url] = new_url
    except FileNotFoundError:
        print(f"Error: The redirect file '{REDIRECT_FILE}' was not found.")
        exit(1)
    return redirects

# Function to replace old links with new links in a single file
def replace_links_in_file(file_path, redirects):
    print(f"Found file: {file_path}")
    with open(file_path, 'r') as file:
        content = file.read()

    links_replaced = False  # Flag to track if any links are replaced

    # Only replace links matching the pattern
    for old_url, new_url in redirects.items():
        search_pattern = r"\{\{site.baseurl\}\}/" + re.escape(old_url)  # Construct the search pattern
        replace_pattern = r"{{site.baseurl}}/" + new_url  # Construct the replacement pattern
        
        # Check if the search pattern is found
        if re.search(search_pattern, content):
            print(f"Replacing {search_pattern} with {replace_pattern}")
            content = re.sub(search_pattern, replace_pattern, content)  # Replace all occurrences
            links_replaced = True  # Set the flag to True if any link is replaced

    # If changes were made, write the updated content back to the file
    if links_replaced:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Links updated successfully in {file_path}")
    else:
        print("No old links found.")

# Main function to run the script
def main():
    # Load redirects from the JavaScript file
    print("Loading redirects...")
    redirects = load_redirects()

    # Process the test page
    print(f"Processing file: {TEST_PAGE_PATH}")
    replace_links_in_file(TEST_PAGE_PATH, redirects)

if __name__ == '__main__':
    main()

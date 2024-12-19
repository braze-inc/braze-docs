#!/usr/bin/env python3

import os
import subprocess
import re

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
REDIRECT_FILE = os.path.join(PROJECT_ROOT, 'assets/js/broken_redirect_list.js')  # Correct path to the redirect file
TEMP_FILE = os.path.join(PROJECT_ROOT, 'temp')  # Path to the file where we log matches

# Function to process the redirects and write the final most recent version to temp
def process_redirects():
    redirects = {}  # This will store the final mapping of old_url to most recent new_url
    try:
        with open(REDIRECT_FILE, 'r') as file, open(TEMP_FILE, 'w') as temp:
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                # Skip any empty lines or lines that are comments
                if not line or line.startswith("//"):
                    continue

                # Process only lines that start with 'validurls'
                if line.startswith("validurls"):
                    match = re.match(r"validurls\['(.*?)'\] = '(.*?)';", line)
                    if match:
                        old_url = match.group(1)  # The old URL
                        new_url = match.group(2)  # The new URL

                        # Check if this old_url has already been encountered
                        if old_url in redirects:
                            # If yes, update it with the most recent new_url
                            redirects[old_url] = new_url
                        else:
                            # If not, add it as a new entry
                            redirects[old_url] = new_url

            # Write the final dictionary of redirects to the temp file
            for old_url, new_url in redirects.items():
                temp.write(f"{old_url} == {new_url}\n")  # Print in the desired format

    except FileNotFoundError:
        print(f"Error: The redirect file '{REDIRECT_FILE}' was not found.")
        exit(1)

# Main function to run the script
def main():
    print("Processing redirects...")
    process_redirects()
    print("Done.")

if __name__ == '__main__':
    main()

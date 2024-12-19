#!/usr/bin/env python3

import os
import subprocess
import re
import json

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
TEMP_FILE = os.path.join(PROJECT_ROOT, 'temp.json')  # Path to the file where we log matches (now in JSON format)

# Function to process the redirects and write the final most recent version to temp.json
def process_redirects():
    redirects = {}  # This will store the final mapping of url_key (new URL) to url_value (old URLs)
    first_line = 0  # Flag to check if it's the first line in the loop
    try:
        with open(REDIRECT_FILE, 'r') as file:
            for line in reversed(file.readlines()):  # Process the file backwards
                line = line.strip()  # Remove leading/trailing whitespace
                # Skip any empty lines or lines that are comments
                if not line or line.startswith("//"):
                    continue

                # Process only lines that start with 'validurls'
                if line.startswith("validurls"):
                    match = re.match(r"validurls\['(.*?)'\] = '(.*?)';", line)
                    if match:
                        url_key = match.group(1)  # The new URL (url_key)
                        url_value = match.group(2)  # The old URL (url_value)

                        # If it's the first line, add url_key and url_value to temp and continue
                        if first_line == 0:
                            redirects[url_key] = [url_value]
                            first_line = 1  # Set flag after first line is processed
                            continue

                        # Check if url_key is assigned as a 'url_value' for any existing redirects
                        if url_key in redirects.values():
                            # If url_key exists as a url_value, find the existing key for it
                            existing_key = [key for key, values in redirects.items() if url_key in values]
                            if existing_key:
                                # Assign the current url_value to the same existing url_key
                                redirects[existing_key[0]].append(url_value)
                                continue  # Skip this line and go to the next one
                        else:
                            # Check if url_key already exists as a key in redirects
                            if url_key in redirects:
                                # If url_key exists, check if the current url_value is already assigned
                                if url_value in redirects[url_key]:
                                    # If url_value is already assigned to the current url_key, write it to temp.json
                                    redirects[url_key].append(url_value)
                                    continue  # Skip this line as it's already added
                                else:
                                    # If the url_value is not assigned, skip this line
                                    continue
                            else:
                                # If url_key is new, create a new entry for it
                                redirects[url_key] = [url_value]

        # Write the final redirects dictionary to temp.json
        with open(TEMP_FILE, 'w') as temp_json:
            json.dump(redirects, temp_json, indent=4)

    except FileNotFoundError:
        print(f"Error: The redirect file '{REDIRECT_FILE}' was not found.")
        exit(1)

# Main function to run the script
def main():
    print("Processing redirects...")
    process_redirects()
    print("Done. Results saved to temp.json.")

if __name__ == '__main__':
    main()

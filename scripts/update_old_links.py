#!/usr/bin/env python3

import os
import json
import re
import subprocess

# Function to get the root directory of the Git repository
def get_git_root():
    return subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()

# Function 1: Build the dict.json from the redirects file (no merging, just creating)
def build_dict():
    root_dir = get_git_root()

    # File paths
    redirect_file = os.path.join(root_dir, 'assets/js/broken_redirect_list.js')
    dict_file = os.path.join(root_dir, 'dict.json')

    # Initialize an empty dictionary
    data_dict = {}

    # Read the redirect file and process it
    with open(redirect_file, 'r') as f:
        for index, line in enumerate(f, start=1):
            match = re.match(r"validurls\['([^']+)'\] = '([^']+)';", line.strip())
            if match:
                url_key, url_value = match.groups()

                # Add a numbered entry to the dictionary
                if url_key in data_dict:
                    data_dict[url_key]["url_values"].append(url_value)
                else:
                    data_dict[url_key] = {
                        "id": index,  # Entry number as id (no "entry_" prefix)
                        "url_values": [url_value]  # Initialize with a list of url_values
                    }

    # Write the initial dictionary to dict.json
    with open(dict_file, 'w') as f:
        json.dump(data_dict, f, indent=4)

# Function 2: Merge duplicates and remove duplicate values per key
def merge_duplicates():
    root_dir = get_git_root()

    # File paths
    dict_file = os.path.join(root_dir, 'dict.json')

    # Read the existing dictionary from dict.json
    with open(dict_file, 'r') as f:
        data_dict = json.load(f)

    # Step 1: Merging duplicates (from oldest to newest, based on id)
    with open(dict_file, 'w') as f:
        # Iterate through the original file line by line
        with open(os.path.join(root_dir, 'assets/js/broken_redirect_list.js'), 'r') as redirect_file:
            for line in redirect_file:
                match = re.match(r"validurls\['([^']+)'\] = '([^']+)';", line.strip())
                if match:
                    url_key, url_value = match.groups()

                    # If the url_key already exists, merge the value
                    if url_key in data_dict:
                        data_dict[url_key]["url_values"].append(url_value)
                    else:
                        # If the url_key doesn't exist, create a new entry
                        data_dict[url_key] = {
                            "id": len(data_dict) + 1,  # Incremental id
                            "url_values": [url_value]
                        }

        # Step 2: Remove duplicate values per key
        for url_key, data in data_dict.items():
            # Remove duplicates for each key's url_values
            data["url_values"] = list(set(data["url_values"]))  # Convert to set and back to list to remove duplicates

        # Write the updated dictionary back to dict.json
        json.dump(data_dict, f, indent=4)

# Main function to run the entire process
def main():
    # Step 1: Build the dict.json from the redirects file
    build_dict()

    # Step 2: Directly edit and merge the dict.json, removing duplicates
    merge_duplicates()

# Run the main function
if __name__ == "__main__":
    main()

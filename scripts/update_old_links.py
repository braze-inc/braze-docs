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

    with open(dict_file, 'w') as f:
        # Iterate through the original file line by line
        redirect_file = os.path.join(root_dir, 'assets/js/broken_redirect_list.js')
        with open(redirect_file, 'r') as rf:
            for line in rf:
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

        # Remove duplicate values per key
        for url_key, data in data_dict.items():
            data["url_values"] = list(set(data["url_values"]))

        # Write the updated dictionary back to dict.json
        json.dump(data_dict, f, indent=4)

# Function 3: Final cleanup
# go to `dict.json`
# start in normal order (i.e. smallest id first)
# for each key:
#   check if this key is listed as a value in any other key
#   if yes: merge this key's url_values into that other key's url_values
#   then remove this key from dict.json
def keep_newest_redirect():
    root_dir = get_git_root()
    dict_file = os.path.join(root_dir, 'dict.json')

    # Load the dictionary
    with open(dict_file, 'r') as f:
        data_dict = json.load(f)

    # Sort keys by their id in ascending order
    # data_dict is { url_key: { "id": number, "url_values": [...] } }
    sorted_keys = sorted(data_dict.keys(), key=lambda k: data_dict[k]["id"])

    # Iterate in ascending order of id
    # We'll make a copy of sorted_keys since we may remove keys from data_dict
    for current_key in sorted_keys:
        if current_key not in data_dict:
            # Might have been removed already in a previous iteration
            continue

        # current_key data
        current_values = data_dict[current_key]["url_values"]

        # Check if current_key appears as a value in any other key
        for other_key, other_data in data_dict.items():
            if other_key == current_key:
                continue
            # If current_key is found as a url_value in other_key
            if current_key in other_data["url_values"]:
                # Merge current_key's values into other_key's values
                other_data["url_values"].extend(current_values)
                # Remove duplicates after merging
                other_data["url_values"] = list(set(other_data["url_values"]))

                # Remove current_key from data_dict
                del data_dict[current_key]
                break  # Move to the next current_key

    # Write the updated dictionary back to dict.json
    with open(dict_file, 'w') as f:
        json.dump(data_dict, f, indent=4)

# Function 4: Remove self references
# after all merging and cleanup, remove any case where a key references itself in url_values
def remove_self_references():
    root_dir = get_git_root()
    dict_file = os.path.join(root_dir, 'dict.json')

    # Load the dictionary
    with open(dict_file, 'r') as f:
        data_dict = json.load(f)

    # For each key, remove itself from its url_values if it appears
    for url_key, data in data_dict.items():
        url_values = data["url_values"]
        if url_key in url_values:
            url_values = [v for v in url_values if v != url_key]
            data["url_values"] = url_values

    # Write the updated dictionary back to dict.json
    with open(dict_file, 'w') as f:
        json.dump(data_dict, f, indent=4)

def count_ids():
    root_dir = get_git_root()
    dict_file = os.path.join(root_dir, 'dict.json')

    # Load the dictionary
    with open(dict_file, 'r') as f:
        data_dict = json.load(f)

    # Number of IDs is the number of keys in the dictionary
    return len(data_dict)

# Main function to run the entire process
def main():
    # Step 1: Build the dict.json from the redirects file
    build_dict()
    print(f"number of IDs after build_dict: {count_ids()}")

    # Step 2: Merge duplicates and remove duplicates per key
    merge_duplicates()
    print(f"number of IDs after merge_duplicates: {count_ids()}")

    # Step 3: Final cleanup
    keep_newest_redirect()
    print(f"number of IDs after keep_newest_redirect: {count_ids()}")

    # Step 4: Remove self references
    remove_self_references()
    print(f"number of IDs after remove_self_references: {count_ids()}")

# Run the main function
if __name__ == "__main__":
    main()

#!/usr/bin/env python3

# This script uses 'assets/js/broken_redirect_list.js' to create a JSON dictionary
# of merged redirect descendants by finding all ancestors and merging them
# into the newest descendant. This script is necessary for 'update_old_links.py'.
#
# As of now, this script is used by ./scripts/update_old_links.py but is 
# not used by bdocs directly. However, you can use the following command to
# call it directly and generate a JSON file of merged duplicates.
#
# Usage: ./scripts/utils/merge_redirect_descendants.py [FILE|DIRECTORY]
#
# Options:
#   FILE              Delete unused reference links in a single file.
#   DIRECTORY         Recursively delete unused reference links in a directory.

import os
import json
import re
import subprocess

PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
REDIRECT_FILE = os.environ.get('REDIRECT_FILE')
REDIRECT_MATCHES = os.environ.get('REDIRECT_MATCHES')


# Create JSON dictionary from 'assets/js/broken_redirect_list.js'. Syntax:
# validurls['OLD'] = 'NEW';
def create_dict():
  # print("Running build_dict...")
    data_dict = {}
    total_old_urls = 0

    with open(REDIRECT_FILE, 'r') as f:
        for index, line in enumerate(f, start=1):
            match = re.match(r"validurls\['/docs([^']+)'\] = '/docs([^']+)';", line.strip())
            if match:
                old_url, new_url = match.groups()

                # Remove leading slash
                old_url = old_url.lstrip('/')
                new_url = new_url.lstrip('/')

                # 1) If '#' not in old_url, ensure it ends with '/'
                if '#' not in old_url:
                    if not old_url.endswith('/'):
                        old_url += '/'

                # 2) If '#' not in new_url, ensure it ends with '/'
                if '#' not in new_url:
                    if not new_url.endswith('/'):
                        new_url += '/'

                # Put the leading slash back into each
                old_url = f"/{old_url}"
                new_url = f"/{new_url}"

                data_dict[f"entry_{index}"] = {
                    "new_url": new_url,
                    "old_urls": [old_url]
                }

                total_old_urls += 1

    with open(REDIRECT_MATCHES, 'w') as f:
        json.dump(data_dict, f, indent=4)

    # After building
    # print(f"# of new_urls: {len(data_dict)}")
    # print(f"# of old_urls: {total_old_urls}\n")


# If 2 or more identical keys exist, merge all values into the key with the
# highest 'entry_key' number, then delete the other keys.
def merge_duplicate_keys():
  # print("Running merge_duplicate_keys...")
    with open(REDIRECT_MATCHES, 'r') as f:
        data_dict = json.load(f)

    # Group entries by new_url
    new_url_map = {}
    for entry_key, data in data_dict.items():
        nu = data["new_url"]
        new_url_map.setdefault(nu, []).append(entry_key)

    merged_count = 0
    for nu, entries in new_url_map.items():
        if len(entries) > 1:
            entries_with_num = [(int(e.split('_')[1]), e) for e in entries]
            entries_with_num.sort(key=lambda x: x[0])  # ascending by number
            largest_num, largest_entry = entries_with_num[-1]

            for (num, e) in entries_with_num[:-1]:
                data_dict[largest_entry]["old_urls"].extend(data_dict[e]["old_urls"])
                del data_dict[e]
                merged_count += 1

    with open(REDIRECT_MATCHES, 'w') as f:
        json.dump(data_dict, f, indent=4)

    # print(f"# of keys merged: {merged_count}")
    # print_counts(data_dict)


# If a key contains more than one identical value, keep one and delete the rest.
def delete_duplicate_values():
  # print("Running delete_duplicate_values...")
    with open(REDIRECT_MATCHES, 'r') as f:
        data_dict = json.load(f)

    values_deleted = 0
    for entry_key, data in data_dict.items():
        old_urls = data["old_urls"]
        unique = list(set(old_urls))
        diff = len(old_urls) - len(unique)
        if diff > 0:
            values_deleted += diff
            data["old_urls"] = unique

    with open(REDIRECT_MATCHES, 'w') as f:
        json.dump(data_dict, f, indent=4)

    # print(f"# of values deleted: {values_deleted}")
    # print_counts(data_dict)


# If A redirects to B, and B to C, both A and B are considered descendants of C.
# This function, merges all descendants into the newest parent (in this case C),
# If 1st entry exists as a value in the last entry:
# reassign all its values to the last entry, then remove the 1st entry.
# If no match, continue to 2nd-to-last entry and so on.
# If no descendants are found, keep 1st entry, then check 2nd entry, and so on.
def merge_descendants():
  # print("Running merge_descendants...")
    with open(REDIRECT_MATCHES, 'r') as f:
        data_dict = json.load(f)

    entry_keys = list(data_dict.keys())

    merged_count = 0
    # Must be in ascending order (i.e. smallest entry number first).
    for i, current_entry in enumerate(entry_keys):
        if current_entry not in data_dict:
            continue

        current_new_url = data_dict[current_entry]["new_url"]
        current_old_urls = data_dict[current_entry]["old_urls"]

        # Must be in descending order (i.e. largest entry number first).
        for j in range(len(entry_keys) - 1, i, -1):
            other_entry = entry_keys[j]
            if other_entry not in data_dict or other_entry == current_entry:
                continue

            other_data = data_dict[other_entry]
            if current_new_url in other_data["old_urls"]:
                other_data["old_urls"].extend(current_old_urls)
                other_data["old_urls"] = list(set(other_data["old_urls"]))
                del data_dict[current_entry]
                merged_count += 1
                break

    with open(REDIRECT_MATCHES, 'w') as f:
        json.dump(data_dict, f, indent=4)

    # print(f"# of descendants merged: {merged_count}")
    # print_counts(data_dict)


# If a key contains a value of itself, remove that value.
def remove_self_references():
  # print("Running remove_self_references...")
    with open(REDIRECT_MATCHES, 'r') as f:
        data_dict = json.load(f)

    self_removed = 0
    for entry_key, data in data_dict.items():
        nu = data["new_url"]
        old_urls = data["old_urls"]
        if nu in old_urls:
            old_len = len(old_urls)
            data["old_urls"] = [v for v in old_urls if v != nu]
            new_len = len(data["old_urls"])
            self_removed += (old_len - new_len)

    with open(REDIRECT_MATCHES, 'w') as f:
        json.dump(data_dict, f, indent=4)

  # print(f"# of self refs removed: {self_removed}")
    with open(REDIRECT_MATCHES, 'r') as f:
        data_dict = json.load(f)
    # print_counts(data_dict)


# Debugging: Counts the number of new and old urls current in file when called.
def print_counts(data_dict):
    # Count how many entries (new_urls)
    new_urls_count = len(data_dict)
    # Count how many old_urls total
    old_urls_count = sum(len(data["old_urls"]) for data in data_dict.values())
  # print(f"# of new_urls: {new_urls_count}")
  # print(f"# of old_urls: {old_urls_count}\n")


def main():
    create_dict()
    merge_duplicate_keys()
    delete_duplicate_values()
    merge_descendants()
    remove_self_references()


if __name__ == "__main__":
    main()

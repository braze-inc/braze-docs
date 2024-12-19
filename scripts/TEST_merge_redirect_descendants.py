#!/usr/bin/env python3

import os
import json

# File paths (update these as necessary)
PROJECT_ROOT = os.getcwd()  # Get the current working directory
TEMP_FILE = os.path.join(PROJECT_ROOT, 'test_dict.json')  # Path to the dict.json file

# Function to check for duplicates by counting occurrences of each url_key as a url_value elsewhere
def verify_duplicates():
    try:
        # Read the JSON data from the dict.json file
        with open(TEMP_FILE, 'r') as file:
            redirects = json.load(file)

        # Track occurrences of keys that appear multiple times as values
        occurrences = {}

        # Go through each url_key in the redirects dictionary
        for new_url in redirects:
            count = 0

            # Check occurrences in the keys (new_url)
            if new_url in redirects:
                count += 1

            # Check occurrences in the values (url_values)
            for data in redirects.values():
                count += data["url_values"].count(new_url)

            # If the new_url appears more than once in total,
            # that means it's used multiple times as a value (multi-use key).
            if count >= 2:
                occurrences[new_url] = count

        # Calculate the number of multi-use keys and unique keys
        multi_use_count = len(occurrences)
        unique_count = len(redirects) - multi_use_count

        # Print the summary lines regardless of duplicates
        print(f"# of multi-use keys: {multi_use_count}")
        print(f"# of unique keys: {unique_count}")
        print()

        # If there are multi-use keys, print them
        if occurrences:
            print("Multi-use keys:\n")
            for url, count in occurrences.items():
                # (count - 1) as per the previous logic
                print(f"[{count - 1}]: {url}")
                print()

    except FileNotFoundError:
        print(f"Error: The file '{TEMP_FILE}' was not found.")
        exit(1)

# Main function to run the script
def main():
    verify_duplicates()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import os
import json

# File paths (update these as necessary)
PROJECT_ROOT = os.getcwd()  # Get the current working directory
TEMP_FILE = os.path.join(PROJECT_ROOT, 'temp.json')  # Path to the temp file

# Function to check for duplicates by counting occurrences of each new URL
def verify_duplicates():
    try:
        # Read the JSON data from the temp.json file
        with open(TEMP_FILE, 'r') as file:
            redirects = json.load(file)

        # Track occurrences
        occurrences = {}

        # Go through each new URL in the redirects dictionary
        for new_url in redirects:
            count = 0

            # Check occurrences in the keys (new_url)
            if new_url in redirects:
                count += 1

            # Check occurrences in the values (old_urls)
            for old_urls_list in redirects.values():
                count += old_urls_list.count(new_url)

            # If the new_url appears more than once, store its count
            if count >= 2:
                occurrences[new_url] = count

        # Output the occurrences if found
        if occurrences:
            print("Duplicate new URLs found:")
            for url, count in occurrences.items():
                print(f"[{count}]: {url}")
        else:
            print("No duplicates found.")

    except FileNotFoundError:
        print(f"Error: The file '{TEMP_FILE}' was not found.")
        exit(1)

# Main function to run the script
def main():
    print("Verifying redirects for duplicates...")
    verify_duplicates()

if __name__ == '__main__':
    main()

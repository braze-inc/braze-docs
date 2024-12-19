#!/usr/bin/env python3

import os
import json

# File paths (update these as necessary)
PROJECT_ROOT = os.getcwd()  # Get the current working directory
TEMP_FILE = os.path.join(PROJECT_ROOT, 'dict.json')  # Path to the temp file

# Function to check for duplicates by counting occurrences of each new URL
def verify_duplicates():
    try:
        # Read the JSON data from the dict.json file
        with open(TEMP_FILE, 'r') as file:
            redirects = json.load(file)

        # Track occurrences
        occurrences = {}

        # Go through each entry in the redirects dictionary
        for url_key, data in redirects.items():
            url_values = data["url_values"]  # List of url_values for the url_key

            # Check for duplicates within the url_values for the current url_key
            for url_value in url_values:
                count = 0

                # Count occurrences of this url_value in the url_values list
                count = url_values.count(url_value)

                # If this url_value appears more than once, store its count
                if count >= 2:
                    occurrences[url_value] = count

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

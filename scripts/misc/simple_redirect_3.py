#!/usr/bin/env python3

import os

# Get the Git root path
GIT_ROOT = os.popen('git rev-parse --show-toplevel').read().strip()

# Define the paths
BROKEN_REDIRECT_LIST = os.path.join(GIT_ROOT, 'assets', 'js', 'broken_redirect_list.js')
TEMP_FILE = os.path.join(GIT_ROOT, 'temp.md')

# Function to remove matching lines from the broken_redirect_list.js file
def remove_lines():
    # Read the lines from temp.md
    with open(TEMP_FILE, 'r') as temp_file:
        lines = temp_file.readlines()

    # Read the current contents of broken_redirect_list.js
    with open(BROKEN_REDIRECT_LIST, 'r') as file:
        file_lines = file.readlines()

    # Loop through each line in temp.md
    for line in lines:
        line = line.strip()
        if line:
            # Construct the target line to remove
            target_line = f"validurls['LATER'] = '{line}';\n"

            # If the target line exists in the broken_redirect_list.js, remove it
            file_lines = [l for l in file_lines if l != target_line]

    # Write the modified content back to broken_redirect_list.js
    with open(BROKEN_REDIRECT_LIST, 'w') as file:
        file.writelines(file_lines)

    print("Finished processing and removing matching lines from broken_redirect_list.js.")

# Run the function
remove_lines()

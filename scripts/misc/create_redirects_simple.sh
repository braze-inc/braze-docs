#!/bin/bash

# Automatically determine the GIT_ROOT path
GIT_ROOT=$(git rev-parse --show-toplevel)

# Define the target file
TARGET_FILE="$GIT_ROOT/assets/js/broken_redirect_list.js"

# Function to process each file
process_file() {
  # Get the relative path of the file from the current directory
  local rel_path="${1#./}"

  # Remove the .md extension if it exists
  local clean_path="${rel_path%.md}"

  # Append the required line to the broken_redirect_list.js file
  echo "validurls['LATER'] = '/docs/developer_guide/platform_integration_guides/$clean_path';" >> "$TARGET_FILE"
}

# Export the process_file function to be used in the find command
export -f process_file

# Start the recursive search and process each file
find . -type f -exec bash -c 'process_file "$0"' {} \;

echo "Finished processing files."

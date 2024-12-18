#!/bin/bash

# Automatically determine the GIT_ROOT path
GIT_ROOT=$(git rev-parse --show-toplevel)

# Define the target file
TARGET_FILE="$GIT_ROOT/assets/js/broken_redirect_list.js"

# Get the name of the starting directory (excluding './')
START_DIR=$(basename "$PWD")

# Loop through each .md file in the current directory and subdirectories
for file in $(find . -type f -name "*.md"); do
  # Get the relative path of the file from the current directory, excluding './'
  rel_path="${file#./}"

  # Remove the .md extension if it exists
  clean_path="${rel_path%.md}"

  # Prepend the starting directory name to the path
  full_path="$START_DIR/$clean_path"

  # Append the required line to the broken_redirect_list.js file
  echo "validurls['LATER'] = '/docs/developer_guide/platform_integration_guides/$full_path';" >> "$TARGET_FILE"
done

echo "Finished processing files."

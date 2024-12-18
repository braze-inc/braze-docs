#!/bin/bash

# Automatically determine the GIT_ROOT path
GIT_ROOT=$(git rev-parse --show-toplevel)

# Define the temporary target file in the Git root (called 'temp', not 'temp.sh')
TEMP_FILE="$GIT_ROOT/temp"

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

  # Write the result directly to the temp file (without 'echo' and '>>')
  echo "/docs/developer_guide/platform_integration_guides/$full_path" >> "$TEMP_FILE"
done

echo "Finished processing files."

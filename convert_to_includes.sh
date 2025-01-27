#!/usr/bin/env bash
set -euo pipefail

# Resolve the directory of this script as PROJECT_ROOT
PROJECT_ROOT="$(dirname "$(realpath "$0")")"

# Prompt the user for the filename to move
echo "Which file do you want to move?"
read -r FILE_TO_MOVE

move_file() {
  local file_to_move="$1"

  # Find all occurrences of the file in the 'platforms' directory
  while IFS= read -r -d '' found_file; do
    # Strip the leading path to _docs/_developer_guide/ to get the relative path
    local relative_path="${found_file#"$PROJECT_ROOT/_docs/_developer_guide/"}"

    # Construct the destination file path
    local dest_file="$PROJECT_ROOT/_includes/developer_guide/$relative_path"
    local dest_dir
    dest_dir="$(dirname "$dest_file")"

    # Create the destination directory if it doesn't exist
    mkdir -p "$dest_dir"

    # Copy the file
    cp "$found_file" "$dest_file"
    echo "Copied $found_file -> $dest_file"
  done < <(find "$PROJECT_ROOT/_docs/_developer_guide/platforms" -type f -name "$file_to_move" -print0)
}

# Execute the function with the user-specified filename
move_file "$FILE_TO_MOVE"

#!/bin/bash
#
# DESCRIPTION
# 
# Usage: ./bdocs redirects -c

# Get the list of renamed files in `_docs` directory from `develop` branch
CHANGED_FILES=$(git diff --name-status origin/develop -- "$PROJECT_ROOT/_docs" | awk '$1 == "R" {print $2 " " $3}')

# Check if there are any renamed files
require_changed_files() {
    if [ -z "$CHANGED_FILES" ]; then
        echo "Error: No files or directories changed in the '_docs' directory."
        exit 1
    fi
}

# Function to format paths to remove underscores and `.md` extension
format_path() {
    echo "$1" | sed -E 's|/_|/|g' | sed -E 's|\.md$||g'
}

main() {
    # Create redirects
    redirects=""
    while IFS= read -r line; do
        old_path=$(echo "$line" | awk '{print $1}')
        new_path=$(echo "$line" | awk '{print $2}')

        # Format the paths
        formatted_old_path=$(format_path "$old_path")
        formatted_new_path=$(format_path "$new_path")

        # Create the redirect entry
        redirect="validurls['$formatted_old_path'] = '$formatted_new_path';"
        redirects+="$redirect"$'\n'
    done <<< "$CHANGED_FILES"

    # Write redirects to the redirect file
    echo "Appending redirects to $REDIRECT_FILE..."
    echo "$redirects" >> "$REDIRECT_FILE"

    echo "Redirects added successfully!"
}

require_changed_files
main

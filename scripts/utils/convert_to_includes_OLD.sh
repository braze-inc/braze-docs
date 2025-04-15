#!/bin/bash
# This script is a misc. script used to delete all the non-yaml content in a
# directly recursively and replace it with a link to the relevant include in a
# platform of your choice in `_includes/developer_guide/`.
# For example, this was used to migrate all Android and FireOS docs to includes.

# Ask for the platform name
read -p "Enter the platform name (e.g., android, swift, web, etc.): " PLATFORM
PLATFORM=$(echo "$PLATFORM" | tr '[:upper:]' '[:lower:]')

# Function to process markdown files
process_file() {
    local file_path="$1"
    
    # Calculate the relative path by stripping the starting directory
    relative_path="${file_path#"$start_dir/"}"
    
    # Check if the file is a markdown file
    if [[ "$file_path" == *.md ]]; then
        # Read the file and check for the YAML frontmatter
        yaml_end_line=$(grep -n '^---$' "$file_path" | tail -n 1 | cut -d: -f1)
        
        if [[ -n "$yaml_end_line" ]]; then
            # We found the YAML front matter, so we process the file
            # Keep only the YAML front matter and the first line of content after it
            head -n "$yaml_end_line" "$file_path" > "$file_path.tmp"
            echo -e "\n{% multi_lang_include developer_guide/$PLATFORM/$relative_path %}" >> "$file_path.tmp"
            
            # Replace the original file with the new content
            mv "$file_path.tmp" "$file_path"
        fi
    fi
}

# Start the recursive process
start_dir=$(pwd)

# Iterate through all files in the directory
find "$start_dir" -type f | while read file; do
    echo "Working on $file"
    process_file "$file"
done

echo "Processing complete."

#!/bin/bash

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
            echo -e "\n{% multi_lang_include developer_guide/android/$relative_path %}" >> "$file_path.tmp"
            
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

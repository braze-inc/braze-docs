#!/usr/bin/env python3

# This is script that converts the Entity Relationship JSON from 
# 'erd_get_json.py' to individual Markdown files and places them in the
# '_includes' directory. These markdown files are used to create this page:
# https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships/
# 
# Usage: ./scripts/utils/erd_generate_markdown.py

import os
import json
import subprocess


def main():
    # 1. Determine project root via Git
    PROJECT_ROOT = subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']
    ).decode('utf-8').strip()

    # 2. Build paths relative to PROJECT_ROOT
    json_inpath = os.path.join(PROJECT_ROOT, "scripts", "temp", "table_mappings.json")
    output_dir = os.path.join(PROJECT_ROOT, "_includes", "snowflake_users_messages")

    # 3. Read the JSON file
    with open(json_inpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # 4. Group tables by channel (3rd part of table name)
    channel_to_tables = {}
    
    for table_name, table_info in data.items():
        parts = table_name.split("_")
        if len(parts) < 3:
            continue
        
        # "USERS_MESSAGES_CONTENTCARD_CLICK_SHARED" -> channel = "CONTENTCARD"
        channel = parts[2]
        
        if channel not in channel_to_tables:
            channel_to_tables[channel] = {}
        
        channel_to_tables[channel][table_name] = table_info
    
    # 5. Create the output dir if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # 6. For each channel, create a markdown file
    for channel, tables_dict in channel_to_tables.items():
        md_filename = os.path.join(output_dir, f"{channel.lower()}.md")
        
        with open(md_filename, "w", encoding="utf-8") as md_file:
            for table_name, table_json in tables_dict.items():
                parts = table_name.split("_")
                
                # "rest" is everything after the channel part
                # e.g. "CONTENTCARD_CLICK_SHARED" if table_name has 5 parts
                if len(parts) > 3:
                    rest_of_name = "_".join(parts[3:])
                else:
                    rest_of_name = ""
                
                # 1) Heading includes backticks around rest_of_name
                md_file.write(f"### `{rest_of_name}`\n\n")
                
                # 2) JSON code block with single-line comment for the full table name
                pretty_json = json.dumps(table_json, indent=4)
                md_file.write(
                    f"```json\n"
                    f"// {table_name}\n\n"
                    f"{pretty_json}\n"
                    f"```\n\n"
                )
        

if __name__ == "__main__":
    main()

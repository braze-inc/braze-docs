#!/usr/bin/env python3

# This script converts the Entity Relationship JSON from 'erd_get_json.py'
# into individual Markdown files, grouping tables by channel. It prints
# the table name and (optionally) its description on separate lines within
# the code block comment, with the description's first letter capitalized
# and a period appended if not present.

import os
import json
import subprocess

def main():
    PROJECT_ROOT = subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']
    ).decode('utf-8').strip()

    json_inpath = os.path.join(PROJECT_ROOT, "scripts", "temp", "table_mappings.json")
    output_dir = os.path.join(PROJECT_ROOT, "_includes", "snowflake_users_messages")

    with open(json_inpath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Group tables by the third underscore-delimited part of the name
    channel_to_tables = {}
    for table_name, table_info in data.items():
        parts = table_name.split("_")
        if len(parts) < 3:
            continue
        channel = parts[2]
        if channel not in channel_to_tables:
            channel_to_tables[channel] = {}
        channel_to_tables[channel][table_name] = table_info

    os.makedirs(output_dir, exist_ok=True)

    for channel, tables_dict in channel_to_tables.items():
        md_filename = os.path.join(output_dir, f"{channel.lower()}.md")
        with open(md_filename, "w", encoding="utf-8") as md_file:
            for table_name, table_json in tables_dict.items():
                # Determine the segment after the channel
                parts = table_name.split("_")
                rest_of_name = "_".join(parts[3:]) if len(parts) > 3 else ""

                # Heading
                md_file.write(f"### `{rest_of_name}`\n\n")

                # Extract description (if any), ensure first char uppercase, end with period
                desc = table_json.get("description", "").strip()
                if desc:
                    desc = desc[0].upper() + desc[1:]
                    if desc[-1] != ".":
                        desc += "."

                # Make a copy to remove the 'description' field from the snippet
                table_json_copy = dict(table_json)
                table_json_copy.pop("description", None)

                # Format the JSON
                pretty_json = json.dumps(table_json_copy, indent=4)

                # Code block
                md_file.write("```json\n")
                md_file.write(f"// {table_name}\n")
                if desc:
                    md_file.write(f"// {desc}\n\n")
                else:
                    md_file.write("\n")  # just a blank line

                md_file.write(f"{pretty_json}\n")
                md_file.write("```\n\n")

if __name__ == "__main__":
    main()

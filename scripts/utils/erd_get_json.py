#!/usr/bin/env python3

import os
import json
import re
import subprocess

# Overrides the logic to force these keys to be foreign:
FOREIGN_OVERRIDE = [
    "APP_GROUP_ID"
]

# Overrides the logic to force these keys to be native:
NATIVE_OVERRIDE = [
    "AD_ID",
    "SEND_ID",
    "LINK_ID",
    "BUTTON_ID",
    "SLIDE_ID"
]

def parse_and_classify(filename):
    # Regex for lines that might contain table info
    table_line_pattern = re.compile(r'^(.*?)\s*:\s*(.*)$')

    tables_dict = {}
    column_comments = {}
    current_table = None

    with open(filename, 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                # If it's a blank line, ignore it, but don't reset current_table
                continue

            # Check if this line might be a table header
            header_match = table_line_pattern.match(line)
            # Its only a table header if it does NOT have '(' or '):'
            if header_match and '(' not in line and '):' not in line:
                potential_table = header_match.group(1).strip()
                # Only track if table name starts with "USERS_MESSAGES" or "USERS_BEHAVIORS"
                if (potential_table.startswith("USERS_MESSAGES") or
                    potential_table.startswith("USERS_BEHAVIORS")):
                    tables_dict[potential_table] = {
                        "primary_key": [],
                        "foreign_keys": [],
                        "native_keys": [],
                        "unknown": []
                    }
                    column_comments[potential_table] = {}
                    current_table = potential_table
                else:
                    current_table = None
                continue

            # If we have a valid table in context, parse for columns
            if current_table:
                # Check if it looks like a column line (has '(')
                if '(' in line:
                    # The column name is everything before the first '('
                    parts = line.split('(', 1)
                    column_name = parts[0].strip()

                    # If there's a '):', then everything after it is the comment
                    comment_text = ""
                    if '):' in line:
                        splitted = line.split('):', 1)
                        comment_text = splitted[1].strip()

                    # Store comment separately
                    column_comments[current_table][column_name] = comment_text

                    # Classify column
                    if column_name == "ID":
                        tables_dict[current_table]["primary_key"].append(column_name)
                    elif column_name.endswith("_ID") or column_name.endswith("_API_ID"):
                        tables_dict[current_table]["foreign_keys"].append(column_name)
                    else:
                        tables_dict[current_table]["native_keys"].append(column_name)
                else:
                    # If it doesn't match our column expectation
                    tables_dict[current_table]["unknown"].append(line)

    return tables_dict, column_comments

def main():
    # Determine project root
    PROJECT_ROOT = subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']
    ).decode('utf-8').strip()

    # Build paths
    txt_filepath = os.path.join(
        PROJECT_ROOT,
        "assets",
        "download_file",
        "data-sharing-raw-table-schemas.txt"
    )
    json_outpath = os.path.join(PROJECT_ROOT, "scripts", "temp", "table_mappings.json")

    # Parse and classify
    tables_dict, column_comments = parse_and_classify(txt_filepath)

    # For each col in FOREIGN_OVERRIDE, move it from native_keys -> foreign_keys if present
    for table_name, categories in tables_dict.items():
        for col in FOREIGN_OVERRIDE:
            if col in categories["native_keys"]:
                categories["native_keys"].remove(col)
                categories["foreign_keys"].append(col)

    # For each col in NATIVE_OVERRIDE, move it from foreign_keys -> native_keys if present
    for table_name, categories in tables_dict.items():
        for col in NATIVE_OVERRIDE:
            if col in categories["foreign_keys"]:
                categories["foreign_keys"].remove(col)
                categories["native_keys"].append(col)

    # Convert each raw column name in the classification lists into
    #    objects with { "name": x, "comment": y }
    for table_name, categories in tables_dict.items():
        for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
            new_list = []
            for col_name in categories[cat_name]:
                cmt = column_comments[table_name].get(col_name, "")
                new_list.append({"name": col_name, "comment": cmt})
            categories[cat_name] = new_list

    # Remove "unknown" if empty
    any_unknown = any(len(tbl_data["unknown"]) > 0 for tbl_data in tables_dict.values())
    if not any_unknown:
        for tbl_data in tables_dict.values():
            del tbl_data["unknown"]

    # Convert each category from list-of-objects -> dictionary { col_name: col_comment }
    for table_name, categories in tables_dict.items():
        for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
            if cat_name not in categories:
                continue
            dct = {}
            for col_info in categories[cat_name]:
                col_nm = col_info["name"]
                col_cmt = col_info["comment"]
                dct[col_nm] = col_cmt
            categories[cat_name] = dct

    # Write final output JSON with minimal indentation (or single line if you prefer)
    os.makedirs(os.path.dirname(json_outpath), exist_ok=True)
    with open(json_outpath, "w", encoding="utf-8") as out:
        # To make format only a single line, do:
        #   json.dump(tables_dict, out, indent=None, separators=(',',':'))
        # To make format more compact but still multi-line, do:
        #   indent=2:
        json.dump(tables_dict, out, indent=2)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os
import json
import re
import subprocess

FOREIGN_OVERRIDE = [
    "APP_GROUP_ID"
]

NATIVE_OVERRIDE = [
    "AD_ID",
    "SEND_ID",
    "LINK_ID",
    "BUTTON_ID",
    "SLIDE_ID"
]

def parse_and_classify(filename):
    table_line_pattern = re.compile(r'^(.*?)\s*:\s*(.*)$')
    tables_dict = {}
    column_comments = {}
    current_table = None

    with open(filename, 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            header_match = table_line_pattern.match(line)
            # Only treat as table if no '(' or '):' is found
            if header_match and '(' not in line and '):' not in line:
                potential_table = header_match.group(1).strip()
                table_comment = header_match.group(2).strip()  # everything after the colon

                # Only track tables starting with specific prefixes
                if potential_table.startswith("USERS_MESSAGES") or potential_table.startswith("USERS_BEHAVIORS"):
                    # Insert "description" above other categories
                    tables_dict[potential_table] = {
                        "description": table_comment,
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

            if current_table:
                if '(' in line:
                    parts = line.split('(', 1)
                    column_name = parts[0].strip()
                    comment_text = ""
                    if '):' in line:
                        splitted = line.split('):', 1)
                        comment_text = splitted[1].strip()

                    # Store comment in separate structure
                    column_comments[current_table][column_name] = comment_text

                    # Classify
                    if column_name == "ID":
                        tables_dict[current_table]["primary_key"].append(column_name)
                    elif column_name.endswith("_ID") or column_name.endswith("_API_ID"):
                        tables_dict[current_table]["foreign_keys"].append(column_name)
                    else:
                        tables_dict[current_table]["native_keys"].append(column_name)
                else:
                    tables_dict[current_table]["unknown"].append(line)

    return tables_dict, column_comments

def main():
    PROJECT_ROOT = subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']
    ).decode('utf-8').strip()

    txt_filepath = os.path.join(
        PROJECT_ROOT,
        "assets",
        "download_file",
        "data-sharing-raw-table-schemas.txt"
    )
    json_outpath = os.path.join(PROJECT_ROOT, "scripts", "temp", "table_mappings.json")

    tables_dict, column_comments = parse_and_classify(txt_filepath)

    # Move specified columns from native to foreign if present
    for table_name, categories in tables_dict.items():
        for col in FOREIGN_OVERRIDE:
            if col in categories["native_keys"]:
                categories["native_keys"].remove(col)
                categories["foreign_keys"].append(col)

    # Move specified columns from foreign to native if present
    for table_name, categories in tables_dict.items():
        for col in NATIVE_OVERRIDE:
            if col in categories["foreign_keys"]:
                categories["foreign_keys"].remove(col)
                categories["native_keys"].append(col)

    # Convert raw column names to objects { "name": x, "comment": y }
    for table_name, categories in tables_dict.items():
        for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
            new_list = []
            for col_name in categories[cat_name]:
                cmt = column_comments[table_name].get(col_name, "")
                new_list.append({"name": col_name, "comment": cmt})
            categories[cat_name] = new_list

    # Remove unknown if empty
    any_unknown = any(len(tbl_data["unknown"]) > 0 for tbl_data in tables_dict.values())
    if not any_unknown:
        for tbl_data in tables_dict.values():
            del tbl_data["unknown"]

    # Convert each category from list-of-objects -> { col_name: col_comment }
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

    os.makedirs(os.path.dirname(json_outpath), exist_ok=True)
    with open(json_outpath, "w", encoding="utf-8") as out:
        # Adjust as desired for spacing
        json.dump(tables_dict, out, indent=2)

if __name__ == "__main__":
    main()

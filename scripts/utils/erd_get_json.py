#!/usr/bin/env python3

# This is script that converts the Entity Relationships raw table schema into a
# JSON file sorted by key-type. This script, along with
# 'erd_generate_markdown.py', is used to create this page:
# https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships/
# 
# Usage: ./scripts/utils/erd_get_json.py

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
    """
    Reads the text file and returns a dictionary of the form:

        {
            "<TABLE_NAME>": {
                "primary_key": [...],
                "foreign_keys": [...],
                "native_keys": [...],
                "unknown": [...]
            },
            ...
        }

    BUT only includes tables that start with `USERS_MESSAGES`.

    Initial Classification Rules (before overrides):
        - primary_key: column == "ID"
        - foreign_keys: column ends with "_ID" or "_API_ID"
        - native_keys: everything else
    """
    table_name_pattern = re.compile(r'^(.*?)\s*:\s*(.*)$')
    tables_dict = {}
    current_table = None

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                current_table = None
                continue
            
            header_match = table_name_pattern.match(line)
            if header_match:
                potential_table = header_match.group(1).strip()
                if potential_table.startswith("USERS_MESSAGES"):
                    tables_dict[potential_table] = {
                        "primary_key": [],
                        "foreign_keys": [],
                        "native_keys": [],
                        "unknown": []
                    }
                    current_table = potential_table
                else:
                    current_table = None
                continue
            
            if current_table:
                column_name = line.split('(')[0].strip()
                
                if column_name == "ID":
                    tables_dict[current_table]["primary_key"].append(column_name)
                elif column_name.endswith("_ID") or column_name.endswith("_API_ID"):
                    tables_dict[current_table]["foreign_keys"].append(column_name)
                else:
                    tables_dict[current_table]["native_keys"].append(column_name)

    return tables_dict

def main():
    # 1. Determine project root via Git
    PROJECT_ROOT = subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']
    ).decode('utf-8').strip()

    # 2. Build paths relative to PROJECT_ROOT
    txt_filepath = os.path.join(
        PROJECT_ROOT,
        "assets",
        "download_file",
        "data-sharing-raw-table-schemas.txt"
    )
    json_outpath = os.path.join(PROJECT_ROOT, "scripts", "temp", "table_mappings.json")

    # 3. Parse and classify
    table_classification = parse_and_classify(txt_filepath)

    # 4. Apply overrides
    for table_name, categories in table_classification.items():
        for col in FOREIGN_OVERRIDE:
            for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
                if col in categories[cat_name]:
                    categories[cat_name].remove(col)
            categories["foreign_keys"].append(col)

    for table_name, categories in table_classification.items():
        for col in NATIVE_OVERRIDE:
            for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
                if col in categories[cat_name]:
                    categories[cat_name].remove(col)
            categories["native_keys"].append(col)

    # 5. Remove "unknown" key if empty across all tables
    any_unknown = any(len(tbl_data["unknown"]) > 0 for tbl_data in table_classification.values())
    if not any_unknown:
        for tbl_data in table_classification.values():
            del tbl_data["unknown"]

    # 6. Write output JSON
    os.makedirs(os.path.dirname(json_outpath), exist_ok=True)
    with open(json_outpath, "w", encoding="utf-8") as out:
        json.dump(table_classification, out, indent=4)
    
    
if __name__ == "__main__":
    main()

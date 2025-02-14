#!/usr/bin/env python3

import json
import re

# Override lists
FOREIGN_OVERRIDE = [
    "APP_GROUP_ID"
]

NATIVE_OVERRIDE = [
    "AD_ID",
    "SEND_ID"
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
            
            # Check if this line is a table definition (TABLE_NAME: desc)
            header_match = table_name_pattern.match(line)
            if header_match:
                # Potentially a new table
                potential_table = header_match.group(1).strip()

                # Only proceed if table name starts with "USERS_MESSAGES"
                if potential_table.startswith("USERS_MESSAGES"):
                    tables_dict[potential_table] = {
                        "primary_key": [],
                        "foreign_keys": [],
                        "native_keys": [],
                        "unknown": []
                    }
                    current_table = potential_table
                else:
                    # Skip this table
                    current_table = None
                continue
            
            # Column definition line?
            if current_table:
                column_name = line.split('(')[0].strip()
                
                # Classification rules
                if column_name == "ID":
                    tables_dict[current_table]["primary_key"].append(column_name)
                elif column_name.endswith("_ID") or column_name.endswith("_API_ID"):
                    tables_dict[current_table]["foreign_keys"].append(column_name)
                else:
                    tables_dict[current_table]["native_keys"].append(column_name)

    return tables_dict

def main():
    filename = "./assets/download_file/data-sharing-raw-table-schemas.txt"
    table_classification = parse_and_classify(filename)

    # Apply FOREIGN_OVERRIDE
    for table_name, categories in table_classification.items():
        for col in FOREIGN_OVERRIDE:
            # Remove col from all categories
            for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
                if col in categories[cat_name]:
                    categories[cat_name].remove(col)
            # Add col to foreign_keys
            categories["foreign_keys"].append(col)

    # Apply NATIVE_OVERRIDE
    for table_name, categories in table_classification.items():
        for col in NATIVE_OVERRIDE:
            # Remove col from all categories
            for cat_name in ["primary_key", "foreign_keys", "native_keys", "unknown"]:
                if col in categories[cat_name]:
                    categories[cat_name].remove(col)
            # Add col to native_keys
            categories["native_keys"].append(col)

    # Remove "unknown" key if empty across all tables
    any_unknown = any(len(tbl_data["unknown"]) > 0 for tbl_data in table_classification.values())
    if not any_unknown:
        for tbl_data in table_classification.values():
            del tbl_data["unknown"]

    # Write output to 'table_mappings.json'
    with open("table_mappings.json", "w", encoding="utf-8") as out:
        json.dump(table_classification, out, indent=4)
    
    print("JSON output written to table_mappings.json")


if __name__ == "__main__":
    main()

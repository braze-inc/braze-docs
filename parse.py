#!/usr/bin/env python3

import json
import re

def parse_file(filename):
    """
    Reads the text file and returns a dictionary:
        {
            "COLUMN_NAME": {"TABLE_1", "TABLE_2", ...},
            "ANOTHER_COLUMN": {"TABLE_1", ...},
            ...
        }
    """
    # This dictionary accumulates columns as keys
    # and a set of table names in which the column appears as values
    column_to_tables = {}

    # Regex to match the start of each table definition line
    # Example line: USERS_CANVASSTEP_PROGRESSION_SHARED: Progression events for a user within a canvas
    # We extract the table name before the ':'
    table_name_pattern = re.compile(r'^(.*?)\s*:\s*(.*)$')
    
    current_table = None  # Will store the current table name
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                # Empty line indicates potential separation between table definitions
                current_table = None
                continue
            
            # Check if the line is the "header" for a new table
            match = table_name_pattern.match(line)
            if match:
                # Found a new table
                current_table = match.group(1).strip()
                # We don't actually need the description part (match.group(2)) for this use-case
                continue
            
            # If not a table header, then this line should be a column definition
            # Column lines look like: ID (VARCHAR(16777216)) or TIME (NUMBER(38,0)) etc.
            # We'll just split by space or parentheses to get the column name
            # But the simplest is: everything before the first '(' is the column name
            if current_table:
                # Attempt to parse column name:
                # e.g. "ID (VARCHAR(16777216))" -> "ID"
                column_name = line.split('(')[0].strip()
                
                # Add to dictionary
                if column_name not in column_to_tables:
                    column_to_tables[column_name] = set()
                column_to_tables[column_name].add(current_table)

    return column_to_tables

def main():
    # 1. Parse the file
    filename = "./assets/download_file/data-sharing-raw-table-schemas.txt"
    column_data = parse_file(filename)
    
    # 2. Convert the sets to lists (to make it JSON serializable), sorted or unsorted as needed
    output_data = {}
    for column_name, table_set in column_data.items():
        output_data[column_name] = sorted(table_set)
    
    # 3. Write out the JSON file
    # The user requested that the JSON have keys for each column,
    # and each key's value is the list of tables where that column is found.
    with open("column_mappings.json", "w", encoding="utf-8") as out:
        json.dump(output_data, out, indent=4)
    
    print("JSON output written to column_mappings.json")

if __name__ == "__main__":
    main()

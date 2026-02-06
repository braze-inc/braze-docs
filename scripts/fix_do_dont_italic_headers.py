#!/usr/bin/env python3
"""
Merge the first data row of Do/Don't tables into the header when that row
is entirely italic (using _underscore_ or *asterisk*). Handles both apostrophe
variants in "Don't".
Run from repo root: python scripts/fix_do_dont_italic_headers.py _docs/_contributing/style_guide.md
"""
import re
import sys

def extract_italic(cell):
    s = cell.strip()
    if len(s) >= 2 and ((s[0] == "_" and s[-1] == "_") or (s[0] == "*" and s[-1] == "*")):
        return s[1:-1].strip()
    return s

def is_italic_cell(cell):
    s = cell.strip()
    if len(s) < 2:
        return False
    return (s[0] == "_" and s[-1] == "_") or (s[0] == "*" and s[-1] == "*")

def parse_table_row(line):
    parts = line.split("|")
    parts = [p.strip() for p in parts]
    if len(parts) >= 3:
        return [parts[1], parts[2]]
    return []

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "_docs/_contributing/style_guide.md"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out = []
    i = 0
    transformed = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        # Skip already transformed headers
        if "<br><br>" in line:
            i += 1
            continue
        # Two-column Do / Don't (any apostrophe)
        if re.match(r"^\| Do \| Don.t \|\s*$", line):
            if i + 1 < len(lines) and re.match(r"^\| :---- \| :---- \|\s*$", lines[i + 1]):
                if i + 2 < len(lines):
                    first_data = lines[i + 2]
                    cells = parse_table_row(first_data)
                    if len(cells) >= 2 and is_italic_cell(cells[0]) and (
                        is_italic_cell(cells[1]) or cells[1].strip() == ""
                    ):
                        c1 = extract_italic(cells[0])
                        c2 = extract_italic(cells[1]) if cells[1].strip() else ""
                        orig_parts = line.split("|")
                        col2_label = orig_parts[2].strip() if len(orig_parts) >= 3 else "Don't"
                        new_header = (
                            f"| Do <br><br> *{c1}* | {col2_label} <br><br> *{c2}* |\n"
                            if c2
                            else f"| Do <br><br> *{c1}* | {col2_label} |\n"
                        )
                        out[-1] = new_header
                        i += 1
                        out.append(lines[i])
                        i += 1
                        i += 1  # skip italic row
                        while i < len(lines) and lines[i].strip().startswith("|"):
                            out.append(lines[i])
                            i += 1
                        transformed += 1
                        continue
        # Do | Do tables
        if re.match(r"^\| Do \| Do \|\s*$", line):
            if i + 1 < len(lines) and re.match(r"^\| :---- \| :---- \|\s*$", lines[i + 1]):
                if i + 2 < len(lines):
                    first_data = lines[i + 2]
                    cells = parse_table_row(first_data)
                    if len(cells) >= 2 and is_italic_cell(cells[0]) and (
                        is_italic_cell(cells[1]) or cells[1].strip() == ""
                    ):
                        c1 = extract_italic(cells[0])
                        c2 = extract_italic(cells[1]) if cells[1].strip() else ""
                        new_header = (
                            f"| Do <br><br> *{c1}* | Do <br><br> *{c2}* |\n"
                            if c2
                            else f"| Do <br><br> *{c1}* | Do |\n"
                        )
                        out[-1] = new_header
                        i += 1
                        out.append(lines[i])
                        i += 1
                        i += 1
                        while i < len(lines) and lines[i].strip().startswith("|"):
                            out.append(lines[i])
                            i += 1
                        transformed += 1
                        continue
        i += 1

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    print(f"Transformed {transformed} Do/Don't table(s).")

if __name__ == "__main__":
    main()

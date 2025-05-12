#!/usr/bin/env python3

# Converts table-mapping JSON (from 'erd_get_json.py') into per-channel 
# Markdown files, then prepends a shared Mermaid template and 
# rewrites the include placeholder.

import os
import json
import subprocess

PROJECT_ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).decode('utf-8').strip()
erd_json = os.path.join(PROJECT_ROOT, "scripts", "temp", "table_mappings.json")
markdown_dir = os.path.join(PROJECT_ROOT, "_includes", "snowflake_users_messages")
mermaid_dir = os.path.join(PROJECT_ROOT, "_includes", "snowflake_mermaid")
mermaid_tpl = os.path.join(mermaid_dir, "_TEMPLATE.md")


def create_tables(data):
    # group tables by third underscore-separated segment
    channel_to_tables = {}
    for name, info in data.items():
        parts = name.split("_")
        if len(parts) < 3:
            continue
        channel = parts[2]
        channel_to_tables.setdefault(channel, {})[name] = info

    # build a dict: {filename: markdown_content}
    files = {}
    for channel, tables in channel_to_tables.items():
        lines = ["## Relationship tables\n"]
        for table_name, table_json in tables.items():
            parts = table_name.split("_")
            rest  = "_".join(parts[3:]) if len(parts) > 3 else ""
            lines.append(f"\n### `{rest}`\n")
            desc = table_json.get("description", "").strip()
            if desc:
                desc = desc[0].upper() + desc[1:]
                if desc[-1] != ".":
                    desc += "."
            table_json_copy = dict(table_json)
            table_json_copy.pop("description", None)
            pretty = json.dumps(table_json_copy, indent=4)
            lines.append("```json")
            lines.append(f"// {table_name}")
            lines.append(f"// {desc}\n" if desc else "\n")
            lines.append(pretty)
            lines.append("```")
        files[f"{channel.lower()}.md"] = "\n".join(lines) + "\n"
    return files


def create_mermaid(file_map, mermaid_dir, template_str):
    # prepend template + replace placeholder if mermaid file exists
    for fname in file_map:
        if fname == "_TEMPLATE.md":
            continue
        mermaid_path = os.path.join(mermaid_dir, fname)
        if not os.path.exists(mermaid_path):
            continue
        include_line = template_str.replace(
            "snowflake_mermaid/FILENAME", f"snowflake_mermaid/{fname}"
        )
        file_map[fname] = f"{include_line}\n{file_map[fname]}"


def main():
    # load JSON
    with open(erd_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    # build markdown content
    file_map = create_tables(data)

    # read template once, then update content
    with open(mermaid_tpl, "r", encoding="utf-8") as t:
        template_content = t.read()
    create_mermaid(file_map, mermaid_dir, template_content)

    # write files to disk
    os.makedirs(markdown_dir, exist_ok=True)
    for fname, content in file_map.items():
        out_path = os.path.join(markdown_dir, fname)
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(content)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script: find_required_permissions.py
Description: List all .md files mentioning required user permissions for features.
"""
import os
import re

# Regex pattern for permission-related phrases
PERMISSION_PATTERNS = [
    r"must have (the )?.+ permission",
    r"need(s)? (the )?.+ permission",
    r"require(s)? (the )?.+ permission",
    r"user permission(s)? required",
    r"role(s)? required",
    r"need(s)? to have (the )?.+ role",
    r"must be an? (admin|administrator|owner|manager)",
    r"can access (if|when) (the )?.+ permission",
    r"allowed to .+ if (the )?.+ permission",
    r"entitlement(s)? required",
    r"authorization required",
    r"prerequisite: .+ permission",
    r"user group(s)? required",
    r"user must belong to (the )?.+ group",
    r"only available to (the )?.+ role",
    r"permission(s)? needed: .+",
    r"permission(s)? required: .+",
]
PERMISSION_REGEXES = [re.compile(p, re.IGNORECASE) for p in PERMISSION_PATTERNS]

results = []

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            try:
                with open(path, encoding='utf-8') as f:
                    for idx, line in enumerate(f, 1):
                        for regex in PERMISSION_REGEXES:
                            if regex.search(line):
                                # Store: file path, line number, line content (stripped)
                                results.append((path, idx, line.strip()))
                                break
            except Exception as e:
                print(f"Error reading {path}: {e}")

# Sort by file path, then line number
for path, idx, content in sorted(results, key=lambda x: (x[0], x[1])):
    print(f"{path}:{idx}: {content}")
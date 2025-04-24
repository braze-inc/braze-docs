#!/bin/bash
#
# For each new redirect in the current branch, the script uses the user-supplied
# base URL to list all old URLs so the user can open old links directly from
# the terminal to test redirects.
# 
# Usage: ./bdocs lredirects

# Check new redirects by comparing the current branch to develop.
NEW_REDIRECTS=$(git diff develop -- $REDIRECT_FILE)

# If there's no differences, print an error message and exit.
if [[ -z "$NEW_REDIRECTS" ]]; then
    echo "Error: No new redirects were found in this branch."
    echo ""
    exit 1
fi

# Check if a base URL was passed as an argument from bdocs, otherwise prompt the user.
if [[ -z "$1" ]]; then
    echo "Which base URL would you like to use? Note: You can use a local or deployment base URL."
    read BASE_URL
else
    BASE_URL=$1
fi

# Read input and remove any trailing '/' (if applicable), to avoid double '//'.
if [[ "$BASE_URL" == */ ]]; then
    BASE_URL="${BASE_URL%/}"
fi

# List all old URLs using 'BASE_URL' so the user can open links from terminal.
echo ""
echo "$NEW_REDIRECTS" | grep '^+' | grep -v '+++' | grep -v '^+$' | sed "s/^+validurls\['\([^']*\)'\].*/\1/" | sed "s|^|$BASE_URL|"

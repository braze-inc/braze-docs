#!/bin/bash

# TODO: create logic for if there's no PRs ready for deploy
# TODO: write script description + rewrite all command comments 
# TODO: cleanup/reformat script using bash scripting best practices
# TODO: add 'gh' and 'jq' to dev dependencies
# TODO: create how to guide and add to confluence

echo "Deploy text is generating..."

# Fetch PR list
PR_LIST=$(gh pr list --state all --limit 1000 --json mergedAt,number,title,url)

# Filter out PRs with 'mergedAt' as null and sort by date in descending order
SORTED_PR_LIST=$(echo "$PR_LIST" | jq '[.[] | select(.mergedAt != null)] | sort_by(.mergedAt) | reverse')

# Find the index of the most recent "Deploy -" PR
# TODO: find better method. Try to do something like "check for last 1000 PRs in 'develop', then check
# TODO: last 1000 PRs in 'master'. get a list of all PRs in 'develop' that are not in 'master'."
DEPLOY_INDEX=$(echo "$SORTED_PR_LIST" \
  | jq -r 'to_entries | map(select(.value.title | startswith("Deploy -"))) | .[0].key')

# Remove the last deploy entry and all entries below it
FILTERED_PR_LIST=$(echo "$SORTED_PR_LIST" | jq --argjson DEPLOY_INDEX "$DEPLOY_INDEX" 'del(.[$DEPLOY_INDEX:])')

# Output the result in Markdown format with modified title
DEPLOY_TEXT=$(echo "$FILTERED_PR_LIST" \
  | jq -r '.[] | "- [#" + (.number|tostring) + "](" + .url + ") - " + (.title | gsub("BD-[^ ]+"; ""))' \
  | tr -s ' ' | sort -t "[" -k2,2n)

cat << EOF
Complete! Copy your deploy text below:

$DEPLOY_TEXT
EOF


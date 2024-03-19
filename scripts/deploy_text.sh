#!/bin/bash
#
# This script generates the body text for deployment PRs in the Braze Docs repository.
# 
# Usage: ~/braze-docs/scripts/deploy_text.sh

TEMP_FILE=$(mktemp)

# Gets the latest commit hash from origin/master that is not in origin/develop.
LATEST_COMMIT_HASH=$(git log --max-count=1 --format="%H" origin/master ^origin/develop)

# Gets the log of commits starting from the latest commit hash.
COMMIT_LOGS=$(git log --first-parent "$LATEST_COMMIT_HASH"..origin/develop --pretty=%s»¦«%b)

# Parses the commit logs, formats them, then writes them to the temp file.
echo "$COMMIT_LOGS" | while IFS=»¦« read -r title body; do
    if [[ $title =~ Merge\ pull\ request\ \#([0-9]+) ]]; then
        PR_NUMBER=${BASH_REMATCH[1]}
        PR_TITLE=${body//¦«/}
        # If applicable, removes the Jira ticket number from the PR title.
        PR_TITLE=$(echo "$PR_TITLE" | sed -E 's/^BD-[0-9]+[:| ]*//')
        echo "- [#$PR_NUMBER](https://github.com/braze-inc/braze-docs/pull/$PR_NUMBER) - $PR_TITLE" >> "$TEMP_FILE"
    fi
done

# Returns the results in reverse order and clean up files.
if command -v tac &> /dev/null
then
    tac "$TEMP_FILE" # 'tac' is used by default
else
    tail -r "$TEMP_FILE" # 'tail -r' is used if tac isn't available
fi
rm "$TEMP_FILE"

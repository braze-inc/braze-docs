#!/bin/bash
#
# Creates the body text for deployment PRs in the Braze Docs repository.
# 
# Usage: ./bdocs deploy

main() {
    TEMP_FILE="$PROJECT_ROOT/scripts/temp/deploy_output"
    rm -f "$TEMP_FILE" # Clear contents from any previous runs

    # Gets the latest commit hash from origin/$PRIMARY_BRANCH that is not in origin/develop.
    LATEST_COMMIT_HASH=$(git log --max-count=1 --format="%H" origin/$PRIMARY_BRANCH ^origin/develop)

    if [ -z "$1" ] || [ -z "$2" ]; then
        # Gets the log of commits starting from the latest 
        # commit hash if no dates are provided.
        COMMIT_LOGS=$(git log --first-parent "$LATEST_COMMIT_HASH"..origin/develop --pretty=%s»¦«%b)
    else
        # Use the provided start and end dates to get the commit logs
        # Needed so 'release_text.sh' can get all deploys for a monthly release.
        START_DATE="$1"
        END_DATE="$2"
        COMMIT_LOGS=$(git log --first-parent --since="$START_DATE" --until="$END_DATE" origin/develop --pretty=%s»¦«%b)
    fi

    # Parses the commit logs, formats them, then writes them to the temp file.
    echo "$COMMIT_LOGS" | while IFS=»¦« read -r title body; do
        # Parse merge commit format
        if [[ $title =~ Merge\ pull\ request\ \#([0-9]+) ]]; then
            PR_NUMBER=${BASH_REMATCH[1]}
            PR_TITLE=${body//¦«/}
            PR_TITLE=$(echo "$PR_TITLE" | sed -E 's/^BD-[0-9]+[:| ]*//')

        # Parse squash merge format
        elif [[ $title =~ \(\#([0-9]+)\)$ ]]; then
            PR_NUMBER=${BASH_REMATCH[1]}
            PR_TITLE=$(echo "$title" \
                        | sed -E 's/[[:space:]]*\(#([0-9]+)\)$//' \
                        | sed -E 's/^BD-[0-9]+[:| ]*//')
        else
            continue   # skip everything else (e.g., Co-authored-by lines)
        fi

        echo "- [#$PR_NUMBER](https://github.com/braze-inc/braze-docs/pull/$PR_NUMBER) - $PR_TITLE" >> "$TEMP_FILE"
    done

    # Returns the results in reverse order and clean up files.
    if command -v tac &> /dev/null
    then
        tac "$TEMP_FILE" # 'tac' is used by default
    else
        tail -r "$TEMP_FILE" # 'tail -r' is used if tac isn't available
    fi
}

main "$1" "$2"

#!/bin/bash
#
# Creates the body text for deployment PRs in the Braze Docs repository.
# 
# Usage: ./bdocs deploy

main() {
    TEMP_FILE="$PROJECT_ROOT/scripts/temp/deploy_output"
    rm -f "$TEMP_FILE" # Clear contents from any previous runs

    # Commits to deploy: on develop but not yet on main.
    # Use origin/main explicitly (not LATEST_COMMIT_HASH) so this works when the
    # workflow checks out develop—otherwise "..origin/develop" would compare to HEAD.
    if [ -z "$1" ] || [ -z "$2" ]; then
        COMMIT_LOGS=$(git log --first-parent origin/$PRIMARY_BRANCH..origin/develop --pretty=%s»¦«%b)
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
    if [ -f "$TEMP_FILE" ]; then
        if command -v tac &> /dev/null; then
            tac "$TEMP_FILE"
        else
            tail -r "$TEMP_FILE"
        fi
    fi
}

main "$1" "$2"

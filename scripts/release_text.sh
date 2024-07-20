#!/bin/bash

# This script lists the commit bodies, commit hash, and full date/time of all parent commits since the last release version tag,
# and runs deploy_text.sh for each commit.
#
# Usage: ~/braze-docs/scripts/release_text.sh

main() {
    # Run script from the root of the git repository
    cd "$PROJECT_ROOT"

    # Get the last release version tag
    LAST_RELEASE_TAG=$(git describe --tags $(git rev-list --tags --max-count=1 --tags="v.*"))

    # Get the timestamp of the last release tag
    LAST_RELEASE_TIMESTAMP=$(git log -1 --pretty=format:"%cI" "$LAST_RELEASE_TAG")

    # Convert Git logs to JSON and sort by date
    COMMIT_LOGS=$(git log --merges --first-parent --since="$LAST_RELEASE_TIMESTAMP" origin/master --pretty=format:'{%n  "commit": "%H",%n  "date": "%cI",%n  "title": "%s",%n  "body": "%b"%n},' | perl -pe 'BEGIN{print "["}; END{print "]\n"}' | perl -pe 's/},]/}]/' | jq -c '. | sort_by(.date)')

    if [ -z "$COMMIT_LOGS" ]; then
        echo "No commit logs found. Exiting."
        exit 1
    fi

    # Remove the first entry from the commit logs. It's from the last release
    COMMIT_LOGS=$(echo "$COMMIT_LOGS" | jq '.[1:]')

    # Initialize the previous commit date with the release timestamp
    PREV_COMMIT_DATE="$LAST_RELEASE_TIMESTAMP"
    
    # Iterate over the commit logs and run deploy_text.sh for each commit
    echo "$COMMIT_LOGS" | jq -c '.[]' | while read commit; do

        # Pull variables from 'COMMIT_LOGS'.
        COMMIT_HASH=$(echo "$commit" | jq -r '.commit')
        COMMIT_DATE=$(echo "$commit" | jq -r '.date')
        COMMIT_TITLE=$(echo "$commit" | jq -r '.title')
        COMMIT_BODY=$(echo "$commit" | jq -r '.body')

        # Print the deploy text for each deployment.
        echo "## $COMMIT_BODY"
        ./scripts/deploy_text.sh "$PREV_COMMIT_DATE" "$COMMIT_DATE"
        echo ""

        # Get the next range of commits by increasing 'PREV_COMMIT_DATE'.
        PREV_COMMIT_DATE="$COMMIT_DATE"
    done
}

main

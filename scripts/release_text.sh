#!/bin/bash
#
# This script lists the commit bodies, commit hash, and full date/time of all parent commits since the last release version tag,
# and runs deploy_text.sh for each commit.
#
# Usage: ~/braze-docs/scripts/release_text.sh

# TODO: everything is working, but the dates being used for both release + deploy scripts are based off of creation date (or some other date)
# instead of using the merge date. So Deploy - May 28, 2024 only returns the following:
# - [#7411](https://github.com/braze-inc/braze-docs/pull/7411) - May 28, 2024 release notes
# 
# rather than the full list found here:
# https://github.com/braze-inc/braze-docs/pull/7419

main() {
    # Ensure the script is executed from the root of the git repository
    cd "$PROJECT_ROOT"

    # Get the last release version tag
    LAST_RELEASE_TAG=$(git describe --tags $(git rev-list --tags --max-count=1 --tags="v.*"))

    # Get the timestamp of the last release tag
    LAST_RELEASE_TIMESTAMP=$(git log -1 --pretty=format:"%cI" "$LAST_RELEASE_TAG")

    echo "Last release timestamp: $LAST_RELEASE_TIMESTAMP"

    # Convert Git logs to JSON and sort by date
    COMMIT_LOGS=$(git log --merges --first-parent --since="$LAST_RELEASE_TIMESTAMP" origin/master --pretty=format:'{%n  "commit": "%H",%n  "date": "%cI",%n  "title": "%s",%n  "body": "%b"%n},' | perl -pe 'BEGIN{print "["}; END{print "]\n"}' | perl -pe 's/},]/}]/' | jq -c '. | sort_by(.date)')

    if [ -z "$COMMIT_LOGS" ]; then
        echo "No commit logs found. Exiting."
        exit 1
    fi

    echo "Commit bodies since the last release timestamp on origin/master:"

    # Initialize the previous commit date with the release timestamp
    PREV_COMMIT_DATE="$LAST_RELEASE_TIMESTAMP"

    # Iterate over the commit logs and run deploy_text.sh for each commit
    echo "$COMMIT_LOGS" | jq -c '.[]' | while read commit; do
        COMMIT_HASH=$(echo "$commit" | jq -r '.commit')
        COMMIT_DATE=$(echo "$commit" | jq -r '.date')
        COMMIT_TITLE=$(echo "$commit" | jq -r '.title')
        COMMIT_BODY=$(echo "$commit" | jq -r '.body')

        echo "Commit: $COMMIT_HASH"
        echo "Title: $COMMIT_TITLE"
        echo "Body: $COMMIT_BODY"
        echo "Processing commits from $PREV_COMMIT_DATE to $COMMIT_DATE"

        ./scripts/deploy_text.sh "$PREV_COMMIT_DATE" "$COMMIT_DATE"
        echo ""

        # Update the previous commit date
        PREV_COMMIT_DATE="$COMMIT_DATE"
    done
}

main

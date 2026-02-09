#!/bin/bash
#
# Lists the commit bodies, commit hash, and full date/time of all parent commits
# since the last release version tag, and runs deploy_text.sh for each commit.
#
# Usage: ./bdocs release

main() {
    # Run script from the root of the git repository.
    cd "$PROJECT_ROOT"

    # Get the last release version tag.
    LAST_RELEASE_TAG=$(git describe --tags $(git rev-list --tags --max-count=1 --tags="v.*"))

    # Get the timestamp of the last release tag.
    LAST_RELEASE_TIMESTAMP=$(git log -1 --pretty=format:"%cI" "$LAST_RELEASE_TAG")

    # Convert Git logs to JSON and sort by date.
    COMMIT_LOGS=$(
      git log --merges --first-parent --since="$LAST_RELEASE_TIMESTAMP" "origin/$PRIMARY_BRANCH" \
        --pretty=format:'%H%x00%cI%x00%s%x00%b%x1e' |
      jq -R -s '
        (split("\u001e") | .[:-1])
        | map(split("\u0000"))
        | map({commit: .[0], date: .[1], title: .[2], body: .[3]})
        | sort_by(.date)
      '
    )

    # Remove the first entry from the commit logs. It's from the last release.
    COMMIT_LOGS=$(echo "$COMMIT_LOGS" | jq '.[1:]')

    # Initialize the previous commit date with the release timestamp.
    PREV_COMMIT_DATE="$LAST_RELEASE_TIMESTAMP"

    # macOS/BSD 'date' parsing for %cI timestamps.
    format_iso_to_header_date() {
      local iso="$1"
      local fixed_tz
      fixed_tz=$(printf "%s" "$iso" | sed -E 's/([+-][0-9]{2}):([0-9]{2})$/\1\2/')
      LC_ALL=C date -j -f "%Y-%m-%dT%H:%M:%S%z" "$fixed_tz" "+%B %-d, %Y"
    }
    
    # Iterate over the commit logs and run 'deploy_text.sh' for each commit.
    echo "$COMMIT_LOGS" | jq -c '.[]' | while read commit; do

        # Pull variables from 'COMMIT_LOGS'.
        COMMIT_HASH=$(echo "$commit" | jq -r '.commit')
        COMMIT_DATE=$(echo "$commit" | jq -r '.date')
        COMMIT_TITLE=$(echo "$commit" | jq -r '.title')
        COMMIT_BODY=$(echo "$commit" | jq -r '.body')

        # Header: "Deploy - MONTH DAY, YEAR"
        DEPLOY_DATE=$(format_iso_to_header_date "$COMMIT_DATE")
        echo "## Deploy - $DEPLOY_DATE"

        # Print the deploy text for each deployment using the sourced DEPLOY.
        "$DEPLOY" "$PREV_COMMIT_DATE" "$COMMIT_DATE"
        echo ""

        # Get the next range of commits by increasing 'PREV_COMMIT_DATE'.
        PREV_COMMIT_DATE="$COMMIT_DATE"
    done
}

main

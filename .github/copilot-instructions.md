<!-- Work in progress. 
Style Guide: https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.uxt7nb8nvq43
-->

# General Instructions

These instructions are for contributors using GitHub Copilot to draft or edit documentation for Braze.

## Pull request titles

The title of the pull request should always match the corresponding issue title, which includes the pre-pended ticket number in the title as `[BD-NUMBER]` where `NUMBER` is the Jira ticket number listed in the corresponding issue. For example:

- **Issue:** `[BD-5016]:Update behaviour on link shortening when used with universal link`
- **PR Title:** `[BD-5016]:Update behaviour on link shortening when used with universal link`

## Pull request body

The pull request body should always use the [PULL_REQUEST_TEMPLATE](./PULL_REQUEST_TEMPLATE) as a base and add/edit the relevant sections in the template as needed. Specifically the Jira ticket number should always be linked using the following syntax:

```
- [BD-NUMBER](https://jira.braze.com/browse/BD-NUMBER)
```

## Voice and Tone

Our brand voice is smart, conversational, and direct. We are a human voice in a world of tech buzzwords; we provide clarity and guidance to anyone interested in the craft of customer engagement.

Clearly structure your writing and make it easy for people to find the information they need. To align on this brand voice in our writing and editing, use these guidelines:

- Explain complicated things simply.
- Be concise.
- Use consistent language for features and actions.

## What Not To Do

When describing Braze products and features, avoid the following:

1. References to future features, or suggestions that something may be supported in the future.
2. Using definitive terms such as "guarantee" or "ensure." Instead, use forward-looking statements like "designed to" or "intended to" to accurately convey the product's capabilities and intentions.
3. Using words and phrases that anchor your writing to a point in time, as they make content become quickly outdated. Focus on how the product works right now, not on what has changed (except for time-focused content, such as in release notes).
4. Specifically avoid the following words and phrases, as they make documentation less clear or more likely to become outdated:
   - as of this writing
   - currently
   - does not yet
   - eventually
   - future
   - in the future
   - latest
   - new
   - newer
   - now
   - old
   - older
   - presently
   - at present
   - soon

## Examples

- ❌ Incorrect: "This feature will be available in the future."
- ✅ Correct: "This feature is not supported."

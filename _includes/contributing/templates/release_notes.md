{% details Show template %}
{% raw %}
`````markdown
---
nav_title: ARTICLE_TITLE
description: "This article contains release notes for DATE."
page_order: ORDER_NUMBER
page_type: reference
---

<!-- The title should include the date the release note is made live. For example, "February 21, 2024 release". -->
# MONTH DAY, YEAR release

<!-- Fill out the following six sections ("Data & Reporting," "BrazeAI<sup>TM</sup>" "Orchestration," "Channels & Touchpoints", “Partnerships”, and “SDK”) using the example section under the next HTML comment. -->
## Data & Reporting

<!-- An example release note title specific to the “Data & Reporting” section. -->
### RELEASE_NOTE_TITLE

<!-- An “Early access” label for this release note. Add labels for “Early access”, “General availability”, and “Beta” beneath release note titles where relevant. -->
{% multi_lang_include release_type.md release="Early access" %}

<!-- You may add includes, images, and links as needed. -->
CONTENT.

### RELEASE_NOTE_TITLE

{% multi_lang_include release_type.md release="General availability" %}

CONTENT.

### RELEASE_NOTE_TITLE

{% multi_lang_include release_type.md release="Beta" %}

## BrazeAI<sup>TM</sup>

### RELEASE_NOTE_TITLE

CONTENT.

## Orchestration

### RELEASE_NOTE_TITLE

CONTENT.

## Channels & Touchpoints

### RELEASE_NOTE_TITLE

CONTENT.

<!-- Use this section to highlight new Braze partnerships by including an overview of each integration and a link to the related partner page on Braze Docs. -->
## Partnerships

### PARTNER_NAME - PARTNER_CATEGORY

CONTENT.

### PARTNER_NAME - PARTNER_CATEGORY

CONTENT.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
## SDK

CONTENT.

### SDK breaking updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [SDK_NAME](LINK_TO_GITHUB_CHANGELOG)
    - OPTIONAL_CONTEXT.
- [SDK_NAME](LINK_TO_GITHUB_CHANGELOG)
- [SDK_NAME](LINK_TO_GITHUB_CHANGELOG)

`````
{% endraw %}
{% enddetails %}
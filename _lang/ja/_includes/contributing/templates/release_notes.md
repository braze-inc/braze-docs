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

<!-- Fill out the following four sections ("Data flexibility," "Unlocking creativity," "Robust channels," and "AI and ML automation") using the example section under the next HTML comment. -->
## Data flexibility

CONTENT.

## Unlocking creativity

CONTENT.

## Robust channels

CONTENT.

## AI and ML automation

CONTENT.

<!-- An example section containing "Release type" includes for each section. You may add addtional sections, subsections, includes, images, and links as needed. -->
## SECTION_TITLE

CONTENT.

### SUBSECTION_TITLE

{% multi_lang_include release_type.md release="Early access" %}

CONTENT.

### SUBSECTION_TITLE

{% multi_lang_include release_type.md release="General availability" %}

CONTENT.

### SUBSECTION_TITLE

{% multi_lang_include release_type.md release="Beta" %}

CONTENT.

### SUBSECTION_TITLE

CONTENT.

<!-- Use this section to highlight new Braze parternships by including an overview of each integration and a link to the related partner page on Braze Docs. -->
## New Braze partnerships

### PARTNER_NAME

CONTENT.

### PARTNER_NAME

CONTENT.

<!-- Use this section list any new SDKs or SDK updates that are already released. -->
## SDK updates

The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.

- [SDK_NAME](LINK_TO_GITHUB_CHANGELOG)
    - OPTIONAL_CONTEXT.
- [SDK_NAME](LINK_TO_GITHUB_CHANGELOG)
- [SDK_NAME](LINK_TO_GITHUB_CHANGELOG)
`````
{% endraw %}
{% enddetails %}
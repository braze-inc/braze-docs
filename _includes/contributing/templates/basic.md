### Basic

You can use this template to create any page or section for Braze Docs. For an example, see [Generating a preview]({{site.baseurl}}/contributing/generating_a_preview/).

{% details Show template %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
---

<!-- The title of your page, used to render the in-page title. -->
# ARTICLE_TITLE

<!-- The description starts with a '>' character and contains an overview of what will be covered. Optionally, in a following paragraph, you can contextualize the topic at a high-level. -->
> DESCRIPTION.

OPTIONAL_CONTEXT.

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Prerequisites

Before you start, you'll need to complete the following:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- An example section. You may add subsections, images, and links as needed. -->
## SECTION_TITLE

CONTENT.

<!-- An example section with subsections. You may add addtional subsections, images, and links as needed. -->
## SECTION_TITLE

### Step 1: ACTION_TO_COMPLETE

CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.
`````
{% endraw %}
{% enddetails %}
---
nav_title: Content Types
article: Content Types
page_order: 4
---

# Content types

> Braze Docs follows the [Diátaxis framework](https://diataxis.fr/), which organizes pages into one of four content types, each one meeting a different learning objective. While a single page on Braze Docs may contain multiple content types, each type should get a dedicated section on the page.

These are the content types you'll find on Braze Docs:

| Documentation type | Purpose |
| --- | --- |
| [How-to guides](#how-to-guides) | Help the user **apply knowledge**. |
| [Tutorials](#tutorials) | Help the user **acquire knowledge**. |
| [References](#references) | Provide the user with **technical knowledge**. |
| [Explanations](#explanations) | Broaden the user’s **contextual knowledge**. |
| [Release notes](#release-notes) | $TODO: Add a description here. |

## Using templates

Each content type has a dedicated template you can use to create [pages]({{site.baseurl}}/contributing/content_management/pages/) or [sections]({{site.baseurl}}/contributing/content_management/sections/) on Braze Docs.

Read HTML comments like the following to learn more about each section in a template:

```markdown
<!-- Here's an HTML comment! -->
```

{% alert important %}
You can keep these comments in your file while writing, but you'll need to remove them before publishing.
{% endalert %}

## Content types

### How-to guides

How-to guides are action-based, chronological steps that show users how to complete a specific task. For an example, see [Creating a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/):

![Screenshot of the "Creating a Content Card" page.]()

{% details Show template %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
—--
<!-- The overview starts with a '>' character and discusses what will be covered. In an optional following paragraph, contextualize the topic at a high-level in an introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Prerequisites

Before you start, you'll need to complete the following:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- An optional, brief explanation of how the feature workflow looks. -->
## How it works

CONTENT.

<!-- A how-to guide with nested steps. -->
## TASK_TO_COMPLETE

<!-- Optional overview of the task. -->
CONTENT.

<!-- Action-oriented header that describes the step’s goal. -->
### Step 1: ACTION_TO_COMPLETE

<!-- Use number bullets or paragraphs to describe how to complete this action -->
CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.
<!-- Optional references, such as supported data types, fields, definitions, and similar. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- For optional steps, add “(optional)” to the end of the header. -->
### Step 3: OPTIONAL_ACTION_TO_COMPLETE (optional)

CONTENT.
<!-- An optional section for what is supported. Add nested headers to be more specific. -->
## Supported data types / Supported attributes / Supported events / Supported ETC.
CONTENT.
``````
{% endraw %}
{% enddetails %}

#### Guidelines

- Cover only what the user needs to know to take action. 
- Only cover the best or recommended way to complete the task. Do not give document alternative methods.
- Only include [reference material](#references) that's vital to the end-user's goal, such as a list of options a user can select during a step.
- Link out to references that are longer than reasonable to include in the same article, such as [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
- Avoid providing troubleshooting steps. Instead, you can include this information in a another section on this page or a separate article.

#### Header syntax

H2 headers (`##` in Markdown) should be action-oriented and reflect the general goal for this step. If there's any optional steps, prepend `(Optional)` to  For example:

{% raw %}
```
## Creating a page

1. Open the relevant directory in `braze-docs`.
2. Create a new Markdown file for your page.
3. Ensure your filename follows our [naming guidelines](#naming-guidelines).
4. (Optional) You can generate a preview by running `rake` in your terminal.
```
{% endraw %}

For long or complicated steps, use nested headers to group related steps. If there's any optional steps, append `(optional)` to the header. For example:

{% raw %}
``````markdown
## Creating a page

### Step 1: Create a new file

Open the relevant directory, then create a new Markdown file for your page.

```plaintext
PAGE_TITLE.md
```

### Step 2: Add a template

Copy and paste one of the following templates into your Markdown file. For more information, see [Templates]({{site.baseurl}}/contributing/templates/).

### Step 3: Generate a preview (optional)

To generate a preview, open your terminal and run the following command:

```bash
rake
```
``````
{% endraw %}

### Tutorials

Tutorials are learning-oriented practical lessons. They focus on what the user learns, such as becoming familiar with terminology, how things interact, how to use commands, and similar.

Examples include:
- [Rules-based recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/rules_based_recommendations/)
- [Assigning Liquid variables]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)

#### Guidelines

Create a guided step-by-step activity that leads to a successful conclusion. In other words, a scenario for the user to follow or roleplay. Assume that the user has little to no familiarity with the platforms, tools, or workflows used during the activity.

Introduce the tutorial with the following format:

```markdown
When you’re finished with this tutorial, you’ll be able to:

- LEARNING_OBJECTIVE
- LEARNING_OBJECTIVE
- LEARNING_OBJECTIVE
```

Replace each `LEARNING_OBJECTIVE` with something the user will broadly learn how to do during the tutorial. For example, a tutorial that walks a user through creating their first contribution to the Braze Docs site might have the following objectives:

```markdown
- Navigate the Braze Docs GitHub repository
- Make changes using the GitHub website or your local environment
- Create pull requests (PRs)
- Preview your changes in a test site
- Request a review from the Braze Docs team
```

##### Headers and bullet points

Follow the same header and bullet point format as [how-to guides](#content-guidelines), but add "Tutorial:" to the beginning of the H2 header. For example, "Tutorial: Your first contribution". 

{% alert tip %}
Provide ready-made assets for the user to input that aren't the key focus of your tutorial. For example, you could provide photos, messaging, and Liquid coding for a tutorial that teaches users how to use a variety of features when creating a campaign.
{% endalert %}

### References

References are information-oriented content. They focus on providing the user with objective, authoritative, and technical knowledge.

Examples include:
- [Message engagement events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) (events glossary)
- [App-by-app user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#app-by-app-user-permissions)
- [Liquid terms to know]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) (definition glossary)

#### Guidelines

Create technical descriptions or information that are necessary to complete a task. Try to organize the information alphabetically, categorically, or hierarchically.

Put references in their respective articles unless they're longer than seems appropriate for a single article or will be referenced by multiple articles. If they're only referenced by a single how-to guide and long enough to disrupt the flow of the steps, you can [make them collapsible]({{site.baseurl}}/contributing/styling_examples/#collapsible-content).

##### Headers

Use Heading 2 (`##`) and nouns for reference names. For example, [Editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) has the following names for its references:

```markdown
- Types
- Properties
    - Title
    - Paragraph
    - List
    - Button
    - Divider
    - Spacer
    - Image
    - Video
    - Social
    - Icons
    - HTML
    - Menu
```

### Explanations

Explanations are understanding-oriented content. They focus on improving the user’s conceptual understanding.

Examples include:
- [Getting started: Braze overview]({{site.baseurl}}/user_guide/getting_started/overview/)
- [Integration overview]({{site.baseurl}}/developer_guide/platform_wide/getting_started/integration_overview/)
- [Braze data retention information]({{site.baseurl}}/api/data_retention/)

#### Guidelines

Create textual or visual descriptions of concepts, such as how data travels between features, third-party partners, tools, and similar. You can also discuss how features and techniques can benefit users.

Explanations should reside in the most relevent article. For example, a basic feature article might have an explanation called "How it works" that describes that feature's workflow. If an explanation is too broad to fit into only one article, it might fit best in a landing page for a general topic, such as [Campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns) or [Personalized messaging]({{site.baseurl}}/user_guide/personalization_and_dynamic_content).

{% alert tip %}
Even though explanations aren't telling users what to do to achieve a specific outcome, you can broadly describe chronological steps to acheive a general goal (such as using A/B testing to improve your messaging). Don't go into the same detail you would for a [how-to guide](#how-to-guides) or [tutorial](#tutorials).
{% endalert %}

##### Headers

Explanation articles use the heading convention "About TOPIC_NAME."

Examples include:
- [About sanitiation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization#about-sanitization)
- [About content management]({{site.baseurl}}/contributing/content_management)

Explanation sections within articles that contain multiple documentation types (such as an article that contains a how-to guide and references) have more leeway with header conventions. We suggest using verbiage that implies an explanation rather than instructions, similar to these:

- About TOPIC_NAME
- TOPIC_NAME overview
- How TOPIC works
- How TOPIC is handled
- What does Braze check?

### Release notes

$TODO: Add a description here.

{% multi_lang_include contributing/templates/release_notes.md %}

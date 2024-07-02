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
| [Release notes](#release-notes) | Inform the user about product updates. |

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

![Screenshot of the "Creating a Content Card" page.]({% image_buster /assets/img/contributing/content_types/how_to_guide_example.png %})

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

# ARTICLE_TITLE

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

H2 headers (`##` in Markdown) should be action-oriented and reflect the general goal for this step. If there's any optional steps, prepend `(Optional)` to the header. For example:

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

Tutorials are learning-oriented practical lessons. They focus on what the user learns, such as becoming familiar with terminology, how things interact, how to use commands, and similar. For an example, see [Rules-based recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/rules_based_recommendations/):

![Screenshot of the "Rules-based recommendations page.]({% image_buster /assets/img/contributing/content_types/tutorial_example.png %})

{% details Show template %}
{% raw %}
```markdown
---
nav_title: NAV_TITLE
article_title: Tutorial: WHAT_THE_USER_WILL_DO
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: tutorial
layout: OPTIONAL_LAYOUT_FILE
—--

# Tutorial: WHAT_THE_USER_WILL_DO

<!-- The overview starts with a '>' character and discusses what will be covered. In an optional following paragraph, contextualize the topic at a high-level in an introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- Introduce the tutorial with the following format:-->
When you’re finished with this tutorial, you’ll be able to:

- LEARNING_OBJECTIVE
- LEARNING_OBJECTIVE
- LEARNING_OBJECTIVE

<!-- Replace each `LEARNING_OBJECTIVE` with something the user will broadly learn how to do during the tutorial. For example, a tutorial that walks a user through creating their first contribution to the Braze Docs site might have the following objectives:-->

- Navigate the Braze Docs GitHub repository
- Make changes using the GitHub website or your local environment
- Create pull requests (PRs)
- Preview your changes in a test site
- Request a review from the Braze Docs team
```
{% endraw %}
{% enddetails %}

#### Guidelines

- Create a guided step-by-step activity or scenario for the user to follow or roleplay. 
- Assume that the user has little to no familiarity with the platforms, tools, or workflows used during the activity.

{% alert tip %}
Provide ready-made assets for the user to input that aren't the key focus of your tutorial. For example, you could provide photos, messaging, and Liquid coding for a tutorial that teaches users how to use a variety of features when creating a campaign.
{% endalert %}

##### Header syntax

The title header should be prepended with `Tutorial:` and generally describe what the user will do or create. For example, "Tutorial: Your first contribution". 

### References

References are information-oriented content. They focus on providing the user with objective, authoritative, and technical knowledge. For an example, see [Message engagement events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) (events glossary).

![Screenshot of the "Message engagement events" page.]({% image_buster /assets/img/contributing/content_types/reference_example.png %})

{% details Show template %}
{% raw %}
```markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
—--

# ARTICLE_TITLE

<!-- The overview starts with a '>' character and discusses what will be covered. In an optional following paragraph, contextualize the topic at a high-level in an introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- An optional section for organizing the page. -->
## SECTION_NAME

CONTENT.

<!-- An optional section for organizing the page. -->
## SECTION_NAME

CONTENT.
```
{% endraw %}
{% enddetails %}

#### Guidelines

- Create technical descriptions or information that are necessary to complete a task.
- Organize the information alphabetically, categorically, or hierarchically.
- Put references in their respective articles unless they're longer than seems appropriate for a single article or will be referenced by multiple articles. 
    - If they're only referenced by a single how-to guide and long enough to disrupt the flow of the steps, you can [make them collapsible]({{site.baseurl}}/contributing/styling_examples/#collapsible-content).

##### Header syntax

Topmost should be nouns. For example, [Editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) has the following names for its references:

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

Explanations are understanding-oriented content. They focus on improving the user’s conceptual understanding. For an example, see [Getting started: Braze overview]({{site.baseurl}}/user_guide/getting_started/overview/).

![Screenshot of the "Getting started: Braze overview" page.]({% image_buster /assets/img/contributing/content_types/explanation_example.png %})

{% details Show template %}
{% raw %}
```markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
—--

# ARTICLE_TITLE

<!-- The overview starts with a '>' character and discusses what will be covered. In an optional following paragraph, contextualize the topic at a high-level in an introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- An optional section for organizing the page. -->
## SECTION_NAME

CONTENT.

<!-- An optional section for organizing the page. -->
## SECTION_NAME

CONTENT.
```
{% endraw %}
{% enddetails %}

#### Guidelines

- Create textual or visual descriptions of concepts, such as how data travels between features, third-party partners, tools, and similar.
- Discuss how features and techniques can benefit users.
- Place explanations in the most relevent article. For example, a basic feature article might have an explanation called "How it works" that describes that feature's workflow. 
- Consider placing explanations that are too broad to fit into only one article onto a landing page for a general topic, such as [Campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns).

{% alert tip %}
Even though explanations aren't telling users what to do to achieve a specific outcome, you can broadly describe chronological steps to acheive a general goal (such as using A/B testing to improve your messaging). Don't go into the same detail you would for a [how-to guide](#how-to-guides) or [tutorial](#tutorials).
{% endalert %}

##### Headers

Topmost headers are formatted as "About TOPIC_NAME." For examples see, [About sanitiation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization#about-sanitization) and [About content management]({{site.baseurl}}/contributing/content_management).

Explanation sections within articles that contain multiple documentation types (such as an article that contains a how-to guide and references) have more leeway with header conventions. We suggest using verbiage that implies an explanation rather than instructions, similar to these:

- About TOPIC_NAME
- TOPIC_NAME overview
- How TOPIC works
- How TOPIC is handled
- What does Braze check?

### Release notes

Release notes are a monthly compilation of product updates in Braze. Each update is placed under one of the below categories:

- Data flexibility
- Unlocking creativity
- Robust channels
- AI and ML automation
- New Braze partnerships
- SDK updates

{% multi_lang_include contributing/templates/release_notes.md %}

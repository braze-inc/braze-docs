---
nav_title: Content Types
article: Content Types
page_order: 4
toc_headers: h2
---

# Content types

> Braze Docs follows the [Diátaxis framework](https://diataxis.fr/), which organizes pages into one of four content types, each one meeting a different learning objective. While a single page on Braze Docs may contain multiple content types, each type should get a dedicated section on the page.

These are the four content types you'll find on Braze Docs:

| Documentation type | Purpose |
| --- | --- |
| [How-to guides](#how-to-guides) | Help the user **apply knowledge**. |
| [Tutorials](#tutorials) | Help the user **acquire knowledge**. |
| [References](#references) | Provide the user with **technical knowledge**. |
| [Explanations](#explanations) | Broaden the user’s **contextual knowledge**. |

Check out [Page templates](#page-templates) for how to structure multiple content types on the following page types:
- [Basic articles](#basic)
- [Technology partner documentation](#technology-partner)
- [Release notes](#release-notes)

## How-to guides

How-to guides are action-based, chronological steps that show users how to complete a specific task.

Examples include:
- [Creating a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
- [WhatsApp setup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)
- [Connected sources integration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/)

{% details Template %}
{% raw %}
```markdown
<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Prerequisites

Before you start, you'll need to complete the following:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- An optional, brief explanation of how the feature workflow looks. -->
## How it works

CONTENT.

<!-- Walk a user through integrating and turning on the feature. -->
 ## Integration
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
```
{% endraw %}
{% enddetails %}

### Guidelines

The how-to guide should cover the "happy path" to the goal, which assumes the best case scenario while completing the task. Avoid providing troubleshooting information, which you can include in a separate reference section or article.

To keep the guide concise and relevant to the user's needs, follow these additional guidelines: 

- Cover only what the user needs to know to take action. 
- Only include [references](#references) (technical, non-action based information) that are vital to reaching their goal, such as a list of the options a user can select from during a step. 
- Link out to references that are longer than reasonable to include in the same article, such as [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

#### Headers

H2 headings (`##`) should be action-oriented and reflect the general goal for this step.

```
## Creating a page

Open the relevant directory, then create a new Markdown file for your page.
```

For how-tos with long or complicated steps, use nested headers to group related steps as shown in the following Markdown sample. For short steps, see [Ordered lists](#ordered-lists) instead.

{% details Example %}
{% raw %}
```markdown
## Creating a page
### Step 1: Create a new file

Open the relevant directory, then create a new Markdown file for your page.

PAGE_TITLE.md

Replace `PAGE_TITLE` with the title of your page, which should follow the Braze Docs Style Guide. Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). Your filename should be similar to the following:

- **Page title:** Setting up your development environment for C++
- **File name:** `setting_up_your_development_environment_for_cpp.md`

### Step 2: Add a template

Copy and paste one of the following templates into your Markdown file. For more information, see [Templates]({{site.baseurl}}/contributing/templates/).

#### Basic template
```
{% endraw %}
{% enddetails %}

For optional steps, put “(optional)” at the end of a header, such as:

{% raw %}
```markdown
Step 4: Add additional content (optional)
```
{% endraw %}

#### Ordered lists

For how-tos with short and straightforward steps, use an ordered list in Markdown format.

For optional steps, put “(Optional)” at the start of the bulleted number, such as: 

{% raw %}
```markdown
5. (optional) Deselect any files you do not wish to import
```
{% endraw %}

If the steps can’t be summarized in concise numbered bullets, consider using nested headers (see “Headers”) to create a more visually-friendly format for users

## Tutorials

Tutorials are learning-oriented practical lessons. They focus on what the user learns, such as becoming familiar with terminology, how things interact, how to use commands, and similar.

Examples include:
- [Rules-based recommendations]({{site.baseurl}}/user_guide/sage_ai/recommendations/rules_based_recommendations/)
- [Assigning Liquid variables]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)

### Guidelines

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

#### Headers and bullet points

Follow the same header and bullet point format as [how-to guides](#content-guidelines), but add "Tutorial:" to the beginning of the H2 header. For example, "Tutorial: Your first contribution". 

{% alert tip %}
Provide ready-made assets for the user to input that aren't the key focus of your tutorial. For example, you could provide photos, messaging, and Liquid coding for a tutorial that teaches users how to use a variety of features when creating a campaign.
{% endalert %}

## References

References are information-oriented content. They focus on providing the user with objective, authoritative, and technical knowledge.

Examples include:
- [Message engagement events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) (events glossary)
- [App-by-app user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#app-by-app-user-permissions)
- [Liquid terms to know]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) (definition glossary)

### Guidelines

Create technical descriptions or information that are necessary to complete a task. Try to organize the information alphabetically, categorically, or hierarchically.

Put references in their respective articles unless they're longer than seems appropriate for a single article or will be referenced by multiple articles. If they're only referenced by a single how-to guide and long enough to disrupt the flow of the steps, you can [make them collapsible]({{site.baseurl}}/contributing/styling_examples/#collapsible-content).

#### Headers

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

#### Use cases 

To demonstrate how a specific industry can use a feature, create a use case. It uses fictional companies to demonstrate how a feature can be used in a specific situation. For example, a use case can cover how a FakeBrandz company could use Canvas boards to retarget users who abandoned carts containing more than three items.

Use dashboard-06 to access FakeBrandz workspaces. Make sure to use practical real-world examples that align with how different industries use features. Use the header format "Use case" for singular use cases. If including multiple use cases, nest them beneath "Use case" and give each use case a descriptive header.

## Explanations

Explanations are understanding-oriented content. They focus on improving the user’s conceptual understanding.

Examples include:
- [Getting started: Braze overview]({{site.baseurl}}/user_guide/getting_started/overview/)
- [Integration overview]({{site.baseurl}}/developer_guide/platform_wide/getting_started/integration_overview/)
- [Braze data retention information]({{site.baseurl}}/api/data_retention/)

### Guidelines

Create textual or visual descriptions of concepts, such as how data travels between features, third-party partners, tools, and similar. You can also discuss how features and techniques can benefit users.

Explanations should reside in the most relevent article. For example, a basic feature article might have an explanation called "How it works" that describes that feature's workflow. If an explanation is too broad to fit into only one article, it might fit best in a landing page for a general topic, such as [Campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns) or [Personalized messaging]({{site.baseurl}}/user_guide/personalization_and_dynamic_content).

{% alert tip %}
Even though explanations aren't telling users what to do to achieve a specific outcome, you can broadly describe chronological steps to acheive a general goal (such as using A/B testing to improve your messaging). Don't go into the same detail you would for a [how-to guide](#how-to-guides) or [tutorial](#tutorials).
{% endalert %}

#### Headers

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

## Page templates

You can use these templates to create [pages]({{site.baseurl}}/contributing/content_management/pages/) or [sections]({{site.baseurl}}/contributing/content_management/sections/) on Braze Docs.

Read HTML comments like the following to learn more about each section in a template:

```markdown
<!-- Here's an HTML comment! -->
```

{% alert important %}
You can keep these comments in your file while writing, but you'll need to remove them before publishing.
{% endalert %}

### Basic

{% multi_lang_include contributing/templates/basic.md %}

### Technology partner

{% multi_lang_include contributing/templates/technology_partner.md %}

### Release notes

{% multi_lang_include contributing/templates/release_notes.md %}

### Modifying a template

You can modify a template by following the steps outlined in these pages:

- [Content management]({{site.baseurl}}/contributing/content_management/)
- [Metadata]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)
- [Page layouts]({{site.baseurl}}/contributing/yaml_front_matter/page_layouts/)
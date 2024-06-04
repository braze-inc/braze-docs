---
nav_title: Page Types
article: Page Types
page_order: 4
toc_headers: h2
---

# Page types

Braze documentation should follow the Diátaxis framework, which organizes documentation into four categories, or types, that each corresponds with a distinct need or learning preference. Each Braze article can contain multiple documentation types, though each type should reside in its own section.

| Documentation type | Purpose |
| --- | --- |
| [How-to guides](#how-to-guides) | Help the user **apply knowledge**. |
| [Tutorials](#tutorials) | Help the user **acquire knowledge**. |
| [References](#references) | Provide the user with **technical knowledge**. |
| [Explanations](#explanations) | Broaden the user’s **contextual knowledge**. |

## How-to guides

How-to guides are action-based and chronological steps. They focus on telling a user how to achieve a specific and successful result.

Examples include:
- [Creating a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
- [WhatsApp setup]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)
- [Connected sources integration]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/)

### Content guidelines

Cover only what the user needs to know to take action. Only include [references](#references) (technical, non-action based information) that are vital to reaching their goal, such as a list of the options a user can select from during a step. Link out to references that are longer than reasonable to include in the same article, such as [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

The how-to guide should cover the "happy path" to the goal, which assumes the best case scenario while completing the task. Avoid providing troubleshooting information, which you can include in a separate reference section or article.

#### Headers

Use Heading 2 and action-oriented language for the primary how-to name, such as "Creating a page".

For how-tos with long or complicated steps, use nested headers to group related steps like so:

{% raw %}
```markdown
[H2] Creating a page
[H3] Step 1: Create a new file

Open the relevant directory, then create a new Markdown file for your page.

PAGE_TITLE.md

Replace `PAGE_TITLE` with the title of your page, which should follow the Braze Docs Style Guide. Use all lowercase characters, remove special characters, and replace spaces with underscores (`_`). Your filename should be similar to the following:

- **Page title:** Setting up your development environment for C++
- **File name:** `setting_up_your_development_environment_for_cpp.md`

[H3] Step 2: Add a template

Copy and paste one of the following templates into your Markdown file. For more information, see [Templates]({{site.baseurl}}/contributing/templates/).

[H4] Basic template
```
{% endraw %}

For optional steps, put “(optional)” at the end of a header, such as:

{% raw %}
```markdown
Step 4: Add additional content (optional)
```
{% endraw %}

#### Bullet points

For how-tos with short and straightfoward steps, use numbered bullets below headers like so:

{% raw %}
```markdown
[H3] Where can I find it?

You can find your campaign ID one of two ways:

1. Go to **Messaging** > **Campaigns** and select a pre-existing campaign. If the campaign you want does not exist yet, create one and save it. At the bottom of the individual campaign page, you will be able to find your **Campaign API Identifier**.

2. Go to **Settings** > **APIs and Identifiers**. Here, Braze offers an **Additional API Identifiers** search where you can look up specific identifiers.
```
{% endraw %}

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

### Content guidelines

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

### Content guidelines

Create technical descriptions or information that are necessary to complete a task. Try to organize the information alphabetically, categorically, or hierarchically.

Put references in their respective articles unless they're longer than seems appropriate for a single article or will be referenced by multiple articles. If they're only referenced by a single how-to guide and long enough to disrupt the flow of the steps, you can [make them collapsible]({{site.baseurl}}/contributing/styling_examples/#collapsible-content).

#### Headers

Use Heading 2 and nouns for reference names. For example, [Editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) has the following names for its references:

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

### Content guidelines

Create textual or visual descriptions of concepts, such as how data travels between features, third-party partners, tools, and similar. You can also discuss how features and techniques can benefit users.

Explanations should reside in the most relevent article. For example, a basic feature article might have an explanation called "How it works" that describes that feature's workflow. If an explanation is too broad to fit into only one article, it might fit best in a landing page for a general topic, such as [Campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns) or [Personalized messaging]({{site.baseurl}}/user_guide/personalization_and_dynamic_content).

{% alert tip %}
Even though explanations aren't telling users what to do to achieve a specific outcome, you can broadly describe chronological steps to acheive a general goal (such as using A/B testing to improve your messaging). Don't go into the same detail you would for a [how-to guide](#how-to-guides) or [tutorial](#tutorials).
{% endalert %}
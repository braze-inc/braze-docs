---
nav_title: Content Guidelines
article: Content Guidelines
page_order: 0
---

# Content guidelines for templates

Braze documentation should follow the Diátaxis framework, which organizes documentation into four categories, or types, that each corresponds with a distinct need or learning preference. Each Braze article can contain multiple documentation types, though each type should reside in its own section.

| Documentation type | Purpose |
| --- | --- |
| [How-to guides](#how-to-guides) | Help the user **apply knowledge**. |
| [Tutorials](#tutorials) | Help the user **acquire knowledge**. |
| [References](#references) | Provide the user with **technical knowledge**. |
| [Explanations](#explanations) | Broaden the user’s **contextual knowledge**. |

## How-to guides

How-to guides are goal-oriented directions. They focus on what the user does to achieve a specific result.

Examples include:
- Creating personalized email campaigns
- Setting up SMS link shortening
- Connecting your Shopify store to your Braze account

### Content guidelines

Cover only what the user needs to know to take action. Only include references that are vital to completing the how-to guide, such as listing options to select from during a step. Link out to references that are longer than reasonable to include in the same article, such as [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

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

Copy and paste one of the following templates into your Markdown file. For more information, see [Templates].

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

Tutorials are learning-oriented practical lessons. They focus on what the user learns, such as becoming familiar with terminology, how things interact, commands, and similar.

Examples include:
- Your first WhatsApp campaign
- Optimizing your Canvas flow
- Improving consumer engagement with Braze

### Content guidelines

Create a guided step-by-step activity that leads to a successful conclusion. In other words, a scenario for the user to follow or roleplay. Assume that the user has little to no familiarity with the platforms, tools, or workflows used during the activity.

Follow the same header and bullet point format as [how-to guides](#content-guidelines).

#### Tips

Provide ready-made assets for the user to input that aren't the key focus of your tutorial. For example, you could provide photos, messaging, and Liquid coding for a tutorial that teaches users how to use a variety of features when creating a campaign.

## References

References are information-oriented content. They focus on providing the user with objective, authoritative, and technical knowledge.

### Content guidelines

Place troubleshooting guides into a dedicated section article

#### Use cases 

To demonstrate how a specific industry can use a feature, create a use case. It uses fictional companies to demonstrate how a feature can be used in a specific situation. For example, a use case can cover how a FakeBrandz company could use Canvas boards to retarget users who abandoned carts containing more than three items.

Use dashboard-06 to access FakeBrandz workspaces. Make sure to use practical real-world examples that align with how different industries use features.

## Explanations

Explanations are understanding-oriented content. They focus on improving the user’s conceptual understanding.

### Content guidelines

Describe concepts, such as how data travels between features, third-party partners, tools, and similar. You can also cover how features and techniques can benefit users.
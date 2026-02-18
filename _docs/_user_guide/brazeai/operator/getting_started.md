---
nav_title: Getting Started
article_title: Getting started with BrazeAI Operator<sup>TM</sup>
page_order: 1
description: "Learn how to access and use BrazeAI Operator<sup>TM</sup>, Braze's AI assistant built into the dashboard, including its features and best practices."
---

# Getting started with BrazeAI Operator<sup>TM</sup>

> Learn how to access and use BrazeAI Operator<sup>TM</sup>, your AI assistant built into the dashboard, including its features and best practices.

## How to access Operator

Open Operator from any page in the Braze dashboard.  

1. Select **BrazeAI Operator<sup>TM</sup>**, next to your user profile.

![The BrazeAI Operator icon next to a user profile.]({% image_buster /assets/img/operator/operator_icon.png %})

2. The Operator chat panel will open on the right-hand side of the screen.

![The Operator chat panel.]({% image_buster /assets/img/operator/operator_chat_panel.png %})

{% alert tip %}
Maximize to expand the panel for easier reading, or minimize to keep Operator available while working.  
{% endalert %} 

## How to use Operator

Describe what you are trying to accomplish using natural language. Prompts can range from simple questions to complex requests:

- **Simple:** Why isn't my Liquid rendering?
- **Complex:** How can I make the `abort_message` tag of my message include the user attribute that caused the abort?

Operator can provide step-by-step instructions, links to Braze documentation, and plain-language explanations. Clear and specific questions lead to more helpful responses. 

## Best practices

Treat Operator as a conversation, not a search engine. Short, natural prompts work best.

- **Be specific:** Instead of "Tell me about Canvas", try "How do I use Action Paths in Canvas?".  
- **Ask follow-up questions:** If the first response doesn't address your need, ask for clarification or additional details.
- **Use page-aware context:** Operator understands your location in Braze. Open Operator while viewing the relevant page for the most accurate results.

## Customizing your experience

### Choose the right model

Operator uses [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2) by default, which offers the strongest reasoning and is best suited for complex, multi-step tasks. Lighter models are also available and consume fewer resources against your daily usage limit, making them a good choice for straightforward questions.

<!-- TODO: Replace with confirmed model list once engineering finalizes the set. -->
| Model | Best for | Resource usage |
| --- | --- | --- |
| [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2) (default) | Complex troubleshooting, multi-step workflows, advanced reasoning | Highest |
| _Additional models TBD_ | _Simpler queries, routine questions_ | _Lower_ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

> Add image for GPT model dropdown.

{% alert tip %}
Use a lighter model for straightforward questions to conserve your daily usage. Reserve GPT-5.2 for complex troubleshooting or multi-step tasks.
{% endalert %}

### Apply brand guidelines

Add brand guidelines as context to Operator queries so responses match your brand's voice, tone, and personality. Operator uses the brand guidelines configured in your workspace, which helps ensure consistent messaging when it suggests copy or explains features.

To set up brand guidelines, go to **Settings** > **Brand Guidelines**. For more, see [Brand Guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Selecting brand guidelines in the Operator chat panel.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Leverage page-aware context

Operator automatically understands your location in Braze and tailors responses based on that context. For example, when you open Operator while building a Canvas, it can suggest relevant steps or provide guidance about Canvas features without you having to explain where you are in your workflow.

This context-awareness means you can ask shorter, more natural questions like "How do I add a delay?" instead of "How do I add a delay step in a Canvas workflow?"

## Working with Operator responses

### Get started with suggested prompts

When you open Operator, suggested prompts appear based on common tasks and your current page. Select one to get started quickly, or type your own custom question.

### Understand how Operator thinks

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator arrived at an answer. This is helpful when you want to understand the logic behind a suggestion or verify the approach.

![The collapsed "Reasoned" dropdown in an Operator response.]({% image_buster /assets/img/operator/operator_reasoning_collapsed.png %}){:style="max-width:50%"}

![The expanded "Reasoned" dropdown showing how Operator arrived at an answer.]({% image_buster /assets/img/operator/operator_reasoning_expanded.png %}){:style="max-width:50%"}

### Take suggested actions

In some cases, Operator recommends next steps and provides direct links to relevant pages in the Braze dashboard. For example, if you ask about email bounce rates, Operator may link directly to the **Deliverability Center** page, saving you navigation time.

## Managing your session

### Stop a response

While Operator is generating a response, the **Send** button becomes a **Stop** button. Select **Stop** to end the response early if you realize you need to rephrase your question or if the response is going in the wrong direction.

### Clear your history

To start fresh or remove sensitive information from the conversation, select **Clear chat history**. This removes all current content and resets the conversation context.

### Provide feedback

At the bottom of each response, use the thumbs up or thumbs down buttons to provide quick feedback. Your feedback helps improve Operator's answers over time.

## Next steps

- [Reviewing actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions/) - Learn how to review and approve Operator's proposed changes
- [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) - Common issues and solutions

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

> Add image for Operator icon next to user profile.

2. The Operator chat panel will open on the right-hand side of the screen.

> Add image for Operator chat panel.

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

Select from these GPT models to use for different request types with Operator. Lighter models respond faster and use fewer resources, while more advanced models handle complex tasks better.

- [GPT-5 Nano](https://platform.openai.com/docs/models/gpt-5-nano) - Fastest, best for simple queries
- [GPT-5 Mini](https://platform.openai.com/docs/models/gpt-5-mini) - Quick responses for routine questions
- [GPT-5](https://platform.openai.com/docs/models/gpt-5) - Balanced performance
- [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1) - Better reasoning for complex tasks
- [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2) (default) - Most capable, best for advanced workflows

> Add image for GPT model dropdown.

{% alert tip %}
Use lighter models (Nano or Mini) for straightforward questions to conserve resources. Reserve more powerful models for complex troubleshooting or multi-step tasks.
{% endalert %}

### Apply brand guidelines

Add brand guidelines as context to Operator queries so responses match your brand's voice, tone, and personality. Operator uses the brand guidelines configured in your workspace, which helps ensure consistent messaging when it suggests copy or explains features.

To set up brand guidelines, go to **Settings** > **Brand Guidelines**. For more, see [Brand Guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

> Add image for Operator brand guidelines selection.

### Leverage page-aware context

Operator automatically understands your location in Braze and tailors responses based on that context. For example, when you open Operator while building a Canvas, it can suggest relevant steps or provide guidance about Canvas features without you having to explain where you are in your workflow.

This context-awareness means you can ask shorter, more natural questions like "How do I add a delay?" instead of "How do I add a delay step in a Canvas workflow?"

## Working with Operator responses

### Get started with suggested prompts

When you open Operator, suggested prompts appear based on common tasks and your current page. Select one to get started quickly, or type your own custom question.

### Understand how Operator thinks

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator arrived at an answer. This is helpful when you want to understand the logic behind a suggestion or verify the approach.

> Add image for Operator reasoning dropdown.

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

- [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) - Common issues and solutions

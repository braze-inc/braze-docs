---
nav_title: Getting Started
article_title: Getting started with BrazeAI Operator<sup>TM</sup>
page_order: 1
description: "Learn how to access and use BrazeAI Operator<sup>TM</sup>, Braze's AI assistant built into the dashboard, including its features and best practices."
---

# Getting started with BrazeAI Operator<sup>TM</sup>

> Learn how to access and use BrazeAI Operator<sup>TM</sup>, Braze's AI assistant built into the dashboard, including its features and best practices.

## How to access Operator

Open Operator from any page in the Braze dashboard.  

1. Select **BrazeAI Operator<sup>TM</sup>**, next to the user profile.

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

## Features

### GPT models

Select from these GPT models to use for different request types with Operator. Refer to the linked provider documentation to determine which model best fits your use case.

- [GPT-5 Nano](https://platform.openai.com/docs/models/gpt-5-nano)
- [GPT-5 Mini](https://platform.openai.com/docs/models/gpt-5-mini)
- [GPT-5](https://platform.openai.com/docs/models/gpt-5)
- [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1)
- [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2) (default)

> Add image for GPT model dropdown.

### Page-aware context

Operator understands your location in Braze and tailors responses based on that context. For example, when opened while building a Canvas, Operator can suggest steps or provide guidance relevant to that feature without requiring you to specify it. 

### Brand guidelines

Add brand guidelines as context to Operator queries so responses match the brand's voice, tone, and personality. Operator uses the brand guidelines configured in the workspace.

To set up brand guidelines, go to **Settings** > **Brand Guidelines**. For more, see [Brand Guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

> Add image for Operator brand guidelines selection.

### Suggested prompts

When Operator is opened, suggested prompts appear. Select one or type a custom question.

### Understanding Operator's reasoning

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator arrived at an answer.

> Add image for Operator reasoning dropdown.

### Suggested actions

In some cases, Operator will recommend next steps and provide direct links to relevant pages in the Braze dashboard. For example, if asked about email bounce rates, Operator may link to the **Deliverability Center** page.

### Stopping generation

While Operator is generating a response, the **Send** button becomes a **Stop** button. To end the response early, select **Stop**.

### Clearing chat history

To reset the conversation, select **Clear chat history**. This removes the current content and starts a fresh conversation.

### Sending feedback

At the bottom of each response, use the thumbs up or thumbs down buttons to provide quick feedback. This helps improve Operator's answers.

## Next steps

- [Approval flow]({{site.baseurl}}/user_guide/brazeai/operator/approval_flow/) - Learn how to review and approve Operator's proposed changes
- [Support tickets]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/) - File support tickets directly from Operator
- [Troubleshooting]({{site.baseurl}}/user_guide/brazeai/operator/troubleshooting/) - Common issues and solutions

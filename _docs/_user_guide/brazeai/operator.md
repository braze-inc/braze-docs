---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 8
alias: /operator/
description: "This reference article covers BrazeAI Operator, an AI-powered assistant built into the Braze dashboard."
---

# BrazeAI Operator<sup>TM</sup>

> BrazeAI Operator<sup>TM</sup> is Braze's AI assistant built into the dashboard. Operator helps get things done—answering questions, walking through setup, troubleshooting issues, and brainstorming ideas.

## About Operator

Operator is Braze's AI assistant built into the dashboard. It is designed to help you accomplish tasks in Braze—answering questions, walking through setup, troubleshooting issues, and brainstorming ideas. Operator uses conversational language to provide guidance and support, similar to consulting with a knowledgeable colleague.

### What Operator can help with

Operator can assist with a wide range of tasks within Braze:

- **Explain anything on the active page:** Metrics, settings, or how a feature works
- **Walk through configuration:** Campaigns, segments, integrations, or workspace settings
- **Write or debug code:** Liquid templates, webhooks, or answer data and API questions
- **Troubleshoot issues:** Why messages aren't sending, delivery problems, or configuration errors
- **Brainstorm strategies:** Campaign ideas, segmentation approaches, or how to tackle complex use cases

Operator uses [page-aware context](#page-aware-context) to tailor guidance based on your location in the dashboard.

## How to access Operator

Open Operator from any page in the Braze dashboard.  

1. Select **BrazeAI Operator<sup>TM</sup>**, next to the user profile.

![The BrazeAI Operator icon next to a user profile.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

2. The Operator chat panel will open on the right-hand side of the screen.

![The chat panel for Operator.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Maximize to expand the panel for easier reading, or minimize to keep Operator available while working.  
{% endalert %} 

## How to use Operator

Describe what you are trying to accomplish using natural language. Prompts can range from simple questions to complex requests:

- **Simple:** Why isn't my Liquid rendering?
- **Complex:** How can I make the `abort_message` tag of my message include the user attribute that caused the abort?

Operator can provide step-by-step instructions, links to Braze documentation, and plain-language explanations. Clear and specific questions lead to more helpful responses. 

### Best practices

Treat Operator as a conversation, not a search engine. Short, natural prompts work best.

- **Be specific:** Instead of "Tell me about Canvas", try "How do I use Action Paths in Canvas?".  
- **Ask follow-up questions:** If the first response doesn't address your need, ask for clarification or additional details.
- **Use page-aware context:** Operator understands your location in Braze. Open Operator while viewing the relevant page for the most accurate results.

## Features

Operator includes the following features:

### GPT models

Select from these GPT models to use for different request types with Operator. Refer to the linked provider documentation to determine which model best fits your use case.

- [GPT-5 Nano](https://platform.openai.com/docs/models/gpt-5-nano)
- [GPT-5 Mini](https://platform.openai.com/docs/models/gpt-5-mini)
- [GPT-5](https://platform.openai.com/docs/models/gpt-5)
- [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1)
- [GPT-5.2](https://platform.openai.com/docs/models/gpt-5.2) (default)

![Dropdown for different GPT models to choose.]({% image_buster /assets/img/operator/operator_model.png %}){:style="max-width:70%"}

### Page-aware context

Operator understands your location in Braze and tailors responses based on that context. For example, when opened while building a Canvas, Operator can suggest steps or provide guidance relevant to that feature without requiring you to specify it. 

### Brand guidelines

Add brand guidelines as context to Operator queries so responses match the brand's voice, tone, and personality. Operator uses the brand guidelines configured in the workspace.

To set up brand guidelines, go to **Settings** > **Brand Guidelines**. For more, see [Brand Guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Placeholder for Operator brand guidelines selection.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Suggested prompts

When Operator is opened, suggested prompts appear. Select one or type a custom question.

### Understanding Operator's reasoning

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator arrived at an answer.

![Dropdown for "Reasoned" expanded with more details on how Operator answered.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:50%"}

### Suggested actions

In some cases, Operator will recommend next steps and provide direct links to relevant pages in the Braze dashboard. For example, if asked about email bounce rates, Operator may link to the **Deliverability Center** page.

### Stopping generation

While Operator is generating a response, the **Send** button becomes a **Stop** button. To end the response early, select **Stop**.

### Clearing chat history

To reset the conversation, select **Clear chat history**. This removes the current content and starts a fresh conversation.

### Sending feedback

At the bottom of each response, use the thumbs up or thumbs down buttons to provide quick feedback. This helps improve Operator's answers.

## Approval flow

When Operator proposes changes in the dashboard (such as filling in form fields, updating settings, or generating images), it presents each change as an approval card for review.

### How approval cards work

1. **Operator summarizes the plan:** Operator explains what it plans to do before showing approval cards.
2. **Individual approval cards appear:** Each proposed change is presented as a separate card that shows:
   - What Operator wants to change
   - The proposed value
   - For changes to existing values: both the previous value and the proposed value for comparison
3. **Review and approve:** Review each card and either approve or decline it.
4. **Action executes:** Approved actions are executed in Braze. Declined actions are not applied.

{% alert note %}
If an action fails after approval, Operator will notify with details about the failure.
{% endalert %}

### Modifying a plan

To change something Operator proposed, describe the modification in the chat using natural language. Operator will refresh the approval list with updated items. Previously approved and executed items remain unchanged.

{% alert note %}
Approved actions cannot be undone through Operator. Make changes manually in the Braze dashboard if needed.
{% endalert %}

### Auto-approve all actions

The **Auto-approve all actions** toggle is located in the Operator chat panel.

- **On:** Operator's suggested actions execute immediately without requiring manual approval. Some actions still require explicit approval for safety, such as generating images or making modifications to workspace-level settings.
- **Off (default):** All proposed actions follow the approval flow described above.

{% alert important %}
Auto-approve resets when you refresh the page, open a new tab, or log out and back in. Moving between pages in the dashboard does not reset it. Auto-approve can be turned off at any time.
{% endalert %}

When auto-approve is enabled, a confirmation modal appears to verify your choice.

![Placeholder for the Auto-approve toggle and confirmation modal.]({% image_buster /assets/img/operator/operator_auto_approve.png %})

## File a support ticket

File a support ticket directly from Operator without leaving the Braze dashboard.

### How to file a ticket

1. Open Operator and select **File a Support Ticket** (or ask Operator to file one).
2. Fill in the title and description of the issue.
3. Operator suggests relevant attachments and context to include.
4. Review and select **Submit**.

### Auto-included context

When filing a ticket from Operator, the following context is automatically included:

- Recent messages from the Operator chat session
- Page context from the active page when Operator was opened
- Workspace name
- Relevant logs and session details

You can add additional context manually using the text field or by attaching files.

### Tips for faster resolution

- Add a detailed description of the steps to reproduce the issue.
- Include relevant error messages or unexpected behavior.
- Review the auto-suggested attachments before submitting.

![Placeholder for the support ticket filing flow.]({% image_buster /assets/img/operator/operator_support_ticket.png %})

## Troubleshooting

| Issue | Troubleshooting |
| --- | --- |
| No response | Try refreshing the page and re-opening the Operator panel. |
| Off-topic answers | Reframe the question more specifically. Mention the feature or workflow being asked about. |
| Error messages | If Operator can't stream content, a "Try again" prompt may appear. Operator may be temporarily unavailable or the connection was interrupted. Retry after a few minutes. |
| Daily usage limit exceeded | The company-wide usage limit has been reached. Wait for the limit to reset (resets every 24 hours). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data privacy and security

### Model providers as sub-processors or third-party providers

When you use an integration with an LLM provider provided by Braze through the Braze Services ("Braze-provided LLM"), the providers of such Braze-provided LLM act as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. BrazeAI Operator integrates with OpenAI.

If you choose to bring your own API Key to integrate with BrazeAI Operator, the provider of your own LLM subscription will be considered a Third Party Provider, as defined in the contract between you and Braze. 

### How data is used with OpenAI

To generate AI output through BrazeAI features that leverage OpenAI ("Output"), Braze will send certain information ("Input") to OpenAI. Input consists of your prompts, the content displayed in the dashboard, and workspace data relevant to your queries. Per [OpenAI's API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI's API via Braze is not used to train or improve OpenAI models. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

## Limitations

- **Data access:** Operator can use the context of the active page, but it cannot query or return company-specific data stored in Braze, such as campaign lists, segment performance, or Canvas analytics.
- **Usage limits:** Operator has a company-wide daily usage limit that resets every 24 hours. If the limit is reached, a "Daily usage limit exceeded" banner will appear in the chat, and no further requests can be made until the limit resets.

{% alert tip %}
To manage usage, consider selecting a lighter model for simple queries and reserving more capable models for complex tasks.
{% endalert %}

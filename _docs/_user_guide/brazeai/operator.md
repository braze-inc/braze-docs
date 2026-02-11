---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 8
alias: /operator/
description: "This reference article covers BrazeAI Operator, an AI-powered assistant built into the Braze dashboard."
---

# BrazeAI Operator<sup>TM</sup>

> BrazeAI Operator<sup>TM</sup> is an AI-powered assistant built into the Braze dashboard. Operator provides answers, troubleshooting guidance, and best practices within your workflow.

## About Operator

Operator is a built-in AI assistant in the Braze dashboard. It answers questions, suggests next steps, and guides you through tasks—all within your workflow. Use Operator to:

- Get answers from Braze documentation
- Troubleshoot issues using [page-aware context](#page-aware-context)
- Learn best practices and onboarding guidance

### Model providers as sub-processors or third-party providers

Where Customer uses an integration with an LLM provider provided by Braze through the Braze Services ("Braze-provided LLM"), the providers of such Braze-provided LLM act as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between Customer and Braze. BrazeAI Operator integrates with OpenAI.

If Customer chooses to bring their own API Key to integrate with Braze AI Operator, the provider of Customer's own LLM subscription will be considered a Third Party Provider, as defined in the contract between Customer and Braze. 

### How is my data used and sent to OpenAI?

In order to generate AI output through Braze AI features that Braze identifies as leveraging OpenAI ("Output"), Braze will send your prompts, the content displayed in the Dashboard and Workspace data relevant to your queries, as applicable ("Input") to OpenAI. Per [OpenAI's API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI's API via Braze is not used to train or improve OpenAI models. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content generally, including Output.

## How to access Operator

Open Operator from any page in the Braze dashboard.  

1. Select **BrazeAI Operator<sup>TM</sup>**, next to the user profile.

![The BrazeAI Operator icon next to a user profile.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"} 
2. The Operator chat panel will open on the right-hand side of the screen.

![The chat panel for Operator.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Try maximizing to expand the panel for easier reading, or minimizing it to keep Operator available while you continue working.  
{% endalert %} 

## How to talk to Operator

Use prompts to communicate with Operator. The best approach is to speak naturally—like speaking to a coworker or a friend. Prompts can range from simple questions to complex requests:

- **Simple:** How can I ensure that users don't get cart abandonment emails while they are still on the site shopping?
- **Complex:** How can I make the `abort_message` tag of my message include the user attribute that caused the abort?

Operator can provide step-by-step instructions, links to Braze docs, and plain-language explanations. The clearer and more specific the question, the more useful the response will be. 

### Best practices

Think of Operator as a conversation, not a search engine. Short, natural prompts usually work best.

- **Be specific:** Instead of "Tell me about Canvas", try "How do I use Action Paths in Canvas?".  
- **Use follow-ups:** If the first response isn't what's needed, ask clarifying questions. Operator can refine answers.
- **Rely on context:** Operator knows what page is active in Braze. Open Operator while on the page being worked with for the most relevant results.

## Features

Operator includes the following features:

### GPT models

Select from these GPT models to use for different request types with Operator. Each model offers a different balance of cost, latency, and capability. Refer to the linked provider documentation to determine which model best fits your use case.

- [GPT-5 nano](https://platform.openai.com/docs/models/gpt-5-nano)
- [GPT-5 mini](https://platform.openai.com/docs/models/gpt-5-mini)
- [GPT-5](https://platform.openai.com/docs/models/gpt-5)
- [GPT-5.1](https://platform.openai.com/docs/models/gpt-5.1) (default)

![Dropdown for different GPT models to choose.]({% image_buster /assets/img/operator/operator_model.png %}){:style="max-width:70%"}

### Page-aware context

Operator understands the page being worked on in Braze and can tailor responses based on that context. For example, if Operator is opened while building a Canvas, it can suggest steps or provide guidance relevant to Canvas without needing to explain where the user is. 

### Brand guidelines

Add brand guidelines as context to Operator queries so responses match the brand's voice, tone, and personality. Operator uses the brand guidelines configured in the workspace.

To set up brand guidelines, go to **Settings** > **Brand Guidelines**. For more, see [Brand Guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

![Placeholder for Operator brand guidelines selection.]({% image_buster /assets/img/operator/operator_brand_guidelines.png %})

### Suggested prompts

When Operator is opened, suggested prompts appear to help get started. Select one to get started or type a custom question.

### Viewing reasoning

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator arrived at an answer.

![Dropdown for "Reasoned" expanded with more details on how Operator answered.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:50%"}

### Suggested actions

In some cases, Operator will recommend next steps and provide direct links to the relevant pages in the Braze dashboard. For example, if asked about email bounce rates, Operator may link to the **Deliverability Center** page. These shortcuts help take action faster without needing to navigate manually.

### Stopping generation

While Operator is generating a response, the **Send** button becomes a **Stop** button. To end the response early, select **Stop**.

### Clearing chat history

To reset the conversation, select **Clear chat history**. This removes the current content to start fresh.

### Maximizing and minimizing the panel

Use the **maximize** button to expand Operator for easier reading, or **minimize** to keep the panel tucked away while you continue working in Braze.

### Sending feedback

At the bottom of each response, use the thumbs up or thumbs down buttons to provide quick feedback. This helps improve Operator's answers.

## Approval flow

When Operator proposes an action, it goes through an approval flow before executing in Braze.

1. **Operator proposes an action:** Based on the prompt, Operator suggests a specific action.
2. **Review:** Review the proposed action and its details, and either approve or decline the action.
3. **Action executes:** Approved actions are executed in Braze. Declined actions are not applied.

{% alert note %}
If an action fails after approval, Operator will notify with details about the failure.
{% endalert %}

### Auto-approve all actions

The **Auto-approve all actions** toggle is located in the Operator chat panel.

- **On:** Operator's suggested actions execute immediately without requiring manual approval. Recommended for trusted workflows only.
- **Off (default):** Operator-proposed actions are routed through the approval flow described above.

When auto-approve is enabled, a confirmation modal appears to verify the choice.

![Placeholder for the Auto-approve toggle and confirmation modal.]({% image_buster /assets/img/operator/operator_auto_approve.png %})

## Filing a support ticket

File a support ticket directly from Operator without leaving the Braze dashboard.

### How to file a ticket

1. Open Operator and select **File a Support Ticket** (or ask Operator to file one).
2. Fill in the title and description of the issue.
3. Operator suggests relevant attachments and context to include.
4. Review and select **Submit**.

### Auto-included context

When filing a ticket from Operator, the following context is automatically included:

- Recent chat messages from the Operator session
- Page-aware context (the page that was active when Operator was opened)
- Current workspace name
- Relevant logs and session details

Add additional context manually using the text field or by attaching files.

### Tips for faster resolution

- Include the workspace name and a timestamp.
- Add a short description of the steps to reproduce the issue.
- Review the auto-suggested attachments before submitting.

![Placeholder for the support ticket filing flow.]({% image_buster /assets/img/operator/operator_support_ticket.png %})

## Troubleshooting

| Issue | Troubleshooting |
| --- | --- |
| No response | Try refreshing the page and re-opening the Operator panel. |
| Off-topic answers | Reframe the question more specifically. Mention the feature or workflow being asked about. |
| Error messages | If Operator can't stream content, a "Try again" prompt may appear. Operator may be temporarily unavailable or the connection was interrupted. Retry after a few minutes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

- **Data access:** Operator can use the context of the page being worked on, but it can't query or return company data stored in Braze, such as campaign lists, segment performance, or Canvas analytics.
- **Usage limits:** Operator has a daily usage limit that resets every 24 hours. The limit is generous and unlikely to be reached during normal use. More complex queries consume more of the limit than simpler ones.

{% alert tip %}
To manage usage, consider selecting a lighter model for simple queries and reserving more capable models for complex tasks.
{% endalert %}

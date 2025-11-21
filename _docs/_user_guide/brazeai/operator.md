---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 0.7
alias: /operator/
description: "This reference article covers BrazeAI Operator, an AI-powered assistant built into the Braze dashboard."
---

# BrazeAI<sup>TM</sup> Operator

> BrazeAI<sup>TM</sup> Operator is an AI-powered assistant built into the Braze dashboard. Operator provides answers, troubleshooting guidance, and best practices within your workflow.

{% alert important %}
BrazeAI<sup>TM</sup> Operator is in a private beta with limited functionality. For help getting started, contact your customer success manager.
{% endalert %}

## About Operator

Operator is a built-in AI assistant in the Braze dashboard. It answers questions, suggests next steps, and guides you through tasks—all within your workflow.

During the beta, Operator supports **Ask** mode only. You can:

- Get answers from Braze documentation
- Troubleshoot issues using [page-aware context](#page-aware-context)
- Learn best practices and onboarding guidance

### Model providers as sub-processors or third-party providers

Where Customer uses an integration with an LLM provider provided by Braze through the Braze Services (“Braze-provided LLM”), the providers of such Braze-provided LLM act as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between Customer and Braze. BrazeAI Operator integrates with OpenAI.

If Customers chooses to bring their own API Key to integrate with Braze AI Operator, the provider of Customer’s own LLM subscription will be considered a Third Party Provider, as defined in the contract between Customer and Braze. 

### How is my data used and sent to OpenAI?

In order to generate AI output through Braze AI features that Braze identifies as leveraging OpenAI (“Output”), Braze will send your prompts, the content displayed in the Dashboard and Workspace data relevant to your queries, as applicable (“Input”) to OpenAI. Per [OpenAI’s API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI’s API via Braze is not used to train or improve OpenAI models. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content generally, including Output.

## How to access Operator

You can open Operator from any page in the Braze dashboard.  

1. Select **BrazeAI<sup>TM</sup> Operator**, next to your user profile.

![The BrazeAI Operator icon next to a user profile.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"} 
2. The Operator chat panel will open on the right-hand side of the screen.

![The chat panel for Operator.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Try maximizing to expand the panel for easier reading, or minimizing it to keep Operator available while you continue working.  
{% endalert %} 

## How to talk to Operator

Use prompts to communicate with Operator. The best approach is to speak naturally—like you would a coworker or a friend. Your prompts can range from simple questions to complex requests:

- **Simple:** How can I ensure that users don't get cart abandonment emails while they are still on the site shopping?
- **Complex:** How can I make the `abort_message` tag of my message include the user attribute that caused the abort?

Operator can provide step-by-step instructions, links to Braze docs, and plain-language explanations. The clearer and more specific your question, the more useful the response will be. 

### Best practices

Think of Operator as a conversation, not a search engine. Short, natural prompts usually work best.

- **Be specific:** Instead of "Tell me about Canvas", try "How do I use Action Paths in Canvas?".  
- **Use follow-ups:** If the first response isn’t what you need, ask clarifying questions. Operator can refine answers.
- **Rely on context:** Operator knows what page you're on in Braze. Open Operator while you’re on the page you’re working with for the most relevant results.

## Features

Operator includes the following features during beta:

### GPT models

You can select from these GPT models to use for different request types with Operator:

- [GPT-5 nano](https://platform.openai.com/docs/models/gpt-5-nano)
- [GPT-5 mini](https://platform.openai.com/docs/models/gpt-5-mini) (default)
- [GPT-5](https://platform.openai.com/docs/models/gpt-5)

![Dropdown for different GPT models to choose.]({% image_buster /assets/img/operator/operator_model.png %}){:style="max-width:70%"}

### Page-aware context

Operator understands the page you're working on in Braze and can tailor responses based on that context. For example, if you open Operator while building a Canvas, it can suggest steps or provide guidance relevant to Canvas without you needing to explain where you are. 

### Suggested prompts

When you open Operator, you’ll see a few suggested prompts to help you get started. Select one to get started or type your own question.

### Viewing reasoning

Operator shows its reasoning steps in collapsible sections labeled **Reasoned**. Select the dropdown to expand these sections and see how Operator arrived at an answer.

![Dropdown for "Reasoned" expanded with more details on how Operator answered.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:50%"}

### Suggested actions

In some cases, Operator will recommend next steps and provide direct links to the relevant pages in your Braze dashboard. For example, if you ask about email bounce rates, Operator may link you to your **Deliverability Center** page. These shortcuts help you take action faster without needing to navigate manually.

### Stopping generation

While the Operator is generating a response, the **Send** button becomes a **Stop** button. If you'd like to end the response early, select **Stop**.

### Clearing chat history

To reset your conversation, select **Clear chat history**. This removes the current content so you can start fresh.

### Maximizing and minimizing the panel

You can use the **maximize** button to expand Operator for easier reading, or **minimize** to keep the panel tucked away while you continue working in Braze.

### Sending feedback

At the bottom of each response, use the thumbs up or thumbs down buttons to provide quick feedback. This helps improve Operator’s answers.

## Troubleshooting

| Issue | Troubleshooting |
| --- | --- |
| No response | Try refreshing the page and re-opening the Operator panel. |
| Off-topic answers | Reframe your question more specifically. Mention the feature or workflow you’re asking about. |
| Error messages | If Operator can’t stream content to you, you may see a “Try again” prompt. Operator may be temporarily unavailable or your connection was interrupted. Retry after a few minutes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

Operator is designed to help you navigate Braze and get work done more efficiently, but there are some current limits to keep in mind:

### No access to your data

While Operator has access to the context of the work you're doing in Braze, Operator can’t query or return answers about your company’s data stored in Braze. For example, it **can’t** respond to requests like:

- “Give me a list of all my email campaigns from last year.”
- “Show me which segments had the highest engagement last quarter.”
- “Analyze my Canvas performance and suggest improvements.”

### Beta stability

As a private beta, Operator may have occasional errors, interruptions, or incomplete features.

If you’re unsure whether a question is supported, try phrasing it in terms of how Operator can help you navigate or take actions inside the Braze dashboard, rather than pulling analytics or historical data.

### Number of messages sent

There is a limit of how many messages you can send to Operator. We recommend using the default GPT-5 mini or GPT-5 nano for your queries and using GPT-5 judiciously for more complex tasks.

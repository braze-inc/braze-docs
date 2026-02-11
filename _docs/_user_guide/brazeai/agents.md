---
nav_title: Agents
article_title: Braze Agents
page_order: 1
description: "Braze Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences."
---

# Braze Agents

> Braze Agents are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences.

{% alert important %}
Braze Agents are currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

## Why use Braze Agents?

Braze Agents help your team deliver smarter, more personalized experiences—without adding extra work. They act as intelligent assistants that don’t just respond to prompts, but understand context, make decisions, and take action toward a goal.

In practice, agents can automatically create message copy—like subject lines or in-product text—so every customer gets communication that feels tailored to them. They can also adapt in real time, routing people through different Canvas paths based on preferences, behaviors, or other data.

Beyond messaging, agents can enrich your catalogs by calculating or generating product and profile field values, keeping your data fresh and dynamic. By taking on repetitive or complex tasks, they free your team to focus on strategy and creativity instead of manual setup. Braze Agents act more like collaborators than background processes—helping you solve problems and deliver impact at scale.

### When to use Braze Agents versus other BrazeAI features

Use agents for personalizing content on the fly using a user’s specific context. For example, if an agent knows a particular user’s favorite ice cream flavor is chocolate and favorite topping is gummy bears, it can come up with push copy specific to that combination for that user as they pass through the Canvas.

However, the agent does not learn through trial and error, and it has no idea of an ultimate marketing goal it is looking to measure and maximize. Even if you tell it to generally write copy that drives conversions, it has no mechanism to “monitor” for the conversion impact of its agentic writing and integrate that data back into future agentic calls. You can think of this as “vibe” decisioning, not reward-based AI Decisioning.

In contrast, other BrazeAI tools are designed to maximize the metrics that they are measuring. For example, agents are very good at qualitatively assessing how a user’s characteristics factor into their likelihood or propensity to do a certain event or like a certain product. However, because the agent doesn’t learn through trial and error, it has no idea of how to measure its accuracy in predicting likelihoods and improving the signal over time. As such, using Predictive Suite outperforms the Agent step when judged on the accuracy of its predictions and improvements over time.

## Features

Features for Braze Agents include:

- **Flexible setup:** Use a Braze-provided LLM or connect your own model provider (such as OpenAI, Anthropic, Google Gemini, or AWS Bedrock).
- **Seamless integration:** Deploy agents directly in Canvas steps or catalog fields.
- **Testing and logging tools:** Preview your agent's output by testing with sample inputs before you launch. View logs for each time the agent runs, including the input and output for that run.
- **Usage controls:** Daily limits help manage performance and costs.

## About Braze Agents

Agents are configured with instructions (system prompts) that define how they behave. When an agent runs, it uses your instructions along with any data you pass in to generate a response. 

### Key concepts

| Term | Definition |
| --- | --- |
| [Model]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#models) | The agent’s “brain,” in this case a large language model (LLM). It interprets inputs, generates responses, and performs reasoning. A stronger model (trained on more relevant data) makes the agent more capable and versatile. |
| [Instructions]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#writing-instructions) | The rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. Clear instructions make the agent more reliable and predictable. |
| Context | Data passed into the agent at runtime wherever it is deployed, such as user profile fields or catalog rows. This input provides the information the agent uses to generate outputs. |
| [Output variable]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/#step-3-define-the-output-variable) | The output the agent produces when used in Canvas steps. Output variables store the agent’s result to personalize content or guide workflow paths. Output variables can be a string, number, or boolean data type.  |
| [Execution](#limitations) | A single run of the agent. This counts against your daily limits. |
| [Output format]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) | The predefined data structure of the agent's response. |
| [Temperature]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) | The level of deviation for the agent's output. This defines how precise or creative your agent can be. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

During the beta period, the following limitations apply:

- Each agent has a default daily execution limit of 50,000 runs, which can be increased up to a maximum of 100,000 runs per day.
- By default, each run must complete within 15 seconds. After 15 seconds, the agent returns a `null` response where it is used. 
    - If your agents consistently time out, contact your Braze account manager to increase this limit.
- Input data is limited to 25 KB per request. Longer inputs are truncated.

## Next steps

Now that you know about Braze Agents, you’re ready for the next steps:

- [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Deploy custom agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)

## Model Providers as Sub-processors or Third Party Providers

Where Customer uses an integration with models provided by Braze through the Braze Services (“Braze-provided LLM”), the providers of such Braze-provided LLMs will be acting as a Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between Customer and Braze. 

If Customer chooses to bring their own API key to integrate with Braze AI functionality, the provider of Customer’s own LLM subscription will be considered a Third Party Provider, as defined in the contract between Customer and Braze. 

### How is my data used and sent to Braze-provided LLMs?

In order to generate AI output through Braze AI features that Braze identifies as leveraging Braze-provided LLMs (“Output”), Braze will send your system prompt or any other input, as applicable (“Input”) to Braze-provided LLM. Data sent to the applicable Braze-provided LLM is not used to train or improve the Braze-provided LLM. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content generally, including Output.

The Braze-provided LLM for Braze Agents, identified as “Auto”, uses Google Gemini models. Google retains Inputs and Outputs submitted through Braze for 55 days, after which the data is deleted.

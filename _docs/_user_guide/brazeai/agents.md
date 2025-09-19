---
nav_title: Agents
article_title: Braze Agents
page_order: 0.5
description: "Braze Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences."
---

# Braze Agents

> Braze Agents are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences.

{% alert important %}
Braze Agents are currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

image

## Why use Braze Agents?

Braze Agents help your team deliver smarter, more personalized experiences—without adding extra work. They act as intelligent assistants that don’t just respond to prompts, but understand context, make decisions, and take action toward a goal.

In practice, Agents can automatically create message copy—like subject lines or in-product text—so every customer gets communication that feels tailored to them. They can also adapt in real time, routing people through different Canvas paths based on preferences, behaviors, or other data.

Beyond messaging, Agents can enrich your catalogs by calculating or generating product and profile field values, keeping your data fresh and dynamic. By taking on repetitive or complex tasks, they free your team to focus on strategy and creativity instead of manual setup.

With a combination of reasoning, context, and tools, Braze Agents act more like collaborators than background processes—helping you solve problems and deliver impact at scale.

## Features

Features for Braze Agents include:

- **Flexible setup:** Use a Braze-provided LLM or connect your own model provider (such as OpenAI, Anthropic, Google Gemini, or AWS Bedrock).
- **Seamless integration:** Deploy agents directly in Canvas steps or catalog fields.
- **Testing tools:** Preview outputs with sample inputs before you launch.
- **Usage controls:** Built-in execution and size limits to manage performance and costs.

## About Braze Agents

Agents are configured with instructions (system prompts) that define how they behave. When an agent runs, it uses your instructions along with any data you pass in (like a consumer’s profile details or catalog fields) to generate a response.

### Key concepts

| Term | Definition |
| --- | --- |
| Model | The agent’s “brain,” in this case a large language model (LLM). It interprets inputs, generates responses, and performs reasoning. A stronger model (trained on more relevant data) makes the agent more capable and versatile.
| Context | Data passed into the agent at runtime, such as profile fields or catalog rows. This provides the information the agent uses to generate outputs. |
| Tools *(Coming soon)* | External services the agent can use (like APIs, databases, or search). They extend the agent’s abilities beyond its training—for example, fetching real-time data or running specialized tasks. Tools help the agent bridge gaps in its native capabilities, much like a human looking something up.
| Instructions | The rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. Clear instructions make the agent more reliable and predictable. |
| Response variable | The output the agent produces (string, number, Boolean). Response variables store the agent’s result to personalize content or guide workflow paths. |
| Execution | A single run of the agent. This counts against your daily and total limits. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

Agents process requests at roughly 1,000 executions per minute. Each workspace can support up to 1,000 agents. If this limit is reached, you'll need to remove an existing agent before creating a new one. 

Additionally, during the beta period:

- Execution is limited to 50,000 runs per day and 500,000 runs in total.
- Each run must complete within 30 seconds. After 30 seconds, the agent will return a null response where it is used.
- Input data is limited to 10 KB per request. Longer inputs are truncated.
- For catalogs, agentic fields update only the first 10,000 rows.

## Next steps


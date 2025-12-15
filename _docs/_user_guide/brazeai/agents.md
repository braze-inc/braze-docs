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

## Why use Braze Agents?

Braze Agents help your team deliver smarter, more personalized experiences—without adding extra work. They act as intelligent assistants that don’t just respond to prompts, but understand context, make decisions, and take action toward a goal.

In practice, agents can automatically create message copy—like subject lines or in-product text—so every customer gets communication that feels tailored to them. They can also adapt in real time, routing people through different Canvas paths based on preferences, behaviors, or other data.

Beyond messaging, agents can enrich your catalogs by calculating or generating product and profile field values, keeping your data fresh and dynamic. By taking on repetitive or complex tasks, they free your team to focus on strategy and creativity instead of manual setup. Braze Agents act more like collaborators than background processes—helping you solve problems and deliver impact at scale.

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

- Each agent can be executed up to 100,000 times per day.
- An agent's default daily execution limit is 50,000.
- Daily execution is limited to 100,000 runs per agent, per day.
- Each run must complete within 30 seconds. After 30 seconds, the agent will return a null response where it is used.
- Input data is limited to 25 KB per request. Longer inputs are truncated.

## Next steps

Now that you know about Braze Agents, you’re ready for the next steps:

- [Creating custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
- [Deploying custom agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)

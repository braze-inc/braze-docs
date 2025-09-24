---
nav_title: Agent
article_title: Agent Step
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "This reference article covers how to use the Agent step in Canvas to generate content or make intelligent decisions in real time."
tool: Canvas
---

# Agent Step  

> The Agent step lets you add AI-powered decisioning and content generation directly into your Canvas workflow. For more general information, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/). 

![An Agent step in a Canvas user journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## How it works

When a user reaches an Agent step in a Canvas, Braze sends the input data you’ve configured (full context or selected fields) to your chosen agent. The agent then processes the input using its model and instructions, and returns an output. That output is stored in the response variable you defined in the step.

You can then use this variable in two main ways:

- **Decisioning:** Route users down different Canvas paths based on the agent’s response. For example, a lead scoring agent might return a number between 1 and 10. You can use this score to decide whether to continue messaging a user or drop them from the journey.
- **Personalization:** Insert the agent’s response directly into a message. For example, an agent could analyze customer feedback and generate an empathetic follow-up email that references the customer’s comment and suggests a resolution.

## Creating an Agent step

### Step 1: Add a step

Drag and drop the **Agent** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Agent**.  

### Step 2: Select your agent  

Select the agent that will process data in this step. Choose an existing agent, or create a new one directly from this step. For setup guidance, see [Creating custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Step 3: Define the response variable

Agent outputs are called "response variables", and are stored in a [context variable]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) for easy access. To define the response variable:

1. Give the variable a name.
2. Select a data type. 

Agent responses can be saved as strings, numbers, or booleans. This makes them flexible for both text personalization and conditional logic in your Canvas. Here are some common uses for each type:

| Data type | Common uses |
| --- | --- |
| String | Message personalization (subject lines, copy, responses) |
| Number | Scoring, thresholds, routing in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolean | Yes/No branching in [Decision Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

When defined, you can use a response variable throughout the Canvas by using the same template syntax as you would with a context variable. Either use the **Context Variable** segment filter, or template agent responses directly using Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

### Step 4: Decide what context to provide the agent  

You must decide what data the agent should receive at runtime. The following options are available:  

- **Include all Canvas context:** Pass all available Canvas context variables (such as [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) and any other context that it has been given through Context steps.  
- **Provide values:** Pass only selected properties, such as a user’s first name or favorite color. Choose this option to only give the agent access to the values you assign here. For each **Key**, enter the [Liquid tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) that defines the specific user profile field or context variable.  

{% alert note %}
Braze will only pass the first 10 KB of content to the agent. Providing values that have a total value of more than 10 KB will result in truncation. To help save costs, Braze Agents in Canvas use short-lived caches for LLM responses for identical inputs. Including all Canvas Context increases the likelihood that cached results cannot be used, which might increase your LLM costs.
{% endalert %}

## Error handling  

- If the connected model returns a rate limit error, Braze retries up to five times with exponential backoff.  
- If the agent fails for any other reason (such as invalid API key), the response variable is set to `null`.  
- Responses are cached for identical inputs to reduce repeated executions.  

## Analytics  

Refer to the following metrics to track how your Agent steps perform:  

| Metric | Description |
| --- | --- |
| _Entries_ | The number of times users entered the Agent step. |
| _Executions_ | The total number of times the agent was called from this step. |
| _Succeeded_ | The number of successful executions that returned a valid response. |
| _Failed_ | The number of executions that resulted in an error or `null` response. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Related articles  

- [Braze Agents overview]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Creating custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Deploying agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
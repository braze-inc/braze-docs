---
nav_title: Agent
article_title: Agent Step
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "This reference article covers how to use the Agent step in Canvas to generate content or make intelligent decisions in real time."
tool: Canvas
toc_headers: h2
---

# Agent step  

> The Agent step lets you add AI-powered decisioning and content generation directly into your Canvas workflow. For more general information, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/). 

![An Agent step in a Canvas user journey.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## How it works

When a user reaches an Agent step in a Canvas, Braze sends the input data you’ve configured (full context or selected fields) to your chosen agent. The agent then processes the input using its model and instructions, and returns an output. That output is stored in the output variable you defined in the step.

You can then use this variable in two main ways:

- **Decisioning:** Route users down different Canvas paths based on the agent’s response. For example, a lead scoring agent might return a number between 1 and 10. You can use this score to decide whether to continue messaging a user or drop them from the journey.
- **Personalization:** Insert the agent’s response directly into a message. For example, an agent could analyze customer feedback and generate an empathetic follow-up email that references the customer’s comment and suggests a resolution.

## Creating an Agent step

### Step 1: Add a step

Drag and drop the **Agent** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Agent**.  

### Step 2: Select your agent  

Select the agent that will process data in this step. Choose an existing agent, or create a new one directly from this step. For setup guidance, see [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Step 3: Define the output variable

Agent outputs are called "output variables" and are stored in a [context variable]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) for easy access. To define the output variable:

1. Give the variable a name.
2. Select a data type. 

Agent outputs can be saved as strings, numbers, booleans, or objects. This makes them flexible for both text personalization and conditional logic in your Canvas. Here are some common uses for each type:

| Data type | Common uses |
| --- | --- |
| String | Message personalization (subject lines, copy, responses) |
| Number | Scoring, thresholds, routing in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolean | Yes/No branching in [Decision Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Object | Leverage one or more of the above data types with a single LLM call in a predictable data structure |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

When defined, you can use an output variable throughout the Canvas by using the same template syntax as you would with a context variable. Either use the **Context Variable** segment filter, or template agent responses directly using Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

To use a specific property from an object output variable, use dot notation to access that property using Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agent step for Body HTML Writer with an object data type output for the variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

Use the Liquid syntax patterns shown above to reference particular fields from the agent output in future Canvas steps.

### Step 4: Decide what context to provide the agent  

You must decide what data the agent should receive at runtime. The following options are available:  

- **Include all Canvas context:** Pass all available Canvas context variables (such as [Canvas entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) into the Agent step. You can use Context steps upstream of the agent steps to add more data to Context ahead of it.
- **Provide values:** Pass only selected properties, such as a user’s first name or favorite color. Choose this option to only give the agent access to the values you assign here. For each **Key**, enter the [Liquid tag]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) that defines the specific user profile field or context variable.  

{% alert note %}
Braze will only pass the first 10 KB of content to the agent. Providing values that have a total value of more than 10 KB will result in truncation.
{% endalert %}

### Step 5: Test the agent

After setting up your Agent step, you can test and preview the output of this step.

## Error handling  

- If the connected model returns a rate limit error, Braze retries up to five times with exponential backoff.  
- If the agent fails for any other reason (such as invalid API key), the output variable is set to `null`.
    - If an agent reaches its daily invocation limit, the output variable is set to `null`. If you're using an agent's output in a Message step, consider using Liquid abort logic.
- Responses are cached for identical inputs and may be reused for repeated identical invocations within a few minutes.
    - Responses that use cached values do still count towards total and daily invocations.

## Analytics  

Refer to the following metrics to track how your Agent steps perform:  

| Metric | Description |
| --- | --- |
| _Entered_ | The number of times users entered the Agent step. |
| _Proceeded to Next Step_ | The number of users that proceeded to the next step in the flow after passing through the Agent step. |
| _Exited Canvas_ | The number of users that exited the Canvas after passing through the Agent step. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### When should I use an Agent step?

In general, we recommend using an Agent step when you want to feed particular contextual data into an LLM and have it agentically assign Canvas context variables intelligently at a scale impossible for humans.

Let’s say you’re sending a personalized message to recommend a new ice cream flavor to a user who previously ordered chocolate and strawberry. Here’s the difference between using an Agent step versus AI item recommendations:

- **Agent step:** Uses LLMs to make a qualitative decision on what the user might want based on the instructions and context data points given to the agent. In this example, an Agent step might recommend a new flavor based on the possibility of the user wanting to try different flavors.
- **AI item recommendations:** Uses machine learning models to predict the products that a user is most likely to want based on past user events, such as purchases. In this example, AI item recommendations would suggest a flavor (vanilla) based on the user’s previous two orders (chocolate and strawberry) and how those compare to the behaviors of other users in your workspace.

### When should I use a standard output format for an agent?

We recommend using the output format when you want the agent to return a data structure with multiple values defined in a structured manner, rather than a single-value output. This allows the output to be better formatted as a consistent context variable.

For example, you may use an output format within an agent that is intended to create a sample travel itinerary for a user based on a form they submitted. The output format allows you to define that every agent response should come back with values for `tripStartDate`, `tripEndDate`, and `destination` values. Each of these values can be extracted from context variables and placed in a Message step for personalization using Liquid.

### How do Agent steps use input data?

Agent steps use specific context data that is [provided to the agent](#step-4-decide-what-context-to-provide-the-agent). 

You can choose to either pass the entirety of Canvas context into the agent as context, or pass specific values using Liquid tags into the context of that Agent step. You can also use Connected Content as an input value in an Agent step.

## Related articles  

- [Braze Agents overview]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Deploy agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
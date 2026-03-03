---
nav_title: Agent
article_title: Agent Step
alias: /agent_step/
page_order: 2
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

You can then use this variable in three main ways:

- **Decisioning:** Route users down different Canvas paths based on the agent’s response. For example, a lead scoring agent might return a number between 1 and 10. You can use this score to decide whether to continue messaging a user or drop them from the journey.
- **Personalization:** Insert the agent’s response directly into a message. For example, an agent could analyze customer feedback and generate an empathetic follow-up email that references the customer’s comment and suggests a resolution.
- **Processing user data:** Analyze and standardize your user data, then store it on the user profile or send it using a webhook. For example, an agent could return a sentiment score or product affinity assignment. You can store that data in a user profile for future usage.

## Prerequisite

Agent steps use [Canvas context variables]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) to ingest relevant context and output a variable that can be leveraged in the Canvas.

## Creating an Agent step

### Step 1: Add a step

Drag and drop the **Agent** component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Agent**.  

### Step 2: Choose your agent  

Select the agent that will process data in this step. Choose an existing agent. For setup guidance, see [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Step 3: Set your agent's output {#define-the-output-variable}

Agent outputs are called "output variables" and are stored in a [context variable]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) for easy access. To define the output variable, give the variable a name.

Note that the output variable's data type is set from the [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents). Agent outputs can be saved as strings, numbers, booleans, or objects. This makes them flexible for both text personalization and conditional logic in your Canvas. Here are some common uses for each type:

| Data type | Common uses |
| --- | --- |
| String | Message personalization (subject lines, copy, responses) |
| Number | Scoring, thresholds, routing in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Boolean | Yes/No branching in [Decision Splits]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Object | Leverage one or more of the above data types with a single LLM call in a predictable data structure |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

You can use an output variable throughout the Canvas by using the same template syntax as you would with a context variable. Either use the **Context Variable** segment filter, or template agent responses directly using Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

To use a specific property from an object output variable, use dot notation to access that property using Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Agent step for Body HTML Writer with an object data type output for the variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### Step 4: Add any additional context (optional)

You can decide to include additional context values for the agent step to reference when it runs. You can enter any Liquid templated values that you would normally use in a Canvas.

{% alert note %}
Note that the agent is already automatically receiving the context configured in the **Instructions** section. Liquid variables that were already configured there do not need to be re-entered here.
{% endalert %}

![The option to add additional context to an Agent step using Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Step 5: Test the agent

After setting up your Agent step, you can test and preview the output of this step.

![Preview the agent output as a random user.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Error handling  

- If the connected model returns a rate limit error, Braze retries up to five times with exponential backoff.  
- If the agent fails for any other reason (such as a timeout error or invalid API key), the output variable is set to `null`.
    - If an agent reaches its daily invocation limit, the output variable is set to `null`. If you're using an agent's output in a Message step, consider using [default Liquid values]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values).
- Responses are cached for identical inputs and may be reused for repeated identical invocations within a few minutes.
    - Responses that use cached values do still count toward total and daily invocations.

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

In general, we recommend using an Agent step when you want to feed particular contextual data into an LLM and have it agentically assign a Canvas context variable intelligently at a scale impossible for humans.

Let’s say you’re sending a personalized message to recommend a new ice cream flavor to a user who previously ordered chocolate and strawberry. Here’s the difference between using an Agent step versus AI item recommendations:

- **Agent step:** Uses LLMs to make a qualitative decision on what the user might want based on the instructions and context data points given to the agent. In this example, an Agent step might recommend a new flavor based on the possibility of the user wanting to try different flavors.
- **AI item recommendations:** Uses machine learning models to predict the products that a user is most likely to want based on past user events, such as purchases. In this example, AI item recommendations would suggest a flavor (vanilla) based on the user’s previous two orders (chocolate and strawberry) and how those compare to the behaviors of other users in your workspace.

### How do Agent steps use input data?

An Agent step analyzes the context data that the agent is configured to use, as well as any additional context that is [provided to the agent](#step-4-add-any-additional-context-optional).

## Related articles  

- [Braze Agents overview]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Deploy agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Reference for agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)  
---
nav_title: Create agents
article_title: Create custom agents
description: "Learn how to create agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management."
page_order: 1
alias: /creating-agents/
---

# Create custom agents

> Learn how to create custom agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management. For more general information, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents).

## Prerequisites

Before you start, you'll need the following:

- [Permission]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#list-of-permissions) to access the **Agent Console** in your workspace. Check with your Braze admins if you don’t see this option.  
- Permission to create and edit custom AI Agents.
- An idea of what you want the agent to accomplish. Braze Agents can support the following actions:  
   - **Messaging:** Generate subject lines, headlines, in-product copy, or other content.  
   - **Decisioning:** Route users in Canvas based on behavior, preferences, or custom attributes.  
   - **Data management:** Calculate values, enrich catalog entries, or refresh profile fields.  

## How it works

When you create an agent, you define its purpose and set guardrails for how it should behave. After it's live, the agent can be deployed in Braze to generate personalized copy, make real-time decisions, or update catalog fields. You can pause or update an agent anytime from the dashboard.

The following use cases showcase a few ways to leverage custom agents.

| Use case | Description |
| --- | --- |
| Customer feedback handling | Pass user feedback to an agent to analyze sentiment and generate empathetic follow-up messages. For high-value users, the agent might escalate the response or include perks. |
| Localize content | Translate catalog text into another language for global campaigns, or adjust tone and length for region-specific channels. For example, translate “Classic Clubmaster Sunglasses” into Spanish as “Gafas de sol Classic Clubmaster,” or shorten descriptions for SMS campaigns. |
| Summarize reviews or feedback | Summarize sentiment or feedback into a new field, such as assigning sentiment scores like Positive, Neutral, or Negative, or creating a short text summary like “Most customers mention great fit, but note slow shipping.” |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Create an agent

### Step 1: Choose an agent type

To create your custom agent:

1. Go to **Agent Console** > **Agent Management** in the Braze dashboard.  
2. Select **Create agent**.
3. Choose to create a Canvas agent or catalog agent.

### Step 2: Set up details

Next, set up the details for your agent:

1. Enter a name and description to help your team understand its purpose.
2. (optional) Add tags to filter your agent.
3. Choose the [model]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) for your agent to use.
4. Select the model's thinking level. You can choose from minimal, low, medium, or high. We recommend starting with **Minimal** and testing your agent's responses and adjusting this as needed.

![Agent Console interface for creating a custom agent in Braze. The screen displays fields for entering the agent name and description, and selecting a model.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Step 3: Write the instructions {#agent-instructions}

Give the agent instructions. We recommend including instructions for what the agent should do in unexpected or ambiguous scenarios. This minimizes the risk that agent confusion leads to errors. For example, rather than asking the agent for only "positive" or "negative" sentiment values, ask it to return "unsure" if it can't decide.

Refer to the [Writing instructions]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) for best practices and [Examples]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) for inspiration on how to prompt your agent.

{% alert tip %}
For Canvas agents, you can use Liquid in your instructions to reference user attributes, such as their first and last name, or custom attributes. Any Liquid variable in the agent instructions is automatically passed to the Agent step when a user enters the step.
{% endalert %}

#### Step 3.1: Add context

Select **Add context** to choose what your agent can reference. This includes:

- [Catalog fields]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Give the agent access to your catalog data for more accurate responses.
- [Segment membership]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Let the agent personalize responses based on which segments a user belongs to. You can select up to three segments.
- [Brand guidelines]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): Reference the brand voice and style guidelines for the agent to follow. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.
- [All Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analyze all Canvas context data for a user when this agent is invoked, including any variables that are not referenced in the **Instructions** section.

#### Step 3.2: Add optional settings

In the **Optional settings**, you can adjust the [temperature]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) of the agent-generated copy. A higher temperature allows the agent to use the information provided to be more creative.

You can also set the daily execution limit for your agent. By default, this value is set to 250,000, but can be raised to 1,000,000. If you're interested in increasing the limit above 1,000,000, contact your customer success manager to learn more.

### Step 4: Select the output {#select-output}

In the **Output** section, you can organize and define the agent's output by basic schemas or advanced schemas.

For best results, make sure that what you specify in the **Output** section matches any agent instructions you entered in [Step 3](#agent-instructions). For example, if you mentioned in the agent instructions that you want an object with two strings, make sure you specify an object with two strings in the **Output** section. If your agent instructions don't align with your specified output, the agent may get confused, time out, or generate undesired outputs.

#### Basic schemas

Basic schemas are a simple output that an agent returns. This can be a string, a number, a boolean, an array of strings, or array of numbers.

For example, if you want to collect user sentiment scores from a simple feedback survey to determine how satisfied your customers are after receiving a product, you can select **Number** as a basic schema to structure the output format.

{% alert important %}
Arrays are only available for Canvas agents, not catalog agents.
{% endalert %}

![Agent Console with number selected as a basic schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Advanced schemas

Advanced schema options include manually structuring fields or using JSON.

- **Fields:** A no-code way to enforce an agent output that you can use consistently.
- **JSON:** A code approach to creating a precise output format, where you can nest variables and objects within the JSON schema. Only available for Canvas agents, not catalog agents.

We recommend using advanced schemas when you want the agent to return a data structure with multiple values defined in a structured manner, rather than a single-value output. This allows the output to be better formatted as a consistent context variable.

For example, you may use an output format within an agent that is intended to create a sample travel itinerary for a user based on a form they submitted. The output format allows you to define that every agent response should come back with values for `tripStartDate`, `tripEndDate`, and `destination` values. Each of these values can be extracted from context variables and placed in a Message step for personalization using Liquid.

{% tabs %}
{% tab Fields %}

If you want to format responses to a simple feedback survey to determine how likely respondents are to recommend your restaurant's newest ice cream flavor, you can set up the following fields to structure the output format:

| Field name | Value |
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | String |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agent Console showing three output fields for likelihood score, explanation, and confidence score.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

If you want to collect user feedback for their most recent dining experience at your restaurant chain, you can select **JSON Schema** as the output format and insert the following JSON to return a data object that includes a sentiment variable and reasoning variable.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

### Step 5: Test and create the agent

The **Preview** pane is an instance of the agent that shows up as a side-by-side panel within the configuration experience. You can use it to test the agent while you're creating or making updates to it to experience it in a similar way to end users. This step helps you confirm that it’s behaving the way you expect, and gives you a chance to fine-tune before it goes live.

1. In the **Test your agent** field, enter example customer data or customer responses—anything that reflects real scenarios your agent will handle.
2. Preview the agent's response for a random user, existing user, or custom user.
3. Select **Simulate response**. The agent will execute based on your configuration and display its response. Test runs count toward your daily execution limit.

![Agent Console showing the Preview pane for testing a custom agent. The interface displays a Sample inputs field with example customer data, a Run test button, and a response area where the agent output appears.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Review the output with a critical eye. Consider the following questions:

- Does the copy feel on brand?
- Does the decision logic route customers as intended?
- Are the calculated values accurate?

If something feels off, update the agent’s configuration and test again. Run a few different inputs to see how the agent adapts across scenarios, especially edge cases like no data or invalid responses.

### Step 6: Use your agent

Your agent is now ready to use! For details, refer to [Deploy agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Related articles  

- [Reference for agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
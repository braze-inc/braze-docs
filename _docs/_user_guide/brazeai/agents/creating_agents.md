---
nav_title: Create agents
article_title: Create custom agents
description: "Learn how to create agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management."
page_order: 1
alias: /creating-agents/
---

# Create custom agents

> Learn how to create custom agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management. For more general information, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Braze Agents are currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

## Prerequisites

Before you start, you'll need the following:

- Access to the **Agent Console** in your workspace. Check with your Braze admins if you don’t see this option.  
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

### Step 1: Set up details

To create your custom agent:

1. Go to **Agent Console** > **Agent Management** in the Braze dashboard.  
2. Select **Create agent**.
3. Enter a name and description to help your team understand its purpose.
4. (optional) Add tags to filter your agent.
5. Select the interaction site, which is the location where the agent is deployed. Note that the interaction site can't be updated after an agent is created.
6. Choose the [model]({{site.baseurl}}/docs/user_guide/brazeai/agents/reference/#models) your agent will use.

![Agent Console interface for creating a custom agent in Braze. The screen displays fields for entering the agent name and description, and selecting a model.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

### Step 2: Write the instructions

Give the agent instructions. Refer to the [Agents reference]({{site.baseurl}}/user_guide/brazeai/agents/reference/) for guidance.

{% alert tip %}
You can use Liquid in your instructions to reference user attributes, such as their first and last name, or custom attributes.
{% endalert %}

#### Step 2.1: Add context

Select **Add context** to choose what your agent can reference. This includes:

- [Catalog fields]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Provide catalog fields for the agent to reference.
- [Segment membership]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Consider a user's membership in a segment when personalizing messages. You can select up to three segments.
- [Brand guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Reference the brand voice and style guidelines for the agent to follow. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.
- [All Canvas Context variables]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analyze all Canvas Context variables for a user when this agent is invoked, including any that are not referenced in the **Instructions** section.

#### Step 2.2: Add optional settings

In the **Optional settings**, you can adjust the [temperature]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) of the agent-generated copy. A higher temperature allows the agent to use the information provided to be more creative.

You can also set the daily execution limit for your agent. By default, this value is set to 50,000, but can be raised to 100,000. If you're interested in increasing the limit above 100,000, contact your customer success manager to learn more.

### Step 3: Select the output

In the **Output** section, you can organize and define the agent's output by basic schemas or advanced schemas.

#### Basic schemas

Basic schemas are a simple output that an agent returns. This can be a string, a number, a boolean, an array of strings, or array of numbers.

Let's say you want to collect user sentiment scores from a simple feedback survey to determine how satisfied your customers are after receiving a product. You can select **Number** as a basic schema to structure the output format.

{% alert important %}
Arrays are only available for Canvas agents, not catalog agents.
{% endalert %}

![Agent Console with number selected as a basic schema.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Advanced schemas

Advanced schema options include manually structuring fields or using JSON.

- **Fields:** A no-code way to enforce an agent output that you can use consistently. 
- **JSON:** A code approach to creating a precise output format, where you can nest variables and objects within the JSON schema.

{% tabs %}
{% tab Fields %}

Let's say you want to format responses to a simple feedback survey to determine how likely respondents are to recommend your restaurant's newest ice cream flavor. You can set up the following fields to structure the output format:

| Field name | Value
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | Text |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agent Console showing three output fields for likelihood score, explanation, and confidence score.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Let's say you want to collect user feedback for their most recent dining experience at your restaurant chain. You could select **JSON Schema** as the output format and insert the following JSON to return a data object that includes a sentiment variable and reasoning variable.

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

### Step 4: Test and create the agent

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

### Step 5: Use and monitor your agent

Your agent is now ready to use! For details, refer to [Deploy agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

In the **Logs** tab of your agent, you can monitor actual agent calls that occur in your Canvases and catalogs. You can filter by information such as the date range, outcome (success or failure), or calling location.

![Logs for an agent Story Teller, which include when and where the agent has been called.]({% image_buster /assets/img/ai_agent/agent_activity_logs.png %})

Select **View** for a specific agent call to see the input, output, and user ID.

![Logs for an agent Story Teller. The details panel shows the input prompt, output response, and an associated user ID.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

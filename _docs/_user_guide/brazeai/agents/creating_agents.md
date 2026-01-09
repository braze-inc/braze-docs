---
nav_title: Create agents
article_title: Create custom agents
description: "Learn how to create agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management."
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

To create your custom agent:  

1. Go to **Agent Console** > **Agent Management** in the Braze dashboard.  
2. Select **Create agent**.  
3. Enter a name and description to help your team understand its purpose.
4. Choose the [model](#models) your agent will use.  

![Agent Console interface for creating a custom agent in Braze. The screen displays fields for entering the agent name and description, and selecting a model.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

{:start="5"}
5. Give the agent instructions. Refer to [Writing instructions](#writing-instructions) for guidance.
6. [Test the agent](#testing-your-agent) output and adjust the instructions as needed.
7. When you’re ready, select **Create Agent** to activate the agent. 

Your agent is now ready to use! For details, see [Deploy agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Models

When you set up an agent, you can choose the model it uses to generate responses. You have two options: using a Braze-powered model or bringing your own API key.

{% alert important %}
When using the Braze-powered **Auto** model, we have optimized for models whose thinking capabilities is sufficient to perform tasks such as catalog search and user segmentation membership. When using other models, we recommend testing to confirm your model works well for your use case. You may need to adjust your [instructions](#writing-instructions) to give different levels of detail or step-by-step thinking to models with different speeds and capabilities.
{% endalert %}

### Option 1: Use a Braze-powered model

This is the simplest option, with no extra setup required. Braze provides access to large language models (LLM) directly. To use this option, select **Auto**, which uses Gemini models.

### Option 2: Bring your own API key

With this option, you can connect your Braze account with providers like OpenAI, Anthropic, AWS Bedrock, or Google Gemini. If you bring your own API key from an LLM provider, costs are billed directly through your provider, not from Braze.

{% alert important %}
We recommend routinely testing the most recent models, as legacy models may be discontinued or deprecated after a few months.
{% endalert %}

To set this up:

1. Go to **Partner Integrations** > **Technology Partners** and find your provider.
2. Enter your API key from the provider.
3. Select **Save**.

Then, you can return to your agent and select your model.

## Writing instructions

Instructions are the rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. System instructions can be up to 25 KB.

Here are some general best practices to get you started with prompting:

1. Start with the end in mind. State the goal first.
2. Give the model a role or persona ("You are a ...").
3. Set clear context and constraints (audience, length, tone, format).
4. Ask for structure ("Return JSON/bullet list/table...").
5. Show, don't tell. Include a few high-quality examples.
6. Break complex tasks into ordered steps ("Step 1... Step 2...").
7. Encourage reasoning ("Think aloud, then answer").
8. Pilot, inspect, and iterate. Small tweaks can lead to big quality gains.
9. Handle the edge cases, add guardrails, and add refusal instructions.
10. Measure and document what works internally for reuse and scaling.

We recommend also including a default as a catch-all response if the agent receives a response that can't be parsed. This error handling allows the agent to inform you of an unknown outcome variable. For example, rather than asking the agent for only "positive" or "negative" sentiment values, ask it to return "unsure" if it can't decide.

### Simple prompt

This example prompt takes a survey input and outputs a simple sentiment analysis:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Complex prompt 

This example prompt takes a survey input from a user and classifies it into a single sentiment label. The result can then be used to route users down different Canvas paths (such as positive versus negative feedback) or store the sentiment as a custom attribute on their profile for future targeting.

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}

For more details on prompting best practices, refer to guides from the following model providers:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

### Output format

Use the **Output Format** field to organize and define the agent's output by manually structuring fields or using JSON. Setting up an output format with fields is a no-code way to enforce an agent output that you can use consistently. Using JSON allows you to use code to prescribe a more precise output format, where you can nest variables and objects within the JSON schema.

#### Fields

Let's say you want to format responses to a simple feedback survey to determine how likely respondents are to recommend your restaurant's newest ice cream flavor. You can set up the following fields to structure the output format:

| Field name | Value
| --- | --- |
| **likelihood_score** | Number |
| **explanation** | Text |
| **confidence_score** | Number |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Agent Console showing three output fields for likelihood score, explanation, and confidence score.]( {% image_buster /assets/img/ai_agent/output_format_fields.png %} )

### JSON schema

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

If you try to use an agent with a JSON output in a catalog, it will not follow your schema. Instead, consider using the [defined output fields](#fields).

{% alert important %}
Output formats aren't currently supported by Claude AI. If you're using an Anthropic key, we recommend manually adding the structure to the agent prompt.
{% endalert %}

## Optional settings

### Brand guidelines

You can select [brand guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) for your agent to adhere to in its responses. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.

### Catalogs

Choose specific catalogs for an agent to reference and to give your agent the context it needs to understand your products and other non-user data when relevant.

![The "restaurants" catalog and "Loyalty_Program" column selected for the agent to search.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

### Segment membership context

You can select up to three segments for the agent to cross-reference each user's segment membership against when the agent is used in a Canvas. Let's say your agent has segment membership selected for a "Loyalty Users" segment, and the agent is used in a Canvas. When users enter an Agent step, the agent can cross-reference if each user is a member of each segment you specified in the agent console, and use each user's membership (or non-membership) as context for the LLM.

![The "Loyalty Users" segment selected for agent membership access.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

### Temperature

If your goal is to use an agent to generate copy to encourage users to log into your mobile app, you can set a higher temperature for your agent to be more creative and use the nuances of the context variables. If you're using an agent to generate sentiment scores, it may be ideal to set a lower temperature to avoid any agent speculation on negative survey responses. We recommend testing this setting and reviewing the agent's generated output to fit your scenario.

{% alert note %}
Temperatures aren't currently supported for use with OpenAI.
{% endalert %}

## Test your agent

The **Live preview** pane is an instance of the agent that shows up as a side-by-side panel within the configuration experience. You can use it to test the agent while you're creating or making updates to it to experience it in a similar way to end users. This step helps you confirm that it’s behaving the way you expect, and gives you a chance to fine-tune before it goes live.

![Agent Console showing the Live preview pane for testing a custom agent. The interface displays a Sample inputs field with example customer data, a Run test button, and a response area where the agent output appears.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. In the **Sample inputs** field, enter example customer data or customer responses—anything that reflects real scenarios your agent will handle. 
2. Select **Run test**. The agent will execute based on your configuration and display its response. Test runs count toward your daily execution limit.

Review the output with a critical eye. Consider the following questions:

- Does the copy feel on brand? 
- Does the decision logic route customers as intended? 
- Are the calculated values accurate? 

If something feels off, update the agent’s configuration and test again. Run a few different inputs to see how the agent adapts across scenarios, especially edge cases like no data or invalid responses.

### Monitor your agent

In the **Logs** tab of your agent, you can monitor actual agent calls that occur in your Canvases and catalogs. You can filter by information such as the date range, outcome (success or failure), or calling location.

![Logs for an agent Random Sport Assignment, which include when and where the agent has been called.]( {% image_buster /assets/img/ai_agent/agent_activity_logs.png %} )

Select **View** for a specific agent call to see the input, output, and user ID.

![Logs for an agent City Trends and Recommendation Booking. The details panel shows the input prompt, output response, and an associated user ID.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )
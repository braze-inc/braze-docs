---
nav_title: Creating agents
article_title: Creating custom agents
description: "Learn how to create agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management."
alias: /creating-agents/
---

# Creating custom agents

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

## Create an agent

To create your custom agent:  

1. Go to **Agent Console** > **Agent Management** in the Braze dashboard.  
2. Select **Create agent**.  
3. Enter a name and description to help your team understand its purpose.  
4. Choose the [model](#models) your agent will use.  

![Agent Console interface for creating a custom agent in Braze. The screen displays fields for entering the agent name and description, and selecting a model.]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. Give the agent instructions. Refer to [Writing instructions](#writing-instructions) for guidance.
6. [Test the agent](#testing-your-agent) output and adjust the instructions as needed.
7. When you’re ready, select **Create Agent** to activate the agent. 

## Next step

Your agent is now ready to use! For details, see [Deploying agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/). 

## Reference

### Models

When you set up an agent, you'll choose the model it uses to generate responses. You have two options:

#### Option 1: Use a Braze-powered model

This is the simplest option, with no extra setup required. Braze provides access to large language models (LLM) directly. To use this option, select **Auto**.

{% alert note %}
If you use the Braze-powered LLM, you will not incur any cost during the Beta period. Invocation is limited to 50,000 runs per day and 500,000 runs in total. See [Limitations]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) for details.
{% endalert %}

#### Option 2: Bring your own API key

With this option, you can connect your Braze account with providers like OpenAI, Anthropic, AWS Bedrock, or Google Gemini. If you bring your own API key from an LLM provider, costs are billed directly through your provider, not from Braze.

To set this up:
1. Go to **Partner Integrations** > **Technology Partners** and find your provider.
2. Enter your API key from the provider.
3. Select **Save**.

Then, you can return to your agent and select your model.

### Writing instructions

Instructions are the rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. System instructions can be up to 10 KB.

{% tabs %}
{% tab Best practices %}

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

For more details on prompting best practices, refer to guides from the following model providers:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

This example prompt takes a survey input and outputs a simple sentiment analysis:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

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
{% enddetails %}

{% endtab %}
{% endtabs %}

### Brand guidelines

You can select [brand guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) for your agent to adhere to in its responses. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.

### Temperature

If your goal is to use an agent to generate copy to encourage users to log into your mobile app, you can set a higher temperature for your agent to be more creative and use the nuances of the context variables. If you're using an agent to generate copy for user sentiment analysis, it may be ideal to set a lower temperature to avoid any agent speculation on negative survey responses. We recommend testing this setting and reviewing the agent's generated copy to fit your scenario.

{% alert note %}
Temperatures aren't currently supported for use with OpenAI.
{% endalert %}

### Catalogs

Select from a list of catalogs for your agent to reference and further personalize your message.

{% alert note %}
Currently, for an agent to be able to reference a desired column of a catalog, that column must exist in at least one [selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) of the catalog.
{% endalert %}

### Output format

Use the **Output format** field to organize and define the agent's output by manually structuring fields or using JSON. 

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

{% alert note %}
Output formats aren't currently supported by Claude AI. If you're using an Anthropic key, we recommend manually adding the structure to the agent prompt.
{% endalert %}

#### Testing your agent  

The **Live preview** pane is an instance of the agent that shows up as a side-by-side panel within the configuration experience. You can use it to test the agent while you're creating or making updates to it to experience it in a similar way to end users. This step helps you confirm that it’s behaving the way you expect, and gives you a chance to fine-tune before it goes live.

![Agent Console showing the Live preview pane for testing a custom agent. The interface displays a Sample inputs field with example customer data, a Run test button, and a response area where the agent output appears.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. In the **Sample inputs** field, enter example customer data or customer responses—anything that reflects real scenarios your agent will handle. 
2. Select **Run test**. The agent will execute based on your configuration and display its response. Test runs count toward your daily and total invocation limit.

Review the output with a critical eye. Consider the following questions:

- Does the copy feel on brand? 
- Does the decision logic route customers as intended? 
- Are the calculated values accurate? 

If something feels off, update the agent’s configuration and test again. Run a few different inputs to see how the agent adapts across scenarios, especially edge cases like no data or invalid responses.

#### Monitoring your agent

In the **Logs** tab of your agent, you can monitor actual agent calls that occur in your Canvases and catalogs. This includes information such as the timestamp, calling location, duration, and token count. Select **View** for a specific agent call to see the input, output, and user ID.

![Logs for an agent City Trends and Recommendation Booking, which include when and where the agent has been called. The details panel shows the input prompt, output response, and an associated user ID.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )
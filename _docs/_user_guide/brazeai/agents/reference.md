---
nav_title: Reference
article_title: Agents reference
description: "Reference key details about Braze Agents."
page_order: 3
---

# Agents reference

> As you create custom agents, refer to this article for more information on key settings, such as instructions and output schemas. For an introduction, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

{% alert important %}
Braze Agents are currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

## Models

When you set up an agent, you can choose the model it uses to generate responses. You have two options: using a Braze-powered model or bringing your own API key.

{% alert important %}
The Braze-powered **Auto** model is optimized for models whose thinking capabilities are sufficient to perform tasks such as catalog search and user segmentation membership. When using other models, we recommend testing to confirm your model works well for your use case. You may need to adjust your [instructions](#writing-instructions) to give different levels of detail or step-by-step thinking to models with different speeds and capabilities.
{% endalert %}

### Option 1: Use a Braze-powered model

This is the simplest option, with no extra setup required. Braze provides access to large language models (LLM) directly. To use this option, select **Auto**, which uses Gemini models.

### Option 2: Bring your own API key

With this option, you can connect your Braze account with providers like OpenAI, Anthropic, AWS Bedrock, or Google Gemini. If you bring your own API key from an LLM provider, token costs are billed directly through your provider, not through Braze.

{% alert important %}
We recommend routinely testing the most recent models, as legacy models may be discontinued or deprecated after a few months.
{% endalert %}

To set this up:

1. Go to **Partner Integrations** > **Technology Partners** and find your provider.
2. Enter your API key from the provider.
3. Select **Save**.

Then, you can return to your agent and select your model.

{% alert important %}
When you use a Braze-provided LLM, the providers of such a model will be acting as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. If you choose to bring your own API key, the provider of your LLM subscription is considered a Third Party Provider under the contract between you and Braze.  
{% endalert %}

## Writing instructions

Instructions are the rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. System instructions can be up to 25 KB.

Here are some general best practices to get you started with prompting:

1. Start with the end in mind. State the goal first.
2. Give the model a role or persona ("You are a ...").
3. Set clear context and constraints (audience, length, tone, format).
4. Ask for structure ("Return JSON/bullet list/table...").
5. Show, don't tell. Include a few high-quality examples.
6. Break complex tasks into ordered steps ("Step 1... Step 2...").
7. Encourage reasoning ("Think through the steps internally, then provide a concise final answer," or "briefly explain your decision").
8. Pilot, inspect, and iterate. Small tweaks can lead to big quality gains.
9. Handle the edge cases, add guardrails, and add refusal instructions.
10. Measure and document what works internally for reuse and scaling.

We recommend also including a default as a catch-all response if the agent receives a response that can't be parsed. This error handling allows the agent to inform you of an unknown outcome variable. For example, rather than asking the agent for only "positive" or "negative" sentiment values, ask it to return "unsure" if it can't decide.

### Simple prompt

This example prompt takes a survey input and outputs a simple sentiment analysis:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
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

### Using Liquid

Including [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) in your agent's instructions can add an extra layer of personalization in its response. You can specify the exact Liquid variable the agent gets and can include it in the context of your prompt. For example, instead of explicitly writing "first name", you can use the Liquid snippet {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

In the **Logs** section of the **Agent Console**, you can review the details for the agent's input and output to understand what value is rendered from the Liquid.

![The details for an agent that has Liquid in its instructions.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## Catalogs and fields

Choose specific catalogs for an agent to reference and to give your agent the context it needs to understand your products and other non-user data when relevant. Agents use tools to find the relevant items only and send those to the LLM to minimize token use.

![The "restaurants" catalog and "Loyalty_Program" column selected for the agent to search.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## Segment membership context

You can select up to three segments for the agent to cross-reference each user's segment membership against when the agent is used in a Canvas. Let's say your agent has segment membership selected for a "Loyalty Users" segment, and the agent is used in a Canvas. When users enter an Agent step, the agent can cross-reference if each user is a member of each segment you specified in the agent console, and use each user's membership (or non-membership) as context for the LLM.

![The "Loyalty Users" segment selected for agent membership access.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## Brand guidelines

You can select [brand guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) for your agent to adhere to in its responses. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.

## Temperature

If your goal is to use an agent to generate copy to encourage users to log into your mobile app, you can set a higher temperature for your agent to be more creative and use the nuances of the context variables. If you're using an agent to generate sentiment scores, it may be ideal to set a lower temperature to avoid any agent speculation on negative survey responses. We recommend testing this setting and reviewing the agent's generated output to fit your scenario.

{% alert note %}
Temperatures aren't currently supported for use with OpenAI.
{% endalert %}
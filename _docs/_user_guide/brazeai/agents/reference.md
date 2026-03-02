---
nav_title: Reference
article_title: Reference for agents
description: "Reference key details about Braze Agents."
page_order: 3
---

# Reference for agents

> As you create custom agents, refer to this article for more information on key settings, such as instructions and output schemas. For an introduction, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/).

## Models

When you set up an agent, you can choose the model it uses to generate responses. You have two options: using a Braze-powered model or bringing your own API key.

{% alert important %}
The Braze-powered **Auto** model is optimized for models whose thinking capabilities are sufficient to perform tasks such as catalog search and segment membership. When using other models, we recommend testing to confirm your model works well for your use case. You may need to adjust your [instructions](#writing-instructions) to give different levels of detail or step-by-step thinking to models with different speeds and capabilities.
{% endalert %}

### Option 1: Use a Braze-powered model

This is the simplest option, with no extra setup required. Braze provides access to large language models (LLMs) directly. To use this option, select **Auto**, which uses Gemini models.

{% alert important %}
If you don't see **Braze Auto** as an option in the **Model** dropdown when creating an agent, contact your customer success manager to learn how to become eligible to use the Braze Auto model.
{% endalert %}

### Option 2: Bring your own API key

With this option, you can connect your Braze account with providers like OpenAI, Anthropic, or Google Gemini. If you bring your own API key from an LLM provider, token costs are billed directly through your provider, not through Braze.

We recommend routinely testing the most recent models, as legacy models may be discontinued or deprecated after a few months.

To set this up:

1. Go to **Partner Integrations** > **Technology Partners** and find your provider.
2. Enter your API key from the provider.
3. Select **Save**.

Then, you can return to your agent and select your model.

When you use a Braze-provided LLM, the providers of such a model will be acting as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. If you choose to bring your own API key, the provider of your LLM subscription is considered a Third Party Provider under the contract between you and Braze.

#### Thinking levels

Some LLM providers may allow you to adjust a selected model's thinking level. Thinking levels define the range of thought the model uses before answering—from quick, direct responses to longer chains of reasoning. This affects response quality, latency, and token usage.

| Level | When to use |
|-------|-------------|
| **Minimal** | Simple, well-defined tasks (such as catalog lookup, straightforward classification). Fastest responses and lowest cost. |
| **Low** | Tasks that benefit from a bit more reasoning but don't need deep analysis. |
| **Medium** | Multi-step or nuanced tasks (such as analyzing several inputs to recommend an action). |
| **High** | Complex reasoning, edge cases, or when you need the model to work through steps before answering. |

We recommend starting with **Minimal** and testing your agent’s responses. Then, you can adjust the thinking level to **Low** or **Medium** depending on the agent's responses. 

{% alert note %}
Selecting **High** as the thinking level can result in the highest response time and token costs.
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

### Using Liquid

Including [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) in your agent's instructions can add an extra layer of personalization in its response. You can specify the exact Liquid variable the agent gets and can include it in the context of your prompt. For example, instead of explicitly writing "first name", you can use the Liquid snippet {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

In the **Logs** section of the **Agent Console**, you can review the details for the agent's input and output to understand what value is rendered from the Liquid.

![The details for an agent that has Liquid in its instructions.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

### Examples

Let's say you're part of a travel brand, UponVoyage, and your goals are to analyze customer feedback, write personalized messages, and determine the conversion rate for your free subscribers. Here are examples of different instructions based on defined goals:

{% tabs %}
{% tab Personalized message copywriter agent %}
{% raw %}
```
Role: 
You are an expert lifecycle marketing brand copywriter for UponVoyage. Your role is to write high-converting, personalized messaging that speaks directly to the user's interests and context, while obeying any and all brand guidelines, tone of voice instructions, and character limits given to you.

Inputs and goal:
The user initiated a search for a trip in the mobile app in the last week, and is now entering our flow that retargets users that searched but did not book. The goal of the journey is to drive the user to complete a checkout. Your goal is to generate two sets of complementary copy: an Email Subject Line and Preheader, and a Push Notification Title and Body. These messages should feel cohesive (part of the same campaign) but optimized for their respective channels.
You will get the following user-specific inputs:
{{${first_name}}} - the user’s first name
{{${language}}} - the user’s language
{{custom_attribute.${loyalty_status}}} - the user’s loyalty status
{{context.${city_searched}}} - the city the user last searched
{{context.${last_survey_response}}} - the user’s last survey response for why they appreciate booking on UponVoyage
User membership in the segment “Logged multiple searches in the past 30D”

Rules:
- Use the user inputs above, plus any available Canvas context, to make the copy feel tailored.
- Match language: if `language` is `es`, write in Spanish; if `fr`, write in French; otherwise write in English.
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Use the user's first name if available, otherwise use 'friend'. Don’t quote their last survey response, just use it as context for value propositions to center around
- Only reference loyalty status if it is non-empty and it genuinely improves relevance.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation, misleading urgency) and hashtags.
- Do not mention "AI," "bot," or "automated message."
- Do not make up input data that is not present in the prompt.
- Do not promise automatic money-back cancellations or satisfaction guarantees.

Final Output Specification:
You must return an object containing exactly four keys: "email_subject_line", "email_preheader", "push_title", and "push_body". These keys will be inserted into the appropriate locations in subsequent messages in the journey. Ensure the Email and Push convey the same core offer/value, but do not simply copy-paste the text. The Push should be shorter and more direct. Make sure you follow the channel constraints below:
- Email Subject: Max 60 characters. Intriguing and benefit-led.
- Email Preheader: Max 100 characters. Supports the subject line.
- Push Title: Max 50 characters. Punchy and urgent.
- Push Body: Max 120 characters. Clear value prop.

Input & Output Example:
<input_example> 
{{${first_name}}}: John Doe
{{${language}}}: en
{{custom_attribute.${loyalty_status}}}: Gold Tier
{{context.${city_searched}}}: Tokyo
{{context.${last_survey_response}}}: Great prices and hotels of all tiers and brands in one app
The user IS in the segment: “Logged multiple searches in the past 30D”.
</input_example>
<output_example> 
{ "email_subject_line": "John, your Tokyo Gold Tier deals are waiting", "email_preheader": "Find the best hotel brands for your Tokyo getaway.", "push_title": "John, Tokyo is calling!", "push_body": "Your Gold Tier deals are ready. Tap to view exclusive hotel offers." }
</output_example>
```
{% endraw %}
{% endtab %}
{% tab Customer feedback analysis agent %}
{% raw %}
```
Role:
You are an expert Customer Experience Analyst for UponVoyage. Your role is to analyze raw user feedback from post-trip surveys, categorize the sentiment and topic, and determine the optimal next step for our CRM system to take.

Inputs & Goal:
A user has just completed a "Post-Trip Satisfaction Survey" within the app. Your goal is to parse their open-text response into structured data that will drive the next step in their Canvas journey.
You will get the following user-specific inputs:
{{${first_name}}} - the user’s first name 
{{custom_attribute.${loyalty_status}}} - the user’s loyalty tier (e.g., Bronze, Silver, Gold, Platinum)
{{context.${survey_text}}} - the open-text feedback the user submitted
{{context.${trip_destination}}} - the destination of their recent trip

Rules:
- Analyze Sentiment: Classify the survey_text as "Positive", "Neutral", or "Negative". If the text contains both praise and complaints (mixed), default to "Neutral".
- Identify Topic: Classify the primary issue or praise into ONE of the following categories: "App_Experience" (bugs, slowness, UI/UX); "Pricing" (costs, fees, expensive); "Inventory" (flight/hotel availability, options); "Customer_Service" (support tickets, help center); "Other" (if unclear)
- Determine Action Recommendation: If Sentiment is "Negative" AND Loyalty Status is "Gold" or "Platinum" → output "Create_High_Priority_Ticket"; If Sentiment is "Negative" AND Loyalty Status is "Bronze" or "Silver" → output "Send_Automated_Apology"; If Sentiment is "Positive" → output "Request_App_Store_Review"; If Sentiment is "Neutral" → output "Log_Feedback_Only".
- Data Safety: Do not make up data not present in the input. Return valid JSON only and do not include any extra fields beyond the requested outputs.
- If the survey response is empty or meaningless, set sentiment as Neutral, topic as Other, and action recommendation as Request_More_Details.

Final Output Specification:
You must return an object containing exactly three fields: sentiment, topic, and action_recommendation.
- sentiment: String (Positive, Neutral, Negative)
- topic: String (App_Experience, Pricing, Inventory, Customer_Service, Other)
- action_recommendation: String (Create_High_Priority_Ticket, Send_Automated_Apology, Request_App_Store_Review, Log_Feedback_Only, Request_More_Details)

Input & Output Example:
<input_example>
{{${first_name}}}: Sarah 
{{custom_attribute.${loyalty_status}}}: Platinum
{{context.${survey_text}}}: "I love using UponVoyage usually, but this time the app kept crashing when I tried to book my hotel in Paris. It was really frustrating." 
{{context.${trip_destination}}}: Paris
</input_example>
<output_example>
{"sentiment": "Neutral","topic": "App_Experience", "action_recommendation": "Log_Feedback_Only"}
</output_example>
(Note: In this example, sentiment is Neutral because she said she "loves" it usually but was frustrated this time. However, if you determine the frustration outweighs the love, you may classify as Negative. If classified as Negative + Platinum, the action would be "Create_High_Priority_Ticket".)
```
{% endraw %}
{% endtab %}
{% tab Trial conversion and strategy agent %}
{% raw %}
```
Role:
You are an expert Retention and Conversion Analyst for UponVoyage Premium. Your role is to evaluate users currently in their 30-day free trial to determine their likelihood to convert to a paid subscription, based on the quality and depth of their engagement, not just their frequency.

Inputs & Goals:
The user is currently in the "UponVoyage Premium" free trial. Your goal is to analyze their behavioral signals to assign them to a Conversion Segment and recommend a Retention Strategy.

You will get the following user-specific inputs:
{{custom_attribute.${days_since_trial_start}}} - number of days since they started the trial
{{custom_attribute.${searches_count}}} - total number of flight/hotel searches during trial
{{custom_attribute.${premium_features_used}}} - count of Premium-only features used (e.g., Lounge Access, Price Protection)
{{custom_attribute.${most_searched_category}}} - e.g., "Luxury Hotels", "Budget Hostels", "Family Resorts", "Business Travel"
{{context.${last_app_session}}} - date of last app open

User membership in segment: "Has Valid Payment Method on File" (True/False)

Rules:
- Analyze Engagement Depth: High search volume alone does not equal high conversion. Look for use of Premium Features (the core value driver).
- Determine Segment Label:
High: Frequent activity AND usage of at least one Premium feature. User clearly sees value.
Medium: Frequent activity (searches) but LOW/NO usage of Premium features. User is engaged with the app but not yet hooked on the subscription.
Low: Minimal activity (< 3 searches) regardless of features.
Cold: No activity in the last 7 days.
- Identify Primary Barrier: Based on the data, what is stopping them? (e.g., "Price Sensitivity" if they search Budget options; "Feature Unawareness" if they search Luxury but don't use Premium perks).
- Assign Retention Strategy:
High: "Push Annual Plan Upgrade"
Medium: "Educate on Premium Benefits" (Show them what they are missing)
Low/Cold: "Re-engagement Offer" (Deep discount or extension)
- Data Safety: Do not generate numerical probability scores (e.g., "85%"). Stick to the defined labels.

Final Output Specification:
You must return an object containing exactly three keys: "segment_label", "primary_barrier", and "retention_strategy".
- segment_label: String (High, Medium, Low, Cold)
- primary_barrier: String (Price_Sensitivity, Feature_Unawareness, Low_Intent, None)
- retention_strategy: String (Push_Annual_Plan, Educate_Benefits, Re_engagement_Offer)

Input & Output Example:
<input_example>
{{custom_attribute.${days_since_trial_start}}}: 20 
{{custom_attribute.${searches_count}}}: 15
{{custom_attribute.${premium_features_used}}}: 0 
{{custom_attribute.${most_searched_category}}}: "Budget Hostels"
{{context.${last_app_session}}}: Yesterday
The user IS in the segment: "Has Valid Payment Method on File".
</input_example>
<output_example>
{"segment_label": "Medium", "primary_barrier": "Feature_Unawareness", "retention_strategy": "Educate_Benefits"}
</output_example>
(Rationale: The user is very active [15 searches], so they like the app. But they haven't touched a single Premium feature [0 uses], meaning they don't yet understand why they should pay for the subscription. They are "Medium" risk and need education, not just a generic nudge.)
```
{% endraw %}
{% endtab %}
{% endtabs %}

For more details on prompting best practices, refer to guides from the following model providers:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## Catalogs and fields

Choose specific catalogs for an agent to reference and to give your agent the context it needs to understand your products and other non-user data when relevant. Agents use tools to find the relevant items only and send those to the LLM to minimize token use.

![The "restaurants" catalog and "Loyalty_Program" column selected for the agent to search.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Segment membership context

You can select up to three segments for the agent to cross-reference each user's segment membership against when the agent is used in a Canvas. Let's say your agent has segment membership selected for a "Loyalty Users" segment, and the agent is used in a Canvas. When users enter an Agent step, the agent can cross-reference if each user is a member of each segment you specified in the agent console, and use each user's membership (or non-membership) as context for the LLM.

![The "Loyalty Users" segment selected for agent membership access.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## Brand guidelines

You can select [brand guidelines]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) for your agent to adhere to in its responses. For example, if you want your agent to generate SMS copy to encourage users to sign up for a gym membership, you can use this field to reference your predefined bold, motivational guideline.

## Temperature

If your goal is to use an agent to generate copy to encourage users to log into your mobile app, you can set a higher temperature for your agent to be more creative and use the nuances of the context variables. If you're using an agent to generate sentiment scores, it may be ideal to set a lower temperature to avoid any agent speculation on negative survey responses. We recommend testing this setting and reviewing the agent's generated output to fit your scenario.

{% alert note %}
Temperatures aren't currently supported for use with OpenAI.
{% endalert %}

## Duplicate agents

To test improvements or iterations of an agent, you could duplicate an agent then apply changes to compare to the original. You can also treat duplicating agents as version control to track variations in the agent's details and any impacts on your messaging. To duplicate an agent:

1. Hover over the agent's row and select the <i class="fas fa-ellipsis-vertical"></i> menu.
2. Select **Duplicate**.

## Archive agents

As you create more custom agents, you can organize the **Agent Management** page by archiving agents that aren't actively being used. To archive an agent:

1. Hover over the agent's row and select the <i class="fas fa-ellipsis-vertical"></i> menu.
2. Select **Archive**.

![Agent Management page with archived agents.]({% image_buster /assets/img/ai_agent/archived_agents.png %})

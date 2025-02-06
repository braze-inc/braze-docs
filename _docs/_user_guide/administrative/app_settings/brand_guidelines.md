---
nav_title: Brand Guidelines
article_title: Brand Guidelines
page_order: 1
page_type: reference
description: "This reference article describes how to create, manage, and use brand buidelines that can be applied to your messages through the AI copywriting assistant."
---

# Brand guidelines

> Tailor the style of your AI-generated copy to match your brand’s voice, tone, and personality with customized brand guidelines.

You can create and manage your brand guidelines by going to **Settings** > **Brand Guidelines**. You can also create them in the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).

## Creating brand guidelines

### Step 1: Create a brand guideline

On the **Brand Guidelines** page, select **Create new**. If you want this brand guideline to be the default for the workspace, check **Use as default brand guideline**. You can have one default per workspace.

### Step 2: Describe your brand personality

For **Brand personality**, think about what makes your brand unique. Include traits, values, voice, and any archetypes that define your brand. Here are some characteristics to consider:

| **Characteristic**       | **Definition**                                                                       | **Example**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputation               | How you want your brand to be perceived in the market.                               | We are known for being the most reliable and customer-focused brand in our industry. |
| Personality traits       | Human-like characteristics that describe your brand’s character.                     | Our brand is friendly, approachable, and always upbeat.          |
| Values                   | Core values that guide your brand’s actions and decisions.                           | We value sustainability, transparency, and community.            |
| Differentiation          | Unique qualities that set your brand apart from competitors.                         | We stand out by offering personalized customer service that goes above and beyond. |
| Brand voice              | The tone and style of communication your brand uses.                                 | Our voice is casual yet informative, ensuring clarity without being too formal. |
| Brand archetype          | The archetype that represents your brand’s persona (The Hero, The Creator, and so on).    | We embody the ‘Explorer’ archetype, always seeking new challenges and adventures. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 3: Define language that should be avoided (optional)

For **Exclusions**, list any language or style that doesn’t align with your brand. For example, you might want to avoid "sarcasm," "negative attitudes," or "condescending" tones.

![The "Create brand guideline" window with fields to enter the name, description, personality, exclusions, and tone.][1]

### Step 4: Test your guidelines

Test your guidelines to see how they perform. Expand **Test your guidelines** to generate example copy and adjust as needed.

### Step 5: Save your guidelines

When you're happy with your guidelines, select **Save brand guideline**. Your new guidelines will be saved in your workspace for future use.

{% alert important %}
You can change the output language regardless of what language your copy is in, but neither Braze nor OpenAI guarantees the quality of translation. Always test and verify translations before using them.
{% endalert %}

## Managing brand guidelines

You can edit brand guidelines by selecting them on the **Brand Guidelines** page. Archive a brand guideline to make it inactive and remove it from the AI copywriting assistant. To make it active and selectable again, you can filter for archived brand guidelines and then unarchive it.

![The "Brand Guidelines" page filtered for archived brand guidelines.][4]

## Using brand guidelines

When composing a message, open the [AI copywriting assistant]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/) and select your brand guideline in the **Apply brand guideline** dropdown. If you designate a specific brand guideline as the default, it will automatically be selected in the dropdown, but you can choose a different guideline. 

!["AI copywriting assistant with "Important Alerts!!" selected as the brand guideline.][2]

## How is my data used and sent to OpenAI?

To generate copy using a brand guideline, Braze will send your query including the content of your guideline to OpenAI. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the input you provide or in your past campaign data when enabling the option labeled "Reference past campaign data". Per [OpenAI’s policy](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API using Braze is not used to train or improve their models and will be deleted after 30 days. Between you and Braze, any content generated using GPT is your intellectual property. Braze will not assert any claims of copyright ownership on such content and makes no warranty of any kind with respect to any AI-generated content.

[1]: {% image_buster /assets/img/guidelines_create.png %}
[2]: {% image_buster /assets/img/guidelines_ai_assistant.png %}
[4]: {% image_buster /assets/img/unarchive_brand_guideline.png %}
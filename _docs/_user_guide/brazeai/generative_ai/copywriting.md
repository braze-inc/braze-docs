---
nav_title: Copywriting
article_title: AI Copywriting Assistant
page_order: 2.1
description: "This reference article covers the AI copywriting assistant, feature that passes a brief product name or description to OpenAI's GPT copy generation tool to generate human-like marketing copy for use in your messaging."
---

# Generating copy with BrazeAI<sup>TM</sup>

> The AI copywriting assistant passes a brief product name or description to a third-party provider GPT copy generation tool owned by OpenAI to generate human-like marketing copy for use in your messaging. This functionality is available by default for most message composers in the Braze dashboard.

## Generating copy

### Step 1: Launch AI copywriter

From your message composer, select <i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter**.

In the drag-and-drop editor for in-app messages, select a text block and select <i class="fa-solid fa-wand-magic-sparkles" title="AI Copywriter"></i> in the block's toolbar.

### Step 2: Enter the details

Enter a product name or description in the input field, then select an approximate output length.

You can choose a specific channel for an output length based on channel-specific best practices or select between short (1 sentence), medium (2-3 sentences), or long (1 paragraph).

### Step 3: Customize it further (optional)

To customize your copy further, you can:

- **Apply brand guidelines:** After [generating brand guidelines with BrazeAI<sup>TM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), you can use them to help generate your copy.
- **Choose a tone:** Each tone will generate copy in a different style. Choose the tone that best matches your brand voice.
- **Reference past campaign data**: When enabled, previous mobile push notifications sent through your campaigns or Canvas steps are used for stylistic reference to generate your new copy. For more information, see [Using past campaign data](#past-campaign-data).
- **Auto-translate copy:** You can choose a different output language for your copy. Generated content will be output to that language.

### Step 4: Generate your copy

When you're finished, select **Generate**. We'll use the information you provide to prompt GPT to write copy for you. The response will be fetched from OpenAI and provided to you. For more information, see [How is my data used and sent to OpenAI?](#ai-policy).

![AI copywriting assistant modal showing various features available"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
We filter out responses for offensive content that violates OpenAI's [content policy](https://beta.openai.com/docs/usage-guidelines/content-policy).
{% endalert %}

## About past campaign data {#past-campaign-data}

When using push as your output length, if you select **Reference past campaign data**, randomly selected previous mobile push campaigns will be sent to OpenAI so that GPT can use it as a basis for its copy generation. Currently, the AI copywriter pulls campaigns that do not have liquid syntax. Furthermore, this only pulls push campaigns. Leave this box unchecked if you do not want to leverage this ability. See the following sections for more information on how Braze and OpenAI use your data. 

If used in conjunction with a [brand guideline]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), both the brand guideline and the past campaign data will be incorporated into the final output.

{% multi_lang_include brazeai/generative_ai/policy.md %}

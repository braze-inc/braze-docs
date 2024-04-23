---
nav_title: AI Copywriting Assistant
article_title: AI Copywriting Assistant
page_order: 4
description: "This reference article covers the AI Copywriting Assistant, feature that passes a brief product name or description to OpenAI's GPT copy generation tool to generate human-like marketing copy for use in your messaging."
---

# AI copywriting assistant

> The AI copywriting assistant passes a brief product name or description to a third-party provider GPT copy generation tool owned by OpenAI to generate human-like marketing copy for use in your messaging. This functionality is available by default for most message composers in the Braze dashboard.

## Steps

To generate copy using the AI copywriting assistant, follow these steps:

1. From your message composer, select <i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter**.
   * In the drag-and-drop editor for in-app messages, select a text block and select <i class="fa-solid fa-wand-magic-sparkles" title="AI Copywriter"></i> in the block's toolbar.
2. Enter a product name or description in the input field.
3. Select an approximate output length. You can choose a specific channel for an output length based on channel-specific best practices or select between short (1 sentence), medium (2-3 sentences), or long (1 paragraph). 
4. Choose a message tone from the available options. This will determine the style of the copy generated.
5. (Optional) Available for push notifications: Select **Reference past campaign data** to use your previous mobile push messages (campaigns and canvas steps) as a stylistic example to use as a reference for generating new copy. The copywriting assistant will mimic the style of your previous messages.
6. Select the output language. This can be different from your input language.
7. Click **Generate**.

We use the information you provide to prompt GPT to write copy for you. The response will be fetched from OpenAI and provided to you. 

![AI copywriting assistant modal showing various features available"][1]{: style="max-width:70%;"}

{% alert important %}
We filter out responses for offensive content that violates OpenAI's [content policy](https://beta.openai.com/docs/usage-guidelines/content-policy).
{% endalert %}

## Using past campaign data

When using push as your output length, if you select **Reference past campaign data**, randomly selected previous mobile push campaigns will be sent to OpenAI so that GPT can use it as a basis for its copy generation. Leave this box unchecked if you do not want to leverage this ability. See the following sections for more information on how Braze and OpenAI use your data.

## What is GPT?

[GPT](https://openai.com/product/gpt-4) is OpenAI's state of the art natural language generation tool powered by artificial intelligence. It can perform a variety of natural language tasks like text generation, completion, and classification. We've plugged it into the Braze dashboard to help inspire and diversify your copy directly as you work.

## How is my data used and sent to OpenAI?

In order to generate copy, Braze will send your query to OpenAI. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the input you provide or in your past campaign data when enabling the option labeled "Reference past campaign data". Per [OpenAI’s policy](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Between you and Braze, any content generated using GPT is your intellectual property. Braze will not assert any claims of copyright ownership on such content and makes no warranty of any kind with respect to any AI-generated content.

## More AI tools

You can also [generate an image using AI]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) from the media library. This leverages DALL·E 2, an AI system from OpenAI that can create realistic images and art from a description in natural language.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"

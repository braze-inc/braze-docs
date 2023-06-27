---
nav_title: AI Copywriting Assistant
article_title: AI Copywriting Assistant
page_order: 4
description: "This reference article covers the AI Copywriting Assistant, feature that passes a brief product name or description to OpenAI's GPT copy generation tool to generate human-like marketing copy for use in your messaging."

---

# AI copywriting assistant

> The AI copywriting assistant passes a brief product name or description to OpenAI's GPT copy generation tool to generate human-like marketing copy for use in your messaging. This functionality is available by default for most message composers in the Braze dashboard.

## Steps

To generate copy using the AI copywriting assistant, follow these steps:

1. From your message composer, select <i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter**.
   * In the drag-and-drop editor for in-app messages, select a text block and select <i class="fa-solid fa-wand-magic-sparkles" title="AI Copywriter"></i> in the block's toolbar.
2. Enter a product name or description in the input field.
3. Select the output language. This can be different from your input language.
4. Select an approximate output length. 
5. Click **Generate Copy**.

The response will be fetched from OpenAI and provided to you. Feel free to experiment and try variations to your heart's content.

![AI copywriting assistant modal showing the input "Braze Marketing Automation", which generated the output: "Looking to take your marketing to the next level? Braze Marketing Automation is the solution for you! With our powerful tools, you'll be able to create, send, and track your marketing campaigns with ease. So why wait? Sign up today and see the results yourself!"][1]

All we do behind the scenes is instruct GPT to generate a creative ad for your product name or description in the desired format. No other customization is performed. The rest is the magic of GPT!

{% alert important %}
We filter out responses for offensive content that violates OpenAI's [content policy](https://beta.openai.com/docs/usage-guidelines/content-policy).
{% endalert %}

## What is GPT?

[GPT](https://openai.com/product/gpt-4) is OpenAI's state of the art natural language generation tool powered by artificial intelligence. It can perform a variety of natural language tasks like text generation, completion, and classification. We've plugged it into the Braze dashboard to help inspire and diversify your copy directly as you work.

## How is my data used and sent to OpenAI?

Braze sends your query to OpenAI in order to generate copy. We anonymize these requests so OpenAI only sees them as coming from Braze. Nothing that identifies Braze customers is sent in the request, unless you provide such information in your query. Per OpenAI's [policy](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI via Braze is not used to train models and is deleted after 30 days.

## More AI tools

You can also [generate an image using AI]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) from the Media Library. This leverages DALL·E 2, an AI system from OpenAI that can create realistic images and art from a description in natural language.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"

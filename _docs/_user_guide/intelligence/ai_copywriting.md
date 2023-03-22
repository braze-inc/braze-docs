---
nav_title: AI Copywriting Assistant
article_title: AI Copywriting Assistant
page_order: 4
description: "This reference article covers the AI Copywriting Assistant, feature that passes a brief product name or description to OpenAI's GPT copy generation tool to generate human-like marketing copy for use in your messaging."

---

# AI copywriting assistant

The AI copywriting assistant passes a brief product name or description to OpenAI's GPT copy generation tool to generate human-like marketing copy for use in your messaging. This functionality is available by default for most message composers in the Braze dashboard.

## Steps

To generate copy using the AI copywriting assistant, follow these steps:

1. From your message composer, select <i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter**.
2. Enter a product name or description in the input field.
3. Select the output language. This can be different from your input language.
4. Select an approximate output length. 
5. Click **Generate Copy**.

The response will be fetched from OpenAI and provided to you. Feel free to experiment and try variations to your heart's content.

![AI copywriting assistant modal showing the input "Braze Marketing Automation", which generated the output: "Looking to take your marketing to the next level? Braze Marketing Automation is the solution for you! With our powerful tools, you'll be able to create, send, and track your marketing campaigns with ease. So why wait? Sign up today and see the results yourself!"][1]

All we do behind the scenes is ask GPT to "generate marketing copy for" your product name. No other customization is performed. The rest is the magic of GPT!

{% alert important %}
We filter out responses for offensive content that violates OpenAI's [content policy](https://beta.openai.com/docs/usage-guidelines/content-policy).
{% endalert %}

## What is GPT?

[GPT](https://openai.com/product/gpt-4) is OpenAI's state of the art natural language generation tool powered by artificial intelligence. It can perform a variety of natural language tasks like text generation, completion, and classification. We've plugged it into the Braze dashboard to help inspire and diversify your copy directly as you work.

## More AI tools

You can also [generate an image using AI]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) from the Media Library. This leverages DALL·E 2, an AI system from OpenAI that can create realistic images and art from a description in natural language.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"

---
nav_title: AI Copywriting Assistant
article_title: AI Copywriting Assistant
page_order: 4
description: "The AI Copywriting Assistant passes a brief product name or description to OpenAI's GPT3 copy generation tool to generate human-like marketing copy for use in your messaging."

---

# AI copywriting assistant

The AI copywriting assistant passes a brief product name or description to OpenAI's GPT3 copy generation tool to generate human-like marketing copy for use in your messaging. This functionality is available out-of-the-box for most message composers in the Braze dashboard.

From your message composer, select <i class="fa-solid fa-wand-magic-sparkles"></i> **Launch AI Copywriter**, then enter a product name or description in the input field and click **Generate Copy**! The response will be fetched from OpenAI and provided to you. Feel free to experiment and try variations to your heart's content.

![AI copywriting assistant modal showing the input "Braze Marketing Automation", which generated the output: "Looking to take your marketing to the next level? Braze Marketing Automation is the solution for you! With our powerful tools, you'll be able to create, send, and track your marketing campaigns with ease. So why wait? Sign up today and see the results yourself!"][1]

All we do behind the scenes is ask GPT3 to "generate marketing copy for" your product name. No other customization is performed. The rest is the magic of GPT3! 

{% alert important %}
We filter out responses for offensive content that violates OpenAI's [content policy](https://beta.openai.com/docs/usage-guidelines/content-policy).
{% endalert %}

## What is GPT3?

[GPT3](https://openai.com/blog/gpt-3-apps/) is OpenAI's state of the art natural language generation tool powered by artificial intelligence. It can perform a variety of natural language tasks like text generation, completion, and classification. We've plugged it into the Braze dashboard to help inspire and diversify your copy directly as you work.


[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"

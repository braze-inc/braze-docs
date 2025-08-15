---
nav_title: Content qa
article_title: Content QA with AI
page_order: 4
description: "This reference article covers how to perform quality assurance on your message content with AI directly from the message composer."
---

# Content QA with BrazeAI<sup>TM</sup>

> Learn how to QA your content with BrazeAI<sup>TM</sup>, so you can catch spelling errors, grammar issues, inappropriate tone, or offensive language&#8212;before hitting send.

## Supported features

The following features are supported to help improve the quality of your content:

| Feature                     | Description |
|----------------------------|-------------|
| Spelling and grammar check | Automatically checks for spelling and grammar mistakes in your message. It suggests corrections and provides recommendations to improve the overall accuracy of the content. |
| Tone analysis              | Evaluates the tone of the message to identify any potential issues. It helps ensure that the intended tone aligns with the desired communication style and helps avoid misunderstandings or unintended offenses. |
| Offensive language detection | Scans your message for any potentially offensive or inappropriate language, allowing you to revise your content and maintain respectful communication. |
| Accidental content check   | Detects any inclusion of code, markup language, or test messages that might have been added unintentionally, including any Liquid code that didn't render for a test user. |
| Multi-language support     | Although not officially supported by OpenAI, GPT can understand [multiple languages](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages). Keep in mind that Braze doesn't pass any information about the language or locale of your copy when it's sent to OpenAI, so your results may vary depending on the language you're writing in. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Using BrazeAI<sup>TM</sup> to QA content

{% alert note %}
This feature is only available for SMS, Android push, and iOS push channels at this time.
{% endalert %}

1. After composing a mobile push or SMS message, navigate to the **Test** tab.
2. Locate the **Content QA with AI** section.
3. Click **Test Content**.

![Content QA with AI section of the Test tab.]({% image_buster /assets/img/content_qa_ai.png %})

## Best practices

Consider the following, so you can make the most of Content QA with AI:

- **Proofread your message:** Although the content checker can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

{% multi_lang_include brazeai/generative_ai/policy.md %}

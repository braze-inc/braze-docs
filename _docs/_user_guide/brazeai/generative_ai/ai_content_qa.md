---
nav_title: Content QA with AI
article_title: Content QA with AI
page_order: 10
description: "This reference article covers how to perform quality assurance on your message content with AI directly from the message composer."
---

# Content QA with AI

> Learn how to perform quality assurance on your message content with AI directly from the message composer.

Content QA with AI uses the capabilities of GPT and OpenAI to perform checks on the content of your message, ensuring it adheres to quality standards by identifying ineffective elements such as spelling errors, grammar issues, inappropriate tone, and offensive language. You can access this feature from the **Test** tab when composing a push, SMS, or in-app message in a campaign or Canvas.

## Key features

Content QA with AI offers the following key features to enhance the quality of your message content:

- **Spelling and grammar check:** Automatically checks for spelling and grammar mistakes in your message. It suggests corrections and provides recommendations to improve the overall accuracy of the content.
- **Tone analysis:** Evaluates the tone of the message to identify any potential issues. It helps ensure that the intended tone aligns with the desired communication style and helps avoid misunderstandings or unintended offenses.
- **Offensive language detection:** Scans your message for any potentially offensive or inappropriate language, allowing you to revise your content and maintain respectful communication.
- **Accidental content check:** Detects any inclusion of code, markup language, or test messages that might have been added unintentionally, including any Liquid code that didn't render for a test user.

## Accessing Content QA with AI

{% alert note %}
Content QA with AI is only available for push and SMS channels at this time.
{% endalert %}

To access the content checker, follow these steps:

1. After composing a push or SMS message, navigate to the **Test** tab.
2. Locate the **Content QA with AI** section.
3. Click **Test Content**.

![Content QA with AI section of the Test tab.][1]{: style="max-width:60%"}

### Language support

GPT is able to understand [multiple languages](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages), although OpenAI doesn't officially support them. Braze does not pass any additional information about the language or locale of your copy when the message content is sent to OpenAI, therefore it is up to GPT to make that determination.

Results may vary depending on the language you're writing in.

## Tips for effective use

Consider the following tips to make the most of the Content QA with AI feature:

- **Proofread your message:** Although the content checker can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

## How is my data used and sent to OpenAI?

In order to check your message content, Braze will send it to OpenAI's API Platform. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the message content you provide. As detailed in [OpenAI’s API Platform Commitments](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days. Please ensure that you adhere to OpenAI’s policies relevant to you, which may include its [Usage Policy](https://openai.com/policies/usage-policies) and its [Sharing & Publication Policy](https://openai.com/policies/sharing-publication-policy). Braze makes no warranty of any kind with respect to any AI-generated content.

[1]: {% image_buster /assets/img/content_qa_ai.png %}

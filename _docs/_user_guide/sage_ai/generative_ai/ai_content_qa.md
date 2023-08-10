---
nav_title: Content QA with AI
article_title: Content QA with AI
page_order: 10
description: "This reference article covers how to QA your message content with AI directly from the message composer."
---

# Content QA with AI

> Learn how to QA your message content with AI directly from the message composer.

Content QA with AI uses the capabilities of ChatGPT and OpenAI to perform checks on the content of your message, ensuring it adheres to quality standards by identifying ineffective elements such as spelling errors, grammar issues, inappropriate tone, and offensive language. You can access this feature from the **Test** tab when composing a message in a campaign or Canvas.

## Key features

Content QA with AI offers the following key features to enhance the quality of your message content:

- **Spelling and grammar check:** Automatically checks for spelling and grammar mistakes in your message. It suggests corrections and provides recommendations to improve the overall accuracy of the content.
- **Tone analysis:** Evaluates the tone of the message to identify any potential issues. It helps ensure that the intended tone aligns with the desired communication style and helps avoid misunderstandings or unintended offenses.
- **Offensive language detection:** Scans your message for any potentially offensive or inappropriate language, allowing you to revise your content and maintain respectful communication.
- **Accidental content check:** Detects any inclusion of code, markup language, or test messages that might have been added unintentionally.

## Accessing Content QA with AI

To access the content checker, follow these steps:

1. After composing a message, navigate to the **Test** tab.
2. Locate the **Content QA with AI** section.
3. Click **Test Content**.

![Content QA with AI section of the Test tab.][1]{: style="max-width:60%"}

## Tips for effective use

Consider the following tips to make the most of the Content QA with AI feature:

- **Proofread your message:** Although the content checker can help identify errors, it is still essential to proofread your content manually. Rely on the AI-generated suggestions as a helpful guide, but use your judgment to ensure accuracy.
- **Understand the tone analysis:** The tone analysis results are subjective and based on the AI model's understanding. While they can provide useful insights, consider your intended tone and the conversation context to make appropriate adjustments.
- **Double-check flagged offensive language:** Offensive language detection is designed to be robust, but it may occasionally flag false positives. Review flagged sections carefully and make appropriate changes as necessary.

## How is my data used and sent to OpenAI?

In order to check your message content, Braze will send it to OpenAI. All queries sent to OpenAI from Braze are anonymized, meaning that OpenAI will not be able to identify from whom the query was sent unless you include uniquely identifiable information in the message content you provide. Per [OpenAI’s policy](https://openai.com/policies/api-data-usage-policies), data sent to OpenAI’s API via Braze is not used to train or improve their models and will be deleted after 30 days.

[1]: {% image_buster /assets/img/content_qa_ai.png %}

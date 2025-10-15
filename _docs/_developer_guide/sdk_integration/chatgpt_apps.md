---
page_order: 2.1
nav_title: ChatGPT Apps
article_title: Integrating Braze with ChatGPT Apps
description: "Learn how to integrate Braze with ChatGPT Apps to enable analytics and event logging within AI-powered applications."
platform:
  - ChatGPT Apps
---

# Integrating Braze with ChatGPT Apps

> This guide covers how to integrate Braze with ChatGPT Apps to enable analytics and event logging within AI-powered applications.

## Overview

ChatGPT Apps provide a powerful platform for building AI-powered applications. By integrating Braze with your ChatGPT App, you can:

- Track user engagement and behavior within your ChatGPT App
- Implement user segmentation based on AI interaction patterns  
- Retarget users across your owned channels based on their AI conversations
- Maintain first-party data control in the age of AI

While we work to create a complete feature-set for this new platform, please keep in mind that session and messaging support is not yet available. This guide will show you how to:

- log custom events
- log purchase events


### Key Benefits for Marketing Teams

**Own Your Customer Journey**: While users interact with your brand through ChatGPT, you maintain visibility into their behavior, preferences, and engagement patterns. This data flows directly into your Braze dashboard, not just the AI platform's analytics.

**Cross-Platform Retargeting**: Track user interactions in your ChatGPT App and retarget them across your owned channels (email, SMS, push notifications) with personalized campaigns based on their AI usage patterns.

**AI Conversation Intelligence**: Understand what users are asking about, what problems they're trying to solve, and how your ChatGPT App is helping them. Use this insight to improve your product, content, and messaging strategies.

**Revenue Attribution**: Track purchases and conversions that originate from ChatGPT App interactions.

### How It Works
high-level flow diagram for non-technical stakeholders

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Prerequisites

Before integrating Braze with your ChatGPT App, ensure you have:

- A Braze account and an SDK API key
- A [ChatGPT App](https://openai.com/index/introducing-apps-in-chatgpt/) created in the OpenAI platform (here is their [sample app](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

{% alert note %}
This integration requires careful consideration of data privacy and user consent. Ensure you comply with all applicable regulations and have proper user consent mechanisms in place.
{% endalert %}

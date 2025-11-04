---
page_order: 2.1
nav_title: ChatGPT apps
article_title: Integrating Braze with ChatGPT Apps
description: "Learn how to integrate Braze with ChatGPT Apps to enable analytics and event logging within AI-powered applications."
platform:
  - ChatGPT Apps
---

# Integrating Braze with ChatGPT apps

> This guide covers how to integrate Braze with ChatGPT apps to enable analytics and event logging within AI-powered applications.

![A Content Card integrated into ChatGPT app.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Overview

ChatGPT apps provide a powerful platform for building AI conversational applications. By integrating Braze with your ChatGPT app, you can continue to maintain first-party data control in the age of AI, including how to:

- Track user engagement and behavior within your ChatGPT app (such as identifying which questions or chat features your customers use)
- Segment and retarget Braze campaigns based on AI interaction patterns (such as emailing users who have used the chat more than three times per week)

### Key benefits

- **Own your customer journey:** While users interact with your brand through ChatGPT, you maintain visibility into their behavior, preferences, and engagement patterns. This data flows directly onto Braze user profiles, not just the AI platform's analytics.
- **Cross-platform retargeting:** Track user interactions in your ChatGPT app and retarget them across your owned channels (email, SMS, push notifications, in-app messaging) with personalized campaigns based on their AI usage patterns.
- **Return 1:1 promotional content to ChatGPT conversations:** Deliver Braze [in-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), and more directly within your ChatGPT experience using the custom conversational UI components your team has built for your app.
- **Revenue attribution:** Track purchases and conversions that originate from ChatGPT app interactions.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Prerequisites

Before integrating Braze with your ChatGPT app, you must have the following:

- A new web app and API key in your Braze workspace
- A [ChatGPT app](https://openai.com/index/introducing-apps-in-chatgpt/) created in the OpenAI platform ([OpenAI sample app](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}


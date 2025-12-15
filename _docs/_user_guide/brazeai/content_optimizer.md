---
nav_title: Content Optimizer
article_title: Content Optimizer
page_order: 6
description: "Content Optimizer enables marketers to test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically."
---

# Content Optimizer

> Content Optimizer enables marketers to test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

{% alert important %}
Content Optimizer is currently in beta and only available for email messages. For help getting started, contact your customer success manager.
{% endalert %}

## About Content Optimizer

Content Optimizer is a Canvas step that lets you define message components to test, generate variants using Generative AI or manual input, and automatically optimize which content combinations are sent to users. 

- Optimize subject lines, body header, body content, or primary CTA for emails.
- Continuously improve message performance without manual A/B test setup.
- Test high volumes of content variants quickly, leveraging AI for ideation.
- Automatically phase out underperforming content and scale up winners.

## How it works

Content Optimizer uses a non-contextual [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) algorithm to allocate more sends to high-performing variants and reduce allocation to underperforming ones. Over time, this results in continuous improvement of your message content, with minimal manual intervention.

Content Optimizer is similar to the Message step in Canvas, with features like quiet hours, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing), and event logging. You can configure a Content Optimizer step by creating a base message and defining which content components (such as subject line, body text, or call-to-action) to optimize. Variants for each component can be generated with AI or entered manually, and Liquid tags must be added to the base message to map components into the message content.

Each user receives one message per entry into the Content Optimizer step. Re-entries are treated as new, with no memory of previous variants.

### Key concepts

| Term                    | Description |
|-------------------------|-------------|
| **Base message**    | The main message template that variants are built from, including all send settings. |
| **Content components**  | Elements within a message (for example, subject line or primary CTA) that can be tested and optimized. Marketers must insert the relevant Liquid tag into the message where the component should appear. |
| **Content variants**    | The different values a content component can take. |
| **Content combinations**| Unique messages created by mixing and matching content variants. |
| **Send settings**       | All standard message configuration options for the selected channel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

- Content Optimizer is currently in beta and only available for email messages.
- Only one message is sent per user per entry. There is no memory of previous sends for re-entries.
- Marketers must manually insert Liquid tags for each component in the message composer where the defined content component variants should render.

## Next steps

- Contact your customer success manager to join the beta or for onboarding support.
- Learn how to create a [Content Optimizer step](placeholder)
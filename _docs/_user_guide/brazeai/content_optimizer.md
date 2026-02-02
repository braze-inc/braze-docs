---
nav_title: Content Optimizer
article_title: Content Optimizer
alias: "/content_optimizer/"
description: "Content Optimizer is an agent that helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically."
page_type: reference
page_order: 4
---

# Content Optimizer

> Content Optimizer is an agent that helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

{% alert important %}
Content Optimizer is currently in beta and only available for email messages. For help getting started, contact your customer success manager.
{% endalert %}

## About Content Optimizer

Content Optimizer is an agent that runs in a Canvas step. It helps you define message components to test, generate variants using Generative AI or manual input, and automatically optimize which content combinations are sent to users. This feature helps you to:

- Optimize subject lines, body header, body content, or primary CTA for emails.
- Continuously improve message performance without manual A/B test setup.
- Test high volumes of content variants quickly, leveraging AI for ideation.
- Automatically phase out underperforming content and scale up winners.

Learn how to create a [Content Optimizer step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Use cases

### Email

| Optimization use case | Goal | Description |
| --- | --- | --- |
| Subject line variations | Increase open rate | Test tone, urgency, personalization, and use of emojis. |
| Header messaging styles | Boost engagement | Compare emotional, value-driven, and clear messaging in the body header. | 
| Body content format | Improve readability and engagement | Test storytelling versus feature lists, bullets versus paragraphs, and content length. |
| CTA copy & tone | Increase click-throughs | Compare action-led, benefit-focused, and first-person CTA phrasing. |
| Themed content combinations | Discover high-performing combinations | Mix and match themed subject, body, and CTA components to find the best overall combination. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## How it works

Content Optimizer uses a non-contextual [multi-armed bandit](https://en.wikipedia.org/wiki/Multi-armed_bandit) algorithm to allocate more sends to high-performing variants and reduce allocation to underperforming ones. Over time, this results in continuous improvement of your message content, with minimal manual intervention.

Content Optimizer is similar to the Message step in Canvas, with features like quiet hours, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing), and event logging. You can configure a Content Optimizer step by creating a base message and defining which content components (such as subject line, body text, or call-to-action) to optimize. Variants for each component can be generated with AI or entered manually, and Liquid tags must be added to the base message to map components into the message content.

Each user receives one message per entry into the Content Optimizer step. Re-entries are treated as new, with no memory of previous variants.

For best results, use Content Optimizer in Canvases where users enter the step gradually over time, such as in recurring or always-on Canvases with consistent daily volume. If all users enter the step at once, the agent won’t have time to learn from early results. The step will behave more like a static A/B test than a live optimization engine.

This means you can still use Content Optimizer in single-send or short-term Canvases, but only if users are entering the step over a prolonged period (for example, through a delay step, scheduled entry, or API-triggered flow). Make sure the step has enough traffic and time to observe performance differences before reaching most users.


### Key concepts

| Term                    | Description |
|-------------------------|-------------|
| Base message   | The main message template that variants are built from, including all send settings. |
| Content components  | Elements within a message (for example, subject line or primary CTA) that can be tested and optimized. Marketers must insert the relevant Liquid tag into the message where the component should appear. |
| Content variants    | The different values a content component can take. |
| Content combinations| Unique messages created by mixing and matching content variants. |
| Optimization event       | Determines how Content Optimizer evaluates performance and allocates traffic to content combinations over time, such as clicks or opens for email. Applies to all content components in a step. Content Optimizer continuously learns from this event and automatically shifts delivery toward higher-performing content combinations. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitations

- Content Optimizer is currently in beta and only available for email messages.
- The agent can generate up to 125 combinations per step:
   - Up to 3 components per step
   - Up to 5 variants for each component
- Only one message is sent per user per entry. There is no memory of previous sends for re-entries.
- Marketers must manually insert Liquid tags for each component in the message composer where the defined content component variants should render.

## How is my data used and sent to OpenAI? {#ai-policy} 

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Next steps

- Contact your customer success manager to join the beta or for onboarding support.
- Learn how to create a [Content Optimizer step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).
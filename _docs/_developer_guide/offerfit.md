---
page_order: 2.5
nav_title: OfferFit by Braze
article_title: OfferFit by Braze
description: "Learn how you can leverage OfferFit with Braze..."
---

# Getting Started with OfferFit by Braze

> Get started with OfferFit by Braze to make 1:1 AI decisions that maximize any business metric!

## What's OfferFit by Braze?

[OfferFit](https://www.offerfit.ai/) replaces A/B testing with AI decisioning that personalizes everything, and maximizes any metric: drive dollars, not clicks&#8212;with OfferFit, you can optimize any business KPI.

OfferFit's AI decisioning agents automatically discover the optimal action for every customer. Using your first-party data, OfferFit can maximize any business KPI for a wide range of use cases, including cross-sell, upsell, repurchase, retention, renewal, referral, winback, and more.

After OfferFit is configured, the automated experimentation platform will automatically send 1:1 personalized activation events to Braze for each user in your target audience. These activation events will be triggered through the Braze campaigns or Canvases you configured.

## Key features

- Orchestrate activation events in Braze.
- Data integration capabilities that allow you to retrieve customer profile (non-PII) and engagement data from Braze through the available API endpoints.
- Analytics data available in Braze.
- In OfferFit: comprehensive reporting layer that allows marketers to explore the customer insights discovered by OfferFit through its self-learning AI capabilities.

## About use cases

A use case is a custom configuration for OfferFit’s AI decisioning engine that's tailor-made to meet a specific business goal.

For example, you could build a repeat purchase use case to increase follow-up conversions after an initial sale. You define the audience and message in Braze, while OfferFit runs daily experiments, automatically testing different combinations of product offers, message timing, and frequency for each customer. Over time, OfferFit learns what works best and orchestrates personalized sends through Braze to maximize repurchase rates.

Building a good use case is consists of:

- Choosing a success metric for OfferFit to optimize for, such as revenue, conversions, or ARPU.
- Defining which dimensions to test, such as offer, subject line, creative, channel, or send time.
- Selecting the options for each dimension, such as email vs. SMS or daily vs. weekly frequency.

## About API key permissions

During your OfferFit integration, you'll create a Braze API key with specific permissions that will define your integration's capabilities. Refer to the following table to learn more about each permission.

{% alert tip %}
This information can also be found on the [OfferFit integration]({{site.baseurl}}/developer_guide/offerfit/integration) page.
{% endalert %}

{% multi_lang_include offerfit/api-key-permissions.md %}

## Next steps

Now that you know more about OfferFit by Braze, you're ready for next steps:

1. [Integrating OfferFit]({{site.baseurl}}/developer_guide/offerfit/integration)
2. [Building a use case]({{site.baseurl}}/developer_guide/offerfit/building_use_cases)

---
nav_title: Building Use Cases
article_title: Building Use Cases for OfferFit by Braze
page_order: 2
description: "Learn how to..."
---

# Building use cases

> Learn how to build an OfferFit use case, so you can automate personalized experimentation and optimize outcomes like conversions, retention, or revenue&#8212;without manual A/B testing.

## About use cases

A use case is a custom configuration for OfferFit’s AI decisioning engine that's tailor-made to meet a specific business goal.

For example, you could build a repeat purchase use case to increase follow-up conversions after an initial sale. You define the audience and message in Braze, while OfferFit runs daily experiments and automatically tests different combinations of product offers, message timing, and frequency for each customer. Over time, OfferFit learns what works best and orchestrates personalized sends through Braze to maximize repurchase rates.

To build a good use case, you'll:

- Choose a success metric for OfferFit to optimize for, such as revenue, conversions, or ARPU.
- Define which dimensions to test, such as offer, subject line, creative, channel, or send time.
- Select the options for each dimension, such as email vs. SMS or daily vs. weekly frequency.

![of_use_case_example]({% image_buster /assets/img/offerfit/of_use_case_example.png %})

## Sample use cases

The OfferFit AI will learn from every customer interaction and apply those insights to the next day's recommendations.


| Use Case                        | Buisness Goal                                                                                         | Using Typical Methods                                                                                                                                           | Using OfferFit by Braze                                                                                                                                                                                                                     |
|---------------------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cross-Sell or Upsell**        | Maximize average revenue per user (ARPU) from internet subscriptions.                        | Run annual campaigns offering every customer the next-highest tier plan.                                                                                  | Empirically discover the best message, sending time, discount, and plan to offer for each customer, learning which customers are susceptible to leapfrog offers and which customers require discounts or other incentives to upgrade. |
| **Renewal & Retention**         | Secure contract renewals, maximizing both contract length and net present value (NPV).       | A/B test manually, and offer significant discounts to secure renewals.                                                                                    | Use automated experimentation to find the best renewal offer for each customer, and identify customers who are less price sensitive and need less significant discounts to renew.                                                     |
| **Repeat Purchase**             | Maximize purchase and repurchase rates.                                                      | All customers receive the same journey after making a website account (such as the same email sequence with the same cadence).                            | Automate experimentation to find the best menu item to offer each customer, as well as the most effective subject line, sending time, and frequency of communication.                                                                 |
| **Winback**                     | Increase reactivation by encouraging past subscribers to resubscribe.                        | Sophisticated A/B testing and segmentation.                                                                                                               | Leverage automated experimentation to test thousands of variables at once, discovering the best creative, message, channel and cadence for each individual.                                                                           |
| **Referral**                    | Maximize new accounts opened through business credit card referrals from existing customers. | Fixed email sequence for all customers, with extensive A/B testing to determine the best sending times, cadence, etc. for the customer population.        | Automate experimentation to determine ideal email, creative, sending time, and credit card to offer specific customers.                                                                                                               |
| **Lead Nurturing & Conversion** | Drive incremental revenue and pay the right amount for each customer.                        | As privacy policies change at Facebook and other platforms, prior approaches to personalized paid ads become last effective.                              | Leverage robust first-party data to automatically experiment on customer segments, biding methodology, bid levels, and creative.                                                                                                      |
| **Loyalty & Engagement**        | Maximize purchases by new enrollees in customer loyalty program.                             | Customers received fixed sequence of emails in response to their actions. For example, all new enrollees in the loyalty program receive the same journey. | Experiment automatically with different email offers, creative, sending time, and frequency to maximize purchase and repurchase for each customer.                                                                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Building a use case

### Prerequisites

Before you can build a use case, you'll need to [integrate OfferFit by Braze]({{site.baseurl}}/developer_guide/offerfit/integration).

### Step 1: Contact OfferFit

You'll work with the OfferFit team to build your use case. If you haven't already, reach out to your customer success manager to get started. They'll walk you through the following steps to help build a custom use case that's right for you.

### Step 2: Define a target audience

<!-- Content in this step largely unedited. Will be tackled monday. -->

Define your target audience by creating at least one segment in Braze. This segment will be used to send your campaign or Canvas to the right users.

### Step 3: Set up API-triggered delivery

<!-- Content in this step largely unedited. Will be tackled monday. -->

Next, you'll create an API-triggered Braze campaign or Canvas and create campaign assets (for example, HTML templates, images).

1. Create a [campaign]({{site.baseurl}}//user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) or [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule) in Braze. OfferFit will use this campaign or Canvas to send 1:1 personalized activation events to the right users from your defined audience. 
2. Do not include a Braze [control group]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) in your campaign or Canvas. This allows the OfferFit control group to be the only active one.
3. Depending on your dimensions, you can configure Liquid tags in your creative content to dynamically populate your campaign or Canvas with OfferFit recommendations. OfferFit will pass customer-specific content to the Liquid tags in your templates via the Braze API.

### Step 4: Orchestrate activation events

You can leverage the OfferFit native activation integration with Braze to orchestrate and schedule 1:1 personalized recommendations for your target audience.

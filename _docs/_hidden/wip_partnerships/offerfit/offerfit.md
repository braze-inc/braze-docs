---
nav_title: OfferFit
article_title: OfferFit
page_order: 1

description: "OfferFit’s Automated Experimentation Platform is the fastest, most scalable way to accelerate testing and learning. Automatically discover the right message, creative, incentive, channel, and timing for every customer to unlock the full value of your customer data."
alias: /partners/offerfit/

page_type: partner
search_tag: OfferFit
hidden: true
layout: dev_guide
---

# [OfferFit]

> Welcome to the Braze partner template! Here, you'll find everything you need to create your partner page. In this first section, include a brief description of your company. Also, include a link to your main site. 
In this second paragraph, explore the relationship between your company and Braze. This paragraph should explain how Braze and your company partner together to tighten the bond between the Braze user and their customer. Explain the "elevation" that occurs when a Braze user integrates with or leverages your partnership and the services you offer.

## Prerequisites


| Requirement         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OfferFit License    | An active OfferFit license is required to take advantage of this partnership.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Braze REST API key  | A Braze REST API key with the following permissions: <li>`users.export.ids`</li> <li>`users.export.segment`</li> <li>`messages.send`</li> <li>`users.export.segment`</li> <li>`campaigns.trigger.send`</li> <li>`campaigns.list`</li> <li>`campaigns.data_series`</li> <li>`campaigns.details`</li> <li>`canvas.trigger.send`</li> <li>`canvas.list`</li> <li>`canvas.data_series`</li> <li>`canvas.details`</li> <li>`segments.list`</li> <li>`segments.data_series`</li> <li>`segments.details`</li> <li>`templates.create`</li> <li>`templates.update`</li> <li>`templates.info`</li> <li>`templates.list`</li> <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}

## Use cases

Lifecycle marketers know that when it comes to engaging their customers, practice beats theory. No matter
how brilliant a campaign, email subject, ad, or creative seems on paper, the only way to know if an idea
works is to try it out with customers. Traditionally, marketers have tried out their ideas through A/B testing,
but A/B testing is slow and doesn’t scale with the number of variables marketers need to test. OfferFit’s
**self learning** platform allows marketers to automate the process of experimentation.
Marketers use OfferFit to optimize campaigns to existing identified customers, with business goals such as
cross-sell, upsell, repurchase, retention, renewal, referral, and winback. To implement OfferFit, marketers:
1. Choose a **success metric** they want to maximize, such as revenue, conversions, ARPU, or any other
KPI they can measure from their data. This is the metric OfferFit’s AI will try to maximize.
2. Choose **dimensions** along which to test (e.g., offer, subject line, creative, channel, time, day,
frequency, etc.)
3. Finally, choose the **options** available for each dimension. For example the options for the “channel”
dimension might be email, SMS and push; while the options for the “frequency” dimension might be
daily, twice a week, and weekly.

![of_use_case_example][2]

OfferFit’s AI then **automates the process of experimentation**. OfferFit makes daily recommendations
for each customer, seeking to maximize the chosen success metric. The AI learns from every customer
interaction, and applies these insights to the next day‘s recommendations.


| Use Case                    | Goal                                                                                         | Prior Approach                                                                                                                                                | OfferFit Approach                                                                                                                                                                                                                     |
|-----------------------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Cross-Sell / Upsell**         | Maximize average revenue per user (ARPU) from internet subscriptions.                        | Run annual campaigns offering every customer the next-highest tier plan.                                                                                      | Empirically discover the best message, sending time, discount, and plan to offer for each customer, learning which customers are susceptible to leapfrog offers and which customers require discounts or other incentives to upgrade. |
| **Renewal & Retention**         | Secure contract renewals, maximizing both contract length and NPV (net present value).       | A/B test manually, and offer significant discounts to secure renewals.                                                                                        | Use automated experimentation to find the best renewal offer for each customer, and identify customers who are less price sensitive and need less significant discounts to renew.                                                     |
| **Repeat Purchase**             | Maximize purchase and repurchase rates.                                                      | All customers receive the same "journey" after making a website account -- the same email sequence with the same cadence.                                     | Automate experimentation to find the best menu item to offer each individual customer, as well as the most effective subject line, sending time, and frequency of communication.                                                      |
| **Winback**                     | Increase reactivation by encouraging past subscribers to resubscribe.                        | Sophisticated A/B testing and segmentation.                                                                                                                   | Leverage automated experimentation to test thousands of variables at once, discovering the best creative, message, channel and cadence for each individual.                                                                           |
| **Referral**                    | Maximize new accounts opened through business credit card referrals from existing customers. | Fixed email sequence for all customers, with extensive A/B testing to determine the best sending times, cadence, etc. for the customer population as a whole. | Automate experimentation to determine ideal email email creative, sending time, and credit card to offer for each specific customer.                                                                                                  |
| **Lead Nurturing & Conversion** | Drive incremental revenue and pay the right amount for each customer.                        | As privacy policies change at Facebook and other platforms, prior approaches to personalized paid ads become last effective.                                  | Leverage robust first-party data to automatically experiment on customer segments, biding methodology, bid levels, and creative.                                                                                                      |
| **Loyalty & Engagement**        | Maximize purchases by new enrollees in customer loyalty program.                                                                                             | Customers received fixed sequence of emails in response to their actions. For example all new enrollees in the loyalty program receive the same "journey."                                                                                                                                                              | Experiment automatically with different email offers (points, coupons, etc), creative, sending time, and frequency to maximize purchase and repurchase for each individual customer.                                                                                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Define Braze target audience

To define your target audience, you will need to create one or multiple segments in Braze. This audience will be used to send your campaign or canvas to the right users.

### Step 2: Configure API-triggered Braze Campaign or Canvas and create campaign assets (e.g. HTML templates, images)

You will need to create a Campaign or Canvas in Braze. This campaign or canvas will be used by OfferFit to send 1:1 personalized activation events to the right users from your defined audience. Because OfferFit will use its own Control Group, you should disable the Braze Control Group to ensure that you do not have 2 control groups active at the same time.

### Step 3: Update your OfferFit use case configuration to orchestrate Braze activation events 

You can leverage the OfferFit native activation integration with Braze to orchestrate and schedule 1:1 personalized recommendations for your target audience.


## Customization

In addition to orchestrating activation events in Braze, OfferFit also provides data integration capabilities that allow marketers to retrieve customer profile (non-PII) and engagement data from Braze through the available API endpoints.

## Using this integration

Once configured, the OfferFit automated experimentation platform will automatically send 1:1 personalized activation events to Braze for each user in your target audience. These activation events will trigger the Braze campaign or canvas you have configured in step 2.

In addition to the analytics data available in Braze, OfferFit also provides a comprehensive reporting layer that allows marketers to explore the customer insights discovered by OfferFit through its self-learning AI capabilities.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}
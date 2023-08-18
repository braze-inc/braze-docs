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

## Prerequisites


| Requirement         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OfferFit License    | An active OfferFit license is required to take advantage of this partnership.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Braze REST API key  | A Braze REST API key with the following permissions: <li>`users.export.ids`</li> <li>`users.export.segment`</li> <li>`messages.send`</li> <li>`campaigns.trigger.send`</li> <li>`campaigns.list`</li> <li>`campaigns.data_series`</li> <li>`campaigns.details`</li> <li>`canvas.trigger.send`</li> <li>`canvas.list`</li> <li>`canvas.data_series`</li> <li>`canvas.details`</li> <li>`segments.list`</li> <li>`segments.data_series`</li> <li>`segments.details`</li> <li>`templates.create`</li> <li>`templates.update`</li> <li>`templates.info`</li> <li>`templates.list`</li> <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}

Please find below a detailed overview of how the various Braze API endpoints can be used by OfferFit. Depending on the OfferFit license and use case specifics, there might be different workflows and API endpoints used.

| API Endpoint                                                                                                                    | OfferFit Usage                                                                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [POST /users/export/ids](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/)                      | OfferFit can use this endpoint to retrieve the list of customers to be targeted by a campaign or canvas. As OfferFit does not accept any PII data, we are leveraging the `fields_to_export` attribute to only retrieve the data attributes agreed together with the platform user.    |
| [POST /users/export/segment](https://www.braze.com/docs/api/endpoints/export/user_data/post_users_segment/)                     | OfferFit can use this endpoint to retrieve all the users that are part of a specific Segment. As previously mentioned, OfferFit does not accept any PII data, so the `fields_to_export` attribute is used to only retrieve non-PII fields, as agreed together with the platform user. |
| [POST /messages/send](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_messages/)                     | OfferFit can use this endpoint to trigger an API Campaign in Braze.                                                                                                                                                                                                                   |
| [POST /campaigns/trigger/send](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | OfferFit can use this endpoint to trigger a send for a Campaign that is configured for API-triggered delivery.                                                                                                                                                                        |
| [GET /campaigns/list](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns/)                                 | OfferFit can use this endpoint to retrieve the list of all the campaigns configured in Braze and their associated metadata.                                                                                                                                                           |
| [GET /campaigns/data_series](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_analytics/)                 | OfferFit can use this endpoint to retrieve the analytics data of a specific Braze campaign.                                                                                                                                                                                           |
| [GET /campaigns/details](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details/)                       | OfferFit can use this endpoint to retrieve the details of a specific Braze campaign.                                                                                                                                                                                                  |
| [POST /canvas/trigger/sed](https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)      | OfferFit can use this endpoint to trigger a send for a Canvas that is configured for API-triggered delivery.                                                                                                                                                                          |
| [GET /canvas/list](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvases/)                                        | OfferFit can use this endpoint to retrieve the list of all the canvases configured in Braze and their associated metadata.                                                                                                                                                            |
| [GET /canvas/data_series](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_analytics/)                         | OfferFit can use this endpoint to retrieve the analytics data of a specific Braze canvas.                                                                                                                                                                                             |
| [GET /canvas/details](https://www.braze.com/docs/api/endpoints/export/canvas/get_canvas_details/)                               | OfferFit can use this endpoint to retrieve the details of a specific Braze canvas.                                                                                                                                                                                                    |
| [GET /segments/list](https://www.braze.com/docs/api/endpoints/export/segments/get_segments/)                                    | OfferFit can use this endpoint to retrieve the list of all the segments configured in Braze and their associated metadata.                                                                                                                                                            |
| [GET /segments/data_series](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_analytics/)                    | OfferFit can use this endpoint to retrieve the size of the Braze segment.                                                                                                                                                                                                             |
| [GET /segments/details](https://www.braze.com/docs/api/endpoints/export/segments/get_segment_details/)                          | OfferFit can use this endpoint to retrieve the details of a specific Braze segment.                                                                                                                                                                                                   |
| [POST /templates/email/create](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_create_email_template/)  | OfferFit can use this endpoint to create a new Braze HTML email template.                                                                                                                                                                                                             |
| [POST /templates/email/update](https://www.braze.com/docs/api/endpoints/templates/email_templates/post_update_email_template/)  | OfferFit can use this endpoint to update an existing Braze HTML email template.                                                                                                                                                                                                       |
| [GET /templates/email/info](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_see_email_template_information/)        | OfferFit can use this endpoint to retrieve the details of a specific Braze HTML email template.                                                                                                                                                                                       |
| [GET /templates/email/list](https://www.braze.com/docs/api/endpoints/templates/email_templates/get_list_email_templates/)      | OfferFit can use this endpoint to retrieve the list of all the Braze HTML email templates configured in Braze and their `subject line` and `HTML content`.                                                                                                                             |
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

### Step 1: Define target audience in Braze

To define your target audience, you will need to create one or multiple segments in Braze. This audience will be used to send your campaign or canvas to the right users.

### Step 2: Configure API-triggered Braze Campaign or Canvas and create campaign assets (e.g. HTML templates, images)

You will need to create at least a Campaign or Canvas in Braze. This campaign or canvas will be used by OfferFit to send 1:1 personalized activation events to the right users from your defined audience. Because OfferFit will use its own Control Group, you should disable the Braze Control Group to ensure that you do not have 2 control groups active at the same time. Depending on the dimensions that you want to experiment on, you have the ability to configure liquid tags in your creative content (e.g. subject line, call to action, offer type, etc.) to dynamically populate the content of your campaign or canvas using OfferFit recommendations. The OfferFit platform can pass the customer-specific personalized content via the Braze API to automatically populate the liquid tags in your templates.

### Step 3: Update your OfferFit use case configuration to orchestrate Braze activation events 

You can leverage the OfferFit native activation integration with Braze to orchestrate and schedule 1:1 personalized recommendations for your target audience.


## Customization

In addition to orchestrating activation events in Braze, OfferFit also provides data integration capabilities that allow marketers to retrieve customer profile (non-PII) and engagement data from Braze through the available API endpoints.

## Using this integration

Once configured, the OfferFit automated experimentation platform will automatically send 1:1 personalized activation events to Braze for each user in your target audience. These activation events will be triggered through the Braze campaigns or canvases you have configured in step 2 for the OfferFit experiment.

In addition to the analytics data available in Braze, OfferFit also provides a comprehensive reporting layer that allows marketers to explore the customer insights discovered by OfferFit through its self-learning AI capabilities.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}
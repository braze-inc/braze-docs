---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "OfferFit replaces manual A/B testing with AI testing. Lifecycle marketers use OfferFit’s AI testing to make the best 1:1 decision for each customer, test all variables simultaneously, and detect and adapt to market changes."
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [OfferFit](https://www.offerfit.ai/) replaces manual A/B testing with AI testing. Lifecycle marketers use OfferFit’s AI testing to make the best 1:1 decision for each customer, test all variables simultaneously, and detect and adapt to market changes.

_This integration is maintained by OfferFit._

## About the integration

The OfferFit and Braze integration allows you to automatically discover the right message, channel, and timing for every customer based on your customer data. You can optimize your campaigns to existing identified customers, with business goals such as cross-sell, upsell, repurchase, retention, renewal, referral, and winback.

## Prerequisites

| Requirement | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OfferFit License | An active OfferFit license is required to take advantage of this partnership.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Braze REST API key | A Braze REST API key with the following permissions: {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>users.track</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.email.create</code></li><li><code>templates.email.update</code></li><li><code>templates.email.info</code></li><li><code>templates.email.list</code></li></ul>{:/} This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST API endpoint | [Your REST API endpoint URL][1]. Your endpoint depends on the Braze URL for your instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Braze REST API endpoints

Your OfferFit license and use case will determine the Braze REST API endpoints you use. Below are various API endpoints you might use.

| Braze REST API endpoint | OfferFit usage |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | Retrieve the list of customers to be targeted by a campaign or Canvas. As OfferFit doesn't accept any PII data, the `fields_to_export` attribute is used to only retrieve the data attributes agreed together with the platform user. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | Retrieve all the users that are part of a specific segment. As OfferFit doesn't accept any PII data, the `fields_to_export` attribute is used to only retrieve the non-PII fields agreed together with the platform user. |
| [POST /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFit can use this endpoint to update user profiles with custom data attributes that can be used to personalize messaging.                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Trigger an API Campaign in Braze. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | Trigger a send for a campaign that is configured for API-triggered delivery. |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Retrieve the list of all the campaigns configured in Braze and their associated metadata. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | Retrieve the analytics data of a specific Braze campaign. |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Retrieve the details of a specific Braze campaign. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | Trigger a send for a Canvas that is configured for API-triggered delivery. |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Retrieve the list of all the Canvases configured in Braze and their associated metadata. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | Retrieve the analytics data of a specific Canvas. |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | Retrieve the details of a specific Canvas. |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Retrieve the list of all the segments configured in Braze and their associated metadata. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Retrieve the size of the Braze segment. |
| [GET /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Retrieve the details of a specific Braze segment. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | Create a new Braze HTML email template. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Update an existing Braze HTML email template. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Retrieve the details of a specific Braze HTML email template. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Retrieve the list of all the Braze HTML email templates configured in Braze and their `subject line` and `HTML content`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

After you [integrate OfferFit](#integration), you can automate the experimentation process by doing the following:

1. Select a **success metric** to maximize, such as revenue, conversions, ARPU, or any other
KPI you can measure from your customer data. This is the metric OfferFit will try to maximize with its AI.
2. Select the **dimensions** to test (for example, offer, subject line, creative, channel, time, day, frequency, etc.).
3. Select the **options** available for each dimension. For example, you could select email, SMS, and push for the channel dimension, and then select daily, twice a week, and weekly for the frequency dimension.

![of_use_case_example][2]


After the experimentation process is automated, OfferFit will begin making daily recommendations for each customer with the goal of maximizing the chosen success metric. 

The OfferFit AI will learn from every customer interaction and apply those insights to the next day's recommendations.


| Use Case | Goal | Prior Approach | OfferFit Approach |
|----------|------|----------------|-------------------|
| **Cross-Sell or Upsell** | Maximize average revenue per user (ARPU) from internet subscriptions. | Run annual campaigns offering every customer the next-highest tier plan. | Empirically discover the best message, sending time, discount, and plan to offer for each customer, learning which customers are susceptible to leapfrog offers and which customers require discounts or other incentives to upgrade. |
| **Renewal & Retention** | Secure contract renewals, maximizing both contract length and net present value (NPV). | A/B test manually, and offer significant discounts to secure renewals. | Use automated experimentation to find the best renewal offer for each customer, and identify customers who are less price sensitive and need less significant discounts to renew. |
| **Repeat Purchase** | Maximize purchase and repurchase rates. | All customers receive the same journey after making a website account (such as the same email sequence with the same cadence). | Automate experimentation to find the best menu item to offer each customer, as well as the most effective subject line, sending time, and frequency of communication. |
| **Winback** | Increase reactivation by encouraging past subscribers to resubscribe. | Sophisticated A/B testing and segmentation. | Leverage automated experimentation to test thousands of variables at once, discovering the best creative, message, channel and cadence for each individual. |
| **Referral** | Maximize new accounts opened through business credit card referrals from existing customers. | Fixed email sequence for all customers, with extensive A/B testing to determine the best sending times, cadence, etc. for the customer population. | Automate experimentation to determine ideal email, creative, sending time, and credit card to offer specific customers. |
| **Lead Nurturing & Conversion** | Drive incremental revenue and pay the right amount for each customer. | As privacy policies change at Facebook and other platforms, prior approaches to personalized paid ads become last effective. | Leverage robust first-party data to automatically experiment on customer segments, biding methodology, bid levels, and creative. |
| **Loyalty & Engagement** | Maximize purchases by new enrollees in customer loyalty program. | Customers received fixed sequence of emails in response to their actions. For example, all new enrollees in the loyalty program receive the same journey. | Experiment automatically with different email offers, creative, sending time, and frequency to maximize purchase and repurchase for each customer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Integration

### Step 1: Define target audience in Braze

Define your target audience by creating at least one segment in Braze. This segment will be used to send your campaign or Canvas to the right users.

### Step 2: Configure an API-triggered Braze campaign or Canvas and create campaign assets (for example, HTML templates, images) {#step-2}

1. Create a campaign or Canvas in Braze. OfferFit will use this campaign or Canvas to send 1:1 personalized activation events to the right users from your defined audience. 
2. Do not include a Braze [control group]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) in your campaign or Canvas. This allows the OfferFit control group to be the only active one.
3. Depending on your dimensions, you can configure Liquid tags in your creative content to dynamically populate your campaign or Canvas with OfferFit recommendations. OfferFit will pass customer-specific content to the Liquid tags in your templates via the Braze API.

### Step 3: Update your OfferFit use case configuration to orchestrate Braze activation events

You can leverage the OfferFit native activation integration with Braze to orchestrate and schedule 1:1 personalized recommendations for your target audience.

## Customization

In addition to orchestrating activation events in Braze, OfferFit provides data integration capabilities that allow you to retrieve customer profile (non-PII) and engagement data from Braze through the available API endpoints.

## Using this integration

After OfferFit is configured, the automated experimentation platform will automatically send 1:1 personalized activation events to Braze for each user in your target audience. These activation events will be triggered through the Braze campaigns or Canvases you configured in [step 2](#step-2).

In addition to the analytics data available in Braze, OfferFit provides a comprehensive reporting layer that allows marketers to explore the customer insights discovered by OfferFit through its self-learning AI capabilities.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}


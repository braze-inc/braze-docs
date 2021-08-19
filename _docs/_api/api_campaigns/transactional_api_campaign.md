---
nav_title: Transactional Campaigns
article_title: Transactional Campaigns
page_order: 5
description: "This reference article covers how to create and configure a new Braze transactional email campaign."
page_type: reference
alias: "/api/api_campaigns/transactional_campaigns"
tool: Campaigns

---

# Transactional Email Campaigns

Transactional emails are those that are sent to facilitate an agreed-upon transaction between a sender and the recipient. Braze's transactional email campaign type is purpose-built for sending automated, non-promotional email messages like order confirmations, password resets, billing alerts, or other business-critical notifications originating from your service for a single user where speed is of the utmost importance. Transactional email is only available as part of select Braze packages. Please reach out to your Braze Customer Success Manager for more details. 

This reference article covers how to create a transational campaign in the Braze dashboard and generate a `campaign_id` to include in your API calls for our [Transactional Email API endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).


## Create a New Campaign
Navigate to the **Campaigns** page in your company Braze account and click __Create Campaign__, then select __Transactional Email__ under the __Transactional__ section.

![Select Transactional Email Campaign][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Now, you can move on to configuring your transactional campaign.

## Configure Your Campaign

When launching a transactional campaign, Braze has simplified the campaign creation flow in order to ensure your business-critical transactional emails can reach all users. As a result, you will notice a few settings you may be familiar with from other Braze campaign types are not required when setting up this campaign type:

- Delivery page has been simplified to remove scheduling options. Transactional emails will always be triggered through Braze's REST API using the Campaign ID shown on the delivery page. Additional settings you may be used to finding on this page, like re-eligibility controls and frequency capping settings, have also been removed in order to ensure all users are reachable for these critical transactional alerts when your service triggers a send request.<br><br>
- As transactional emails enroll your entire user base as eligible, including unsubscribed users, there is no need to specify filters or segments with the target Users page. As a result, if you have any logic to apply to who should receive this message, we recommend applying that logic before determining whether to make the API request to Braze to trigger the message to a specific user.<br><br>
- Transactional emails do not support Conversion Event Tracking at this time.

![Transactional Campaign Creation Flow][2]

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Compose your email or select from a template. 
3. Take note of your `campaign_id`. After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Transactional Email Endpoint Spec]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)
4. Click __Save Campaign__ and you're set to begin your API campaign!

### Disallowed Tags in Transactional Emails 

Please note that the `Connected Content` and `Promotion Code` Liquid tags are currently not available within transactional email campaigns. 

Using the `Connected Content` tag requires Braze to make an outbound API request during our sending process, which can slow down the message sending process if the external service we request is experiencing latency.  Similarly, the `Promotion Code` tag requires Braze to perform additional processing to evaluate the availability of a promotion before sending, which can slow the sending process should one not be available.

As a result, we do not support including `Connected Content` or `Promotion Code` tags within any field of your transactional email campaign.


[1]: {% image_buster /assets/img/transactional_email_campaign.png %} 
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}

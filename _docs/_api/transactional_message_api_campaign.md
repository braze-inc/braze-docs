---
nav_title: API Campaigns
platform: REST APIs
page_order: 5

description: "This reference article covers how to create and configure a new Braze Transactional Email Campaign."
page_type: reference
hidden: false
tool:
  - Dashboard
  - Docs
platform:
  - APIs

alias: "/api/api_campaigns/transactional_campaigns"
---
# Transactional Email Campaigns

Transactional Emails are those that are sent to facilitate an agreed-upon transaction between a sender and the recipient. Braze's Transactional Email campaign type is purpose-built for sending automated, non-promotional email messages like order confirmations, password resets, billing alerts, or other business-critical notifications originating from your service for a single user where speed is of the utmost importance. Transactional Email is only available as part of select Braze packages. Please reach out to your Braze Customer Success Manager for more details. 

This reference article covers how to create a Transactional Campaign in the Braze dashboard and generate a `campaign_id` to include in your API calls for our [Transactional Email API endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).


## Create a New Campaign
Navigate to the Campaigns page in your company Braze account and click the `Create Campaign` button, then select `Transactional Email` under the Transactional section.

![Select Transactional Email Campaign][1]{: style="float:right;max-width:30%;margin-left:15px;"}

Now, you can move on to configuring your Transactional Campaign

## Configure Your Campaign

When launching a Transactional Campaign, Braze has simplified the campaign creation flow in order to ensure your business-critical transactional emails can reach all users. As a result, you will notice a few settings you may be familiar with from other Braze campaign types are not required when setting up this campaign type:

- Delivery Page has been simplified to remove scheduling options. Transactional Emails will always be triggered through Braze's REST API using the Campaign ID shown on the Delivery Page. Additional settings you may be used to finding on this page like re-eligibility controls and frequency capping settings have also been removed in order to ensure all users are reachable for these critical transactional alerts when your service triggers a send request.  
- As transactional emails enroll your entire user base as eligible, including unsubscribed users, there is no need to specify filters or segments with the Target Users page. As a result, if you have any logic to apply to who should receive this message, we recommend applying that logic before determining whether to make the API request to Braze to trigger the message to a specific user.. 
- Transactional Emails do not support Conversion Event Tracking at this time.

![Transactional Campaign Creation Flow][2]

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Compose your email or select from a template. 
3. Take note of your `campaign_id`. After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Transactional Email Endpoint Spec]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message)
4. Click `Save Campaign` and you're set to begin your API campaign!

### Disallowed Tags in Transactional Emails 

Please note that the `Connected Content` and `Promotion Code` Liquid tags are currently not available within Transactional Email campaigns. 

Using the Connected Content tag requires Braze to make an outbound API request during our sending process which can slow down the message sending process if the external service we request is experiencing latency.  Similarly, the Promotion Code tag requires Braze to perform additional processing to evaluate the availability of a promotion before sending which can slow the sending process should one not be available.

As a result, we do not support including Connected Content or Promotion Code tags within any field of your Transactional Email campaign.


[1]: {% image_buster /assets/img/transactional_email_campaign.png %} 
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}

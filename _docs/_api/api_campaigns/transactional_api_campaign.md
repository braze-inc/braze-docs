---
nav_title: Transactional Campaigns
article_title: Transactional Campaigns
page_order: 5
description: "This reference article covers how to create and configure a new Braze transactional email campaign."
page_type: reference
alias: "/api/api_campaigns/transactional_campaigns"
tool: Campaigns

---

# Transactional Email campaigns

Transactional Emails are those that are sent to facilitate an agreed-upon transaction between a sender and the recipient. Braze's Transactional Email campaign type is purpose-built for sending automated, non-promotional email messages like order confirmations, password resets, billing alerts, or other business-critical notifications originating from your service for a single user where speed is of the utmost importance. 

{% alert important %}
Transactional Email is only available as part of select Braze packages. Reach out to your Braze Customer Success Manager for more details.
{% endalert %}

This reference article covers how to create a transational campaign in the Braze dashboard and generate a `campaign_id` to include in your API calls for our [Transactional Email API endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).


## Create a new campaign

![][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Navigate to the **Campaigns** page in your company Braze account and click **Create Campaign**, then select **Transactional Email** under the **Transactional** section.

Now, you can move on to configuring your transactional campaign.

## Configure your campaign

When launching a transactional campaign, Braze has simplified the campaign creation flow in order to ensure your business-critical transactional emails can reach all users. As a result, you will notice a few settings you may be familiar with from other Braze campaign types are not required when setting up this campaign type:

- The **Delivery** step doesn't include scheduling options. Transactional emails will always be triggered through Braze's REST API using the Campaign ID shown on the Delivery step. Additional settings, like re-eligibility controls and frequency capping settings, are not included to ensure all users are reachable for these critical transactional alerts when your service triggers a send request.
- As transactional emails enroll your entire user base as eligible (including unsubscribed users) there is no need to specify filters or segments with the **Target Users** step. As a result, if you have any logic to apply to who should receive this message, we recommend applying that logic before determining whether to make the API request to Braze to trigger the message to a specific user.
- Transactional emails do not support conversion event tracking at this time.

![][2]

1. Add a descriptive title so you can find the results on our campaigns page after you've sent your messages.
2. Compose your email or select from a template. 
3. Take note of your `campaign_id`. After you save your API campaign, you must include the generated `campaign_id` fields with your API request where noted in the [Transactional email endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message).
4. Click **Save Campaign** and you're set to begin your API campaign!

### Disallowed tags in Transactional Emails 

Note that the `Connected Content` and `Promotion Code` Liquid tags are currently not available within transactional email campaigns. 

Using the `Connected Content` tag requires Braze to make an outbound API request during our sending process, which can slow down the message sending process if the external service we request is experiencing latency.  Similarly, the `Promotion Code` tag requires Braze to perform additional processing to evaluate the availability of a promotion before sending, which can slow the sending process should one not be available.

As a result, we do not support including `Connected Content` or `Promotion Code` tags within any field of your transactional email campaign.


[1]: {% image_buster /assets/img/transactional_email_campaign.png %} 
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}

---
nav_title: Campaign alerts
article_title: Campaign Alerts
page_order: 6

page_type: reference
description: "This reference article gives an overview of campaign alerts, their benefits, as well as how to set them up to help provide you peace of mind."
tool: Campaigns
channel:
- email
- webhooks

---

# Campaign alerts

> We want to alert you when something doesn't seem quite as expected and give you peace of mind that the ship is sailing smoothly. Campaign threshold alerts provide peace of mind—be the first to know if an important campaign sends more or fewer messages than you expect.

Campaign alerts are available for the following campaigns:

- Recurring scheduled campaigns
- Action-based campaigns
- API-triggered campaigns

## Setting up your campaign alert

Navigate to the analytics page of your campaign to start setting up your alert. When you select **Set Up Alert**, you'll be able to specify upper and lower alert thresholds as well as the alert recipients and channels.

![Campaign Monitoring dialog box with two buttons: Cancel and Save.]({% image_buster /assets/img_archive/campaign_alerts.png %})

For a scheduled recurring campaign, you can set upper and lower thresholds for the messages sent each time the campaign sends. For a triggered campaign, you can set upper and lower thresholds for the number of messages sent hourly and daily.

You can set up an email alert, a webhook alert or both. Webhook alerts can be very useful, as they allow you to send an alert to a Slack channel. For more information on integrating campaign alerts with Slack, see our [documentation]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration).

{% alert note %}
When setting campaign alerts for future campaigns, you may receive updates before the campaign starts and after it ends. This is because campaign alerts will continue to send until the campaign has been manually stopped.
{% endalert %}

## Campaign alert webhook payload

The following is a sample payload for the body of a campaign alert webhook. This example uses an alert that is configured to send when messages sent falls below 500 for a given campaign send.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```


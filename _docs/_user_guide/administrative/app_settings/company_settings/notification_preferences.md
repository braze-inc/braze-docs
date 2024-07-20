---
nav_title: Notification Preferences
article_title: Notification Preferences
page_order: 1
page_type: reference
description: "This reference article covers your available options for monitoring messaging and activity in your company account."

---

# Notification preferences

> If you would like to monitor the messaging and activity in your company account, you can choose to set up specific notifications and select where they go.

The **Notification Preferences** page is where you can configure who (if anyone) receives notifications about your company. You can configure who should receive notifications about campaign delivery or technical errors. You can also specify recipients for the weekly analytics report. For most notifications, Braze supports email and webhook channels.

![Notification Preferences page in the Braze dashboard]({% image_buster /assets/img_archive/notification_preferences.png %})

To access this page, go to **Settings** > **Admin Settings** > **Notification Preferences**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), select your account dropdown and go to **Company Settings** > **Notification Preferences**.
{% endalert %}

## Available notifications

The following table lists available notifications:

| Notification | Description | Available notification channels |
|--------------|-------------|-----------------|
| AWS Credential Errors | Notifies recipients when Braze receives an error while attempting to use your Amazon Web Services credentials for a data export. | Email, Webhook |
| Campaign Automatically Stopped | Notifies recipients when Braze has stopped a campaign. | Email |
| Campaign Interaction Expiration | Notifies recipients about any campaign that is due for campaign interaction data expiration, along with any information about segments, campaigns, or Canvases that reference it in a retargeting filter and were used to send a message in the previous 30 days. | Email |
| Campaign/Canvas Updated | Notifies recipients when an active campaign/canvas is updated or deactivated, as well as when an inactive campaign/canvas is reactivated or when drafts are launched. | Email |
| Canvas Interaction Expiration | Notifies recipients about any Canvas that is due for Canvas interaction data expiration, along with any information about segments, campaigns, or Canvases that reference it in a retargeting filter and were used to send a message in the previous 30 days. | Email |
| News Feed Card Published/Live | Notifies recipients when News Feed cards are scheduled or published. | Email, Webhook |
| Push Credential Errors | Notifies recipients when an app's push credentials are invalid and when an app's push credentials are expiring soon. | Email, Webhook |
| Scheduled Campaign Sent/Not Sent | Notifies recipients when scheduled campaigns begin sending or when scheduled campaigns attempted to send but had no eligible users to send to. | Email, Webhook |
| Scheduled Campaign Limit Met | Notifies recipients when the limit for a recurring scheduled campaign has been reached. | Email, Webhook |
| Scheduled Campaign Finished Sending | Notifies recipients when a scheduled campaign has finished sending. | Email, Webhook |
| Weekly Analytics Report | Sends a summary of the past week's workspace activity to recipients every Monday. Recipients receive a summary for each workspace that they belong to. | Email |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Weekly analytics reporting

Braze optionally sends a weekly report via email to individuals you designate within your company every Monday at 5 am EST. You can select the custom events to be included in the weekly report from **Data Settings** > **Custom Events**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is located at **Manage Settings** > **Custom Events**.
{% endalert %}

You may select up to five events to be included in your weekly report:

![Selecting events to be included in the Analytics Report]({% image_buster /assets/img_archive/company_analytics_report_new.png %})

## Slack incoming webhook integration

Slack has an [incoming webhook app](https://my.slack.com/services/new/incoming-webhook/) that allows messages to be posted from external sources into Slack. To get started, open the incoming webhook app.

1. Select the Slack channel that you'd like the notifications to go to and click **Add Incoming Webhooks Integration**.<br><br>
    ![Add incoming webhooks integration in Slack]({% image_buster /assets/img_archive/slack_f.png %})<br><br>
  Slack will generate a URL that you'll need to enter into Braze for the notifications that you wish to receive.<br><br>
2. Copy the **Webhook URL**.<br><br>
    ![Copy webhook URL]({% image_buster /assets/img_archive/copy_url.png %})<br><br>
3. Navigate to the **Notification Preferences** tab in **Company Settings**.<br><br>
4. Select the notification that you wish to enable for Slack. Or, if you have multiple notifications that you want to send to this Slack channel, use **Bulk Add** to add the webhook to multiple notifications.<br><br>
    ![Select Slack notifications to enable]({% image_buster /assets/img_archive/click_edit_f.png %}){: style="max-width:60%;"}<br><br>
5. Enter the URL that Slack generated for you.

That's it! You should start receiving notifications about your company to this Slack channel. You can also check out Slack's help article on this topic: [Sending messages using Incoming Webhooks](https://api.slack.com/incoming-webhooks).



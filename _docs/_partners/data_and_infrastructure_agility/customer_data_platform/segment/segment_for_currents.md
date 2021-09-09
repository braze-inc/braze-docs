---
nav_title: Segment for Currents
article_title: Segment for Currents
page_order: 1.2
alias: /partners/segment_for_currents/
description: "This article outlines the partnership between Braze Currents and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment for Currents  

{% include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

## Integration Details

### Step 1: Obtain Segment Write Key

1. To get started, find the __Segment Write Key__ from your Segment dashboard.
2. On the Braze dashboard, navigate to __Currents__ under __Integrations__ and create a __Segment Data Export__. 
3. Add the Segment write key in the __API Key__ field. 

![Segment][1]

{% alert warning %}
It's important to keep your Segment API Key up to date. If your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

### Step 2: Export Message Engagement Events 

Next, select the message engagement events you would like to export. Reference the export events and properties table listed below. All events sent to Segment will include the user's `external_user_id` as the `userId`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

Lastly, select __Launch Current__.

{% alert warning %}
If you intend to create more than one of the same Currents connectors (for example, two message engagement event connectors), they must be in different app groups. Because the Braze Segment Currents integration cannot isolate events by different apps in a single app group, failure to do this will lead to unnecessary data deduping and lost data. 
{% endalert %}

![Segment][2]

To read more, visit Segments [documentation](https://segment.com/docs/sources/cloud-apps/appboy/).

## Data Configuration

{% tabs %}
{% tab Export Events %}

You can export the following data from Braze to Segment:

| Event Name | Description |
| ----- | ----- |
| Push Notification Sent         | A push notification was successfully sent. |
| Push Notification Tapped       | User opened a push notification. |
| Push Notification Bounced      | Braze was not able to send a push notification to this User. |
| iOS Foreground Push Opened     | User received a push notification on iOS while the app was open. |
| Email Sent                     | An email was successfully sent. |
| Email Delivered                | An email was successfully delivered to a User's mail server. |
| Email Opened                   | User opened an email. |
| Email Link Clicked             | User clicked a link in an email. Email click tracking must be enabled. |
| Email Bounced                  | Braze attempted to send an email, but the User's receiving mail server did not accept it. |
| Email Soft Bounced             | Braze attempted to send an email, but the User's receiving mail server temporarily bounced it. <br> <br> (Reasons may include a full inbox or a downed server, among other things.) |
| Email Marked As Spam           | User marked an email as spam. |
| Email Unsubscribed             | User clicked the unsubscribe link in an email. |
| SMS Sent                       | An SMS was sent. |
| SMS Sent to Carrier            | An SMS was sent to the Carrier for delivery. |
| SMS Delivered                  | An SMS was delivered successfully. |
| SMS Delivery Failed            | An SMS was unable to be delivered successfully. |
| SMS Rejected                   | An SMS was rejected. |
| SMS Inbound Received           | An inbound SMS was received. |
| Subscription Group State Changed | User's subscription group state changed to 'Subscribed' or 'Unsubscribed'. |
| In-App Message Viewed          | User viewed an In-App Message. |
| In-App Message Clicked         | User tapped or clicked a button in an In-App Message. |
| Content Card Sent              | A Content Card was sent to a user's device. |
| Content Card Viewed            | User viewed a Content Card. |
| Content Card Clicked           | User clicked a Content Card. |
| Content Card Dismissed         | User dismissed a Content Card. |
| News Feed Viewed               | User viewed the native Braze News Feed. |
| News Feed Card Viewed          | User viewed a Card within the native Braze News Feed. |
| News Feed Card Clicked         | User clicked on a Card within the native Braze News Feed. |
| Webhook Sent                   | A webhook message was sent. |
| Campaign Converted             | User performed a conversion event for a campaign within its conversion window. |
| Canvas Converted               | User performed a conversion event for a Canvas within its conversion window. |
| Canvas Entered                 | User was entered into a Canvas. |
| Campaign Control Group Entered | User was enrolled in a campaign control group. |
| Application Uninstalled        | User uninstalled the App. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Export Properties %}

The following properties will be included with all Braze Events sent to Segment:

| Property Name          | Type     | Description |
| ---------------------- | -------- | ----        |
| `app_id`               | `String` | The API Identifier of the App on which a user received a message or performed an action, if applicable. |
| `send_id`              | `String` | The id of the message if specified for the campaign, if applicable. |
| `dispatch_id`          | `String` | The id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user. |
| `campaign_id`          | `String` | The API Identifier of the campaign associated with the event, if applicable. |
| `campaign_name`        | `String` | The name of the campaign associated with the event, if applicable. |
| `message_variation_id` | `String` | The API Identifier of the Message Variation for the campaign associated with the event, if applicable. |
| `canvas_id`            | `String` | The API Identifier of the Canvas associated with the event, if applicable. |
| `canvas_name`          | `String` | The name of the Canvas associated with the event, if applicable. |
| `canvas_variation_id`  | `String` | The API Identifier of the Canvas Variation associated with the event, if applicable.                           |
| `canvas_step_id`       | `String` | The API Identifier of the Canvas Step associated with the event, if applicable. |
| `in_control_group`     | `String` | For Canvas Entered events, whether or not the user was enrolled in the control group - always either `true` or `false` |
| `context.traits.email` | `String` | For Email events, the email address that the email was sent to. |
| `link_url`             | `String` | For Email Clicked events, the URL of the link that the user clicked on. |
| `button_id`            | `String` | For In-App Message Clicked events, the index of the button the user clicked on. |
| `card_id`              | `String` | For News Feed Card and Content Card events, the API Identifier of the Card. |
| `subscription_group_id` | `String` | For Subscription Group State Changed events, the API Identifier of the Subscription Group. |
| `subscription_status`  | `String` | For Subscription Group State Changed events, the status the user changed to, either 'Subscribed' or 'Unsubscribed'. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img_archive/currents-segment-edit.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}

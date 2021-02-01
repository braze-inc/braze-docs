---
nav_title: Segment for Currents
page_order: 1.2
alias: /partners/segment_for_currents/

description: "This article outlines the partnership between Braze Currents and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: currents

---

# About Segment & Currents  

{% include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

To get started, find the following information from your Segment dashboard:

-   Segment Write Key

Add this information to the Segment integration page on the dashboard, and press save.

![Segment]({% image_buster /assets/img_archive/currents-segment-edit.png %})

All events sent to Segment will include the user's `external_user_id` as the `userId`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

Segment's documentation is available [here](https://segment.com/docs/sources/cloud-apps/appboy/).

## Integration Details

You can export the following data from Braze to Segment:

| Event Name | Description |
| ----- | ----- |
| Push Notification Sent         | A push notification was successfully sent. |
| Push Notification Tapped       | User opened a push notification. |
| Push Notification Bounced      | Braze was not able to send a push notification to this User. |
| iOS Foreground Push Opened     | User received a push notification on iOS while the app was open. |
| Email Sent                     | An email was successfully sent. |
| Email Delivered                | An email was successfully delivered to a User’s mail server. |
| Email Opened                   | User opened an email. |
| Email Link Clicked             | User clicked a link in an email. Email click tracking must be enabled. |
| Email Bounced                  | Braze attempted to send an email, but the User’s receiving mail server did not accept it. |
| Email Soft Bounced             | Braze attempted to send an email, but the User’s receiving mail server temporarily bounced it. <br> <br> (Reasons may include a full inbox or a downed server, among other things.) |
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
| Campaign Converted             | User performed a conversion event for a Campaign within its conversion window. |
| Canvas Converted               | User performed a conversion event for a Canvas within its conversion window. |
| Canvas Entered                 | User was entered into a Canvas. |
| Campaign Control Group Entered | User was enrolled in a Campaign control group. |
| Application Uninstalled        | User uninstalled the App. |
{: .reset-td-br-1 .reset-td-br-2}

The following properties will be included with all Braze Events sent to Segment:

| Property Name          | Type     | Description |
| ---------------------- | -------- | ----        |
| `app_id`               | `String` | The API Identifier of the App on which a user received a message or performed an action, if applicable. |
| `send_id`              | `String` | The id of the message if specified for the campaign, if applicable. |
| `dispatch_id`          | `String` | The id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user. |
| `campaign_id`          | `String` | The API Identifier of the Campaign associated with the event, if applicable. |
| `campaign_name`        | `String` | The name of the Campaign associated with the event, if applicable. |
| `message_variation_id` | `String` | The API Identifier of the Message Variation for the Campaign associated with the event, if applicable. |
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

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

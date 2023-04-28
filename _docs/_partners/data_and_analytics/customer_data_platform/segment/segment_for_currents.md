---
nav_title: Segment.io for Currents
article_title: Segment.io for Currents
page_order: 1.2
alias: /partners/segment_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Segment.io, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment.io for Currents  

> [Segment.io](https://segment.com) is a customer data platform that helps you collect, clean, and activate your customer data. This reference article will give an overview of the connection between Braze Currents and Segment.io and describe requirements and processes for proper implementation and usage.

The Braze and Segment.io integration allows you to leverage Braze Currents to export your Braze events to Segment.io to drive deeper analytics into conversions, retention, and product usage. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Segment.io account | A [Segment.io account](https://app.segment.com/login) is required to take advantage of this partnership. |
| Braze destination | You must have already [set up Braze as a destination]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/#connection-settings/) in your Segment.io integration.<br><br>This includes providing the correct Braze data center and REST API key in your [connection settings]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/#connection-settings). |
| Currents | In order to export data back into Segment.io, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Obtain Segment.io write key

1. In your Segment.io dashboard, select your Segment.io source. Next, go to **Settings > API keys**. Here you will find the **Segment.io Write Key**.
2. In Braze, navigate to **Currents > + Create Currents > Create Segment.io Export**.
3. Next, provide an integration name, contact email, Segment.io write key, and Segment.io region.

![The Segment.io Currents page in Braze. Here, you can find fields for integration name, contact email, segment region, and API key.][3]

{% alert warning %}
It's important to keep your Segment.io write key up to date. If your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

### Step 2: Export message engagement events 

Next, select the message engagement events you would like to export. Reference the following export events and properties table listed. All events sent to Segment.io will include the user's `external_user_id` as the `userId`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

![List of all available message engagement events on the Segment.io Currents page in Braze.][2]

Lastly, select **Launch Current**.

{% alert warning %}
If you intend to create more than one of the same Currents connectors (for example, two message engagement event connectors), they must be in different app groups. Because the Braze Segment.io Currents integration cannot isolate events by different apps in a single app group, failure to do this will lead to unnecessary data deduping and lost data. 
{% endalert %}

To read more, visit Segment.io [documentation](https://segment.com/docs/sources/cloud-apps/appboy/).

## Supported Currents events

Braze supports exporting the following data listed in the Currents [user behavior]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) and [message engagement]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) event glossaries to Segment.io:
 
### Behaviors
- Uninstall: `users.behaviors.Uninstall`
- App (news feed impression)
  - `users.behaviors.app.NewsFeedImpression`
- Subscription (global state change): `users.behaviors.subscription.GlobalStateChange`
- Subscription group (state change): `users.behaviors.subscriptiongroup.StateChange`
  
### Campaigns
- Abort: `users_campaigns_abort`
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canvas
- Abort: `users_canvas_abort`
- Conversion: `users.canvas.Conversion`
- Entry: `users.canvas.Entry`
- Exit (matched audience, performed event)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Experiment Step (conversion, split entry)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Messages
- Content Card (abort, click, dismiss, impression, send)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- Email (abort, bounce, click, delivery, markasspam, open, send, softbounce, unsubscribe)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- In-app message (abort, click, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- News Feed card (abort, click, impression)
  - `users.messages.newsfeedcard.Abort`
  - `users.messages.newsfeedcard.Click`
  - `users.messages.newsfeedcard.Impression`
- Push notification (abort, bounce, iOSforeground, open, send)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abort, carrier send, delivery, delivery failure, inbound recieve, rejection, send, short link click)
  - `users.messages.sms.Abort`
  - `users.messages.sms.CarrierSend`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abort, send)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}

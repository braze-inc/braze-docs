---
nav_title: Segment for currents
article_title: Segment for Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Segment, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment for Currents  

> [Segment](https://segment.com) is a customer data platform that helps you collect, clean, and activate your customer data. This reference article will give an overview of the connection between Braze Currents and Segment and describe requirements and processes for proper implementation and usage.

The Braze and Segment integration allows you to leverage Braze Currents to export your Braze events to Segment to drive deeper analytics into conversions, retention, and product usage. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Segment account | A [Segment account](https://app.segment.com/login) is required to take advantage of this partnership. |
| Braze destination | You must have already [set up Braze as a destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) in your Segment integration.<br><br>This includes providing the correct Braze data center and REST API key in your [connection settings]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | In order to export data back into Segment, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Obtain Segment write key

In your Segment dashboard, select your Segment source. Next, go to **Settings > API keys**. Here you will find the **Segment Write Key**.

{% alert warning %}
It's important to keep your Segment write key up to date. If your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

### Step 2: Create a new Currents connector

1. In Braze, navigate to **Partner Integrations** > **Data Export**.
2. Click **+ Create New Current** > **Segment Data Export**.
3. Next, provide an integration name, contact email, Segment write key, and Segment region.

![The Segment Currents page in Braze. Here, you can find fields for integration name, contact email, segment region, and API key.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Step 3: Export message engagement events

Next, select the message engagement events you would like to export. Reference the following export events and properties table listed. All events sent to Segment will include the user's `external_user_id` as the `userId` and the user's `braze_id` as the `anonymousId`.

Keep in mind, Braze only sends event data for users without an `external_user_id` if **Include events from anonymous users** is checked.

{% alert important %}
Anonymous user export is currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

![List of all available message engagement events on the Segment Currents page in Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Lastly, select **Launch Current**.

{% alert warning %}
If you intend to create more than one of the same Currents connectors (for example, two message engagement event connectors), they must be in different workspaces. Because the Braze Segment Currents integration cannot isolate events by different apps in a single workspace, failure to do this will lead to unnecessary data deduping and lost data. 
{% endalert %}

To read more, visit Segment [documentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/).

## Updating your Current

{% multi_lang_include updating_currents.md %}

## Supported Currents events

Braze supports exporting the following data listed in the Currents [user behavior]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) and [message engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) event glossaries to Segment:
 
### Behaviors
- Uninstall: `users.behaviors.Uninstall`
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
- Push notification (abort, bounce, iOSforeground, open, send)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (abort, carrier send, delivery, delivery failure, inbound receive, rejection, send, short link click)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (abort, send)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (abort, delivery, failure, inbound receive, read, send)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`


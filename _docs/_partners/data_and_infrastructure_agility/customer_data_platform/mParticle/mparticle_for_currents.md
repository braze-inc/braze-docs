---
nav_title: mParticle for Currents
article_title: mParticle for Currents
page_order: 0.5
alias: /partners/mparticle_for_currents/
description: "This reference article outlines the partnership between Braze Currents and mParticle, a customer data platform that collects and routes information between sources in your marketing stack."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle for Currents

> [mParticle](https://www.mparticle.com) is a customer data platform that collects and routes information from multiple sources to a variety of other locations in your marketing stack.

The Braze and mParticle integration allows you to seamlessly control the flow of information between the two systems. With Currents, you can also connect data to mParticle to make it actionable across the entire growth stack. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| mParticle account | An [mParticle account](https://app.mparticle.com/login) is required to take advantage of this partnership. |
| Currents | In order to export data back into mParticle, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
| mParticle server to server key<br><br>mParticle server to server secret | These can be obtained by navigating to your mParticle dashboard and creating the [necessary feeds](#step-1-create-feeds) that allow mParticle to receive Braze interaction data for iOS, Android, and Web platforms.|
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create feeds

From your mParticle admin account, navigate to **Setup > Inputs**. Locate **Braze** in the mParticle **Directory** and add the feed integration.

The Braze feed integration supports four separate feeds: iOS, Android, Web, and Unbound. The unbound feed can be used for events such as emails that are not connected to a platform. You will need to create an input for each main platform feed. You can create additional inputs from **Setup > Inputs**, on the **Feed Configurations** tab.

![][1]

For each feed, under **Act as Platform** select the matching platform from the list. If you do not see an option to select an **act-as** feed, the data will be treated as unbound, but can still be forwarded to data warehourse outputs.

![The first integration dialog box, prompting you to provide a configuration name, determine a feed status, and select a platform to act as.][2]{: style="max-width:40%;"}  ![The second integration dialog box showing the server-to-server key and server-to-server secret.][3]{: style="max-width:37%;"}

As you create each input, mParticle will provide you with a key and secret. Copy these credentials, making sure to note which feed each pair of credentials is for.

### Step 2: Create Current

In Braze, navigate to **Currents > + Create Current > Create mParticle Export**. Provide an integration name,  contact email and the mParticle API key and mParticle secret key for each platform. Next, select the events you want to track; a list of available events is provided. Lastly, click **Launch Current**

![The mParticle Currents page in Braze. Here, you can find fields for integration name, contact email, API key, and secret key.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
It's important to keep your mParticle API Key and mParticle Secret Key up to date; if your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped and data will be permanently lost.
{% endalert %}

All events sent to mParticle will include the user's `external_user_id` as the `customerid`. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

## Supported Currents events

Braze supports exporting the following data listed in the Currents [user behavior]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) and [message engagement]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) event glossaries to mParticle:

### Behaviors
- Uninstall: `users.behaviors.Uninstall`
- App (news feed impression): `users.behaviors.app.NewsFeedImpression`
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
- In-app message (abort, click, impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- News Feed card (abort, click, impression)
  - `users.messages.newsfeedcard.Abort`
  - `users.messages.newsfeedcard.Click`
  - `users.messages.newsfeedcard.Impression`
- Push notification (abort, bounce, open, send)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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
- WhatsApp (abort, delivery, failure, inbound recieve, read, send)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`


To read more about the mParticle integration, visit their documentation [here](http://docs.mparticle.com/integrations/braze/feed).

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}

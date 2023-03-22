---
nav_title: Mixpanel for Currents
article_title: Mixpanel for Currents
page_order: 0
alias: /partners/mixpanel_for_currents/
description: "This reference article outlines the partnership between Braze Currents and Mixpanel, a business analytics platform, allowing you to import Mixpanel Cohorts into Braze to create Braze segments that can be used to target users in future Braze campaigns or Canvases."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel for Currents

{:.subintro}
[Mixpanel](https://mixpanel.com/) is a business analytics platform that allows you to export events from Mixpanel into other platforms to perform deeper analysis. The data collected can then be used to build custom reports and measure user engagement and retention.

The Braze and Mixpanel integration allows you to [import Mixpanel Cohorts into Braze](#data-import-integration) to create Braze segments that can be used to target users in future Braze campaigns or Canvases. You can also leverage Braze Currents to [export your Braze events to Mixpanel](#data-export-integration) to drive deeper analytics into conversions, retention, and product usage. 

## Prerequisites

| Requirement | Description |
|---|---|
| Mixpanel account | A [Mixpanel account](https://mixpanel.com/) is required to take advantage of this partnership. |
| Currents | In order to export data back into Mixpanel, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2} 

## Data import integration

Use Braze and Mixpanel's partnership to configure your integration and import Mixpanel cohorts directly into Braze for retargeting, creating a full loop of data from one system to another. This allows you to perform a deeper analysis using Mixpanel and seamlessly execute your strategies using Braze.

Any integration you set up will count towards your account's data point volume.

{% alert important %}
In adherence to Mixpanel's data retention policies, events sent before January 1, 2010 will be removed during import.
{% endalert %}

### Step 1: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Mixpanel**. Here, you will find the REST endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Mixpanel's dashboard.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Step 2: Set up the Braze integration in Mixpanel

In Mixpanel, navigate to **Data Management > Integrations.** Next, select the Braze integration tab and click **Connect**. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Continue**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Step 3: Export a Mixpanel cohort to Braze

In Mixpanel, navigate to **Data Management > Cohorts.** Select the cohort to send to Braze and then select **Export to Braze**. Lastly, select a one-time sync or dynamic sync. Selecting dynamic sync will sync your Braze cohort every 15 minutes to match users in Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### Step 4: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement**, name your segment, and select **Mixpanel_Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Mixpanel. 

![In the Braze segment builder, the user attributes filter "Mixpanel cohorts" is set to "includes" and "Braze cohort".]({% image_buster /assets/img_archive/mixpanel1.png %})

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

## Data export integration

A full list of the events that can be exported from Braze to Mixpanel can be found below. All events sent to Mixpanel will include the user's `external_user_id` as the Mixpanel Distinct ID. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

You can export two types of events to Mixpanel: [Message Engagement Events](#message-engagement-events) consisting of the Braze Events directly related to message sending, and [Customer Behavior Events](#customer-behavior-events) including other app or website activity such as sessions, custom events, and purchases tracked through the platform. All custom events are prefixed with `[Braze Custom Event]`. Custom event properties and purchase event properties are prefixed with `[Custom event property]` and `[Purchase property]`, respectively.

Contact your account manager or open a [support ticket][support] if you need access to additional event entitlements.

### Step 1: Get Mixpanel credentials

In your Mixpanel dashboard, click into the **Project Settings**in either a new or existing project. Here you will find the Mixpanel API secret and Mixpanel Token. These credentials will be used in the next step to create your Currents connection. 

### Step 2: Create Braze Current

In Braze, navigate to **Currents > + Create Current > Create Mixpanel Export**. Provide an integration name, contact email, Mixpanel API secret, and Mixpanel token in the listed fields. Next, select the events you want to track; a list of available events is provided. Lastly, click **Launch Current**

![The Braze Mixpanel Currents page. This page includes fields for integration name, contact email, API secret, and mixpanel export token. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Check out Mixpanel's [integration docs](https://help.mixpanel.com/hc/en-us/articles/360001243663) to learn more. 
{% endtab %}

## Supported Currents events

Braze supports exporting the following data listed in the Currents [user behavior]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) and [message engagement]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) event glossaries to Mixpanel:

### Behaviors
- Custom event: `users.behaviors.CustomEvent`
- Install Attribution: `users.behaviors.InstallAttribution`
- Location: `users.behaviors.Location`
- Purchase: `users.behaviors.Purchase`
- Uninstall: `users.behaviors.Uninstall`
- App (first session, news feed impression, session end, session start)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.NewsFeedImpression`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Subscription (global state change): `users.behaviors.subscription.GlobalStateChange`
- Subscription Group (state change): `users.behaviors.subscriptiongroup.StateChange`
  
### Campaigns
<!--- Abort// not live yet-->
- Conversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canvas
<!--- Abort// not live yet-->
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

[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}

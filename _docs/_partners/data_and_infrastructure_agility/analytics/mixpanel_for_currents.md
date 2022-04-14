---
nav_title: Mixpanel for Currents
article_title: Mixpanel for Currents
page_order: 0
alias: /partners/mixpanel_for_currents/
description: "This article outlines the partnership between Braze Currents and Mixpanel, a business analytics platform."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# Mixpanel for Currents

> [Mixpanel](https://mixpanel.com/) is a business analytics platform that allows you to export events from Mixpanel into other platforms to perform deeper analysis. The data collected can then be used to build custom reports and measure user engagement and retention.

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

A full list of the events that can be exported from Braze to Mixpanel is included in the [user profile endpoints section](#amplitude-user-profile-api-endpoints). All events sent to Mixpanel will include the user's `external_user_id` as the Mixpanel Distinct ID. At this time, Braze does not send event data for users who do not have their `external_user_id` set.

You can export two types of events to Mixpanel: [Message Engagement Events](#message-engagement-events) consisting of the Braze Events directly related to message sending, and [Customer Behavior Events](#customer-behavior-events) including other app or website activity such as sessions, custom events, and purchases tracked through the platform. All custom events are prefixed with `[Braze Custom Event]`. Custom event properties and purchase event properties are prefixed with `[Custom event property]` and `[Purchase property]`, respectively.

Contact your Account Manager or open a [support ticket][support] if you need access to additional event entitlements.

### Step 1: Get Mixpanel credentials

In your Mixpanel dashboard, click into the **Project Settings**in either a new or existing project. Here you will find the Mixpanel API secret and Mixpanel Token. These credentials will be used in the next step to create your Currents connection. 

### Step 2: Create Braze Current

In Braze, navigate to **Currents > + Create Current > Create Mixpanel Export**. Provide an integration name, contact email, Mixpanel API secret, and Mixpanel token in the listed fields. Next, select the events you want to track; a list of available events is provided. Lastly, click **Launch Current**

![The Braze Mixpanel Currents page. This page includes fields for integration name, contact email, API secret, and mixpanel export token. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Check out Mixpanel's [integration docs](https://help.mixpanel.com/hc/en-us/articles/360001243663) or this Braze [Mixpanel LAB course](https://lab.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2) to learn more. 
{% endtab %}

## Customer behavior events

### Custom events

```json
// <Custom Event Name>
{
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Purchase events

```json
// Purchase
{
  "product_id": (string) id of product purchased (sent in the “productId” field of Mixpanel HTTP API),
  "price": (float) price of product (sent in the “price” field of Mixpanel HTTP API),
  "currency": (string) three letter alpha ISO 4217 currency code,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Session events

```json
// First Session
{
  "session_id": (string) id of the session,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// Session Start
{
  "session_id": (string) id of the session,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// Session End
{
  "session_id": (string) id of the session,
  "duration": (float) seconds session lasted,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Location events

```json
// Location
{
  "longitude": (float) longitude of recorded location,
  "latitude": (float) latitude of recorded location,
  "altitude": (float) altitude of recorded location,
  "ll_accuracy": (float) a percentage representing the OS determined accuracy of the recorded location,
  "alt_accuracy": (float) altitude accuracy of recorded location,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Install attribution events

```json
// Install Attribution
{
  "source": (string) the source of the attribution
}
```

### Uninstall events

```json
// Uninstall
{
  "app_id": (string) id for the app on which the user action occurred
}
```

## Message engagement events

### Push notification events

```json
// Push Notification Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
// Push Notification Open
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
// Push Notification iOS Foreground Open
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
// Push Notification Bounce
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the bounce occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
```

### Email events

```json
// Email Send
// Email Delivery
// Email Open
// Email Click
// Email Bounce
// Email Soft Bounce
// Email Mark As Spam
// Email Unsubscribe
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user’s system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "link_id": (string) unique value generated by Braze for the URL (Email Click events only and requires link aliasing to be enabled),
  "link_alias": (string) alias name set when the message was sent (Email Click events only and requires link aliasing to be enabled),
  "machine_open": (string) Indicator of whether the email was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (e.g., "Apple" or "Google" to indicate which process made the fetch) may be added in the future. (Email Open events only)
}
```

Behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [`dispatch_id` behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in campaigns and Canvases. For additional information, refer to the [Customer Behavior and User Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) and [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).


### SMS events

```json
// SMS Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
}

// SMS Send To Carrier
// SMS Delivery
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
}

// SMS Rejection
// SMS Delivery Failure
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
  "error": (string) Error message for the rejection or delivery failure,
  "provider_error_code": (string) Error code for the rejection or delivery failure,
}

// SMS Inbound Receipt
{
  "inbound_phone_number": (string) phone number on which the message was received,
  "subscription_group_id": (string) api id of the subscription group from which this SMS message was received,
  "user_phone_number": (string) the number from which message was sent,
  "action": (string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),
  "message_body": (string) the text of the message,
}
```

### Subscription events

```json
// Subscription Group State Change
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "email_address": (string) email address for this event,
  "subscription_group_id": (string) id of the subscription group,
  "subscription_status": (string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed'
}
```

### In-app message Events

```json
// In-app message Impression
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// In-app message Click
{
  "button_id": (string) index of the button clicked, if it was a button that was clicked, or tracking ID of the click, if the event came from an appboyBridge.logClick invocation,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Webhook events

```json
// Webhook Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

### Content Card events

```json
// Content Card Send
{
  "card_id": (string) id of the content card that was sent,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

```json
// Content Card Impression
// Content Card Click
// Content Card Dismiss
{
  "card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### News Feed events

```json
// News Feed Card Impression
{
  "card_id": (string) id of the card that was viewed,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// News Feed Card Click
{
  "card_id": (string) id of the card that was clicked,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// News Feed Impression
{
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Conversion events

```json
// Campaign Conversion Event
{
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
// Canvas Conversion Event
{
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) id of the last step the user was sent before the conversion
}
```

### Canvas entry events

```json
// Canvas Entry
{
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "in_control_group": (boolean) whether the user was enrolled in the control group for a Canvas
}
```

### Campaign enrollment events

```json
// Campaign Control Group Enrollment
{
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}

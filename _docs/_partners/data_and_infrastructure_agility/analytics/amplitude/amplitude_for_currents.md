---
nav_title: Amplitude for Currents
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_for_currents/
description: "This article outlines the partnership between Braze Currents and Amplitude, a product analytics and business intelligence platform."
page_type: partner
tool: Currents
search_tag: Partner

---

# Amplitude for Currents

{% include video.html id="7yadPjDImxQ" align="right" %}

> [Amplitude](https://amplitude.com/) is a product analytics and business intelligence platform.

The Braze and Amplitude integration allows you to [import Amplitude Cohorts into Braze](#data-import-integration) to create segments that can target users in future campaigns or Canvases. You can also leverage Braze Currents to [export your Braze events to Amplitude](#data-export-integration) to perform deeper analytics of your product and marketing data.

## Prerequisites

| Requirement | Description |
|---|---|
| Amplitude account | An [Amplitude account](https://amplitude.com/) is required to take advantage of this partnership. |
| Currents | In order to export data back into Amplitude, you need to have [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) set up for your account. |
{: .reset-td-br-1 .reset-td-br-2} 

## Data import integration

Use Braze and Amplitude's partnership to import Amplitude cohorts directly into Braze for audience segmentation. This allows you to perform deep analysis using Amplitude and seamlessly execute your strategies using Braze.

Any integration you set up will count towards your account's data point volume.

### Step 1: Get the Braze data import key

In Braze, navigate to **Technology Partners** and select **Amplitude**. Here, you will find the REST endpoint and generate your Braze data import key. Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Amplitude's dashboard.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Step 2: Set up the Braze integration in Amplitude

In Amplitude, navigate to **Sources & Destinations > [project name] > Destinations > Braze**. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Save**.

![]({% image_buster /assets/img/amplitude.png %}){: style="max-width:50%;"}

### Step 3: Export an Amplitude cohort to Braze

To export users from Amplitude to Braze, first create a [cohort](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) of users you wish to export. Once you have created a cohort, click **Sync to...** to export these users to Braze.

#### Scheduled cohort syncs

Cohort syncs can be scheduled to be performed hours or daily. Scheduled sync will only send the updated data set deltas to minimize data point usage.

### Step 4: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement**, name your segment, and select **Amplitude Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Amplitude. 

![In the Braze segment builder, the filter "amplitude_cohorts" is set to "includes_value" and "Amplitude cohort test".]({% image_buster /assets/img/amplitude2.png %})

Once saved, you can reference this segment during Canvas or campaign creation in the targeting users step.

## Data export integration

A full list of the events that can be exported from Braze to Amplitude is shown below. All events sent to Amplitude will include the user's `external_user_id` as the Amplitude user ID. Braze will only send event data for users who have their `external_user_id` set or anonymous users who have their `device_id` set. Braze-specific event properties will be sent under the `event_properties` key in the data sent to Amplitude. The properties for each event type are listed below.

You can export two types of events to Amplitude: [Message Engagement Events](#message-engagement-events) consisting of the Braze Events directly related to message sending, and [Customer Behavior Events](#customer-berhavior-events), including other app or website activity such as sessions, custom events, and purchases tracked through the platform. All regular events are prefixed with `[Appboy]`, and all custom events are prefixed with `[Appboy] [Custom Event]`. Custom event properties and purchase event properties are prefixed with `[Custom event property]` and `[Purchase property]`, respectively.

All cohorts named and imported into Braze will be prefixed with `[Amplitude]` and suffixed with their `cohort_id`. This means that a cohort named "TEST_COHORT" with the `cohort_id` "abcd1234" will be titled `[Amplitude] TEST_COHORT: abcd1234` in Braze filters.

Please contact your Account Manager or open a [support ticket][support] if you need access to additional event entitlements.

### Step 1: Configure Amplitude Integration in Braze 

In Amplitude, locate your Amplitude export API key.

{% alert warning %}
Keep your Amplitude API Key up to date. If your connector's credentials expire, the connector will stop sending events. If this persists for more than **48 hours**, the connector's events will be dropped, and data will be permanently lost.
{% endalert %}

### Step 2: Create Braze Current

In Braze, navigate to **Currents > + Create Current > Create Amplitude Export**. Provide an integration name, contact email, Amplitude export API key, and Amplitude region in the listed fields. Next, select the events you want to track; a list of available events is provided below. Lastly, click **Launch Current**

![The Braze Amplitude Currents page. This page includes fields for integration name, contact email, API key, and US region. The lower half of the Currents page lists available Currents events you can send.]({% image_buster /assets/img/amplitude4.png %})

{% tab note %}
Check out Amplitude's [integration docs](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) or this Braze [Amplitude LAB course](https://lab.braze.com/amplitude-integration-with-braze) to learn more. 
{% endtab %}

## Rate limits

Currents connect to Amplitude's HTTP API, which has a [Rate Limit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) of 30 events/second per device and an undocumented limit of 500K events/day per device. Above these thresholds, Amplitude will throttle events that are logged through Currents. If a device in your integration is sending above this rate limit, you may experience a delay in when events from all devices will appear in Amplitude.

Devices should not report more than 30 events/second or 500K events/day under normal circumstances, and this event pattern should only occur due to a misconfigured integration. To avoid this type of delay, ensure that your SDK integration is reporting events at a normal rate as specified in our SDK integration instructions and refrain from running automated tests that generate many events for a single device.

## Amplitude user profile API endpoints

To check out some of the common Amplitude API endpoints, view our dedicated [Amplitude API documentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/).

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
  "product_id": (string) id of product purchased (sent in the “productId” field of Amplitude HTTP API),
  "price": (float) price of product (sent in the “price” field of Amplitude HTTP API),
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user’s system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "link_id": (string) unique value generated by Braze for the URL (Email Click events only, and requires link aliasing to be enabled),
  "link_alias": (string) alias name set when the message was sent (Email Click events only, and requires link aliasing to be enabled),
  "machine_open": (string) Indicator of whether the email was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (e.g. "Apple" or "Google" to indicate which process made the fetch) may be added in the future. (Email Open events only)
}
```

### SMS events
```json
// SMS Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
}

// SMS Send To Carrier
// SMS Delivery
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "error": (string) Error message for the rejection or delivery failure,
  "provider_error_code": (string) Error code for the rejection or delivery failure,
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "email_address": (string) email address for this event,
  "subscription_group_id": (string) id of the subscription group,
  "subscription_status": (string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed'
}
```

### In-App Message Events

```json
// In-App Message Impression
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// In-App Message Click
{
  "button_id": (string) index of the button clicked, if it was a button that was clicked, or tracking ID of the click, if the event came from an appboyBridge.logClick invocation,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
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

### Uninstall events

```json
// Uninstall
{
  "app_id": (string) id for the app on which the user action occurred
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
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
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
}
```
[support]: {{site.baseurl}}/braze_support/

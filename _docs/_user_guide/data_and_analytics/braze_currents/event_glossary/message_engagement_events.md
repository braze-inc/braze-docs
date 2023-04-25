---
nav_title: Message Engagement Events
layout: message_engagement_events_glossary
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 6
---

Contact your account manager or open a [support ticket]({{site.baseurl}}/braze_support/) if you need access to additional event entitlements. If you can't find what you need in this article, check out our [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of message engagement event structure and platform values %}

### Event structure

This event breakdown shows what type of information is generally included in a message engagement event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports, charts and take advantage of other valuable data metrics.

![Breakdown of a message engagement event showing an email unsubscribe event with the listed properties grouped by user-specific properties, campaign or Canvas tracking properties, and event-specific properties]({% image_buster /assets/img/message_engagement_event.png %})

Message engagement events are comprised of **user-specific** properties, **campaign/canvas tracking** properties, and **event-specific** properties.

### Platform values

Certain events return a `platform` value that specifies the platform of the user's device. 
<br>The following table details the possible returned values:

| User device | Platform value |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2}

{% enddetails %}

{% alert important %}
These schemas only apply to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage). For schemas that apply to the other partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) and check their respective pages.<br><br>Additionally, note that Currents will drop events with excessively large payloads of greater than 900KB.
{% endalert %}

{% api %}

## Content Card abort message events

{% apitags %}
Abort, Content Cards
{% endapitags %}

This event occurs if a Content Card message was aborted based on Liquid aborts, quiet hours, etc.

```json
// Content Card Abort: users.messages.contentcard.Abort

{
  "abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
  "abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_name": (optional, string) name of the campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_step_id": (optional, string) id of the canvas step this event belongs to,
  "canvas_step_message_variation_id": (optional, string) id of the canvas step message variation this user received,
  "canvas_step_name": (optional, string) name of the canvas step this event belongs to,
  "canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
  "canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
  "device_id": (optional, string) id of the device on which the event occurred,
  "dispatch_id": (optional, string) ID of the dispatch this message belongs to,
  "external_user_id": (optional, string) External user ID of the user,
  "id": (required, string) globally unique ID of this event,
  "message_variation_id": (optional, string) message variation ID of the variation this user received,
  "message_variation_name": (optional, string) name of the message variation this user received,
  "send_id": (optional, string) message send ID this message belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "timezone": (optional, string) timezone of the user,
  "user_id": (required, string) BSON id of the user that performed this event
}
```
{% endapi %}

{% api %}

## Email abort message events

{% apitags %}
Abort, Email
{% endapitags %}

This event occurs if an email message was aborted based on Liquid aborts, quiet hours, etc.

```json
// Email Abort: users.messages.email.Abort

{
  "abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
  "abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_name": (optional, string) name of the campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_step_id": (optional, string) id of the canvas step this event belongs to,
  "canvas_step_message_variation_id": (optional, string) id of the canvas step message variation this user received,
  "canvas_step_name": (optional, string)name of the canvas step this event belongs to,
  "canvas_variation_id": (optional, string) Canvas variation ID of the variation this event belongs to,
  "canvas_variation_name": (optional, string) name of the Canvas variation this event belongs to,
  "device_id": (optional, string) id of the device on which the event occurred,
  "dispatch_id": (optional, string) ID of the dispatch this message belongs to,
  "email_address": (required, string) email address of the user,
  "external_user_id": (optional, string) External user ID of the user,
  "id": (required, string) globally unique ID of this event,
  "ip_pool": (optional, string) IP Pool from which the email send was made
  "message_variation_id": (optional, string) message variation ID of the variation this user received,
  "message_variation_name": (optional, string) name of the message variation this user received,
  "send_id": (optional, string) message send ID this message belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "timezone": (optional, string) timezone of the user,
  "user_id": (required, string) BSON id of the user that performed this event, 
}
```
{% endapi %}

{% api %}

## Push notification abort events

{% apitags %}
Abort, Push
{% endapitags %}

This event occurs if a push notification message was aborted based on Liquid aborts, quiet hours, etc.

```json
// Push Notification Abort: users.messages.pushnotification.Abort

{
  "abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
  "abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "app_id": (required, string) BSON id of the app this user belongs to,
  "campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_name": (optional, string) name of the campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (optional, string) id of the canvas step message variation this user received
  "canvas_step_name": (optional, string) API id of the canvas step this event belongs to,
  "canvas_variation_id": (optional, string) id of the canvas variation this event belongs to,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "dispatch_id": (optional, string) ID of the dispatch this message belongs to,
  "external_user_id": (optional, string) External user ID of the user,
  "message_variation_id": (optional, string) ID of the message variation this user received,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "platform": (required, string) platform of the device,
  "send_id": (optional, string) message send ID this message belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "user_id": (required, string) BSON id of the user that performed this event
}
```
{% endapi %}

{% api %}

## SMS abort message events

{% apitags %}
Abort, SMS
{% endapitags %}

This event occurs if an SMS message was aborted based on Liquid aborts, quiet hours, etc.

```json
// SMS Abort: users.messages.sms.Abort

{
  "abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
  "abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_name": (optional, string) name of the campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (optional, string) id of the canvas step message variation this user received
  "canvas_step_name": (optional, string) API id of the canvas step this event belongs to,
  "canvas_variation_id": (optional, string) id of the canvas variation this event belongs to,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "external_user_id": (optional, string) External user ID of the user,
  "id": (required, string) globally unique ID of this event,
  "message_variation_id": (optional, string) ID of the message variation this user received,
  "message_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "subscription_group_id": (optional, string) id of the subscription group targeted for this SMS message,
  "time": (required, int) unix timestamp at which the event happened,
  "user_id": (required, string) BSON id of the user that performed this event
}
```
{% endapi %}

{% api %}

## Webhook abort message events

{% apitags %}
Abort,  Webhooks
{% endapitags %}

This event occurs if a webhook message was aborted based on Liquid aborts, quiet hours, etc.

```json
// Webhook Abort: users.messages.webhook.Abort

{
  "abort_log": (optional, string) log message describing abort details (MAX: 128 CHARS),
  "abort_type": (optional, string) type of abort, e.g.: "liquid_abort_message", "quiet_hours", etc.,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "campaign_id": (optional, string) internal-use Braze ID of the campaign this event belongs to,
  "campaign_name": (optional, string) name of the campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (optional, string) id of the canvas step message variation this user received
  "canvas_step_name": (optional, string) API id of the canvas step this event belongs to,
  "canvas_variation_id": (optional, string) id of the canvas variation this event belongs to,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "device_id": (optional, string) id of the device on which the event occurred,
  "dispatch_id": (optional, string) ID of the dispatch this message belongs to,
  "external_user_id": (optional, string) External user ID of the user,
  "id": (required, string) globally unique ID of this event,
  "message_variation_id": (optional, string) ID of the message variation this user received,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "send_id": (optional, string) message send ID this message belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "user_id": (required, string) BSON id of the user that performed this event
}
```
{% endapi %}


{% api %}

## Canvas exit performed event events

{% apitags %}
Exit, Canvas
{% endapitags %}

This event occurs when a user has exited a Canvas by performing an event.

```json
// Canvas Exit Performed Event: users.canvas.exit.PerformedEvent

{
  "id": (required, string) globally unique ID of this event,
  "user_id": (required, string) Braze user id of the user, 
  "external_user_id": (optional, string) External user ID of the user,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "app_group_api_id": (optional, string) API ID of the app group this user belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "canvas_id": (required, string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (required, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_api_id": (optional, string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (optional, string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (optional, string) API id of the canvas step this event belongs to
}
```
{% endapi %}

{% api %}

## Canvas exit matched audience events

{% apitags %}
Exit, Canvas
{% endapitags %}

This event occurs when a user has exited a Canvas by matching an audience.

```json
// Canvas Exit Matched Audience: users.canvas.exit.MatchedAudience

{
  "id": (required, string) globally unique ID of this event,
  "user_id": (required, string) Braze user id of the user, 
  "external_user_id": (optional, string) External user ID of the user,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "app_group_api_id": (optional, string) API ID of the app group this user belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "canvas_id": (required, string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_api_id": (optional, string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (optional, string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (optional, string) API id of the canvas step this event belongs to
}
```
{% endapi %}
{% api %}
## Experiment split entry events

{% apitags %}
Experiment Step, Canvas
{% endapitags %}

This event occurs when a user enters a Canvas experiment step path.

```json
// Experiment Step Split Path Entry: users.canvas.experimentstep.SplitEntry

{
  "id": (required, string) globally unique ID of this event,
  "user_id": (required, string) Braze user id of the user, 
  "external_user_id": (optional, string) External user ID of the user,
  "time": (required, int) unix timestamp at which the event happened,
  "canvas_id": (required, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "experiment_step_id": (required, string) BSON ID of the experiment step this event belongs to,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "experiment_split_id": (required, string) BSON ID of the experiment split the user enrolled in,
  "experiment_split_name": (optional, string) name of the experiment split the user enrolled in,
  "in_control_group": (required, boolean) whether the user was enrolled in the control group
}
```
{% endapi %}

{% api %}

## Experiment conversion events

{% apitags %}
Experiment Step, Canvas
{% endapitags %}

This event occurs when a user convert for a Canvas experiment step.

```json
// Experiment Step Conversion: users.canvas.experimentstep.Conversion

{
  "id": (required, string) globally unique ID of this event,
  "user_id": (required, string) Braze user id of the user, 
  "external_user_id": (optional, string) External user ID of the user,
  "app_id": (optional, string) BSON id of the app this user belongs to,
  "time": (required, int) unix timestamp at which the event happened,
  "canvas_id": (required, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "experiment_step_id": (optional, string) BSON ID of the experiment step this event belongs to,
  "experiment_split_id": (required, string) BSON ID of the experiment split variation this user received,
  "experiment_split_name": (optional, string) name of the experiment split the user enrolled in,
  "conversion_behavior_index": (optional, int) index of the conversion behavior,
  "conversion_behavior": (optional, string) conversion behavior
}
```
{% endapi %}
{% api %}

## Push send events

{% apitags %}
Push, Sends
{% endapitags %}

This event occurs when Braze processes a push message for a user, communicating this to Apple Push Notification Service or Fire Cloud Messaging. This does not mean the push was delivered to the device, just that a message was sent.

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,  
  "platform": (required, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,  
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) id of the device that we made a delivery attempt to,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device,
  "message_extras": (optional, object) key-value pairs sent with this event
}
```

#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google ADID through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.
{% endapi %}
{% api %}

## Push open events

{% apitags %}
Push, Opens
{% endapitags %}

This event occurs when a user directly clicks on the Push notification to open the application. Currently, Push Open Events refer specifically to "Direct Opens" rather than "Total Opens". This does not include statistics shown at the campaign level of "influenced opens" as these are not attributed at the user level.

```json
// Push Notification Open: users.messages.pushnotification.Open
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "app_id": (required, string) id for the app on which the user action occurred,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (optional, string) API id of the Canvas step message variation this user received,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) id of the device that we made a delivery attempt to,
  "button_action_type": (optional, string) Action type of the push notification,
  button. One of [URI, DEEP_LINK, NONE, CLOSE, SHARE]. null if not
  from a button click,
  "button_string": (optional, string) identifier (button_string) of the push notification button clicked. null if not from a button click,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google ADID through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}
{% api %}

## Push notifications in the iOS foreground events

{% apitags %}
Push, iOS, Sends
{% endapitags %}

Please note, this event is not supported by our [Swift SDK](https://github.com/braze-inc/braze-swift-sdk).

This event is now deprecated using our [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk).

```json
// Push Notification iOS Foreground: users.messages.pushnotification.IosForeground
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) id of the device that we made a delivery attempt to,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google ADID through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}
{% api %}

## Push notifications bounce

{% apitags %}
Push, Sends, Bounce
{% endapitags %}

This event occurs when an error is received from either Apple Push Notification Service or Fire Cloud Messaging. This means that the push message was bounced, and therefore not delivered to the user's device.

```json
// Push Notification Bounce: users.messages.pushnotification.Bounce
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (requried, string) id for the app on which the bounce occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "device_id": (optional, string) id of the device that we made a delivery attempt to,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}
{% api %}

## Email send events

{% apitags %}
Email, Sends
{% endapitags %}

This event occurs when an email send request was successfully communicated between Braze and SendGrid. Though, this does not mean the email was received in the end user's inbox.

```json
// Email Send: users.messages.email.Send
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "ip_pool": (optional, string) IP pool used for message sending, 
  "message_extras": (optional, object) key-value pairs sent with this event
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.
{% endapi %}


{% api %}

## Email delivery events

{% apitags %}
Email, Delivery
{% endapitags %}

This event occurs when an email sent made it successfully to the end-users inbox.

```json
// Email Delivery: users.messages.email.Delivery
{
  "id": (requried, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,  
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "sending_ip": (optional, string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (optional, string) IP pool used for message sending,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Email open events

{% apitags %}
Email, Opens
{% endapitags %}

This event occurs when a user opens an email. Multiple events may be generated for the same campaign if a user opens the email multiple times.

```json
// Email Open: users.messages.email.Open
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (requied, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),  
  "user_agent": (optional, string) description of the user's system and browser for the event,
  "ip_pool": (optional, string) IP pool used for message sending,
  "machine_open": (optional, string) Indicator of whether the email was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (e.g., "Apple" or "Google" to indicate which process made the fetch) may be added in the future.,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email,
  "is_amp": (optional, boolean) indicates that this is an AMP event
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Email clicks events

{% apitags %}
Email, Clicks
{% endapitags %}

This event occurs when a user clicks an email. Multiple events may be generated for the same campaign if a user clicks multiple times or clicks different links within the email.

```json
// Email Click: users.messages.email.Click
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Only included when campaign_id is present. Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "url": (optional, string) the URL that was clicked,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "user_agent": (optional, string) description of the user's system and browser for the event,
  "ip_pool": (optional, string) IP pool used for message sending,
  "link_id": (optional, string) unique value generated by Braze for the URL - null unless link aliasing is enabled,
  "link_alias": (optional, string) alias name set when the message was sent - null unless link aliasing is enabled,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email,
  "is_amp": (optional, boolean) indicates that this is an AMP event
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Email bounce event

{% apitags %}
Email, Bounce
{% endapitags %}

This event occurs when an Internet Service Provider returns a hard bounce. A hard bounce signifies a permanent deliverability failure.

```json
// Email Bounce: users.messages.email.Bounce
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "sending_ip": (optional, string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (optional, string) IP pool used for message sending (for certain bounce cases, IP pool will not be provided) ,
  "bounce_reason": (optional, string) reason for bounce provided by server,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email,
  "is_drop": (optional, boolean) indicates that this event counts as a drop event
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Email soft bounce event

{% apitags %}
Email, Bounce
{% endapitags %}

This event occurs when an Internet Service Provider returns a soft bounce. A soft bounce signifies that an email could not be delivered because of a temporary deliverability failure.

```json
// Email Soft Bounce: users.messages.email.SoftBounce
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "sending_ip": (optional, string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (optional, string) IP pool used for message sending(for certain bounce cases, IP pool will not be provided),
  "bounce_reason": (optional, string) reason for bounce provided by server,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Email spam events

{% apitags %}
Email, Spam
{% endapitags %}

This event occurs when the end-user hits the "spam" button on the email. Note that this does not represent the fact the email went into the spam folder as Braze does not track this.

```json
// Email Mark As Spam: users.messages.email.MarkAsSpam
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "user_agent": (optional, string) This field is no longer used in any destination for this event and will always be empty,
  "ip_pool": (optional, string) IP pool used for message sending,
  "esp": (optional, string) ESP related to the event (SparkPost or SendGrid),
  "from_domain": (optional, string) sending domain for the email
}
```
#### Property details

The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}


{% api %}

## Email unsubscribe events

{% apitags %}
Email, Subscription
{% endapitags %}

This event occurs when the end-user has clicked "unsubscribe" from the email.

{% alert important %}
The `Unsubscribe` event is actually a specialized click event that is fired when your user clicks on the unsubscribe link in the email (either a normal unsubscribe link within the email body or footer, or using the [list-unsubscribe header]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), not when the user changes state to unsubscribed. If subscription state change is sent through the API, it will not trigger an event on Currents.
{% endalert %}

```json
// Email Unsubscribe: users.messages.email.Unsubscribe
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "email_address": (required, string) email address for this event,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "ip_pool": (optional, string) IP pool used for message sending
}
```
#### Property details

The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## In-app message impression events

{% apitags %}
In-App Messages, Impressions
{% endapitags %}

This event occurs when a user views an in-app message.

```json
// In-App Message Impression: users.messages.inappmessage.Impression
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "app_id": (required, string) id for the app on which the user action occurred,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "card_id": (optional, string) id of the card that was viewed,  
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "device_id": (optional, string) id of the device on which the event occurred,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google ADID through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}

{% api %}

## In-app message click events

{% apitags %}
In-App Messages, Clicks
{% endapitags %}

This event occurs when a user clicks on an in-app message.

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "card_id": (optional, string) id of the card that was viewed,  
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "button_id": (optional, string) index of the button clicked if it was a button that was clicked, tracking ID of the click if the event came from an appboyBridge.logClick invocation, or choice_id if the in app-message type is a simple survey,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "device_id": (optional, string) id of the device on which the event occurred,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google ADID through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}


{% api %}

## Webhook send events

{% apitags %}
Webhooks, Sends
{% endapitags %}

This event occurs when a webhook was processed and sent to the third party specified in that webhook. Note that this does not signify whether or not the request was received.

```json
// Webhook Send: users.messages.webhook.Send
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
  "message_extras": (optional, object) key-value pairs sent with this event
}
```
#### Property details

- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.

{% endapi %}

{% api %}
## Content Card send events

{% apitags %}
Content Cards, Sends
{% endapitags %}

This event occurs when a Content Card gets sent to a user.

```json
// Content Card Send: users.messages.contentcard.Send
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) id of the content card that was sent,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) id of the device on which the event occurred,
  "message_extras": (optional, object) key-value pairs sent with this event
}
```
#### Property details

- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.
{% endapi %}

{% api %}
## Content Card impression events

{% apitags %}
Content Cards, Impressions
{% endapitags %}

This event occurs when a user views a Content Card.

```json
// Content Card Impression: users.messages.contentcard.Impression
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) id of the content card that was viewed/clicked/dismissed,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) id for the app on which the user action occurred,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) id of the device on which the event occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google adid through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}

{% api %}
## Content Card click events

{% apitags %}
Content Cards, Clicks
{% endapitags %}

This event occurs when a user clicks a Content Card.

```json
// Content Card Click: users.messages.contentcard.Click
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) id of the content card that was viewed/clicked/dismissed,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) id for the app on which the user action occurred,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) id of the device on which the event occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}


{% api %}
## Content Card dismissal events

{% apitags %}
Content Cards, Dismissal
{% endapitags %}

This event occurs when a user dismisses a Content Card.

```json
// Content Card Dismiss: users.messages.contentcard.Dismiss
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "content_card_id": (required, string) id of the content card that was viewed/clicked/dismissed,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) id for the app on which the user action occurred,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,  
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "device_id": (optional, string) id of the device on which the event occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}

{% api %}

## News Feed impression event

{% alert note %}
News Feed is being deprecated. Braze recommends that customers who use our News Feed tool move over to our Content Cards messaging channel—it's more flexible, customizable, and reliable. Check out the [migration guide]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) for more.
{% endalert %}

{% apitags %}
News Feed, Impressions
{% endapitags %}

This event occurs when a user views the News Feed.

{% alert tip %}
The [News Feed Impression]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event) schema (`users.behaviors.app.NewsFeedImpression`) is located in the Customer Behavior Events glossary, as this data is not categorized as a Message Engagement Event. 
{% endalert %}

```json
// News Feed Card Impression: users.messages.newsfeedcard.Impression
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "card_id": (required, string) id of the card that was viewed,  
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred
}
```
{% endapi %}


{% api %}

## News Feed click events

{% apitags %}
News Feed, Clicks
{% endapitags %}

This event occurs when a user clicks the News Feed.

{% alert tip %}
The [News Feed Impression]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event) schema (`users.behaviors.app.NewsFeedImpression`) is located in the Customer Behavior Events glossary, as this data is not categorized as a Message Engagement Event. 
{% endalert %}

```json
// News Feed Card Click: users.messages.newsfeedcard.Click
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,  
  "timezone": (optional, string) IANA time zone of the user at the time of the event,  
  "card_id": (optional, string) id of the card that was clicked,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred
}
```
{% endapi %}

{% api %}

## SMS click events

{% apitags %}
SMS, Clicks
{% endapitags %}

This event occurs when a user clicks an SMS short link.

```json
// SMS Send: users.messages.sms.ShortLinkClick
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user ID of the user targeted by short_url,
  "external_user_id": (optional, string) External ID of the user, null if short_url,
  "app_group_id": (required, string) API ID of the app group associated with the inbound phone number,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA timezone of the user at the time of the event, null if short_url did not use user click tracking,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign if from a campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas if from a Canvas,
  "canvas_variation_id": (optional, string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation a user is in if from a Canvas,
  "url": (required, string) original URL contained in message that was shortened for click tracking,
  "short_url": (required, string) shortened URL that is sent to user for click tracking,
  "user_agent": (optional, string) User-Agent header of the device performing the click event,
  "user_phone_number": (optional, string) Phone number of the user that short_url was sent to
}
```
{% endapi %}
{% api %}
## SMS send events

{% apitags %}
SMS, Sends
{% endapitags %}

This event occurs when a user sends an SMS.

```json
// SMS Send: users.messages.sms.Send
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) message send ID this message belongs to,
  "category": (optional, string) If the SMS was sent as a result of auto-response to one of your global SMS keywords, the Category will be reflected here (e.g Opt-In, Opt-Out, Help)
  "message_extras": (optional, object) key-value pairs sent with this event
}
```
#### Property details
- `message_extras` allow you to annotate your send events with dynamic data from Connected Content, custom attributes (such as language, country), and Canvas entry properties. Refer to [Message extras]({{site.baseurl}}/message_extras_tag/) to learn more.

{% endapi %}

{% api %}

## SMS sends to carrier events

{% apitags %}
SMS, Delivery
{% endapitags %}

This event occurs when an SMS is sent to the carrier.

```json
// SMS Delivery: users.messages.sms.CarrierSend
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) id of the subscription group targeted for this SMS message,
  "from_phone_number": (optional, string) the from phone number of the message (Delivered and Undelivered only),
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) message send ID this message belongs to
}
```
{% endapi %}

{% api %}

## SMS delivery events

{% apitags %}
SMS, Delivery
{% endapitags %}

This event occurs when an SMS was successfully delivered to the users mobile phone.

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) id of the subscription group targeted for this SMS message,
  "from_phone_number": (optional, string) the from phone number of the message (Delivered and Undelivered only),
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) message send ID this message belongs to
}
```
{% endapi %}

{% api %}

## SMS rejection events

{% apitags %}
SMS, Rejection
{% endapitags %}

This event occurs when an SMS send gets rejected by the carrier, this can happen for several reasons. Use this event and the provided error codes to help troubleshoot issues with SMS delivery.

```json
// SMS Rejection: users.messages.sms.Rejection
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) id of the subscription group targeted for this SMS message,
  "from_phone_number": (optional, string) the from phone number of the message (Delivered and Undelivered only),
  "error": (optional, string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (optional, string) the provider's reason code as to why the message was not sent (Rejection and Delivery Failure events only),
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```
{% endapi %}


{% api %}

## SMS delivery failure events

{% apitags %}
SMS, Delivery
{% endapitags %}

This event occurs when an SMS experiences delivery failure. Use this event and the provided error codes to help troubleshoot issues with SMS delivery.

```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "dispatch_id": (optional, string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,  
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "to_phone_number": (optional, string) the number the message was sent to,
  "subscription_group_id": (optional, string) id of the subscription group targeted for this SMS message,
  "error": (optional, string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (optional, string) the provider's reason code as to why the message was not sent (Rejection and Delivery Failure events only),
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) message send ID this message belongs to
}
```
{% endapi %}
{% api %}

## SMS inbound received events

{% apitags %}
SMS, InboundReceived
{% endapitags %}

This event occurs when one of your users sends an SMS to a phone number in one of your Braze SMS subscription groups. 

When Braze receives an inbound SMS, we attribute that inbound message to any user that shares that phone number. As a result, you may receive multiple events per inbound message if multiple users in your Braze instance share the same phone number. If you require attribution of specific user IDs based on previous messages sent to that user, you can use the SMS Delivered event to attribute Inbound Received events to the user ID who most recently received a message from your Braze number.

If we detect that this inbound message is a reply to an outbound campaign or Canvas component sent from Braze, we will also include the campaign or Canvas metadata with the event. Braze defines a reply as an inbound message coming within four hours of an outbound message. However, there is a one-minute cache for the attributed campaign information of the last outbound SMS received.

```json
// SMS Inbound Received: users.messages.sms.InboundReceive
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_group_id": (required, string) API ID of the app group associated with the inbound phone number,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "user_phone_number": (required, string) the phone number of the user who sent the message to your Braze number,
  "subscription_group_id": (optional, string) id of the subscription group which the phone number the user messaged belongs to,
  "inbound_phone_number": (required, string) the phone number the message was sent to,
  "inbound_media_urls": (optional, string) the URLs of inbound media attachments if received, 
  "action": (required, string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),
  "message_body": (required, string) the body of the message sent by the user,
  "message_urls": (optional, array of string) the message URLs sent by the user,
  "campaign_id": (optional, string) id of the campaign if Braze identifies this inbound message is a reply to a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "message_variation_name": (optional, string) the name of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas
}
```
{% endapi %}


{% api %}

## Campaign conversion events

{% apitags %}
Campaign, Conversion
{% endapitags %}

This event occurs when a user does an action that has been set as a conversion event in a campaign.

{% alert important %}
Note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_behavior_index` field represents which conversion event. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Campaign Conversion Event: users.campaigns.Conversion
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (required, string) id of the campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (required, string) id of the message variation,
  "message_variation_name": (optional, string) the name of the message variation,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
  "conversion_behavior_index": (optional, int) index of the conversion behavior,
  "conversion_behavior": (optional, string) JSON-encoded string describing the conversion behavior
}
```
{% endapi %}


{% api %}

## Canvas conversion events

{% apitags %}
Canvas, Conversion
{% endapitags %}

This event occurs when a user does an action that has been set as a conversion event in Canvas.

{% alert important %}
Note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_behavior_index` field represents which conversion event. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Canvas Conversion Event: users.canvas.Conversion
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "canvas_id": (required, string) id of the Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (required, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (required, string) id of the last step the user was sent before the conversion
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas
  "conversion_behavior_index": (optional, int) index of the conversion behavior,
  "conversion_behavior": (optional, string) JSON-encoded string describing the conversion behavior
}
```
{% endapi %}


{% api %}

## Canvas entry events

{% apitags %}
Canvas, Entry
{% endapitags %}

This event occurs when a user enters into the Canvas. This event tells you which variant the user entered into.

```json
// Canvas Entry Event: users.canvas.Entry
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "canvas_id": (required, string) id of the Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (required, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step the user entered into,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "in_control_group": (required, boolean) whether the user was enrolled in the control group for a Canvas
}
```

{% endapi %}

{% api %}
## Campaign control group enrollment events

{% apitags %}
Campaign, Entry
{% endapitags %}

This event occurs when a user is enrolled in a control variant set on a multi-variant campaign. This event is generated as there will be no channel send event for this user.

```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "campaign_id": (optional, string) id of the campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation,
  "message_variation_name": (optional, string) the name of the message variation,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

{% endapi %}

{% api %}

## Subscription events

{% apitags %}
Subscription
{% endapitags %}

This event occurs when the subscription state of a user in a subscription group changes.

{% alert important %}
Subscription groups are only available for email and SMS channels at this time.
{% endalert %}

```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "email_address": (optional, string) email address for this user,
  "phone_number": (optional, string) phone number of the user (presented in e.164 format),
  "app_id": (optional, string) id for the app on which the user action occurred,
  "campaign_id": (optional, string) id of the campaign if from a campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "message_variation_name": (optional, string) the name of the message variation if from a campaign,
  "canvas_id": (optional, string) id of the Canvas if from a canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the step for this message if from a Canvas,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "subscription_group_id": (required, string) id of the subscription group,
  "subscription_status": (required, string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed',
  "channel": (optional, string) either 'sms', 'email', or 'whats_app',
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "send_id": (optional, string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "state_change_source": (optional, string) Source of the state change, e.g: REST, SDK, Dashboard, Preference Center etc.
}
```

#### Property details

`state_change_source` will return a one or two-letter string depending on the source. Available sources and associated strings are listed below:

| Source | Letter |
| --- | --- |
| SDK | s |
| Dashboard | d |
| Subscription page | p |
| REST API | r |
| Attribution provider | a |
| CSV import | c |
| Enhanced preference center | e |
| Inbound SMS | i |
| Outbound SMS | o |
| Migration | m |
| User merge | g |
| Backfill | b |
| Shopify provider | sh |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}

{% api %}

## Global state change events

{% apitags %}
Subscription
{% endapitags %}

This event occurs when the global subscription state of the user changes.

```json
// Global State Change: users.behaviors.subscription.GlobalStateChange
{
  "id": (required, string) unique ID of this event,
  "user_id": (required, string) Braze BSON id of the user with this global subscription state change,
  "external_user_id": (optional, string) External ID of the user,
  "email_address": (optional, string) User email address,
  "state_change_source": (optional, string) Source of the state change, e.g: REST, SDK, Dashboard, Preference Center etc.,
  "subscription_status": (required, string) Global subscription status: Subscribed, Unsubscribed and Opt-In,
  "channel": (optional, string) Channel: only email for now,
  "time": (required, string) 10-digit UTC time of the state change event in seconds since the epoch,
  "timezone": (optional, string) IANA timezone of the user at the time of the event,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "campaign_id": (optional, string) BSON id of the Campaign if from a Campaign,
  "campaign_name": (optional, string) name of the campaign,
  "message_variation_id": (optional, string) id of the message variation if from a campaign,
  "canvas_id": (optional, string) BSON id of the Canvas if from a Canvas,
  "canvas_name": (optional, string) name of the Canvas,
  "canvas_variation_id": (optional, string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (optional, string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (optional, string) id of the canvas step this event belongs to,
  "canvas_step_name": (optional, string) name of the step for this message if from a Canvas,
  "send_id": (optional, string) Message send id this subscription state change action originated from
}
```

#### Property details

`state_change_source` will return a one or two-letter string depending on the source. Available sources and associated strings are listed below:

| Source | Letter |
| --- | --- |
| SDK | s |
| Dashboard | d |
| Subscription page | p |
| REST API | r |
| Attribution provider | a |
| CSV import | c |
| Enhanced preference center | e |
| Inbound SMS | i |
| Outbound SMS | o |
| Migration | m |
| User merge | g |
| Backfill | b |
| Shopify provider | sh |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
{% api %}
## Uninstall events

{% apitags %}
Uninstall
{% endapitags %}

This event occurs when a user uninstalls an app. Use this data to track when users uninstall an app. While this is currently a message engagement event, this will be changed to a user behavior event in the future.

{% alert important %}
This event is not fired when the user actually uninstalls the app, as that's impossible to track exactly. Braze sends a daily silent push to determine if the app still exists on your user's device, and if we get an error on that silent push, it is assumed the app has been uninstalled.
{% endalert %}

```json
// Uninstall Event: users.behaviors.Uninstall
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "device_id": (optional, string) id of the device on which the session occurred,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch
}
```

{% endapi %}
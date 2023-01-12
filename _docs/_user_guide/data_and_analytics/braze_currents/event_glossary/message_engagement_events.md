---
nav_title: Message Engagement Events
layout: message_engagement_events_glossary
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents

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

## Canvas exit performed event events

{% apitags %}
Exit, Canvas
{% endapitags %}

This event occurs when a user has exited a Canvas by performing an event.

```json
// Canvas Exit Performed Event: users.canvas.exit.PerformedEvent
// Canvas Exit Performed Event Details: users_canvas_exit_PerformedEvent_Details

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) BSON id of the Canvas step this event belongs to,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
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
// Canvas Exit Matched Audience: users_canvas_exit_MatchedAudience
// Canvas Exit Matched Audience Details :users_canvas_exit_MatchedAudience_Details

{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) BSON id of the Canvas step this event belongs to,
  "canvas_api_id": (string) BSON id of the experiment step this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
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
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "experiment_step_id": (string) BSON ID of the experiment step this event belongs to,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "experiment_split_id": (string) BSON ID of the experiment split the user enrolled in,
  "experiment_split_name": (string) name of the experiment split the user enrolled in,
  "in_control_group": (boolean) whether the user was enrolled in the control group
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
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user, 
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "workflow_id": (string) internal-use Braze ID of the workflow this event belongs to,
  "experiment_step_id": (string) BSON ID of the experiment step this event belongs to,
  "experiment_split_id": (string) BSON ID of the experiment split variation this user received,
  "conversion_behavior_index": (int) index of the conversion behavior
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
#### Property details
- For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS IDFA and Android Google ADID through the native SDKs. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- If you are using Kafka to ingest [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) data, reach out to your customer success manager or account manager to enable the feature flipper for sending `ad_id`.
{% endapi %}
{% api %}

## Push open events

{% apitags %}
Push, Opens
{% endapitags %}

This event occurs when a user directly clicks on the Push notification to open the application. Currently, Push Open Events refer specifically to "Direct Opens" rather than "Total Opens". This does not include statistics shown at the campaign level of “influenced opens” as these are not attributed at the user level.

```json
// Push Notification Open: users.messages.pushnotification.Open
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "canvas_step_message_variation_id": (string) API id of the Canvas step message variation this user received,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device that we made a delivery attempt to,
  "button_action_type": (string) Action type of the push notification,
  button. One of [URI, DEEP_LINK, NONE, CLOSE, SHARE]. null if not
  from a button click,
  "button_string": (string) identifier (button_string) of the push notification button clicked. null if not from a button click,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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

This event occurs when an error is received from either Apple Push Notification Service or Fire Cloud Messaging. This means that the push message was bounced, and therefore not delivered to the user’s device.

```json
// Push Notification Bounce: users.messages.pushnotification.Bounce
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the bounce occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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

This event occurs when an email send request was successfully communicated between Braze and Sendgrid. Though, this does not mean the email was received in the end user's inbox.

```json
// Email Send: users.messages.email.Send
{
  // User Specific Properties
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  // Campaign/Canvas Tracking Properties
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  // Event Specific Properties
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending
}
```
#### Property details
- The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (string) IP pool used for message sending,
  "esp": (string) ESP related to the event (Sparkpost or Sendgrid),
  "from_domain": (string) sending domain for the email
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending,
  "user_agent": (string) description of the user’s system and browser for the event,
  "machine_open": (string) Indicator of whether the e-mail was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (e.g., "Apple" or "Google" to indicate which process made the fetch) may be added in the future.,
  "esp": (string) ESP related to the event (Sparkpost or Sendgrid),
  "from_domain": (string) sending domain for the email,
  "is_amp": (boolean) indicates that this is an AMP event
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Only included when campaign_id is present. Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked,
  "ip_pool": (string) IP pool used for message sending,
  "user_agent": (string) description of the user’s system and browser for the event,
  "link_id": (string) unique value generated by Braze for the URL - null unless link aliasing is enabled,
  "link_alias": (string) alias name set when the message was sent - null unless link aliasing is enabled,
  "esp": (string) ESP related to the event (Sparkpost or Sendgrid),
  "from_domain": (string) sending domain for the email,
  "is_amp": (boolean) indicates that this is an AMP event
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (string) IP pool used for message sending (for certain bounce cases, IP pool will not be provided) ,
  "bounce_reason": (string) reason for bounce provided by server,
  "esp": (string) ESP related to the event (Sparkpost or Sendgrid),
  "from_domain": (string) sending domain for the email,
  "is_drop": (boolean) indicates that this event counts as a drop event
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only. Will only be shown on events if the message was actually attempted for delivery. For certain other bounces, the information could be lost if the recipient server has already accepted the mail and only later after the connection is closed decided it could not deliver the mail),
  "ip_pool": (string) IP pool used for message sending(for certain bounce cases, IP pool will not be provided),
  "bounce_reason": (string) reason for bounce provided by server,
  "esp": (string) ESP related to the event (Sparkpost or Sendgrid),
  "from_domain": (string) sending domain for the email
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

This event occurs when the end-user hits the “spam” button on the email. Note that this does not represent the fact the email went into the spam folder as Braze does not track this.

```json
// Email Mark As Spam: users.messages.email.MarkAsSpam
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending,
  "user_agent": (string) This field is no longer used in any destination for this event and will always be empty,
  "esp": (string) ESP related to the event (Sparkpost or Sendgrid),
  "from_domain": (string) sending domain for the email
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

This event occurs when the end-user has clicked “unsubscribe” from the email.

{% alert important %}
The `Unsubscribe` event is actually a specialized click event that is fired when your user clicks on the unsubscribe link in the email (either a normal unsubscribe link within the email body or footer, or using the [list-unsubscribe header]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), not when the user changes state to unsubscribed. If subscription state change is sent through the API, it will not trigger an event on Currents.
{% endalert %}

```json
// Email Unsubscribe: users.messages.email.Unsubscribe
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending
}
```
#### Property details

The behavior for `dispatch_id` differs between Canvas and campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". Learn more about [dispatch ID behavior]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}

## Subscription events

{% apitags %}
Subscription, Email, SMS
{% endapitags %}

This event occurs when the subscription state of a user in a subscription group changes.

{% alert important %}
Subscription groups are only available for email and SMS channels at this time.
{% endalert %}

```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "channel": (string) either 'sms', 'email', or 'whats_app',
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "email_address": (string) email address for this user,
  "phone_number": (string) phone number of the user (presented in e.164 format),
  "subscription_group_id": (string) id of the subscription group,
  "subscription_status": (string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed'
}
```
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "card_id": (string) deprecated,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "button_id": (string) index of the button clicked, if it was a button that was clicked, or tracking ID of the click, if the event came from an appboyBridge.logClick invocation,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "card_id": (string) deprecated,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "content_card_id": (string) id of the content card that was sent,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "device_id": (string) id of the device on which the event occurred
}
```

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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "card_id": (string) id of the card that was viewed,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "card_id": (string) id of the card that was clicked,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user
  "send_id": (string) message send ID this message belongs to,
  "category" : (string) If the SMS was sent as a result of auto-response to one of your global SMS keywords, the Category will be reflected here (e.g Opt-In, Opt-Out, Help) 
}
```
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider’s reason code as to why the message was not sent (Rejection and Delivery Failure events only)
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user,
  "send_id": (string) message send ID this message belongs to,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider’s reason code as to why the message was not sent (Rejection and Delivery Failure events only)
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "app_group_id": (string) API ID of the app group associated with the inbound phone number,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "user_phone_number": (string) the phone number of the user who sent the message to your Braze number,
  "subscription_group_id": (string) id of the subscription group which the phone number the user messaged belongs to,
  "inbound_phone_number": (string) the phone number the message was sent to,
  "inbound_media_urls": (string) the URLs of inbound media attachments if received, 
  "action" : (string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),
  "message_body" : (string) the body of the message sent by the user,
  "campaign_id": (string) id of the campaign if Braze identifies this inbound message is a reply to a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "message_variation_name": (string) the name of the message variation if Braze identifies this inbound message is a reply to a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "message_variation_id": (string) id of the message variation,
  "message_variation_name": (string) the name of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the last step the user was sent before the conversion
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step the user entered into,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "in_control_group": (boolean) whether the user was enrolled in the control group for a Canvas
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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "app_id": (string) id for the app on which the user action occurred,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation,
  "message_variation_name": (string) the name of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

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
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (string) id for the app on which the user action occurred,
  "device_id": (string) id of the device on which the session occurred
}
```

{% endapi %}
---
nav_title: Message Engagement Events
layout: message_engagement_events_glossary

page_order: 5

excerpt_separator: ""
page_type: glossary

description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using our tool, Currents."

tool: currents
---

Please contact your Account Manager or [open a support ticket][support] if you need access to additional event entitlements. If you can't find what you need below, check out our [Customer Behavior Events Library]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of Message Engagement Event Structure %}
<br>
This event breakdown shows what type of information is generally included in a message engagement event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming currents event data to make data-driven reports, charts and take advantage of other valuable data metrics. 

![image]({% image_buster /assets/img/message_engagement_event.png %})

Message engagement events are comprised of __user specific__ properties, __campaign/canvas tracking__ properties and __event specific__ properties. 

{% enddetails %}

{% alert important %}
Please note that these schemas __only apply to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage)__. For schema that apply to the other partners, please check [their respective pages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/integration/available_partners/).<br><br>Additionally, note that Currents will drop events with excessively large payloads of greater than 900KB. 
{% endalert %}

{% api %}

## Push Send Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}
{% api %}

## Push Open Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}
{% api %}

## Push Notifications in the iOS Foreground Events

{% apitags %}
Push, iOS, Sends
{% endapitags %}

This event occurs if a push was sent while the iOS app was in the foreground. Whether the user sees the push when the app is in the foreground, is determined by how your developers have integrated the iOS SDK for foreground push handling detailed [here]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#ios-10). 

```json
// Push Notification iOS Foreground: users.messages.pushnotification.IosForeground
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}
{% api %}

## Push Notifications Bounce

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the bounce occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```
{% endapi %}
{% api %}

## Email Send Events

{% apitags %}
Email, Sends
{% endapitags %}

This event occurs when an email send request was successfully communicated between Braze and Sendgrid. Though, this does not mean the email was received in the end-user’s inbox

```json
// Email Send: users.messages.email.Send
{
  // User Specific Properties
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  // Campaign/Canvas Tracking Properties
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  // Event Specific Properties
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}


{% api %}

## Email Delivery Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only),
  "ip_pool": (string) IP pool used for message sending
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}


{% api %}

## Email Open Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "ip_pool": (string) IP pool used for message sending
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}



{% api %}

## Email Clicks Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the url that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "ip_pool": (string) IP pool used for message sending
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}

{% api %}

## Email Bounces Events

{% apitags %}
Email, Bounce
{% endapitags %}

This event occurs when an Internet Service Provider returns a soft or hard bounce. A soft bounce signifies that an email could not be delivered because of a temporary deliverability failure. A hard bounce signifies a permanent deliverability failure.

```json
// Email Bounce: users.messages.email.Bounce
// Email Soft Bounce: users.messages.email.SoftBounce
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only),
  "ip_pool": (string) IP pool used for message sending,
  "bounce_reason": (string) reason for bounce provided by server,
  "bounce_code": (string) code for bounce provided by server
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}

{% api %}

## Email Spam Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only),
  "ip_pool": (string) IP pool used for message sending
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}


{% api %}

## Email Unsubscribe Events

{% apitags %}
Email, Subscription
{% endapitags %}

This event occurs when the end-user has clicked “unsubscribe” from the email.

{% alert important %}
Please note that the `Unsubscribe` event is actually a specialized click event that is fired when your user _clicks on the unsubscribe link in the email_, __not__ when the user changes state to unsubscribed.
{% endalert %}

```json
// Email Unsubscribe: users.messages.email.Unsubscribe
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "ip_pool": (string) IP pool used for message sending
}
```

{% alert update %}
The behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}

{% api %}

## Subscription Events

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
  "channel": (string) either 'sms' or 'email',
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "email_address": (string) email address for this user,
  "phone_number": (string) phone number of the user (presented in e.164 format),
  "subscription_group_id": (string) id of the subscription group,
  "subscription_status": (string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed'
}
```
{% endapi %}


{% api %}

## In-App Message Impression Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "card_id": (string) API ID of the card this in app message comes from,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}


{% api %}

## In-App Message Click Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "button_id": (string) index of the button clicked, if it was a button that was clicked,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "card_id": (string) API ID of the card this in app message comes from,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}


{% api %}

## Webhook Send Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
}
```
{% endapi %}

{% api %}
## Content Card Send Events

{% apitags %}
Content Cards, Sends
{% endapitags %}

This event occurs when a content card gets sent to a user. 

```json
// Content Card Send: users.messages.contentcard.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "content_card_id": (string) id of the content card that was sent,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}

{% api %}
## Content Card Impression Events

{% apitags %}
Content Cards, Impressions
{% endapitags %}

This event occurs when a user views a content card.

```json
// Content Card Impression: users.messages.contentcard.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}

{% api %}
## Content Card Click Events

{% apitags %}
Content Cards, Clicks
{% endapitags %}

This event occurs when a user clicks a content card.

```json
// Content Card Click: users.messages.contentcard.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}


{% api %}
## Content Card Dismissal Events

{% apitags %}
Content Cards, Dismissal
{% endapitags %}

This event occurs when a user dismisses a content card.

```json
// Content Card Dismiss: users.messages.contentcard.Dismiss
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "ad_id": (string) advertising identifier,
  "ad_id_type": (string) One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (boolean) whether advertising tracking is enabled for the device
}
```

{% alert update %}
For `ad_id`, `ad_id_type` and `ad_tracking_enabled`, you will need to explicitly collect the iOS idfa and Android Google adid through the native sdks. Learn more about them here: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).

_Update noted in June 2020._
{% endalert %}

{% endapi %}

{% api %}

## News Feed Impression Event

{% apitags %}
News Feed, Impressions
{% endapitags %}

This event occurs when a user views the News Feed.

{% alert tip %}
  The [News Feed Impression schema (`users.behaviors.app.NewsFeedImpression`) is located in Customer Behavior Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event), as this data is categorized as such, opposed to being categorized as a Message Engagement Event.
{% endalert %}

```json
// News Feed Card Impression: users.messages.newsfeedcard.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "card_id": (string) id of the card that was viewed,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```
{% endapi %}


{% api %}

## News Feed Click Events

{% apitags %}
News Feed, Clicks
{% endapitags %}

This event occurs when a user clicks the News Feed.

{% alert tip %}
  The [News Feed Impression schema (`users.behaviors.app.NewsFeedImpression`) is located in Customer Behavior Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event), as this data is categorized as such, opposed to being categorized as a Message Engagement Event.
{% endalert %}

```json
// News Feed Card Click: users.messages.newsfeedcard.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "card_id": (string) id of the card that was clicked,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```
{% endapi %}

{% api %}

## SMS Send Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user
}
```
{% endapi %}

{% api %}

## SMS Sends to Carrier Events

{% apitags %}
SMS, Delivery
{% endapitags %}

This event occurs when an SMS is sent to the carrier. 

```json
// SMS Delivery: users.messages.sms.SendToCarrier
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user
}
```
{% endapi %}

{% api %}

## SMS Delivery Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user
}
```
{% endapi %}

{% api %}

## SMS Rejection Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider’s reason code as to why the message was not sent (Rejection and Delivery Failure events only)
}
```
{% endapi %}


{% api %}

## SMS Delivery Failure Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
  "subscription_group_id": (string) id of the subscription group targeted for this SMS message,
  "subscription_group_api_id": (string) api id of the subscription group targeted for this SMS message,
  "to_phone_number": (string) the number the message was sent to,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider’s reason code as to why the message was not sent (Rejection and Delivery Failure events only)
}
```
{% endapi %}
{% api %}

## SMS Inbound Received Events

{% apitags %}
SMS, InboundReceived
{% endapitags %}

This event occurs when one of your users sends an SMS to a phone number in one of your Braze SMS subscription groups. Note when Braze receives an Inbound SMS, we attribute that inbound message to any user that shares that phone number. As a result, you may receive multiple events per inbound message if multiple users in your Braze instance share the same phone number. If you require attribution of specific user IDs based on previous messages sent to that user, you can use the SMS Delivered event to attribute Inbound Received events to the user ID who most recently received a message from your Braze number.

```json
// SMS Inbound Received: users.messages.sms.InboundReceived
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "user_phone_number": (string) the phone number of the user who sent the message to your Braze number,
  "subscription_group_id": (string) id of the subscription group which the phone number the user messaged belongs to,
  "inbound_phone_number": (string) the phone number the message was sent to,
  "action" : (string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),  
  "message_body" : (string) the body of the message sent by the user
}
```
{% endapi %}


{% api %}

## Campaign Conversion Events

{% apitags %}
Campaign, Conversion
{% endapitags %}

This event occurs when a user does an action that has been set as a conversion event in a campaign. 

{% alert important %}
Please note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_index` field represents which conversion event. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Campaign Conversion Event: users.campaigns.Conversion
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
}
```
{% endapi %}


{% api %}

## Canvas Conversion Events

{% apitags %}
Canvas, Conversion
{% endapitags %}

This event occurs when a user does an action that has been set as a conversion event in canvas.

{% alert important %}
Please note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_index` field represents which conversion event. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Canvas Conversion Event: users.canvas.Conversion
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "canvas_id": (string) id of the canvas,
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

## Canvas Entry Events

{% apitags %}
Canvas, Entry
{% endapitags %}

This event occurs when a user enters into the canvas. This event tells you which variant the user entered into. 

```json
// Canvas Entry Event: users.canvas.Entry
{
  "id": (string) unique id of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_name": (string) will always return 'null' for this engagement event, 
  "canvas_step_id": (string) id of the step the user entered into,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "in_control_group": (boolean) whether the user was enrolled in the control group for a Canvas
}
```

{% endapi %}

{% api %}
## Campaign Control Group Enrollment Events

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
  "time": (int) UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
}
```

{% endapi %}

[support]: {{site.baseurl}}/support_contact/

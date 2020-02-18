---
nav_title: Message Engagement Events
layout: message_engagement_events_glossary

page_order: 5

excerpt_separator: ""
page_type: glossary

description: "This glossary lists the various Message Engagement Events that Braze can track and send to chosen Data Warehouses using our tool, Currents."

tool: currents
---

Please contact your Account Manager or [open a support ticket][support] if you need access to additional event entitlements.

{% alert important %}
Please note that these schemas __only apply to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage)__. For schema that apply to the other partners, please check [their respective pages]({{ site.baseurl }}/user_guide/data_and_analytics/braze_currents/integration/available_partners/).
{% endalert %}

{% api %}

## Push Send Events

{% apitags %}
Push, Engagement, Sends
{% endapitags %}

Data accumulates when a user engages with a Push Notification, or as a Push Notification moves through the message pipeline. Use this data to track all events related to push engagement and message pipeline.

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.
}
```
{% endapi %}
{% api %}

## Push Open Events

{% apitags %}
Push, Engagement, Opens
{% endapitags %}

Data accumulates when a user engages with a Push Notification, or as a Push Notification moves through the message pipeline. Use this data to track all events related to push engagement and message pipeline. Currently, Push Open Events refer specifically to "Direct Opens" rather than "Total Opens".

```json
// Push Notification Open: users.messages.pushnotification.Open
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.
}
```
{% endapi %}
{% api %}

## Push Notifications in the iOS Foreground Events

{% apitags %}
Push, Engagement, iOS, Sends
{% endapitags %}

Data accumulates when a user engages with a Push Notification, or as a Push Notification moves through the message pipeline. Use this data to track all events related to push engagement and message pipeline.

```json
// Push Notification iOS Foreground: users.messages.pushnotification.IosForeground
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.
}
```
{% endapi %}
{% api %}

## Push Notifications Bounce

{% apitags %}
Push, Engagement, iOS, Sends, Bounce
{% endapitags %}

Data accumulates when a user engages with a Push Notification, or as a Push Notification moves through the message pipeline. Use this data to track all events related to push engagement and message pipeline.

```json
// Push Notification Bounce: users.messages.pushnotification.Bounce
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the bounce occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "device_id": (string) id of the device that we made a delivery attempt to,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.
}
```
{% endapi %}
{% api %}

## Email Send Events

{% apitags %}
Email, Engagement, Sends
{% endapitags %}

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

```json
// Email Send: users.messages.email.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}


{% api %}

## Email Delivery Events

{% apitags %}
Email, Engagement, Delivery
{% endapitags %}

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

```json
// Email Delivery: users.messages.email.Delivery
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only),
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}


{% api %}

## Email Open Events

{% apitags %}
Email, Engagement, Opens
{% endapitags %}

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

```json
// Email Open: users.messages.email.Open
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only)
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}



{% api %}

## Email Clicks Events

{% apitags %}
Email, Engagement, Clicks
{% endapitags %}

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the url that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only)
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}

{% api %}

## Email Bounces Events

{% apitags %}
Email, Engagement, Bounces
{% endapitags %}

This event accounts for both Bounces and Soft Bounces.

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

```json
// Email Bounce: users.messages.email.Bounce
// Email Soft Bounce: users.messages.email.SoftBounce
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "sending_ip": (string) the IP address from which the message was sent (Email Delivery, Bounce, and SoftBounce events only),
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}

{% api %}

## Email Spam Events

{% apitags %}
Email, Engagement, Spam
{% endapitags %}

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

```json
// Email Mark As Spam: users.messages.email.MarkAsSpam
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and MarkAsSpam events only)
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}


{% api %}

## Email Unsubscribe Events

{% apitags %}
Email, Engagement, Subscription
{% endapitags %}

Data accumulates when a user engages with an email, or as an email moves through the message pipeline. You can use this data to track all events related to email message engagement and message pipeline.

{% alert important %}
Please note that the `Unsubscribe` event is actually a specialized click event that is fired when your user _clicks on the unsubscribe link in the email_, __not__ when the user changes state to unsubscribed.
{% endalert %}

```json
// Email Unsubscribe: users.messages.email.Unsubscribe
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
}
```

{% alert update %}
Behavior for `dispatch_id` differs between Canvas and Campaigns because Braze treats Canvas steps (except for Entry Steps, which can be scheduled) as triggered events, even when they are "scheduled". [Learn more about `dispatch_id` behavior in Canvas and Campaigns here]({{ site.baseurl }}/help/help_articles/data/dispatch_id/).

_Update noted in August 2019._
{% endalert %}

{% endapi %}

{% api %}

## Subscription Events

{% apitags %}
Subscription, Engagement
{% endapitags %}

Data accumulates when a user's performs a subscription event. You can use this data to track all events related to a user's subscription.

{% alert important %}
Subscription groups are only available for email and SMS channels at this time.
{% endalert %}

```json
// Subscription Group State Change: users.behaviors.subscriptiongroup.StateChange
// Note that subscription groups are only available for email at this time.
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "channel": (string) either 'sms' or 'email',
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
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
In-App Messages, Engagement, Impressions
{% endapitags %}

Data accumulates when a user engages with in-app messages in any of the ways defined below. You can use this data to track all events related to in-app message engagement.

```json
// In-App Message Impression: users.messages.inappmessage.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "card_id": (string) API ID of the card this in app message comes from,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}


{% api %}

## In-App Message Click Events

{% apitags %}
In-App Messages, Engagement, Clicks
{% endapitags %}

Data accumulates when a user engages with in-app messages in any of the ways defined below. You can use this data to track all events related to in-app message engagement.

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "button_id": (string) index of the button clicked, if it was a button that was clicked,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "card_id": (string) API ID of the card this in app message comes from,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}


{% api %}

## Webhook Send Events

{% apitags %}
Webhooks, Engagement, Sends
{% endapitags %}

Data accumulates when a Webhook is sent. Use this data to track when webhooks are sent.

```json
// Webhook Send: users.messages.webhook.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
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
{% endapi %}

{% api %}
## Content Card Send Events

{% apitags %}
Content Cards, Engagement, Sends
{% endapitags %}

Data accumulates when a user engages with Content Cards. Use this data to track all events related to Content Card engagement.

```json
// Content Card Send: users.messages.contentcard.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "content_card_id": (string) id of the content card that was sent,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions),
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}

{% api %}
## Content Card Impression Events

{% apitags %}
Content Cards, Engagement, Impressions
{% endapitags %}

Data accumulates when a user engages with Content Cards. Use this data to track all events related to Content Card engagement.

```json
// Content Card Impression: users.messages.contentcard.Impression
// Content Card Click: users.messages.contentcard.Click
// Content Card Dismiss: users.messages.contentcard.Dismiss
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
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
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}

{% api %}
## Content Card Click Events

{% apitags %}
Content Cards, Engagement, Clicks
{% endapitags %}

Data accumulates when a user engages with Content Cards. Use this data to track all events related to Content Card engagement.

```json
// Content Card Click: users.messages.contentcard.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
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
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}


{% api %}
## Content Card Dismissal Events

{% apitags %}
Content Cards, Engagement, Dismissals
{% endapitags %}

Data accumulates when a user engages with Content Cards. Use this data to track all events related to Content Card engagement.

```json
// Content Card Dismiss: users.messages.contentcard.Dismiss
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "content_card_id": (string) id of the content card that was viewed/clicked/dismissed,
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
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}

{% api %}

## News Feed Impression Event

{% apitags %}
News Feed, Engagement, Impressions
{% endapitags %}

Data accumulates when a user engages with the News Feed. Use this data to track all events related to News Feed engagement.

{% alert tip %}
  The [News Feed Impression schema (`users.behaviors.app.NewsFeedImpression`) is located in Customer Behavior Events]({{ site.baseurl }}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event), as this data is categorized as such, opposed to being categorized as a Message Engagement Event.
{% endalert %}

```json
// News Feed Card Impression: users.messages.newsfeedcard.Impression
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
News Feed, Engagement, Clicks
{% endapitags %}

Data accumulates when a user engages with the News Feed. Use this data to track all events related to News Feed engagement.

{% alert tip %}
  The [News Feed Impression schema (`users.behaviors.app.NewsFeedImpression`) is located in Customer Behavior Events]({{ site.baseurl }}/user_guide/data_and_analytics/braze_currents/customer_behavior_events/#news-feed-impression-event), as this data is categorized as such, opposed to being categorized as a Message Engagement Event.
{% endalert %}

```json
// News Feed Card Click: users.messages.newsfeedcard.Click
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
SMS, Engagement, Sends
{% endapitags %}

```json
// SMS Send: users.messages.sms.Send
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user
}
```
{% endapi %}

{% api %}

## SMS Sends to Carrier Events

{% apitags %}
SMS, Engagement, Delivery
{% endapitags %}

```json
// SMS Delivery: users.messages.sms.SendToCarrier
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user
}
```
{% endapi %}

{% api %}

## SMS Send Events

{% apitags %}
SMS, Engagement, Delivery
{% endapitags %}

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user
}
```
{% endapi %}

{% api %}

## SMS Rejection Events

{% apitags %}
SMS, Engagement, Rejection
{% endapitags %}

```json
// SMS Rejection: users.messages.sms.Rejection
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider’s reason code as to why the message was not sent (Rejection and Delivery Failure events only)
}
```
{% endapi %}


{% api %}

## SMS Delivery Failure Events

{% apitags %}
SMS, Engagement, Delivery
{% endapitags %}

```json
// SMS Delivery Failure: users.messages.sms.DeliveryFailure
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform and users who are sent a schedule message get the same dispatch_id. Action-based or API triggered messages get a unique dispatch_id per user,
  "error": (string) the Braze provided error (Rejection and Delivery Failure events only),
  "provider_error_code": (string) the provider’s reason code as to why the message was not sent (Rejection and Delivery Failure events only)
}
```
{% endapi %}


{% api %}

## Campaign Conversion Events

{% apitags %}
Campaign, Engagement, Conversion
{% endapitags %}

Data accumulates when a user converts on a Campaign.

{% alert important %}
Please note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_index` field represents which conversion event. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Campaign Conversion Event: users.campaigns.Conversion
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
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
Canvas, Engagement, Conversion
{% endapitags %}

Data accumulates when a user converts on a  Canvas. You can use this data to track conversions on Canvas Steps.

{% alert important %}
Please note that the conversion event is encoded in the `conversion_behavior` field, which includes the type of conversion event, the window (timeframe), and additional information depending on the conversion event type. The `conversion_index` field represents which conversion event. i.e., 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

```json
// Canvas Conversion Event: users.canvas.Conversion
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "app_id": (string) id for the app on which the user action occurred,
  "canvas_id": (string) id of the canvas,
  "canvas_name": (string) name of the Canvas,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) id of the last step the user was sent before the conversion
}
```
{% endapi %}


{% api %}

## Canvas Entry Events

{% apitags %}
Canvas, Engagement, Entry
{% endapitags %}

Data accumulates when your users enter a Canvas. You can use this data to track when users enter a Canvas.

```json
// Canvas Entry Event: users.canvas.Entry
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) id of the step the user entered into,
  "in_control_group": (boolean) whether the user was enrolled in the control group for a Canvas
}
```

{% endapi %}

{% api %}
## Campaign Control Group Enrollment Events

{% apitags %}
Campaign, Engagement, Entry
{% endapitags %}

Data accumulates when your users are enrolled in a control group for a Campaign. You can use this data to track when users are enrolled in the control group for a specific campaign.

```json
// Campaign Control Group Enrollment: users.campaigns.EnrollInControl
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under REST API Parameter Definitions)
}
```

{% endapi %}

[support]: {{ site.baseurl }}/support_contact/

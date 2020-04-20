---
nav_title: Customer Behavior Events
layout: customer_behavior_events_glossary

page_order: 4

excerpt_separator: ""
page_type: glossary

description: "This glossary lists the various Customer Behavior Events that Braze can track and send to chosen Data Warehouses using our tool, Currents."

tool: currents
---

Please contact your Braze representative or [open a support ticket][support] if you need access to additional event entitlements. If you can't find what you need below, check out our [Message Engagement Events Library]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of Customer Behavior Event Structure %}
<br>
This Customer Behavior Events breakdown shows what type of information is generally included in a customer behavior event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming currents event data to make data-driven reports, charts and take advantage of other valuable data metrics. 

![image]({% image_buster /assets/img/customer_engagement_event.png %})

Customer Behavior Events events are comprised of __user specific__ properties, __behavior specific__ properties and __device specific__ properties. 

{% enddetails %}

{% alert important %}
Please note that these schemas __only apply to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage)__. For schema that apply to the other partners, please check [their respective pages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).
{% endalert %}

{% api %}

## Custom Events

{% apitags %}
Custom Events
{% endapitags %}

This event occurs when a specific custom event is triggered. Use this to track when users perform custom events in your application.

```json
// Custom Event: users.behaviors.CustomEvent
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "name": (string) name of the custom event,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred,
  "properties": (string) JSON encoded string of the custom properties for this event
}
```

{% endapi %}
{% api %}

## Purchase Event

{% apitags %}
Purchases
{% endapitags %}

This event occurs when a user makes a purchase. Use this data to track when users purchase something in the application.

{% alert tip %}
Purchases are special custom events and come with a JSON encoded string of custom event properties the same way custom events do.
{% endalert %}

```json
// Purchase Event: users.behaviors.Purchase
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "product_id": (string) id of the product purchased,
  "price": (float) price of the purchase,
  "currency": (string) three letter alpha ISO 4217 currency code,
  "properties": (string) JSON encoded string of the custom properties for this event,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```
{% endapi %}


{% api %}

## First Session Event

{% apitags %}
Sessions
{% endapitags %}

This event occurs when a user starts their first session in your application. Use this data to track when users start sessions. 

{% alert tip %}
When a user starts their first session, both a `FirstSession` and a `SessionStart` event are fired.
{% endalert %}

```json
// Session Start: users.behaviors.app.FirstSession
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "timezone": (string) IANA timezone of the user at the time of the event,
  "session_id": (string) id of the session,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the session occurred
}
```
{% endapi %}

{% api %}

## Session Start Event

{% apitags %}
Sessions
{% endapitags %}

This event occurs when a user starts a session. Use this data to track when users start sessions.

{% alert tip %}
When a user starts their first session, both a `FirstSession` and a `SessionStart` event are fired.
{% endalert %}

```json
// Session Start: users.behaviors.app.SessionStart
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "session_id": (string) id of the session,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the session occurred
}
```

{% endapi %}

{% api %}

## End Session Event

{% apitags %}
Sessions
{% endapitags %}

This occurs when a user exits your application, therefore ending their current session. Use this data to track when sessions end, and along with the appropriate session start event, calculate the duration of their time in a session.

{% alert tip %}
When a user starts their first session, both a `FirstSession` and a `SessionStart` event are fired.
{% endalert %}

```json
// Session End: users.behaviors.app.SessionEnd
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "session_id": (string) id of the session,
  "duration": (float) seconds session lasted,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the session occurred
}
```
{% endapi %}

{% api %}

## Location Event

{% apitags %}
Locations
{% endapitags %}

This event is triggered when a user visits a specified location. Use this to track users triggering location events in your app.

```json
// Location Event: users.behaviors.Location
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "longitude": (float) longitude of recorded location,
  "latitude": (float) latitude of recorded location,
  "altitude": (float) altitude of recorded location,
  "ll_accuracy": (float) latitude/longitude accuracy of recorded location,
  "alt_accuracy": (float) altitude accuracy of recorded location,
  "app_id": (string) id for the app on which the user action occurred,
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
Impression, News Feed
{% endapitags %}

This event occurs when the user views the entire news feed, not a specific News Feed Card. Use this to track users viewing the News Feed.

{% alert tip %}
We do track other News Feed events; these are located in [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/).
{% endalert %}

```json
// News Feed Impression: users.behaviors.app.NewsFeedImpression
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "device_id": (string) id of the device on which the event occurred
}
```

{% endapi %}
{% api %}
## Uninstall Events

{% apitags %}
Uninstall
{% endapitags %}

This event occurs when a user uninstalls an app. Use this data to track when users uninstall an app.

{% alert important %}
Please note that this is not fired when the user actually uninstalls the app - that's impossible to track exactly. Braze sends a daily silent push to determine if the app still exists on your user's device, and if we get an error on that silent push, it is assumed the app has been uninstalled.
{% endalert %}

```json
// Uninstall Event: users.behaviors.Uninstall
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "app_id": (string) id for the app on which the user action occurred
}
```

{% endapi %}

{% api %}

## Attribution Events

{% apitags %}
Attribution
{% endapitags %}

This event occurs when an app installation is attributed to a source. Use this to track where your app installs are coming from.

```json
// Install Attribution Event: users.behaviors.InstallAttribution
{
  "id": (string) unique id of this event,
  "user_id": (string) braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) time of the event in seconds since the epoch,
  "source": (string) the source of the attribution
}
```
{% endapi %}

[support]: {{site.baseurl}}/support_contact/

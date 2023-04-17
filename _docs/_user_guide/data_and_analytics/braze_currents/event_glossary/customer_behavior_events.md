---
nav_title: Customer Behavior and User Events
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "This glossary lists the various Customer Behavior and User Events that Braze can track and send to chosen Data Warehouses using Currents."
tool: Currents
search_rank: 7
---

Contact your Braze representative or open a [support ticket]({{site.baseurl}}/braze_support/) if you need access to additional event entitlements. If you can't find what you need in this article, check out our [Message Engagement Events Library]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) or our [Currents sample data examples](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of customer behavior and user event structure and platform values %}

### Event structure 

This customer behavior and user events breakdown shows what type of information is generally included in a customer behavior or user event. With a solid understanding of its components, your developers and business intelligence strategy team can use the incoming Currents event data to make data-driven reports, charts and take advantage of other valuable data metrics. 

![Breakdown of a user event showing a purchase event with the listed properties grouped by user-specific properties, behavior-specific properties, and device-specific properties]({% image_buster /assets/img/customer_engagement_event.png %})

Customer behavior and user events are comprised of **user-specific** properties, **behavior-specific** properties, and **device-specific** properties. 

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
Note that these schemas only apply to the flat file event data we send to Data Warehouse partners (Google Cloud Storage, Amazon S3, and Microsoft Azure Blob Storage), and are not available for Segment.io connectors. For schema that apply to other partners, refer to our list of [available partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) and check their respective pages.<br><br>Additionally, note that Currents will drop events with excessively large payloads of greater than 900KB. 

{% endalert %}
{% api %}

## Custom events

{% apitags %}
Custom Events
{% endapitags %}

This event occurs when a specific custom event is triggered. Use this to track when users perform custom events in your application.

```json
// Custom Event: users.behaviors.CustomEvent
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred,
  "name": (required, string) name of the custom event,
  "properties": (required, string) JSON encoded string of the properties for this event,
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

## Purchase event

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
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred,
  "product_id": (required, string) id of the product purchased,
  "price": (required, float) price of the purchase,
  "currency": (required, string) three letter alpha ISO 4217 currency code,
  "properties": (required, string) JSON encoded string of the custom properties for this event,
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

## First session event

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
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "session_id": (required, string) id of the session,
  "app_id": (required, string) id for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the session occurred,
  "gender": (optional, string) gender of the user,
  "country": (optional, string) country of the user,
  "language": (optional, string) language of the user,
  "sdk_version": (optional, string) version of the Braze SDK in use during the session
}
```
{% endapi %}

{% api %}

## Session start event

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
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the session occurred
}
```

{% endapi %}

{% api %}

## End session event

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
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "duration": (optional, float) seconds session lasted,
  "session_id": (required, string) id of the session,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the session occurred
}
```
{% endapi %}

{% api %}

## Location event

{% apitags %}
Locations
{% endapitags %}

This event is triggered when a user visits a specified location. Use this to track users triggering location events in your app.

```json
// Location Event: users.behaviors.Location
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "latitude": (required, float) latitude of recorded location,
  "longitude": (required, float) longitude of recorded location,
  "altitude": (optional, float) altitude of recorded location,
  "ll_accuracy": (optional, float) latitude/longitude accuracy of recorded location,
  "alt_accuracy": (optional, float) altitude accuracy of recorded location,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred,
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
Impression, News Feed
{% endapitags %}

This event occurs when the user views the entire News Feed, not a specific News Feed Card. Use this to track users viewing the News Feed.

{% alert tip %}
We do track other News Feed events; these are located in [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/).
{% endalert %}

```json
// News Feed Impression: users.behaviors.app.NewsFeedImpression
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) id for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred
}
```

{% endapi %}
{% api %}

## Attribution events

{% apitags %}
Attribution
{% endapitags %}

This event occurs when an app installation is attributed to a source. Use this to track where your app installs are coming from.

```json
// Install Attribution Event: users.behaviors.InstallAttribution
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (requierd, int) 10-digit UTC time of the event in seconds since the epoch,
  "source": (required, string) the source of the attribution
}
```

{% endapi %}

{% api %}

## Random bucket number event

{% apitags %}
Random Bucket Number
{% endapitags %}

This user event occurs every time a new user is created within their app group. During this event, each new user gets assigned a random bucket number that you can then use to create uniformly distributed segments of random users. Use this to group a range of random bucket number values and compare performance across your campaigns and campaign variants. 

```json
// Random Bucket Number Event: users.RandomBucketNumberUpdate
{
  "id": (required, string) unique id of this event,
  "app_group_id": (required, string) AppGroup API id
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (optional, int) UTC time of the event in milliseconds since the epoch,
  "random_bucket_number": (required, int) new random bucket number
  "prev_random_bucket_number":  (optional, int) old random bucket number, optional
}
```

{% alert important %}
Note that this Currents event is only available for customers that have purchased an "all events connector" and is only available for storage event connectors (i.e Amazon S3, Microsoft Azure, Google Cloud Storage).
<br><br>To get this event enabled and to schedule the backfill for existing users' random bucket numbers in your app group, contact your customer success manager.
{% endalert %}

{% endapi %}



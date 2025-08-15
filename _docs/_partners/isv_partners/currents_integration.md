---
nav_title: Custom currents connector
alias: /currents_connector/
hidden: true
---

# Custom Currents connector

> Learn how to integrate a custom Currents connector, so you can get event data from Braze in real time, enabling more customized analytics, reporting, and automation.

## Prerequisites

To integrate a custom Currents connector in Braze, you'll need to provide an endpoint URL and an [optional authentication token](#authentication).

Additionally, if you have more than one app group in Braze, you'll need to configure a custom Currents connector for each group. However, you can point all app groups to the same endpoint, or to an endpoint with an additional `GET` parameter, such as `your_app_group_key=”Brand A”`.

## Preventing data loss

### Error monitoring

To avoid data loss and service interruption, its essential that you monitor your endpoints at all times and aim to address hard errors or downtime within 24 hours.

For most error types, (such as server errors, network connection errors, etc.), Braze will continue to queue and retry event transmissions for up to 24 hours. After that time, non-transmitted events will be dropped. Connectors with consistently poor error rates or uptime will be automatically suspended.

### Change resilience

Occasionally, we'll make non-breaking changes to Braze Currents schemas. Non-breaking changes are new nullable columns or event types.

We typically give a two-week notice for these changes, but sometimes this isn't possible. Its essential that you design your integration to handle unrecognized fields or event types, otherwise it will likely lead to data loss.

{% alert tip %}
For the full list of Currents event schemas, [Message Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events).
{% endalert %}

## Batching and serialization

The target data format is JSON over HTTPS. By default, events are batched into groups of 100 based on the following:

- **Number of queued events**: For example, if batch size is configured for 200 events and there are 200 events in the queue.
- **Length of an event:** Typically events are not queued if an event is longer than 15 minutes. Each event type has a separate queue, so latency may vary across event types.

Events are then sent to the endpoint as a JSON array of all events in the following format:

```json
{"events": [event1, event2, event3, etc...]}
```

There will be a top-level JSON object with the key `"events"` that maps to an array of further JSON objects, each representing a single event.

## Payload examples

The following examples show payloads for individual events, meaning the payloads would belong to a larger array of JSON objects, where each JSON object represents a single event in the batch.

Additionally, their structure varies slightly from the flat structure found in [Message Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events). In particular, they contain two sub-objects:

|Name|Description|
|----|-----------|
|`"user"`|Contains user properties such as `user_id`, `external_user_id`, `device_id`, and `timezone`.|
|`"properties"`|Contains attributes of an event, such as the `app/campaign/canvas/platform` it applies to.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

If a downstream endpoint receives a payload with zero events or an empty request body, the result should be considered a no-op, meaning no downstream effects should occur from this call. However, you should still check the `Authorization` header (like you would a normal API call), and give an appropriate HTTP response for [invalid credentials](#authentication), such as `401` or `403`. This let's Braze know that the connector's credentials are valid.

### Campaign-associated events

Here are some example event payloads for various events, as they would appear if associated with a campaign:

#### In-App Message Click

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Push Notification Send

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### Email Open

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### SMS Delivery

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Canvas-associated events

Here are some example event payloads for various events, as they would appear if associated with a Canvas:

#### In-App Message Click

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Push Notification Send

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### Email Open

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### SMS Delivery

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Other events

Here are some example event payloads for various other events that are not associated with either campaigns or Canvases:

#### Custom Event

```json
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Purchase Event

```json
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Session Start

```json
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentication

Authentication tokens in your payload are optional. They can be passed through an HTTP `Authorization` header using the `Bearer` authorization scheme, as specified in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). Although optional, if an authentication token is passed, Braze will always validate it first&#8212;even if no events are in the payload.

Per RFC 6750, tokens should be Base64-encoded values with at least one character. Keep in mind, RFC 6750 allows tokens to contain the following characters in addition to the normal Base64 characters: `-`, `.`, `_`, and `~`. You can choose whether you'd like to include these characters in your token or not&#8212;however, it must be in Base64 format.

Additionally, if the `Authorization` header is present, it will be constructed using the following format:

```plaintext
"Authorization: Bearer " + <token>
```

For example, if your authentication token is `0p3n5354m3==`, your `Authorization` header should be similar to the following:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
In the future, we may use `Authorization` headers to implement a custom, key-value-pair, authorization scheme that's unique to Braze. This would adhere to the [RFC 7235](https://tools.ietf.org/html/rfc7235) specification, which is how some companies implement their authentication schemes, such as Amazon Web Services (AWS).
{% endalert %}

## Versioning

All requests from our HTTP connector integration will be sent with a custom header designating the version of the Currents request being made:

```plaintext
Braze-Currents-Version: 1
```

The version will always be `1` unless, as we don't expect to increment this number very often, if ever.

Just like our [data warehouse storage schemas]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1), every event field in an individual event is guaranteed to be backward-compatible with previous event payload versions, according to the [Apache Avro](https://avro.apache.org/) definition of backward-compatibility:

1. Specific event fields are guaranteed to always have the same datatype over time.
2. Any new fields that are added to the payload over time must be considered optional by all parties.
3. Required fields will never be removed.

## Error handling and retry mechanism

If an error occurs, Braze will queue and retry the request based on the HTTP return code received. It will continue to retry for at least two days, as long as data is buffered in the system. If data is stuck for more than 24 hours, our on-call engineers will be alerted automatically. At this time, our backoff strategy is to retry periodically.

If your Currents integration starts returning `4XX` errors, Braze will automatically send you a notification email and automatically extend the retention period to a minimum of seven days.

Any HTTP error code not listed below will be treated as an HTTP `5XX` error.

{% alert warning %}
If the Braze retry mechanism fails to deliver an event for more than 24 hours, data loss will occur.
{% endalert %}

The following HTTP status codes will be recognized by our connector client:

<table>
  <thead>
    <tr>
      <th>Status Code</th>
      <th>Response</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Success</td>
      <td>Event data will not be re-sent.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Server-side error</td>
      <td>Event data will be re-sent in an exponential backoff pattern with jitter. If the data is not successfully sent within 24 hours, it will be dropped.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Client-side error</td>
      <td>The connector sent at least one malformed event. The event data will be split into batches of size 1 and re-sent. Any events in these size-1 batches that receive another <code>400</code> response will be dropped permanently. You should report repeated occurrences.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Unauthorized</td>
      <td>The connector was configured with invalid credentials. Event data will be re-sent after a delay of 2–5 minutes. If unresolved within 48 hours, the event data will be dropped.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Forbidden</td>
      <td>The connector was configured with invalid credentials. Event data will be re-sent after a delay of 2–5 minutes. If unresolved within 48 hours, the event data will be dropped.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Not Found</td>
      <td>The connector was configured with invalid credentials. Event data will be re-sent after a delay of 2–5 minutes. If unresolved within 48 hours, the event data will be dropped.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload Too Large</td>
      <td>Event data will be split into smaller batches and re-sent.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Too Many Requests</td>
      <td>Indicates rate limiting. Event data will be re-sent in an exponential backoff pattern with jitter. If not successfully sent within 24 hours, it will be dropped.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

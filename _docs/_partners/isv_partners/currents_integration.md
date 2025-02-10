---
nav_title: Custom Currents Connector
alias: /currents_connector/
hidden: true
---

# Partner custom Currents connector

## Integration Overview
Braze will invoke a REST API (JSON over HTTPS) that conforms to the specification in this document. To configure a new Custom Currents Connector on the Braze side, a customer need only provide an endpoint URL and an optional Authentication Token. Note that Currents Connectors are configured at the App Group level, so customers with multiple App Groups will need to configure at least one Custom Currents Connector per App Group. They can all point to the same endpoint, or to an endpoint with an additional GET parameter (e.g. customer_app_group_key=”Brand A”).

Braze batches events based on a combination of number of queued events (e.g. if batch size is configured for 200 events and there are 200 events in the queue) and time (we typically won’t queue events for more than 15 minutes). Each event type has a separate queue, so latency will vary across event types..

## Non-Functional Requirements
Braze makes every reasonable effort to prevent data loss. For many types of errors (e.g. server errors, network connection errors), we will continue to retry event transmission. Braze will continue to queue and retry transmission for up to 24 hours, after which we will drop untransmitted events. Connectors displaying consistently poor uptime/error rates will be automatically suspended.

To avoid data loss and service interruption, it is strongly recommended that customers monitor their endpoints 24x7 and aim to address hard errors or downtime within 24 hours.

## Change Resilience
Braze may, from time to time, make non-breaking changes to Currents schemas. A non-breaking change is a new nullable column, or a new event type. We typically aim to provide at least 2 weeks’ notice for such changes but don’t guarantee it. As such, Braze strongly recommends that customer implementations are resilient to unrecognized fields and event types. 

A brittle integration that isn’t properly monitored will likely lead to data loss at some point. Please refer to the Non-Functional Requirements section.


## Serialization and data format

The target data format is JSON over HTTPS. Events will be grouped into batches of 100 events by default, and sent to the endpoint as a JSON array containing all of the events. The batches will be sent in the following format:

`{"events": [event1, event2, event3, etc...]}`

There will be a top-level JSON object with the key "events" that maps to an array of further JSON objects, each representing a single event.

The following examples are for _individual_ events (such as they would be part of the larger array of JSON objects, with each JSON object representing a single event in the batch).

Note that Braze may add fields to events and new events from time to time. Customers should design their integrations to be resilient to such changes and refer to our [documentation](https://www.braze.com/docs/user_guide/data/braze_currents/event_glossary/message_engagement_events) for up-to-date event schemas. Note that, per the below examples, the structure for Custom Connector events is slightly different from the flat structure in the general documentation linked above. In particular, there are two sub-objects, “user”, which contains user properties such as user_id, external_user_id, device_id, and timezone, and “properties”, which contains attributes of an event, like the app/campaign/canvas/platform to which it applies. 

In the case where the downstream endpoint receives either a payload with zero events, or an empty request body, the result should be considered a no-op, and no downstream effects should happen as a result of this call. However, the request's Authorization header should be checked anyway as if it were a normal API call, and an appropriate HTTP response should be given (401 or 403) if the credentials are not valid. This will enable us to use this mechanism to verify that our connector is configured with the proper credentials.


### Campaign-associated events

Here are some example event payloads for various events, as they would appear if associated with a campaign:

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

If required, authentication is performed by passing a token in the HTTP `Authorization` header, via the `Bearer` authorization scheme, as specified in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). In the future, Braze may choose to use the `Authorization` header to implement a custom (unique to Braze) key-value pair authorization scheme conforming to [RFC 7235](https://tools.ietf.org/html/rfc7235) (which is how for example, AWS's custom auth scheme works).

As per RFC 6750, the token should be a Base64-encoded value of at least one character. A notable quirk of RFC 6750 is that it allows the token to contain the following characters in addition to the normal Base64 characters: '-', '.', '_', and '~'. Partners and customers are free to decide whether to include these characters in their token or not. Note that customers are required to provide this token in Base64 form; Braze will not perform this encoding on our end.

Per RFC 6750, the header, if present, will be constructed using the following format:

`"Authorization: Bearer " + <token>`

So for example, if the API token is `0p3n5354m3==`, the Authorization header will look like this:

`Authorization: Bearer 0p3n5354m3==`

Note that authentication must be validated even if there are no events in the payload. Braze may make such calls to confirm credentials are up to date.

## Versioning

All requests from our Integratable HTTP Connectors will be sent with a custom header designating the version of the Currents request being made:

`Braze-Currents-Version: 1`

The version will always be `1` unless we make severely backward-incompatible changes to the request payload or semantics. We don't expect to increment this number very often, if ever.

Individual events will follow the same evolution rules as our existing S3 Avro schemas for Currents Data Export. That is, every event's fields will be guaranteed to be backward-compatible with prior versions of the event payloads according to the Avro definition of backward-compatibility, including the following rules:

- Specific event fields are guaranteed to always have the same datatype over time.
- Any new fields that are added to the payload over time must be considered optional by all parties.
- Required fields will never be removed.

## Error handling and retry mechanism

In the event of an error, Braze will queue and retry the request based on the HTTP return code received. Any HTTP error code not listed below will be treated as an HTTP 5XX error.

{% alert important %}
If our retry mechanism fails to deliver events to their endpoint for more than 24 hours, there will be data loss.
{% endalert %}

The following HTTP status codes will be recognized by our connector client:
- **2XX** — Success
  - Event data will not be re-sent.<br><br>
- **5XX** — Serverside error
  - Event data will be re-sent in an exponential backoff pattern with jitter. If the data is not successfully sent within 24 hours, it will be dropped.<br><br>
- **400** — Client-side error
  - Our connector somehow sent at least one malformed event. If this occurs, the event data will be split into batches of size 1 and re-sent. Any events in these size-1 batches that receive an additional HTTP 400 response will be dropped permanently. Partners and/or customers are encouraged to let us know if they detect this occurring on their end.<br><br>
- **401** (Unauthorized), **403** (Forbidden), **404**
  - The connector was configured with invalid credentials. Event data will be re-sent after a delay of between 2 and 5 minutes. If this issue is not resolved by the customer within 48 hours, the event data will be dropped.<br><br>
- **413** — Payload Too Large
  - Event data will be split into smaller batches and re-sent.<br><br>
- **429** — Too Many Requests
  - Indicates rate limiting. Event data will be re-sent in an exponential backoff pattern with jitter. If the data is not successfully sent within 24 hours, it will be dropped.

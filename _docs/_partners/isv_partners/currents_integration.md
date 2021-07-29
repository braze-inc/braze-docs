---
nav_title: Custom Currents Connector
alias: /currents_connector/
hidden: true
---

# Partner Custom Currents Connector

## Serialization and Data Format

The target data format will be JSON over HTTPS. Events will be grouped into batches of events,
the size of which is configurable, and sent to the endpoint as a JSON array containing all of the
events. The batches will be sent in the following format:

`{"events": [event1, event2, event3, etc...]}`

i.e. There will be a top-level JSON object with the key "events" that maps to an array of further JSON objects, each representing a single event.

The examples below are for _individual_ events (i.e. they'd just be part of the larger array of JSON objects as described above, with each JSON object representing a single event in the batch).

### Campaign-Associated Events

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
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Canvas-Associated Events

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

### Other Events

Here are some example event payloads for various other events that are not associated with either campaigns or Canvases:

```
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
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

If required, authentication will be performed by passing a token in the HTTP `Authorization` header, via the `Bearer` authorization scheme, as specified in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1). This is also automatically forwards-compatible with any custom authentication scheme we may choose to implement in the future, since using the `Authorization` header would allow us to switch over to a custom (unique to Braze) key-value pair authorization scheme conforming to [RFC 7235](https://tools.ietf.org/html/rfc7235) (which is how e.g. AWS's custom auth scheme works) if we so choose in the future.

As per RFC 6750, the token will be a Base64-encoded value of at least one character. (Obviously though, we must vet our partners and customers so that we know that they are unlikely to choose incredibly weak tokens.) A notable quirk of RFC 6750 is that it allows the token to contain the following characters in addition to the normal Base64 characters: '-', '.', '_', and '~'. Since the exact contents of the token make absolutely no difference to any of our systems, we won't care whether our partners decide to include these characters in their token or not.

Per RFC 6750, the header will be constructed using the following format:

`"Authorization: Bearer " + <token>`

So for example, if the API token is `0p3n5354m3==`, the Authorization header will look like this:

`Authorization: Bearer 0p3n5354m3==`

## Versioning

All requests from our Integratable HTTP Connectors will be sent with a custom header designating the version of the Currents request being made:

`Braze-Currents-Version: 1`

The version will always be 1 unless we make severely backward-incompatible changes to the request payload or semantics. We don't expect to increment this number very often, if ever. 

Individual events will follow the same evolution rules as our existing Avro schemas. That is, every event's fields will be guaranteed to be backward-compatible with prior versions of the event payloads according to the Avro definition of backward-compatibility, including the following rules:

- Specific event fields are guaranteed to always have the same datatype over time.
- Any new fields that are added to the payload over time must be considered optional by all parties.
- Required fields will never be removed.
  - What is considered "required" will be specified via documentation that we will likely want to auto-generate from our Avro schemas as the central source of truth. This will require us to annotate the Avro schema fields with some metadata, and a special script that can read that metadata to generate the documentation.

## Error Handling and Retry Mechanism

In the event of an error, Braze will queue and retry the request based on the HTTP return code received.

{% alert important %}
If our retry mechanism fails to deliver events to their endpoint for more than 24 hours, there will be data loss.
{% endalert %}

The following HTTP status codes will be recognized by our connector client:
- __2XX__ — Success
  - Event data will not be re-sent.<br><br>
- __5XX__ — Serverside error
  - Event data will be re-sent in an exponential backoff pattern with jitter. If the data is not successfully sent within 24 hours, it will be dropped.<br><br>
- __400__ — Client-side error
  - Our connector somehow sent at least one malformed event. If this occurs, the event data will be split into batches of size 1 and re-sent. Any events in these size-1 batches that receive an additional HTTP 400 response will be dropped permanently. Partners and/or customers should be encouraged to let us know if they detect this occurring on their end.<br><br>
- __401__ (Unauthorized) or __403__ (Forbidden)
  - The connector was configured with invalid credentials. The connector task will halt sending, and will be marked as "Failed". Event data will be re-sent after a delay of between 2 and 5 minutes (this is handled by the Connect Task Restarter). If this issue is not resolved by the customer within 48 hours, the event data will be dropped.<br><br>
- __413__ — Payload Too Large
  - Event data will be split into smaller batches and re-sent.<br><br>
- __429__ — Too Many Requests
  - Indicates rate limiting. Event data will be re-sent in an exponential backoff pattern with jitter. If the data is not successfully sent within 24 hours, it will be dropped.
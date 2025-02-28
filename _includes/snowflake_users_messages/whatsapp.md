### `ABORT_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_ABORT_SHARED
// When a scheduled WhatsApp message cannot be delivered, before sending to Meta.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "TO_PHONE_NUMBER": "[PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
        "TIMEZONE": "Time zone of the user",
        "ABORT_TYPE": "Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
        "ABORT_LOG": "[PII] Log message describing abort details (up to 128 chars)",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `DELIVERY_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED
// When a WhatsApp message is delivered to the end user.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "TO_PHONE_NUMBER": "[PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
        "TIMEZONE": "Time zone of the user",
        "FROM_PHONE_NUMBER": "Phone number used to send in e.164 format (for example +14155552671)",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `FAILURE_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_FAILURE_SHARED
// When a WhatsApp message cannot be delivered, after sending to Meta.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "TO_PHONE_NUMBER": "[PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
        "TIMEZONE": "Time zone of the user",
        "FROM_PHONE_NUMBER": "Phone number used to send in e.164 format (for example +14155552671)",
        "PROVIDER_ERROR_CODE": "Error code from WhatsApp",
        "PROVIDER_ERROR_TITLE": "Description of error from WhatsApp",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `INBOUNDRECEIVE_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED
// When a WhatsApp message is received from a user.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "USER_PHONE_NUMBER": "[PII] The user's phone number from which the message was received",
        "INBOUND_PHONE_NUMBER": "The inbound number that the message was sent to",
        "TIMEZONE": "Time zone of the user",
        "MESSAGE_BODY": "Typed response from the user",
        "QUICK_REPLY_TEXT": "Text of button pressed by the user",
        "MEDIA_URLS": "Media URLs from the user",
        "ACTION": "Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `READ_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_READ_SHARED
// When a WhatsApp message is read by the user.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "TO_PHONE_NUMBER": "[PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
        "TIMEZONE": "Time zone of the user",
        "FROM_PHONE_NUMBER": "Phone number used to send in e.164 format (for example +14155552671)",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `SEND_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_SEND_SHARED
// When a WhatsApp message is sent to Meta.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "TO_PHONE_NUMBER": "[PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
        "TIMEZONE": "Time zone of the user",
        "FROM_PHONE_NUMBER": "Phone number used to send in e.164 format (for example +14155552671)",
        "MESSAGE_EXTRAS": "[PII] A JSON string of the tagged key-value pairs during liquid rendering",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```


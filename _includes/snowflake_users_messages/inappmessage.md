### `ABORT_SHARED`

```json
// USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED
// An originally scheduled inappmessage message was aborted for some reason.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "APP_API_ID": "API ID of the app on which this event occurred",
        "CARD_API_ID": "API ID of the card",
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DEVICE_ID": "ID of the device on which the event occurred"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "SDK_VERSION": "Version of the Braze SDK in use during the event",
        "PLATFORM": "Platform of the device",
        "OS_VERSION": "Version of the operating system of the device",
        "DEVICE_MODEL": "Model of the device",
        "RESOLUTION": "Resolution of the device",
        "CARRIER": "Carrier of the device",
        "BROWSER": "Device browser - extracted from user_agent - on which the open occurred",
        "VERSION": "Which version of in-app message, legacy or triggered",
        "AD_ID_TYPE": "One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
        "AD_TRACKING_ENABLED": "Whether advertising tracking is enabled for the device",
        "ABORT_TYPE": "Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
        "ABORT_LOG": "[PII] Log message describing abort details (up to 128 chars)",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "AD_ID": "[PII] Advertising identifier",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `CLICK_SHARED`

```json
// USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED
// When a user clicks an in app message.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "APP_API_ID": "API ID of the app on which this event occurred",
        "CARD_API_ID": "API ID of the card",
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DEVICE_ID": "ID of the device on which the event occurred"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "SDK_VERSION": "Version of the Braze SDK in use during the event",
        "PLATFORM": "Platform of the device",
        "OS_VERSION": "Version of the operating system of the device",
        "DEVICE_MODEL": "Model of the device",
        "RESOLUTION": "Resolution of the device",
        "CARRIER": "Carrier of the device",
        "BROWSER": "Device browser - extracted from user_agent - on which the open occurred",
        "VERSION": "Which version of in-app message, legacy or triggered",
        "AD_ID_TYPE": "One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
        "AD_TRACKING_ENABLED": "Whether advertising tracking is enabled for the device",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "AD_ID": "[PII] Advertising identifier",
        "SEND_ID": "Message send ID this message belongs to",
        "BUTTON_ID": "ID of the button clicked, if this click represents a click on a button"
    }
}
```

### `IMPRESSION_SHARED`

```json
// USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED
// When a user views an in app message.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "APP_API_ID": "API ID of the app on which this event occurred",
        "CARD_API_ID": "API ID of the card",
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DEVICE_ID": "ID of the device on which the event occurred"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "SDK_VERSION": "Version of the Braze SDK in use during the event",
        "PLATFORM": "Platform of the device",
        "OS_VERSION": "Version of the operating system of the device",
        "DEVICE_MODEL": "Model of the device",
        "RESOLUTION": "Resolution of the device",
        "CARRIER": "Carrier of the device",
        "BROWSER": "Device browser - extracted from user_agent - on which the open occurred",
        "VERSION": "Which version of in-app message, legacy or triggered",
        "AD_ID_TYPE": "One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
        "AD_TRACKING_ENABLED": "Whether advertising tracking is enabled for the device",
        "MESSAGE_EXTRAS": "[PII] A JSON string of the tagged key-value pairs during liquid rendering",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "AD_ID": "[PII] Advertising identifier",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```


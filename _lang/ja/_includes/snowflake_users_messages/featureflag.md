## リレーションシップテーブル

### `IMPRESSION_SHARED`

```json
// USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED
// When a user views an feature flag.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "APP_API_ID": "API ID of the app on which this event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "USER_ID": "Braze user ID of the user who performed this event"
    },
    "native_keys": {
        "FEATURE_FLAG_ID_NAME": "The Feature Flag Rollout identifier",
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "BROWSER": "Device browser - extracted from user_agent - on which the open occurred",
        "CARRIER": "Carrier of the device",
        "COUNTRY": "[PII] Country of the user",
        "DEVICE_MODEL": "Model of the device",
        "LANGUAGE": "[PII] Language of the user",
        "OS_VERSION": "Version of the operating system of the device",
        "PLATFORM": "Platform of the device",
        "RESOLUTION": "Resolution of the device",
        "SDK_VERSION": "Version of the Braze SDK in use during the event",
        "TIMEZONE": "Time zone of the user",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

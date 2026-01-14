## リレーションシップテーブル

### `SHARED`

```json
// USERS_BEHAVIORS_UNINSTALL_SHARED
// When a user uninstalls an app.

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
        "APP_API_ID": "API ID of the app on which this event occurred"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

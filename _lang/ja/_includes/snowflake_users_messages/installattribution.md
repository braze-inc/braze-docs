## リレーションシップテーブル

### `SHARED`

```json
// USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED
// When a user installs an app and we attribute it to a partner.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "DEVICE_ID": "ID of the device on which the event occurred",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "SOURCE": "The source of the attribution",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

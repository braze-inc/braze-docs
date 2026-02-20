## リレーションシップテーブル

### `SHARED`

```json
// USERS_BEHAVIORS_CUSTOMEVENT_SHARED
// When a user performs a custom event.

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
        "DEVICE_ID": "ID of the device on which the event occurred",
        "LOCATION_SET_ID": "The ID of the location set of the geofence that was triggered",
        "GEOFENCE_ID": "The ID of the geofence that was triggered"
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
        "NAME": "Name of the custom event",
        "PROPERTIES": "Custom properties stored as a JSON encoded string",
        "AD_ID_TYPE": "One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
        "AD_TRACKING_ENABLED": "Whether advertising tracking is enabled for the device",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED: When a user triggers a geofenced area": "",
        "EVENT_TYPE": "What kind of geofence event was triggered. (for example 'enter' or 'exit')",
        "USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED: When a user triggers a geofenced area": "",
        "AD_ID": "[PII] Advertising identifier"
    }
}
```

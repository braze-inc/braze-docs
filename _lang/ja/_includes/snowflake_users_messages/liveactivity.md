## リレーションシップテーブル

### `PUSHTOSTARTTOKENCHANGE_SHARED`

```json
// USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED
// Live Activity Push To Start Token Change Events.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "DEVICE_ID": "ID of the device on which the event occurred"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "ACTIVITY_ATTRIBUTES_TYPE": "Live Activity attribute type",
        "PUSH_TO_START_TOKEN": "Live Activity push to start token",
        "SDK_VERSION": "Version of the Braze SDK in use during the event",
        "IOS_PUSH_TOKEN_APNS_GATEWAY": "APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
        "PUSH_TOKEN_STATE_CHANGE_TYPE": "A description of the push token state change type",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `UPDATETOKENCHANGE_SHARED`

```json
// USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED
// Live Activity Update Token Change Events.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "ACTIVITY_ID": "Live Activity identifier",
        "DEVICE_ID": "ID of the device on which the event occurred"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "UPDATE_TOKEN": "Live Activity update token",
        "SDK_VERSION": "Version of the Braze SDK in use during the event",
        "IOS_PUSH_TOKEN_APNS_GATEWAY": "APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
        "PUSH_TOKEN_STATE_CHANGE_TYPE": "A description of the push token state change type",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `OUTCOME_SHARED`

```json
// USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED
// Live Activity Outcome Events.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "ACTIVITY_ID": "Live Activity identifier"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "ACTIVITY_ATTRIBUTES_TYPE": "Live Activity attribute type",
        "PUSH_TO_START_TOKEN": "Live Activity push to start token",
        "UPDATE_TOKEN": "Live Activity update token",
        "LIVE_ACTIVITY_EVENT_TYPE": "Event type of Live Activity. One of ['start', 'update', 'end']",
        "LIVE_ACTIVITY_EVENT_OUTCOME": "Outcome of Live Activity event",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

### `SEND_SHARED`

```json
// USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED
// Live Activity Send Events.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "ACTIVITY_ID": "Live Activity identifier"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "ACTIVITY_ATTRIBUTES_TYPE": "Live Activity attribute type",
        "PUSH_TO_START_TOKEN": "Live Activity push to start token",
        "UPDATE_TOKEN": "Live Activity update token",
        "LIVE_ACTIVITY_EVENT_TYPE": "Event type of Live Activity. One of ['start', 'update', 'end']",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe"
    }
}
```

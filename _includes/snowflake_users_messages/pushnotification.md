### `ABORT_SHARED`

```json
// USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "APP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "PLATFORM",
        "ABORT_TYPE",
        "ABORT_LOG",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```

### `BOUNCE_SHARED`

```json
// USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "APP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "PUSH_TOKEN",
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "PLATFORM",
        "AD_ID_TYPE",
        "AD_TRACKING_ENABLED",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```

### `INFLUENCEDOPEN_SHARED`

```json
// USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "APP_GROUP_API_ID",
        "APP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DEVICE_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "SDK_VERSION",
        "PLATFORM",
        "OS_VERSION",
        "DEVICE_MODEL",
        "RESOLUTION",
        "CARRIER",
        "BROWSER",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```

### `IOSFOREGROUND_SHARED`

```json
// USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "APP_GROUP_API_ID",
        "APP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DEVICE_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "SDK_VERSION",
        "PLATFORM",
        "OS_VERSION",
        "DEVICE_MODEL",
        "RESOLUTION",
        "CARRIER",
        "BROWSER",
        "AD_ID_TYPE",
        "AD_TRACKING_ENABLED",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```

### `OPEN_SHARED`

```json
// USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "APP_GROUP_API_ID",
        "APP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DEVICE_ID",
        "SLIDE_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "SDK_VERSION",
        "PLATFORM",
        "OS_VERSION",
        "DEVICE_MODEL",
        "RESOLUTION",
        "CARRIER",
        "BROWSER",
        "BUTTON_STRING",
        "BUTTON_ACTION_TYPE",
        "SLIDE_ACTION_TYPE",
        "AD_ID_TYPE",
        "AD_TRACKING_ENABLED",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```

### `SEND_SHARED`

```json
// USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "APP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "PUSH_TOKEN",
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "PLATFORM",
        "AD_ID_TYPE",
        "AD_TRACKING_ENABLED",
        "MESSAGE_EXTRAS",
        "IS_SAMPLED",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```


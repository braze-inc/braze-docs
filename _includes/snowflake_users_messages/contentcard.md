### `ABORT_SHARED`

```json
// USERS_MESSAGES_CONTENTCARD_ABORT_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
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
        "ABORT_TYPE",
        "ABORT_LOG",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```

### `CLICK_SHARED`

```json
// USERS_MESSAGES_CONTENTCARD_CLICK_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "CONTENT_CARD_ID",
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

### `DISMISS_SHARED`

```json
// USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "CONTENT_CARD_ID",
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

### `IMPRESSION_SHARED`

```json
// USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "CONTENT_CARD_ID",
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

### `SEND_SHARED`

```json
// USERS_MESSAGES_CONTENTCARD_SEND_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "DISPATCH_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "CONTENT_CARD_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "MESSAGE_EXTRAS",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```


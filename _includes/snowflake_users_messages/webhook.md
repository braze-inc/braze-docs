### `ABORT_SHARED`

```json
// USERS_MESSAGES_WEBHOOK_ABORT_SHARED

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

### `SEND_SHARED`

```json
// USERS_MESSAGES_WEBHOOK_SEND_SHARED

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
        "MESSAGE_EXTRAS",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID"
    ]
}
```


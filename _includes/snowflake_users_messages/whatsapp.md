### `ABORT_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_ABORT_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DISPATCH_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "TO_PHONE_NUMBER",
        "TIMEZONE",
        "ABORT_TYPE",
        "ABORT_LOG",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `DELIVERY_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DISPATCH_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "TO_PHONE_NUMBER",
        "TIMEZONE",
        "FROM_PHONE_NUMBER",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `FAILURE_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_FAILURE_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DISPATCH_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "TO_PHONE_NUMBER",
        "TIMEZONE",
        "FROM_PHONE_NUMBER",
        "PROVIDER_ERROR_CODE",
        "PROVIDER_ERROR_TITLE",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `INBOUNDRECEIVE_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
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
        "USER_PHONE_NUMBER",
        "INBOUND_PHONE_NUMBER",
        "TIMEZONE",
        "MESSAGE_BODY",
        "QUICK_REPLY_TEXT",
        "MEDIA_URLS",
        "ACTION",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `READ_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_READ_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DISPATCH_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "TO_PHONE_NUMBER",
        "TIMEZONE",
        "FROM_PHONE_NUMBER",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `SEND_SHARED`

```json
// USERS_MESSAGES_WHATSAPP_SEND_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "DISPATCH_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "TO_PHONE_NUMBER",
        "TIMEZONE",
        "FROM_PHONE_NUMBER",
        "MESSAGE_EXTRAS",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```


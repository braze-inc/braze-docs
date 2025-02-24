### `ABORT_SHARED`

```json
// USERS_MESSAGES_SMS_ABORT_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "APP_GROUP_API_ID",
        "CAMPAIGN_ID",
        "CAMPAIGN_API_ID",
        "MESSAGE_VARIATION_API_ID",
        "CANVAS_ID",
        "CANVAS_API_ID",
        "CANVAS_VARIATION_API_ID",
        "CANVAS_STEP_API_ID",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID",
        "SUBSCRIPTION_GROUP_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
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

### `SEND_SHARED`

```json
// USERS_MESSAGES_SMS_SEND_SHARED

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
        "SUBSCRIPTION_GROUP_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "TO_PHONE_NUMBER",
        "CATEGORY",
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

### `CARRIERSEND_SHARED`

```json
// USERS_MESSAGES_SMS_CARRIERSEND_SHARED

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
        "SUBSCRIPTION_GROUP_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "TO_PHONE_NUMBER",
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

### `DELIVERY_SHARED`

```json
// USERS_MESSAGES_SMS_DELIVERY_SHARED

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
        "SUBSCRIPTION_GROUP_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "TO_PHONE_NUMBER",
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

### `DELIVERYFAILURE_SHARED`

```json
// USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED

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
        "SUBSCRIPTION_GROUP_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "TO_PHONE_NUMBER",
        "ERROR",
        "PROVIDER_ERROR_CODE",
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
// USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "APP_GROUP_API_ID",
        "SUBSCRIPTION_GROUP_ID",
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
        "ACTION",
        "MESSAGE_BODY",
        "MEDIA_URLS",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `REJECTION_SHARED`

```json
// USERS_MESSAGES_SMS_REJECTION_SHARED

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
        "SUBSCRIPTION_GROUP_API_ID",
        "APP_GROUP_ID"
    ],
    "native_keys": [
        "TIME",
        "GENDER",
        "COUNTRY",
        "TIMEZONE",
        "LANGUAGE",
        "TO_PHONE_NUMBER",
        "FROM_PHONE_NUMBER",
        "ERROR",
        "PROVIDER_ERROR_CODE",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `SHORTLINKCLICK_SHARED`

```json
// USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED

{
    "primary_key": [
        "ID"
    ],
    "foreign_keys": [
        "USER_ID",
        "EXTERNAL_USER_ID",
        "DEVICE_ID",
        "APP_GROUP_API_ID",
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
        "TIMEZONE",
        "URL",
        "SHORT_URL",
        "USER_AGENT",
        "USER_PHONE_NUMBER",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```


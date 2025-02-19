### `ABORT_SHARED`

```json
// USERS_MESSAGES_EMAIL_ABORT_SHARED

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
        "EMAIL_ADDRESS",
        "IP_POOL",
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

### `BOUNCE_SHARED`

```json
// USERS_MESSAGES_EMAIL_BOUNCE_SHARED

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
        "EMAIL_ADDRESS",
        "SENDING_IP",
        "IP_POOL",
        "BOUNCE_REASON",
        "ESP",
        "FROM_DOMAIN",
        "IS_DROP",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `CLICK_SHARED`

```json
// USERS_MESSAGES_EMAIL_CLICK_SHARED

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
        "EMAIL_ADDRESS",
        "URL",
        "USER_AGENT",
        "IP_POOL",
        "LINK_ALIAS",
        "ESP",
        "FROM_DOMAIN",
        "IS_AMP",
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
// USERS_MESSAGES_EMAIL_DELIVERY_SHARED

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
        "EMAIL_ADDRESS",
        "SENDING_IP",
        "IP_POOL",
        "ESP",
        "FROM_DOMAIN",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `MARKASSPAM_SHARED`

```json
// USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED

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
        "EMAIL_ADDRESS",
        "USER_AGENT",
        "IP_POOL",
        "ESP",
        "FROM_DOMAIN",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `OPEN_SHARED`

```json
// USERS_MESSAGES_EMAIL_OPEN_SHARED

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
        "EMAIL_ADDRESS",
        "USER_AGENT",
        "IP_POOL",
        "MACHINE_OPEN",
        "ESP",
        "FROM_DOMAIN",
        "IS_AMP",
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
// USERS_MESSAGES_EMAIL_SEND_SHARED

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
        "EMAIL_ADDRESS",
        "IP_POOL",
        "MESSAGE_EXTRAS",
        "ESP",
        "FROM_DOMAIN",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `SOFTBOUNCE_SHARED`

```json
// USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED

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
        "EMAIL_ADDRESS",
        "SENDING_IP",
        "IP_POOL",
        "BOUNCE_REASON",
        "ESP",
        "FROM_DOMAIN",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```

### `UNSUBSCRIBE_SHARED`

```json
// USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED

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
        "EMAIL_ADDRESS",
        "IP_POOL",
        "SF_CREATED_AT",
        "AD_ID",
        "SEND_ID",
        "LINK_ID",
        "BUTTON_ID",
        "SLIDE_ID"
    ]
}
```


## 関係図

```mermaid
---
config:
  layout: elk
  elk:
    mergeEdges: true
    nodePlacementStrategy: LINEAR_SEGMENTS
---
erDiagram
    {% multi_lang_include snowflake_mermaid/email.md %}

    CHANGELOGS_CANVAS_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
        string conversion_behaviors
        string variations
    }
    SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {
        string Id FK
        string time
        string app_group_id
        string type
        string api_step_id
        string experiment_splits
        string conversion_behaviors
        string name
    }
    SNAPSHOTS_CANVAS_STEP_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
        string actions
    }
    SNAPSHOTS_CANVAS_VARIATION_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
    }
    SNAPSHOTS_EXPERIMENT_STEP_SHARED {
        string Id FK
        string time
        string app_group_id
        string type
        string api_step_id
        string experiment_splits
        string conversion_behaviors
        string name
    }

    CHANGELOGS_CAMPAIGN_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
        string conversion_behaviors
        string actions
    }
    SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {
        string Id FK
        string time
        string app_group_id
        string api_id
        string name
    }

    CAMPAIGN_ENROLLMENT_EVENT {
        string id PK
        string campaign_id FK
        string campaign_updated_at FK
        string user_id FK
        string external_user_id
        string message_variation_id
        string send_id
        string time
        string timezone
    }
    CAMPAIGN_CONVERSION_EVENT {
        string id PK
        string campaign_id FK
        string campaign_updated_at FK
        string conversion_behavior_index FK
        string message_variation_id FK
        string user_id FK
        string event_type
        string app_id
        string external_user_id
        string send_id
        string time
        string timezone
    }

    CANVAS_VARIATION {
        string id PK
        string name PK
        string canvas_id FK
        string canvas_updated_at FK
    }
    CANVAS_STEP {
        string id PK
        string canvas_id FK
        string canvas_updated_at FK
        string canvas_step_name
        string channel_android_push
        string channel_content_cards
        string channel_email
        string channel_ios_push
        string channel_in_app_message
        string channel_sms
        string channel_web_push
        string channel_webhook
    }

    CANVAS_ENTRY_EVENT {
        string id PK
        string canvas_id FK
        string canvas_updated_at FK
        string canvas_step_id FK
        string canvas_step_updated_at FK
        string canvas_variation_id FK
        string user_id FK
        string event_type
        string external_user_id
        string in_control_group
        string time
        string timezone
    }
    CANVAS_EXPERIMENT_STEP_ENTRY_EVENT {
        string id PK
        string canvas_id FK
        string canvas_updated_at FK
        string canvas_step_id FK
        string canvas_step_updated_at FK
        string canvas_variation_id FK
        string user_id FK
        string event_type
        string experiment_split_id
        string experiment_split_name
        string experiment_step_id
        string external_user_id
        string in_control_group
        string time
    }
    CANVAS_EXIT_EVENT {
        string id PK
        string canvas_id FK
        string canvas_updated_at FK
        string canvas_step_id FK
        string canvas_step_updated_at FK
        string canvas_variation_id FK
        string user_id FK
        string app_group_id
        string event_type
        string time
    }

    CANVAS_EXPERIMENT_STEP_CONVERSION_EVENT {
        string id PK
        string canvas_id FK
        string canvas_updated_at FK
        string canvas_step_id FK
        string canvas_step_updated_at FK
        string canvas_conversion_behaviour_id FK
        string canvas_variation_id FK
        string user_id FK
        string app_id
        string event_type
        string experiment_step_id
        string experiment_split_id
        string experiment_split_name
        string time
    }
    CANVAS_CONVERSION_EVENT {
        string id PK
        string canvas_id FK
        string canvas_updated_at FK
        string canvas_step_id FK
        string canvas_conversion_behaviour_id FK
        string canvas_variation_id FK
        string user_id FK
        string event_type
        string app_id
        string external_user_id
        string time
        string timezone
    }

    %% Relationships for Group Labels
    GROUP_1["Campaign Snapshots and Log"] { }
    CHANGELOGS_CAMPAIGN_SHARED ||--o{ GROUP_1 : joins
    SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED ||--o{ GROUP_1 : joins
    GROUP_1 ||--o{ EVENT : joins

    GROUP_2["Campaign Events"] { }
    CAMPAIGN_ENROLLMENT_EVENT ||--o{ GROUP_2 : joins
    CAMPAIGN_CONVERSION_EVENT ||--o{ GROUP_2 : joins
    GROUP_2 ||--o{ EVENT : joins

    GROUP_3["Canvas Events"] { }
    CANVAS_ENTRY_EVENT ||--o{ GROUP_3 : joins
    CANVAS_EXPERIMENT_STEP_ENTRY_EVENT ||--o{ GROUP_3 : joins
    CANVAS_EXIT_EVENT ||--o{ GROUP_3 : joins
    GROUP_3 ||--o{ EVENT : joins

    GROUP_4["Canvas Steps"] { }
    CANVAS_VARIATION ||--o{ GROUP_4 : joins
    CANVAS_STEP ||--o{ GROUP_4 : joins
    GROUP_4 ||--o{ EVENT : joins

    GROUP_5["Canvas Experiments"] { }
    CANVAS_EXPERIMENT_STEP_CONVERSION_EVENT ||--o{ GROUP_5 : joins
    CANVAS_CONVERSION_EVENT ||--o{ GROUP_5 : joins
    GROUP_5 ||--o{ EVENT : joins

    GROUP_6["Canvas Snapshots and Log"] { }
    CHANGELOGS_CANVAS_SHARED ||--o{ GROUP_6 : joins
    SNAPSHOTS_CANVAS_FLOW_STEP_SHARED ||--o{ GROUP_6 : joins
    SNAPSHOTS_CANVAS_STEP_SHARED ||--o{ GROUP_6 : joins
    SNAPSHOTS_CANVAS_VARIATION_SHARED ||--o{ GROUP_6 : joins
    SNAPSHOTS_EXPERIMENT_STEP_SHARED ||--o{ GROUP_6 : joins
    GROUP_6 ||--o{ EVENT : joins
```

- `PK` ＝主キー
- `FK` = 外部キー

## リレーションシップテーブル

### `ABORT_SHARED`

```json
// USERS_MESSAGES_EMAIL_ABORT_SHARED
// An originally scheduled email message was aborted for some reason.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "IP_POOL": "IP pool from which the email send was made",
        "ABORT_TYPE": "Type of abort, one of ['liquid_abort_message', 'quiet_hours', 'rate_limit']",
        "ABORT_LOG": "[PII] Log message describing abort details (up to 128 chars)",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `BOUNCE_SHARED`

```json
// USERS_MESSAGES_EMAIL_BOUNCE_SHARED
// An Email Service Provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "SENDING_IP": "IP address from which the email send was made",
        "IP_POOL": "IP pool from which the email send was made",
        "BOUNCE_REASON": "[PII] The SMTP reason code and user friendly message received for this bounce event",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "IS_DROP": "Indicates that this event counts as a drop event",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `CLICK_SHARED`

```json
// USERS_MESSAGES_EMAIL_CLICK_SHARED
// When a user clicks a link in an email.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "URL": "URL that the user clicked on",
        "USER_AGENT": "User agent on which the spam report occurred",
        "IP_POOL": "IP pool from which the email send was made",
        "LINK_ALIAS": "Alias associated with this link ID",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "IS_AMP": "Indicates that this is an AMP event",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to",
        "LINK_ID": "Unique ID for the link which was clicked, as created by Braze"
    }
}
```

### `DEFERRAL_SHARED`

```json
// USERS_MESSAGES_EMAIL_DEFERRAL_SHARED
// When an email deferred.

{
    "primary_key": {
        "ID": "Globally unique ID for this event"
    },
    "foreign_keys": {
        "USER_ID": "Braze user ID of the user who performed this event",
        "EXTERNAL_USER_ID": "[PII] External ID of the user",
        "APP_GROUP_ID": "BSON ID of the app group this user belongs to",
        "APP_GROUP_API_ID": "API ID of the app group this user belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "RECIPIENT_DOMAIN": "Receipient's email domain",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "IP_POOL": "IP pool from which the email send was made",
        "SENDING_IP": "IP address from which the email send was made",
        "TIMEZONE": "Time zone of the user",
        "DEFERRAL_REASON": "[PII] The SMTP reason code and user friendly message received for this deferral event",
        "ATTEMPT_COUNT": "Number of attempts made to send the message",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `DELIVERY_SHARED`

```json
// USERS_MESSAGES_EMAIL_DELIVERY_SHARED
// When an email is delivered.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "SENDING_IP": "IP address from which the email send was made",
        "IP_POOL": "IP pool from which the email send was made",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `MARKASSPAM_SHARED`

```json
// USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED
// When an email is marked as spam.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "USER_AGENT": "User agent on which the spam report occurred",
        "IP_POOL": "IP pool from which the email send was made",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `OPEN_SHARED`

```json
// USERS_MESSAGES_EMAIL_OPEN_SHARED
// When a user begins opens an email.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "USER_AGENT": "User agent on which the spam report occurred",
        "IP_POOL": "IP pool from which the email send was made",
        "MACHINE_OPEN": "Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "IS_AMP": "Indicates that this is an AMP event",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `SEND_SHARED`

```json
// USERS_MESSAGES_EMAIL_SEND_SHARED
// When we send an email to a user.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "IP_POOL": "IP pool from which the email send was made",
        "MESSAGE_EXTRAS": "[PII] A JSON string of the tagged key-value pairs during liquid rendering",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `SOFTBOUNCE_SHARED`

```json
// USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED
// When an email soft bounces.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "SENDING_IP": "IP address from which the email send was made",
        "IP_POOL": "IP pool from which the email send was made",
        "BOUNCE_REASON": "[PII] The SMTP reason code and user friendly message received for this bounce event",
        "ESP": "ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
        "FROM_DOMAIN": "Sending domain for the email",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

### `UNSUBSCRIBE_SHARED`

```json
// USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED
// When a user unsubscribes from email.

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
        "DISPATCH_ID": "ID of the dispatch this message belongs to",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "CANVAS_STEP_MESSAGE_VARIATION_API_ID": "API ID of the Canvas step message variation this user received"
    },
    "native_keys": {
        "TIME": "UNIX timestamp at which the event happened",
        "GENDER": "[PII] Gender of the user",
        "COUNTRY": "[PII] Country of the user",
        "TIMEZONE": "Time zone of the user",
        "LANGUAGE": "[PII] Language of the user",
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "IP_POOL": "IP pool from which the email send was made",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

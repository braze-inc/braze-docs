## Beziehungs-Tabellen

### `STATECHANGE_SHARED`

```json
// USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED
// When a user is subscribed or unsubscribed to/from a subscription group.

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
        "APP_API_ID": "API ID of the app on which this event occurred",
        "CAMPAIGN_ID": "BSON ID of the campaign this event belongs to",
        "CAMPAIGN_API_ID": "API ID of the campaign this event belongs to",
        "MESSAGE_VARIATION_API_ID": "API ID of the message variation this user received",
        "CANVAS_ID": "BSON ID of the Canvas this event belongs to",
        "CANVAS_API_ID": "API ID of the Canvas this event belongs to",
        "CANVAS_VARIATION_API_ID": "API ID of the Canvas variation this event belongs to",
        "CANVAS_STEP_API_ID": "API ID of the Canvas step this event belongs to",
        "SUBSCRIPTION_GROUP_API_ID": "Subscription group API ID",
        "DISPATCH_ID": "ID of the dispatch this message belongs to"
    },
    "native_keys": {
        "EMAIL_ADDRESS": "[PII] Email address of the user",
        "PHONE_NUMBER": "[PII] Phone number of the user in e.164 format (for example +14155552671)",
        "CHANNEL": "Channel this event belongs to",
        "SUBSCRIPTION_STATUS": "Subscription status: 'Subscribed' or 'Unsubscribed'",
        "TIME": "UNIX timestamp at which the event happened",
        "TIMEZONE": "Time zone of the user",
        "STATE_CHANGE_SOURCE": "Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
        "CHANNEL_IDENTIFIER": "[PII] The user's identifier on the channel the event is for.",
        "SF_CREATED_AT": "when this event was picked up by the Snowpipe",
        "SEND_ID": "Message send ID this message belongs to"
    }
}
```

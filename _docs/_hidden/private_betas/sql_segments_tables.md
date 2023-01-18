---
nav_title: "SQL Segment Extensions Tables"
permalink: "/sql_segments_tables/"
hidden: true
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL Segment Extensions Tables

Table | Description
------|------------
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | when a user makes a performs a custom event
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | when a user installs an app and we attribute it to a partner
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | when a user records a location
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | when a user makes a purchase
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | when a user uninstalls an app
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | when a user upgrades the app
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | when a user has their first session
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | when a user views the news feed
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | when a user ends a session on an app
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | when a user begins a session on an app
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | When a user triggers a geofenced area (e.g. when they enter/exit a geofence). This event was batched with other events and received through the standard events endpoint, and therefore may not have been received by the endpoint in real-time.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | When a user triggers a geofenced area (e.g. when they enter/exit a geofence). This event was received through the dedicated Geofence endpoint, and is therefore received in real-time as soon as a user's device detects that it has triggered a geofence. In addition, due to rate-limiting on the geofence endpoint, it is possible that some geofence events are not reflected as a RecordEvent. All geofence events, however, are represented by DataEvent (but potentially with some delay due to batching).
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | when a user is subscribed or unsubscribed globally from a channel such as email
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | when a user is subscribed or unsubscribed to/from a subscription group
[USERS_CAMPAIGNS_ABORT_SHARED](#USERS_CAMPAIGNS_ABORT_SHARED) | An originally scheduled campaign message was aborted for some reason.
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | when a user converts for a campaign
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | when a user is enrolled in the control group for a campaign
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | when a user gets frequency capped for a campaign
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | when a user generates revenue with in the primary conversion period
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | An originally scheduled contentcard message was aborted for some reason.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | when a user clicks a content card
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | when a user dismisses a content card
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | when a user views a content card
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | when we send a content card to a user
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | An originally scheduled email message was aborted for some reason.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | An Email Service Provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | when a user clicks a link in an email
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | when an email is delivered
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | when an email is marked as spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | when a user begins opens an email
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | when we send an email to a user
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | when an email soft bounces
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | when a user unsubscribes from email
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | An originally scheduled inappmessage message was aborted for some reason.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | when a user clicks an in app message
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | when a user views an in app message
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | An originally scheduled newsfeedcard message was aborted for some reason.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | when a user clicks a news feed card
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | when a user views a a news feed card
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | An originally scheduled pushnotification message was aborted for some reason.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | when a push notification bounces
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | when a user opens the app after receiving a notification without clicking on the notification
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | when a user receives a push notification while the app is open
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | when a user opens a push notification or clicks a push notification button (including a CLOSE button that does NOT open the app)
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | when we send a push notification to a user
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | An originally scheduled sms message was aborted for some reason.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | when a SMS message is sent to carrier
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | when a SMS message is delivered
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | when Braze is unable to deliver the SMS message to the SMS service provider
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | when a SMS message is received from a user
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | when a SMS message is not delivered to a user
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | when a SMS message is sent
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | when a user clicks a Braze shortened URL included in an SMS message
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | An originally scheduled webhook message was aborted for some reason.
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | when we send a webhook for a user


### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed the event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which this action occurred
`time` | `int` | unix timestamp at which the user performed the event
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the custom event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`name` | `string` | name of the custom event
`properties` | `string` | custom properties of the event stored as a JSON encoded string
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that installed
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the user installed
`source` | `string` | the source of the attribution

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that records the location
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which this location was recorded
`time` | `int` | unix timestamp at which the location was recorded
`latitude` | `float` | [PII] latitude of recorded location
`longitude` | `float` | [PII] longitude of recorded location
`altitude` | `null, float` | [PII] altitude of recorded location
`ll_accuracy` | `null, float` | latitude/longitude accuracy of recorded location
`alt_accuracy` | `null, float` | altitude accuracy of recorded location
`device_id` | `null, string` | id of the device on which the location was recorded
`sdk_version` | `null, string` | version of the Braze SDK in use when the location was recorded
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that made a purchase
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which the purchase occurred
`time` | `int` | unix timestamp at which the user made the purchase
`device_id` | `null, string` | id of the device on which the purchase occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the purchase
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`product_id` | `string` | id of the product purchased
`price` | `float` | price of the purchase
`currency` | `string` | currency of the purchase
`properties` | `string` | custom properties of the purchase stored as a JSON encoded string
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that uninstalled
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app that was uninstalled
`time` | `int` | unix timestamp at which the user uninstalled

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that upgraded the app
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app the user upgraded
`time` | `int` | unix timestamp at which the user upgraded the app
`device_id` | `null, string` | id of the device on which the user upgraded the app
`sdk_version` | `null, string` | version of the Braze SDK in use
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`old_app_version` | `null, string` | old version of the app
`new_app_version` | `null, string` | new version of the app

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performs this action
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which this session occurred
`time` | `int` | unix timestamp at which the session started
`session_id` | `string` | uuid of the session
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the session occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the session
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that viewed the news feed
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which the user viewed the news feed
`time` | `int` | unix timestamp at which the user viewed the news feed
`device_id` | `null, string` | id of the device on which the impression occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the impression
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performs this action
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which this session occurred
`time` | `int` | unix timestamp at which the session ended
`duration` | `null, float` | duration of the session
`session_id` | `string` | uuid of the session
`device_id` | `null, string` | id of the device on which the session occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the session
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performs this action
`external_user_id` | `null, string` | [PII] external user id of the user
`app_api_id` | `null, string` | API ID of the app on which this session occurred
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the session started
`session_id` | `string` | uuid of the session
`device_id` | `null, string` | id of the device on which the session occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the session
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed the event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which this action occurred
`time` | `int` | unix timestamp at which the user performed the event
`device_id` | `null, string` | id of the device on which the custom event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`event_type` | `string` | What kind of geofence event was triggered. (e.g. 'enter' or 'exit')
`location_set_id` | `string` | The ID of the location set of the geofence that was triggered
`geofence_id` | `string` | The ID of the geofence that was triggered

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed the event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | API ID of the app on which this action occurred
`time` | `int` | unix timestamp at which the user performed the event
`device_id` | `null, string` | id of the device on which the custom event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`event_type` | `string` | What kind of geofence event was triggered. (e.g. 'enter' or 'exit')
`location_set_id` | `string` | The ID of the location set of the geofence that was triggered
`geofence_id` | `string` | The ID of the geofence that was triggered

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user affected
`external_user_id` | `null, string` | [PII] external user id of the user
`email_address` | `null, string` | [PII] email address of the user
`state_change_source` | `null, string` | source of the state change, e.g: REST, SDK, Dashboard, etc.
`subscription_status` | `string` | subscription status: 'Subscribed' or 'Unsubscribed'
`channel` | `null, string` | channel of the global subscription state such as email
`time` | `int` | unix timestamp at which the subscription state changed
`timezone` | `null, string` | timezone of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`app_api_id` | `null, string` | api id of the app the event belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | api id of the campaign this event belongs to
`message_variation_api_id` | `null, string` | api id of the message variation this event belongs to
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | api id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | api id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | api id of the canvas step this event belongs to
`send_id` | `null, string` | message send ID this subscription state change action originated from

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user affected
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`email_address` | `null, string` | [PII] email address of the user
`phone_number` | `null, string` | [PII] phone number of the user in e164 format
`app_api_id` | `null, string` | api id of the app the event belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | api id of the campaign this event belongs to
`message_variation_api_id` | `null, string` | api id of the message variation this event belongs to
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | api id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | api id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | api id of the canvas step this event belongs to
`subscription_group_api_id` | `string` | subscription group api id
`channel` | `null, string` | channel: 'email' or 'sms', depending on the channel type of the subscription group
`subscription_status` | `string` | subscription status: 'Subscribed' or 'Unsubscribed'
`time` | `int` | unix timestamp at which the subscription state changed
`timezone` | `null, string` | timezone of the user
`send_id` | `null, string` | message send ID this subscription state change action originated from
`state_change_source` | `null, string` | source of the state change, e.g: REST, SDK, Dashboard, etc.

### USERS_CAMPAIGNS_ABORT_SHARED {#USERS_CAMPAIGNS_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`channel` | `null, string` | channel this event belongs to
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`conversion_behavior_index` | `null, int` | index of the conversion behavior
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`channel` | `null, string` | channel this event belongs to
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`revenue` | `long` | the amount of USD revenue in cents generated

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`content_card_id` | `string` | id of the card that generated this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`content_card_id` | `string` | id of the card that generated this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`content_card_id` | `string` | id of the card that generated this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`content_card_id` | `string` | id of the card that generated this event

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`ip_pool` | `null, string` | IP Pool from which the email send was made
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`sending_ip` | `null, string` | IP address from which the email send was made
`ip_pool` | `null, string` | IP Pool from which the email send was made
`bounce_reason` | `null, string` | [PII] The SMTP reason code and user friendly message received for this bounce event
`esp` | `null, string` | ESP related to the event (Sparkpost or Sendgrid)
`from_domain` | `null, string` | sending domain for the email
`is_drop` | `null, boolean` | indicates that this event counts as a drop event

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`url` | `null, string` | URL that the user clicked on
`user_agent` | `null, string` | user agent on which the click occurred
`ip_pool` | `null, string` | IP Pool from which the email send was made
`link_id` | `null, string` | unique ID for the link which was clicked, as created by Braze
`link_alias` | `null, string` | alias associated with this link ID
`esp` | `null, string` | ESP related to the event (Sparkpost or Sendgrid)
`from_domain` | `null, string` | sending domain for the email
`is_amp` | `null, boolean` | indicates that this is an AMP event

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`sending_ip` | `null, string` | IP address from which the email was sent
`ip_pool` | `null, string` | IP Pool from which the email send was made
`esp` | `null, string` | ESP related to the event (Sparkpost or Sendgrid)
`from_domain` | `null, string` | sending domain for the email

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`user_agent` | `null, string` | user agent on which the spam report occurred
`ip_pool` | `null, string` | IP Pool from which the email send was made
`esp` | `null, string` | ESP related to the event (Sparkpost or Sendgrid)
`from_domain` | `null, string` | sending domain for the email

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`user_agent` | `null, string` | user agent on which the open occurred
`ip_pool` | `null, string` | IP Pool from which the email send was made
`machine_open` | `null, string` | Populated to 'true' if the open event is triggered without user engagement, e.g. by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.
`esp` | `null, string` | ESP related to the event (Sparkpost or Sendgrid)
`from_domain` | `null, string` | sending domain for the email
`is_amp` | `null, boolean` | indicates that this is an AMP event

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`ip_pool` | `null, string` | IP Pool from which the email send was made

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`sending_ip` | `null, string` | IP address from which the email send was made
`ip_pool` | `null, string` | IP Pool from which the email send was made
`bounce_reason` | `null, string` | [PII] The SMTP reason code and user friendly message received for this bounce event
`esp` | `null, string` | ESP related to the event (Sparkpost or Sendgrid)
`from_domain` | `null, string` | sending domain for the email

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`email_address` | `string` | [PII] email address of the user
`ip_pool` | `null, string` | IP Pool from which the email send was made

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`card_api_id` | `null, string` | API ID of the card
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`version` | `string` | which version of in app message, legacy or triggered
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`card_api_id` | `null, string` | API ID of the card
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`version` | `string` | which version of in app message, legacy or triggered
`button_id` | `null, string` | id of the button clicked, if this click represents a click on a button
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`card_api_id` | `null, string` | API ID of the card
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`version` | `string` | which version of in app message, legacy or triggered
`ad_id` | `null, string` | [PII] Advertising identifier
`ad_id_type` | `null, string` | One of 'ios_idfa', 'google_ad_id', 'windows_ad_id', OR 'roku_ad_id'
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`card_api_id` | `null, string` | API ID of the card
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`card_api_id` | `null, string` | API ID of the card
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`card_api_id` | `null, string` | API ID of the card
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that we made a delivery attempt to
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`platform` | `string` | platform of the device
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`push_token` | `null, string` | push token that bounced
`device_id` | `null, string` | device_id that we made a delivery attempt to that bounced
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`platform` | `null, string` | platform of the device
`ad_id` | `null, string` | [PII] advertising id of the device that we made a delivery attempt to
`ad_id_type` | `null, string` | type of the advertising id
`ad_tracking_enabled` | `null, boolean` | whether or not tracking is enabled for advertising

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`ad_id` | `null, string` | [PII] advertising id of the device that we made a delivery attempt to
`ad_id_type` | `null, string` | type of the advertising id
`ad_tracking_enabled` | `null, boolean` | whether or not tracking is enabled for advertising

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`device_id` | `null, string` | id of the device on which the event occurred
`sdk_version` | `null, string` | version of the Braze SDK in use during the event
`platform` | `null, string` | platform of the device
`os_version` | `null, string` | version of the operating system of the device
`device_model` | `null, string` | model of the device
`resolution` | `null, string` | resolution of the device
`carrier` | `null, string` | carrier of the device
`browser` | `null, string` | browser of the device
`button_string` | `null, string` | identifier (button_string) of the push notification button clicked. null if not from a button click
`button_action_type` | `null, string` | Action type of the push notification button. One of [URI, DEEP_LINK, NONE, CLOSE, SHARE]. null if not from a button click
`slide_id` | `null, string` | slide identifier of the push carousel slide user clicks on
`slide_action_type` | `null, string` | action type of the push carousel slide
`ad_id` | `null, string` | [PII] advertising id of the device that we made a delivery attempt to
`ad_id_type` | `null, string` | type of the advertising id
`ad_tracking_enabled` | `null, boolean` | whether or not tracking is enabled for advertising

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`push_token` | `null, string` | push token that we made a delivery attempt to
`device_id` | `null, string` | device_id that we made a delivery attempt to
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`app_api_id` | `null, string` | API ID of the app on which this event occurred
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`platform` | `string` | platform of the device
`ad_id` | `null, string` | [PII] advertising id of the device that we made a delivery attempt to
`ad_id_type` | `null, string` | type of the advertising id
`ad_tracking_enabled` | `null, boolean` | whether or not tracking is enabled for advertising

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`subscription_group_api_id` | `null, string` | external ID of the subscription group
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`to_phone_number` | `null, string` | [PII] phone number of the recipient
`from_phone_number` | `null, string` | phone number from which the SMS message was sent
`subscription_group_api_id` | `null, string` | external ID of the subscription group

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`to_phone_number` | `null, string` | [PII] phone number of the recipient
`from_phone_number` | `null, string` | phone number from which the SMS message was sent
`subscription_group_api_id` | `null, string` | external ID of the subscription group

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`to_phone_number` | `null, string` | [PII] phone number of the recipient
`subscription_group_api_id` | `null, string` | external ID of the subscription group
`error` | `null, string` | error name
`provider_error_code` | `null, string` | error code from SMS service provider

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `null, string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`app_group_api_id` | `null, string` | API ID of the app group associated with the inbound phone number
`time` | `int` | unix timestamp at which the event happened
`user_phone_number` | `string` | [PII] the user's phone number from which the message was received
`subscription_group_id` | `null, string` | id of the subscription group targeted for this SMS message
`subscription_group_api_id` | `null, string` | API id of the subscription group targeted for this SMS message
`inbound_phone_number` | `string` | the inbound number that the message was sent to
`action` | `string` | Action taken in respons to this message. (e.g. Subscribed, Unsubscribed or None).
`message_body` | `string` | response from the user
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | media urls from the user
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this event belongs to
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this event belongs to

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`to_phone_number` | `null, string` | [PII] phone number of the recipient
`from_phone_number` | `null, string` | phone number from which the SMS message was sent
`subscription_group_api_id` | `null, string` | external ID of the subscription group
`error` | `null, string` | error name
`provider_error_code` | `null, string` | error code from SMS service provider

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`to_phone_number` | `null, string` | [PII] phone number of the recipient
`subscription_group_api_id` | `null, string` | external ID of the subscription group
`category` | `null, string` | Keyword Category Name, only populated for auto-reply messages: 'Opt-in', 'Opt-out', 'Help', or custom value

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique ID for this event
`user_id` | `null, string` | BSON ID of the user targeted by short_url, null if short_url did not use user click tracking
`external_user_id` | `null, string` | [PII] external ID of the user targeted by short_url if one exists, null if short_url did not use user click tracking
`app_group_api_id` | `null, string` | API ID of the app group used to generate short_url
`time` | `int` | unix timestamp at which short_url was clicked
`timezone` | `null, string` | timezone of the user
`campaign_id` | `null, string` | BSON ID of the campaign short_url was generated for, null if not from a campaign
`campaign_api_id` | `null, string` | API ID of the campaign short_url was generated for, null if not from a campaign
`message_variation_api_id` | `null, string` | API ID of the message variation short_url was generated for, null if not from a campaign
`canvas_id` | `null, string` | BSON ID of the canvas short_url was generated for, null if not from a canvas
`canvas_api_id` | `null, string` | API ID of the canvas short_url was generated for, null if not from a canvas
`canvas_variation_api_id` | `null, string` | API ID of the canvas variation short_url was generated for, null if not from a canvas
`canvas_step_api_id` | `null, string` | API ID of the canvas step short_url was generated for, null if not from a canvas
`canvas_step_message_variation_api_id` | `null, string` | API ID of the canvas step message variation short_url was generated for, null if not from a canvas
`url` | `string` | original URL contained in message that is redirected to by short_url
`short_url` | `string` | shortened URL that was clicked
`user_agent` | `null, string` | user agent requesting short_url
`user_phone_number` | `string` | [PII] the user's phone number

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user
`abort_type` | `null, string` | type of abort, one of: "liquid_abort_message", "quiet_hours", "rate_limit"
`abort_log` | `null, string` | [PII] log message describing abort details (MAX: 128 CHARS)

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | globally unique id for this event
`user_id` | `string` | BSON id of the user that performed this event
`external_user_id` | `null, string` | [PII] external user id of the user
`device_id` | `null, string` | device_id that is tied to this user if user is anonymous
`app_group_api_id` | `null, string` | API ID of the app group this user belongs to
`time` | `int` | unix timestamp at which the event happened
`dispatch_id` | `null, string` | ID of the dispatch this message belongs to
`send_id` | `null, string` | message send ID this message belongs to
`campaign_id` | `null, string` | internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null, string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null, string` | API ID of the message variation this user received
`canvas_id` | `null, string` | internal-use Braze ID of the canvas this event belongs to
`canvas_api_id` | `null, string` | API id of the canvas this event belongs to
`canvas_variation_api_id` | `null, string` | API id of the canvas variation this event belongs to
`canvas_step_api_id` | `null, string` | API id of the canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null, string` | API id of the canvas step message variation this user received
`gender` | `null, string` | [PII] gender of the user
`country` | `null, string` | [PII] country of the user
`timezone` | `null, string` | timezone of the user
`language` | `null, string` | [PII] language of the user

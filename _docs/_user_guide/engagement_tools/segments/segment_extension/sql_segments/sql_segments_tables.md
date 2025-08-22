---
nav_title: "SQL table reference"
article_title: SQL Table Reference
page_order: 3
page_type: reference
toc_headers: h2
description: "This article contains tables and columns available to be queried in the Query Builder or when generating SQL Segment Extensions."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL table reference

This page is a reference of tables and columns available to be queried in the [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) or when generating [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

## Table of contents

Table | Description
------|------------
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | When a user performs a custom event
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | When a user installs an app and we attribute it to a partner
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | When a user records a location
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | When a user makes a purchase
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | When a user uninstalls an app
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | When a user upgrades the app
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | When a user has their first session
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | When a user views the News Feed
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | When a user ends a session on an app
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | When a user begins a session on an app
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | When a user triggers a geofenced area (for example, when they enter or exit a geofence). This event was batched with other events and received through the standard events endpoint, and therefore may not have been received by the endpoint in real time.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | When a user triggers a geofenced area (for example, when they enter or exit a geofence). This event was received through the dedicated geofence endpoint and is therefore received in real-time as soon as a user's device detects that it has triggered a geofence. <br><br>In addition, due to rate limiting on the geofence endpoint, it is possible that some geofence events are not reflected as a RecordEvent. All geofence events, however, are represented by DataEvent (but potentially with some delay due to batching).
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | When a user is subscribed or unsubscribed globally from a channel such as email
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | When a user is subscribed or unsubscribed to or from a subscription group
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | When a user converts for a campaign
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | When a user is enrolled in the control group for a campaign
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | When a user gets frequency capped for a campaign
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | When a user generates revenue within the primary conversion period
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | When a user progresses to a Canvas step
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | When a user converts for a Canvas conversion event
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | When a user enters a Canvas
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | When a user exits a Canvas because they match audience exit criteria
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | When a user exits a Canvas because they performed an exception event
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | When a user converts for a Canvas Experiment step
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | When a user enters an Experiment step path
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | When a user gets frequency capped for a Canvas step
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | When a user generates revenue within the primary conversion event period
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | An originally scheduled Content Card message was aborted for some reason.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | When a user clicks a Content Card
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | When a user dismisses a Content Card
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | When a user views a Content Card
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | When we send a Content Card to a user
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | An originally scheduled email message was aborted for some reason.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | An Email Service Provider returned a hard bounce. A hard bounce signifies a permanent deliverability failure.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | When a user clicks a link in an email
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | When an email is delivered
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | When an email is marked as spam
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | When a user opens an email
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | When we send an email to a user
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | When an email soft bounces
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | When a user unsubscribes from email
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | An originally scheduled in-app message was aborted for some reason.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | When a user clicks an in-app message
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | When a user views an in-app message
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | An originally scheduled News Feed card message was aborted for some reason.
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | When a user clicks a News Feed card
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | When a user views a News Feed card
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | An originally scheduled push notification message was aborted for some reason.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | When a push notification bounces
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | When a user opens the app after receiving a notification without clicking on the notification
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | When a user receives a push notification while the app is open
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | When a user opens a push notification or clicks a push notification button (including a CLOSE button that does NOT open the app). <br><br> Push button actions have multiple outcomes. No, Decline, and Cancel actions are "clicks", and Accept actions are "opens". Both are represented in this table, but they can be distinguished in the **BUTTON_ACTION_TYPE** column. For example, a query can be used to group by a `BUTTON_ACTION_TYPE` that is not No, Decline, or Cancel.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | When we send a push notification to a user
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | An originally scheduled SMS message was aborted for some reason.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | When an SMS message is sent to the carrier
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | When an SMS message is delivered
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | When Braze is unable to deliver the SMS message to the SMS service provider
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | When an SMS message is received from a user
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | When an SMS message is not delivered to a user
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | When an SMS message is sent
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | When a user clicks a Braze shortened URL included in an SMS message
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | An originally scheduled webhook message was aborted for some reason
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | When we send a webhook for a user
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | An originally scheduled WhatsApp message was aborted for some reason
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |When a WhatsApp message is delivered
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | When a WhatsApp message is not delivered to a user
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | When a WhatsApp message is received from a user
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | When a user opens a WhatsApp message
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | When we send a WhatsApp message for a user
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | When a user's random bucket number is changed
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | When a user is deleted by a customer request
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | When a user is merged with another user's profile and the original profile is orphaned


## Behaviors

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed the event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this action occurred
`time` | `int` | Unix timestamp at which the user performed the event
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the custom event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`name` | `string` | Name of the custom event
`properties` | `string` | Custom properties of the event stored as a JSON encoded string
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that installed
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the user installed
`source` | `string` | the source of the attribution
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that records the location
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this location was recorded
`time` | `int` | Unix timestamp at which the location was recorded
`latitude` | `float` | [PII] Latitude of recorded location
`longitude` | `float` | [PII] Longitude of recorded location
`altitude` | `null, float` | [PII] altitude of recorded location
`ll_accuracy` | `null, float` | latitude and longitude accuracy of recorded location
`alt_accuracy` | `null, float` | altitude accuracy of recorded location
`device_id` | `null,`&nbsp;`string` | ID of the device on which the location was recorded
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use when the location was recorded
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that made a purchase
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which the purchase occurred
`time` | `int` | Unix timestamp at which the user made the purchase
`device_id` | `null,`&nbsp;`string` | ID of the device on which the purchase occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the purchase
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`product_id` | `string` | ID of the product purchased
`price` | `float` | Price of the purchase
`currency` | `string` | Currency of the purchase
`properties` | `string` | Custom properties of the purchase stored as a JSON encoded string
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that uninstalled
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app that was uninstalled
`time` | `int` | Unix timestamp at which the user uninstalled
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that upgraded the app
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app the user upgraded
`time` | `int` | Unix timestamp at which the user upgraded the app
`device_id` | `null,`&nbsp;`string` | ID of the device on which the user upgraded the app
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`old_app_version` | `null,`&nbsp;`string` | Old version of the app
`new_app_version` | `null,`&nbsp;`string` | New version of the app
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performs this action
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this session occurred
`time` | `int` | Unix timestamp at which the session started
`session_id` | `string` | UUID of the session
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the session occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the session
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that viewed the News Feed
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which the user viewed the News Feed
`time` | `int` | Unix timestamp at which the user viewed the News Feed
`device_id` | `null,`&nbsp;`string` | ID of the device on which the impression occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the impression
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performs this action
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this session occurred
`time` | `int` | Unix timestamp at which the session ended
`duration` | `null, float` | Duration of the session
`session_id` | `string` | UUID of the session
`device_id` | `null,`&nbsp;`string` | ID of the device on which the session occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the session
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performs this action
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this session occurred
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the session started
`session_id` | `string` | UUID of the session
`device_id` | `null,`&nbsp;`string` | ID of the device on which the session occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the session
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed the event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this action occurred
`time` | `int` | Unix timestamp at which the user performed the event
`device_id` | `null,`&nbsp;`string` | ID of the device on which the custom event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`event_type` | `string` | What kind of geofence event was triggered. (for example, 'enter' or 'exit')
`location_set_id` | `string` | The ID of the location set of the geofence that was triggered
`geofence_id` | `string` | The ID of the geofence that was triggered
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed the event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this action occurred
`time` | `int` | Unix timestamp at which the user performed the event
`device_id` | `null,`&nbsp;`string` | ID of the device on which the custom event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`event_type` | `string` | What kind of geofence event was triggered. (for example, 'enter' or 'exit')
`location_set_id` | `string` | The ID of the location set of the geofence that was triggered
`geofence_id` | `string` | The ID of the geofence that was triggered
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user affected
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`email_address` | `null,`&nbsp;`string` | [PII] email address of the user
`state_change_source` | `null,`&nbsp;`string` | source of the state change (REST, SDK, Dashboard, etc)
`subscription_status` | `string` | Subscription status: 'Subscribed' or 'Unsubscribed'
`channel` | `null,`&nbsp;`string` | Channel of the global subscription state such as email
`time` | `int` | Unix timestamp at which the subscription state changed
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`app_api_id` | `null,`&nbsp;`string` | API ID of the app the event belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this event belongs to
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this subscription state change action originated from
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user affected
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`email_address` | `null,`&nbsp;`string` | [PII] email address of the user
`phone_number` | `null,`&nbsp;`string` | [PII] phone number of the user in e164 format
`app_api_id` | `null,`&nbsp;`string` | API ID of the app the event belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this event belongs to
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`channel` | `null,`&nbsp;`string` | Channel: 'email' or 'sms', depending on the channel type of the subscription group
`subscription_status` | `string` | Subscription status: 'Subscribed' or 'Unsubscribed'
`time` | `int` | Unix timestamp at which the subscription state changed
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`send_id` | `null,`&nbsp;`string` | Message send ID this subscription state change action originated from
`state_change_source` | `null,`&nbsp;`string` | Source of the state change (REST, SDK, Dashboard, etc)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Campaigns

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`conversion_behavior_index` | `null, int` | Index of the conversion behavior
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`channel` | `null,`&nbsp;`string` | Channel this event belongs to
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`revenue` | `long` | The amount of USD revenue in cents generated
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Field                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globally unique ID for this event                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] External user ID of the user                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                                                                      |
| `canvas_id`                            | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to        |         
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                                                                 |
| `progression_type`                     | `string`,&nbsp;`null`    | Type of step progression event |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Whether this is entry into a first step in a Canvas        |
| `exit_reason`                          | `string`,&nbsp;`null`    | If this is an exit, the reason a user exited the canvas during the step                  |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Unique identifier for this instance of a user in a Canvas  |
| `next_step_id`                         | `string`,&nbsp;`null`    | BSON ID of the next step in the canvas |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | API ID of the next step in the Canvas |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Field                                  | Type                     | Description                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globally unique ID for this event                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] External user ID of the user                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | API ID of the app on which this event occurred                                                                  |
| `canvas_id`                            | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas step message variation this user received                                                  |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Type of conversion event the user performed where "0" is a primary conversion and "1" is a secondary conversion |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Gender of the user                                                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] Country of the user                                                                                       |
| `timezone`                             | `string`,&nbsp;`null`    | Time zone of the user                                                                                            |
| `language`                             | `string`,&nbsp;`null`    | [PII] Language of the user                                                                                      |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Field                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globally unique ID for this event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] External user ID of the user                                   |
| `device_id`               | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                         |
| `time`                    | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Deprecated] API ID of the Canvas step this event belongs to         |
| `gender`                  | `string`,&nbsp;`null`    | [PII] Gender of the user                                             |
| `country`                 | `string`,&nbsp;`null`    | [PII] Country of the user                                            |
| `timezone`                | `string`,&nbsp;`null`    | Time zone of the user                                                 |
| `language`                | `string`,&nbsp;`null`    | [PII] Language of the user                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | True if the user was enrolled in the control group                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Field                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globally unique ID for this event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] External user ID of the user                                   |
| `device_id`               | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                         |
| `time`                    | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Field                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globally unique ID for this event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] External user ID of the user                                   |
| `device_id`               | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                         |
| `time`                    | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Field                       | Type                     | Description                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | Globally unique ID for this event                                                                               |
| `user_id`                   | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                                                                   |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] External user ID of the user                                                                              |
| `device_id`                 | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous                                            |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                                                                   |
| `time`                      | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | API ID of the app on which this event occurred                                                                  |
| `canvas_id`                 | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to                                                     |
| `canvas_api_id`             | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | API ID of the Experiment step this event belongs to                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Type of conversion event the user performed where "0" is a primary conversion and "1" is a secondary conversion |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Field                     | Type                     | Description                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globally unique ID for this event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] External user ID of the user                                   |
| `device_id`               | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                        |
| `time`                    | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                      |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | API ID of the Experiment step this event belongs to                  |
| `in_control_group`        | `boolean`,&nbsp;`null`   | True if the user was enrolled in the control group                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Field                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globally unique ID for this event                                    |
| `user_id`                              | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] External user ID of the user                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                         |
| `time`                                 | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas step message variation this user received       |
| `channel`                              | `string`,&nbsp;`null`    | Messaging Channel this event belongs to (email, push, etc.)          |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Gender of the user                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] Country of the user                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Time zone of the user                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] Language of the user                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Field                                  | Type                     | Description                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globally unique ID for this event                                    |
| `user_id`                              | `string`,&nbsp;`null`    | Braze ID of the user that performed this event                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] External user ID of the user                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                         |
| `time`                                 | `int`,&nbsp;`null`       | Unix timestamp at which the event happened                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (For Braze use only) ID of the Canvas this event belongs to          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API ID of the Canvas this event belongs to                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API ID of the Canvas variation this event belongs to                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API ID of the Canvas step this event belongs to                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API ID of the Canvas step message variation this user received       |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Gender of the user                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] Country of the user                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Time zone of the user                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] Language of the user                                           |
| `revenue`                              | `int`,&nbsp;`null`       | Amount of revenue generated in USD, displayed as cents               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Messages

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`content_card_id` | `string` | ID of the card that generated this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`content_card_id` | `string` | ID of the card that generated this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`content_card_id` | `string` | ID of the card that generated this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`content_card_id` | `string` | ID of the card that generated this event
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`sending_ip` | `null,`&nbsp;`string` | IP address from which the email send was made
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`bounce_reason` | `null,`&nbsp;`string` | [PII] The SMTP reason code and user friendly message received for this bounce event
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
`is_drop` | `null, boolean` | Indicates that this event counts as a drop event
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`url` | `null,`&nbsp;`string` | URL that the user clicked on
`user_agent` | `null,`&nbsp;`string` | User agent on which the click occurred
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`link_id` | `null,`&nbsp;`string` | Unique ID for the link which was clicked, as created by Braze
`link_alias` | `null,`&nbsp;`string` | Alias associated with this link ID
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
`is_amp` | `null, boolean` | Indicates that this is an AMP event
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`sending_ip` | `null,`&nbsp;`string` | IP address from which the email was sent
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`user_agent` | `null,`&nbsp;`string` | User agent on which the spam report occurred
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`user_agent` | `null,`&nbsp;`string` | User agent on which the open occurred
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`machine_open` | `null,`&nbsp;`string` | Populated to 'true' if the open event is triggered without user engagement, for example, by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
`is_amp` | `null, boolean` | Indicates that this is an AMP event
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`message_extras` | `null,`&nbsp;`string` | [PII] A JSON string of the tagged key-value pairs during Liquid rendering
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`sending_ip` | `null,`&nbsp;`string` | IP address from which the email send was made
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
`bounce_reason` | `null,`&nbsp;`string` | [PII] The SMTP reason code and user friendly message received for this bounce event
`esp` | `null,`&nbsp;`string` | ESP related to the event (SparkPost, SendGrid, or Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Sending domain for the email
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`email_address` | `string` | [PII] email address of the user
`ip_pool` | `null,`&nbsp;`string` | IP Pool from which the email send was made
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`card_api_id` | `null,`&nbsp;`string` | API ID of the card
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
`version` | `string` | Which version of in-app message, legacy or triggered
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`card_api_id` | `null,`&nbsp;`string` | API ID of the card
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | resolution of the device
`carrier` | `null,`&nbsp;`string` | carrier of the device
`browser` | `null,`&nbsp;`string` | browser of the device
`version` | `string` | which version of in-app message, legacy or triggered
`button_id` | `null,`&nbsp;`string` | ID of the button clicked, if this click represents a click on a button
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`card_api_id` | `null,`&nbsp;`string` | API ID of the card
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | resolution of the device
`carrier` | `null,`&nbsp;`string` | carrier of the device
`browser` | `null,`&nbsp;`string` | browser of the device
`version` | `string` | which version of in-app message, legacy or triggered
`ad_id` | `null,`&nbsp;`string` | [PII] Advertising identifier
`ad_id_type` | `null,`&nbsp;`string` | One of `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Whether advertising tracking is enabled for the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`card_api_id` | `null,`&nbsp;`string` | API ID of the card
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | resolution of the device
`carrier` | `null,`&nbsp;`string` | carrier of the device
`browser` | `null,`&nbsp;`string` | browser of the device
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`card_api_id` | `null,`&nbsp;`string` | API ID of the card
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | resolution of the device
`carrier` | `null,`&nbsp;`string` | carrier of the device
`browser` | `null,`&nbsp;`string` | browser of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`card_api_id` | `null,`&nbsp;`string` | API ID of the card
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | resolution of the device
`carrier` | `null,`&nbsp;`string` | carrier of the device
`browser` | `null,`&nbsp;`string` | browser of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that we made a delivery attempt to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`platform` | `string` | Platform of the device
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`push_token` | `null,`&nbsp;`string` | Push token that bounced
`device_id` | `null,`&nbsp;`string` | `device_id` that we made a delivery attempt to that bounced
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`platform` | `null,`&nbsp;`string` | Platform of the device
`ad_id` | `null,`&nbsp;`string` | [PII] advertising ID of the device that we made a delivery attempt to
`ad_id_type` | `null,`&nbsp;`string` | Type of the advertising id
`ad_tracking_enabled` | `null, boolean` | Whether or not tracking is enabled for advertising
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
`ad_id` | `null,`&nbsp;`string` | [PII] advertising ID of the device that we made a delivery attempt to
`ad_id_type` | `null,`&nbsp;`string` | Type of the advertising id
`ad_tracking_enabled` | `null, boolean` | Whether or not tracking is enabled for advertising
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`device_id` | `null,`&nbsp;`string` | ID of the device on which the event occurred
`sdk_version` | `null,`&nbsp;`string` | Version of the Braze SDK in use during the event
`platform` | `null,`&nbsp;`string` | Platform of the device
`os_version` | `null,`&nbsp;`string` | Version of the operating system of the device
`device_model` | `null,`&nbsp;`string` | Model of the device
`resolution` | `null,`&nbsp;`string` | Resolution of the device
`carrier` | `null,`&nbsp;`string` | Carrier of the device
`browser` | `null,`&nbsp;`string` | Browser of the device
`button_string` | `null,`&nbsp;`string` | Identifier (button_string) of the push notification button clicked. null if not from a button click
`button_action_type` | `null,`&nbsp;`string` | Action type of the push notification button. One of [URI, DEEP_LINK, NONE, CLOSE]. null if not from a button click
`slide_id` | `null,`&nbsp;`string` | Slide identifier of the push carousel slide user clicks on
`slide_action_type` | `null,`&nbsp;`string` | Action type of the push carousel slide
`ad_id` | `null,`&nbsp;`string` | [PII] advertising ID of the device that we made a delivery attempt to
`ad_id_type` | `null,`&nbsp;`string` | Type of the advertising id
`ad_tracking_enabled` | `null, boolean` | Whether or not tracking is enabled for advertising
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`push_token` | `null,`&nbsp;`string` | Push token that we made a delivery attempt to
`device_id` | `null,`&nbsp;`string` | `device_id` that we made a delivery attempt to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`app_api_id` | `null,`&nbsp;`string` | API ID of the app on which this event occurred
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`platform` | `string` | Platform of the device
`ad_id` | `null,`&nbsp;`string` | [PII] advertising ID of the device that we made a delivery attempt to
`ad_id_type` | `null,`&nbsp;`string` | Type of the advertising id
`ad_tracking_enabled` | `null, boolean` | Whether or not tracking is enabled for advertising
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`subscription_group_api_id` | `null,`&nbsp;`string` | External ID of the subscription group
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`from_phone_number` | `null,`&nbsp;`string` | phone number from which the SMS message was sent
`subscription_group_api_id` | `null,`&nbsp;`string` | external ID of the subscription group
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`from_phone_number` | `null,`&nbsp;`string` | Phone number from which the SMS message was sent
`subscription_group_api_id` | `null,`&nbsp;`string` | External ID of the subscription group
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`subscription_group_api_id` | `null,`&nbsp;`string` | external ID of the subscription group
`error` | `null,`&nbsp;`string` | error name
`provider_error_code` | `null,`&nbsp;`string` | error code from SMS service provider
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `null,`&nbsp;`string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace associated with the inbound phone number
`time` | `int` | Unix timestamp at which the event happened
`user_phone_number` | `string` | [PII] the user's phone number from which the message was received
`subscription_group_id` | `null,`&nbsp;`string` | ID of the subscription group targeted for this SMS message
`subscription_group_api_id` | `null,`&nbsp;`string` | API ID of the subscription group targeted for this SMS message
`inbound_phone_number` | `string` | The inbound number that the message was sent to
`action` | `string` | Action taken in response to this message. For example, `Subscribed`, `Unsubscribed`, or `None`.
`message_body` | `string` | Response from the user
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Media URLs from the user
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this event belongs to
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this event belongs to
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`from_phone_number` | `null,`&nbsp;`string` | phone number from which the SMS message was sent
`subscription_group_api_id` | `null,`&nbsp;`string` | external ID of the subscription group
`error` | `null,`&nbsp;`string` | error name
`provider_error_code` | `null,`&nbsp;`string` | error code from SMS service provider
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`subscription_group_api_id` | `null,`&nbsp;`string` | external ID of the subscription group
`category` | `null,`&nbsp;`string` | Keyword Category Name, only populated for auto-reply messages: 'Opt-in', 'Opt-out', 'Help', or custom value
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `null,`&nbsp;`string` | Braze ID of the user targeted by short_url, null if short_url did not use user click tracking
`external_user_id` | `null,`&nbsp;`string` | [PII] External ID of the user targeted by short_url if one exists, null if short_url did not use user click tracking
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace used to generate short_url
`time` | `int` | Unix timestamp at which short_url was clicked
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`campaign_id` | `null,`&nbsp;`string` | Braze ID of the campaign short_url was generated for, null if not from a campaign
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign short_url was generated for, null if not from a campaign
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation short_url was generated for, null if not from a campaign
`canvas_id` | `null,`&nbsp;`string` | Braze ID of the Canvas short_url was generated for, null if not from a Canvas
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas short_url was generated for, null if not from a Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation short_url was generated for, null if not from a Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step short_url was generated for, null if not from a Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation short_url was generated for, null if not from a Canvas
`url` | `string` | original URL contained in message that is redirected to by short_url
`short_url` | `string` | shortened URL that was clicked
`user_agent` | `null,`&nbsp;`string` | user agent requesting short_url
`user_phone_number` | `string` | [PII] the user's phone number
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`time` | `int` | Unix timestamp at which the event happened
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`send_id` | `null,`&nbsp;`string` | Message send ID this message belongs to
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`gender` | `null,`&nbsp;`string` | [PII] Gender of the user
`country` | `null,`&nbsp;`string` | [PII] Country of the user
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`language` | `null,`&nbsp;`string` | [PII] Language of the user
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`time` | `int` | Unix timestamp at which the event happened
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] phone number of the recipient
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`app_group_id` | `null,`&nbsp;`string` | ID of the workspace this user belongs to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`abort_type` | `null,`&nbsp;`string` | Type of abort, one of: `liquid_abort_message` or `rate_limit`
`abort_log` | `null,`&nbsp;`string` | [PII] Log message describing abort details (maximum of 128 characters)
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`time` | `int` | Unix timestamp at which the event happened
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`from_phone_number` | `null,`&nbsp;`string` | Phone number from which the WhatsApp message was sent
`app_group_id` | `null,`&nbsp;`string` | ID of the workspace this user belongs to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`time` | `int` | Unix timestamp at which the event happened
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`from_phone_number` | `null,`&nbsp;`string` | Phone number from which the WhatsApp message was sent
`app_group_id` | `null,`&nbsp;`string` | ID of the workspace this user belongs to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`provider_error_code` | `null,`&nbsp;`string` | Error code from WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Error title from WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`time` | `int` | Unix timestamp at which the event happened
`user_phone_number` | `string` | [PII] the user’s phone number from which the message was received
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`inbound_phone_number` | `string` | The inbound number that the message was sent to
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`app_group_id` | `null,`&nbsp;`string` | ID of the workspace this user belongs to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`message_body` | `string` | Response from the user
`quick_reply_text` | `string` | Text of button pressed by the user
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Media URLs from the user
`action` | `string` | Action taken in response to this message. For example, `Subscribed`, `Unsubscribed`, or `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`time` | `int` | Unix timestamp at which the event happened
`to_phone_number` | `null,`&nbsp;`string` | [PII] phone number of the recipient
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`from_phone_number` | `null,`&nbsp;`string` | Phone number from which the WhatsApp message was sent
`app_group_id` | `null,`&nbsp;`string` | ID of the workspace this user belongs to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Field | Type | Description
------|------|------------
`id` | `string` | Globally unique ID for this event
`time` | `int` | Unix timestamp at which the event happened
`to_phone_number` | `null,`&nbsp;`string`	| [PII] phone number of the recipient
`user_id` | `string` | Braze ID of the user that performed this event
`external_user_id` | `null,`&nbsp;`string` | [PII] External user ID of the user
`device_id` | `null,`&nbsp;`string` | `device_id` that is tied to this user if user is anonymous
`timezone` | `null,`&nbsp;`string` | Time zone of the user
`from_phone_number` | `null,`&nbsp;`string` | phone number from which the WhatsApp message was sent
`app_group_id` | `null,`&nbsp;`string` | ID of the workspace this user belongs to
`app_group_api_id` | `null,`&nbsp;`string` | API ID of the workspace this user belongs to
`subscription_group_api_id` | `string` | Subscription group API ID
`campaign_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the campaign this event belongs to
`campaign_api_id` | `null,`&nbsp;`string` | API ID of the campaign this event belongs to
`message_variation_api_id` | `null,`&nbsp;`string` | API ID of the message variation this user received
`canvas_id` | `null,`&nbsp;`string` | Internal-use Braze ID of the Canvas this event belongs to
`canvas_api_id` | `null,`&nbsp;`string` | API ID of the Canvas this event belongs to
`canvas_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas variation this event belongs to
`canvas_step_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step this event belongs to
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API ID of the Canvas step message variation this user received
`dispatch_id` | `null,`&nbsp;`string` | ID of the dispatch this message belongs to
`message_extras` | `null,`&nbsp;`string` | [PII] A JSON string of the tagged key-value pairs during Liquid rendering
`sf_created_at` | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Users

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Field                       | Type                     | Description                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | Globally unique ID for this event                  |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to      |
| `app_group_api_id`          | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to       |
| `user_id`                   | `string`,&nbsp;`null`    | Braze ID of the user that performed this event      |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] External user ID of the user                 |
| `time`                      | `int`,&nbsp;`null`       | Unix timestamp at which the event happened         |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Current random bucket number assigned to the user  |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Previous random bucket number assigned to the user |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Field              | Type                     | Description                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Globally unique ID for this event                             |
| `user_id`          | `string`,&nbsp;`null`    | Braze ID of the user that was deleted                          |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                  |
| `time`             | `int`,&nbsp;`null`       | Unix timestamp at which the user delete request was processed |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Field              | Type                     | Description                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Globally unique ID for this event                                             |
| `user_id`          | `string`,&nbsp;`null`    | Braze ID of the user that was orphaned                                         |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] External user ID of the user                                            |
| `device_id`        | `string`,&nbsp;`null`    | ID of the device that is tied to this user, if the user is anonymous          |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze ID of the workspace this user belongs to                                 |
| `app_group_api_id` | `string`,&nbsp;`null`    | API ID of the workspace this user belongs to                                  |
| `app_api_id`       | `string`,&nbsp;`null`    | API ID of the app the orphaned user belonged to                               |
| `time`             | `int`,&nbsp;`null`       | Unix timestamp at which the user was orphaned                                 |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | Braze ID of the user whose profile was merged with the orphaned user's profile |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | When this event was picked up by the Snowpipe                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

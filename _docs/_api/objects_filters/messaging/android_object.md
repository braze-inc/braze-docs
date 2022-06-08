---
nav_title: "Android Objects"
article_title: Android Messaging Object
page_order: 0
page_type: reference
channel: push
platform: Android
description: "This article lists and explains the different Android objects used at Braze."

---
# Android object specification

The `android_push` object allows you to define or request information related to Android Push and Android Push Alert content via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

##  Android push object

You must include an Android Push Object in `messages` if you want users you have targeted to receive a push on their Android devices. The total number of bytes in your `alert` string and `extra` object should not exceed 4000. The Messaging API will return an error if you exceed the message size allowed by Google.

### Body

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android Push Action Button Objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed via Conversation Push.
}
```


You can send "Big Picture" notifications by specifying the key `appboy_image_url` in the `extra` object. The value for `appboy_image_url` should be a URL that links to where your image is hosted. Images need to be cropped to a 2:1 aspect ratio and should be at least 600x300. Images used for notifications will only display on devices running Jelly Bean (Android 4.1) or higher.

#### Additional parameter details

| Parameter | Details |
| --------- | ------- |
| `priority` | This parameter will accept values from `-2` to `2`, where `-2` represents "MIN" priority and `2` represents "MAX". `0` is the "DEFAULT" value. <br> <br> Any values sent that outside of that integer range will default to 0. For more information on which priority level to use, see our section on [Android Notification Priority][29]. |
| `collapse_key` | FCM can simultaneously store only up to four collapse keys per device. If you use more than four collapse keys, FCM does not make any guarantees as to which ones will be kept. Braze uses one of these by default for campaigns, so make sure to specify only up to three additional collapse keys for Android messages. |
| `push_icon_image_url` | The value for the large icon parameter should be a URL that links to where your image is hosted. <br> <br> Images need to be cropped to a 1:1 aspect ratio and should be at least 40x40. |
| `notification_channel` | If this is not specified, Braze will attempt to send the notification payload with the [dashboard fallback][45] channel ID. For more, see [Notification channels][44] and refer to the steps for [defining notification channels][43] during integration. |
| `send_to_sync` | For more information on `send_to_sync` messages, see [Silent Android Notifications][28]. |
{: .reset-td-br-1 .reset-td-br-2}


## Android push action button object

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android conversation push object {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

The concepts in this message correspond to those in the [Android People and Conversations][46] push documentation.

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android conversation push message object

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Android conversation push person object

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```

[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[44]: {{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/
[43]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels
[45]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel
[46]: https://developer.android.com/guide/topics/ui/conversations
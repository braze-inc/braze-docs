---
nav_title: "안드로이드 개체"
article_title: Android 메시징 개체
page_order: 0
page_type: reference
channel: push
platform: Android
description: "이 참조 문서에서는 Braze에서 사용되는 다양한 Android 객체를 나열하고 설명합니다."

---
# 안드로이드 개체

> `android_push` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 Android 푸시 및 Android 푸시 알림 콘텐츠와 관련된 정보를 정의하거나 요청할 수 있습니다.

## Android 푸시 개체

타겟팅한 사용자가 Android 디바이스에서 푸시를 수신하도록 하려면 `messages` 에 Android 푸시 개체를 포함해야 합니다. `alert` 문자열과 `extra` 객체의 총 바이트 수는 4,000개를 초과하지 않아야 합니다. 메시징 API는 Google에서 허용하는 메시지 크기를 초과하면 오류를 반환합니다.

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "android_priority": (optional, string) the FCM sender priority,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to false,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (maximum of 2,419,200 seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android push action button objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed through Conversation Push
}
```

`extra` 객체에 `appboy_image_url` 키를 지정하여 “큰 그림” 알림을 보낼 수 있습니다. `appboy_image_url` 값은 이미지가 호스팅되는 위치로 연결되는 URL이어야 합니다. 이미지는 2:1 가로세로 비율로 잘라야 하며 최소 600 x 300픽셀이어야 합니다.

### 추가 매개변수 세부 정보

| 매개변수 | 세부 정보 |
| --------- | ------- |
| `priority` | 이 매개변수는 `-2` ~ `2` 범위의 값을 허용하며, `-2` 은 "최소" 우선순위를 나타내고 `2` 은 "최대"를 나타냅니다. `0` 은 "기본" 값입니다. <br> <br> 이 범위를 벗어나는 값은 기본값이 0으로 설정됩니다. 사용할 우선순위에 대한 자세한 내용은 [Android 알림 우선순위를]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority) 참조하세요. |
| `android_priority` | 이 매개변수는 `normal` 또는 `high` 값을 사용하여 FCM 발신자 우선순위를 지정할 수 있습니다. 기본적으로 메시지는 [푸시 설정]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/#default-fcm-priority-for-android-campaigns) 페이지에서 구성된 기본 FCM 우선순위로 전송됩니다.<br><br> 다양한 값이 배달에 미치는 영향에 대한 자세한 내용은 [Android 메시지 우선순위를](https://firebase.google.com/docs/cloud-messaging/android/message-priority) 참조하세요. |
| `collapse_key` | FCM은 장치당 최대 4개의 축소 키만 동시에 저장할 수 있습니다. 축소 키를 4개 이상 사용하는 경우 FCM은 어떤 축소 키가 유지될지 보장하지 않습니다. Braze는 기본적으로 캠페인에 이 중 하나를 사용하므로 Android 메시지에는 최대 3개의 추가 축소 키만 지정해야 합니다. |
| `push_icon_image_url` | 큰 아이콘 매개변수의 값은 이미지가 호스팅되는 위치로 연결되는 URL이어야 합니다. <br> <br> 이미지는 1:1 가로세로 비율로 잘라야 하며 최소 40x40이어야 합니다. |
| `notification_channel` | 이를 지정하지 않으면 Braze는 [대시보드 폴백]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel) 채널 ID로 알림 페이로드를 전송하려고 시도합니다. 자세한 내용은 [알림 채널을]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/) 참조하고 통합 중 [알림 채널을 정의하는]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels) 단계를 참조하세요. |
| `send_to_sync` | `send_to_sync` 메시지에 대한 자세한 내용은 [무음 Android 알림을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 안드로이드 푸시 액션 버튼 개체

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Android 대화 푸시 개체 {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

이 메시지의 개념은 [Android 사용자 및 대화](https://developer.android.com/guide/topics/ui/conversations) 푸시 문서에 나와 있는 개념과 일치합니다.

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Android 대화 푸시 메시지 개체

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### 안드로이드 대화 푸시 사람 개체

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```


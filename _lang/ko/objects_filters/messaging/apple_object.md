---
nav_title: "Apple 개체"
article_title: Apple 메시징 개체
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "이 참조 문서에서는 Braze에서 사용되는 다양한 Apple 객체를 나열하고 설명합니다."

---

# Apple 푸시 개체

> `apple_push` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 Apple 푸시 및 Apple 푸시 알림 콘텐츠와 관련된 정보를 정의하거나 요청할 수 있습니다.

## Apple 푸시 개체

```json
{
   "badge": (optional, integer) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "interruption_level": (optional, string: "passive", "active", "time-sensitive", or "critical") specifies the interruption level passed (iOS 15+),
   "relevance_score": (optional, float) specifies the relevance score between 0.0 and 1.0 used for grouping notification summaries (iOS 15+),
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device after you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple push action button objects) push action buttons to display,
   "apns_priority": (optional, integer) override the default apns_priority value using an integer between 1 and 10; use 10 for immediate delivery, 5 for power-aware delivery, and 1 to minimize power impact and avoid waking the device,
}
```

타겟팅한 사용자가 iOS 기기에서 푸시를 수신하도록 하려면 `messages`에 Apple 푸시 개체를 포함해야 합니다. `alert` 문자열, `extra` 객체 및 기타 선택적 매개변수의 총 바이트 수는 1912를 초과하지 않아야 합니다. 메시징 API는 Apple에서 허용하는 메시지 크기를 초과하면 오류를 반환합니다. `extra` 객체에 `ab` 또는 `aps` 키가 포함된 메시지는 거부됩니다.

{% alert note %}
Apple 푸시 오브젝트를 라이브 활동 페이로드의 일부로 전송하는 경우 `alert` 오브젝트에 `sound` 문자열을 포함해야 합니다.
{% endalert %}

### Apple 푸시 알림 개체

대부분의 경우 `apple_push` 객체에서 `alert`를 문자열로 지정할 수 있습니다.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button's title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key,
   "sound": (optional, string) the location of a custom notification sound within the app (live activities only),
}
```

#### 예시

```json
{
  "broadcast": false,
  "external_user_ids": ["PushTest12"],
  "campaign_id": "9c2fefcd-9115-3932-f771-c7f43d18d6b6",
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "apple_push": {
      "alert": {
        "title": "Hello!",
        "body": "Message here"
      },
      "message_variation_id": "iosPush-640"
    }
  }
}
```

## Apple 푸시 액션 버튼 개체

iOS 푸시 액션 버튼을 사용하려면 Apple 푸시 개체에 `category` 필드를 포함해야 합니다. `category` 필드를 포함하면 관련된 모든 푸시 동작 버튼이 표시되며, 버튼의 개별 클릭 동작을 추가로 정의하려는 경우에만 `buttons` 필드를 포함하세요. Braze SDK는 다음 표와 같이 사용할 수 있는 기본 푸시 액션 버튼 세트를 제공합니다. 앱에 등록되어 있는 경우 직접 만든 버튼을 사용할 수도 있습니다.

### Braze 기본 버튼용 Apple 푸시 액션 버튼 개체

| 카테고리 식별자   | 버튼 텍스트 | 버튼 동작 식별자 | 허용된 작업         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | 수락      | `ab_pb_accept`             | OPEN_APP, URI, 또는 DEEP_LINK |
| `ab_cat_accept_decline` | 거부     | `ab_pb_decline`            | 닫기                   |
| `ab_cat_yes_no`         | 예         | `ab_pb_yes`                | OPEN_APP, URI, 또는 DEEP_LINK |
| `ab_cat_yes_no`         | 아니요          | `ab_pb_no`                 | 닫기                   |
| `ab_cat_confirm_cancel` | 확인     | `ab_pb_confirm`            | OPEN_APP, URI, 또는 DEEP_LINK |
| `ab_cat_confirm_cancel` | 취소      | `ab_pb_cancel`             | 닫기                   |
| `ab_cat_more`           | 더 보기        | `ab_pb_more`               | OPEN_APP, URI, 또는 DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### 앱에서 정의한 카테고리에 대한 Apple 푸시 액션 버튼 개체

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

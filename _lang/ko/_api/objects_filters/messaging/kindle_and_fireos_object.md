---
nav_title: "Kindle 및 FireOS 푸시 개체"
article_title: Kindle 및 FireOS 푸시 메시징 개체
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "이 참조 문서에서는 Braze Kindle 및 FireOS 푸시 개체의 다양한 구성 요소에 대해 설명합니다."

---

# Kindle 및 FireOS 푸시 개체

> `kindle_push` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 Kindle 및 FireOS 푸시 알림을 수정하거나 생성할 수 있습니다.

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "priority": (optional, integer) the notification priority value,
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI
}
```

`priority` 매개변수는 `-2`에서 `2` 사이의 값을 허용하며, 이때 `-2`는 가장 낮은 우선순위를, `2`는 가장 높은 우선순위를 나타냅니다. 기본값은 `0`입니다. 해당 정수 범위를 벗어나는 값을 전송하면 기본값은 `0` 입니다.

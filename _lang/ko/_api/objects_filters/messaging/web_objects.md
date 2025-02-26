---
nav_title: "웹 개체"
article_title: 웹 메시징 개체
page_order: 12
page_type: reference
channel: push
platform: Web
description: "이 참조 문서에서는 Braze에서 사용되는 다양한 웹 객체를 나열하고 설명합니다."

---
# 웹 푸시 개체

> `web_push` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 웹 푸시 및 웹 푸시 알림 콘텐츠와 관련된 정보를 정의하거나 요청할 수 있습니다.

## 웹 푸시 개체

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "custom_uri": (optional, string) a web URL,
   "image_url": (optional, string) URL for image to show,
   "large_image_url": (optional, string) URL for large image, supported on Chrome Windows/Android,
   "require_interaction": (optional, boolean) whether to require the user to dismiss the notification. for a list of supported platforms, see: "https://developer.mozilla.org/en-US/docs/Web/API/Notification/requireInteraction#browser_compatibility",
   "time_to_live": (optional, integer (seconds)),
   "send_to_most_recent_device_only" : (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used browser, rather than all eligibles browsers,
   "buttons" : (optional, array of Web push action button objects) push action buttons to display
}
```

`image_url` 값은 이미지가 호스팅되는 위치로 연결되는 URL이어야 합니다. 이미지는 1:1 화면 비율로 잘라야 합니다.

## 웹 푸시 액션 버튼 개체

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```

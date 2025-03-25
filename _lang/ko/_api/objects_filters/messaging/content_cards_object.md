---
nav_title: "콘텐츠 카드 객체"
article_title: 콘텐츠 카드 메시징 개체
page_order: 4
page_type: reference
channel: content cards
description: "이 참조 문서에서는 브레이즈 콘텐츠 카드 객체의 다양한 구성 요소에 대해 설명합니다."

---

# 콘텐츠 카드 객체

> `content_card` 객체를 사용하면 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 통해 콘텐츠 카드를 만들 수 있습니다.

```json
{
  "type": (required, string) one of "CLASSIC", "CAPTIONED_IMAGE", or "BANNER",
  "title": (required, string) the card's title,
  "description": (required, string) the card's description,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Content Card Message),
  "pinned": (optional, boolean) whether the card is pinned. Defaults to false,
  "image_url": (optional, string) the card's image URL. Required for "CAPTIONED_IMAGE" and "BANNER",
  "time_to_live": (optional, integer) the number of seconds before the card expires. You must include either "time_to_live" or "expire_at",
  "expire_at": (optional, string) ISO 8601 date when the card expires. You must include either "time_to_live" or "expire_at", a maximum expiration time exists of 30 days,
  "expire_in_local_time": (optional, boolean) if using "expire_at", determines whether the card should expire in users' local time. Defaults to false,
  "ios_uri": (optional, string) a web URL, or Deep Link URI,
  "android_uri": (optional, string) a web URL, or Deep Link URI,
  "web_uri": (optional, string) a web URL, or Deep Link URI,
  "ios_use_webview": (optional, boolean) whether to open the web URL inside the app, defaults to true,
  "android_use_webview": (optional, boolean) whether to open the web URL inside the app, defaults to true,
  "uri_text": (optional, string) the card's link text,
  "extra": (optional, object) additional keys and values sent with the card,
}
```

{% alert important %}
현재 Braze는 최대 만료 시간을 30일로 지원합니다.
{% endalert %}

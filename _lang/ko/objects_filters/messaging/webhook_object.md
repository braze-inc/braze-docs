---
nav_title: "웹훅 객체"
article_title: 웹훅 메시징 개체
page_order: 13
page_type: reference
channel: 
  - webhook
description: "이 참조 문서에서는 Braze 웹훅 객체에 대해 간략하게 설명합니다."

---

# 웹훅 객체

> `webhook` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 웹훅 메시지를 수정하거나 생성할 수 있습니다.

```json
{
  "url": (required, string),
  "request_method": (required, string) one of "POST", "PUT", "DELETE", or "GET",
  "request_headers": (optional, Hash) key-value pairs to use as request headers,
  "body": (optional, string) if you want to include a JSON object, make sure to escape quotes and backslashes,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under
}
```

Braze는 시간이 지남에 따라 발신자와 서버가 변경될 수 있으므로 일관되고 예측 가능한 동작을 위해 `request_headers` 필드에서 `Content-Type`에 대한 명시적인 가치를 제공하는 것이 좋습니다. `Content-Type` 헤더에 값을 지정하지 않으면 요청 본문에서 값을 유추합니다.

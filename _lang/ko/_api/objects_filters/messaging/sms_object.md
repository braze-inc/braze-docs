---
nav_title: "SMS 개체"
article_title: SMS 메시징 객체
page_order: 10
page_type: reference
channel: SMS
description: "이 참고 문서에서는 Braze SMS 객체의 다양한 구성 요소에 대해 설명합니다."

---
# SMS 개체

> `sms` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 SMS 메시지를 수정하거나 생성할 수 있습니다.

```json
{
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message.    
}
```

- [앱 식별자]({{site.baseurl}}/api/identifier_types/)
---
nav_title: "SMS 개체"
article_title: SMS 메시징 개체
page_order: 10
page_type: reference
channel: SMS
description: "이 참고 문서에서는 Braze SMS 객체의 다양한 구성 요소에 대해 설명합니다."

---
# SMS 개체

> `sms` 개체를 사용하면 [메시징 엔드포인트를]({{site.baseurl}}/api/endpoints/messaging) 통해 SMS 메시지를 수정하거나 생성할 수 있습니다.

```json
{
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.     
}
```

- [앱 식별자]({{site.baseurl}}/api/identifier_types/)
  - 워크스페이스에 구성된 앱의 유효한 `app_id` 은 사용자의 프로필에 특정 앱이 있는지 여부에 관계없이 워크스페이스의 모든 사용자에게 적용됩니다.
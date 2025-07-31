---
nav_title: "사용자 옵트인 수집"
article_title: 사용자 SMS 옵트인 수집 모범 사례
page_order: 7
description: "이 참고 문서에서는 사용자 옵트인 수집을 위한 세 가지 모범 사례를 다룹니다."
page_type: reference
channel:
  - SMS
  
---

# 사용자 옵트인 수집

> 다음 문서에는 몇 가지 일반적인 SMS 수신 동의 방법이 나와 있습니다.

## 옵션 1: 사용자에게 짧은 코드 또는 긴 코드를 문자로 보내도록 요청

사용자에게 "START", "UNSTOP", "YES" 또는 커스텀 옵트인 키워드를 문자로 보내도록 요청하면 자동으로 구독 그룹에 추가됩니다. 웹사이트, 모바일 앱 또는 광고에서 사용자에게 옵트인을 요청할 수 있으며, 도움이 된다면 인센티브를 제공할 수 있습니다.

## 옵션 2: 사용자가 인앱 메시지를 통해 옵트인

사용자가 인앱 메시지에서 SMS를 수신할 수 있도록 하려면 Braze에서 제공하는 [전화번호 캡처 양식을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/) 사용하여 전화번호를 수집하고 SMS 목록을 늘릴 수 있는 브랜드 양식을 만드세요.

![][3]{: style="max-width:30%;"}

Braze는 [SMS 이중 옵트인]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/) 기능도 사용할 것을 권장합니다. 이 기능은 인앱 메시지 전화번호 캡처 양식과 자동으로 연동되어 사용자가 양식을 통해 전화번호를 제출한 후 의사를 확인하는 메시지를 표시합니다.

## 옵션 3: 가입 흐름

신규 사용자가 웹사이트나 앱에 가입하거나 등록할 때 전화번호와 이메일을 요청하세요. 프로모션 이메일 및 SMS 수신을 위한 확인란을 포함하세요. 

사용자가 가입한 후 다음을 수행합니다:

1. [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status)를 사용하여 사용자를 생성하고 해당 사용자의 속성을 저장합니다.

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

{: start="2"}
2\. [`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 사용하여 사용자를 SMS에 가입시킵니다.

```json
POST `https://rest.aid-03.braze.com/users/track` \
--header `Content-Type: application/json` \
--header `Authorization: Bearer YOUR-REST-API-KEY` \
--data-raw `{
"attributes" : [
Unknown macro: { "external_id" }
]
}
```

[1]: {% image_buster /assets/img/sms/opt-in1.png %}
[2]: {% image_buster /assets/img/sms/opt-in2.png %}
[3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}

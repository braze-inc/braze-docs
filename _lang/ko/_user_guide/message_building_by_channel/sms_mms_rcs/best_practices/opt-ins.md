---
nav_title: "사용자 옵트인 수집"
article_title: 사용자 SMS 옵트인 수집을 위한 모범 사례
page_order: 7
description: "이 참조 기사는 사용자 옵트인을 수집하기 위한 세 가지 모범 사례를 다룹니다."
page_type: reference
channel:
  - SMS
  
---

# 사용자 옵트인 수집

> 다음 기사는 몇 가지 일반적인 SMS 옵트인 방법을 나열합니다.

## 옵션 1: 사용자에게 짧은 코드 또는 긴 코드로 문자 메시지를 보내도록 요청합니다.

사용자에게 "START", "UNSTOP", "YES" 또는 사용자 지정 옵트인 키워드를 귀하의 번호로 문자 메시지를 보내 자동으로 구독 그룹에 추가하도록 요청합니다. 웹사이트, 모바일 앱 또는 광고에서 사용자가 옵트인하도록 요청할 수 있으며, 도움이 된다면 인센티브를 제공할 수 있습니다.

## 옵션 2: 사용자가 인앱 메시지를 통해 옵트인합니다.

사용자가 인앱 메시지에서 SMS에 옵트인할 수 있도록 하려면, Braze에서 제공하는 [전화번호 수집 양식]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)을 사용하여 전화번호를 수집하고 SMS 목록을 늘릴 수 있는 브랜드 양식을 만드세요.

\![전화번호 수집을 위한 템플릿이 있는 인앱 메시지 작성기.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze는 [SMS 이중 옵트인]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) 기능을 사용하는 것도 권장합니다. 이 기능은 인앱 메시지 전화번호 수집 양식과 자동으로 작동하여 사용자가 양식을 통해 전화번호를 제출한 후 의도를 확인하도록 요청합니다.

## 옵션 3: 가입 흐름

새 사용자가 웹사이트나 앱에 가입하거나 등록할 때 전화번호와 이메일을 요청합니다. 프로모션 이메일 및 SMS를 수신하기 위한 체크박스를 포함합니다. 

사용자가 가입한 후 다음을 수행합니다:

1. [`/subscription/status/set` 엔드포인트]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status)를 사용하여 사용자를 생성하고 속성을 저장합니다.

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
2\. 사용자가 SMS에 가입하도록 하려면 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하세요.

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


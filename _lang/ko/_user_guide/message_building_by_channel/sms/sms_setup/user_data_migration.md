---
nav_title: "사용자 데이터 마이그레이션"
article_title: 사용자 데이터 마이그레이션
page_order: 4
description: "이 참조 문서에서는 사용자 데이터를 Braze로 마이그레이션할 때 염두에 두어야 할 모든 고려 사항을 설명합니다."
page_type: reference
channel:
  - SMS
noindex: true

---

# 사용자 데이터 마이그레이션

> 이 글에서는 사용자 데이터를 Braze로 마이그레이션할 때 염두에 두어야 할 모든 고려 사항을 살펴봅니다.

## 사용자 전화번호를 통신사 표준에 맞게 포맷

각 기기가 전 세계적으로 고유한 번호를 갖도록 하는 국제 전화 번호 계획인 E.164라는 특정 형식이 있습니다. E.164 번호는 다음 이미지와 같이 형식이 지정되며 최대 15자리까지 사용할 수 있습니다.

![E.164 형식은 더하기 기호, 국가 코드, 지역 번호 및 전화번호로 구성됩니다][그림]{: style="max-width:50%;border: 0;"}

자세한 내용은 [사용자 전화번호를][userphone] 참조하세요.

## 사용자 구독 상태에 대한 기록 정보 업데이트

사용자의 [구독 상태] [다양한 메시징 채널의 구독 상태]에 대한 기록 정보가 있는 경우, Braze에서 이 정보를 업데이트해야 합니다.

## 마이그레이션 단계 예시

Braze를 통해 SMS 캠페인을 작성하기 전에 사용자 데이터를 업데이트하여 이 모든 것이 제대로 작동하는지 확인해야 합니다.

**다음은 Braze에서 업데이트해야 하는 사용자 데이터에 대한 간략한 요약입니다:**

1. **사용자의 전화번호를 올바른 형식**([E.164][0]) 형식에는 더하기 기호(+)와 국가 코드가 필요합니다. 예를 들어 +12408884782. 사용자 전화번호 가져오기 방법에 대한 자세한 내용은 [사용자 전화번호][userphone]를 참조하세요.
    * [`/users/track` 엔드포인트][1]를 사용하여 `phone` 값을 할당합니다.<br><br>

2. 이 정보가 있는 경우 **사용자의 SMS [구독 상태][구독 상태]**(예: 구독 또는 구독 취소)]를 지정합니다.
    * [`/subscription/status/set` 엔드포인트][6]를 사용하여 사용자를 SMS 구독 그룹에서 구독 또는 구독 취소 상태로 설정합니다.

{% alert note %}
대시보드에서 SMS 구독 그룹을 구성한 후에는 API 요청에 필요한 관련 `subscription_group_id`를 가져올 수 있습니다.
{% endalert %}

[0]: https://en.wikipedia.org/wiki/E.164
[userphone]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#aliasing-users
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/#aliasing-users
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#aliasing-users
[6]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[picture]: {% image_buster /assets/img/sms/e164.jpg %}
[customkeyword]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/custom_keyword_handling/
[subscriptionstate]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#sms-subscription-states

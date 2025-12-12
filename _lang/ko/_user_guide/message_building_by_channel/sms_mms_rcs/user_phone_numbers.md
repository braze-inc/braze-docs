---
nav_title: "사용자 전화번호"
article_title: SMS 사용자 전화번호
page_order: 7
description: "이 참조 문서에서는 SMS 전화번호 형식, 전화번호 가져오기 방법, SMS 구독 그룹에 사용자 추가 방법을 다룹니다."
page_type: reference
alias: /user_phone_numbers/
channel: 
  - SMS
  - MMS
  - RCS
---

# 사용자 전화번호

> 이 문서에서는 사용자 또는 고객의 전화번호에 대한 다양한 주제를 논의합니다. 자신의 번호에 대한 정보가 필요하면 [전화번호 전송]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/)에 대한 문서를 참조하세요.

## 권장 형식

여러 지역에 서로 다른 국가 또는 지역 코드가 있는 경우에도 정확성을 보장하기 위해 [`E.164`](https://en.wikipedia.org/wiki/e.164) 형식으로 전화번호를 가져오는 것을 권장합니다. U.S.-기반 전화번호에 대해서도 마찬가지입니다.

- **U.S. 번호:** 모든 U.S. 번호는 유효한 지역 코드가 있는 10자리 전화번호여야 합니다. 어떤 10자리 전화번호에 `+` 및 국가 코드가 누락된 경우, Braze는 이를 U.S. 번호로 매핑합니다.
- **국제 번호:** 모든 국제 번호는 `+`로 시작해야 하며, 그 다음에 국가 코드와 전화번호가 와야 합니다. 예를 들어, `+442071838750`.

\![유효한 e164 국제 전화번호의 예.]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

여기에는 로컬 형식과 `E.164` 형식 간의 차이를 보여주는 몇 가지 예가 있습니다:

| 국가 | 로컬 | 국가 코드 | `E.164` |
|---|---|---|---|
| 미국 | `4155552671` | 1 | `+14155552671` |
| 영국 | `2071838750` | 44 | `+442071838750` |
| 브라질 | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 reset-td-br-4}

## 전화번호 가져오기

전화번호를 가져올 때는 [권장 형식](#recommended-format)을 따르는 것이 중요합니다. 전화번호를 가져오려면 다음 방법 중 하나를 사용하세요:

- [CSV를 Braze에 업로드하기]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv)
- [ `/users/track` 엔드포인트 사용하기]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
사용자의 전화번호는 Braze에서 숫자 문자열로 표시됩니다. 숫자가 아닌 문자가 포함된 번호(예: `,`, `-`, `(` 등)를 가져오면, Braze에서 렌더링될 때 숫자가 아닌 문자는 제거됩니다. 예를 들어, `+1 (724) 123-4567`를 가져오면 `17241234567`으로 표시됩니다.
{% endalert %}

## 유효하지 않은 전화번호 처리

전화번호가 유효하지 않은 것으로 간주되면, Braze는 사용자의 전화번호를 유효하지 않다고 표시하고 해당 전화번호로 추가 통신을 시도하지 않습니다. 유효하지 않은 전화번호는 사용자 프로필의 **참여 탭**에 표시됩니다.

\![Braze에서 유효하지 않은 전화번호에 대한 예시 오류 메시지.]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

전화번호가 유효하지 않은 이유는 다음과 같습니다:

- **제공자 오류**: SMS 및 RCS 제공자로부터 영구적인 오류가 수신되었습니다. 이것은 제공된 전화번호가 잘못된 형식이거나 SMS 또는 RCS 메시지를 영구적으로 수신할 수 없음을 나타냅니다.
- **비활성화됨**: 전화번호는 모바일 가입자가 서비스를 종료하고 번호를 통신사에서 해제하여 비활성화되었습니다(그리고 결국 재활용되어 새로운 사용자에게 할당될 수 있습니다).

이러한 잘못된 전화번호는 [SMS 및 RCS 엔드포인트]({{site.baseurl}}/api/endpoints/sms/)를 사용하여 관리할 수 있습니다. 

{% alert note %}
여러 사용자 프로필이 동일한 전화번호를 가지고 있고 해당 전화번호가 잘못된 것으로 표시되면, 해당 번호를 가진 모든 기존 사용자 프로필이 잘못된 것으로 표시됩니다. 새로 생성된 사용자 프로필은 처음에는 절대 잘못된 것으로 표시되지 않습니다.
{% endalert %}

[세그먼트 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment) 시 잘못된 전화번호를 가진 사용자를 포함하거나 제외할 수도 있습니다.

## SMS 및 RCS 구독 그룹에 사용자 추가

사용자가 SMS 또는 RCS 메시지를 수신하려면 유효한 전화번호를 가지고 있어야 하며 구독 그룹에 가입해야 합니다. 구독 그룹은 귀하가 운영하는 SMS 또는 RCS 프로그램에 연결되어 있습니다(법적 요구 사항 [SMS, MMS 및 RCS에 대한 법적 요구 사항]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)을 준수하고 각 고객의 동의를 기록했는지 확인하십시오). 자세한 내용은 [SMS 및 RCS 구독 그룹]({{site.baseurl}}/sms_rcs_subscription_groups/)를 참조하십시오.

## 제3자 소싱 및 검증

Braze는 잘못된 번호를 소싱하기 위해 제3자 도구에 의존합니다. Braze는 이러한 서비스의 중단이나 잘못된 정보에 대해 책임을 지지 않습니다. 따라서 이 도구는 잘못된 번호를 검증하기 위한 유일한 준수 방법으로 의존해서는 안 됩니다.

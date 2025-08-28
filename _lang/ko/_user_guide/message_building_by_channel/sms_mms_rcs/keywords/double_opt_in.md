---
nav_title: 이중 옵트인
article_title: 이중 옵트인
description: "이 참조 문서에서는 더블 옵트인 기능을 다루고 있으며, 기능을 활성화하고, 옵트인 키워드를 선택하고, 응답 메시지를 설정하며, REST API, SDK 및 기본 설정 센터 업데이트를 통해 사용자를 더블 옵트인 워크플로에 입력하는 방법을 설명합니다."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# 이중 옵트인

> 더블 옵트인 기능은 사용자가 SMS, MMS 또는 RCS 메시지를 받을 수 있도록 하기 전에 명시적으로 옵트인 의사를 확인하도록 요구할 수 있게 해줍니다. 이는 채널에 참여할 가능성이 있는 사용자 또는 이미 참여하고 있는 사용자에게 초점을 맞추고, 준수 모범 사례를 따르는 데 도움이 됩니다.

더블 옵트인이 활성화되면, 사용자는 캠페인이나 캔버스에서 메시지를 받을 수 있도록 하기 전에 명시적인 동의를 요청하는 메시지를 받습니다. 

1991년 전화 소비자 보호법(TCPA)의 명시적인 요구 사항은 아니지만, Braze는 사용자가 SMS, MMS 또는 RCS 프로그램의 일원이 되는 것에 대해 인지하고 동의하고 있음을 확인하기 위해 더블 옵트인을 구성할 것을 권장합니다. 준수에 대한 자세한 정보는 [Laws, regulations, and abuse prevention for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)를 참조하십시오.

## 더블 옵트인 워크플로

더블 옵트인은 인바운드 및 아웃바운드 옵트인 캠페인을 통해 명시적인 동의를 얻을 수 있게 해줍니다.

### 아웃바운드

사용자가 전화번호를 제공하면, 동의를 요청하는 메시지가 전송됩니다.

![브랜드 문자 메시지의 스크린샷, "BRAND 문자 업데이트에 오신 것을 환영합니다!" 최신 제안을 위해 주당 1개의 메시지. "Y"라고 답장하여 옵트인합니다."Y"라고 답장하는 사용자와 "감사합니다!"라고 응답하는 브랜드. 이제 BRAND 알림을 수신하도록 옵트인했습니다. 여기 첫 구매 시 10% 할인 코드 SMS10이 있습니다!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### 인바운드

사용자가 옵트인 키워드를 포함한 메시지를 보내면, 동의를 요청하는 메시지가 전송됩니다.

![사용자가 "JOIN"을 보내고 "우리 SMS 프로그램에 가입하려면 Y를 회신하세요."라는 응답을 받는 수신 SMS 메시지의 스크린샷. 주 3회 메시지, 언제든지 STOP을 입력하여 중지할 수 있으며, 그 후 "Y"를 다시 입력하십시오.]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## 더블 옵트인 활성화

더블 옵트인을 활성화하려면, 해당 구독 그룹의 **Global Keywords** 테이블로 이동하여 **Edit**를 클릭하십시오 **Opt-In Keyword Category**. 다음으로, 옵트인 방법(**옵트인** 또는 **더블 옵트인**)을 선택하세요. **더블 옵트인**을 선택하면 추가 [구성 가능한 필드](#configurable-fields)를 표시하도록 페이지가 확장됩니다.

![옵트인 방법 섹션에는 두 가지 옵트인 방법이 있습니다: 옵트인 및 더블 옵트인.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### 구성 가능한 필드 {#configurable-fields}

| 카테고리   |    필드    | 설명   
| ----------- |----------- |---------------- 
| 옵트인 안내 | 키워드 | 사용자가 옵트인 의도를 나타내기 위해 문자로 보낼 수 있는 키워드입니다. `START`은(는) 필수 키워드입니다. 이 옵트인 안내는 [구독 소스](#subscription-sources) 섹션에 나열된 소스에 의해 구독 상태가 업데이트될 때 사용자에게도 전송됩니다.
| | 회신 메시지 | 이것은 사용자가 옵트인 키워드(예: "이 번호로부터 메시지를 받으려면 Y로 회신하십시오.")를 문자로 보낸 후 받게 되는 초기 응답입니다. 메시지 및 데이터 요금이 적용될 수 있습니다."
| 이중 옵트인 확인 | 키워드 | 이것들은 사용자가 옵트인 의도를 확인하기 위해 응답할 수 있는 키워드입니다. 적어도 하나의 키워드가 필요합니다. 이 키워드는 **옵트인 안내 응답 메시지** 필드에 지정해야 합니다.
| | 회신 메시지 | 이는 사용자가 명시적으로 옵트인을 확인한 후 받게 되는 확인 응답입니다. 사용자의 구독 그룹 상태는 `Subscribed`로 설정됩니다.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 옵트인 안내를 받으면, 옵트인 의도를 확인하는 데 30일이 있습니다. 사용자가 30일 후에 가입하려면, 더블 옵트인 워크플로를 다시 시작하기 위해 옵트인 키워드를 문자로 보내야 합니다.

![구성 가능한 필드는 두 개의 섹션, 옵트인 안내 및 더블 옵트인 확인으로 나뉘며, 각 섹션에는 키워드 및 응답 메시지 필드가 있습니다.]({% image_buster /assets/img/double_opt_in_fields.png %})

## 구독 그룹 상태

사용자가 더블 옵트인 워크플로를 완료한 후에만 그들의 [subscription group status]({{site.baseurl}}/sms_rcs_subscription_groups/)가 `Subscribed`로 업데이트됩니다. 사용자가 워크플로를 시작하지만 완료하지 않으면, 그들은 `Unsubscribed` 상태로 남아 해당 구독 그룹에서 메시지를 받을 수 없습니다.

사용자는 [subscribed from other sources]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (예: REST API, SDK)인 경우에도 더블 옵트인 워크플로에 입력될 수 있습니다.

## 구독 소스 {#subscription-sources}

사용자는 수신 메시지 외부에서 발생하는 구독 업데이트를 통해 이중 옵트인 워크플로에 들어갈 수 있습니다. 이러한 소스에는 REST API, 소프트웨어 개발 키트 및 환경 설정 센터의 업데이트가 포함됩니다. 사용자가 이러한 소스를 통해 이중 옵트인 워크플로에 들어가면 **옵트인 안내 메시지**를 받게 됩니다.

각 구독 소스는 다음 표에 설명된 대로 다른 등록 동작을 가지고 있습니다.

소스    | 더블 옵트인 등록 행동   
----------- | -----------
SDK | 사용자는 Braze SDK를 통해 구독할 때 자동으로 이중 옵트인 워크플로에 들어갑니다.
REST API | 사용자는 구독 상태가 `/subscription/status/set`, `/v2/subscription/status/set` 또는 `/users/track`을 통해 설정되고 선택적 매개변수 `use_double_opt_in_logic`가 `true`로 전달될 때 워크플로에 들어갈 수 있습니다 (예: [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). 이 매개변수가 생략되면 사용자는 이중 옵트인 워크플로에 들어가지 않습니다.
Shopify | 사용자의 구독 상태가 Shopify 통합에 의해 설정될 때 사용자는 이중 옵트인 워크플로에 들어가지 않습니다.
사용자 가져오기 | 사용자의 구독 상태가 사용자 가져오기에 의해 설정될 때 사용자는 이중 옵트인 워크플로에 들어가지 않습니다.
[환경설정 센터]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | 사용자는 선호 센터를 통해 구독할 때 자동으로 이중 옵트인 워크플로에 들어갑니다.
사용자 업데이트 단계 | 사용자는 사용자 업데이트 단계에서 구독 상태가 설정되고 선택적 매개변수 `use_double_opt_in_logic`가 `true`로 전달될 때 이중 옵트인 워크플로에 들어갈 수 있습니다. 이 매개변수가 생략되면 사용자는 이중 옵트인 워크플로에 들어가지 않습니다.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 다국어 지원
수신 메시지의 경우, 이중 옵트인은 구독 그룹에 정의된 모든 언어를 지원합니다. 이는 자동 응답을 다양한 언어로 정의할 수 있으며, 일치하는 키워드가 수신되면 특정 언어와 연결된 자동 응답을 Braze가 전송한다는 것을 의미합니다.

수신 메시지 외부에서 발생하는 구독 업데이트를 통해 이중 옵트인 워크플로에 들어가는 사용자(예: SDK, REST API, Shopify)는 영어 키워드만 전송됩니다.


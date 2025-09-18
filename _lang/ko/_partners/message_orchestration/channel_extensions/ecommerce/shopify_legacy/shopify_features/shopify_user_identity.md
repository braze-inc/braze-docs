---
nav_title: Shopify 사용자 ID 관리
article_title: "Shopify 사용자 ID 관리"
description: "이 참고 문서에서는 Shopify 사용자 ID 관리 기능에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Shopify 사용자 ID 관리

> Braze는 현장 행동을 통해 그리고 통합의 일부로 구성한 Shopify 웹훅을 수신 대기하여 Shopify 고객으로부터 신호를 수신합니다. 헤드리스가 아닌 Shopify 사이트의 경우 Braze가 결제 페이지에서 사용자를 조정하는 데 도움을 줍니다. 헤드리스 Shopify 사이트의 경우 [결제에서 사용자를 조정]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-checkout)하는 방법에 대한 통합 지침을 참조하세요.

## 사용자 프로필에 대한 정보 캡처 

### Shopify 사용자 추적

스토어 방문자가 게스트(즉, 익명)인 경우 Braze는 해당 특정 고객의 세션에 대해 `device_id` 을 캡처합니다. [웹 SDK를 구현하는]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) 동안 Shopify 양식에 대한 사용자 조정을 설정하면 고객이 양식에 정보를 입력할 때마다 고객 이메일이 익명 사용자 프로필에 추가됩니다. 

스토어 방문자가 Shopify 뉴스레터 또는 이메일 캡처 양식에 이메일을 입력하면 Braze는 사용자 프로필을 생성하는 Shopify 웹훅 이벤트를 수신합니다. 그런 다음 Braze는 이 사용자 프로필을 웹 SDK에서 추적하는 익명 사용자 프로필과 병합하고 사용자 프로필의 사용자 별칭으로 Shopify 고객 ID를 할당합니다. 

고객이 결제를 진행하고 전화번호와 같은 기타 식별 가능한 정보를 제공하면 Braze는 Shopify 웹훅에서 관련 사용자 데이터를 캡처하여 `device_id` 을 사용하여 익명 사용자와 병합해야 합니다.
- 헤드리스가 없는 Shopify 사이트 또는 Google 태그 관리자를 통해 Shopify ScriptTag를 통해 웹 SDK를 구현한 경우 Braze는 결제 페이지의 사용자 데이터와 익명 사용자 프로필의 세션 데이터가 할당된 Shopify 고객 ID가 있는 사용자 별칭 프로필에 자동으로 병합되도록 합니다.
- Shopify 헤드리스 사이트에서 웹 SDK를 구현한 경우 결제 페이지 내에서 제출된 사용자 데이터가 웹 SDK 또는 API를 통해 올바른 사용자 프로필에 적절하게 할당되었는지 확인해야 합니다. 자세한 내용은 [헤드리스 Shopify 사이트에 직접 웹 SDK 구현]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-site)을 확인하세요.

고객이 결제 프로세스를 계속 진행하면 Braze는 입력한 이메일 주소, 전화 번호 또는 Shopify 고객 ID가 기존 사용자 프로필과 일치하는지 확인합니다. 일치하는 항목이 있는 경우 Braze는 Shopify 사용자 데이터를 해당 프로필에 동기화합니다.

이메일 주소 또는 전화 번호가 여러 개의 식별된 사용자 프로필과 연결되어 있는 경우 Braze는 가장 최근 활동이 있는 프로필에 Shopify 데이터를 동기화합니다.

이메일 주소나 전화번호와 일치하는 이메일 주소나 전화번호를 찾지 못하면 Braze는 지원되는 Shopify 데이터로 새 사용자 프로필을 생성합니다.

### Shopify 고객이 Braze와 동기화할 때

Braze는 Shopify 스토어에서 캡처한 리드, 가입 및 계정 등록에 대해 기존 사용자 프로필을 업데이트하거나 새 프로필을 생성합니다. Shopify 등에서 다음과 같은 방법으로 사용자 프로필 데이터를 수집할 수 있습니다:
- 고객이 계정을 생성합니다.
- 고객 이메일 주소 또는 전화 번호는 Shopify 캡처 양식에서 수집됩니다.
- 고객 이메일 주소는 뉴스레터 양식에서 수집됩니다.
- 고객 이메일 주소 또는 전화 번호는 EcomSend와 같이 Shopify에 연결된 타사 도구를 통해 수집됩니다.

Braze는 먼저 고객의 이메일 주소 또는 전화번호를 사용하여 지원되는 Shopify 데이터를 기존 사용자 프로필에 매핑하려고 시도합니다. 

사용자 프로필 중복을 방지하려면 [Shopify 웹사이트에 웹 SDK를 구현하는]() 데 사용한 방법에 대한 Shopify Forms 지침에 대한 사용자 조정을 검토하는 것이 중요합니다.

## 사용자 프로필 병합 

{% alert note %}
기본 Shopify 통합은 익명 사용자 프로필과 Shopify 별칭 프로필을 병합하는 데 도움이 되는 툴을 제공합니다. 헤드리스 Shopify 사이트에 통합을 구현하는 경우 [헤드리스 Shopify 사이트에 직접 웹 SDK 구현]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)을 검토하여 사용자를 올바르게 조정하고 있는지 확인합니다. <br><br> 중복된 고객 프로필이 있는 경우 [일괄 병합 툴]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/)을 사용하여 데이터를 간소화할 수 있습니다.
{% endalert %}

다음 중 하나와 일치하는 항목이 발견되면 Braze는 익명 고객 프로필의 필드를 식별된 고객 프로필에 병합합니다.
- Shopify 고객 ID
- 이메일
- 전화번호

Braze는 익명 사용자 프로필에서 식별된 사용자 프로필로 다음 필드를 병합합니다:
- 이름
- 성
- 이메일
- 성별
- 생년월일
- 전화번호
- 시간대
- 출생지
- 국가
- 언어
- 사용자 지정 속성
    - 커스텀 이벤트 및 구매 이벤트 데이터(이벤트 속성, 개수, 첫 날짜와 마지막 날짜 타임스탬프 제외)
    - "Y일 동안 X회" 세분화에 대한 사용자 지정 이벤트 및 구매 이벤트 속성(여기서 X<=50, Y<=30)
- 푸시 토큰
- 메시지 기록
- 사용자 지정 이벤트, 구매 이벤트 수, 첫 날짜 및 마지막 날짜 타임스탬프 등 익명 사용자 프로필 또는 식별된 사용자 프로필에 있는 다음 필드 중 하나입니다.
    - 이렇게 병합된 필드는 'Y일 동안의 X 이벤트에 대해' 필터를 업데이트합니다. 구매 이벤트의 경우 이러한 필터에는 'Y일 내 구매 횟수' 및 '지난 Y일 동안 지출한 금액'이 포함됩니다.

{% alert important %}
세션 데이터는 아직 병합 프로세스의 일부로 지원되지 않습니다.
{% endalert %}

## Shopify 가입자 동기화

Shopify 설정 프로세스 중에 Braze는 고객 이메일 주소 및 SMS 옵트인 상태를 Braze 사용자 프로필의 가입 그룹 및 가입 상태에 동기화할 수 있는 유연한 제어 기능을 제공합니다. 

### 이메일 또는 SMS 구독자 수집

Braze에서 Shopify 스토어를 설정하는 동안 이메일 및 SMS 구독자를 Shopify에서 Braze로 동기화하는 옵션이 제공됩니다. 

#### 이메일 구독자 수집

이메일 구독자 수집을 사용하도록 설정하려면 Shopify 설정에서 해당 기능을 켭니다. Shopify 이메일 구독자와 같이 Braze [구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups)을 하나 이상 할당하는 것이 좋습니다. Braze는 이메일 구독자를 지정된 구독 그룹에 추가하여 메시지를 보낼 때 오디언스 타겟팅에 포함되도록 합니다. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

사용하도록 설정하면 Braze는 Shopify 이메일 가입자의 업데이트와 이메일 가입 상태 업데이트를 실시간으로 동기화합니다. 재정의 옵션을 활성화하지 않으면 Shopify 스토어와 연결된 구독 그룹에서 Shopify 고객이 가입하거나 탈퇴합니다.

재정의 옵션을 활성화하면 Braze는 고객 프로필에서 글로벌 가입 상태를 업데이트합니다. 즉, 고객이 Shopify에서 구독 취소로 표시된 경우 Braze는 사용자 프로필에서 글로벌 가입 상태를 구독 취소로 표시하고 사용 가능한 모든 이메일 가입 그룹에서 해당 고객의 가입을 취소합니다. 따라서 전 세계적으로 이메일에서 탈퇴한 사용자에게는 메시지가 전송되지 않습니다.

#### SMS 구독자 수집

Shopify에서 SMS 구독자를 수집하려면 [SMS 설정]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup)의 일부로 [SMS 구독 그룹]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/)을 생성해야 합니다. 

Shopify SMS 구독자를 수집할 준비가 되면 Shopify 설정 페이지에서 SMS 구독자 수집을 활성화합니다. SMS 메시지를 적절하게 타겟팅하고 보낼 수 있도록 하나 이상의 SMS 구독 그룹을 선택해야 합니다. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

활성화하면 Braze는 Shopify SMS 가입자의 업데이트와 해당 가입자의 SMS 가입 상태를 실시간으로 동기화합니다. 재정의 옵션을 활성화하지 않으면 Shopify 스토어와 연결된 구독 그룹에서 Shopify 고객이 가입하거나 탈퇴합니다.

SMS 구독자에게는 글로벌 가입 상태가 없으므로 재정의 옵션을 사용할 때 이를 고려할 필요가 없습니다. 사용자는 SMS 구독 그룹에 대해서만 가입 또는 탈퇴가 가능합니다.

#### 레거시 사용자 지정 속성

기존 Shopify 고객은 `shopify_accepts_marketing` 및 `shopify_sms_consent` 사용자 지정 속성을 통해 이메일 및 SMS 가입자를 수집하는 기존 방법을 사용할 수 있습니다. 위의 설정을 재정의가 활성화된 상태로 저장하면 Braze는 사용자 프로필에서 사용자 지정 속성을 제거하고 해당 값을 각각의 이메일 구독 그룹 및 SMS 구독 그룹에 동기화합니다.

이러한 레거시 사용자 지정 속성을 사용하는 기존 캠페인 또는 캔버스가 있는 경우 해당 속성을 제거하고 캠페인 또는 캔버스가 적절한 구독 상태, 그룹 또는 둘 다를 사용하고 있는지 확인합니다.

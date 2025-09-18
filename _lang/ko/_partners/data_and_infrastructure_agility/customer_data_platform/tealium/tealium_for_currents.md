---
nav_title: 전류용 테일륨
article_title: 전류용 테일륨
page_order: 3
alias: /partners/tealium_for_currents/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Braze Currents와 Tealium의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# 전류용 테일륨

> [Tealium](https://www.tealium.com)은 여러 소스로부터 정보를 수집하여 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼입니다.

Braze와 Tealium의 통합을 통해 두 시스템 간의 정보 흐름을 원활하게 제어할 수 있습니다. 이제 커런츠를 사용하면 데이터를 Tealium에 연결하여 전체 성장 스택에서 실행 가능한 데이터로 만들 수 있습니다. 

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Tealium EventStream 또는 Tealium AudienceStream | 이 파트너십을 이용하려면 [Tealium 계정이](https://my.tealiumiq.com/) 필요합니다. |
| 커런츠 | 데이터를 Tealium으로 다시 내보내려면 계정에 [Braze 커런츠]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)를 설정해야 합니다. |
| Tealium URL | 이 정보는 Tealium 대시보드로 이동하고 수집 URL을 복사하면 얻을 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Tealium 내에서 Braze용 데이터 소스 만들기

데이터 소스 생성에 대한 지침은 [Tealium](https://docs.tealium.com/server-side/data-sources/webhooks/braze-currents/) 사이트에서 확인할 수 있습니다. 완료되면 Tealium은 다음 단계에서 사용할 수 있도록 복사할 데이터 소스 URL을 제공합니다.

### 2단계: 현재 만들기

Braze에서 **커런츠 > + 커런츠 생성 > Tealium 내보내기**로 이동합니다. 통합 이름, 연락처 이메일, Tealium URL을 제공합니다. 다음으로, 사용 가능한 이벤트 목록에서 추적할 이벤트를 선택합니다. 마지막으로, **커런츠 시작**을 클릭합니다.

Tealium으로 전송되는 모든 이벤트에는 사용자의 `external_user_id`가 포함됩니다. 현재 Braze는 `external_user_id` 설정이 없는 사용자에 대해서는 이벤트 데이터를 Tealium으로 전송하지 않습니다.

{% alert important %}
Tealium URL을 최신 상태로 유지하는 것이 중요합니다. 커넥터의 URL이 올바르지 않으면 Braze에서 이벤트를 전송할 수 없습니다. **48시간** 넘게 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## 통합 세부 정보

Braze는 [커런츠 이벤트 용어집에]({{site.baseurl}}/user_guide/data/braze_currents/) 나열된 모든 데이터( [메시지 참여]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) 및 [고객 행동]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) 이벤트의 모든 속성 포함)를 Tealium으로 내보낼 수 있도록 지원합니다.

내보낸 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일하며, [커스텀 HTTP 커넥터의 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 확인할 수 있습니다.
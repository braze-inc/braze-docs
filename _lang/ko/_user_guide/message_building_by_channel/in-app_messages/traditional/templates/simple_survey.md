---
nav_title: "간단한 설문조사"
article_title: 앱 내 간단한 설문조사 메시지
page_order: 1.5
page_type: reference
description: "이 참조 문서에서는 앱 내 메시지 설문조사를 사용하여 캠페인 전략을 강화하기 위해 사용자 속성, 통찰력 및 선호도를 수집하는 방법을 다룹니다."
channel:
  - in-app messages
tool:
  - Templates
---

# 간단한 설문조사

> **간단한 설문조사** 앱 내 메시지 템플릿을 사용하여 캠페인 전략을 강화하는 사용자 속성, 통찰력 및 선호도를 수집하세요. 

예를 들어, 사용자에게 앱 사용 방법, 개인 선호도에 대한 정보, 또는 특정 기능에 대한 만족도를 물어볼 수 있습니다.

\![세 가지 간단한 설문조사 메시지: 알림 선호도, 식이 선호도, 고객 만족도 설문조사. 설문조사에서 선택된 옵션은 해당 사용자에 대해 기록될 사용자 정의 속성에 해당합니다.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK 요구 사항 {#supported-sdk-versions}

이 앱 내 메시지는 [Flex CSS](https://caniuse.com/flexbox)를 지원하는 장치에만 전달되며, 최소한 다음 [SDK 버전]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)이 필요합니다. 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Web SDK를 통해 HTML 앱 내 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다.
{% endalert %}

## 설문조사 만들기 {#create}

앱 내 메시지 [생성]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) 시, **간단한 설문조사**를 **메시지 유형**으로 선택하세요.

이 설문조사 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다. 이 기능에 필요한 [최소 SDK 버전](#supported-sdk-versions)이 SDK에 있는지 확인하세요.

### 1단계: 설문조사 질문 추가

설문조사를 시작하려면 질문을 설문조사 **헤더** 필드에 추가하세요. 원하는 경우, 설문조사 질문 아래에 표시될 선택적 **본문** 메시지를 추가할 수 있습니다.

\![간단한 설문 편집기의 Compose 탭, 헤더, 선택적 본문 및 선택적 도움말 텍스트에 대한 필드가 있습니다.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
이 필드에는 Liquid와 이모지를 모두 포함할 수 있으므로 멋지게 꾸며보세요!
{% endalert %}

### 2단계: 선택지 구성 {#single-multiple-choice}

설문조사에 최대 12개의 선택지를 추가할 수 있습니다.

**단일 선택 선택** 또는 **다중 선택 선택** 중 하나를 선택하세요. **도움말 텍스트**는 두 옵션 간에 전환할 때 자동으로 업데이트되어 사용자가 선택할 수 있는 선택지 수를 알 수 있도록 합니다. 

그런 다음 [사용자 정의 속성 수집](#custom-attributes) 또는 [응답만 기록](#no-attributes)할 것인지 결정하세요.

\!["제출 시 속성 기록"이 선택된 선택지 드롭다운.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### 사용자 정의 속성 수집 {#custom-attributes}

사용자의 제출을 기반으로 속성을 수집하려면 **제출 시 속성 기록**을 선택하세요. 이 옵션을 사용하여 새로운 세그먼트 및 리타겟팅 캠페인을 만들 수 있습니다. 예를 들어, [만족도 조사](#user-satisfaction)에서는 불만족한 모든 사용자에게 후속 이메일을 보낼 수 있습니다.

각 선택지에 사용자 정의 속성을 추가하려면 드롭다운 메뉴에서 사용자 정의 속성 이름을 선택(또는 새로 만들기)한 다음, 이 선택지가 제출될 때 설정할 값을 입력하세요. [설정 페이지]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/)에서 새 사용자 정의 속성을 만들 수도 있습니다.

사용자 정의 속성의 데이터 유형은 설문조사를 설정한 방식에 따라 중요합니다.

- **다중 선택 선택:** 사용자 정의 속성의 데이터 유형은 배열이어야 합니다. 사용자 정의 속성이 다른 데이터 유형으로 설정되면 응답이 기록되지 않습니다.
- **단일 선택:** 사용자 정의 속성의 데이터 유형은 _배열이 아니어야_ 합니다. 응답은 속성이 배열인 경우 기록되지 않습니다.

{% alert important %}
사용자 정의 속성 수집이 활성화되면 동일한 사용자 정의 속성 이름을 공유하는 선택지는 배열로 결합됩니다.
{% endalert %}

##### 예시 

예를 들어, [알림 기본 설정 설문조사](#notification-preferences)에서 각 선택지를 불리언(참/거짓) 속성으로 만들어 사용자가 관심 있는 주제를 선택할 수 있도록 할 수 있습니다. 사용자가 "프로모션" 선택지를 체크하면, 해당 사용자의 [사용자 프로필]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)이 사용자 정의 속성 `Promotions Topic`이 `true`로 설정되어 업데이트됩니다. 선택지를 체크하지 않으면, 동일한 속성은 변경되지 않습니다.

그런 다음 `Custom Attribute` 필터를 사용하여 사용자 정의 속성 `Promotions Topic` `is` `true`가 있는 사용자 세그먼트를 생성하여 프로모션에 관심 있는 사용자만 관련 캠페인을 받을 수 있도록 할 수 있습니다.

#### 응답 기록하기만 {#no-attributes}

또는 **응답만 기록하기(속성 없음)**을 선택할 수 있습니다. 이 옵션이 선택되면, 설문 응답은 버튼 클릭으로 기록되지만 사용자 정의 속성은 사용자 프로필에 기록되지 않습니다. 이는 각 설문 옵션에 대한 클릭 메트릭을 여전히 볼 수 있음을 의미합니다(참조 [분석](#analytics)), 그러나 해당 선택은 사용자 프로필에 반영되지 않습니다.

이 클릭 메트릭은 리타겟팅에 사용할 수 없습니다.

### 4단계: 제출 동작 선택

사용자가 응답을 제출하면, 선택적으로 확인 페이지를 표시하거나 메시지를 단순히 닫을 수 있습니다.

확인 페이지는 사용자의 시간에 감사하거나 추가 정보를 제공하기에 좋은 장소입니다. 이 페이지의 클릭 유도 문안을 사용자 앱 또는 웹사이트의 다른 페이지로 안내하도록 사용자 정의할 수 있습니다.

**제출 버튼** 섹션에서 버튼 텍스트와 클릭 동작을 편집하세요 **설문조사** 탭의 하단에:

\![클릭 시 동작이 "응답 제출 및 확인 페이지 표시"로 설정됨.]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

확인 페이지를 추가하기로 선택한 경우, 메시지를 사용자 정의하려면 **확인 페이지** 탭으로 전환하십시오:

\![간단한 설문 편집기의 확인 페이지 탭. 사용 가능한 필드는 헤더, 선택적 본문, 버튼 텍스트 및 버튼 클릭 동작입니다.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

사용자를 앱 또는 웹사이트의 다른 페이지로 안내하려면 버튼의 **클릭 동작**을 변경하십시오.

### 5단계: 메시지를 스타일화하십시오(선택 사항) {#styling}

메시지의 글꼴 색상과 강조 색상을 **색상 테마** 선택기를 사용하여 사용자 정의할 수 있습니다.

\![사용자가 색상 팔레트를 클릭한 후 색상 테마 선택기가 확장된 간단한 설문 편집기의 작성 탭.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## 결과 분석 {#analytics}

캠페인이 시작되면 실시간으로 결과를 분석하여 각 선택 항목의 세부 사항을 확인할 수 있습니다. [사용자 정의 속성 수집](#custom-attributes)을 활성화한 경우, 설문을 제출한 사용자에 대한 새로운 세그먼트 또는 후속 캠페인을 생성할 수 있습니다.

{% alert note %}
삭제된 설문 선택지는 여전히 분석에 나타나지만 새로운 사용자에게는 선택 항목으로 표시되지 않습니다.
{% endalert %}

특정 변형의 **앱 내 메시지 성과** 섹션에서 **결과** 드롭다운을 확장하여 설문 성과 지표를 찾을 수 있습니다. 다음은 당신이 볼 수 있는 세부 사항입니다:

- **설문 참여**은 사용자가 설문에 어떻게 상호작용했는지를 보여주며, 총 제출 수, 거부 수 및 메시지 본문 내 클릭 수를 포함합니다.
- **설문 결과**은 각 응답 옵션을 선택한 사용자 수의 세부 사항과 각 선택이 나타내는 총 제출 수의 비율을 표시합니다.
- **확인 페이지 메트릭** (활성화된 경우)은 몇 명의 사용자가 확인 화면을 보고, 버튼을 클릭하거나 상호작용 없이 거부했는지를 포함합니다.

설문 메트릭의 정의는 [보고서 메트릭 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)을 참조하고 "앱 내 메시지"로 필터링하십시오.

캠페인 메트릭의 세부 사항을 보려면 [앱 내 메시지 보고]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)를 확인하십시오.

### 현재 {#currents}

선택한 선택 사항은 [**앱 내 메시지 클릭 이벤트**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` 필드로 자동으로 흐릅니다. 각 선택 사항은 고유 식별자(UUID)와 함께 전송됩니다.

## 사용 사례

{% tabs %}
{% tab User satisfaction %}

### 사용자 만족도

**목표:** 고객 만족도를 측정하고 낮은 점수를 남긴 사용자에게 재유치 캠페인을 보냅니다.

이를 설정하려면 “😡 매우 불만족”에서 “😍 매우 만족”까지 다섯 가지 옵션이 있는 단일 선택 설문조사를 사용하세요. 각 선택 사항은 사용자 정의 속성 `customer_satisfaction`에 매핑되며, 1에서 5까지의 숫자 값이 있습니다. 여기서 1은 가장 불만족을 나타내고 5는 가장 만족을 나타냅니다.

| 선택 사항                                | 속성              | 값 |
|---------------------------------------|------------------------|-------|
| 😡 매우 불만족                  | `customer_satisfaction` | 1     |
| 😟 불만족                       | `customer_satisfaction` | 2     |
| 🙂 만족도 중립 | `customer_satisfaction` | 3     |
| 😊 만족                          | `customer_satisfaction` | 4     |
| 😍 매우 만족함                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 설문조사를 제출하면 선택한 값이 사용자 정의 속성으로 기록됩니다. 그런 다음 청중 필터를 사용하여 후속 캠페인을 구축할 수 있습니다. 예를 들어, `customer_satisfaction` 속성이 1 또는 2인 사용자에게 재유치 메시지를 타겟팅합니다.

{% endtab %}
{% tab Notification preferences %}

### 알림 기본 설정

**목표:** 사용자가 특정 유형의 알림에 선택할 수 있도록 합니다.

이를 설정하려면 각 선택지가 알림 주제를 나타내는 다중 선택 설문조사를 사용하세요. 같은 속성에 다른 값을 할당하는 대신, 각 선택지는 사용자의 해당 주제에 대한 관심을 반영하는 고유한 불리언 속성에 매핑됩니다. 사용자가 선택을 하면 해당 속성이 `true`로 설정됩니다. 선택하지 않으면 속성은 변경되지 않습니다.

| 선택 사항             | 속성              | 값  |
|--------------------|------------------------|--------|
| 제품 업데이트    | `wants_product_updates`| `true` |
| 프로모션         | `wants_promotions`     | `true` |
| 이벤트 초대      | `wants_event_invites`  | `true` |
| 설문조사 & 피드백 | `wants_surveys`        | `true` |
| 팁 & 튜토리얼   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### 고객 목표 식별

**목표:** 사용자가 귀하의 앱을 방문하는 주요 이유를 식별합니다.

이를 설정하려면 각 옵션이 일반적인 목표 또는 의도를 나타내는 단일 선택 설문조사를 사용하세요. 각 선택지는 선택된 사용자 의도에 해당하는 값으로 사용자 정의 속성 `product_goal`에 매핑됩니다.

| 선택 사항                     | 속성       | 값     |
|----------------------------|------------------|-----------|
| 상태 확인            | `product_goal`   | `status`  |
| 계정 업그레이드       | `product_goal`   | `upgrade` |
| 약속 예약  | `product_goal`   | `schedule`|
| 고객 지원           | `product_goal`   | `support` |
| 그냥 둘러보기              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 설문조사를 제출하면 선택한 값이 프로필의 사용자 정의 속성으로 기록됩니다. 그런 다음 이 데이터를 사용하여 향후 경험을 개인화하거나 사용자의 주요 목표에 따라 세분화할 수 있습니다.

{% endtab %}
{% tab Improve conversion rates %}

### 전환율 개선

**목표:** 고객이 업그레이드하거나 구매하지 않는 이유를 이해합니다.

이를 설정하려면 각 옵션이 업그레이드에 대한 일반적인 장벽을 나타내는 단일 선택 설문조사를 사용하십시오. 각 선택지는 사용자 정의 속성 `upgrade_reason`에 매핑되며, 해당 값은 사용자의 선택을 반영합니다.

| 선택 사항              | 속성        | 값       |
|---------------------|------------------|-------------|
| 너무 비쌈       | `upgrade_reason` | `expensive` |
| 가치 없음        | `upgrade_reason` | `value`     |
| 사용하기 어려움    | `upgrade_reason` | `difficult` |
| 경쟁사 사용  | `upgrade_reason` | `competitor`|
| 기타 이유        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 설문조사를 제출하면 선택한 값이 프로필에 저장됩니다. 그런 다음 이러한 사용자에게 할인 제안이나 사용성 개선과 같은 특정 반대 의견에 맞춘 캠페인으로 타겟팅할 수 있습니다.

{% endtab %}
{% tab Favorite features %}

### 좋아하는 기능

**목표:** 고객이 즐겨 사용하는 기능을 이해합니다.

이 설정을 하려면 각 옵션이 앱의 기능을 나타내는 다중 선택 설문조사를 사용하세요. 각 선택지는 사용자 정의 속성 `favorite_features`에 매핑되며, 사용자가 설문조사를 제출하면 속성이 선택된 값의 배열로 설정됩니다.

| 선택 사항            | 속성          | 값        |
|-------------------|--------------------|--------------|
| 북마크         | `favorite_features`| `bookmarks`  |
| 모바일 앱        | `favorite_features`| `mobile`     |
| 게시물 공유     | `favorite_features`| `sharing`    |
| 고객 지원  | `favorite_features`| `support`    |
| 맞춤화     | `favorite_features`| `custom`     |
| 가격 / 가치     | `favorite_features`| `value`      |
| 커뮤니티         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

이 설문조사는 다중 선택을 사용하므로 사용자의 프로필은 선택된 모든 기능 값의 목록으로 업데이트됩니다.

{% endtab %}
{% endtabs %}

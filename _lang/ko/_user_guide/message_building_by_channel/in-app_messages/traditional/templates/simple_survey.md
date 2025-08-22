---
nav_title: "간단한 설문조사"
article_title: 간단한 설문조사 인앱 메시지
page_order: 1.5
page_type: reference
description: "이 참고 문서에서는 인앱 메시지 설문조사를 사용하여 캠페인 전략을 강화하기 위해 사용자 속성, 인사이트 및 선호도를 수집하는 방법을 설명합니다."
channel:
  - in-app messages
tool:
  - Templates
---

# 간단한 설문 조사

> **간단한 설문조사** 인앱 메시지 템플릿을 사용하여 캠페인 전략을 강화하는 사용자 속성, 인사이트 및 선호도를 수집할 수 있습니다. 

예를 들어, 사용자에게 앱 사용 방법을 묻거나, 개인 선호도에 대해 자세히 알아보고, 특정 기능에 대한 만족도를 물어볼 수 있습니다.

![알림 선호도, 식단 선호도, 고객 만족 설문조사의 세 가지 간단한 설문조사 메시지입니다. 설문조사에서 선택한 옵션은 해당 사용자에 대해 기록될 사용자 지정 속성에 해당합니다.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK 요구 사항 {#supported-sdk-versions}

이 인앱 메시지는 [Flex CSS](https://caniuse.com/flexbox)를 지원하는 기기에만 전달되며, 최소 다음 [SDK 버전]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)이 설치되어 있어야 합니다. 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
웹 SDK를 통해 HTML 인앱 메시지를 활성화하려면 Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다.
{% endalert %}

## 설문조사 만들기 {#create}

[인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)를 작성할 때 **메시지 유형**으로 **간편 설문조사**를 선택합니다.

이 설문조사 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다. 이 기능을 사용하는 데 필요한 [최소 SDK 버전](#supported-sdk-versions)이 있는지 확인하세요.

### 1단계: 설문조사 질문 추가

설문조사 작성을 시작하려면 설문조사 **헤더** 필드에 질문을 추가합니다. 원하는 경우 설문조사 질문 아래에 표시할 **본문** 메시지(선택 사항)를 추가할 수 있습니다.

![간단한 설문조사 편집기의 작성 탭에는 머리글, 본문(선택 사항), 헬퍼 텍스트(선택 사항) 필드가 있습니다.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
이 필드에는 Liquid와 이모티콘을 모두 포함할 수 있으므로 멋지게 꾸며보세요!
{% endalert %}

### 2단계: 선택 사항 구성 {#single-multiple-choice}

설문조사에 최대 12개의 선택 항목을 추가할 수 있습니다.

**단답형 선택** 또는 **객관식 선택** 중 하나를 선택합니다. 두 옵션 사이를 전환할 때 **도우미 텍스트가** 자동으로 업데이트되어 사용자가 선택할 수 있는 선택 항목의 수를 알려줍니다. 

그런 다음 [사용자 지정 속성을 수집할지](#custom-attributes) 아니면 [응답만 기록할지](#no-attributes) 결정합니다.

!["제출 시 속성 로그"가 선택된 선택 드롭다운.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### 커스텀 속성 수집 {#custom-attributes}

**제출 시 속성 로그**를 선택하여 사용자의 제출을 기반으로 속성을 수집합니다. 이 옵션을 사용하여 새 세그먼트와 리타겟팅 캠페인을 만들 수 있습니다. 예를 들어 [만족도 설문조사에서](#user-satisfaction) 만족스럽지 않은 모든 사용자에게 후속 이메일을 보낼 수 있습니다.

각 선택 항목에 사용자 지정 속성을 추가하려면 드롭다운 메뉴에서 사용자 지정 속성 이름을 선택하거나 새 이름을 만든 다음 이 선택 항목이 제출될 때 설정할 값을 입력합니다. [설정 페이지에서]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) 새 사용자 지정 속성을 만들 수도 있습니다.

사용자 지정 속성의 데이터 유형은 설문조사를 설정한 방식에 따라 달라집니다.

- **객관식 선택:** 사용자 지정 속성의 데이터 유형은 배열이어야 합니다. 사용자 지정 속성이 다른 데이터 유형으로 설정되어 있으면 응답이 기록되지 않습니다.
- **단수 선택:** 사용자 지정 속성의 데이터 유형은 배열이 _아니어야_ 합니다. 속성이 배열인 경우 응답이 기록되지 않습니다.

{% alert important %}
사용자 지정 속성 컬렉션이 활성화되면 동일한 사용자 지정 속성 이름을 공유하는 선택 항목이 배열로 결합됩니다.
{% endalert %}

##### 예시 

예를 들어 [알림 선호도 설문조사에서](#notification-preferences) 각 선택 항목을 부울(참/거짓) 속성으로 설정하여 사용자가 관심 있는 주제를 선택할 수 있도록 할 수 있습니다. 사용자가 "프로모션" 선택 항목을 선택하면 [고객 프로필]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)이 커스텀 속성 `Promotions Topic`이 `true`로 설정된 상태로 업데이트됩니다. 선택 항목을 선택하지 않으면 동일한 속성이 변경되지 않습니다.

그런 다음 `Custom Attribute` 필터를 사용하여 사용자 지정 속성 `Promotions Topic` `is` `true` 을 가진 사용자에 대한 세그먼트를 생성하여 프로모션에 관심이 있는 사용자만 관련 캠페인을 수신하도록 할 수 있습니다.

#### 응답만 로깅 {#no-attributes}

또는 **응답만 기록(속성 없음)**을 선택할 수도 있습니다. 이 옵션을 선택하면 설문조사 응답은 버튼 클릭으로 기록되지만 사용자 지정 속성은 사용자 프로필에 기록되지 않습니다. 즉, 각 설문조사 옵션에 대한 클릭 지표는 계속 볼 수 있지만( [애널리틱스](#analytics) 참조) 해당 선택 사항은 사용자 프로필에 반영되지 않습니다.

이러한 클릭 지표는 리타겟팅에 사용할 수 없습니다.

### 4단계: 제출 동작 선택

사용자가 응답을 제출하면 선택적으로 확인 페이지를 표시하거나 메시지를 닫을 수 있습니다.

확인 페이지는 사용자의 시간에 감사하거나 추가 정보를 제공할 수 있는 좋은 공간입니다. 이 페이지의 클릭 유도 문안을 사용자 지정하여 사용자를 앱이나 웹사이트의 다른 페이지로 안내할 수 있습니다.

**설문조사** 탭 하단의 **제출 버튼** 섹션에서 버튼 텍스트와 클릭 시 동작을 수정합니다:

![클릭 시 동작을 "응답 제출 및 확인 페이지 표시"로 설정합니다.]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

확인 페이지를 추가하기로 선택한 경우 **확인 페이지** 탭으로 전환하여 메시지를 사용자 지정합니다:

![간편 설문조사 편집기의 확인 페이지 탭으로 이동합니다. 사용 가능한 필드는 헤더, 본문(선택 사항), 버튼 텍스트, 버튼 클릭 시 동작입니다.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

사용자를 앱이나 웹사이트의 다른 페이지로 안내하려면 버튼의 **클릭 시 동작을** 변경하세요.

### 5단계: 메시지 스타일 지정(선택 사항) {#styling}

**색상 테마** 선택기를 사용하여 메시지의 글꼴 색상과 강조 색상을 사용자 지정할 수 있습니다.

![사용자가 색상 팔레트를 클릭한 후 색상 테마 선택기가 펼쳐진 상태에서 간단한 설문조사 편집기의 작성 탭을 클릭합니다.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## 결과 분석 {#analytics}

캠페인이 시작되면 실시간으로 결과를 분석하여 선택한 각 선택 항목의 세부 정보를 확인할 수 있습니다. [사용자 지정 속성 수집을](#custom-attributes) 사용 설정한 경우 설문조사에 참여한 사용자를 위한 새 세그먼트 또는 후속 캠페인을 만들 수도 있습니다.

{% alert note %}
삭제된 설문조사 선택 항목은 분석에 계속 표시되지만 새 사용자에게는 선택 항목으로 표시되지 않습니다.
{% endalert %}

분석의 **인앱 메시지 성과** 섹션에서 특정 변형에 대한 **결과** 드롭다운을 확장하여 설문조사 성과 지표를 찾을 수 있습니다. 다음은 표시되는 내용을 자세히 설명합니다:

- **설문조사 참여도는** 메시지 본문의 총 제출, 삭제 및 클릭 수를 포함하여 사용자가 설문조사와 전반적으로 어떻게 상호작용했는지를 보여줍니다.
- **설문조사 결과에는** 각 응답 옵션을 선택한 사용자 수와 각 선택 항목이 전체 제출물에서 차지하는 비율에 대한 분석이 표시됩니다.
- **확인 페이지 지표** (활성화된 경우)에는 확인 화면을 보거나 버튼을 클릭하거나 상호 작용하지 않고 화면을 닫은 사용자 수가 포함됩니다.

설문조사 측정기준의 정의는 [보고서 측정기준 용어집]({{site.baseurl}}/user_guide/data/report_metrics/)을 참조하고 "인앱 메시지"로 필터링하세요.

캠페인 지표에 대한 자세한 내용은 [인앱 메시지 리포팅을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) 확인하세요.

### 커런츠 {#currents}

선택한 선택 항목은 자동으로 커런츠 아래의 [**인앱 메시지 클릭 이벤트**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` 필드를 클릭합니다. 각 선택 항목은 UUID(범용 고유 식별자)와 함께 전송됩니다.

## 사용 사례

### 사용자 만족도

**목표:** 고객 만족도를 측정하고 낮은 점수를 남긴 사용자에게 윈백 캠페인을 보내세요.

이를 설정하려면 "😡 매우 불만족"에서 "😍 매우 만족"까지 5가지 옵션이 있는 단답형 선택 설문조사를 사용합니다. 각 선택 항목은 사용자 지정 속성 `customer_satisfaction` 에 매핑되며, 1에서 5까지의 숫자 값(1은 만족도가 가장 낮고 5는 가장 만족도가 높음을 나타냄)으로 표시됩니다.

| 선택                                | 속성              | 값 |
|---------------------------------------|------------------------|-------|
| 😡 매우 불만족                  | `customer_satisfaction` | 1     |
| 😟 불만족                       | `customer_satisfaction` | 2     |
| 🙂 만족하지도 불만족하지도 않음 | `customer_satisfaction` | 3     |
| 😊 만족                          | `customer_satisfaction` | 4     |
| 😍 매우 만족                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 설문조사를 제출하면 선택한 값이 사용자 지정 속성으로 기록됩니다. 그런 다음 오디언스 필터를 사용하여 후속 캠페인을 구축할 수 있습니다. 예를 들어, `customer_satisfaction` 속성이 1 또는 2인 사용자를 대상으로 윈백 메시지를 타겟팅합니다.

### 알림 환경설정

**목표:** 사용자가 특정 유형의 알림을 선택할 수 있도록 합니다.

이를 설정하려면 각 선택 항목이 알림 주제를 나타내는 객관식 선택 설문조사를 사용합니다. 동일한 속성을 다른 값으로 할당하는 대신, 각 선택 항목은 해당 주제에 대한 사용자의 관심사를 반영하는 별개의 부울 속성에 매핑됩니다. 사용자가 선택 항목을 선택하면 해당 속성이 `true` 로 설정됩니다. 선택하지 않으면 속성이 변경되지 않은 상태로 유지됩니다.

| 선택             | 속성              | 값  |
|--------------------|------------------------|--------|
| 제품 업데이트    | `wants_product_updates`| `true` |
| 프로모션         | `wants_promotions`     | `true` |
| 이벤트 초대      | `wants_event_invites`  | `true` |
| 설문조사 및 피드백 | `wants_surveys`        | `true` |
| 팁 및 튜토리얼   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 고객 목표 파악

**목표:** 사용자가 앱을 방문하는 주요 이유를 파악하세요.

이를 설정하려면 각 옵션이 공통의 목표 또는 의도를 나타내는 단답형 선택 설문조사를 사용합니다. 각 선택 사항은 선택한 사용자 의도에 해당하는 값으로 사용자 지정 속성 `product_goal` 에 매핑됩니다.

| 선택                     | 속성       | 값     |
|----------------------------|------------------|-----------|
| 상태 확인            | `product_goal`   | `status`  |
| 내 계정 업그레이드하기       | `product_goal`   | `upgrade` |
| 약속 예약하기  | `product_goal`   | `schedule`|
| 고객 지원           | `product_goal`   | `support` |
| 그냥 브라우징              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 설문조사를 제출하면 선택한 값이 프로필에 사용자 지정 속성으로 기록됩니다. 그런 다음 이 데이터를 사용하여 향후 경험을 개인화하거나 주요 목표에 따라 사용자를 세분화할 수 있습니다.

### 전환율 향상

**목표:** 고객이 업그레이드나 구매를 하지 않는 이유를 파악하세요.

이를 설정하려면 각 옵션이 업그레이드의 공통 장벽을 나타내는 단답형 선택 설문조사를 사용합니다. 각 선택 항목은 사용자의 선택을 반영하는 해당 값을 사용하여 사용자 지정 속성 `upgrade_reason` 에 매핑됩니다.

| 선택              | 속성        | 값       |
|---------------------|------------------|-------------|
| 너무 비싸다       | `upgrade_reason` | `expensive` |
| 가치 없음        | `upgrade_reason` | `value`     |
| 사용하기 어려움    | `upgrade_reason` | `difficult` |
| 경쟁사 사용  | `upgrade_reason` | `competitor`|
| 기타 이유        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

사용자가 설문조사를 제출하면 선택한 값이 프로필에 저장됩니다. 그런 다음 할인 혜택이나 사용성 개선과 같은 특정 목적에 맞는 캠페인으로 이러한 사용자를 타겟팅할 수 있습니다.

### 즐겨 찾는 기능

**목표:** 고객이 즐겨 사용하는 기능을 파악하세요.

이를 설정하려면 각 옵션이 앱의 기능을 나타내는 객관식 선택 설문조사를 사용합니다. 각 선택 항목은 사용자 지정 속성 `favorite_features` 에 매핑되며, 사용자가 설문조사를 제출하면 해당 속성은 선택한 값의 배열로 설정됩니다.

| 선택            | 속성          | 값        |
|-------------------|--------------------|--------------|
| 북마크         | `favorite_features`| `bookmarks`  |
| 모바일 앱        | `favorite_features`| `mobile`     |
| 게시물 공유     | `favorite_features`| `sharing`    |
| 고객 지원  | `favorite_features`| `support`    |
| 사용자 정의     | `favorite_features`| `custom`     |
| 가격 / 가치     | `favorite_features`| `value`      |
| 커뮤니티         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

이 설문조사는 객관식 선택을 사용하므로 선택한 모든 기능 값의 목록으로 사용자의 프로필이 업데이트됩니다.




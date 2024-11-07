---
nav_title: 사용자 지정 이벤트
article_title: 사용자 지정 이벤트
page_order: 9
page_type: reference
description: "이 참조 문서에서는 사용자 지정 이벤트 및 속성, 세분화, 사용 방법, 캔버스 항목 속성, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다."
search_rank: 2
---

# [![브레이즈 학습 과정]](https://learning.braze.com/custom-events-and-attributes) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}맞춤 이벤트

> 이 문서에서는 사용자 지정 이벤트 및 속성, 세분화, 사용 방법, 캔버스 항목 속성, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다. Braze의 이벤트에 대해 자세히 알아보려면 [이벤트를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events) 참조하세요.

## 개요

사용자 지정 이벤트는 사용자가 수행한 작업 또는 사용자에 대한 업데이트입니다. 애플리케이션 내에서 가치가 높은 사용자 상호작용을 추적하는 데 가장 적합합니다. 사용자 지정 이벤트를 기록하면 원하는 수와 유형의 후속 캠페인이 트리거될 수 있으며, 해당 이벤트의 최근성과 빈도에 따라 나열된 세분화 필터를 사용할 수 있습니다.

### 사용 사례

몇 가지 일반적인 사용자 지정 이벤트 사용 사례는 다음과 같습니다:
- [액션 기반 전달을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) 사용하여 사용자 지정 이벤트를 기반으로 캠페인 또는 캔버스를 트리거합니다.
- 사용자 지정 이벤트를 수행한 횟수, 마지막으로 이벤트가 발생한 시간 등을 기준으로 사용자를 세분화합니다.
- 대시보드 [사용자 지정 이벤트 분석을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics) 사용하여 각 이벤트의 발생 빈도에 대한 집계 보기
- [퍼널]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) 및 [리텐션]({{site.baseurl}}/user_guide/data_and_analytics/reporting/retention_reports/) 보고서를 사용하여 추가 분석을 찾아보세요.
- [영구 항목 속성을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/) 활용하여 고객 이벤트의 메타데이터를 사용하여 캔버스 단계에서 개인화할 수 있습니다.
- [Currents로]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents) 더욱 정교한 분석을 생성하세요.
- 캔버스 [예외 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events#canvas-exception-events) 설정하여 사용자가 캔버스의 다음 단계로 진행하지 않아야 하는 시점을 정의하세요.

### 사용자 지정 이벤트 관리

대시보드에서 사용자 지정 이벤트를 만들고 관리하려면 **데이터 설정** > **사용자 지정 이벤**트로 이동합니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 **설정 관리에서** **사용자 지정 이벤트를** 찾을 수 있습니다.
{% endalert %}

이 페이지에서 기존 사용자 지정 이벤트를 확인, 관리, 생성 또는 차단할 수 있습니다. 사용자 지정 이벤트 옆의 메뉴를 선택하여 다음 작업을 수행합니다:

#### 차단 목록에 추가 중

사용자 지정 이벤트는 작업 메뉴를 통해 개별적으로 차단하거나 최대 10개의 이벤트를 선택하여 일괄적으로 차단할 수 있습니다. 사용자 지정 이벤트를 차단하면 해당 이벤트와 관련된 데이터가 수집되지 않으며, 다시 활성화하지 않는 한 기존 데이터를 사용할 수 없고, 차단된 이벤트는 필터나 그래프에 표시되지 않습니다. 또한 이벤트가 현재 Braze 대시보드의 다른 영역에 있는 필터나 트리거에 의해 참조되고 있는 경우, 해당 이벤트를 참조하는 필터나 트리거의 모든 인스턴스가 제거되고 보관된다는 경고 모달이 표시됩니다.

#### 설명 추가하기

`Manage Events, Attributes, Purchases` [사용자 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) 있는 경우 사용자 지정 이벤트가 생성된 후 설명을 추가할 수 있습니다. 사용자 지정 이벤트에 대한 **설명 수정을** 선택하고 팀에 대한 메모 등 원하는 내용을 입력합니다.

### 태그 추가하기

`Manage Events, Attributes, Purchases` [사용자 권한이]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) 있는 경우 사용자 지정 이벤트가 생성된 후 태그를 추가할 수 있습니다. 그런 다음 태그를 사용하여 이벤트 목록을 필터링할 수 있습니다. (이 기능은 현재 얼리 액세스 중입니다. 이 얼리 액세스에 참여하려면 고객 성공 관리자에게 문의하세요).

#### 사용량 보고서 보기

사용량 보고서에는 특정 사용자 지정 이벤트를 사용하는 모든 캔버스, 캠페인 및 세그먼트가 나열됩니다. 이 목록에 Liquid 사용은 포함되지 않습니다. 

각 사용자 지정 이벤트 옆의 확인란을 선택한 다음 **사용량 보고서 보기를** 선택하면 한 번에 최대 10개의 사용량 보고서를 볼 수 있습니다.

### 데이터 내보내기 ###

사용자 지정 이벤트 목록을 CSV 파일로 내보내려면 페이지 상단의 '모두 내보내기' 버튼을 클릭합니다. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다. (이 기능은 현재 얼리 액세스 버전에서 사용할 수 있습니다. 이 얼리 액세스에 참여하려면 고객 성공 관리자에게 문의하세요).

### 사용자 지정 이벤트 로깅

사용자 지정 이벤트에는 추가 설정이 필요합니다. 다음은 사용자 지정 이벤트를 기록하는 데 사용되는 다양한 플랫폼의 메서드 목록입니다. 이 페이지에서는 사용자 지정 이벤트에 속성 및 수량을 추가하는 방법에 대한 문서도 찾을 수 있습니다.

{% details 플랫폼별 문서 확장 %}

- [Android 및 FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
- [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_custom_events/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/)

{% enddetails %}

### 사용자 지정 이벤트 스토리지

사용자 지정 이벤트 메타데이터(첫 번째/마지막 발생, 총 횟수, 30일간 Y의 X)를 포함하여 **사용자 프로필에** 저장된 모든 데이터는 각 프로필이 [활성화되어]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) 있는 한 무기한 유지됩니다.

## 세분화 필터

다음 표는 사용자 지정 이벤트별로 사용자를 세분화하는 데 사용할 수 있는 필터를 보여줍니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 사용자 지정 이벤트가 **X회 이상** 발생했는지 확인합니다. | **그 이상** | **번호** |
| 사용자 지정 이벤트가 **X 횟수 미만으로** 발생했는지 확인합니다. | **미만** | **번호** |
| 사용자 지정 이벤트가 **정확히 X회** 발생했는지 확인합니다. | **정확히** | **번호** |
| 사용자 지정 이벤트가 **X 날짜 이후에** 마지막으로 발생했는지 확인합니다. | **이후** | **시간** |
| 사용자 지정 이벤트가 **X 날짜 이전에** 마지막으로 발생했는지 확인합니다. | **전에** | **시간** |
| 사용자 지정 이벤트가 마지막으로 발생한 지 **X일이 넘었는지** 확인합니다. | **그 이상** | **일수** (양수) |
| 사용자 지정 이벤트가 마지막으로 발생한 **날짜가 X일 미만인지** 확인합니다. | **미만** | **일수** (양수) |
| 사용자 지정 이벤트가 **X(최대 = 50) 횟수 이상** 발생했는지 확인합니다 **.** | **그 이상** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 사용자 지정 이벤트가 **X(최대 = 50) 횟수 미만으로** 발생했는지 확인합니다 **.** | **미만** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 사용자 지정 이벤트가 **정확히 X(최대 = 50) 횟수만큼** 발생했는지 확인합니다. | **정확히** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 분석

Braze는 세분화를 위해 이러한 이벤트가 발생한 횟수와 각 사용자가 마지막으로 수행한 시간을 기록합니다. 이러한 분석은 **분석** > **사용자 지정 이벤트 보고서에서** 볼 수 있습니다.

{% alert note %}
[이전 탐색을]({{site.baseurl}}/navigation) 사용하는 경우 **데이터에서** **사용자 지정 이벤트** 보고서를 찾을 수 있습니다.
{% endalert %}

대시보드의 **사용자 지정 이벤트 보고서** 페이지에서 각 사용자 지정 이벤트의 발생 빈도와 시간 경과에 따른 세그먼트별로 집계하여 더 자세한 분석을 볼 수 있습니다. 이는 특히 캠페인이 마지막으로 전송된 시간을 나타내는 시계열에 겹쳐진 회색 선을 확인하여 캠페인이 사용자 지정 이벤트 활동에 어떤 영향을 미쳤는지 확인하는 데 유용합니다.

![대시보드의 사용자 지정 이벤트 페이지에 있는 사용자 지정 이벤트 수 그래프는 사용자 지정 이벤트의 추세를 보여줍니다.][8]

**필터를** 사용하여 시간, 월평균 사용자 수(MAU), 세그먼트 또는 KPI 공식에 따라 사용자 지정 이벤트를 세분화할 수도 있습니다. 

![사용자 지정 이벤트 그래프 필터][9]{: style="max-width:40%;"}

{% alert tip %}
사용자 지정 [속성을 증가시키면]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers) 사용자 지정 이벤트와 유사한 사용자 행동에 대한 카운터를 유지할 수 있습니다. 그러나 사용자 지정 속성 데이터는 시계열로 볼 수 없습니다. 시계열로 분석할 필요가 없는 사용자 행동은 이 방법을 사용하여 기록해야 합니다.
{% endalert %}

### 사용자 지정 이벤트 분석이 표시되지 않나요?

사용자 지정 이벤트 데이터로 생성된 세그먼트는 생성되기 전의 이전 기록 데이터를 표시할 수 없습니다.

## 사용자 지정 이벤트 속성

사용자 지정 이벤트 속성은 이벤트의 특정 발생을 설명하는 사용자 지정 이벤트 메타데이터 또는 속성입니다. 그런 다음 이러한 속성을 사용하여 트리거 조건을 추가로 지정하고, 메시징에서 개인화를 강화하고, 전환을 추적하고, 로데이터 내보내기를 통해 보다 정교한 분석을 생성할 수 있습니다.

사용자 지정 이벤트 속성은 Braze 프로필에 저장되지 않으므로 데이터 포인트를 소비하지 않습니다(예외 사항은 아래 [데이터 포인트](#data-points) 참조).

{% alert important %}
각 사용자 지정 이벤트 또는 구매에는 최대 256개의 고유한 사용자 지정 이벤트 속성이 있을 수 있습니다. 사용자 지정 이벤트 또는 구매가 256개 이상의 속성과 함께 기록되는 경우 처음 256개만 캡처되어 사용할 수 있습니다.
{% endalert %}

### 예상 형식

속성 값은 키가 속성 이름이고 값이 속성 값인 객체여야 합니다. 속성 이름은 선행 달러 기호(`$`)가 없는 255자 이하의 비어 있지 않은 문자열이어야 합니다.

속성 값은 다음 데이터 유형 중 하나를 사용할 수 있습니다:

| 데이터 유형 | 설명 |
| --- | --- |
| 숫자 | [정수](https://en.wikipedia.org/wiki/Integer) 또는 [부동 소수점](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| 부울 | |
| 데이터 시간 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열로 포맷됩니다. 배열 내에서는 지원되지 않습니다. |
| 문자열 | 255자 이하. |
| 배열 | 배열에는 날짜/시간을 포함할 수 없습니다. |
| 개체 | 오브젝트는 문자열로 수집됩니다. |
| 중첩된 개체 | 다른 객체 안에 있는 객체. 자세한 내용은 이 문서의 [중첩된 객체에](#nested-objects) 대한 섹션을 참조하세요.
{: .reset-td-br-1 .reset-td-br-2}

배열 또는 개체 값을 포함하는 이벤트 속성 개체는 최대 50KB의 이벤트 속성 페이로드를 가질 수 있습니다.

사용자 지정 이벤트 속성의 데이터 유형을 변경할 수 있지만, 데이터가 수집된 후에 [데이터 유형을 변경하면]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) 어떤 영향이 있는지 주의하세요.

### 사용자 지정 이벤트 속성 사용

사용자 지정 이벤트 속성을 사용하여 캠페인 트리거의 자격을 부여하고, 전환을 추적하고, 메시지를 개인화할 수 있습니다.

#### 트리거 메시지

사용자 지정 이벤트 속성을 사용하여 특정 캠페인 또는 캔버스에 대한 대상 범위를 더 좁힐 수 있습니다. 예를 들어, 전자상거래 애플리케이션이 있고 사용자가 장바구니를 이탈할 때 메시지를 보내려는 경우, 사용자 지정 이벤트 속성 `cart value` 을 추가하여 타겟 고객을 개선하고 캠페인 개인화를 강화할 수 있습니다.

![버려진 카드에 대한 사용자 지정 이벤트 속성 필터. 두 개의 필터를 AND 연산자와 결합하여 장바구니 금액이 100~200달러인 카드를 포기한 사용자에게 이 캠페인을 보냅니다.][16]

중첩된 사용자 지정 이벤트 속성은 \[액션 기반 전달][19] 에서도 지원됩니다.

![버려진 카드에 대한 사용자 지정 이벤트 속성 필터. 카트에 있는 품목의 가격이 100달러 이상인 경우 하나의 필터가 선택됩니다.][20]

#### 메시지 개인화

메시징 템플릿 내에서 사용자 지정 이벤트 속성을 사용하여 개인화할 수도 있습니다. 트리거 이벤트가 있는 \[액션 기반 전달][19] ]을 사용하는 모든 캠페인은 해당 이벤트의 사용자 지정 이벤트 속성을 사용하여 메시징 개인화를 수행할 수 있습니다.

예를 들어 게임 애플리케이션이 있고 레벨을 완료한 사용자에게 메시지를 보내려는 경우, 사용자가 해당 레벨을 완료하는 데 걸린 시간 속성을 사용하여 메시지를 더욱 맞춤화할 수 있습니다. 이 예제에서는 \[조건부 로직][18] 을 사용하여 세 가지 세그먼트에 대해 메시지를 개인화합니다. `time_spent` 라는 사용자 지정 이벤트 속성은 ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` 을 호출하여 메시지에 포함할 수 있습니다.

{% alert warning %}
사용자가 인터넷에 연결되어 있지 않으면 템플릿화된 사용자 지정 이벤트 속성을 사용하여 트리거된 인앱 메시지(예: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %})가 실패하고 표시되지 않습니다.
{% endalert %}

인앱 메시지가 템플릿화된 인앱 메시지로 전달되도록 하는 Liquid 태그의 전체 목록은 [자주 묻는 질문을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/) 참조하세요.

##### 필터 사용 시 고려 사항

- **API 호출:** API 호출을 하고 "is blank" 필터를 사용할 때 사용자 지정 이벤트 속성이 호출에서 제외되면 "비어 있는" 것으로 간주됩니다. 예를 들어 `"event_property": ""` 을 포함하면 사용자는 "비어 있지 않음"으로 간주됩니다.
- **정수:** 숫자 사용자 지정 이벤트 속성을 필터링할 때 그 숫자가 매우 큰 경우에는 '정확히' 필터를 사용하지 마세요. 숫자가 너무 크면 특정 길이에서 반올림될 수 있으므로 필터가 예상대로 작동하지 않을 수 있습니다.

#### 세분화

이벤트 속성 세분화를 사용하면 발생한 사용자 지정 이벤트 및 해당 이벤트와 관련된 속성을 기반으로 사용자를 타겟팅할 수 있습니다. 이 기능은 구매 및 사용자 지정 이벤트를 세분화할 때 더 많은 필터링 옵션을 추가합니다.

사용자 지정 이벤트의 이벤트 속성은 해당 이벤트를 사용하는 모든 세그먼트에 대해 실시간으로 업데이트됩니다. **데이터 설정** > **사용자 지정** 이벤트 페이지에서 사용자 지정 이벤트의 **속성 관리를** 클릭하여 속성을 관리할 수 있습니다. 특정 세그먼트 필터에 사용되는 사용자 지정 이벤트 속성에는 최대 30일의 룩백 기록이 있습니다.

{% alert note %}
이벤트 속성 최근성 및 빈도를 기준으로 세그먼트를 만들려면 고객 성공 관리자에게 문의하여 특정 사용자 지정 이벤트 속성에 대한 세그먼테이션을 사용 설정하세요. 활성화하면 세분화할 때 추가 필터링 옵션에 액세스할 수 있습니다.
{% endalert %}

이러한 세분화 필터에는 다음이 포함됩니다:

- 지난 Y일 동안 값 B가 있는 속성 A로 사용자 지정 이벤트를 X회 수행했습니다.
- 지난 Y일 동안 B값의 부동산 A를 X회 구매한 적이 있습니다.
- 1일, 3일, 7일, 14일, 21일, 30일 이내로 세분화하는 기능을 추가합니다.

![][3]

데이터는 고객 성공 관리자가 해당 이벤트 속성을 사용 설정한 후에만 기록되며, 이벤트 속성은 해당 날짜 이후부터만 사용할 수 있습니다.

##### 데이터 포인트

구독 사용량과 관련하여 다음 필터를 사용하여 세분화를 위해 활성화된 사용자 지정 이벤트 속성은 모두 사용자 지정 이벤트 자체에서 계산되는 데이터 포인트에 추가하여 별도의 데이터 포인트로 계산됩니다:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### 캔버스 항목 속성 및 이벤트 속성

Canvas 사용자 여정에서 `canvas_entry_properties` 및 `event_properties` 을 활용할 수 있습니다. 자세한 정보와 예시는 [캔버스 항목 속성 및 이벤트 속성을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) 확인하세요.

{% tabs local %}
{% tab 캔버스 항목 속성 %}

[캔버스 항목 속성은]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) 액션 기반 또는 API로 트리거되는 캔버스에 매핑하는 속성입니다. `canvas_entry_properties` 객체의 최대 크기 제한은 50KB입니다.

{% alert note %}
특히 인앱 메시지 채널의 경우, 이전 얼리 액세스의 일부로 원래 편집기에서 영구 항목 속성을 활성화한 경우에만 캔버스 흐름 및 원래 캔버스 편집기에서 `canvas_entry_properties` 을 참조할 수 있습니다.
{% endalert %}

캔버스 플로우 메시징의 경우, `canvas_entry_properties` 는 Liquid의 모든 메시지 단계에서 사용할 수 있습니다. 다음 속성을 참조할 때 이 리퀴드를 사용하십시오: ``{% raw %} canvas_entry_properties.${property_name} {% endraw %}``. 이 방법을 사용하려면 이벤트가 사용자 지정 이벤트 또는 구매 이벤트여야 합니다. 

#### 사용 사례

{% raw %}
소매점인 RetailApp에 대한 다음 요청을 고려해 보세요: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Liquid `{{canvas_entry_properties.${product_name}}}` 를 사용하여 메시지에 "신발"이라는 단어를 추가할 수 있습니다.
{% endraw %}

또한 리테일앱은 구매 이벤트를 트리거한 사용자를 대상으로 하는 캔버스의 다양한 `product_name` 속성에 대해 특정 메시지를 전송하도록 트리거할 수 있습니다. 예를 들어, 신발을 구매한 사용자와 다른 제품을 구매한 사용자에게 각각 다른 메시지를 보낼 수 있도록 다음 Liquid를 메시지 단계에 추가할 수 있습니다.

{% raw %}
```markdown
{% if  {{canvas_entry_properties.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add any additional items to your cart and enjoy storewide discounts. 
{% endif %}

```
{% endraw %}

{% details 원본 캔버스 편집기를 위한 확장 %}

2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 섹션은 참고용으로만 제공됩니다.

원본 편집기로 제작한 캔버스의 경우 `canvas_entry_properties` 은 캔버스의 첫 번째 전체 단계에서만 참조할 수 있습니다.

{% enddetails %}
{% endtab %}

{% tab 이벤트 속성 %}

{% alert important %}
리드 메시지 단계에서는 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties` 을 사용하거나 `event_properties` 을 포함하는 메시지 단계 **앞에** 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다.
{% endalert %}

이벤트 속성은 사용자 지정 이벤트 및 구매에 대해 설정한 속성을 나타냅니다. 이러한 `event_properties` 은 액션 기반 전달 및 캔버스가 있는 캠페인에서 사용할 수 있습니다.

캔버스 플로우에서 사용자 지정 이벤트 및 구매 이벤트 속성은 액션 경로 단계 뒤에 오는 모든 메시지 단계에서 Liquid에서 사용할 수 있습니다. `event_properties` 을 참조하는 경우 {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} 을 사용해야 합니다. 이러한 이벤트는 메시지 구성 요소에서 이러한 방식으로 사용하려면 사용자 지정 이벤트 또는 구매 이벤트여야 합니다.

작업 경로 다음의 첫 번째 메시지 단계에서 해당 작업 경로에 참조된 이벤트와 관련된 `event_properties` 을 사용할 수 있습니다. 이러한 `event_properties` 은 사용자가 실제로 작업을 수행한 경우에만 사용할 수 있습니다(다른 모든 사용자 그룹으로 이동하지 않음). 이 작업 경로와 메시지 단계 사이에 다른 단계(다른 작업 경로나 메시지 단계가 아닌)를 배치할 수 있습니다.

{% details 원본 캔버스 편집기를 위한 확장 %}

2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 섹션은 참고용으로만 제공됩니다.

원래 캔버스 편집기의 경우 `event_properties` 을 예약된 전체 단계에서 사용할 수 없습니다. 그러나 전체 단계가 예약되어 있더라도 액션 기반 캔버스의 첫 번째 전체 단계에서는 `event_properties` 을 사용할 수 있습니다.

{% enddetails %}

{% endtab %}
{% endtabs %}

### 중첩된 개체 {#nested-objects}

중첩된 개체(다른 개체 안에 있는 개체)를 사용하여 중첩된 JSON 데이터를 사용자 지정 이벤트 및 구매의 속성으로 전송할 수 있습니다. 이 중첩된 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하고, 세분화하는 데 사용할 수 있습니다.

자세히 알아보려면 [중첩된 객체에]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/nested_objects/) 대한 전용 문서를 참조하세요.

## 사용자 지정 이벤트 속성 저장소

사용자 지정 이벤트 속성은 타겟팅 정확도를 높이고 메시지를 더욱 개인화된 느낌으로 만들 수 있도록 설계되었습니다. 사용자 지정 이벤트 속성은 단기 및 장기적으로 Braze에 저장할 수 있습니다.

이벤트 속성 값을 세분화하려는 경우 두 가지 옵션이 있습니다:

1. **30일 이내:** 브레이즈 지원 담당자는 브레이즈 세그먼트 내에서 특정 이벤트 속성 값의 빈도 및 최신성을 기반으로 이벤트 속성 세분화를 활성화할 수 있습니다. 세그먼트 내에서 이벤트 속성을 활용하려면 Braze 계정 담당자 또는 고객 성공 관리자에게 문의하세요. 이 옵션은 데이터 사용량에 영향을 미칩니다.<br><br>
2. **30일 이내 및 그 이후:** 단기 및 장기 이벤트 속성 세분화를 모두 포함하려면 [세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) 사용할 수 있습니다. 이 기능을 사용하면 지난 2년 동안 추적된 사용자 지정 이벤트 및 이벤트 속성을 기반으로 세분화할 수 있습니다. 이 옵션은 데이터 사용량에 영향을 미치지 않습니다.

특정 요구 사항에 따라 가장 적합한 접근 방식에 대한 권장 사항은 Braze 고객 성공 관리자에게 문의하세요.


[1]: {% image_buster /assets/img/nested_object1.png %}
[2]: {% image_buster /assets/img/nested_object2.png %}
[3]: {% image_buster /assets/img/nested_object3.png %}
[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}
[8]: {% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png"
[9]: {% image_buster /assets/img/custom_events_report_filters.png %}
[16]: {% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"
[18]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
[19]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/
[20]: {% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"

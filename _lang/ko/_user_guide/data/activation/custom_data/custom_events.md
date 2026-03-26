---
nav_title: 커스텀 이벤트
article_title: Custom Events
page_order: 9
page_type: reference
description: "이 문서에서는 커스텀 이벤트 및 속성정보, 세분화, 사용 방법, 캔버스 진입 속성정보, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다."
search_rank: 2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}커스텀 이벤트

> 이 문서에서는 커스텀 이벤트 및 속성정보, 관련 세분화 필터, 캔버스 진입 속성정보, 관련 분석 등에 대해 설명합니다. Braze 이벤트에 대해 전반적으로 알아보려면 [이벤트]({{site.baseurl}}/user_guide/data/custom_data/events/)를 참조하세요.

커스텀 이벤트는 사용자가 수행한 작업 또는 사용자에 대한 업데이트입니다. 커스텀 이벤트가 기록되면 원하는 수와 유형의 후속 캠페인을 트리거할 수 있습니다. 그런 다음 [세분화 필터](#segmentation-filters)를 사용하여 해당 커스텀 이벤트가 발생한 최근성 및 빈도에 따라 사용자를 세분화할 수 있습니다. 따라서 커스텀 이벤트는 애플리케이션 내에서 가치가 높은 사용자 상호 작용을 추적하는 데 가장 적합합니다.

## 활용 사례

몇 가지 일반적인 커스텀 이벤트 활용 사례는 다음과 같습니다:

- [실행 기반 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)을 사용하여 커스텀 이벤트를 기반으로 캠페인 또는 캔버스 트리거하기
- 커스텀 이벤트를 수행한 횟수, 마지막으로 이벤트가 발생한 시간 등을 기준으로 사용자를 세분화하기
- 대시보드 [커스텀 이벤트 분석]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#custom-event-analytics)을 사용하여 각 이벤트의 발생 빈도에 대한 집계 보기
- [퍼널]({{site.baseurl}}/user_guide/data_and_analytics/reporting/funnel_reports/#step-2-select-events-for-funnel-steps) 및 [리텐션]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) 보고서를 사용하여 추가 분석 찾기
- [영구 진입 속성정보]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)를 활용하여 고객 이벤트의 메타데이터를 캔버스 단계의 개인화에 활용하기
- [커런츠]({{site.baseurl}}/user_guide/data/braze_currents/)로 더욱 정교한 분석 생성하기
- [종료 기준]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)을 설정하여 사용자가 캔버스를 종료해야 하는 시점을 정의하기

## 커스텀 이벤트 관리

대시보드에서 **데이터 설정** > **커스텀 이벤트**로 이동하여 커스텀 이벤트를 관리, 생성 또는 차단 목록에 추가할 수 있습니다.

커스텀 이벤트 옆의 메뉴를 선택하여 다음 작업을 수행합니다:

### 차단 목록에 추가

작업 메뉴를 통해 개별 커스텀 이벤트를 차단하거나, 최대 100개의 이벤트를 선택하여 일괄 차단할 수 있습니다.

커스텀 이벤트를 차단하면:

- 향후 해당 이벤트에 대한 데이터는 수집되지 않습니다.
- 해당 이벤트가 차단 해제되지 않으면 기존 데이터를 사용할 수 없습니다.
- 해당 이벤트는 필터나 그래프에 표시되지 않습니다.

또한 차단된 커스텀 이벤트가 현재 Braze의 다른 영역에 있는 필터나 트리거에서 참조되고 있는 경우, 해당 이벤트를 참조하는 필터나 트리거의 모든 인스턴스가 제거되고 아카이브된다는 경고 모달이 표시됩니다.

### 설명 추가하기

`Manage Events, Attributes, Purchases` [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 이벤트가 생성된 후 설명을 추가할 수 있습니다. 커스텀 이벤트에 대한 **설명 편집**을 선택하고 팀에 대한 메모 등 원하는 내용을 입력합니다.

## 태그 추가하기

"Manage Events, Attributes, Purchases" [사용자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있는 경우 커스텀 이벤트가 생성된 후 태그를 추가할 수 있습니다. 그런 다음 태그를 사용하여 이벤트 목록을 필터링할 수 있습니다.

### 사용량 보고서 보기

사용량 보고서에는 특정 커스텀 이벤트를 사용하는 모든 캔버스, 캠페인 및 세그먼트가 나열됩니다. 이 목록에는 Liquid 사용은 포함되지 않습니다.

여러 커스텀 이벤트의 체크박스를 선택한 다음 **사용량 보고서 보기**를 선택하면 한 번에 최대 100개의 사용량 보고서를 볼 수 있습니다.

## 데이터 내보내기

커스텀 이벤트 목록을 CSV 파일로 내보내려면 페이지 상단의 **모두 내보내기** 버튼을 선택합니다. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

## 커스텀 이벤트 로깅

커스텀 이벤트에는 추가 설정이 필요합니다. 아래 목록에서 각 플랫폼에 대한 설명서를 참조하면 커스텀 이벤트를 기록하는 데 사용되는 방법과 커스텀 이벤트에 속성정보 및 수량을 추가하는 방법에 대한 정보를 찾을 수 있습니다.

{% details 플랫폼별 설명서 펼치기 %}

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=unity)
- [.NET MAUI (구 Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=roku)

{% enddetails %}

## 커스텀 이벤트 저장

커스텀 이벤트 메타데이터(첫 번째 또는 마지막 발생, 총 횟수, 30일간 Y 중 X)를 포함하여 **고객 프로필**에 저장된 모든 데이터는 각 프로필이 [활성]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) 상태인 한 무기한 유지됩니다.

## 세분화 필터

다음 표는 커스텀 이벤트별로 사용자를 세분화하는 데 사용할 수 있는 필터를 보여줍니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 커스텀 이벤트가 **X회 이상** 발생했는지 확인 | **초과** | **숫자** |
| 커스텀 이벤트가 **X회 미만으로** 발생했는지 확인 | **미만** | **숫자** |
| 커스텀 이벤트가 **정확히 X회** 발생했는지 확인 | **정확히** | **숫자** |
| 커스텀 이벤트가 **X 날짜 이후에** 마지막으로 발생했는지 확인 | **이후** | **시간** |
| 커스텀 이벤트가 **X 날짜 이전에** 마지막으로 발생했는지 확인 | **이전** | **시간** |
| 커스텀 이벤트가 마지막으로 발생한 지 **X일이 넘었는지** 확인 | **초과** | **일수** (양수) |
| 커스텀 이벤트가 마지막으로 발생한 지 **X일 미만인지** 확인 | **미만** | **일수** (양수) |
| 커스텀 이벤트가 **X회(최대 = 50) 넘게** 발생했는지 확인 | **초과** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 커스텀 이벤트가 **X회(최대 = 50) 미만으로** 발생했는지 확인 | **미만** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
| 커스텀 이벤트가 **정확히 X회(최대 = 50)만큼** 발생했는지 확인 | **정확히** | 지난 **Y일 동안(Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 분석

Braze는 커스텀 이벤트가 발생한 횟수와 세분화를 위해 각 사용자가 마지막으로 수행한 시간을 기록합니다. **분석** > **커스텀 이벤트 보고서**로 이동하여 이러한 분석을 볼 수 있습니다.

대시보드의 **커스텀 이벤트 보고서** 페이지에서 각 커스텀 이벤트가 얼마나 자주 발생하는지 집계하여 볼 수 있습니다. 시계열에 겹쳐진 회색 선은 마지막으로 캠페인이 전송된 시간을 나타내며, 이는 캠페인이 커스텀 이벤트 활동에 미친 영향을 확인하는 데 유용합니다.

![대시보드의 커스텀 이벤트 페이지에 있는 커스텀 이벤트 수 그래프는 커스텀 이벤트의 추세를 보여줍니다]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

**필터**를 사용하여 시간, 월평균 사용자 수(MAU), 세그먼트 또는 KPI 공식에 따라 커스텀 이벤트를 세분화할 수도 있습니다.

![커스텀 이벤트 그래프 필터]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[커스텀 속성을 증가]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#integers)시켜 커스텀 이벤트와 유사한 사용자 행동에 대한 카운터를 유지할 수 있습니다. 그러나 커스텀 속성 데이터는 시계열로 볼 수 없습니다. 시계열로 분석할 필요가 없는 사용자 행동은 이 방법을 사용하여 기록해야 합니다.
{% endalert %}

### 커스텀 이벤트 분석이 표시되지 않는 이유

커스텀 이벤트 데이터로 생성된 세그먼트는 생성되기 전의 이전 기록 데이터를 표시할 수 없습니다.

## 커스텀 이벤트 속성정보

커스텀 이벤트 속성정보는 이벤트의 특정 발생을 설명하는 커스텀 이벤트 메타데이터 또는 속성입니다. 이러한 속성정보는 트리거 조건을 더욱 구체화하고, 메시징의 개인화 수준을 높이고, 전환을 추적하고, 원시 데이터 내보내기를 통해 더욱 정교한 분석을 생성하는 데 사용할 수 있습니다.

커스텀 이벤트 속성정보는 Braze 프로필에 저장되지 않으므로 데이터 포인트를 기록하지 않습니다(예외는 [데이터 포인트](#data-points) 참조).

{% alert important %}
각 커스텀 이벤트 또는 구매에는 최대 256개의 고유한 커스텀 이벤트 속성정보가 있을 수 있습니다. 커스텀 이벤트 또는 구매가 256개 이상의 속성정보와 함께 기록되는 경우 처음 256개만 캡처되어 사용할 수 있습니다.
{% endalert %}

### 예상 형식

속성정보 값은 키가 속성정보 이름이고 값이 속성정보 값인 오브젝트여야 합니다. 속성정보 이름은 비어 있지 않은 255자 이하의 문자열이어야 하며 선행 달러 기호(`$`)가 없어야 합니다.

속성정보 값은 다음 데이터 유형 중 하나를 사용할 수 있습니다:

| 데이터 유형 | 설명 |
| --- | --- |
| 숫자 | [정수](https://en.wikipedia.org/wiki/Integer) 또는 [플로트](https://en.wikipedia.org/wiki/Floating-point_arithmetic) |
| 부울 | `true` 또는 `false` 값입니다. |
| 날짜/시간 | [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식의 문자열로 포맷됩니다. 배열 내에서는 지원되지 않습니다. |
| 문자열 | 255자 이하. |
| 배열 | 배열에는 날짜/시간을 포함할 수 없습니다. |
| 중첩된 오브젝트 | 다른 오브젝트 안에 있는 오브젝트입니다. 자세한 내용은 이 문서의 [중첩된 오브젝트](#nested-objects) 섹션을 참조하세요.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

배열 또는 오브젝트 값을 포함하는 이벤트 속성정보 오브젝트는 최대 100&nbsp;KB의 이벤트 속성정보 페이로드를 가질 수 있습니다.

속성정보 값 데이터 유형은 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/) 값과 유사하게 감지 및 처리되지만, 두 가지 주요 차이점이 있습니다:

- **문자열-시간 변환:** 인식된 시간 형식과 일치하는 문자열 값은 자동으로 날짜/시간 유형으로 변환됩니다. 이는 일부 문자열 값이 이벤트 속성정보에 있는 그대로 저장될 수 없음을 의미합니다.
- **유형 강제 변환 없음:** 이벤트 속성정보에는 자동 유형 강제 변환이 없습니다. 트리거 필터가 숫자 값 `5`를 기대하는 경우, 문자열 값 `"5"`는 일치하지 않습니다. Liquid 템플릿 및 커런츠 이벤트 데이터에도 동일하게 적용됩니다.

이러한 동작은 [구매 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#purchase-properties)에도 적용됩니다.

커스텀 이벤트 속성정보의 데이터 유형을 변경할 수 있지만, 데이터가 수집된 후에 [데이터 유형을 변경]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/)하면 어떤 영향이 있는지 주의하세요.

#### 예약 키

예약된 키를 이벤트 속성정보 이름으로 사용할 수 없습니다. `properties` 오브젝트에서 예약된 키를 사용하면 "유효하지 않은 'properties' 필드"라는 오류가 반환됩니다.

| 등록정보 | 예약 키 |
| --- | --- |
| 커스텀 이벤트 | `time` 및 `event_name` | 
| 구매 이벤트 |`time`, `product_id`, `quantity`, `event_name`, `price`, `currency` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 커스텀 이벤트 속성정보 사용

커스텀 이벤트 속성정보를 사용하여 캠페인 트리거의 자격을 부여하고, 전환을 추적하고, 메시징을 개인화할 수 있습니다.

#### 메시지 트리거

커스텀 이벤트 속성정보를 사용하여 특정 캠페인 또는 캔버스의 오디언스 범위를 더욱 좁힐 수 있습니다. 예를 들어 이커머스 애플리케이션이 있고 사용자가 장바구니를 유기했을 때 메시지를 보내려는 경우, `item price`의 커스텀 이벤트 속성정보를 추가하여 타겟 오디언스를 개선하고 캠페인 개인화를 높일 수 있습니다.

![유기한 장바구니에 대한 커스텀 이벤트 속성정보 필터. 두 개의 필터가 AND 연산자로 결합되어 100달러에서 200달러 사이의 아이템 가격으로 장바구니를 유기한 사용자에게 이 캠페인을 전송합니다]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

중첩된 커스텀 이벤트 속성정보도 [실행 기반 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)에서 지원됩니다.

![유기한 장바구니에 대한 커스텀 이벤트 속성정보 필터. 장바구니에 있는 품목의 가격이 100달러 이상인 경우 하나의 필터가 선택됩니다.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png")

#### 메시지 개인화

메시징 템플릿 내에서 커스텀 이벤트 속성정보를 사용하여 개인화할 수도 있습니다. 트리거 이벤트가 있는 [실행 기반 전달]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/)을 사용하는 모든 캠페인은 해당 이벤트의 커스텀 이벤트 속성정보를 메시징 개인화에 사용할 수 있습니다.

예를 들어 게임 앱이 있고 레벨을 완료한 사용자에게 메시지를 보내려는 경우, 사용자가 해당 레벨을 완료하는 데 걸린 시간 속성정보를 사용하여 메시지를 더욱 개인화할 수 있습니다. 이 예에서는 [조건 로직]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/)을 사용하여 세 가지 다른 세그먼트에 대해 메시지를 개인화합니다. `time_spent`라는 커스텀 이벤트 속성정보는 ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``를 호출하여 메시지에 포함할 수 있습니다.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
사용자가 인터넷에 연결되어 있지 않으면 템플릿화된 커스텀 이벤트 속성정보를 사용하여 트리거된 인앱 메시지(예: {% raw %}``{{event_properties.${time_spent}}}``{% endraw %})가 실패하고 표시되지 않습니다.
{% endalert %}

인앱 메시지가 템플릿화된 인앱 메시지로 전달되도록 하는 Liquid 태그의 전체 목록은 [자주 묻는 질문]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/faq/#what-are-templated-in-app-messages/)을 참조하세요.

##### 필터 사용 시 고려 사항

- **API 호출:** API 호출을 하고 "is blank" 필터를 사용할 때 커스텀 이벤트 속성정보가 호출에서 제외되면 "비어 있음"으로 간주됩니다. 예를 들어 `"event_property": ""`를 포함하면 사용자는 "비어 있지 않음"으로 간주됩니다.
- **정수:** 숫자 커스텀 이벤트 속성정보를 필터링할 때 그 숫자가 매우 큰 경우에는 "정확히" 필터를 사용하지 마세요. 숫자가 너무 크면 특정 길이에서 반올림될 수 있으므로 필터가 예상대로 작동하지 않을 수 있습니다.

#### 세분화

이벤트 속성정보 세분화를 사용하여 발생한 커스텀 이벤트 및 해당 이벤트와 관련된 속성정보를 기반으로 사용자를 타겟팅합니다. 이렇게 하면 구매 및 커스텀 이벤트별로 세분화할 때 필터링 옵션이 늘어납니다.

커스텀 이벤트의 이벤트 속성정보는 해당 이벤트를 사용하는 모든 세그먼트에 대해 실시간으로 업데이트됩니다. **데이터 설정** > **커스텀 이벤트**로 이동하여 관련 커스텀 이벤트에 대해 **속성정보 관리**를 선택하여 속성정보를 관리할 수 있습니다. 특정 세그먼트 필터에 사용되는 커스텀 이벤트 속성정보에는 최대 30일의 과거 조회 기록이 있습니다.

##### 세분화를 위한 이벤트 속성정보 추가

이벤트 속성정보의 최근성과 빈도를 기반으로 세그먼트를 생성하려면 "커스텀 이벤트 속성정보 세분화 편집" [사용자 권한]({{site.baseurl}}/user_guide/data/data_points/#viewing-data-point-usage)이 필요합니다.

{% multi_lang_include deprecations/user_permissions.md %}

기본적으로 워크스페이스당 20개의 세분화 가능한 이벤트 속성정보를 가질 수 있습니다. 이 한도를 늘리려면 Braze 계정 매니저에게 문의하세요.

세분화를 위한 이벤트 속성정보를 추가하려면 다음을 수행합니다:

1. 커스텀 이벤트로 이동하여 **속성정보 관리**를 선택합니다.
2. **세분화 활성화** 토글을 선택하여 세분화를 위한 이벤트 속성정보를 추가합니다. 세분화 시 추가 필터링 옵션에 접근할 수 있습니다.

이벤트 속성정보 세분화 필터에는 다음이 포함됩니다:

- 지난 Y일 동안 값 B가 있는 속성정보 A로 커스텀 이벤트를 X회 수행했습니다.
- 지난 Y일 동안 값 B의 속성정보 A로 구매를 X회 한 적이 있습니다.
- 1일에서 30일 이내에 세분화할 수 있는 기능이 추가되었습니다.

!['유기한 장바구니'와 속성정보 '아이템 수'가 2이고 지난 30일 캘린더 일 동안 1회 이상인 필터 그룹입니다.]({% image_buster /assets/img/nested_object3.png %})

데이터는 해당 이벤트 속성정보를 활성화한 후에만 기록되며, 이벤트 속성정보는 해당 날짜 이후에만 사용할 수 있습니다.

##### 데이터 포인트

구독 사용량과 관련하여 다음 필터를 사용하여 세분화를 위해 활성화된 커스텀 이벤트 속성정보는 모두 커스텀 이벤트 자체에서 계산되는 데이터 포인트에 추가하여 별도의 데이터 포인트로 계산됩니다:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### 캔버스 진입 속성정보 및 이벤트 속성정보

{% multi_lang_include canvas_entry_event_properties.md %}

### 중첩된 오브젝트 {#nested-objects}

중첩된 오브젝트(다른 오브젝트 안에 있는 오브젝트)를 사용하여 중첩된 JSON 데이터를 커스텀 이벤트 및 구매의 속성정보로 전송할 수 있습니다. 이 중첩된 데이터는 메시지에서 개인화된 정보를 템플릿화하고, 메시지 전송을 트리거하고, 사용자를 세분화하는 데 사용할 수 있습니다.

자세히 알아보려면 [중첩된 오브젝트]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/)에 대한 전용 페이지를 참조하세요.

## 커스텀 이벤트 속성정보 저장

커스텀 이벤트 속성정보는 타겟팅 정확도를 높이고 메시지를 더욱 개인화된 느낌으로 만들 수 있도록 설계되었습니다. 커스텀 이벤트 속성정보는 단기 및 장기적으로 Braze에 저장할 수 있습니다.

이벤트 속성정보 값을 기반으로 다음과 같은 방법으로 세분화할 수 있습니다:

- **30일 이내:** Braze 세그먼트 내에서 특정 이벤트 속성정보 값의 빈도와 최근성을 기반으로 이벤트 속성정보 세분화를 사용할 수 있습니다. 이 옵션은 데이터 사용에 영향을 미칩니다.<br><br>
- **30일 이내 및 그 이후:** 단기 및 장기 이벤트 속성정보 세분화를 모두 포함하려면 [세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)을 사용할 수 있습니다. 이 기능은 지난 2년 동안 추적된 커스텀 이벤트 및 이벤트 속성정보를 기반으로 사용자를 세분화합니다. 이 옵션은 데이터 사용에 영향을 미치지 않습니다.<br><br>
- **커스텀 속성 배열을 사용한 캔버스:** 커스텀 이벤트에 의해 트리거되는 캔버스를 구축하고 시작합니다. **사용자 업데이트** 단계를 구성하여 **항목 추가**를 사용해 이벤트 속성정보를 고객 프로필의 커스텀 속성 배열에 추가한 다음, 이벤트 속성정보 필터 대신 해당 커스텀 속성 배열의 필터를 사용하여 사용자를 세분화합니다. 이 옵션은 커스텀 속성 배열에 대한 각 업데이트가 데이터 포인트를 소비하므로 데이터 사용에 영향을 미칩니다. 구현 세부 사항은 [캔버스의 사용자 업데이트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) 및 [커스텀 속성 배열]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/#arrays)을 참조하세요.

특정 요구 사항에 따라 가장 적합한 접근 방식에 대한 권장 사항은 Braze 고객 성공 매니저에게 문의하세요.
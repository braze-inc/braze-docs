---
nav_title: 세그먼트 확장
article_title: 세그먼트 확장
page_order: 3.1
page_type: reference
description: "이 도움말 문서에서는 세그먼트 확장 기능을 설정하고 사용하여 세분화 기능을 향상시키는 방법을 안내합니다."
tool: Segments
---

# 세그먼트 확장

> Segment Extensions allow you to build very precise segments over an extended period of a user's history. For example, using Segment Extensions you can target users who have purchased a particular product in the last sixteen months or have spent a certain amount of money with your service. Refine this audience by using event properties to make targeting even more granular.

Braze segmentation allows you to target users based on custom event or purchase behavior. Segment Extensions enhances this capacity, letting you draw on historic data saved on the user profile. Using Segment Extensions, you can identify and reach users who have completed any custom event or purchase event any number of times in the past two years (730 days). 

## Why use Segment Extensions?

Braze segments give you powerful targeting tools to create dynamic groups of users. For most use cases, this is enough to reach your audience effectively. Segment Extensions are designed for advanced use cases where you need to analyze behaviors from up to two years ago or apply complex logic—without compromising data retention or system performance. You can use [SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments) queries or data from your own [data warehouse]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) to refine your audience further.

For example, Braze default segmentation will find users that fit specific criteria you define, such as identifying a user who recently purchased one of your products. Segment Extensions let you go deeper—like identifying users who bought a particular color of a specific product at least twice between 18 to 24 months ago. Segment Extensions are an enhancement, not a requirement. If you need more advanced filters or a longer lookback window, they're a great tool to help while keeping your data usage optimized.

{% alert note %}
특정 시점에 워크스페이스당 25개의 활성 세그먼트 확장이 기본적으로 할당되어 있습니다. 이 한도를 늘려야 하는 경우 Braze 고객 성공 관리자에게 문의하여 사용 사례에 대해 논의하세요.
{% endalert %}

## Creating a Segment Extension

To create a Segment Extension, you will create a filter to refine a segment of your users based on custom event properties. When creating a Segment Extension, you will choose whether the segment will be static or dynamically refreshed at a set interval.

### 1단계: 세그먼트 확장으로 이동

**대상** > **세그먼트 확장으로** 이동합니다.

From the Segment Extensions table, select  **Create New Extension**, then select your Segment Extension creation experience:

- **단순 확장:** 안내 양식을 사용하여 단일 이벤트에 초점을 맞춘 세그먼트 확장을 생성합니다.
SQL을 사용하고 싶지 않을 때 가장 적합합니다.
- **템플릿으로 시작하세요:** Snowflake 데이터를 사용하여 사용자 지정할 수 있는 템플릿으로 SQL 세그먼트를 생성합니다.
- **증분 새로 고침:** 최근 2일간의 데이터를 자동으로 새로 고치거나 필요에 따라 수동으로 새로 고치는 Snowflake SQL 세그먼트를 작성합니다. 정확성과 비용 효율성의 균형을 맞추는 데 가장 적합합니다.
- **전체 새로 고침:** 수동으로 새로 고칠 때 전체 오디언스를 다시 계산하는 Snowflake SQL 세그먼트를 작성합니다. 오디언스를 위한 완벽한 최신 보기가 필요한 경우에 가장 적합합니다.

![다양한 세그먼트 확장 생성 경험을 선택할 수 있는 표입니다.][20]{: style="max-width:50%"}

SQL을 사용하는 경험을 선택하는 경우 자세한 내용은 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을 참조하세요.

**단순 확장**을 선택한 경우 아래 단계를 계속 진행합니다.

### 2단계: 세그먼트 확장 이름 지정

필터링하려는 사용자 유형을 설명하여 세그먼트 확장의 이름을 지정합니다. 이렇게 하면 세그먼트에 필터로 적용할 때 이 확장 프로그램을 쉽고 정확하게 검색할 수 있습니다.

!["온라인 쇼핑객 확장 - 90일"이라는 이름의 세그먼트 확장에 "매일 확장 재생성" 확인란을 선택합니다.][2]

### 3단계: 기준 선택

타겟팅할 구매, 메시지 인게이지먼트 또는 커스텀 이벤트 기준 중에서 선택합니다. 원하는 이벤트 유형 기준을 선택한 후 사용자 목록에 타겟팅할 구매 항목, 메시지 상호 작용 또는 특정 커스텀 이벤트를 선택합니다. 그런 다음 사용자가 이벤트를 완료해야 하는 횟수(이상, 미만 또는 같음)와 기간(특히 세그먼트 확장의 경우 과거 730일(2년)까지 거슬러 올라갈 수 있음)을 선택합니다.

730일 이상의 이벤트 데이터를 기반으로 **세그먼트**에 있는 다른 필터를 사용하여 세그먼테이션을 수행할 수 있습니다. 기간을 선택할 때 상대적인 날짜 범위(예: 지난 X일), 시작 날짜, 종료 날짜 또는 정확한 날짜 범위(날짜 A~날짜 B)를 지정할 수 있습니다.

![사용자가 사용자 정의 이벤트 "# of aaa"를 0회 이상 수행한 경우의 세분화 기준입니다. 날짜 범위는 2023년 8월 1일부터 2023년 8월 10일까지입니다.][3]

#### 이벤트 속성 세분화

타겟팅 정밀도를 높이려면 **속성 필터 추가** 확인란을 선택합니다. 이렇게 하면 구매 또는 사용자 지정 이벤트의 특정 속성을 기반으로 드릴다운할 수 있습니다. 문자열, 숫자, 부울, 시간 개체를 기반으로 이벤트 속성정보 세분화를 지원합니다.

문자열 속성의 경우 한 번에 여러 값을 입력할 수 있습니다. 아래 예에서 이 필터는 골드, 실버 또는 브론즈 중 하나에 해당하는 상태를 가진 사용자를 찾습니다.

![문자열 속성을 기반으로 세그먼트화.][13.5]

![숫자 속성을 기반으로 세분화합니다.][13]

![부울 속성을 기반으로 세분화합니다.][14]

![날짜/시간 개체를 기반으로 세분화하기.][15]

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![중첩된 이벤트 속성을 기반으로 세분화합니다.][18]

세그먼트 확장은 이벤트 속성정보의 장기 저장에 의존하며 타임스탬프가 찍힌 속성 저장 제한이 없습니다. 지난 2년 동안 추적된 이벤트 속성정보를 되돌아볼 수 있습니다. 세그먼트 확장 내에서 이벤트 속성을 사용해도 데이터 포인트 사용에는 영향을 미치지 않습니다.

{% alert note %}
You don't need Segment Extensions to use event properties or nested custom attributes in your segment. Segment Extensions just extend the historic window used to create a segment. You can create a real-time [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) that uses event properties from the past 30 days or uses nested custom attributes. Similarly, you can [schedule your message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) to trigger in real time based on an event property—no Segment Extension required.
{% endalert %}

### 4단계: 새로고침 설정 지정(선택 사항)

정기적으로 확장 프로그램을 새로고침할 필요가 없다면, 새로고침 설정을 사용하지 않고 저장할 수 있으며, Braze는 그 순간의 사용자 멤버십에 따라 세그먼트 확장 프로그램을 생성하는 기본값으로 설정됩니다. 기본값 동작을 사용하면 오디언스를 한 번만 생성한 다음 일회성 캠페인으로 타겟팅할 수 있습니다.

당신의 세그먼트는 항상 초기 저장 후에 처리를 시작합니다. 세그먼트가 새로고침될 때마다, Braze는 세그먼트를 다시 실행하고 새로고침 시점의 세그먼트에 있는 사용자들을 반영하도록 세그먼트 멤버십을 업데이트합니다. 이것은 귀하의 반복 캠페인이 가장 관련성이 높은 사용자에게 도달하는 데 도움이 될 수 있습니다.

#### 정기적인 새로고침 설정

정기 일정을 설정하려면 특정 확장 프로그램의 오른쪽 상단 모서리에서 **새로고침 설정**을 선택하십시오. 모든 유형의 세그먼트 확장, SQL 세그먼트, CDI 세그먼트 및 간단한 양식 기반 세그먼트 확장을 포함하여 새로고침 설정을 지정하는 옵션이 제공됩니다.

{% alert important %}
To optimize your data management, refresh settings are automatically turned off for unused Segment Extensions. Segment Extension are considered unused when they're:

- Not used in any active or inactive (draft, stopped, archived) campaigns, Canvases, or segments; or
- 7일이 넘도록 수정되지 않음

Braze will notify the company contact and creator of the extension if this setting is turned off. 매일 확장 프로그램을 재생성하는 옵션은 언제든지 다시 설정할 수 있습니다.
{% endalert %}

#### 새로고침 설정 선택하기

![새로고침 간격 설정은 주간 새로고침 빈도로, 시작 시간은 오전 10시이며, 월요일이 선택된 날입니다.][21]{: style="max-width:60%;"}

**새로고침 설정** 패널 내에서 이 세그먼트 확장이 새로고침되는 빈도: 매시간, 매일, 매주 또는 매월을 선택할 수 있습니다. 당신은 또한 새로고침이 발생할 특정 시간(귀사의 시간대에 있는)을 선택해야 합니다, 예를 들어:

- 매주 월요일 오전 11시 회사 시간에 발송되는 이메일 캠페인이 있고, 발송 직전에 세그먼트가 새로고침되도록 하려면, 매주 월요일 오전 10시에 새로고침 일정을 선택해야 합니다.
- 세그먼트가 매일 새로고침되도록 하려면, 일일 새로고침 빈도를 선택한 다음 새로고침할 시간을 선택하세요.

{% alert note %}
양식 기반 세그먼트 확장에 대해 시간별 새로고침 일정 설정 기능은 제공되지 않습니다(하지만 일별, 주별 또는 월별 일정을 설정할 수 있습니다).
{% endalert %}

#### 신용 소비 및 추가 비용

새로고침이 세그먼트의 쿼리를 다시 실행하기 때문에, SQL 세그먼트의 각 새로고침은 SQL 세그먼트 크레딧을 소모하고, CDI 세그먼트의 각 새로고침은 서드파티 데이터 웨어하우스 내에서 비용이 발생합니다.

{% alert note %}
세그먼트는 데이터 처리 시간 때문에 새로고침하는 데 최대 60분이 걸릴 수 있습니다. 현재 새로 고침 중인 세그먼트는 세그먼트 확장 목록에서 "처리 중" 상태를 가집니다. 이것은 몇 가지 의미를 갖습니다:

- 특정 시간 전에 세그먼트 처리를 완료하려면 60분 더 이른 새로고침 시간을 선택하세요. 
- 특정 세그먼트 확장에 대해 한 번에 하나의 새로고침만 발생할 수 있습니다. 기존 새로고침이 이미 처리 중일 때 새 새로고침이 시작되면, Braze는 새 새로고침 요청을 취소하고 진행 중인 처리를 계속합니다.
{% endalert %}

#### 오래된 확장을 자동으로 비활성화하는 기준

세그먼트 확장이 오래된 경우 예약된 새로고침은 자동으로 비활성화됩니다. 세그먼트 확장이 오래된 경우 다음 기준을 충족합니다:

- 활성 캠페인이나 캔버스에서 사용되지 않음
- 활성 캠페인이나 캔버스에 있는 세그먼트에서 사용되지 않음
- [분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking#segment-analytics-tracking)이 켜져 있는 세그먼트에서 사용되지 않음
- 7일 이상 수정되지 않음
- 7일 이상 캠페인이나 캔버스(초안 포함) 또는 세그먼트에 추가되지 않음

세그먼트 확장에 대한 예약된 새로고침이 비활성화된 경우, 해당 확장은 그렇게 표시하는 알림이 있습니다.

![이 확장은 활성 캠페인, 캔버스 또는 세그먼트에서 사용되지 않기 때문에 "예약된 새로고침이 이 확장에 대해 꺼졌습니다."라는 알림이 있습니다. 세그먼트 확장은 2025년 2월 23일 오전 12:00에 비활성화되었습니다."][1]

오래된 세그먼트 확장을 사용하려면 [새로고침 설정을 검토](#step-4-designate-refresh-settings-optional)하고, 사용 사례에 맞는 새로고침 일정을 선택한 다음, 수정 사항을 저장하십시오.

### 5단계: 세그먼트 확장 저장

Once you select **Save**, your extension will begin processing. 확장 프로그램을 생성하는 데 걸리는 시간은 사용자 수, 캡처하는 커스텀 이벤트 또는 구매 이벤트의 수, 기록에서 되돌아보는 일수에 따라 달라집니다.

확장 프로그램이 처리되는 동안 확장 프로그램 이름 옆에 작은 애니메이션이 표시되고 확장 프로그램 목록의 **마지막 처리된** 열에 "처리 중"이라는 단어가 표시됩니다. 처리 중일 때는 확장자를 편집할 수 없다는 점에 유의하세요.

!["세그먼트 확장" 페이지에 두 개의 활성 확장이 있습니다.][5]

### 6단계: 세그먼트에서 확장 프로그램 사용

확장을 생성한 후에는 세그먼트를 만들거나 캠페인 또는 캔버스의 오디언스를 정의할 때 필터로 사용할 수 있습니다. 먼저 **사용자 속성** 섹션의 필터 목록에서 **Braze 세그먼트 확장**을 선택합니다.

!["필터" 섹션에 "Braze 세그먼트 확장"을 보여주는 필터 드롭다운이 있습니다.][6]

Braze 세그먼트 확장자 필터 목록에서 이 세그먼트에 포함하거나 제외할 확장자를 선택합니다.

!["브레이즈 세그먼트 확장" 필터로 세그먼트 "온라인 쇼핑객 확장..."을 포함합니다.][7]

To view the extension criteria, select **View Extension Details** to show the details in a modal popup.

!["온라인 쇼핑객 확장 - 90일"에 대한 확장 세부정보입니다.][8]{: style="max-width:70%;"}

이제 평소와 같이 [세그먼트 만들기][11]를 진행할 수 있습니다.

## Frequently asked questions

### 여러 커스텀 이벤트를 사용하는 세그먼트 확장을 만들 수 있나요?

예. [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을 사용할 때 여러 이벤트를 추가하거나 여러 Snowflake 테이블을 참조할 수 있습니다. 

**간단한 확장** 세그먼트 확장을 사용할 때 하나의 커스텀 이벤트, 하나의 구매 이벤트 또는 하나의 채널 상호작용을 선택할 수 있습니다. 그러나 세그먼트를 만들 때 여러 세그먼트 확장을 AND 또는 OR로 결합할 수 있습니다.

### 활성 캠페인에 존재하는 세그먼트 확장을 보관할 수 있나요?

아니요. 세그먼트 확장을 보관하기 전에 모든 활성 메시징에서 제거해야 합니다.

[1]: {% image_buster /assets/img/segment/segment_extension_disabled.png %}
[2]: {% image_buster /assets/img/segment/segment_extension2.png %}
[3]: {% image_buster /assets/img/segment/segment_extension1.png %}
[5]: {% image_buster /assets/img/segment/segment_extension5.png %}
[6]: {% image_buster /assets/img/segment/segment_extension7.png %}
[7]: {% image_buster /assets/img/segment/segment_extension6.png %}
[8]: {% image_buster /assets/img/segment/segment_extension8.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/
[11]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[12]: {% image_buster /assets/img/segment/property1.png %}
[13]: {% image_buster /assets/img/segment/property2.png %}
[13.5]: {% image_buster /assets/img/segment/property5.png %}
[14]: {% image_buster /assets/img/segment/property3.png %}
[15]: {% image_buster /assets/img/segment/property4.png %}
[16]: {% image_buster /assets/img/Shopify/arrow.jpeg %}
[17]: {% image_buster /assets/img/segment/segment_extension9.png %}
[18]: {% image_buster /assets/img/segment/nested_segment_extensions.png %}
[20]: {% image_buster /assets/img/segment/segment_extension_modal.png %}
[21]: {% image_buster /assets/img/segment/segment_interval_settings.png %}

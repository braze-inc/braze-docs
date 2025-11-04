---
nav_title: 세그먼트 확장
article_title: 세그먼트 확장
page_order: 6
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

![Table with different Segment Extension creation experiences to select from.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

SQL을 사용하는 경험을 선택하는 경우 자세한 내용은 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을 참조하세요.

**단순 확장**을 선택한 경우 아래 단계를 계속 진행합니다.

### 2단계: 세그먼트 확장 이름 지정

필터링하려는 사용자 유형을 설명하여 세그먼트 확장의 이름을 지정합니다. 이렇게 하면 세그먼트에 필터로 적용할 때 이 확장 프로그램을 쉽고 정확하게 검색할 수 있습니다.

![Segment Extension named "Online Shoppers Extension - 90 Days".]({% image_buster /assets/img/segment/segment_extension2.png %})

### 3단계: 기준 선택

타겟팅할 구매, 메시지 인게이지먼트 또는 커스텀 이벤트 기준 중에서 선택합니다. 원하는 이벤트 유형 기준을 선택한 후 사용자 목록에 타겟팅할 구매 항목, 메시지 상호 작용 또는 특정 커스텀 이벤트를 선택합니다. 그런 다음 사용자가 이벤트를 완료해야 하는 횟수(이상, 미만 또는 같음)와 기간(특히 세그먼트 확장의 경우 과거 730일(2년)까지 거슬러 올라갈 수 있음)을 선택합니다.

730일 이상의 이벤트 데이터를 기반으로 **세그먼트**에 있는 다른 필터를 사용하여 세그먼테이션을 수행할 수 있습니다. When choosing your time period, you can specify a relative date range to select the past X number of days, a start date, an end date, or an exact date range (date A to date B).

![Segmentation criteria for users who performed a custom event more than 2 times in the date range of March 1st, 2025 through March 31st, 2025.]({% image_buster /assets/img/segment/segment_extension1.png %})

#### 이벤트 속성 세분화

타겟팅 정밀도를 높이려면 **속성 필터 추가** 확인란을 선택합니다. 이렇게 하면 구매 또는 사용자 지정 이벤트의 특정 속성을 기반으로 드릴다운할 수 있습니다. 문자열, 숫자, 부울, 시간 개체를 기반으로 이벤트 속성정보 세분화를 지원합니다.

문자열 속성의 경우 한 번에 여러 값을 입력할 수 있습니다. 아래 예에서 이 필터는 골드, 실버 또는 브론즈 중 하나에 해당하는 상태를 가진 사용자를 찾습니다.

![Segmenting based on string properties.]({% image_buster /assets/img/segment/property5.png %})

![Segmenting based on numeric properties.]({% image_buster /assets/img/segment/property2.png %})

![Segmenting based on boolean properties.]({% image_buster /assets/img/segment/property3.png %})

![Segmenting based on datetime objects.]({% image_buster /assets/img/segment/property4.png %})

We also support segmentation based on [nested event properties]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

![Segmenting based on nested event properties.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

세그먼트 확장은 이벤트 속성정보의 장기 저장에 의존하며 타임스탬프가 찍힌 속성 저장 제한이 없습니다. 지난 2년 동안 추적된 이벤트 속성정보를 되돌아볼 수 있습니다. 세그먼트 확장 내에서 이벤트 속성을 사용해도 데이터 포인트 사용에는 영향을 미치지 않습니다.

{% alert note %}
You don't need Segment Extensions to use event properties or nested custom attributes in your segment. Segment Extensions just extend the historic window used to create a segment. You can create a real-time [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) that uses event properties from the past 30 days or uses nested custom attributes. Similarly, you can [schedule your message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) to trigger in real time based on an event property—no Segment Extension required.
{% endalert %}

### 4단계: 새로고침 설정 지정(선택 사항)

{% multi_lang_include segments.md section='Refresh settings' %}

### 5단계: 세그먼트 확장 저장

After you select **Save**, your extension will begin processing. 확장 프로그램을 생성하는 데 걸리는 시간은 사용자 수, 캡처하는 커스텀 이벤트 또는 구매 이벤트의 수, 기록에서 되돌아보는 일수에 따라 달라집니다.

확장 프로그램이 처리되는 동안 확장 프로그램 이름 옆에 작은 애니메이션이 표시되고 확장 프로그램 목록의 **마지막 처리된** 열에 "처리 중"이라는 단어가 표시됩니다. 처리 중일 때는 확장자를 편집할 수 없다는 점에 유의하세요.

!["Segment Extensions" page with two active extensions.]({% image_buster /assets/img/segment/segment_extension5.png %})

When a Segment Extension is processing, Braze will continue to use the version history of the segment from before the processing began for audience segmentation purposes. Processing takes place each time a save or refresh occurs, and involves querying and updating user profiles - in other words, your segment's membership does not update instantaneously. This means that unless a user's action is performed before the refresh begins processing, we can't guarantee that the user will be included in the Segment Extension once that particular refresh is complete. Conversely, users who were in the Segment Extension before the refresh that  no longer meet the criteria will continue to match your segment until the refresh process is complete and updates are applied.

### 6단계: 세그먼트에서 확장 프로그램 사용

After you have created an extension, you can use it as a filter when creating a segment or defining an audience for a campaign or Canvas. 먼저 **사용자 속성** 섹션의 필터 목록에서 **Braze 세그먼트 확장**을 선택합니다.

!["Filters" section with a filter dropdown showing "Braze Segment Extensions".]({% image_buster /assets/img/segment/segment_extension7.png %})

Braze 세그먼트 확장자 필터 목록에서 이 세그먼트에 포함하거나 제외할 확장자를 선택합니다.

![A "Braze Segment Extensions" filter that includes a segment "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension6.png %})

To view the extension criteria, select **View Extension Details** to show the details in a new window.

![Extension for "1 email click in the last 56 days".]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

Now you can proceed as usual with [creating your segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

## Frequently asked questions

### 여러 커스텀 이벤트를 사용하는 세그먼트 확장을 만들 수 있나요?

예. [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)을 사용할 때 여러 이벤트를 추가하거나 여러 Snowflake 테이블을 참조할 수 있습니다. 

**간단한 확장** 세그먼트 확장을 사용할 때 하나의 커스텀 이벤트, 하나의 구매 이벤트 또는 하나의 채널 상호작용을 선택할 수 있습니다. 그러나 세그먼트를 만들 때 여러 세그먼트 확장을 AND 또는 OR로 결합할 수 있습니다.

### 활성 캠페인에 존재하는 세그먼트 확장을 보관할 수 있나요?

아니요. 세그먼트 확장을 보관하기 전에 모든 활성 메시징에서 제거해야 합니다.

### Can I use arrays in Segment Extensions?

예. To use arrays, append brackets (`[]`) to your property name. If your property is `location_code`,  you would enter `location_code[]`. 

Braze uses `[]` to traverse arrays and check if any item in the traversed array matches the event property. For example, you could create a segment of users who match at least one value of an array property.

### How does Braze calculate the time period for a relative time period of "last \__ days"?

When Segment Extensions calculates the relative time period ("last X days"), the start time is set to midnight UTC. For example, for a Segment Extension that refreshes at 2024-09-16 21:00 UTC and specifies 10 days, the start time is set to 2024-09-06 00:00 UTC, not 2024-09-06 21:00 UTC. 

However, you can specify the time zones by using SQL segments to identify users who performed the custom event 10 days ago based on midnight in company time, or users who performed the event 10 days ago based on the current time.


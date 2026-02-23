---
nav_title: Heap Cohort Import
article_title: Heap Cohort Import
description: "This reference article details the integration between Braze and Heap, a digital insights platform, that allows you to import Heap data to Braze, create user cohorts, as well as export Braze data to Heap to create segments."
alias: /partners/heap_cohort_import/
page_type: partner
search_tag: Partner

---

# Heap cohort import

> [Heap](https://heap.io/), a digital insights platform, focuses you on opportunities in your digital experience that most impact your business, eliminating friction, delighting your customers, and accelerating revenue.

The Braze and Heap integration enables you to [import Heap data to Braze](#data-import-integration), create user cohorts, as well as [export Braze data to Heap]({{site.baseurl}}/partners/data_and_analytics/analytics/heap/) to create segments.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Heap account | A [Heap](https://heap.io/about) account is required to take advantage of this partnership. |
| Braze Data Import key | This can be captured in the Braze dashboard from **Partner Integrations** > **Technology Partners** and then select **Heap**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Braze Currents | 데이터를 브레이즈에서 힙으로 내보내려면 계정에서 [브레이즈 커런츠를]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) 인에이블먼트해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases
- Re-engage users who have abandoned a funnel: Trigger re-engagement messaging when users abandon the purchase or subscription funnel.
- Personalize the trial experience: Identify friction points in your trial experience and send correctly timed reminders to re-engage users during a trial and help them get to value.
- Drive higher engagement on announcements and offers: Target promotions, updates, and new service announcements to the relevant audiences.

## Data import integration

Use the Heap to Braze integration to automatically sync cohorts defined in Heap to Braze.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and then select **Heap**. 

On this page, you can find your data import key and a REST endpoint. Take note of both of these values and provide them to your Heap account manager to finish setting up the integration.

![]({% image_buster /assets/img/heap/heap2.png %}){: style="max-width:90%;"}

### 2단계: Segment imported users in Braze

In Braze, navigate to **Segments**, name your Heap cohort segment, and select **Heap Cohorts** as your filter. From here, you can choose which Heap cohort you wish to include. 힙 코호트 세그먼트가 생성된 후에는 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

![Braze 세그먼트 빌더에서 사용자 속성 필터 'Heap 코호트'는 '포함' 및 'Heap 테스트 코호트'로 설정되어 있습니다.]({% image_buster /assets/img/heap/heap1.png %}){: style="max-width:90%;"}

### 이 통합 사용

힙 세그먼트를 사용하려면 Braze 캠페인 또는 캔버스를 생성하고 세그먼트를 타겟 오디언스로 선택합니다.

![타겟팅 단계의 Braze 캠페인 빌더에서 '세그먼트별 타겟 사용자' 필터가 'Heap 코호트'로 설정되어 있습니다.]({% image_buster /assets/img/heap/heap3.png %}){: style="max-width:90%;"}

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

## Integration details

The payload structure for exported data is the same as the payload structure for custom HTTP connectors, which can be viewed in the [examples repository for custom HTTP connectors](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.


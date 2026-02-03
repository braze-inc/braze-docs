---
nav_title: Amplitude
article_title: Amplitude Cohort Import
description: "This reference article outlines the cohort import functionality of Amplitude, a product analytics and business intelligence platform."
page_type: partner
search_tag: Partner
---

# Amplitude cohort import

> This article covers how to import user cohorts from [Amplitude](https://amplitude.com/) to Braze. For more information on integrating Amplitude and its other functionalities, see the main [Amplitude article]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Data import integration

Any integration you set up will count toward your account's data point volume.

### Step 1: Get the Braze data import key

In Braze, navigate to **Partner Integrations** > **Technology Partners** and select **Amplitude**. Here, you will find the REST endpoint and generate your Braze data import key. 

Once generated, you can create a new key or invalidate an existing one. The data import key and the REST endpoint are used in the next step when setting up a postback in Amplitude's dashboard.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### 2단계: Set up the Braze integration in Amplitude

Amplitude에서 **Sources & 대상** > **[프로젝트 이름]** > **대상** > Braze로 이동합니다. In the prompt that appears, provide the Braze data import key and REST endpoint, and click **Save**.

![]({% image_buster /assets/img/amplitude.png %})

### 3단계: Export an Amplitude cohort to Braze

First, to export users from Amplitude to Braze, create a [cohort](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) of users you wish to export. Amplitude can sync cohorts to Braze using the following identifiers:
- User Alias
- Device ID
- User ID (External ID)

Amplitude는 우선순위에 따라 여러 식별자 매핑 속성을 지원합니다. 1차, 2차, 3차 식별자 매핑을 구성할 수 있습니다. 동기화 중 사용자가 기본 계정을 놓친 경우 Amplitude는 다음 사용 가능한 계정을 사용합니다. 이렇게 하면 동기화 범위가 개선되고, 삭제된 사용자가 줄어들며, 더 많은 익명 사용자와 부분 식별자를 동기화에 포함할 수 있습니다. 

Once you have created a cohort, click **Sync to...** to export these users to Braze.

{% alert important %}
Only users who already exist within Braze will be added or removed from a cohort. Cohort Import will not create new users in Braze.
{% endalert %}

#### Defining sync cadence

Cohort syncs can be set to be one-time sync, scheduled as daily or hourly, or even real-time which updates every minute. 

설정한 모든 통합은 데이터 포인트를 기록합니다. Braze 데이터 포인트의 미묘한 차이에 대해 궁금한 점이 있으면 Braze 계정 매니저가 답변해 드립니다.

### 4단계: Segment users in Braze

In Braze, to create a segment of these users, navigate to **Segments** under **Engagement**, name your segment, and select **Amplitude Cohorts** as the filter. Next, use the "includes" option and choose the cohort you created in Amplitude. 

![Braze 세그먼트 빌더에서 "amplitude_cohorts" 필터를 "includes_value" 및 "Amplitude 코호트 테스트"로 설정합니다.]({% image_buster /assets/img/amplitude2.png %})

After saving, you can reference this segment during Canvas or campaign creation in the targeting users step.

## User Matching

Identified users can be matched by either their `external_id` or `alias`. Anonymous users can be matched by their `device_id`. Identified users who were originally created as anonymous users can't be identified by their `device_id`, and must be identified by their `external_id` or `alias`.

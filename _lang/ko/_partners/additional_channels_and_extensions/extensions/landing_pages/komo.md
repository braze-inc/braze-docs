---
nav_title: Komo
article_title: Komo
description: "This reference article outlines the partnership between Braze and Komo, a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty. Through this integration, first and zero-party data captured in Komo can be published to Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) is a customer engagement platform specializing in gamification, interactive content, competitions, prizing, and loyalty.

_This integration is maintained by Komo._

## About the integration

The Braze and Komo integration allows you to gather first and zero-party data through Komo Engagement Hubs. These hubs are dynamic microsites that offer interactive content and gamification features. The user data collected from these hubs are then transmitted to the Braze API.

- Ingest first and zero-party user data gather from Komo to Braze in real-time
- Ingest market research and user preference data when they answer surveys, polls, and quiz questions
- Progressively build user profiles in Braze over time as the user continues to engage and share more data about themselves
- Standardize the look and feel of transactional emails sent through Braze

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Komo account | You will need an active Komo account to take advantage of this partnership. Visit [Komo](https://komo.tech/) to start a trial now. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.<br><br>For example, it should look something like: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 사용 사례

{% tabs local %}
{% tab Data Capture - Form Submission %}

When a user submits a customizable data capture form in Komo, the Komo fields mapped in the Braze integration will be passed to Braze via the `/users/track/` API call.

Data capture forms exist either at the start or end of Cards.

{% endtab %}
{% tab Market Research - Coming soon %}

또한 Komo는 사용자가 퀴즈, 설문조사, 성격 테스트, 스위퍼 등에 응답할 때 수집된 시장 조사 데이터를 전달할 수 있는 기능을 인에이블먼트합니다. This data will enable you to enhance a user's profile beyond data captured in form submissions.

{% endtab %}
{% endtabs %}

## Integration

### Step 1: Publish a Komo Engagement Hub and card

데이터 캡처 양식이 포함된 카드가 하나 이상 포함된 코모 허브를 게시해야 합니다. When published, you can test the user experience end-to-end and verify the integration is working correctly.

![코모 허브.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### 2단계: Braze 커넥티드 앱 추가하기 

코모에서 **회사 설정** 탭으로 이동하여 **연결된 앱** 섹션을 선택합니다. 

Next, find the Braze integration from the list, and select the **Connect** button to enable the integration.

![Braze 통합을 연결합니다.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![연결 Braze 통합 2b 단계.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### 워크플로우를 통해 통합 구성하기

이제 워크스페이스, 사이트 또는 카드 내에서 데이터를 Braze에 동기화하기 위한 워크플로우를 설정해야 합니다. 

워크플로우의 범위를 전체 워크스페이스, 사이트(많은 카드가 포함된 사이트) 또는 단일 카드 중 어느 범위로 설정할지는 워크플로우를 여러 카드 또는 캠페인에서 트리거할지 여부에 따라 달라집니다. 

워크플로를 만든 후 트리거를 정의하고 단계 메뉴에서 Braze를 검색하여 "사용자 추적" 단계를 추가하세요. 

![사용자 설정을 추적합니다.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

여기에서 Komo에서 Braze로 동기화할 이벤트, 기여도 및 구독을 구성합니다. 

![Content blocks list.]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## Using the integration

이제 통합이 실행 중이며 워크플로 실행 탭에서 각 실행을 모니터링할 수 있습니다. 

---
nav_title: 이메일에 대한 봇 필터링
article_title: 이메일에 대한 봇 필터링
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "이 문서에서는 이메일에 대한 봇 필터링에 대한 개요를 제공합니다."
---

# 이메일에 대한 봇 필터링

> [이메일 환경설정에서]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) 봇 필터링을 설정하여 의심되는 모든 컴퓨터 또는 봇 클릭을 제외하세요. 이메일에서 '봇 클릭'이란 자동화 프로그램에 의해 생성된 이메일 내의 하이퍼링크를 클릭하는 것을 말합니다. 이러한 봇 클릭을 필터링하여 참여 중인 수신자에게 의도적으로 메시지를 트리거하고 전달할 수 있습니다.

{% alert important %}
2025년 7월 9일부터 새로 생성되는 모든 워크스페이스에 봇 필터링 설정이 적용되어 Braze에서 보다 정확한 클릭 보고가 가능해집니다.
{% endalert %}

## 봇 클릭 정보

Braze는 여러 입력을 사용하여 의심되는 봇 클릭(비인간 상호작용(NHI)이라고도 함)을 식별하는 탐지 시스템을 갖추고 있습니다. 봇 클릭은 클릭률을 인위적으로 부풀려 이메일 참여 측정기준을 왜곡할 수 있습니다. 이러한 접근 방식을 통해 실제 사용자 상호작용과 봇 활동으로 의심되는 활동을 구분하여 클릭 참여 측정기준과 인사이트의 통합성을 유지할 수 있습니다.

## 봇 클릭의 영향을 받는 측정기준

{% alert note %}
봇 필터링은 자동화가 의심되는 클릭을 적극적으로 차단하여 참여 측정기준의 정확성을 높입니다. 그러나 스캐너와 봇은 시간이 지남에 따라 계속 진화하기 때문에 Braze가 사람 이외의 모든 상호작용을 제거한다고 보장할 수는 없습니다.
{% endalert %}

봇 클릭의 영향을 받을 수 있는 Braze 측정기준은 다음과 같습니다:

- 총 클릭률
- 고유 클릭률
- 클릭 투 오픈율
- 전환율('클릭 캠페인'을 전환 이벤트로 선택한 경우)
- 히트맵
- 특정 세그먼트 필터

탐지 시스템에서 클릭 데이터를 활용하는 [Braze 인텔리전스 기능이]({{site.baseurl}}/user_guide/brazeai/intelligence) 영향을 받을 수 있습니다. 이 설정을 켜면 봇으로 의심되는 클릭이 제외되어 일시적으로 탐지 시스템이 중단될 수 있으며, 이로 인해 측정기준 또는 입력값이 감소할 수 있습니다:

- 지능형 선택
- 인텔리전트 채널
- Intelligent Timing
- 실험 단계
    - 우승 경로
    - 개인화된 경로
- 캠페인
    - 우승 배리언트
    - 개인화된 배리언트
- 예상 실제 열람율

의심되는 봇 클릭에 대한 탈퇴는 영향을 받지 않습니다. Braze는 평소와 같이 모든 탈퇴 요청을 계속 처리할 것입니다. Braze에서 이러한 탈퇴를 차단하려면 [제품 피드백을]({{site.baseurl}}/user_guide/administrative/access_braze/portal) 제출하세요.

## 봇 필터링의 영향을 받는 세분화 필터

이메일 메시지에 대한 봇 필터링의 영향을 받을 수 있는 [세분화 필터는]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) 다음과 같습니다:

- [클릭/열린 캠페인 또는 태그가 있는 캔버스]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [클릭/열기 단계]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-step)
- [캠페인에서 별칭 클릭]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-campaign)
- [캔버스 단계에서 별칭 클릭]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [캠페인 또는 캔버스 단계에서 별칭 클릭]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [마지막으로 메시징에 참여한 시간]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#last-engaged-with-message)
- [인텔리전트 채널]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#intelligent-channel)

## 봇 필터링 켜기

**설정** > **이메일 환경설정으로** 이동합니다. 그런 다음 **봇 클릭 제거를** 선택합니다. 이 설정은 워크스페이스 수준에서 적용됩니다.

의심되는 봇 클릭은 이 설정을 켠 후에만 제거되며, 워크스페이스의 측정기준에는 소급 적용되지 않습니다.

\![이메일 환경설정에서 봇 필터링 이메일 설정이 켜져 있습니다.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
이 설정을 켰다가 나중에 끄면 이전에 제거한 봇 활동을 분석에 복원할 수 없습니다.
{% endalert %}

## 커런츠 및 Snowflake에 대한 이메일 클릭 이벤트의 필드

Braze는 이메일 클릭 이벤트를 위해 커런츠와 스노우플레이크에서 `is_suspected_bot_click` 및 `suspected_bot_click_reason` 필드를 전송합니다.

| 필드 | 데이터 유형 | 설명 | 설명
| `is_suspected_bot_click` | 부울 | 봇 클릭으로 의심되는 경우임을 나타냅니다. **봇 클릭** 작업 영역 **제거** 설정을 켜기 전까지는 null 값으로 전송됩니다. 이 접근 방식을 사용하면 작업 공간에서 의심되는 봇 클릭에 대한 필터링이 시작된 시점을 프로그래밍 방식으로 파악하여 커런츠 및 Snowflake의 데이터와 정확하게 비교할 수 있습니다. |
| `suspected_bot_click_reason` | 배열 | 봇 클릭으로 의심되는 이유를 표시합니다. 봇 필터링 작업 영역 설정이 비활성화되어 있어도 `user_agent` 및 `ip_address` 과 같은 값으로 채워집니다. 이 필드는 봇 클릭으로 의심되는 클릭 수와 사람과의 상호작용을 비교하여 이 설정을 켰을 때의 잠재적 영향에 대한 인사이트를 제공할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 자주 묻는 질문

### 봇 필터링이 캠페인의 성능/성과에 어떤 영향을 미치나요?

이미 전송된 이전 캠페인의 측정기준에는 영향을 미치지 않습니다. 작업 영역에서 봇 필터링이 켜져 있으면 Braze는 모든 클릭에서 봇으로 의심되는 클릭을 필터링하기 시작합니다. 클릭률이 떨어질 수 있지만 클릭률은 이메일 메시징에 대한 사용자의 참여율을 더 정확하게 나타냅니다.

### 봇 필터링이 Braze 구독 취소 링크를 클릭하는 봇의 탈퇴를 방지하나요?

아니요. 모든 탈퇴 요청은 계속 처리됩니다.

### 봇 클릭 필터링에서 머신 오픈이 고려되나요?

아니요.

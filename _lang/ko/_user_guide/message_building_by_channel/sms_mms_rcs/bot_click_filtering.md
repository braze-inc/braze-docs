---
nav_title: "봇 클릭 필터링"
article_title: "SMS 및 RCS 봇 클릭 필터링"
description: "이 참고 문서에서는 SMS 및 RCS 봇 클릭 필터링에 대해 설명합니다."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 11
channel:
  - SMS
  - RCS
---

# SMS 및 RCS 봇 클릭 필터링

> SMS 및 RCS 봇 클릭 필터링은 의심스러운 봇 클릭을 제외하여 캠페인 분석 및 워크플로우를 개선합니다. "봇 클릭"이란 웹 크롤러, Android 및 iOS 링크 미리보기 또는 CPaaS 보안 소프트웨어와 같은 SMS 및 RCS 메시징의 단축 링크에 대한 자동화된 클릭을 의미합니다. 이 기능은 정확한 보고, 세분화 및 오케스트레이션을 통해 실제 사용자의 참여를 유도할 수 있습니다. <br><br> 이메일 캠페인 봇 클릭 필터링에 대해서는 [이메일에 대한 봇 필터링을]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/bot_filtering/) 참조하세요.

## 작동 방식

Braze는 여러 입력을 사용하여 의심되는 봇 클릭, 즉 비인간 상호작용(NHI)을 식별하는 독자적인 탐지 시스템을 보유하고 있습니다. 봇 클릭은 클릭률을 부풀려 참여율 측정기준을 왜곡할 수 있습니다. 이를 필터링함으로써 Braze는 의사 결정에 필요한 신뢰할 수 있는 데이터를 쉽게 캡처할 수 있습니다.

저희 시스템은 웹 크롤러, Android 및 iOS 링크 미리보기 또는 CPaaS 보안 소프트웨어와 관련된 사용자 에이전트를 분석합니다. 필터링된 사용자 에이전트의 몇 가지 예는 `GoogleBot`, `python-requests/2.32.3`, `Barracuda Sentinel (EE)` 입니다.

## 영향을 받는 측정기준 및 워크플로

봇 클릭의 영향을 받는 Braze 측정기준 및 워크플로는 다음과 같습니다:

- **_총 클릭 수_:** 캠페인 분석과 캔버스 분석은 봇 클릭을 제외하여 사람의 상호 작용만 반영합니다.
- **세분화 필터:** SMS 링크 상호 작용을 참조하는 세그먼트 필터는 캠페인과 캔버스에서 보다 정확한 리타겟팅을 위해 봇 클릭을 제외합니다.
- **오케스트레이션:** 봇 클릭은 행동 기반 트리거와 SMS 링크 상호 작용을 참조하는 캔버스 행동 경로에서 필터링되어 트리거가 사람의 행동을 반영할 수 있도록 합니다.
- **Braze Intelligence:**
    - **지능형 선택:** 배리언트 선택 최적화 시 봇 클릭을 제외합니다.
    - **인텔리전트 채널:** 정확한 채널 선택을 위해 SMS 또는 RCS를 선택한 경우 봇 클릭은 제외합니다.
    - **실험 단계:** 신뢰할 수 있는 실험 결과를 위해 봇 클릭은 제외합니다.
    - **커런츠 데이터 내보내기:** `is_suspected_bot_click` 및 `suspected_bot_click_reason` 필드를 포함하여 사람과 봇의 클릭을 분석하는 데 도움이 됩니다. 이러한 필드는 [커런츠]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), [쿼리 빌더에서]({{site.baseurl}}/user_guide/analytics/query_builder/) 사용할 수 있습니다.

의심되는 봇 클릭에 대한 탈퇴는 영향을 받지 않습니다. Braze는 평소와 같이 모든 탈퇴 요청을 처리합니다. 이러한 탈퇴를 차단하려면 [제품 피드백을 제출하세요]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## SMS 클릭 이벤트의 커런츠 필드

Braze에는 SMS 클릭 이벤트를 위한 다음 커런츠 필드가 포함되어 있습니다:

| 필드 | 데이터 유형 | 설명 |
| --- | --- | --- |
| `is_suspected_bot_click` | 부울 | 클릭이 봇 클릭으로 의심되는지 여부를 표시합니다. 회사에 봇 클릭 필터링이 인에이블먼트될 때까지 모든 사용자에 대해 `null` 을 반환합니다. 인에이블먼트가 활성화되면 앞으로 모든 신규 클릭에 대해 `true` 또는 `false` 으로 채워집니다. |
| `suspected_bot_click_reason` | 문자열, 배열 | 봇으로 의심되는 클릭의 이유를 표시합니다(예: `user_agent`). 필터링이 비활성화되어 있어도 봇 활동에 대한 잠재적 인사이트를 제공합니다. 이 필드는 전 세계에서 사용할 수 있으며 봇 클릭 필터링이 아직 인에이블먼트되지 않은 경우에도 모든 사용자의 사유로 채워집니다. 이를 통해 봇 클릭 필터링을 인에이블먼트하기 전에 잠재적인 봇 활동에 대한 인사이트를 얻을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## 쿼리 빌더 템플릿

데이터 분석에 도움이 필요하면 [쿼리 빌더에서]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) 미리 구축된 **봇별** 모바일 템플릿 **SMS 클릭 이벤트를** 사용할 수 있습니다.

## 자주 묻는 질문

### 봇 클릭 필터링은 캠페인 성능/성과에 어떤 영향을 미치나요?

필터링은 이전에 전송한 캠페인에는 영향을 미치지 않습니다. 인에이블먼트가 활성화되면 해당 순간부터 봇 클릭을 제외하여 클릭률을 낮춥니다.

### 봇 클릭 필터링으로 봇이 탈퇴 링크를 클릭하는 것을 방지할 수 있나요?

아니요. 모든 탈퇴 요청은 평소와 같이 처리됩니다.

### 봇 클릭 필터링에 링크 미리보기가 포함되나요?

예. 링크 미리보기(예: Android 및 iOS 링크 미리보기)는 봇 클릭으로 플래그가 지정되고 필터링됩니다.

### 봇 클릭 필터링은 어떻게 인에이블하나요?

얼리 액세스 기간 동안 봇 클릭 필터링을 인에이블하려면 Braze 계정 팀에 문의해야 합니다. 봇 클릭 필터링이 일반 사용 가능하면 모든 SMS 및 RCS 사용자에게 이 기능이 기본값으로 켜집니다.

또한 [링크 단축을]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) 위한 고급 클릭 추적을 인에이블했는지 확인하세요. 이렇게 하면 개별 사용자 수준에서 이 데이터를 추적하여 봇 클릭 분석을 받을 수 있습니다. 

{% alert note %}
추가 도움이 필요하면 [지원팀에 문의하세요]({{site.baseurl}}/braze_support/).
{% endalert %}
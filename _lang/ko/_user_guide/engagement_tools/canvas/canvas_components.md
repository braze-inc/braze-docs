---
nav_title: 캔버스 구성 요소
article_title: 캔버스 구성 요소
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "캔버스 구성 요소"
guide_top_text: "캔버스 구성 요소로 캔버스 여정을 향상하세요. 캔버스 구성 요소를 사용하면 과도한 전체 단계를 단 한 단계로 대체하여 캔버스의 효과를 결정하는 프로세스를 간소화할 수 있습니다. 캔버스의 구성 요소는 캔버스 브랜치에서 개인화된 사용자 여정을 나타냅니다."

page_type: landing
description: "이 랜딩 페이지에는 고급 캔버스를 만드는 데 도움이 되는 캔버스 구성 요소 문서가 있습니다. 이러한 구성 요소 중 일부에는 메시지 단계, 지연 단계, 결정 분할 단계 등이 포함됩니다."
tool: Canvas

guide_featured_title: "섹션 기사"
guide_featured_list:
  - name: 메시지 단계
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: 지연 단계
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: 결정 분할 단계
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: 오디언스 경로 단계
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: 행동 경로 단계  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: 실험 경로 단계
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: 사용자 업데이트 단계
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: 캔버스의 기능 플래그
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: 캔버스 오디언스 동기화
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## 캔버스 구성 요소 정보

캔버스 구성 요소를 사용하면 새로운 사용자 여정을 열어 프로세스를 개선하고 오디언스 도달의 효율성을 높일 수 있습니다.

### 사용자 여정 맞춤화

![의사 결정 분할 단계와 지연 단계 및 메시지 단계가 있는 캔버스 사용자 여정의 예.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

[작업 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths)를 사용하여 구매와 같은 행동 및 인게이지먼트 이벤트를 기반으로 사용자 여정을 분할할 수 있습니다. 오디언스를 필터링하고 타겟팅하려는 경우, [오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)를 사용하면 오디언스 기준에 따라 사용자를 다양한 캔버스 경로로 전송하여 사용자 타겟팅을 간소화할 수 있습니다.

[의사 결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 구성 요소는 간단한 "예 또는 아니오" 논리를 사용하여 작업 또는 사용자 속성을 기반으로 사용자 여정에 대한 두 개의 상호 배타적인 경로를 만듭니다. 이를 통해 사용자 그룹을 식별하고 타겟팅할 수 있습니다.

[지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) 구성 요소를 사용하면 캔버스에서 단일 단계를 지연시킬 수 있습니다. 캔버스의 이 독립형 지연 단계는 특정 시간에 사용자에게 메시지를 전달하는 데 가장 적합합니다. 또한 지연 구성 요소를 사용하면 오디언스가 구성 요소의 기준을 충족하는 데 더 많은 시간을 허용하여 잠재고객 도달 범위를 늘릴 수도 있습니다.

### 테스트

사용자 여정을 만들 때 가장 효과적인 캔버스 경로를 테스트할 수도 있습니다. [실험 경로를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) 사용하면 어느 단계에서나 여러 캔버스 경로를 테스트할 수 있습니다. 단계 간 연결을 개략적인 미리보기로 사용할 수도 있습니다. 주황색 연결은 이전 단계에서 사용자가 즉시 다음 단계로 넘어가는 것을 나타냅니다.

### 통합

브랜드의 퍼스트 파티 사용자 데이터와 동기화하고 싶으신가요? [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) 및 [Google에서]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) 사용 가능한 오디언스 동기화 옵션을 활용하세요.


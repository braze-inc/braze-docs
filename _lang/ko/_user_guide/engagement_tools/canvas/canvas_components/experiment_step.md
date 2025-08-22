---
nav_title: 실험 경로 
article_title: 실험 경로 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "이 문서에서는 사용자 여정의 어느 시점에서든 여러 캔버스 경로를 서로 비교하고 대조군을 테스트할 수 있는 구성 요소인 실험 경로에 대해 설명합니다."
tool: Canvas
---

# 실험 경로

> 실험 경로를 사용하면 사용자 여정의 어느 시점에서든 여러 캔버스 경로를 서로 비교하고 대조군을 테스트할 수 있습니다. 이 구성 요소를 사용하면 경로 성과를 추적하여 Canvas 여정에 대한 정보에 입각한 결정을 내릴 수 있습니다.

사용자 여정에 실험 경로 단계를 포함하면 생성한 여러 경로(또는 선택적 대조군)에 사용자를 무작위로 할당합니다. 선택한 비율에 따라 대상의 일부가 다른 경로에 할당되므로 서로 다른 메시지 또는 경로를 테스트하고 가장 효과적인 경로를 결정할 수 있습니다. 

![경로 1, 경로 2 및 제어로 분할되는 실험 경로 단계입니다.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## 사용 사례

실험 경로는 전달, 케이던스, 메시지 카피 및 채널 조합을 테스트하는 데 가장 적합합니다.

- **전달:** 사용자 작업[(작업 경로)]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)을 기반으로 [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas)을 사용하여 서로 다른 시간 [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)으로 전송된 메시지 간의 결과를 비교합니다.<br><br>
- **케이던스:** 특정 기간 동안 여러 메시징 흐름을 테스트합니다. 예를 들어 두 가지 다른 온보딩 케이던스를 테스트할 수 있습니다:
    - 케이던스 1: 사용자의 첫 2주 동안 2번의 메시지 보내기
    - 케이던스 2: 사용자의 첫 2주 동안 3번의 메시지 보내기
    
    휴면 사용자를 타겟팅할 때 일주일에 두 번의 윈백 메시지를 보내는 것과 한 번만 보내는 것의 효과를 테스트해 볼 수 있습니다.
- **메시지 복사본:** 표준 [A/B 테스트와]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) 마찬가지로 다양한 메시지 문구를 테스트하여 어떤 문구가 더 높은 전환율을 가져오는지 확인할 수 있습니다.<br><br>
- **채널 조합:** 다양한 메시지 채널 조합의 효과를 테스트하세요. 예를 들어 이메일만 사용하는 경우와 푸시와 함께 사용하는 경우의 효과를 비교할 수 있습니다.

## 필수 조건

실험 경로를 사용하려면 캔버스에 전환 이벤트가 포함되어 있어야 합니다. 캔버스가 실행된 후에는 전환 이벤트를 추가할 수 없지만, 실행된 캔버스를 복제하고 전환 이벤트를 추가하여 실험 경로를 추가할 수 있습니다.

## 실험 경로 만들기

실험 경로 구성 요소를 만들려면 먼저 캔버스에 단계를 추가합니다. 사이드바에서 구성요소를 끌어서 놓거나 단계 하단의 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **실험 경로**를 선택합니다. 

이 구성요소의 기본 구성에는 **경로 1**과 **경로 2**의 두 가지 기본 경로가 있으며, 각 경로를 통해 오디언스의 50%가 전송됩니다. 컴포넌트를 클릭하여 **실험 설정** 패널을 확장하면 컴포넌트에 대한 구성 옵션이 표시됩니다.

### 1단계: 경로 수 및 대상자 분포 선택

**경로 추가를** 클릭하여 최대 4개의 경로를 추가할 수 있으며, **제어 그룹 추가를** 선택하여 선택적 제어 그룹을 추가할 수 있습니다. 각 경로의 백분율 상자를 사용하여 각 경로와 대조군으로 이동해야 하는 오디언스의 백분율을 지정할 수 있습니다. 계속 진행하려면 제공된 백분율을 100%로 합산해야 합니다. 사용 가능한 모든 경로(및 제어)를 동일한 비율로 빠르게 설정하려면 **경로 균등 배포**를 클릭합니다.

또한 대조군의 사용자가 캔버스에서 계속 내려갈지 아니면 **대조군 행동**에 대한 전환 추적 창이 끝난 후 종료할지 선택할 수 있습니다. 선택 사항으로 설명을 추가하여 이 실험 경로에서 테스트하려는 내용을 다른 사람에게 설명하거나 참고할 만한 추가 정보를 포함할 수 있습니다.

![실험 설정에서 경로를 추가하고 각 경로의 사용자 비율을 배포할 수 있습니다.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
캔버스 재자격성이 활성화된 경우 캔버스에 들어가서 무작위로 선택한 경로를 따라 이동한 사용자가 재자격이 되어 캔버스에 다시 들어가면 동일한 경로를 다시 따라 이동합니다. 이렇게 하면 실험 및 관련 분석의 유효성을 유지할 수 있습니다. 단계에서 항상 경로 할당을 무작위로 지정하려면 **실험 경로에서 무작위 경로**를 선택합니다. 이 옵션은 위닝 또는 개인화된 경로를 사용할 때는 사용할 수 없습니다.
{% endalert %}

### 2단계: 위닝 경로 또는 개인화된 설정된 경로 켜기(선택 사항) {#step-2}

[위닝 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) 또는 [개인화된 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths)를 켜서 실험을 최적화하도록 선택할 수 있습니다. 두 옵션 모두 처음에 일부 오디언스를 대상으로 경로를 테스트하는 방식으로 작동합니다. 실험이 종료되면 남은 사용자와 후속 사용자에게 전체적으로 가장 성과가 좋은 경로(우승 경로) 또는 각 사용자별로 가장 성과가 좋은 경로(개인화된 경로)가 전송됩니다.

### 3단계: 경로 만들기

마지막으로 다운스트림 경로를 구축해야 합니다. **완료**를 선택하고 캔버스 빌더로 돌아갑니다. 각 경로 아래에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하여 원하는 대로 일반적인 캔버스 도구를 사용하여 여정을 만들기 시작하고 준비가 되면 캔버스를 실행합니다.

![실험 경로 구성 요소에서 분리되는 각 경로에 단계 추가.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

경로와 그 하위 단계는 생성된 후에는 캔버스에서 제거할 수 없다는 점에 유의하세요. 그러나 시작하면 경로 전반에 걸친 오디언스 분포를 원하는 대로 수정할 수 있습니다. 예를 들어, 캔버스를 시작한 지 하루가 지난 후 분석 결과 한 경로가 다른 경로보다 우수하다고 결론을 내린 경우 해당 경로를 100%로 설정하고 다른 경로를 0%로 설정할 수 있습니다. 또는 필요에 따라 여러 경로로 사용자를 계속 보낼 수도 있습니다.

{% alert important %}
실험 오염을 방지하기 위해 캔버스에 활성 또는 진행 중인 실험이 있고 활성 캔버스를 업데이트하는 경우(실험 경로 단계가 아니더라도) 진행 중인 실험이 종료됩니다. 실험을 다시 시작하려면 기존 실험 경로의 연결을 끊고 새 실험 경로를 시작하거나 캔버스를 복제하고 새 캔버스를 시작하면 됩니다. 또한 실험 경로 단계가 있는 이미 활성화된 캔버스에 대해서는 개인화된 경로 또는 위닝 경로를 켤 수 없습니다.<br><br>For more information, refer to [Editing Canvases after launch]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## 성과 추적

**캔버스 애널리틱스** 페이지에서 실험 경로를 클릭하여 **변형 분석** 탭과 동일한 [세부 테이블을]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) 열어 경로 전반의 세부 성과 및 전환 통계를 비교합니다. 또한 CSV를 통해 테이블을 내보내고 선택한 경로 또는 컨트롤을 기준으로 관심 있는 지표의 변경 비율을 비교할 수도 있습니다.

Each step in each path will display statistics in the [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) view, just like any Canvas step. 그러나 개별 단계의 분석은 실험의 구조를 **고려하지 않는다는** 점에 유의하세요. 실험 단계의 분석은 여러 경로를 비교하는 데 사용해야 합니다.

### 우승 경로 및 개인화된 경로 성과

위닝 경로를 활용하여 일정 기간 동안의 성과를 추적한 다음, 가장 성과가 좋은 경로로 후속 사용자를 자동으로 보내세요. 실험에 대해 **위닝 경로** 또는 **개인화된 경로**가 켜져 있는 경우의 분석에 대한 자세한 내용은 다음을 참조하세요:

- [위닝 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [개인화된 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### 추가 설정

실험 경로는 각 단계를 입력하고 지정된 경로에 있는 동안 변환하는 사용자를 기록합니다. 이렇게 하면 캔버스 설정에 지정된 모든 전환 이벤트를 추적할 수 있습니다. **추가 설정** 탭에서 이 실험에서 전환을 추적할 일수(1~30일 사이)를 입력합니다. 여기에서 지정하는 시간 창에 따라 실험을 위해 (캔버스 설정에서 선택한) 전환 이벤트를 추적할 기간이 결정됩니다. 캔버스 설정에 지정된 이벤트별 전환 기간은 이 단계의 추적에 적용되지 않으며 이 전환 기간으로 대체됩니다.


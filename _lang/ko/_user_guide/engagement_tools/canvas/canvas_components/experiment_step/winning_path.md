---
nav_title: 위닝 경로 
article_title: 실험 경로에서의 위닝 경로 
page_type: reference
description: "이 참조 문서에서는 실험 경로 단계를 켰을 때 A/B 테스트를 자동화할 수 있는 기능인 위닝 경로에 대해 설명합니다."
tool: Canvas
---

# 실험 경로에서의 위닝 경로

> Winning Path is similar to [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) in campaigns, and lets you automate your A/B tests.

실험 경로 단계에서 위닝 경로가 켜져 있으면 지정된 기간이 지나면 이후의 모든 사용자가 전환율이 가장 높은 경로로 전송됩니다.

## 승리 경로 사용

### 1단계: Add an Experiment Path step

캔버스에 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)를 추가한 다음 **위닝 경로를 켭니다**.

![실험 경로의 "후속 사용자를 위닝 경로에 배포"라는 제목의 설정. The section includes a toggle for Winning Path, and options to configure the conversion event and experiment window.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### 2단계: 당첨 경로 설정 구성

당첨자를 결정할 전환 이벤트를 지정합니다. 사용 가능한 전환 이벤트가 없는 경우 캔버스 설정의 첫 번째 단계로 돌아가서 [전환 이벤트를 할당합니다]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 열기 및 클릭으로 당첨자를 결정하는 경우, 열기 또는 클릭을 생성하는 경로의 첫 번째 메시지만 당첨자 결정에 기여한다는 점에 유의하세요.

다음으로 **실험 기간**을 설정합니다. **실험** 기간은 실험을 실행할 기간을 지정하여 위닝 경로가 결정되고 모든 사용자가 해당 경로로 이동하기 전까지 실험을 진행하도록 합니다. 기간은 첫 번째 사용자가 단계에 들어가면 시작됩니다.

![Winning Path Settings with the conversion event "Clicks" selected for a 12-hour experiment window.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### 3단계: 대체 결정 {#statistical-significance}

기본적으로 테스트 결과가 통계적으로 유의미한 승자를 결정하기에 충분하지 않은 경우, 모든 향후 사용자는 가장 성능이 좋은 경로로 보내집니다.

또는 **향후 모든 사용자에게 경로 혼합을 계속 보내기**를 선택할 수도 있습니다. 이 옵션을 선택하면 실험 경로 분포에 지정된 비율에 따라 향후 사용자에게 경로 혼합을 보냅니다.

!["Continue sending all future users the mix of paths" selected as what will happen to users if the test result isn't statistically significant.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
지연 그룹은 캔버스가 일회성 항목으로 설정되어 있고 실험 단계의 경로가 3개 이하인 경우에만 경로 분포에 나타납니다. 반복 및 트리거된 캔버스에는 위닝 경로가 켜져 있는 경우 지연 그룹이 없습니다.
{% endalert %}

### 4단계: 경로를 추가하고 캔버스를 시작합니다.

하나의 실험 경로 구성 요소에는 최대 4개의 경로를 포함할 수 있습니다. 그러나 캔버스가 [일회성 항목](#one-time-entry)으로 설정된 경우, 위닝 경로가 켜져 있을 때 Braze가 자동으로 추가하는 지연 그룹을 위해 하나의 경로를 예약해야 합니다. 즉, 일회성 항목이 있는 캔버스의 경우 실험에 최대 3개의 경로를 추가할 수 있습니다.

필요에 따라 캔버스 설정을 완료한 다음 캔버스를 실행합니다. 첫 번째 사용자가 실험에 참여하면 캔버스에서 분석이 들어오는 것을 확인하고 [실험의 성과를 추적]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)할 수 있습니다.

위닝 경로가 종료되면 캔버스에 다시 입장하여 이전에 실험 경로 단계의 대조군에 속했던 사용자를 포함하여 이후 캔버스에 입장하는 모든 사용자가 위닝 경로로 이동합니다.

## 분석 {#analytics}

승리 경로가 켜져 있으면 분석 보기가 두 개의 탭으로 분리됩니다: **초기 실험** 및 **성공 경로**.

- **초기 실험:** 실험 기간 동안 각 경로에 대한 메트릭을 표시합니다. 지정된 전환 이벤트에 대한 모든 경로의 실적과 어떤 경로가 위너로 선택되었는지에 대한 요약을 확인할 수 있습니다.
- **위닝 경로:** 초기 실험이 완료된 순간부터 시작하여 위닝 경로에 대한 측정기준만 표시합니다.

## 알아두어야 할 사항

### 일회성 항목 {#one-time-entry}

사용자가 한 번만 입장할 수 있는 캔버스에서 위닝 경로를 사용하는 경우 지연 그룹이 자동으로 포함됩니다. 실험 기간 동안 일부 사용자는 지연 그룹에 유지되고 나머지 사용자는 실험 경로로 들어갑니다.

![Experiment Step with a Delay Group for Winning Path]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

테스트가 완료되고 우승 경로가 결정되면 지연 그룹에 할당된 사용자는 선택한 경로로 이동하여 캔버스를 계속 진행하게 됩니다.

![Experiment Step with a Delay Group sent down the Winning Path]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### 현지 시간 배송

위닝 경로가 있는 캔버스에서는 현지 시간 전달을 사용하지 않는 것이 좋습니다. 이는 첫 번째 사용자가 통과할 때 실험 기간이 시작되기 때문입니다. 매우 이른 시간대에 있는 사용자는 예상보다 훨씬 일찍 단계에 진입하여 실험 기간의 시작을 트리거할 수 있으며, 이로 인해 일반적인 시간대에 있는 대부분의 사용자가 캔버스에 진입하거나 전환할(또는 두 가지 모두) 충분한 시간을 갖기 전에 실험이 종료될 수 있습니다. 

또는 로컬 전달을 사용하려면 24-48시간 이상의 실험 기간을 사용하세요. 이렇게 하면 이른 시간대의 사용자가 캔버스에 들어가서 실험을 시작해도 실험 창에 충분한 시간이 남아 있습니다. 이후 시간대의 사용자는 캔버스와 실험 단계에 들어가서 실험 기간이 만료되기 전에 전환할 수 있는 충분한 시간을 가질 수 있습니다.


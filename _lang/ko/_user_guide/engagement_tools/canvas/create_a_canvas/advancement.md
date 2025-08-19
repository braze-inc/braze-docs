---
nav_title: 발전 행동
article_title: 발전 행동
page_order: 10
alias: /auto_advance/
page_type: reference
description: "이 참조 문서에서는 진도 동작에 대해 설명하고 캔버스를 진행하면서 발생할 수 있는 다양한 시나리오를 다룹니다."
tool: Canvas

---

# 발전 행동

{% alert important %}
2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 문서는 사용자가 원래 편집기에서 캔버스 구성 요소를 진행하는 방법을 이해하는 데 참조할 수 있습니다. <br><br>캔버스 흐름의 구성요소의 경우, **진행 동작**은 항상 오디언스 즉시 진행 또는 **즉시 심화 오디언스**로 설정됩니다. 이는 [연결이 끊어진 단계에도]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#disconnected-steps/) 적용됩니다.
{% endalert %}

> The **Advancement Behavior** feature allows you to choose the criteria for advancement through your [Canvas component]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). 

![Advancement Behavior settings with two options to either advance the audience when the message is sent, or to immediately advance the audience.]({% image_buster /assets/img/push-advancement-behavior.png %} "Advancement Behavior")

사용자가 해당 단계를 진행하려면 해당 단계의 기준을 충족해야 합니다. [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 단계를 사용하면 전달 유효성 검사를 켜서 메시지 전송 시 대상 그룹이 전달 기준을 충족하는지 확인할 수 있습니다. 이는 캔버스 흐름을 사용할 때 단계의 기준에 포함됩니다. 따라서 사용자가 배달 유효성 검사 기준을 충족하지 못하면 캔버스에서 종료됩니다.

**메시지 전송 시 사전 진행**을 선택하면 다음 조건 중 하나가 발생할 때만 사용자가 후속 캔버스 단계로 진행됩니다:

- 이메일 메시지가 전송됩니다.
- 푸시 메시지가 전송됩니다.
- 웹훅이 전송됩니다.
- 인앱 메시지 보기
- 콘텐츠 카드가 전송됩니다.

**즉시 심화 오디언스**를 선택하면 다음 조건 중 하나가 발생하면 사용자가 다음 캔버스 단계로 진행됩니다:

- 모든 메시지가 전송되거나 단계의 인앱 메시지가 라이브 상태가 됩니다.
- 웹훅으로 인해 오류가 발생하여 웹훅이 전송되지 않습니다.
- 푸시 또는 이메일로 사용자에게 연결할 수 없기 때문에 푸시 또는 이메일이 전송되지 않습니다.
- 콘텐츠 카드 전송이 시도되었습니다 
- 카드가 중단되어 전송되지 않음
- 최대 게재빈도가 설정되어 메시지가 전송되지 않습니다.
- 메시지가 중단되어 전송되지 않습니다.

### 예약된 단계

예약된 구성 요소의 경우 사용자가 단계를 진행하려면 해당 단계의 오디언스 옵션을 충족해야 합니다. If the step has an [exception event]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events), users who perform the exception event will not be advanced through the step.

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)을 사용하여 멀티채널 구성요소를 보낼 때 채널별로 서로 다른 시간에 메시지를 보내거나 보내려고 시도할 수 있습니다. Braze는 구성요소의 첫 번째 메시지가 전송을 시도할 때 사용자에게 자동 전진합니다.

### 작업 기반 단계

동작 기반 단계의 경우 사용자가 트리거 동작을 수행하고 오디언스 옵션을 충족해야 단계를 진행시킬 수 있습니다. 단계에 예외 이벤트가 설정되어 있는 경우, 해당 예외 이벤트를 수행하는 사용자는 단계를 넘어서 진행되지 않습니다.

{% alert important %}
메시지 수신 없이 단계가 진행된 사용자는 해당 단계에 대한 고유 수신자로 카운트되지 않습니다. 사용자가 고유 수신자로서 카운트되려면 단계에서 하나 이상의 메시지를 수신해야 합니다.
{% endalert %}

## 사용 사례

진행은 후속 메시징이 이전 메시지와 관련이 있을 때 잘 작동합니다. 예를 들어, 사용자에게 전송되지 않은 이메일에 대한 후속 푸시를 보내고 싶지 않을 것입니다.

사용자가 특정 메시지를 받지 못하더라도 캔버스를 계속 진행하기를 원하는 경우가 있을 수 있습니다. 예를 들어 3일차에는 "환영" 푸시를 보내고 6일차에는 "환영" 이메일을 보낼 수 있습니다. 모든 사용자가 푸시 메시지 수신에 동의하는 것은 아니므로 일부 사용자는 푸시 알림을 통해 연락이 닿지 않을 수 있습니다. 3일차 푸시를 받지 않은 사용자라도 6일차 이메일을 모든 사용자에게 보낼 수 있습니다.

이 시나리오에서는 진행 행동 옵션을 사용하여 사용자가 3일차 푸시를 받지 않더라도 캔버스를 계속 진행하도록 할 수 있습니다.

3일차 푸시를 받지 못했더라도 모든 사용자가 6일차 이메일을 받도록 하려면 3일차 푸시에 대해 **진행 동작**을 **즉시 심화 오디언스**로 설정하면 됩니다.

3일차 푸시에 대해 **즉시 심화 오디언스** 진행 동작을 선택하면, Braze가 푸시를 보내려고 할 때 사용자가 진도 진행됩니다. 오디언스 옵션과 일치하지만 푸시를 통해 도달할 수 없는 사용자에게는 푸시가 전송되지 않지만 어쨌든 진행됩니다.

{% details 이전 캔버스 발전 동작 %}

진행 동작이 출시되기 전에는 사용자가 캔버스 구성요소에서 메시지를 받은 후 해당 구성요소를 통해 고급 사용자에게 고급 행동을 제공했습니다. 예를 들어 캔버스 구성 요소에 이메일과 푸시가 포함된 경우, 사용자는 Braze가 사용자에게 푸시 또는 이메일을 보낼 때까지 캔버스의 다음 단계로 진행하지 못합니다.

사용자가 푸시 또는 이메일을 받지 못하면 캔버스의 다음 단계로 진행하지 못합니다.

캔버스 인앱 메시지 베타 1라운드에 참여하지 않은 Braze 고객은 2019년 7월 30일 이전에 생성된 모든 캔버스 단계에 "메시지 전송" 진행 동작 옵션이 적용됩니다. 진행 동작이 릴리스되기 전에는 캔버스 단계에서 메시지를 보낼 때 사용자 진행이 발생했습니다.

캔버스 인앱 메시지 베타 1라운드에 참여했던 Braze 고객은 2019년 7월 30일 이전에 생성된 인앱 메시지가 없는 모든 캔버스 단계에 "메시지 전송" 진행 동작 옵션이 적용되며, 2019년 7월 30일 이전에 생성된 인앱 메시지가 있는 모든 캔버스 단계에는 "지연 후 심화 오디언스" 옵션이 적용됩니다. 진행 동작이 출시되기 전에는 캔버스 인앱 메시지가 라이브 상태가 되면 사용자 승급이 이루어졌습니다.

{% enddetails %}


---
nav_title: 모범 사례
article_title: 캔버스 모범 사례
page_order: 1
description: "이 문서에서는 캔버스와 캔버스 플로우를 사용하여 고객 여정을 만들고 커스텀하는 몇 가지 모범 사례를 제공합니다."
tool: Canvas

---

# 캔버스 모범 사례

> 이 문서에서는 캔버스와 캔버스 플로우를 사용하여 고객 여정을 만들고 커스텀하는 몇 가지 모범 사례를 제공합니다.

## 목적 식별자 지정

무엇을, 누가, 왜 하는지에 대해 자세히 알아보세요!
- 사용자가 무엇을 달성할 수 있도록 지원하려고 하나요?
- 도달하려는 사용자는 누구인가요?
- 이 캔버스를 구축하는 이유는 무엇인가요?

## 믹스 앤 매치

[캔버스 구성 요소로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) 사용자 여정의 새로운 조합을 실현하세요.
- [결정 분할을]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) 통해 사용자를 분할하고 다양한 워크플로를 구축하세요.
- [지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) 단계로 사용자 여정에 간격을 두세요.
- 캔버스 흐름의 원하는 위치에 [독립형 메시지를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 추가하세요. 

## 더욱 풍부한 메시지 만들기

더욱 풍부한 메시지로 사용자의 마음을 사로잡으세요.

- 온보딩 캔버스를 위한 [인앱 메시지를]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) 구축하여 첫인상을 최대한 활용하세요.
- 프로모션 혜택과 푸시 알림을 위해 캔버스 여정에 [콘텐츠 카드를]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) 도입하세요.

## 사용자 여정 테스트하기

대조군을 통합하여 캔버스 메시징의 영향을 파악하세요. 이렇게 하면 캔버스가 어떻게 수신되었는지에 대한 이해를 구축할 수 있습니다!

- 사용자 여정을 식별할 수 있도록 캔버스의 각 단계에 이름을 지정하세요.
- 사용자 여정에서 [실험 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) 구성 요소를 활용하여 생성한 다양한 경로에 사용자를 무작위로 할당할 수 있습니다. 
- 지연 및 메시지 단계를 통해 사용자 여정을 다양화하여 가장 효과적인 경로를 파악할 수 있습니다.
- [캔버스 분석을]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) 통해 사용자 여정에서 각 구성 요소의 성능/성과를 확인할 수 있습니다.
- 처음 실행한 후 [캔버스를 편집합니다]({{site.baseurl}}/post-launch_edits/).

## 캔버스 예약하기

{% alert note %}
캔버스는 이미 시간이 지난 예약 전송을 사용할 수 없도록 합니다. 그러나 캠페인이 예약된 바로 그 순간(또는 그 전 몇 초)에 캔버스를 실행할 수 있습니다. 이로 인해 캔버스가 예정된 입력 시간을 놓치고 사용자가 캔버스에 입력하지 않을 수 있습니다. 예정된 전송 시간으로부터 몇 분 이내에 캠페인이 편집되는 경우 즉시 캔버스를 전송하는 것이 좋습니다.
{% endalert %}

캔버스 단계의 경우 캔버스를 예약할 때 다음 세부 사항을 고려하세요:

- 일정 변경은 아직 단계를 받기 위해 대기하고 있지 않은 사용자에게만 적용됩니다.
- 단계를 받기를 기다리지 않는 사용자에게 변경 사항이 적용되도록 예약하지 않는 한, 오디언스 변경 사항은 기본적으로 모든 사용자에게 적용됩니다.
- 배포되는 즉시 전송되도록 예약된 캔버스를 편집하고 **업데이트를** 선택하면 기본적으로 전송됩니다.

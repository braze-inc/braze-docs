---
nav_title: 예외 이벤트 
article_title: 예외 이벤트
page_order: 4
page_type: reference
description: "이 참조 문서에서는 예외 이벤트 및 캔버스 구성 요소에 미치는 영향을 설명합니다."
tool: Canvas

---

# 캔버스 예외 이벤트

{% alert important %}
2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 문서는 원래 캔버스 워크플로우에 대한 예외 이벤트를 설정할 때 참조할 수 있습니다. <br><br> Braze에서는 기존 캔버스 환경을 사용하는 고객은 캔버스 플로우로 전환할 것을 권장합니다. 향상된 편집 경험을 통해 캔버스를 더 잘 구축하고 관리할 수 있습니다. [캔버스를 캔버스 플로우에 복제하는 방법]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)에 대해 자세히 알아보세요.
{% endalert %}

> 캔버스의 원래 캔버스 편집기를 사용하여 구성 요소를 예약할 때 예외 이벤트를 설정할 수 있습니다. 구성 요소에 예외 이벤트를 추가할 수 있지만 오디언스가 즉시 고급되지 않는 한 가능합니다. 예외 이벤트를 수행하는 사용자는 단계][2]를 진행하지 않으며 캔버스 오디언스에서 제외됩니다.

예외 이벤트는 사용자가 관련된 캔버스 구성 요소를 받기 위해 기다리는 동안에만 트리거됩니다. 사용자가 이전 캔버스 단계에서 동일한 작업을 수행하면 예외 이벤트가 트리거되지 않습니다.

{% alert important %}
캔버스 플로우의 경우 예외 이벤트는 [액션 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)를 사용하여만 구성됩니다. 예를 들어, 행동 경로를 정의하고 예외로 모든 사람 경로를 사용할 수 있습니다.
{% endalert %}

액션 기반 단계의 예외 이벤트는 단계 지연 또는 창 동안 작동합니다. 예약된 단계에는 창이 없으므로 지연 중에 발생하는 경우에만 예외 이벤트가 작동합니다.

예를 들어, 캔버스의 세 번째 단계에서 "유기한 장바구니"에 대한 예외 이벤트가 있지만 사용자가 두 번째 단계에서 장바구니를 포기하면 예외 이벤트가 트리거되지 않습니다. 이 예제에서 예외 이벤트는 사용자가 캔버스의 세 번째 단계에서 장바구니를 포기할 때만 트리거됩니다. 

![][1]


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/

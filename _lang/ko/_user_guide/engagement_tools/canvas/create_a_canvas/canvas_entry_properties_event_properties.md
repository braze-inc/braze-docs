---
nav_title: 캔버스 항목 속성 및 이벤트 속성
article_title: 캔버스 항목 속성 및 이벤트 속성
page_order: 4.2
page_type: reference
description: "이 참고 문서에서는 캔버스 항목 속성과 이벤트 속성정보의 차이점과 각 속성을 언제 사용해야 하는지 설명합니다."
tool: Canvas
---

# 캔버스 항목 속성 및 이벤트 속성

> 이 참조 문서에서는 각 속성의 사용 시기 및 동작의 차이점을 포함하여 `canvas_entry_properties` 및 `event_properties`에 대한 정보를 다룹니다. <br><br> 커스텀 이벤트 속성정보 일반에 대한 자세한 내용은 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)에서 확인하세요.

{% alert important %}
[컨텍스트 구성 요소 얼리 액세스에]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) 참여하는 경우 캔버스 항목 속성은 캔버스 컨텍스트 변수의 일부입니다. 즉, `canvas_entry_properties` 은 이제 `context` 으로 참조됩니다. 각 `context` 변수에는 이름, 데이터 유형, Liquid를 포함할 수 있는 값이 포함됩니다.
{% endalert %}

캔버스 항목 속성과 이벤트 속성정보는 캔버스 워크플로 내에서 서로 다르게 작동합니다. 사용자의 캔버스 입력을 트리거하는 이벤트 또는 API 호출의 속성을 `canvas_entry_properties`라고 합니다. 사용자가 캔버스 여정을 진행하면서 발생하는 이벤트의 속성정보를 `event_properties`라고 합니다. 주요 차이점은 `canvas_entry_properties` 은 API 트리거 캔버스에서 항목 페이로드의 속성에도 액세스하여 이벤트 그 이상의 것에 초점을 맞춘다는 점입니다.

캔버스 항목 속성과 이벤트 속성 간의 차이점을 요약한 표는 다음 표를 참조하세요.

| | 캔버스 진입 등록정보 | 이벤트 등록정보
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **지속성** | 캔버스 플로우를 사용하여 만든 캔버스의 기간 동안 모든 [메시지][1] 단계에서 참조할 수 있습니다. | \- 한 번만 참조할 수 있습니다. <br> \- 후속 메시지 단계에서 참조할 수 없습니다. |
| **원본 캔버스 동작** | \- 영구 항목 속성이 켜져 있어야 합니다. <br> \- 캔버스의 첫 번째 전체 단계에서만 `canvas_entry_properties`를 참조할 수 있습니다. 캔버스는 액션 기반 또는 API 트리거형이어야 합니다. | \- 캔버스에서 실행 기반 전달을 사용하는 모든 단계에서 `event_properties`를 참조할 수 있습니다. <br> \- 실행 기반 캔버스의 첫 번째 전체 단계 이외의 예약된 전체 단계에서는 사용할 수 없습니다. 그러나 사용자가 [캔버스 구성요소][2]를 사용하는 경우 동작은 `event_properties`에 대한 캔버스 흐름 규칙을 따릅니다. |
| **캔버스 흐름 동작** | 캔버스의 모든 단계에서 `canvas_entry_properties` 을 참조할 수 있습니다. 출시 후 동작에 대해서는 [출시 후 캔버스 편집을]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties) 참조하세요. | \- 커스텀 이벤트 또는 구매 이벤트가 수행되는 [작업 경로][3] 단계 **뒤의** 첫 번째 메시지 단계에서 `event_properties`를 참조할 수 있습니다. <br> \- 작업 경로 단계의 다른 모든 사람 경로 뒤에 있을 수 없습니다. <br> \- 액션 경로와 메시지 단계 사이에 메시지 캔버스가 아닌 다른 구성 요소를 넣을 수 있습니다. 이러한 메시지 이외의 구성 요소 중 하나가 작업 경로 단계인 경우 사용자는 해당 작업 경로의 다른 모든 사람 경로를 통해 이동할 수 있습니다. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details 오리지널 캔버스 편집기 세부 정보 %}
2023년 2월 28일부터 더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 문서는 원래 캔버스 워크플로에 대해 `canvas_entry_properties` 및 `event_properties`를 사용할 때 참조할 수 있습니다.

원래 캔버스 편집기 및 캔버스 흐름의 경우 리드 메시지 단계에서 `event_properties`를 사용할 수 없습니다. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **앞에** 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다.
{% enddetails %}

### 알아두어야 할 사항

- 캔버스 항목 프로퍼티는 Liquid에서만 참조할 수 있습니다. To filter on the properties within the Canvas, use [event property segmentation]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) instead.
- 인앱 메시지 채널의 경우 `canvas_entry_properties` 은 캔버스에서만 참조할 수 있으며, `event_properties` 은 인앱 메시지 채널에 사용할 수 없습니다.
- 리드 메시지 단계에서는 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **앞에** 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다. 
- 행동 경로 단계에 "SMS 인바운드 메시지 보내기" 또는 "WhatsApp 인바운드 메시지 보내기" 트리거가 포함된 경우 후속 캔버스 단계에 SMS 또는 WhatsApp Liquid 속성정보를 포함할 수 있습니다. 이는 캔버스에서 이벤트 프로퍼티가 작동하는 방식을 반영합니다. 이렇게 하면 메시지를 활용하여 고객 프로필 및 대화 메시지에 대한 퍼스트파티 데이터를 저장하고 참조할 수 있습니다.

### 이벤트 속성에 대한 타임스탬프

캔버스에서 `event_properties` 를 사용하는 경우 타임스탬프는 아래에 자세히 설명된 몇 가지 예외를 제외하고 UTC로 정규화됩니다. 이러한 동작을 고려할 때, Braze는 다음 예시와 같은 Liquid 시간대 필터를 사용하여 [원하는 시간대로]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) 메시지가 전송되도록 할 것을 강력히 권장합니다.

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### 예외

- 캔버스의 첫 번째 단계가 메시지 단계인 경우 타임스탬프는 UTC로 정규화되지 않습니다.
- 캔버스에서의 순서와 관계없이 인앱 메시지 채널을 사용하는 메시지 단계에서는 타임스탬프가 UTC로 정규화되지 않습니다.

## 사용 사례

![작업 경로 단계와 위시리스트에 항목을 추가한 사용자를 위한 지연 단계 및 메시지 단계, 그 외 모든 사용자를 위한 경로가 뒤따릅니다.][7]{: style="float:right;max-width:30%;margin-left:15px;"}

`canvas_entry_properties` 와 `event_properties` 의 차이점을 더 자세히 이해하기 위해 사용자가 "위시리스트에 항목 추가" 사용자 지정 이벤트를 수행하면 액션 기반 캔버스에 들어가는 이 시나리오를 고려해 보겠습니다. 

`canvas_entry_properties`는 캔버스 생성의 [입력 일정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) 단계에서 구성되며 사용자가 캔버스에 입력하는 시점에 해당합니다. 캔버스 플로우는 영구 항목 속성을 지원하므로 이러한 `canvas_entry_properties`는 캔버스 플로우의 모든 메시지 단계에서도 참조할 수 있습니다. 

이 캔버스에는 사용자가 위시리스트에 항목을 추가했는지 확인하는 작업 경로 단계로 시작되는 사용자 여정이 있습니다. 여기에서 사용자가 아이템을 추가한 경우 메시지 단계에서 "위시리스트에 새 아이템이 추가되었습니다!"라는 메시지가 표시되기까지 지연이 발생합니다. 

사용자 여정의 첫 번째 메시지 단계에서는 작업 경로 단계에서 커스텀 `event_properties`에 액세스할 수 있습니다. 이 경우 이 메시지 단계에 ``{% raw %} {{event_properties.${property_name}}} {% endraw %}``를 메시지 콘텐츠의 일부로 포함할 수 있습니다. 사용자가 위시리스트에 항목을 추가하지 않으면 다른 모든 사람 경로를 거치게 되므로 `event_properties`를 참조할 수 없으며 잘못된 설정 오류가 반영됩니다.

메시지 단계가 행동 경로 단계에서 모든 사람이 아닌 경로로 추적할 수 있는 경우에만 `event_properties`에 액세스할 수 있습니다. 메시지 단계가 다른 모든 사람 경로에 연결되어 있지만 사용자 여정에서 작업 경로 단계로 거슬러 올라갈 수 있는 경우에도 `event_properties`에 액세스할 수 있습니다. 이러한 동작에 대한 자세한 내용은 [메시지 단계][8]를 참조하세요.

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/
[7]: {% image_buster /assets/img_archive/canvas_entry_properties1.png %}
[8]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/

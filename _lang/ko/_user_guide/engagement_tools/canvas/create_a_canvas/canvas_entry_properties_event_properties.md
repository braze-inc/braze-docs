---
nav_title: 캔버스 항목 속성 및 이벤트 속성정보
article_title: 캔버스 항목 속성 및 이벤트 속성정보
page_order: 4.2
page_type: reference
description: "이 참고 문서에서는 캔버스 항목 속성과 이벤트 속성정보의 차이점과 각 속성의 사용 시기를 설명합니다."
tool: Canvas
---

# 캔버스 항목 속성 및 이벤트 속성정보

> 이 참조 문서에서는 각 속성의 사용 시기 및 동작의 차이점을 포함하여 `canvas_entry_properties` 및 `event_properties` 에 대한 정보를 다룹니다. <br><br> 커스텀 이벤트 속성정보 전반에 대한 자세한 내용은 [커스텀 이벤트 속성을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) 참조하세요.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

캔버스 항목 속성정보와 이벤트 속성정보는 캔버스 워크플로 내에서 서로 다른 방식으로 작동합니다. 사용자의 캔버스 진입을 트리거하는 이벤트 또는 API 호출의 속성정보는 `canvas_entry_properties` 로 알려져 있습니다. 사용자가 캔버스 여정을 이동하면서 발생하는 이벤트의 속성정보를 `event_properties` 이라고 합니다. 주요 차이점은 `canvas_entry_properties` API 트리거 캔버스에서 엔트리 페이로드의 속성정보에도 액세스하여 이벤트 그 이상의 것에 집중한다는 점입니다.

캔버스 항목 속성과 이벤트 속성정보의 차이점을 요약한 표는 다음 표를 참조하세요.

| | 캔버스 항목 속성 | 이벤트 속성정보
|----|----|----|
| **Liquid** | `canvas_entry_properties` | `event_properties` |
| **지속성** | 캔버스를 사용하여 구축된 캔버스 기간 동안 모든 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 단계에서 참조할 수 있습니다. | \- 한 번만 참조할 수 있습니다. <br> \- 후속 메시지 단계에서 참조할 수 없습니다. |
| **캔버스 동작** | 캔버스의 모든 단계에서 `canvas_entry_properties` 을 참조할 수 있습니다. 출시 후 동작에 대해서는 [출시 후 캔버스 편집을]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties) 참조하세요. | - [행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 단계 **후** 첫 번째 메시지 단계에서 커스텀 이벤트 또는 구매 이벤트가 수행되는 경우 `event_properties` 을 참조할 수 있습니다. <br> \- 행동 경로 단계의 다른 모든 사람 경로 뒤에 있을 수 없습니다. <br> \- 행동 경로와 메시지 단계 사이에 메시징이 아닌 다른 구성 요소를 포함할 수 있습니다. 이러한 메시지 이외의 구성 요소 중 하나가 행동 경로 단계인 경우 사용자는 해당 행동 경로의 다른 모든 사람 경로를 통해 이동할 수 있습니다. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

더 이상 원본 편집기를 사용하여 캔버스를 만들거나 복제할 수 없습니다. 이 문서는 이전 캔버스 워크플로에서 캔버스 항목 속성 및 이벤트 속성을 사용할 때 참고할 수 있습니다.

**캔버스 항목 속성:**
- 지속성 항목 속성정보가 켜져 있어야 합니다. 
- 캔버스의 첫 번째 전체 단계에서 `canvas_entry_properties` 만 참조할 수 있습니다. 캔버스는 액션 기반이거나 API 트리거 동작이어야 합니다.

**항목 속성:**
- 캔버스에서 실행 기반 전달을 사용하는 모든 단계에서 `event_properties` 을 참조할 수 있습니다.
- 액션 기반 캔버스의 첫 번째 전체 단계 이외의 예약된 전체 단계에서는 사용할 수 없습니다. 그러나 사용자가 [캔버스 컴포넌트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) 사용하는 경우 동작은 `event_properties` 에 대한 현재 캔버스 워크플로 규칙을 따릅니다.

**이벤트 속성정보:**
- 리드 메시지 단계에서 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties` 을 사용하거나 `event_properties` 을 포함하는 메시지 단계 **앞에** 해당 이벤트가 있는 행동 경로 단계를 추가해야 합니다.

{% enddetails %}

### 알아두어야 할 사항

- 캔버스 항목 속성은 Liquid에서만 참조할 수 있습니다. 캔버스 내의 속성을 필터링하려면 [이벤트 속성 세분화를]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) 대신 사용하세요.
- 인앱 메시지 채널의 경우 `canvas_entry_properties` 은 캔버스에서만 참조할 수 있으며 `event_properties` 은 인앱 메시지 채널에 사용할 수 없습니다.
- 리드 메시지 단계에서는 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties` 을 사용하거나 `event_properties` 을 포함하는 메시지 단계 **앞에** 해당 이벤트가 있는 행동 경로 단계를 추가해야 합니다. 
- 행동 경로 단계에 "SMS 인바운드 메시지 전송" 또는 "WhatsApp 인바운드 메시지 전송" 트리거가 포함된 경우 후속 캔버스 단계에 SMS 또는 WhatsApp Liquid 프로퍼티가 포함될 수 있습니다. 이는 캔버스에서 이벤트 속성정보가 작동하는 방식을 반영합니다. 이렇게 하면 메시지를 활용하여 사용자 프로필 및 대화 메시징의 퍼스트파티 데이터를 저장하고 참조할 수 있습니다.

### 이벤트 속성정보에 대한 타임스탬프

액션 기반 캔버스의 [트리거 이벤트 속성정보에서]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) [날짜/시간 유형의]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) 타임스탬프를 사용하는 경우, 타임스탬프는 UTC로 정규화됩니다. 일부 예외 사항은 아래에 자세히 설명되어 있습니다.

이러한 동작을 고려할 때, Braze는 다음 예시와 같은 Liquid 시간대 필터를 사용하여 메시징이 [원하는 시간대로]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) 전송되도록 할 것을 강력히 권장합니다.

{% raw %}
```liquid
{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }
```
{% endraw %}

#### 예외

- 캔버스 단계가 메시지 단계인 경우 타임스탬프는 첫 번째 단계에서 UTC로 정규화되지 않습니다.
- 타임스탬프는 캔버스에서의 순서와 관계없이 인앱 메시지 채널을 사용하는 모든 메시지 단계에서 UTC로 정규화되지 않습니다.

## 사용 사례

위시리스트에 항목을 추가한 사용자를 위한 지연 단계와 메시지 단계, 그 외 모든 사용자를 위한 행동 경로 단계가 이어집니다.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

`canvas_entry_properties` 와 `event_properties` 의 차이점을 더 이해하기 위해 사용자가 "위시리스트에 항목 추가" 커스텀 이벤트를 수행하면 액션 기반 캔버스에 들어가는 이 시나리오를 고려해 보겠습니다. 

`canvas_entry_properties` 은 캔버스 생성의 [참가 일정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) 단계에서 구성되며 사용자가 캔버스에 참가할 때 해당됩니다. 이러한 `canvas_entry_properties` 은 모든 메시지 단계에서도 참조할 수 있습니다.

이 캔버스에는 사용자가 위시리스트에 항목을 추가했는지 확인하는 행동 경로 단계로 시작되는 사용자 여정이 있습니다. 여기에서 사용자가 아이템을 추가한 경우 메시지 단계에서 "위시리스트에 새 아이템이 추가되었습니다!"라는 메시지가 표시되기까지 잠시 지연됩니다. 

고객 여정의 첫 번째 메시지 단계는 행동 경로 단계에서 커스텀 `event_properties` 에 액세스할 수 있습니다. 이 경우 이 메시지 단계에 ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` 을 메시지 콘텐츠의 일부로 포함할 수 있습니다. 사용자가 위시리스트에 항목을 추가하지 않으면 다른 모든 사람 경로를 거치게 되므로 `event_properties` 을 참조할 수 없으며 잘못된 설정 오류가 반영됩니다.

메시지 단계가 행동 경로 단계에서 모든 사람이 아닌 경로로 추적할 수 있는 경우에만 `event_properties` 에 액세스할 수 있습니다. 메시지 단계가 다른 모든 사람 경로에 연결되어 있지만 사용자 여정에서 행동 경로 단계로 거슬러 올라갈 수 있는 경우에도 `event_properties` 에 액세스할 수 있습니다. 이러한 동작에 대한 자세한 내용은 [메시지 단계를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 참조하세요.


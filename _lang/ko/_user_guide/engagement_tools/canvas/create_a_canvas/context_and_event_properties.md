---
nav_title: 컨텍스트 및 이벤트 속성
article_title: 컨텍스트 및 이벤트 속성
page_order: 4.2
page_type: reference
description: "이 참조 문서에서는 컨텍스트 속성과 이벤트 속성의 차이점과 각 속성을 사용할 때를 설명합니다."
tool: Canvas
---

# 컨텍스트 및 이벤트 속성

> 이 참조 문서에서는 각 속성의 사용 시기 및 동작의 차이점을 포함하여 `context` 및 `event_properties`에 대한 정보를 다룹니다. <br><br> 커스텀 이벤트 속성정보 일반에 대한 자세한 내용은 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)에서 확인하세요.

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

컨텍스트 속성과 이벤트 속성은 Canvas 워크플로 내에서 다르게 작동합니다. 사용자의 캔버스 입력을 트리거하는 이벤트 또는 API 호출의 속성을 `context`라고 합니다. 사용자가 Canvas 여정 내에서 이동할 때 발생하는 이벤트의 속성을 `event_properties`라고 합니다. 주요 차이점은 `context` 은 API 트리거 캔버스에서 항목 페이로드의 속성에도 액세스하여 이벤트 그 이상의 것에 초점을 맞춘다는 점입니다.

컨텍스트 속성과 이벤트 속성 간의 차이를 요약한 표를 참조하십시오.

| | 컨텍스트 속성 | 이벤트 등록정보 |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **지속성** | Canvas를 사용하여 구축된 Canvas의 모든 [메시지]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) 단계에서 참조할 수 있습니다. | \- 한 번만 참조할 수 있습니다. <br> \- 후속 메시지 단계에서 참조할 수 없습니다. |
| **캔버스 동작** | 캔버스의 모든 단계에서 `context` 을 참조할 수 있습니다. 출시 후 동작에 대해서는 [출시 후 캔버스 편집을]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-entry-properties) 참조하세요. | \- 커스텀 이벤트 또는 구매 이벤트가 수행되는 [작업 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 단계 **뒤의** 첫 번째 메시지 단계에서 `event_properties`를 참조할 수 있습니다. <br> \- 작업 경로 단계의 다른 모든 사람 경로 뒤에 있을 수 없습니다. <br> \- 액션 경로와 메시지 단계 사이에 메시지 이외의 다른 구성 요소를 포함할 수 있습니다. 이러한 메시지 이외의 구성 요소 중 하나가 작업 경로 단계인 경우 사용자는 해당 작업 경로의 다른 모든 사람 경로를 통해 이동할 수 있습니다. | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% details Original Canvas editor details %}

You can no longer create or duplicate Canvases using the original editor. Canvas 컨텍스트는 원래 Canvas 편집기에서 지원되지 않으므로 이 섹션은 이전 Canvas 워크플로에 대한 Canvas 진입 속성과 이벤트 속성을 사용할 때 참조용으로 제공됩니다.

**캔버스 항목 속성:**
- 영구 항목 속성이 켜져 있어야 합니다. 
- 캔버스의 첫 번째 전체 단계에서만 `canvas_entry_properties` 을 참조할 수 있습니다. 캔버스는 액션 기반 또는 API 트리거형이어야 합니다.

**항목 속성:**
- 캔버스에서 액션 기반 전달을 사용하는 모든 단계에서 `event_properties` 을 참조할 수 있습니다.
- 액션 기반 캔버스의 첫 번째 전체 단계 이외의 예약된 전체 단계에서는 사용할 수 없습니다. 그러나 사용자가 [Canvas 구성 요소]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)를 사용하는 경우, 동작은 `event_properties`에 대한 현재 Canvas 워크플로 규칙을 따릅니다.

**이벤트 속성:**
- 리드 메시지 단계에서 `event_properties` 을 사용할 수 없습니다. 대신 `canvas_entry_properties`를 사용하거나 `event_properties`를 포함하는 메시지 단계 **앞에** 해당 이벤트가 포함된 작업 경로 단계를 추가해야 합니다.

{% enddetails %}

### 알아두어야 할 사항

- 컨텍스트는 Liquid에서만 참조할 수 있습니다. To filter on the properties within the Canvas, use [event property segmentation]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/) instead.
- 인앱 메시지 채널의 경우, Canvas에서 `context` 및 `event_properties`를 참조할 수 있습니다. `event_properties`는 트리거 기반이기 때문에 첫 번째 Canvas 단계에 포함될 때 접근할 수 있습니다.
- You can't use `event_properties` in the lead Message step. 대신 `context`를 사용하거나 메시지 단계에 `event_properties`를 포함하는 해당 이벤트 **이전**의 Action Paths 단계를 추가할 수 있습니다.
- 행동 경로 단계에 "SMS 인바운드 메시지 보내기" 또는 "WhatsApp 인바운드 메시지 보내기" 트리거가 포함된 경우 후속 캔버스 단계에 SMS 또는 WhatsApp Liquid 속성정보를 포함할 수 있습니다. 이는 캔버스에서 이벤트 프로퍼티가 작동하는 방식을 반영합니다. 이렇게 하면 메시지를 활용하여 고객 프로필 및 대화 메시지에 대한 퍼스트파티 데이터를 저장하고 참조할 수 있습니다.

{% alert note %}
오디언스 적격성은 Canvas 진입 시 한 번 평가됩니다. 사용자가 진입 중에 병합되면, 식별된 사용자는 Canvas를 통해 계속 진행하며 Canvas 세그먼트 기준에 대해 다시 평가되지 않습니다.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### 트리거의 타임스탬프

이벤트에서 동작 기반 Canvas를 트리거하는 [날짜 시간 유형]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties)과 함께 타임스탬프를 사용하는 경우, 타임스탬프는 UTC로 정규화됩니다.

이러한 동작을 고려할 때, Braze는 다음 예시와 같은 Liquid 시간대 필터를 사용하여 [원하는 시간대로]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#time-zone-filter) 메시지가 전송되도록 할 것을 강력히 권장합니다.

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

#### 예외

- 캔버스의 첫 번째 단계가 메시지 단계인 경우 타임스탬프는 UTC로 정규화되지 않습니다.
- 캔버스에서의 순서와 관계없이 인앱 메시지 채널을 사용하는 메시지 단계에서는 타임스탬프가 UTC로 정규화되지 않습니다.

## Use case

![위시리스트에 항목을 추가한 사용자에 대한 지연 단계와 메시지 단계가 뒤따르는 Action Path 단계, 그리고 다른 모든 사용자에 대한 경로입니다.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

`context` 및 `event_properties`의 차이를 더 잘 이해하기 위해, 사용자가 "위시리스트에 항목 추가"라는 사용자 정의 이벤트를 수행할 경우 동작 기반 Canvas에 진입하는 시나리오를 고려해 보겠습니다. 

컨텍스트는 Canvas를 생성할 때 [진입 일정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#step-2b-set-your-canvas-entry-schedule) 단계에서 구성되며 사용자가 Canvas에 진입할 때와 관련이 있습니다. 컨텍스트는 모든 메시지 단계에서 참조될 수 있습니다.

이 캔버스에는 사용자가 위시리스트에 항목을 추가했는지 확인하는 작업 경로 단계로 시작되는 사용자 여정이 있습니다. 여기서 사용자가 항목을 추가하면, 메시지 단계에서 "위시리스트에 새 항목이 추가되었습니다!"라는 메시지를 받기 전에 지연을 경험합니다. 

사용자 여정의 첫 번째 메시지 단계는 작업 경로 단계에서 사용자 정의 `event_properties`에 접근할 수 있습니다. 이 경우 이 메시지 단계에 ``{% raw %} {{event_properties.${property_name}}} {% endraw %}``를 메시지 콘텐츠의 일부로 포함할 수 있습니다. 사용자가 위시리스트에 항목을 추가하지 않으면, 그들은 모두 다른 경로를 거치게 되며, 이는 `event_properties`을 참조할 수 없고 잘못된 설정 오류를 반영합니다.

메시지 단계가 행동 경로 단계에서 모든 사람이 아닌 경로로 추적할 수 있는 경우에만 `event_properties`에 액세스할 수 있습니다. 메시지 단계가 모두 다른 경로에 연결되어 있지만 사용자 여정의 작업 경로 단계로 추적할 수 있다면, 여전히 `event_properties`에 접근할 수 있습니다. 이러한 행동에 대한 자세한 정보는 [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)를 참조하십시오.


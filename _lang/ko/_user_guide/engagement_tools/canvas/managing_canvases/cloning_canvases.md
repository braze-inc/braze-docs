---
nav_title: 캔버스 복제
article_title: 캔버스 복제
page_order: 3
alias: "/cloning_canvases/"
description: "이 참조 문서에서는 원래 캔버스 편집기에서 캔버스 흐름 워크플로로 캔버스를 복제하는 방법을 설명합니다."
tool: Canvas
---

# 캔버스를 캔버스 흐름으로 복제

{% alert important %}
2023년 2월 28일부터는 더 이상 기존 캔버스 환경을 사용하여 캔버스를 만들거나 복제할 수 없습니다. Braze는 원래 캔버스 경험을 사용하는 고객이 캔버스 플로우로 이동할 것을 권장합니다.
{% endalert %}

> 원본 편집기에서 기존 캔버스가 있는 경우 이 캔버스를 복제하여 캔버스 플로우에 복사본을 만들 수 있습니다. By switching to the Canvas Flow workflow, you gain access to lightweight [Canvas components]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), [persistent entry properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/), and [post-launch editing]({{site.baseurl}}/post-launch_edits). 귀하의 원래 캔버스는 변경되거나 삭제되지 않습니다.

캔버스를 복제하려면 다음을 수행하세요.

1. 캔버스 대시보드로 이동하세요. 
2. 캔버스 흐름 워크플로우에서 복사할 캔버스를 식별합니다. 캔버스를 **초안**, **활성**, 또는 **중지됨** 상태로 복제할 수 있습니다. 
3. 클릭 <i class="fas fa-ellipsis-vertical"></i> **추가 작업** 및 **캔버스 흐름으로 복제**을 선택합니다.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. 새 캔버스의 이름을 입력하고 **캔버스 흐름으로 복제**을 클릭하십시오. 

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

이제 두 가지 버전의 캔버스가 있습니다: 원래 캔버스와 캔버스 플로우 버전입니다. 원래 캔버스는 여전히 원래 상태를 유지하고 있으며, 복제된 캔버스는 **초안** 상태입니다. 여전히 원래 캔버스에 접근할 수 있지만, Braze는 캔버스 플로우 워크플로우를 사용하여 캔버스를 계속 구축할 것을 권장합니다.

이전에 일부 브랜치가 있는 캔버스를 복제할 수 없었습니다. 이제 브랜치를 사용하여 캔버스를 복제할 수 있습니다. 캔버스를 브랜치와 함께 복제하면 연결이 끊긴 단계가 발생할 수 있습니다. 이 연결되지 않은 단계들(이전 단계와 연결되지 않은 단계들)을 해결하여 캔버스 여정이 제대로 매핑되었는지 확인하십시오.

{% alert note %}
활성 캔버스를 복제하면 Braze는 원래 캔버스를 통해 사용자에게 계속 전송됩니다. 캔버스를 복제하기 전에 캔버스를 중지하여 두 캔버스에서 사용자에게 중복 메시지를 보내지 않도록 하는 것이 좋습니다.
{% endalert %}

![캔버스 대시보드 with two 캔버스s listed: 캔버스 V1의 V2 사본 및 캔버스 V1. The V2 Copy of Canvas V1 has an icon that indicates it is using the Canvas Flow workflow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

캔버스 복제를 완료하여 캔버스 플로우 워크플로우에 넣었습니다. 이제 이 업데이트된 환경에서 캔버스를 계속 만들 수 있습니다!

## 추천

기존 사용자가 원래 캔버스를 캔버스 플로우로 복제한 후 사용자 여정을 계속할 수 있도록 기존 캔버스에 필터를 추가하여 새 사용자가 새 캔버스에 들어가지 못하도록 할 수 있습니다.

재자격이 꺼져 있으면 "캔버스 변형 입력됨" 필터를 추가하세요. 재자격이 활성화된 경우 사용자가 동일한 캔버스를 두 번 입력하지 않도록 하기 위해 고려할 수 있는 가능한 방법은 다음과 같습니다.
- 기존 캔버스를 업데이트하여 고유한 태그를 포함합니다. 새로운 캔버스의 경우 필터 "캠페인 또는 캔버스에서 태그가 있는 마지막 수신 메시지"를 추가합니다. 이것은 사용자가 특정 입력 날짜 이후에 두 번 캔버스에 들어가는 것을 방지합니다(원래 캔버스에서 마지막 메시지가 전송된 후 총 일수와 전환 창을 더한 값). 
- **다음 방법은 데이터 포인트를 소비할 것입니다.** 원래 캔버스를 업데이트하여 입장 시 커스텀 속성 날짜 타임스탬프를 트리거하는 Braze-to-Braze 웹훅을 포함합니다. 이 속성은 사용자가 지정된 날짜 이후에 새 캔버스에 들어가는 것을 방지하는 데 사용할 수 있습니다(원래 캔버스에서 마지막 메시지가 전송된 후 총 일수에 전환 창을 더한 값).

API로 트리거된 캔버스의 경우, 새로운 캔버스를 출시할 준비가 되었을 때 이러한 캔버스가 새로운 캔버스 ID를 사용하고 있는지 확인하기 위해 엔지니어링 팀과 조율하세요.

원래 캔버스 편집기와 캔버스 플로우 경험의 차이에 대한 자세한 내용은 [캔버스 FAQ]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor)를 확인하세요.



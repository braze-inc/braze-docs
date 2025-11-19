---
nav_title: 기능 플래그
article_title: 기능 플래그
page_order: 8
page_type: reference
description: "이 참조 문서에서는 캔버스에서 기능 플래그를 사용하는 방법에 대해 설명합니다."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# 기능 플래그

> 기능 플래그를 사용하면 새로운 기능에 대한 가설을 실험하고 확인할 수 있습니다. 마케터는 기능 플래그를 사용하여 [캔버스에서]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) 오디언스를 세분화하고 기능 출시가 전환에 미치는 영향을 추적할 수 있습니다. 또한 [실험 경로를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) 사용하면 다양한 메시지 또는 경로를 서로 테스트하고 가장 효과적인 경로를 결정하여 이러한 전환을 최적화할 수 있습니다. 더 많은 오디언스에게 기능을 점진적으로 출시할 때 오디언스 경로를 사용하세요.

기능 플래그와 Braze에서 기능 플래그를 사용하는 방법에 대해 자세히 알아보고 싶으신가요? [기능 플래그]({{site.baseurl}}/developer_guide/feature_flags/) 전용 문서를 확인하세요.

## 기능 플래그 만들기

실시간 채팅 버튼 기능에 대한 기능 플래그 단계 예시입니다.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

기능 플래그 컴포넌트를 만들려면 먼저 캔버스에 단계를 추가합니다. 사이드바에서 컴포넌트를 드래그 앤 드롭하거나 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 클릭하고 **기능 플래그를** 선택합니다. 그런 다음 드롭다운에서 보관되지 않은 기능 플래그가 포함된 기능 플래그를 선택합니다.

## 이 단계의 작동 방식

캔버스가 중지되거나 보관되거나 단계가 제거되면 해당 단계를 통과한 모든 사용자는 더 이상 해당 단계의 기능 플래그와 해당 속성을 받지 못합니다. 사용자는 여전히 해당 기능 플래그 및 아직 활성화되어 있을 수 있는 다른 캔버스에 대한 기본값 롤아웃 비율 및 오디언스 세그먼트의 적용을 받습니다.

캔버스 단계의 속성은 실행 후, 심지어 사용자가 단계를 통과한 후에도 변경할 수 있습니다. 사용자는 이전에 저장된 이전 버전 대신 항상 실시간 동적 버전의 기능 플래그를 받게 됩니다.

## 속성 덮어쓰기

기능 플래그를 만들 때 기본값 속성을 지정합니다. 기능 플래그 캔버스 단계를 설정할 때 기본값을 유지하거나 이 단계를 입력한 사용자의 값을 덮어쓸 수 있습니다.

기능 플래그 "기본 설정 센터"에 "문자열"을 속성으로, "URL"을 속성 키로, 값을 입력합니다.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

**메시징** > **기능 플래그로** 이동하여 추가 속성을 편집, 추가 또는 제거합니다.

## 캔버스와 롤아웃의 차이점

캔버스와 기능 플래그 롤아웃(슬라이더 드래그)은 서로 독립적으로 작동할 수 있습니다. 중요한 주의 사항은 캔버스 단계를 입력하면 기본값 롤아웃 구성을 덮어쓴다는 점입니다. 즉, 사용자가 기능 플래그를 사용할 자격이 없는 경우 캔버스 단계에서 해당 사용자에게 해당 기능을 인에이블먼트할 수 있습니다.

마찬가지로 사용자가 특정 속성을 가진 기능 플래그 롤아웃 자격이 있는 경우 캔버스 단계에도 들어가면 해당 캔버스 단계의 덮어쓴 값을 받게 됩니다.


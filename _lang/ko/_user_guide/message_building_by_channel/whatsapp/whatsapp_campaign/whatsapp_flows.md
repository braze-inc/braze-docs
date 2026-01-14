---
nav_title: WhatsApp 흐름
article_title: WhatsApp 흐름
page_order: 1
description: "이 참고 문서에서는 WhatsApp 플로우 메시지를 구축하고 생성하는 단계에 대해 설명합니다."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp 흐름

> WhatsApp 플로우는 기존 WhatsApp 채널을 개선한 기능으로, 대화형 및 동적 메시징 경험을 만들 수 있습니다. 이 페이지에서는 미리 맛보기 프로그램에 참여하고 WhatsApp 흐름을 사용하기 위한 단계별 지침을 제공합니다.

## WhatsApp 플로우 설정하기

1. 메타 계정에 로그인합니다.
2. 두 가지 주요 위치 중 하나에서 플로우를 만듭니다:
    - **계정 도구:** **플로우** 탭으로 이동하여 플로우 ID를 확인하고 새 플로우를 만듭니다.
    - **템플릿을 관리합니다:** 이 방법은 플로우를 만드는 데 권장되는 방법입니다. 여기에서 템플릿을 생성하고 템플릿 생성 과정에서 플로우 옵션을 선택할 수 있습니다.

플로우 템플릿을 만들 수 있는 페이지가 있는 WhatsApp 매니저.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. 기존 플로우를 선택하거나 새로 만듭니다. 플로우를 만드는 경우 두 가지 옵션 중에서 선택합니다:
  - **커스텀 양식:** 특정 요구 사항의 경우
  - **미리 디자인된 요소:** 더 빠른 설정을 위해

## WhatsApp Flow 메시지 및 응답 구성하기

{% tabs local %}
{% tab Template message %}

1. Braze 캔버스에서 해당 플로우가 포함된 템플릿 메시지를 사용하는 WhatsApp 메시지 단계를 만듭니다.
2. 템플릿 생성을 계속합니다. 필요한 경우 메시징에 미디어, 가변 콘텐츠 또는 둘 다를 추가합니다. 템플릿을 만들 때 플로우를 선택했으므로 플로우 경험에 대한 추가 정보는 필요하지 않습니다.

\![WhatsApp 플로우 템플릿을 사용하는 WhatsApp 메시지 작성기.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Braze 캔버스에서 응답 메시지와 플로우 메시지를 사용하는 WhatsApp 메시지 단계를 만듭니다.

WhatsApp 응답 메시지 유형 및 플로우 메시지 레이아웃에 대한 메시지 단계입니다.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. 해당 플로우를 선택한 다음 메시지 작성을 계속합니다. 

플로우를 선택하기 위한 확장된 드롭다운이 있는 플로우 메시지 응답 작성기입니다.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### 미리보기 흐름

흐름이 있는 캔버스를 시작하기 전에 흐름 **미리** 보기를 선택하여 Braze에서 바로 흐름을 미리 보고 예상대로 작동하는지 확인할 수 있습니다. 또한 미리보기에서 플로우와 상호 작용하여 사용자가 플로우를 탐색하는 방식을 경험한 다음 실시간으로 조정할 수 있습니다. 플로우에 여러 페이지가 포함되어 있는 경우 각 페이지와 상호 작용할 수 있습니다.

\![사용자가 가입을 완료할 수 있는 양식을 표시하는 미리보기 창입니다.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## 전체 흐름 응답 저장하기 {#full-flow}

### 1단계: 행동 경로 만들기

[행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 캔버스 단계 또는 행동 기반 캠페인을 만듭니다. **WhatsApp 인바운드 메시지 보내기** 트리거 및 **흐름에 응답** 조건을 선택한 다음 관련 흐름 또는 **모든 흐름을** 선택합니다.

인바운드 WhatsApp 메시지를 보내고 모든 플로우에 응답한 사용자에 대한 트리거입니다.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### 2단계: WhatsApp 메시지 작성하기

WhatsApp 메시지를 작성할 때 더하기 아이콘을 선택하여 **개인화 추가** 창을 연 다음, 개인화 유형에 대해 **WhatsApp 속성을** 선택하고 사용자 지정 속성에 대해 **inbound_flow_response** 을 선택하고 커스텀 속성을 선택합니다. 이렇게 하면 정보를 고객 프로필에 저장하거나 웹훅과 같은 다른 서비스로 전달할 수 있습니다.

\![커스텀 속성을 사용하여 WhatsApp 속성 개인화를 삽입하기 위해 "개인화 추가" 구성요소가 있는 WhatsApp 메시지 작성기 `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:60%;"}

### 3단계: 전체 흐름 응답 저장하기

고급 JSON 편집기를 사용하여 플로우 응답의 속성을 커스텀 속성에 저장하거나 다단계 캔버스를 사용하여 응답을 중첩된 고객 속성에 저장할 수 있습니다. 

{% tabs %}
{% tab Advanced JSON editor %}

진행형 JSON 편집기에서 {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %} 을 입력합니다. 여기서 “flow_1” 은 플로우를 저장할 커스텀 속성입니다.

고급 JSON 편집기로 사용자 업데이트 단계를 진행합니다.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endtab %}
{% tab UI editor %}

1. 워크스페이스 데이터 설정 내에서 객체 데이터 유형(이 예에서는 ("flow_1" )으로 커스텀 속성을 이미 만들었는지 확인하세요.
2. UI 편집기에서 Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` 를 사용하여 커스텀 속성을 채우고 이에 대한 전체 사용자의 플로우 응답을 저장합니다. 생성한 커스텀 속성을 선택하기 전에 키 값을 ```{{whats_app.${inbound_flow_response}}}```{% endraw %} 으로 입력해야 합니다.

\![UI 편집기를 사용하는 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Braze가 플로우 응답을 받으면 지정된 이름을 가진 중첩된 고객 속성을 고객 프로필에 저장합니다. 해당 커스텀 속성은 캔버스를 구축할 때 가져올 수 있습니다. 

"flow_1" 커스텀 속성의 내용을 표시하는 창입니다.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endtab %}
{% endtabs %}

준비가 되면 테스트 메시지를 전송하여 플로우를 테스트합니다. 그런 다음 캔버스를 시작하세요!

## 플로우 응답의 특정 필드를 특정 커스텀 속성에 저장하기 

중첩된 고객 속성 또는 `json_parse` Liquid 태그를 사용하여 플로우 응답에서 특정 필드를 추출할 수 있습니다.

{% tabs %}
{% tab Nested custom attributes %}

사용자 플로우 응답의 특정 부분을 저장하려면 **캔버스 실행을 포함하여** [전체 플로우 응답 저장하기의](#full-flow) 모든 단계를 완료하세요. 참조할 중첩된 고객 속성을 만들려면 캔버스를 실행해야 합니다. 캔버스를 시작하고 플로우를 완료한 후 다음 단계를 수행합니다:

1. UI 편집기를 사용하는 후속 사용자 업데이트 단계를 만듭니다.
2. **개인화 추가를** 선택한 다음 **중첩된 고객 속성** 및 흐름이 저장된 해당 최상위 속성을 선택합니다.  

중첩 고객 속성 개인화가 포함된 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. 저장하려는 키 속성을 선택하고 **키 값** 필드에 Liquid를 입력합니다.

속성을 선택할 수 있는 "flow_1" 창이 열립니다.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. 저장할 속성을 선택합니다.
5\. 테스트 메시지를 전송하여 플로우를 테스트합니다.

{% endtab %}
{% tab Parse function %}

`json_parse` Liquid 태그를 사용하여 플로우에서 특정 응답을 추출하세요. 예를 들어, 플로우 토큰과 선택한 옵션을 꺼내 후속 메시지를 커스텀할 수 있습니다.

### 1단계: 행동 경로 만들기

**WhatsApp 인바운드 메시지 보내기** 트리거를 사용하여 [행동 경로를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 만들어 플로우 정보를 처리합니다.

{% alert note %}
얼리 액세스 기간 동안 추가 기능이 출시되면 흐름을 지정할 수 있습니다.
{% endalert %}

### 2단계: WhatsApp 메시지 작성하기

WhatsApp 메시지를 작성할 때 더하기 아이콘을 선택하여 **개인화 추가** 창을 연 다음, 개인화 유형에 대해 **WhatsApp 속성을** 선택하고 사용자 지정 속성에 대해 **inbound_flow_response** 을 선택하고 커스텀 속성을 선택합니다. 이렇게 하면 정보를 고객 프로필에 저장하거나 웹훅과 같은 다른 서비스로 전달할 수 있습니다.

### 3단계: 흐름 응답에서 특정 필드 저장하기

UI 편집기에서 다음을 선택합니다: 

- **속성 이름:** YOUR_CUSTOM_ATTRIBUTE (이 예제에서는 “First_name”)
- **액션:** 업데이트
- **키 값:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

\![커스텀 속성을 사용하여 WhatsApp 속성 개인화를 삽입하기 위해 "개인화 추가" 구성요소가 있는 WhatsApp 메시지 작성기 `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

{% alert note %}
새 WhatsApp 메시지는 캔버스의 Liquid Flow 응답 사용(및 재사용) 기능을 "지우므로" 후속 메시지는 모든 사용자 업데이트 단계, 웹훅 또는 Liquid Flow 응답을 사용하는 기타 단계 이후에 보내야 합니다.
{% endalert %}

준비가 되면 테스트 메시지를 전송하여 플로우를 테스트합니다. 그런 다음 캔버스를 시작하세요!

{% endtab %}
{% endtabs %}

{% alert note %}
진행 중인 작업 단계 필터와 플로우 요소를 통합한 응답 메시지 등 추가적인 플로우 기능이 도입될 예정입니다.
{% endalert %}

궁금한 점이 있거나 추가 지원이 필요한 경우 [지원팀에]({{site.baseurl}}/braze_support/) 문의하세요.
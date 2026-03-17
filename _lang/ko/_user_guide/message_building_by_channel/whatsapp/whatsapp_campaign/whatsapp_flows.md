---
nav_title: WhatsApp 흐름
article_title: WhatsApp 흐름
page_order: 1
description: "이 참조 문서에서는 WhatsApp 흐름 메시지를 구축하고 생성하는 데 필요한 단계에 대해 설명합니다."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp 흐름

> WhatsApp 흐름은 기존 WhatsApp 채널을 향상시켜 상호작용적이고 동적인 메시징 경험을 생성할 수 있게 합니다. 이 페이지에서는 WhatsApp 흐름을 사용하는 단계별 지침을 제공합니다.

## WhatsApp 흐름 설정하기

1. Meta 계정에 로그인합니다.
2. 두 가지 주요 위치 중 하나에서 흐름을 생성합니다:
    - **계정 도구:** **흐름** 탭으로 이동하여 흐름 ID를 보고 새 흐름을 생성합니다.
    - **템플릿 관리:** 이것은 흐름을 생성하는 데 권장되는 방법입니다. 여기에서 템플릿을 생성하고 템플릿 생성 과정 중에 흐름 옵션을 선택할 수 있습니다.

![WhatsApp 매니저와 흐름 템플릿을 생성하는 페이지입니다.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. 기존 흐름을 선택하거나 새로 만듭니다. 흐름을 생성하는 경우 두 가지 옵션 중에서 선택합니다:
  - **커스텀 양식:** 특정 요구 사항에 대한
  - **사전 설계된 요소:** 더 빠른 설정을 위해

## WhatsApp 흐름 메시지 및 응답 구성하기

{% tabs local %}
{% tab Template message %}

1. Braze Canvas에서 WhatsApp 메시지 단계를 생성하고 해당 Flow를 포함하는 템플릿 메시지를 사용합니다.
2. 템플릿 생성을 계속합니다. 필요한 경우 메시지에 미디어, 변수 콘텐츠 또는 둘 다 추가합니다. 템플릿이 만들어질 때 Flow 선택이 결정되므로 Flow 경험을 위한 추가 정보는 필요하지 않습니다.

![WhatsApp Flow 템플릿을 사용하는 WhatsApp 메시지 작성기입니다.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Braze Canvas에서 응답 메시지와 흐름 메시지를 사용하는 WhatsApp 메시지 단계를 생성합니다.

![WhatsApp 응답 메시지 유형 및 Flow 메시지 레이아웃을 위한 메시지 단계입니다.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. 해당 Flow를 선택한 후 메시지 생성을 계속합니다. 

![Flow 선택을 위한 확장 드롭다운이 있는 Flow 메시지 응답 작성기입니다.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Flow 미리보기

Flow로 Canvas를 시작하기 전에 **Flow 미리보기**를 선택하여 Braze에서 Flow를 직접 미리 보고 예상대로 작동하는지 확인할 수 있습니다. 미리보기에서 Flow와 상호작용하여 사용자가 Flow를 탐색하는 방식을 경험하고 실시간으로 조정할 수 있습니다. Flow에 여러 페이지가 포함된 경우 각 페이지와 상호작용할 수 있습니다.

![사용자가 가입을 완료하기 위한 양식을 표시하는 미리보기 창입니다.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## 전체 Flow 응답 저장 {#full-flow}

WhatsApp Flow 메시지를 Braze Canvas 또는 캠페인에 통합할 때 사용자가 Flow를 통해 제출한 특정 정보를 캡처하고 활용하고 싶을 수 있습니다. Braze는 사용자 응답의 구조에 대한 추가 정보를 수신해야 하며, 특히 JSON 응답의 예상 형식을 통해 필요한 중첩 사용자 정의 속성(NCA) 스키마를 생성합니다.

### 1단계: Flow 사용자 정의 속성 생성

{% tabs local %}
{% tab Recommended method %}

Braze에 응답 구조에 대한 정보를 제공하는 가장 간단한 방법은 Flow 응답을 사용자 정의 속성으로 저장하고 테스트 전송을 완료하는 것입니다.

#### Braze에서 사용되지 않은 Flow 사용

Braze에서 이전에 사용되지 않은 Flow를 사용하는 경우, **Flow Custom Attribute** 섹션을 **Compose Messages**에서 볼 때 정보가 표시되지 않을 수 있습니다. 이는 스키마가 아직 생성되지 않았음을 의미합니다.

![Flow 커스텀 속성을 볼 수 있는 옵션이 있는 Meta Flow 섹션입니다.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

이를 해결하려면 다음을 수행하십시오:

1. WhatsApp 메시지 단계를 설정하는 작업을 완료하십시오.
2. **Flow 응답을 커스텀 속성으로 저장**을 확인했는지 확인하십시오.

![Flow 응답을 커스텀 속성으로 저장하는 체크박스가 있는 Meta Flow 섹션입니다.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. 테스트 메시지를 자신에게 보내고 사용자가 Flow를 완료하십시오.

이제 Braze는 Flow 응답 JSON의 형태를 가지고 있으며 커스텀 속성을 생성할 수 있습니다.

{% endtab %}
{% tab Alternative methods %}

고급 JSON 편집기를 사용하여 Flow 응답에서 커스텀 속성으로 속성을 저장하거나, 다단계 캔버스를 사용하여 응답을 중첩 커스텀 속성으로 저장하십시오. 

{% subtabs %}
{% subtab Advanced JSON editor %}

고급 JSON 편집기에서 {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}을 입력하십시오. 여기서 “flow_1”는 Flow가 저장될 커스텀 속성입니다.

![고급 JSON 편집기를 사용하는 사용자 업데이트 단계입니다.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. 이 예제에서 ("flow_1" 객체 데이터 유형의 커스텀 속성을 이미 생성했는지 확인하십시오. 작업 공간 데이터 설정 내에서입니다.
2. UI 편집기에서 Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}```를 사용하여 커스텀 속성을 채우고 전체 사용자의 Flow 응답을 저장하십시오. 커스텀 속성을 선택하기 전에 키 값을 ```{{whats_app.${inbound_flow_response}}}```{% endraw %}로 채워야 합니다.

![UI 편집기를 사용하는 사용자 업데이트 단계입니다.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Braze가 Flow 응답을 수신한 후, 지정된 이름으로 중첩 커스텀 속성을 사용자 프로필에 저장합니다. 해당 커스텀 속성은 캔버스를 구축할 때 가져올 수 있습니다. 

![커스텀 속성의 내용을 표시하는 창입니다."flow_1"

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 2단계: 저장된 Flow 응답 보기

흐름이 완료되면, Braze는 흐름 ID를 기반으로 이름이 지정된 흐름 커스텀 속성을 자동으로 생성합니다. 그런 다음 고객 프로필로 이동하여 **커스텀 속성** 섹션에서 중첩된 객체로 저장된 흐름 응답을 볼 수 있습니다.

스키마가 생성된 후, 흐름 **커스텀 속성** 섹션은 각 응답에 대한 예상 데이터 유형(예: "문자열" 또는 "문자열 배열")을 포함하여 예상 구조를 표시합니다.

![흐름 커스텀 속성 세부 정보 창과 스키마 드롭다운.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### 고려 사항

- **기존 속성:** 특정 흐름에 대한 커스텀 속성이 이미 생성된 경우, 흐름은 사용 가능한 속성 정보와 함께 로드됩니다. 이 경우, Braze가 예상 응답 메시지를 이미 인식하고 있으므로 스키마를 생성하기 위해 테스트 메시지를 보낼 필요가 없습니다.
- **흐름 변경:** 스키마가 생성된 후 흐름에 변경 사항을 적용하면, Braze가 흐름 응답의 형태가 변경되었음을 이해하고 속성 구조를 조정할 수 있도록 추가 테스트 메시지를 보내야 합니다. 이 작업은 24시간마다 한 번으로 제한됩니다. 
- **일관성:** 생성된 흐름 커스텀 속성은 일관성이 있으며, 사용되는 캔버스와 관계없이 이 특정 흐름에 대해 동일한 속성이 됩니다.
- **수동 옵션:** **흐름 응답을 커스텀 속성으로 저장** 체크박스를 선택할 필요는 없습니다. 특정 커스텀 속성에 흐름 응답의 특정 필드를 저장하여 커스텀 속성을 수동으로 생성할 수 있으며, 이는 사용자 단계를 중복하지 않도록 합니다.

## 흐름 응답의 특정 필드를 특정 커스텀 속성에 저장하기 

### 1단계: 행동 경로 생성

[행동 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) 캔버스 단계 또는 행동 기반 캠페인을 생성합니다. **WhatsApp 수신 메시지 전송** 트리거와 **흐름에 응답** 조건을 선택한 다음, 관련 흐름 또는 **모든 흐름**을 선택합니다.

![수신 WhatsApp 메시지를 보내고 모든 흐름에 응답한 사용자에 대한 트리거입니다.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### 2단계: 플로우 응답에서 필드를 추출합니다.

중첩 커스텀 속성 또는 `json_parse` Liquid 태그를 사용하여 플로우 응답에서 특정 필드를 추출할 수 있습니다.

{% tabs %}
{% tab Nested custom attributes %}

사용자의 플로우 응답의 특정 부분을 저장하려면 [플로우 응답 전체 저장](#full-flow), **캔버스 시작 포함**의 모든 단계를 완료하십시오. 중첩 커스텀 속성을 생성하려면 캔버스를 시작해야 합니다. 캔버스를 시작하고 플로우를 완료한 후 다음 단계를 수행하십시오:

1. UI 편집기를 사용하는 후속 사용자 업데이트 단계를 만듭니다.
2. **개인화 추가**를 선택한 다음 **중첩 커스텀 속성** 및 플로우가 저장된 해당 최상위 속성을 선택합니다.  

![중첩 커스텀 속성 개인화가 있는 사용자 업데이트 단계.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. 저장하려는 키 속성을 선택하고 Liquid를 **키 값** 필드에 삽입합니다.

![선택할 속성이 있는 "flow_1"의 창.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. 저장할 속성을 선택하십시오.
5\. 플로우를 테스트하기 위해 테스트 메시지를 보냅니다.

{% endtab %}
{% tab Parse function %}

`json_parse` Liquid 태그를 사용하여 플로우에서 특정 응답을 추출합니다. 예를 들어, 플로우 토큰과 선택된 옵션을 추출하여 후속 메시지를 사용자화할 수 있습니다.

UI 편집기에서 다음을 선택하십시오: 

- **속성 이름:** YOUR_CUSTOM_ATTRIBUTE (이 예에서는: “First_name”)
- **Action:** 업데이트
- **키 값:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![WhatsApp 메시지 작성기에서 "개인화 추가" 구성 요소를 사용하여 커스텀 속성 `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})를 삽입합니다.

준비가 되면 플로우를 테스트하기 위해 테스트 메시지를 보냅니다. 그런 다음, 캔버스를 시작하세요!

{% endtab %}
{% endtabs %}

{% alert note %}
새로운 WhatsApp 메시지는 Canvas의 Liquid Flow 응답을 사용(및 재사용)하는 능력을 "지우기" 때문에 후속 메시지는 모든 사용자 업데이트 단계, 웹후크 또는 Liquid Flow 응답을 사용하는 다른 단계 이후에 있어야 합니다.
{% endalert %}

## Flow 개인화 태그 추가

[지원되는 개인화 태그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)를 통해 Liquid를 사용하여 Flow 응답을 사용하려면 다음 단계를 완료하십시오:

1. WhatsApp 메시지를 작성할 때, **개인화 추가** 창을 열기 위해 더하기 아이콘을 선택하십시오.
2. 개인화 유형으로 **WhatsApp 속성**을 선택하고 사용자 정의 속성으로 **inbound_flow_response**을 선택하십시오. 이것은 사용자 프로필에 정보를 저장하거나, 메시지에 포함시키거나, 웹후크와 같은 다른 서비스로 전달하는 데 사용할 수 있습니다.

![WhatsApp 메시지 작성기와 "개인화 추가" 구성 요소를 사용하여 사용자 정의 속성 inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}를 포함한 WhatsApp 속성 개인화를 삽입합니다.

질문이나 추가 지원이 필요하면 [지원]({{site.baseurl}}/braze_support/)에 문의하십시오.
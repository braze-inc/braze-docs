# Braze MCP 서버 사용하기

> Claude 및 Cursor와 같은 도구를 사용하여 자연어로 Braze 데이터와 상호작용하는 방법을 배우세요. 더 일반적인 정보는 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}를 참조하세요.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건

이 기능을 사용하기 전에 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}를 설정해야 합니다.

## Best practices

Claude 및 Cursor와 같은 자연어 도구를 통해 Braze MCP 서버를 사용할 때 최상의 결과를 얻기 위해 다음 팁을 염두에 두세요:

- LLM은 실수를 할 수 있으므로 항상 그들의 답변을 다시 확인하세요.
- 데이터 분석을 위해 필요한 시간 범위를 명확히 하세요. 짧은 범위가 더 정확한 결과를 제공하는 경우가 많습니다.
- 정확한 [Braze 용어](https://www.braze.com/resources/articles/glossary)를 사용하여 LLM이 올바른 기능을 호출하도록 하세요.
- 결과가 불완전해 보이면 LLM에게 계속 진행하거나 더 깊이 파고들도록 요청하세요.
- 창의적인 프롬프트를 시도해 보세요! MCP 클라이언트에 따라 CSV 또는 기타 유용한 파일을 내보낼 수 있습니다.

## 사용 예시

[Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "개발자" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}를 설정한 후, Claude 또는 Cursor와 같은 도구를 사용하여 자연어로 Braze와 상호작용할 수 있습니다. 시작하는 데 도움이 되는 몇 가지 예시입니다:

### 내가 사용할 수 있는 Braze 기능은 무엇인가요?

{% tabs %}
{% tab Claude %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?'가 Claude에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab 커서 %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?'가 커서에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### 캔버스 ID에 대한 세부정보 가져오기

{% tabs %}
{% tab Claude %}
!['캔버스 ID에 대한 세부정보 가져오기'가 클로드에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab 커서 %}
!['캔버스 ID에 대한 세부정보 가져오기'가 커서에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### 내 최근 캔버스를 보여줘

{% tabs %}
{% tab Claude %}
!['내 최근 캔버스를 보여줘'가 클로드에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab 커서 %}
!['내 최근 캔버스를 보여줘'가 커서에서 질문되고 답변됩니다.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}

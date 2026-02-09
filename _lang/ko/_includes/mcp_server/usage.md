# Braze MCP 서버 사용하기

> Claude 및 Cursor와 같은 도구를 사용하여 자연어를 통해 Braze 데이터와 상호 작용하는 방법을 알아보세요. 자세한 내용은 [Braze MCP 서버]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## 필수 조건

이 기능을 사용하려면 먼저 [Braze MCP 서버 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Best practices

Claude 및 Cursor와 같은 자연어 도구를 통해 Braze MCP 서버를 사용할 때 최상의 결과를 얻으려면 다음 팁을 염두에 두세요:

- LLM은 실수를 할 수 있으므로 항상 답변을 다시 한 번 확인해야 합니다.
- 데이터 분석을 위해서는 필요한 시간 범위를 명확히 해야 합니다. 범위가 짧을수록 더 정확한 결과를 얻을 수 있습니다.
- LLM이 올바른 함수를 호출할 수 있도록 정확한 [Braze 용어를](https://www.braze.com/resources/articles/glossary) 사용하세요.
- 결과가 불완전해 보이면 LLM에게 계속 진행하거나 더 깊이 파고들라는 메시지를 표시하세요.
- 창의적인 프롬프트를 사용해 보세요! MCP 클라이언트에 따라 CSV 파일이나 기타 유용한 파일을 내보낼 수 있습니다.

## 사용 예

Braze MCP 서버 설정]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, 클로드 또는 커서와 같은 도구를 사용하여 자연어를 통해 Braze와 상호 작용할 수 있습니다. 다음은 시작하는 데 도움이 되는 몇 가지 예시입니다:

### 내가 사용할 수 있는 Braze 기능은 무엇인가요?

{% tabs %}
{% tab Claude %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가요?"라는 질문을 Claude에서 묻고 답합니다.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['내가 사용할 수 있는 Braze 기능은 무엇인가'라는 질문을 받고 Cursor에서 답변합니다.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### 캔버스 ID에 대한 세부 정보 보기

{% tabs %}
{% tab Claude %}
!['캔버스 ID에 대한 세부 정보 가져오기' 질문과 답변이 Claude에서 이루어지고 있습니다.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![커서에서 '캔버스 ID에 대한 세부 정보 가져오기'를 묻고 답하는 모습.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### 내 최근 캔버스 보기

{% tabs %}
{% tab Claude %}
!['최근 캔버스를 보여줘'라는 질문과 답변이 Claude에서 이루어지고 있습니다.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![커서에서 '최근 캔버스 표시'를 묻고 답하는 모습.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}

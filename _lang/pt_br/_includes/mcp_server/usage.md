# Usando o servidor Braze MCP

> Saiba como interagir com seus dados do Braze por meio de linguagem natural usando ferramentas como Claude e Cursor. Para saber mais sobre informações gerais, consulte [Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos

Antes de poder usar esse recurso, você precisará [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Melhores práticas

Ao usar o servidor Braze MCP por meio de ferramentas de linguagem natural, como Claude e Cursor, lembre-se destas dicas para obter os melhores resultados:

- Os LLMs podem cometer erros, portanto, sempre verifique novamente suas respostas.
- Para a análise de dados, seja claro quanto ao intervalo de tempo de que você precisa. Alcances mais curtos geralmente fornecem resultados mais precisos.
- Use [a terminologia](https://www.braze.com/resources/articles/glossary) exata [do Braze](https://www.braze.com/resources/articles/glossary) para que seu LLM chame a função correta.
- Se os resultados parecerem incompletos, peça ao seu LLM para continuar ou se aprofundar.
- Experimente sugestões criativas! Dependendo do seu cliente MCP, você poderá exportar um arquivo CSV ou outros arquivos úteis.

## Exemplos de uso

Após [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode interagir com o Braze por meio de linguagem natural usando ferramentas como Claude ou Cursor. Aqui estão alguns exemplos para você começar:

### Quais são minhas funções disponíveis no Braze?

{% tabs %}
{% tab Claude %}
!["Quais são as minhas funções de Braze disponíveis?" sendo perguntadas e respondidas no Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Quais são minhas funções Braze disponíveis' sendo perguntadas e respondidas no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Obter detalhes sobre uma ID de tela

{% tabs %}
{% tab Claude %}
!['Get details about a canva ID' being asked and answered in Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Get details about a canva ID' sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Mostre-me minhas telas recentes

{% tabs %}
{% tab Claude %}
!['Show my recent canvas' sendo perguntado e respondido em Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Show my recent canvas' sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}

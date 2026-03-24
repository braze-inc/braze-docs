# Usando o servidor Braze MCP

> Aprenda a interagir com seus dados Braze por meio de linguagem natural usando ferramentas como Claude e Cursor. Para obter informações mais gerais, consulte [Servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Pré-requisitos

Antes de poder usar esse recurso, você precisará [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Melhores práticas

Ao usar o servidor Braze MCP por meio de ferramentas de linguagem natural, como Claude e Cursor, lembre-se destas dicas para obter os melhores resultados:

- Os LLMs podem cometer erros, portanto, certifique-se sempre de verificar suas respostas.
- Para a análise de dados, seja claro quanto ao intervalo de tempo necessário. Intervalos mais curtos geralmente fornecem resultados mais precisos.
- Use [uma terminologia](https://www.braze.com/resources/articles/glossary) exata [do Braze](https://www.braze.com/resources/articles/glossary) para que seu LLM chame a função correta.
- Se os resultados parecerem incompletos, solicite ao seu LLM que continue ou aprofunde a pesquisa.
- Experimente sugestões criativas! Dependendo do seu cliente MCP, você poderá exportar um arquivo CSV ou outros arquivos úteis.

## Exemplos de uso

Após [configurar o servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, você pode interagir com o Braze por meio de linguagem natural usando ferramentas como Claude ou Cursor. Aqui estão alguns exemplos para você começar:

### Quais são as funções disponíveis do Braze?

{% tabs %}
{% tab Claude %}
![“Quais são as funções disponíveis do Braze?” sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![“Quais são as funções disponíveis do Braze?” sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Obtenha detalhes sobre um ID do Canvas

{% tabs %}
{% tab Claude %}
!["Obter detalhes sobre um ID de canva" sendo perguntado e respondido no Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!["Obter detalhes sobre um ID de canva" sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Mostre-me meus canvases recentes

{% tabs %}
{% tab Claude %}
![“Mostre meus canvases recentes” sendo perguntado e respondido em Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![“Mostrar meus canvases recentes” sendo perguntado e respondido no Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}

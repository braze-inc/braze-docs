# Uso del servidor MCP de Braze

> Aprende a interactuar con tus datos de Braze mediante lenguaje natural utilizando herramientas como Claude y Cursor. Para obtener información más general, consulta [Servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Requisitos previos

Antes de poder utilizar esta característica, tendrás que [configurar el servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Buenas prácticas

Cuando utilices el servidor Braze MCP a través de herramientas de lenguaje natural como Claude y Cursor, ten en cuenta estos consejos para obtener los mejores resultados:

- Los LLM pueden cometer errores, así que asegúrate siempre de verificar sus respuestas.
- Para el análisis de datos, ten claro el intervalo de tiempo que necesitas. Los rangos más cortos suelen dar resultados más precisos.
- Utiliza [la terminología](https://www.braze.com/resources/articles/glossary) exacta [de Braze](https://www.braze.com/resources/articles/glossary) para que tu LLM llame a la función correcta.
- Si los resultados parecen incompletos, pide a tu LLM que continúe o profundice más.
- ¡Prueba con sugerencias creativas! Dependiendo de tu cliente MCP, es posible que puedas exportar un archivo CSV u otros archivos útiles.

## Ejemplos de uso

Después de [configurar el servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes interactuar con Braze mediante lenguaje natural utilizando herramientas como Claude o Cursor. Aquí tienes algunos ejemplos para empezar:

### ¿Cuáles son las funciones disponibles de Braze?

{% tabs %}
{% tab Claude %}
![«¿Cuáles son las funciones de Braze que tengo disponibles?», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«¿Cuáles son las funciones disponibles de Braze?» Pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Obtener detalles sobre un ID de Canvas

{% tabs %}
{% tab Claude %}
![Pregunta y respuesta sobre «Obtener detalles sobre un ID de Canvas» en Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![Pregunta y respuesta sobre «Obtener detalles sobre un ID de Canvas» en Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Muéstrame mis lienzos recientes.

{% tabs %}
{% tab Claude %}
![«Mostrar mis lienzos recientes», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«Mostrar mis lienzos recientes» preguntado y respondido en Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}

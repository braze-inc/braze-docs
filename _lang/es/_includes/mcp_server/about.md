# El servidor MCP de Braze

> Descubre el servidor MCP de Braze, una conexión segura y de solo lectura que permite a herramientas de IA como Claude y Cursor acceder a datos de Braze que no son PII para responder preguntas, analizar tendencias y proporcionar información sin alterar los datos.

{% multi_lang_include mcp_server/beta_alert.md %}

## ¿Qué es el Protocolo de Contexto de Modelo (MCP)?

​El Protocolo de contexto de modelo, o MCP, es un estándar que permite a los agentes de IA conectarse y trabajar con datos de otra plataforma. Tiene dos partes principales:

- **Cliente MCP:** La aplicación en la que se ejecuta el agente de IA, como Cursor o Claude.
- **Servidor MCP:** Servicio prestado por otra plataforma, como Braze, que define qué herramientas puede utilizar la IA y a qué datos puede acceder.

## Acerca del servidor MCP de Braze

Después de [configurar el servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes conectar herramientas de IA como agentes, asistentes y chatbots directamente a Braze, lo que les permite leer datos agregados como análisis de Canvas y campañas, atributos personalizados, segmentos y mucho más. El servidor MCP de Braze es ideal para:

- Creación de herramientas basadas en inteligencia artificial que necesitan el contexto de Braze.
- Ingenieros de CRM en la ingeniería de flujos de trabajo de varios pasos para los agentes.
- Especialistas en marketing que experimentan con consultas en lenguaje natural.

El servidor MCP de Braze admite 38 puntos finales de solo lectura que no devuelven datos de los perfiles de usuario de Braze. Puedes optar por asignar solo algunos de estos puntos finales a tu clave de API de Braze para restringir aún más los datos a los que puede acceder un agente.

{% alert warning %}
No asignes permisos a tu clave de API que **no** sean de solo lectura. Los agentes pueden intentar escribir o eliminar datos en Braze, lo que podría provocar consecuencias no deseadas.
{% endalert %}

## Ejemplo de uso

Puedes interactuar con Braze mediante lenguaje natural utilizando herramientas como Claude o Cursor. Para ver otros ejemplos y prácticas recomendadas, consulta [Uso del servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![«¿Cuáles son las funciones de Braze que tengo disponibles?», pregunta y respuesta en Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![«¿Cuáles son las funciones disponibles de Braze?» Pregunta y respuesta en Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Preguntas más frecuentes (FAQ) {#faq}

### ¿Qué clientes MCP son compatibles?

Solo [Claude](https://claude.ai/) y [Cursor](https://cursor.com/) son oficialmente compatibles. Debes tener una cuenta para uno de estos clientes para poder utilizar el servidor MCP de Braze.

### ¿A qué datos de Braze puede acceder tu cliente MCP?

Los clientes de MCP solo pueden acceder a puntos finales de solo lectura que no estén diseñados para recuperar PII. No pueden manipular datos en Braze.

### ¿El cliente MCP puede manipular los datos de Braze?

No. El servidor MCP solo expone herramientas que manejan datos no PII y de solo lectura.

### ¿Puedes utilizar un servidor MCP de terceros para Braze?

No se recomienda utilizar un servidor MCP de terceros para los datos de Braze. Utiliza únicamente el servidor oficial Braze MCP alojado en [PyPi](https://pypi.org/project/braze-mcp-server/).

### ¿Por qué el servidor MCP de Braze no ofrece información de identificación personal (PII) ni acceso de escritura?

Para proteger los datos sin dejar de habilitar la innovación, el servidor se limita a puntos finales que son de solo lectura y que normalmente no devuelven información de PII. Esto reduce el riesgo y, al mismo tiempo, respalda casos de uso valiosos.

### ¿Puedo reutilizar mis claves de API?

No. Tendrás que crear una nueva clave de API para tu cliente MCP. Recuerda dar acceso a tus herramientas de IA solo a aquello con lo que te sientas cómodo y evita conceder permisos elevados.

### ¿El servidor Braze MCP está alojado localmente o de forma remota?

El servidor MCP de Braze está alojado localmente.

### ¿Por qué Cursor solo muestra funciones?

Comprueba si estás en modo de consulta o en modo de agente. Para utilizar el servidor MCP, debes estar en modo agente.

### ¿Qué hago cuando el agente devuelve una respuesta que parece incorrecta?

Cuando trabajes con herramientas como Cursor, es posible que desees probar a cambiar el modelo utilizado. Por ejemplo, si lo tienes configurado en automático, prueba a cambiarlo a un modelo específico y experimenta para descubrir cuál es el modelo con mejor rendimiento para tu caso de uso. También puedes intentar iniciar un nuevo chat y volver a intentar el mensaje. 

Si los problemas persisten, puedes realizar un envío por correo electrónico a [mcp-product@braze.com](mailto:mcp-product@braze.com) para informarnos. Si es posible, incluye un video y amplía las funciones de llamada para que podamos ver qué llamadas intentó realizar el agente.

{% multi_lang_include mcp_server/legal_disclaimer.md %}

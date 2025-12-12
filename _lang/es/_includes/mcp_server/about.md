# El servidor Braze MCP

> Infórmate sobre el servidor Braze MCP, una conexión segura de sólo lectura que permite a herramientas de IA como Claude y Cursor acceder a datos Braze no PII para responder preguntas, analizar tendencias y proporcionar información sin alterar los datos.

{% multi_lang_include mcp_server/beta_alert.md %}

## ¿Qué es el Protocolo de Contexto Modelo (MCP)?

​El Protocolo de Contexto de Modelos, o MCP, es un estándar que permite a los agentes de IA conectarse y trabajar con datos de otra plataforma. Tiene dos partes principales:

- **Cliente de MCP:** La aplicación donde se ejecuta el agente de IA, como Cursor o Claude.
- **Servidor MCP:** Un servicio proporcionado por otra plataforma, como Braze, que define qué herramientas puede utilizar la IA y a qué datos puede acceder.

## Acerca del servidor Braze MCP

Después de [configurar el servidor Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "desarrollador" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, puedes conectar herramientas de IA como agentes, asistentes y chatbots directamente a Braze, permitiéndoles leer datos agregados como análisis de Canvas y campañas, atributos personalizados, segmentos y mucho más. El servidor Braze MCP es estupendo para:

- Crear herramientas basadas en IA que necesiten el contexto de Braze.
- Ingenieros de CRM creando flujos de trabajo de agentes en varios pasos.
- Especialistas en marketing técnico que experimentan con consultas en lenguaje natural.

El servidor Braze MCP admite 38 puntos finales de sólo lectura que no devuelven datos de perfiles de usuario Braze. Puedes optar por asignar sólo algunos de estos puntos finales a tu clave de API Braze para restringir aún más a qué datos puede acceder un agente.

{% alert warning %}
No asignes permisos a tu clave de API que **no sean** de sólo lectura. Los agentes pueden intentar escribir o borrar datos en Braze, lo que podría causar consecuencias no deseadas.
{% endalert %}

## Ejemplo de uso

Puedes interactuar con Braze mediante lenguaje natural utilizando herramientas como Claude o Cursor. Para otros ejemplos y buenas prácticas, consulta [Uso del servidor MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "desarrollador" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![Pregunta "¿Cuáles son mis funciones Braze disponibles?" y responde en Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
!['Cuáles son mis funciones Braze disponibles' se pregunta y se responde en Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Preguntas más frecuentes (FAQ) {#faq}

### ¿Qué clientes MCP son compatibles?

Actualmente, sólo [Claude](https://claude.ai/) y [Cursor](https://cursor.com/) son compatibles oficialmente. Necesitarás una cuenta de uno de estos clientes para utilizar el servidor Braze MCP.

### ¿A qué datos de Braze puede acceder mi cliente MCP?

Los clientes MCP sólo pueden acceder a puntos finales de sólo lectura que no estén creados para recuperar PII. No pueden manipular datos en Braze.

### ¿Puede mi cliente MCP manipular datos Braze?

No. El servidor MCP sólo expone herramientas que manejan datos no PII, de sólo lectura.

### ¿Puedo utilizar un servidor MCP de terceros para Braze?

No se recomienda utilizar un servidor MCP de terceros para los datos de Braze. Utiliza sólo el servidor oficial Braze MCP alojado en [PyPi](https://pypi.org/project/braze-mcp-server/).

### ¿Por qué el servidor Braze MCP no ofrece PII ni acceso de escritura?

Para proteger los datos sin dejar de habilitar la innovación, hemos construido el servidor de forma que se limite a puntos finales de sólo lectura y que no suelen devolver PII. Esto reduce el riesgo al tiempo que da soporte a valiosos casos de uso.

### ¿Puedo reutilizar mis claves de API?

No. Tendrás que crear una nueva clave de API para tu cliente MCP. Recuerda que sólo debes dar acceso a tus herramientas de IA a aquello con lo que te sientas cómodo, y evita los permisos elevados.

### ¿El servidor Braze MCP está alojado local o remotamente?

Actualmente, el servidor MCP de Braze está alojado localmente.

### ¿Por qué Cursor sólo enumera funciones?

Comprueba si estás en modo pregunta o en modo agente. Para utilizar el servidor MCP, tienes que estar en modo agente.

### ¿Qué hago cuando el agente devuelve una respuesta que parece incorrecta?

Cuando trabajes con herramientas como Cursor, puedes probar a cambiar el modelo utilizado. Por ejemplo, si lo tienes configurado en automático, prueba a cambiarlo por un modelo concreto y experimenta para encontrar cuál es el que mejor se adapta a tu caso de uso. También puedes probar a iniciar un nuevo chat y volver a intentar la solicitud. 

Si los problemas persisten, puedes enviarnos un correo electrónico a [mcp-product@braze.com](mailto:mcp-product@braze.com) para informarnos. Si es posible, incluye un video y amplía las funciones de llamada para que podamos ver qué llamadas intentó el agente.

{% multi_lang_include mcp_server/legal_disclaimer.md %}

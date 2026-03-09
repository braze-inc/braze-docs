---
nav_title: Construye con un LLM
article_title: Construcción con un LLM
page_order: 4
description: "Aprende a utilizar los asistentes de codificación con IA con la documentación de Braze para acelerar tu flujo de trabajo de integración de SDK."
platform:
  - Web
  - React Native
---

# Construcción con un LLM

> Utiliza asistentes de codificación con IA para acelerar tu flujo de trabajo de integración con Braze. Conecta tu IDE al servidor MCP de Braze Docs a través de Context7 y obtén orientación precisa y actualizada sobre el SDK directamente en tu entorno de desarrollo.

Los asistentes de codificación con IA pueden ayudarte a escribir código de integración, realizar la solución de problemas y explorar las características del SDK de Braze, pero solo si disponen del contexto adecuado. El servidor Braze Docs MCP proporciona a tu asistente de IA acceso directo a la documentación de Braze, para que pueda generar fragmentos de código precisos y responder a preguntas técnicas basándose en las últimas referencias del SDK.

## Conexión a Braze Docs MCP

[Context7](https://context7.com/braze-inc/braze-docs) sirve de puente entre tu asistente de IA y la biblioteca de documentación de Braze. Al añadir Context7 a la configuración MCP de tu IDE, tu asistente de IA puede realizar consultas sobre toda la documentación de Braze y recuperar referencias relevantes del SDK, ejemplos de código y guías de integración bajo demanda.

### Configuración de Context7

Para conectar tu asistente de IA al MCP de Braze Docs a través de Context7, añade la siguiente configuración al archivo `mcp.json`de tu IDE.

{% tabs %}
{% tab Cursor %}
En [Cursor](https://cursor.com/), ve a **Configuración** > **Herramientas e integraciones** > **Herramientas MCP** > **Añadir MCP personalizado** y, a continuación, añade el siguiente fragmento de código:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Guarda la configuración y reinicia Cursor. Tu asistente de IA ahora puede acceder a la documentación de Braze a través de Context7 cuando incluyes`use context7`  en tus indicaciones.
{% endtab %}

{% tab Claude %}
En Claude Desktop, ve a **Configuración** > **Desarrollador** > **Editar configuración** y, a continuación, añade lo siguiente a tu`claude_desktop_config.json`archivo:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Guarda la configuración y reinicia Claude Desktop.
{% endtab %}

{% tab VS Code %}
Añade lo siguiente a tu VS Code`settings.json`  o`.vscode/mcp.json`  archivo:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Guarda la configuración y reinicia VS Code.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7 es diferente del [servidor MCP de]({{site.baseurl}}/developer_guide/mcp_server/) [Braze]({{site.baseurl}}/developer_guide/mcp_server/). Context7 proporciona a tu asistente de IA acceso a **la documentación de Braze**, mientras que el servidor MCP de Braze proporciona acceso de solo lectura a **los datos de tu espacio de trabajo de Braze** (como campañas, segmentos y análisis). Puedes utilizar ambos juntos para disfrutar de una experiencia de desarrollo asistida por IA más completa.
{% endalert %}

## Pistas para escribir sobre el desarrollo del SDK de Braze para desarrolladores

Después de configurar Context7, incluye`use context7`  en tus indicaciones para indicar a tu asistente de IA que utilice la documentación de Braze como contexto. Los siguientes ejemplos muestran cómo escribir indicaciones eficaces para tareas comunes del SDK.

### SDK de React Native

Estas indicaciones muestran tareas de integración comunes para el [SDK de Braze React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/).

#### Inicialización del SDK

```text
Using the Braze React Native SDK, show me how to initialize the SDK 
in my App.tsx with an API key and custom endpoint. Include the 
configuration for automatic session tracking. Use context7.
```

#### Registro de eventos personalizados con propiedades

```text
I need to track user activity in my React Native app using the Braze 
React Native SDK. Show me how to log a custom event called 
"ProductViewed" with properties for product_id, category, and price. 
Use context7.
```

#### Configuración de notificaciones push

```text
Using the Braze React Native SDK, walk me through requesting push 
notification permissions on both iOS and Android 13+. Include the 
code for registering the push token with Braze. Use context7.
```

#### Gestión de mensajes dentro de la aplicación

```text
Show me how to subscribe to in-app messages using the Braze React 
Native SDK, including how to log impressions and button clicks 
programmatically. Use context7.
```

### SDK Web

Estas indicaciones muestran tareas de integración comunes para el [SDK Web de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).

#### Inicialización del SDK

```text
Using the Braze Web SDK, show me how to initialize the SDK with 
braze.initialize(), including the API key, base URL, and options 
for enabling logging and automatic in-app message display. 
Use context7.
```

#### Seguimiento de eventos personalizados y compras

```text
Using the Braze Web SDK, create a JavaScript module that logs a 
custom event called "VideoPlayed" with properties for video_id, 
duration_seconds, and completion_percentage. Also show how to log 
a purchase with product ID, price, currency code, and quantity. 
Use context7.
```

#### Registro para notificaciones push web

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to 
register a user for web push notifications after they click a 
"Subscribe to updates" button. Include the service worker setup. 
Use context7.
```

#### Gestión de los atributos de usuario

```text
Using the Braze Web SDK, show me how to set standard user attributes 
(first name, email, country) and custom user attributes (favorite_genre, 
subscription_tier) for the current user. Use context7.
```

## Documentación en texto sin formato

Puedes acceder a la documentación de la Guía para desarrolladores de Braze como archivos de texto sin formato optimizados para herramientas de IA y LLM. Estos archivos proporcionan documentación de Braze en un formato que los asistentes de IA pueden analizar y comprender sin la sobrecarga que supone la representación HTML.

| Archivo | Descripción |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | Índice de las páginas de documentación para desarrolladores de Braze con títulos y descripciones. Utiliza esto como punto de partida para descubrir la documentación disponible. |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | La documentación completa para desarrolladores de Braze en un único archivo de texto sin formato, formateado para su uso con LLM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Estos archivos siguen el[llms.txt](https://llmstxt.org/)[estándar](https://llmstxt.org/), una convención emergente para hacer que la documentación sea accesible para las herramientas de IA. Puedes hacer referencia a estos archivos directamente en tus indicaciones o pegar su contenido en un LLM para contextualizar.

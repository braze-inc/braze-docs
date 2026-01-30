---
nav_title: Historia completa
article_title: Historia completa
description: "Este artículo de referencia describe la asociación entre Braze y Fullstory."
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# Historia completa

La plataforma de datos de comportamiento de Fullstory ayuda a los líderes tecnológicos a tomar decisiones mejores y más informadas. Al inyectar datos de comportamiento digital en su pila de análisis, la tecnología patentada de Fullstory libera el poder de los datos de comportamiento de calidad a escala, transformando cada visita digital en información accionable. 

*Esta integración está mantenida por Fullstory*

## Acerca de esta integración
Puedes aprovechar la información de Fullstory en Braze para crear imágenes en cada momento de la experiencia de un usuario en el sitio web o la aplicación para entregar mensajes hipercontextuales. La API de resumen de sesión de Fullstory permite capturar metadatos detallados sobre el comportamiento de navegación de un usuario para utilizarlos en la mensajería Braze, que es especialmente potente cuando se aprovecha en un viaje de mensajería de varios pasos como un Canvas. 

El valor en tiempo real de los datos del Resumen de Sesión de Fullstory se aprovecha mejor a través del Contenido conectado. Al utilizar contenido conectado en un paso en Canvas, puedes almacenar los datos de Fullstory a lo largo del recorrido de un usuario en Canvas para utilizarlos en cualquier paso posterior en Canvas. Esto también evita la necesidad de escribir estos datos en un perfil de usuario Braze a través de eventos o atributos personalizados. 

En el siguiente ejemplo, se aprovechan los datos de contexto de Canvas en un paso en Canvas de IA de Agente para generar el mensaje óptimo que anime a un usuario a volver a recoger un carrito abandonado. Sin embargo, puedes aprovechar los datos para personalizar el mensaje directamente, para determinar el recorrido del usuario a través de las rutas de audiencia, o para determinar el texto o los activos utilizados en los pasos posteriores de la mensajería.

## Ejemplos

![Diagrama que muestra los casos de uso de la integración de Fullstory con Braze]({% image_buster /assets/img/fullstory/1.png %})

## Requisitos previos

Antes de empezar, necesitas lo siguiente:

|Requisito     | Descripción |                        
|-----------------------|-----------------|
| Un token de autorización de la API de sesión de Fullstory   | Consulta el Paso 1 más abajo.  | 
| Un token de autorización de contenido conectado Braze habilitado | Consulta la nota siguiente sobre Acceso anticipado |
| Un Paso en Canvas Braze Contexto |Consulta la nota siguiente sobre Acceso anticipado |
| Habilitación del Paso Agente Braze AI | Consulta la nota siguiente sobre Acceso anticipado|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Integración Fullstory

### Paso 1: Configurar Fullstory para la habilitación de la API de Resumen de Sesión

#### A: Recuperar el [token de autenticación](https://developer.fullstory.com/server/authentication/) para el punto final de la API de resumen de sesión

Para crear una clave de API de Fullstory, ve a la plataforma de Fullstory y, a continuación, a **Configuración** > **Claves de API**. Selecciona el nivel de permiso **Estándar** y copia inmediatamente el valor de la clave, ya que sólo aparece una vez.

#### B: Crear un resumen de sesión ID de perfil

Siguiendo [las indicaciones de Fullstory](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles), crea un perfil de resumen de sesión utilizando el punto final dedicado. Aquí es donde defines qué tipo de datos quieres que la respuesta Resumen de sesión proporcione a Braze.
En la respuesta a esta solicitud, Fullstory proporciona un "ID de perfil" de sesión. Este ID de perfil es un componente clave del cuerpo de la solicitud de contenido conectado que se utiliza en el siguiente caso de uso.


### Paso 2: Crear el token de contenido conectado Auth
1. En Braze, ve a **Configuración > Configuración del espacio de trabajo > Contenido conectado > Añadir credenciales > Autenticación por token**. 

2. Nombra la autenticación "fullstory".

3. Añade la clave de cabecera "Autorización". Suministra el valor de Cabecera Fullstory proporcionado en el paso anterior. 

4. En Dominio permitido, introduce "api.fullstory.com".

![Captura de pantalla de Braze mostrando los campos Editar credenciales]({% image_buster /assets/img/fullstory/2.png %})

## Casos de uso: Aprovecha los datos del Resumen de Sesión de Fullstory y los pasos en Canvas del Contexto Braze y los Agentes de IA para crear recorridos de mensajes dinámicos

Utilizando [los Flujos de Activación](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams) de Fullstory, puedes desencadenar Lienzos Braze inmediatamente después de las interacciones clave de los usuarios. El poder de esta integración reside en el `client_session_id` único (accesible a través de {% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %}), que el sistema pasa automáticamente de Fullstory a Braze. Este ID actúa como clave, permitiendo a Braze obtener el Resumen de Sesión completo de lo que experimentó exactamente el usuario. 

Aprovechando los pasos en Contexto Canvas y el Contenido conectado, puedes utilizar este ID para hacer una solicitud de API a Fullstory, recuperar los datos de la sesión y almacenarlos como una variable para utilizarlos más adelante en el viaje. 

![Captura de pantalla del paso en Canvas de Braze que muestra la variable de contexto `summary_result` creada y rellenada con una llamada de contenido conectado a Fullstory, para recuperar un resumen de sesión]({% image_buster /assets/img/fullstory/3.png %})

Con el token de Autorización creado anteriormente, utiliza la siguiente estructura de petición para obtener los datos del Resumen de Sesión. 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 La respuesta se almacena como etiqueta de Liquid {% raw %}`{{context.${summary_result}.response}}`{% endraw %}. Utilizaremos esta etiqueta Contexto en los siguientes pasos en Canvas.
{% endalert %}

En esta fase, el Canvas puede acceder a la respuesta a la llamada de Contenido Conectado, que contiene toda la carga útil del mensaje para la sesión de un usuario.

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

Puedes aprovechar cualquiera de los datos disponibles en el objeto anterior utilizando la etiqueta de contexto Liquid más adelante en el recorrido del usuario por el Canvas. Los pasos siguientes muestran cómo puedes utilizar estos datos en un paso en Canvas [de Agente de IA](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step).

{% alert Note %}
Para evitar comportamientos inesperados, incluye un paso de Ruta de audiencia después del paso Contexto, que puede sacar a los usuarios del contexto si su etiqueta Contexto está vacía, indicando que la llamada al contenido conectado falló o no devolvió ninguna información.

![Captura de pantalla del paso Audiencia Braze]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## Crea un Agente de IA que pueda analizar las cargas útiles de Fullstory y producir la copia adecuada para tu caso de uso

[La guía de agentes de Braze]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents) describe cómo los usuarios de Braze pueden crear Agentes de IA. Insertando un paso del Agente de IA en un Canvas desencadenado por Fullstory, e incluyendo el paso Contexto del Canvas descrito anteriormente, los usuarios pueden alimentar a su Agente de IA con los datos de resumen de sesión de Fullstory, para una amplia gama de fines. 

En este ejemplo, utilizamos estos datos para permitir que el Agente de IA genere una copia de mensaje adecuada para su uso en una tarjeta de contenido, que puede animar al usuario a volver a su cesta abandonada.

![Captura de pantalla del Agente Braze Creador de Contexto con el prompt]({% image_buster /assets/img/fullstory/4.png %})

Utiliza el mismo nombre para la etiqueta de Contexto Liquid creada en este paso que la etiqueta de contexto Liquid utilizada en el paso Agente AI creado anteriormente. 

La instrucción necesaria para tu caso de uso varía, pero para conocer nuestras mejores prácticas para crear instrucciones eficaces para los agentes, consulta [Escribir instrucciones]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions) en *Crear agentes*. 


En tu Canvas, selecciona un paso de Agente AI y, a continuación, selecciona el agente "Contexto de sesión" creado en el menú desplegable. Guarda el resultado como una variable, en este caso "mensaje", que puedes colocar en la copia del mensaje utilizando la etiqueta de Liquid {% raw %}`{{context.${message}.message}}`{% endraw %}.

![Captura de pantalla del paso en Canvas contextual del Agente Braze con la consulta]({% image_buster /assets/img/fullstory/5.png %})

Crea un paso de mensaje que aproveche la copia creada por el Agente de IA. Utiliza la etiqueta de Liquid en este paso. 

{% alert Note %}

La API de resumen de sesión de Fullstory puede devolver datos de usuario identificadores sensibles. Para garantizar el cumplimiento al manejar PII (Información de Identificación Personal), asegúrate de que tus reglas de captura de datos de Fullstory excluyen la PII antes de aprovechar este caso de uso.

{% endalert %}
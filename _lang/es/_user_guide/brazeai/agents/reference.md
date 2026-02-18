---
nav_title: Referencia
article_title: Agentes de referencia
description: "Consulta los detalles clave sobre los Agentes Braze."
page_order: 3
---

# Agentes de referencia

> Cuando crees agentes personalizados, consulta este artículo para obtener más información sobre configuraciones clave, como instrucciones y esquemas de salida. Para una introducción, ver [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

{% alert important %}
Los Agentes Braze están actualmente en fase beta. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Modelos

Cuando configuras un agente, puedes elegir el modelo que utiliza para generar respuestas. Tienes dos opciones: utilizar un modelo potenciado por Braze o aportar tu propia clave de API.

{% alert important %}
El modelo **Auto** impulsado por Braze está optimizado para modelos cuya capacidad de pensamiento sea suficiente para realizar tareas como la búsqueda de catálogos y la pertenencia a segmentos de usuarios. Cuando utilices otros modelos, te recomendamos que hagas pruebas para confirmar que tu modelo funciona bien para tu caso de uso. Puede que tengas que ajustar tus [instrucciones](#writing-instructions) para dar diferentes niveles de detalle o paso a paso a modelos con diferentes velocidades y capacidades.
{% endalert %}

### Opción 1: Utiliza un modelo accionado por Braze

Esta es la opción más sencilla, sin necesidad de configuración adicional. Braze proporciona acceso directo a grandes modelos lingüísticos (LLM). Para utilizar esta opción, selecciona **Auto**, que utiliza los modelos Gemini.

### Opción 2: Trae tu propia clave de API

Con esta opción, puedes conectar tu cuenta de Braze con proveedores como OpenAI, Anthropic, AWS Bedrock o Google Gemini. Si traes tu propia clave de API de un proveedor de LLM, los costes del token se facturan directamente a través de tu proveedor, no a través de Braze.

{% alert important %}
Recomendamos probar rutinariamente los modelos más recientes, ya que los modelos heredados pueden dejar de fabricarse o quedar obsoletos al cabo de unos meses.
{% endalert %}

Para configurarlo:

1. Ve a **Integraciones de socios** > **Socios tecnológicos** y encuentra a tu proveedor.
2. Introduce tu clave de API del proveedor.
3. Seleccione **Guardar**.

Después, puedes volver a tu agente y seleccionar tu modelo.

{% alert important %}
Cuando utilices un LLM proporcionado por Braze, los proveedores de dicho modelo estarán actuando como Subprocesadores de Braze, sujetos a los términos del Anexo de Procesamiento de Datos (DPA) entre tú y Braze. Si decides aportar tu propia clave de API, el proveedor de tu suscripción a LLM se considera un Tercero Proveedor según el contrato entre tú y Braze.  
{% endalert %}

## Instrucciones de escritura

Las instrucciones son las normas o directrices que das al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Las instrucciones del sistema pueden ser de hasta 25 KB.

Estas son algunas de las mejores prácticas generales para empezar con la incitación:

1. Empieza pensando en el final. Enuncia primero el objetivo.
2. Dale al modelo un papel o personaje ("Eres un ...").
3. Establece un contexto y unas limitaciones claras (audiencia, duración, tono, formato).
4. Pide estructura ("Devuelve JSON/lista de viñetas/tabla...").
5. Muestra, no cuentes. Incluye algunos ejemplos de alta calidad.
6. Divide las tareas complejas en pasos ordenados ("Paso 1... Paso 2...").
7. Fomenta el razonamiento ("Piensa internamente en los pasos, luego da una respuesta final concisa", o "explica brevemente tu decisión").
8. Pilota, inspecciona e itera. Pequeños ajustes pueden dar lugar a grandes ganancias de calidad.
9. Trata los casos extremos, añade guardarraíles y añade instrucciones de rechazo.
10. Mide y documenta lo que funciona internamente para su reutilización y ampliación.

Recomendamos incluir también un predeterminado como respuesta comodín si el agente recibe una respuesta que no se puede analizar. Este tratamiento de errores permite al agente informarte de una variable de resultado desconocida. Por ejemplo, en lugar de pedir al agente sólo valores de sentimiento "positivos" o "negativos", pídele que devuelva "inseguro" si no puede decidir.

### Aviso simple

Este ejemplo de consulta toma la entrada de un cuestionario y genera un sencillo análisis de sentimientos:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative.
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Aviso complejo 

Este ejemplo toma la entrada de un cuestionario de un usuario y la clasifica en una única etiqueta de sentimiento. El resultado puede utilizarse para dirigir a los usuarios por diferentes rutas de Canvas (como las opiniones positivas frente a las negativas) o almacenar el sentimiento como un atributo personalizado en su perfil para una futura orientación.

{% raw %}
```
You are a customer research AI for a retail brand.  
Input: one open-text survey response from a user.  
Output: A single structured JSON object with:  
- sentiment (Positive, Neutral, Negative)  
- topic (Product, Delivery, Price, Other)  
- action_recommendation (Route: High-priority follow-up | Low-priority follow-up | No action)  

Rules:  
- Always return valid JSON.  
- If the topic is unclear, default to Other.  
- If sentiment is mixed, default to Neutral.  
- If sentiment is Negative and topic = Product or Delivery → action_recommendation = High-priority follow-up.  
- Otherwise, action_recommendation = Low-priority follow-up.  

Example Input:  
"The product works great, but shipping took forever and the cost felt too high."  

Example Output:  
{  
  "sentiment": "Neutral",  
  "topic": "Delivery",  
  "action_recommendation": "High-priority follow-up"  
}  
```
{% endraw %}

Para más detalles sobre las mejores prácticas de incitación, consulta las guías de los siguientes proveedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Antrópico](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Géminis](https://support.google.com/a/users/answer/14200040?hl=en)

### Utilizar Liquid

Incluir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) en las instrucciones de tu agente puede añadir una capa extra de personalización en su respuesta. Puedes especificar la variable Liquid exacta que recibe el agente e incluirla en el contexto de tu consulta. Por ejemplo, en lugar de escribir explícitamente "nombre", puedes utilizar el fragmento de código Liquid {% raw %}`{{${first_name}}}`{% endraw %}:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

En la sección **Registros** de **la Consola del Agente**, puedes revisar los detalles de la entrada y salida del agente para comprender qué valor se obtiene del Liquid.

![Los datos de un agente que tiene Liquid en sus instrucciones.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:65%;"}

## Catálogos y campos

Elige catálogos específicos para que un agente los consulte y para dar a tu agente el contexto que necesita para entender tus productos y otros datos no relacionados con el usuario cuando sean relevantes. Los agentes utilizan herramientas para encontrar sólo los elementos relevantes y enviarlos al LLM para minimizar el uso de tokens.

![El catálogo "restaurantes" y la columna "Loyalty_Program" seleccionados para que el agente realice la búsqueda.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

## Contexto de pertenencia a un segmento

Puedes seleccionar hasta tres segmentos para que el agente compare la pertenencia a un segmento de cada usuario cuando el agente se utilice en un Canvas. Supongamos que tu agente tiene seleccionada la pertenencia a un segmento de "Usuarios fidelizados", y el agente se utiliza en un Canvas. Cuando los usuarios entran en un paso del Agente, éste puede cotejar si cada usuario es miembro de cada segmento que hayas especificado en la consola del Agente, y utilizar la pertenencia (o no pertenencia) de cada usuario como contexto para el LLM.

![El segmento "Usuarios fidelizados" seleccionado para el acceso de los agentes.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

## Directrices de marca

Puedes seleccionar [directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) para que tu agente se adhiera a ellas en sus respuestas. Por ejemplo, si quieres que tu agente genere un SMS para animar a los usuarios a registrarse en un gimnasio, puedes utilizar este campo para hacer referencia a tu directriz predefinida en negrita y motivadora.

## Temperatura

Si tu objetivo es utilizar un agente para generar textos que animen a los usuarios a entrar en tu aplicación móvil, puedes establecer una temperatura más alta para que tu agente sea más creativo y utilice los matices de las variables de contexto. Si utilizas un agente para generar puntuaciones de sentimiento, puede ser ideal establecer una temperatura más baja para evitar cualquier especulación del agente sobre las respuestas negativas de los cuestionarios. Te recomendamos que pruebes esta configuración y revises la salida generada por el agente para adaptarla a tu escenario.

{% alert note %}
Actualmente no es posible utilizar las temperaturas con OpenAI.
{% endalert %}
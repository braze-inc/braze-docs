---
nav_title: Crear agentes
article_title: Crear agentes personalizados
description: "Aprende a crear agentes, qué debes preparar antes de empezar y cómo ponerlos a trabajar en la mensajería, la toma de decisiones y la gestión de datos."
alias: /creating-agents/
---

# Crear agentes personalizados

> Aprende a crear agentes personalizados, qué debes preparar antes de empezar y cómo ponerlos a trabajar en mensajería, toma de decisiones y administración de datos. Para más información general, consulta [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Los Agentes Braze están actualmente en fase beta. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

- Acceso a la **Consola del Agente** en tu espacio de trabajo. Consulta con tus administradores de Braze si no ves esta opción.  
- Permiso para crear y editar Agentes AI personalizados. 
- Una idea de lo que quieres que consiga el agente. Los Agentes Braze pueden realizar las siguientes acciones:  
   - **Mensajería:** Genera líneas del asunto, titulares, textos dentro del producto u otros contenidos.  
   - **Toma de decisiones:** Dirige a los usuarios en Canvas en función de su comportamiento, preferencias o atributos personalizados.  
   - **Gestión de datos:** Calcula valores, enriquece entradas del catálogo o actualiza campos del perfil.  

## Cómo funciona

Cuando creas un agente, defines su finalidad y estableces los límites de su comportamiento. Una vez en vivo, el agente puede desplegarse en Braze para generar copias personalizadas, tomar decisiones en tiempo real o actualizar los campos del catálogo. Puedes pausar o actualizar un agente en cualquier momento desde el panel.

## Crear un agente

Para crear tu agente personalizado:  

1. Ve a **Consola de Agente** > **Gestión de Agente** en el panel de Braze.  
2. Selecciona **Crear agente**.  
3. Introduce un nombre y una descripción para ayudar a tu equipo a entender su finalidad.  
4. Elige el [modelo](#models) que utilizará tu agente.  

\![Interfaz de la Consola de Agentes para crear un agente personalizado en Braze. La pantalla muestra campos para introducir el nombre y la descripción del agente, y para seleccionar un modelo.]( {% image_buster /assets/img/ai_agent/create_custom_agent.png %} )

5. Da instrucciones al agente. Consulta [las Instrucciones de escritura](#writing-instructions) para orientarte.
6. [Prueba la](#testing-your-agent) salida [del agente](#testing-your-agent) y ajusta las instrucciones según sea necesario.
7. Cuando estés listo, selecciona **Crear Agente** para activar el agente. 

## Siguiente paso

¡Tu agente ya está listo para usar! Para más detalles, consulta [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/). 

## Referencia

### Modelos

Cuando configures un agente, elegirás el modelo que utiliza para generar respuestas. Tienes dos opciones:

#### Opción 1: Utiliza un modelo accionado por Braze

Esta es la opción más sencilla, sin necesidad de configuración adicional. Braze proporciona acceso directo a grandes modelos lingüísticos (LLM). Para utilizar esta opción, selecciona **Auto.**

{% alert note %}
Si utilizas el LLM impulsado por Braze, no incurrirás en ningún coste durante el periodo Beta. La invocación está limitada a 50.000 ejecuciones diarias y 500.000 ejecuciones en total. Consulta [Limitaciones]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) para más detalles.
{% endalert %}

#### Opción 2: Trae tu propia clave de API

Con esta opción, puedes conectar tu cuenta de Braze con proveedores como OpenAI, Anthropic, AWS Bedrock o Google Gemini. Si traes tu propia clave de API de un proveedor de LLM, los costes se facturan directamente a través de tu proveedor, no de Braze.

Para configurarlo:
1. Ve a **Integraciones de socios** > **Socios tecnológicos** y encuentra a tu proveedor.
2. Introduce tu clave de API del proveedor.
3. Selecciona **Guardar**.

Después, puedes volver a tu agente y seleccionar tu modelo.

### Instrucciones de escritura

Las instrucciones son las normas o directrices que das al agente (indicación del sistema). Definen cómo debe comportarse el agente cada vez que se ejecuta. Las instrucciones del sistema pueden ser de hasta 10 KB.

{% tabs %}
{% tab Best practices %}

Estas son algunas de las mejores prácticas generales para empezar con la incitación:

1. Empieza pensando en el final. Enuncia primero el objetivo.
2. Dale al modelo un papel o personaje ("Eres un ...").
3. Establece un contexto y unas limitaciones claras (audiencia, duración, tono, formato).
4. Pide estructura ("Devuelve JSON/lista de viñetas/tabla...").
5. Muestra, no cuentes. Incluye algunos ejemplos de alta calidad.
6. Divide las tareas complejas en pasos ordenados ("Paso 1... Paso 2...").
7. Fomenta el razonamiento ("Piensa en voz alta, luego responde").
8. Pilota, inspecciona e itera. Pequeños ajustes pueden dar lugar a grandes ganancias de calidad.
9. Trata los casos extremos, añade guardarraíles y añade instrucciones de rechazo.
10. Mide y documenta lo que funciona internamente para su reutilización y ampliación.

Para más detalles sobre las mejores prácticas de incitación, consulta las guías de los siguientes proveedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Antrópico](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Géminis](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

Este ejemplo de consulta toma la entrada de un cuestionario y genera un sencillo análisis de sentimientos:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

Este mensaje de ejemplo toma la entrada de un cuestionario de un usuario y la clasifica en una única etiqueta de sentimiento. El resultado puede utilizarse para dirigir a los usuarios por diferentes rutas de Canvas (como las opiniones positivas frente a las negativas) o almacenar el sentimiento como un atributo personalizado en su perfil para una futura orientación.

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
{% enddetails %}

{% endtab %}
{% endtabs %}


#### Pon a prueba a tu agente  

El panel de **vista previa en vivo** es una instancia del agente que se muestra como un panel en paralelo dentro de la experiencia de configuración. Puedes utilizarlo para probar el agente mientras lo creas o lo actualizas para experimentarlo de forma similar a los usuarios finales. Este paso te ayuda a confirmar que se comporta como esperas y te da la oportunidad de hacer ajustes antes de que salga en vivo.

La Consola del Agente muestra el panel de vista previa en vivo para probar un agente personalizado. La interfaz muestra un campo de entradas de ejemplo con datos de clientes de ejemplo, un botón Ejecutar prueba y un área de respuesta donde aparece la salida del agente.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. En el campo **Entradas de ejemplo**, introduce datos de clientes de ejemplo o respuestas de clientes: cualquier cosa que refleje escenarios reales que tu agente vaya a manejar. 
2. Selecciona **Ejecutar prueba**. El agente se ejecutará en función de tu configuración y mostrará su respuesta. Las ejecuciones de prueba cuentan para tu límite diario y total de invocaciones.

Revisa los resultados con ojo crítico. Considera las siguientes preguntas:

- ¿El texto parece de marca? 
- ¿La lógica de decisión dirige a los clientes según lo previsto? 
- ¿Son exactos los valores calculados? 

Si algo te parece mal, actualiza la configuración del agente y vuelve a probar. Ejecuta unas cuantas entradas diferentes para ver cómo se adapta el agente a los distintos escenarios, especialmente a casos extremos como la ausencia de datos o las respuestas no válidas.


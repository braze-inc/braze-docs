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

Los siguientes casos de uso muestran algunas formas de aprovechar los agentes personalizados.

| Casos de uso | Descripción |
| --- | --- |
| Gestión de las opiniones de los clientes | Pasa las opiniones de los usuarios a un agente para que analice el sentimiento y genere mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente puede intensificar la respuesta o incluir ventajas. |
| Localización de contenidos | Traduce el texto del catálogo a otro idioma para campañas globales, o ajusta el tono y la longitud para canales específicos de una región. Por ejemplo, traduce "Gafas de sol Classic Clubmaster" al español como "Gafas de sol Classic Clubmaster", o acorta las descripciones de las campañas por SMS. |
| Resume las opiniones o comentarios | Resume el sentimiento o las opiniones en un nuevo campo, como asignar puntuaciones de sentimiento como Positivo, Neutral o Negativo, o crear un breve resumen de texto como "La mayoría de los clientes mencionan un gran ajuste, pero notan lentitud en el envío". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Crear un agente

Para crear tu agente personalizado:  

1. Ve a **Consola de Agente** > **Gestión de Agente** en el panel de Braze.  
2. Selecciona **Crear agente**.  
3. Introduce un nombre y una descripción para ayudar a tu equipo a entender su finalidad.
4. Elige el [modelo](#models) que utilizará tu agente.  

![Interfaz de la Consola de Agente para crear un agente personalizado en Braze. La pantalla muestra campos para introducir el nombre y la descripción del agente, y para seleccionar un modelo.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Da instrucciones al agente. Consulta [las Instrucciones de escritura](#writing-instructions) para orientarte.
6\. [Prueba la](#testing-your-agent) salida [del agente](#testing-your-agent) y ajusta las instrucciones según sea necesario.
7\. Cuando estés listo, selecciona **Crear Agente** para activar el agente. 

¡Tu agente ya está listo para usar! Para más detalles, consulta [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Modelos

Cuando configuras un agente, puedes elegir el modelo que utiliza para generar respuestas. Tienes dos opciones: utilizar un modelo potenciado por Braze o aportar tu propia clave de API.

{% alert important %}
Al utilizar el modelo **Auto** potenciado por Braze, hemos optimizado los modelos cuya capacidad de pensamiento es suficiente para realizar tareas como la búsqueda de catálogos y la pertenencia a segmentos de usuarios. Cuando utilices otros modelos, te recomendamos que hagas pruebas para confirmar que tu modelo funciona bien para tu caso de uso. Puede que tengas que ajustar tus [instrucciones](#writing-instructions) para dar diferentes niveles de detalle o paso a paso a modelos con diferentes velocidades y capacidades.
{% endalert %}

### Opción 1: Utiliza un modelo accionado por Braze

Esta es la opción más sencilla, sin necesidad de configuración adicional. Braze proporciona acceso directo a grandes modelos lingüísticos (LLM). Para utilizar esta opción, selecciona **Auto**, que utiliza los modelos Gemini.

### Opción 2: Trae tu propia clave de API

Con esta opción, puedes conectar tu cuenta de Braze con proveedores como OpenAI, Anthropic, AWS Bedrock o Google Gemini. Si traes tu propia clave de API de un proveedor de LLM, los costes del token se facturan directamente a través de tu proveedor, no de Braze.

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
7. Fomenta el razonamiento ("Piensa en voz alta, luego responde").
8. Pilota, inspecciona e itera. Pequeños ajustes pueden dar lugar a grandes ganancias de calidad.
9. Trata los casos extremos, añade guardarraíles y añade instrucciones de rechazo.
10. Mide y documenta lo que funciona internamente para su reutilización y ampliación.

Recomendamos incluir también un predeterminado como respuesta comodín si el agente recibe una respuesta que no se puede analizar. Este tratamiento de errores permite al agente informarte de una variable de resultado desconocida. Por ejemplo, en lugar de pedir al agente sólo valores de sentimiento "positivos" o "negativos", pídele que devuelva "inseguro" si no puede decidir.

### Aviso simple

Este ejemplo de consulta toma la entrada de un cuestionario y genera un sencillo análisis de sentimientos:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

### Aviso complejo 

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

Para más detalles sobre las mejores prácticas de incitación, consulta las guías de los siguientes proveedores de modelos:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Antrópico](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Géminis](https://support.google.com/a/users/answer/14200040?hl=en)

### Formato de salida

Utiliza el campo **Formato de salida** para organizar y definir la salida del agente estructurando manualmente los campos o utilizando JSON. 

- **Campos:** Una forma sin código de imponer una salida de agente que puedes utilizar de forma coherente. 
- **JSON:** Un enfoque de código para crear un formato de salida preciso, en el que puedes anidar variables y objetos dentro del esquema JSON.

#### Campos

Supongamos que quieres formatear las respuestas a un cuestionario sencillo para determinar la probabilidad de que los encuestados recomienden el nuevo sabor de helado de tu restaurante. Puedes configurar los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor
| --- | --- |
| **likelihood_score** | Número |
| **explicación** | Texto |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![La Consola del Agente muestra tres campos de salida para la puntuación de probabilidad, la explicación y la puntuación de confianza.]( {% image_buster /assets/img/ai_agent/output_format_fields.png %} )

### Esquema JSON

Supongamos que quieres recoger las opiniones de los usuarios sobre su experiencia gastronómica más reciente en tu cadena de restaurantes. Podrías seleccionar **Esquema JSON** como formato de salida e insertar el siguiente JSON para devolver un objeto de datos que incluya una variable de sentimiento y una variable de razonamiento.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

Si intentas utilizar un agente con una salida JSON en un catálogo, no seguirá tu esquema. En su lugar, considera la posibilidad de utilizar los [campos de salida definidos](#fields).

{% alert important %}
Los formatos de salida no son compatibles actualmente con Claude AI. Si utilizas una clave antrópica, te recomendamos que añadas manualmente la estructura a la consulta del agente.
{% endalert %}

## Configuraciones opcionales

### Directrices de marca

Puedes seleccionar [directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) para que tu agente se adhiera a ellas en sus respuestas. Por ejemplo, si quieres que tu agente genere un SMS para animar a los usuarios a registrarse en un gimnasio, puedes utilizar este campo para hacer referencia a tu directriz predefinida en negrita y motivadora.

### Catálogos

Elige catálogos específicos para que un agente los consulte y para dar a tu agente el contexto que necesita para entender tus productos y otros datos no relacionados con el usuario cuando sean relevantes.

![El catálogo "restaurantes" y la columna "Loyalty_Program" seleccionados para que el agente realice la búsqueda.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:85%;"}

### Contexto de pertenencia a un segmento

Puedes seleccionar hasta tres segmentos para que el agente compare la pertenencia a un segmento de cada usuario cuando el agente se utilice en un Canvas. Supongamos que tu agente tiene seleccionada la pertenencia a un segmento de "Usuarios fidelizados", y el agente se utiliza en un Canvas. Cuando los usuarios entran en un paso del Agente, éste puede cotejar si cada usuario es miembro de cada segmento que hayas especificado en la consola del Agente, y utilizar la pertenencia (o no pertenencia) de cada usuario como contexto para el LLM.

![El segmento "Usuarios fidelizados" seleccionado para el acceso de los agentes.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:85%;"}

### Temperatura

Si tu objetivo es utilizar un agente para generar textos que animen a los usuarios a entrar en tu aplicación móvil, puedes establecer una temperatura más alta para que tu agente sea más creativo y utilice los matices de las variables de contexto. Si utilizas un agente para generar puntuaciones de sentimiento, puede ser ideal establecer una temperatura más baja para evitar cualquier especulación del agente sobre las respuestas negativas de los cuestionarios. Te recomendamos que pruebes esta configuración y revises la salida generada por el agente para adaptarla a tu escenario.

{% alert note %}
Actualmente no es posible utilizar las temperaturas con OpenAI.
{% endalert %}

## Pon a prueba a tu agente

El panel de **vista previa en vivo** es una instancia del agente que se muestra como un panel en paralelo dentro de la experiencia de configuración. Puedes utilizarlo para probar el agente mientras lo creas o lo actualizas para experimentarlo de forma similar a los usuarios finales. Este paso te ayuda a confirmar que se comporta como esperas y te da la oportunidad de hacer ajustes antes de que salga en vivo.

![La Consola del Agente muestra el panel de vista previa en vivo para probar un agente personalizado. La interfaz muestra un campo de entradas de muestra con datos de clientes de ejemplo, un botón Ejecutar prueba y un área de respuesta donde aparece la salida del agente.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. En el campo **Entradas de ejemplo**, introduce datos de clientes de ejemplo o respuestas de clientes: cualquier cosa que refleje escenarios reales que tu agente vaya a manejar. 
2. Selecciona **Ejecutar prueba**. El agente se ejecutará en función de tu configuración y mostrará su respuesta. Las ejecuciones de prueba cuentan para tu límite diario de ejecuciones.

Revisa los resultados con ojo crítico. Considera las siguientes preguntas:

- ¿El texto parece de marca? 
- ¿La lógica de decisión dirige a los clientes según lo previsto? 
- ¿Son exactos los valores calculados? 

Si algo te parece mal, actualiza la configuración del agente y vuelve a probar. Ejecuta algunas entradas diferentes para ver cómo se adapta el agente a los distintos escenarios, especialmente en casos extremos como la ausencia de datos o las respuestas no válidas.

### Controla a tu agente

En la pestaña **Registros** de tu agente, puedes controlar las llamadas reales del agente que se producen en tus Lienzos y catálogos. Puedes filtrar por información como el intervalo de fechas, el resultado (éxito o fracaso) o la ubicación de la llamada.

![Registros de un agente Asignación aleatoria de deportes, que incluyen cuándo y dónde se ha llamado al agente.]( {% image_buster /assets/img/ai_agent/agent_activity_logs.png %} )

Selecciona **Ver** para una llamada de agente concreta para ver la entrada, la salida y el ID de usuario.

![Registros de un agente Tendencias de la ciudad y Reserva de recomendaciones. El panel de detalles muestra la solicitud de entrada, la respuesta de salida y un ID de usuario asociado.]( {% image_buster /assets/img/ai_agent/agent_logs.png %} )

---
nav_title: Crear agentes
article_title: Crear agentes personalizados
description: "Aprende a crear agentes, qué debes preparar antes de empezar y cómo ponerlos a trabajar en mensajería, toma de decisiones y gestión de datos."
page_order: 1
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
   - **Toma de decisiones:** Enruta a los usuarios en Canvas en función de su comportamiento, preferencias o atributos personalizados.  
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

### Paso 1: Detalles de configuración

Para crear tu agente personalizado:

1. Ve a **Consola de Agente** > **Gestión de Agente** en el panel de Braze.  
2. Selecciona **Crear agente**.
3. Introduce un nombre y una descripción para ayudar a tu equipo a entender su finalidad.
4. (opcional) Añade etiquetas para filtrar tu agente.
5. Selecciona el lugar de interacción, que es la ubicación donde está desplegado el agente. Ten en cuenta que el sitio de interacción no se puede actualizar después de crear un agente.
6. Elige el [modelo]({{site.baseurl}}/docs/user_guide/brazeai/agents/reference/#models) que utilizará tu agente.

![Interfaz de la Consola de Agente para crear un agente personalizado en Braze. La pantalla muestra campos para introducir el nombre y la descripción del agente, y para seleccionar un modelo.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:85%;"}

### Paso 2: Escribe las instrucciones

Da instrucciones al agente. Consulta [la referencia de los Agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/) para orientarte.

{% alert tip %}
Puedes utilizar Liquid en tus instrucciones para hacer referencia a atributos del usuario, como su nombre y apellidos, o atributos personalizados.
{% endalert %}

#### Paso 2.1: Añadir contexto

Selecciona **Añadir contexto** para elegir a qué puede hacer referencia tu agente. Esto incluye lo siguiente:

- [Campos del catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Proporciona campos de catálogo para que el agente los consulte.
- [Pertenencia a segmentos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Ten en cuenta la pertenencia de un usuario a un segmento a la hora de personalizar los mensajes. Puedes seleccionar hasta tres segmentos.
- [Directrices de la marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Haz referencia a la voz de la marca y a las directrices de estilo que debe seguir el agente. Por ejemplo, si quieres que tu agente genere un SMS para animar a los usuarios a registrarse en un gimnasio, puedes utilizar este campo para hacer referencia a tu directriz predefinida en negrita y motivadora.
- [Variables de contexto del Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analiza todas las variables del Contexto Canvas de un usuario cuando se invoca a este agente.

#### Paso 2.2: Añadir configuración opcional

En la **configuración Opcional**, puedes ajustar la [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) de la copia generada por el agente. Una temperatura más alta permite al agente utilizar la información proporcionada para ser más creativo.

También puedes establecer el límite de ejecución diaria de tu agente. Por defecto, este valor está predeterminado a 50.000, pero puede aumentarse a 100.000. Si estás interesado en aumentar el límite por encima de 100.000, ponte en contacto con tu administrador del éxito del cliente para obtener más información.

### Paso 3: Selecciona la salida

En la sección **Salida**, puedes organizar y definir la salida del agente por esquemas básicos o esquemas avanzados.

#### Esquemas básicos

Los esquemas básicos son una salida simple que devuelve un agente. Puede ser una cadena, un número, un booleano, una matriz de cadenas o una matriz de números.

Supongamos que quieres recopilar las puntuaciones de los sentimientos de los usuarios a partir de un simple cuestionario para determinar el grado de satisfacción de tus clientes tras recibir un producto. Puedes seleccionar **Número** como esquema básico para estructurar el formato de salida.

{% alert important %}
Las matrices sólo están disponibles para los agentes Canvas, no para los agentes catálogo.
{% endalert %}

![Consola de Agente con el número seleccionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Esquemas avanzados

Las opciones avanzadas de esquema incluyen la estructuración manual de los campos o el uso de JSON.

- **Campos:** Una forma sin código de imponer una salida de agente que puedes utilizar de forma coherente. 
- **JSON:** Un enfoque de código para crear un formato de salida preciso, en el que puedes anidar variables y objetos dentro del esquema JSON.

{% tabs %}
{% tab Fields %}

Supongamos que quieres formatear las respuestas a un cuestionario sencillo para determinar la probabilidad de que los encuestados recomienden el nuevo sabor de helado de tu restaurante. Puedes configurar los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor
| --- | --- |
| **likelihood_score** | Número |
| **explicación** | Texto |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![La Consola del Agente muestra tres campos de salida para la puntuación de probabilidad, la explicación y la puntuación de confianza.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

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

{% endtab %}
{% endtabs %}

### Paso 4: Prueba y crea el agente

El panel de **vista previa** es una instancia del agente que se muestra como un panel lateral dentro de la experiencia de configuración. Puedes utilizarlo para probar el agente mientras lo creas o lo actualizas para experimentarlo de forma similar a los usuarios finales. Este paso te ayuda a confirmar que se comporta como esperas y te da la oportunidad de hacer ajustes antes de que salga en vivo.

1. En el campo **Prueba tu agente**, introduce datos de clientes de ejemplo o respuestas de clientes: cualquier cosa que refleje escenarios reales que tu agente vaya a manejar.
2. Vista previa de la respuesta del agente para un usuario aleatorio, un usuario existente o un usuario personalizado.
3. Selecciona **Simular respuesta**. El agente se ejecutará en función de tu configuración y mostrará su respuesta. Las ejecuciones de prueba cuentan para tu límite diario de ejecuciones.

![La Consola del Agente muestra el panel Vista previa para probar un agente personalizado. La interfaz muestra un campo de entradas de ejemplo con datos de clientes de ejemplo, un botón Ejecutar prueba y un área de respuesta donde aparece la salida del agente.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revisa los resultados con ojo crítico. Considera las siguientes preguntas:

- ¿El texto parece de marca?
- ¿La lógica de decisión dirige a los clientes según lo previsto?
- ¿Son exactos los valores calculados?

Si algo te parece mal, actualiza la configuración del agente y vuelve a probar. Ejecuta algunas entradas diferentes para ver cómo se adapta el agente a los distintos escenarios, especialmente en casos extremos como la ausencia de datos o las respuestas no válidas.

### Paso 5: Utiliza y controla a tu agente

¡Tu agente ya está listo para usar! Para más detalles, consulta [Desplegar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

En la pestaña **Registros** de tu agente, puedes controlar las llamadas reales del agente que se producen en tus Lienzos y catálogos. Puedes filtrar por información como el intervalo de fechas, el resultado (éxito o fracaso) o la ubicación de la llamada.

![Registros de un agente Contador de Historias, que incluyen cuándo y dónde se ha llamado al agente.]({% image_buster /assets/img/ai_agent/agent_activity_logs.png %})

Selecciona **Ver** para una llamada de agente concreta para ver la entrada, la salida y el ID de usuario.

![Bitácoras para un agente Contador de historias. El panel de detalles muestra la solicitud de entrada, la respuesta de salida y un ID de usuario asociado.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

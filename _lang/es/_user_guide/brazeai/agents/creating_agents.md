---
nav_title: Crear agentes
article_title: Crear agentes personalizados
description: "Aprende a crear agentes, qué preparar antes de empezar y cómo ponerlos a trabajar en mensajería, toma de decisiones y gestión de datos."
page_order: 1
alias: /creating-agents/
---

# Crear agentes personalizados

> Aprende a crear agentes personalizados, qué preparar antes de empezar y cómo ponerlos en funcionamiento en mensajería, toma de decisiones y gestión de datos. Para obtener más información general, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents).

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

- [Permiso]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) para acceder a la **consola del agente** en tu espacio de trabajo. Consulta con tus administradores de Braze si no ves esta opción.  
- Permiso para crear y editar agentes de IA personalizados.
- Una idea de lo que quieres que logre el agente. Los agentes de Braze pueden realizar las siguientes acciones:  
   - **Mensajería:** Genera líneas del asunto, titulares, textos para productos u otro tipo de contenido.  
   - **Toma de decisiones:** Dirigid a los usuarios en Canvas en función de su comportamiento, preferencias o atributos personalizados.  
   - **Gestión de datos:** Calcula valores, mejora las entradas del catálogo o actualiza los campos del perfil.  

## Cómo funciona

Cuando creas un agente, defines su propósito y estableces las pautas sobre cómo debe comportarse. Una vez que esté en vivo, el agente se puede implementar en Braze para generar copias de personalización, tomar decisiones en tiempo real o actualizar campos del catálogo. Puedes pausar o actualizar un agente en cualquier momento desde el panel.

Los siguientes casos de uso muestran algunas formas de aprovechar los agentes personalizados.

| Casos de uso | Descripción |
| --- | --- |
| Gestión de los comentarios de los clientes | Transmite los comentarios de los usuarios a un agente para que analice el sentimiento y genere mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente podría escalar la respuesta o incluir ventajas adicionales. |
| Realizar la localización del contenido | Traduce el texto del catálogo a otro idioma para campañas globales o ajusta el tono y la longitud para canales específicos de cada región. Por ejemplo, traduce «Classic Clubmaster Sunglasses» al español como «Gafas de sol Classic Clubmaster» o acorta las descripciones para las campañas de SMS. |
| Resume las reseñas o comentarios. | Resume las opiniones o comentarios en un nuevo campo, por ejemplo, asignando puntuaciones como «Positivo», «Neutro» o «Negativo», o creando un breve resumen de texto como «La mayoría de los clientes mencionan que el producto se ajusta muy bien, pero señalan que el envío es lento». |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Crear un agente

### Paso 1: Elige un tipo de agente

Para crear tu agente personalizado:

1. Ve a **Consola del agente** > **Gestión de agentes** en el panel de Braze.  
2. Selecciona **Crear agente**.
3. Elige entre crear un agente Canvas o un agente de catálogo.

### Paso 2: Configurar detalles

A continuación, configura la configuración de tu agente:

1. Introduce un nombre y una descripción para ayudar a tu equipo a comprender su finalidad.
2. (opcional) Añade etiquetas para filtrar tu agente.
3. Elige el [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) que utilizará tu agente.
4. Selecciona el nivel de pensamiento del modelo. Puedes elegir entre mínimo, bajo, medio o alto. Te recomendamos que comiences con **Minimal**, pruebes las respuestas de tu agente y las ajustes según sea necesario.

![Interfaz de la consola de agente para crear un agente personalizado en Braze. La pantalla muestra campos para introducir el nombre y la descripción del agente, y seleccionar un modelo.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### Paso 3: Escribe las instrucciones. {#agent-instructions}

Dale instrucciones al agente. Recomendamos incluir instrucciones sobre lo que debe hacer el agente en situaciones inesperadas o ambiguas. Esto minimiza el riesgo de que la confusión de los agentes provoque errores. Por ejemplo, en lugar de pedirle al agente solo valores de sentimiento «positivos» o «negativos», pídele que devuelva «indeciso» si no puede decidir.

Consulta las [instrucciones]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) de [redacción]({{site.baseurl}}/user_guide/brazeai/agents/reference/#writing-instructions) para conocer las mejores prácticas y [los ejemplos]({{site.baseurl}}/user_guide/brazeai/agents/reference/#examples) para inspirarte sobre cómo dar instrucciones a tu agente.

{% alert tip %}
Para los agentes de Canvas, puedes utilizar Liquid en tus instrucciones para hacer referencia a los atributos de los usuarios, como su nombre y apellidos, o atributos personalizados. Cualquier variable Liquid en las instrucciones del agente se pasa automáticamente al paso del agente cuando un usuario ingresa al paso.
{% endalert %}

#### Paso 3.1: Añadir contexto

Selecciona **Añadir contexto** para elegir lo que tu agente puede consultar. Esto incluye lo siguiente:

- [Campos del catálogo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#catalogs-and-fields): Permite que el agente acceda a los datos de tu catálogo para obtener respuestas más precisas.
- [Pertenencia al segmento]({{site.baseurl}}/user_guide/brazeai/agents/reference/#segment-membership-context): Permite que el agente personalice las respuestas en función de los segmentos a los que pertenezca el usuario. Puedes seleccionar hasta cinco segmentos.
- [Directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines): Consulta las directrices sobre el tono y el estilo de la marca que debe seguir el agente. Por ejemplo, si deseas que tu agente genere un texto SMS para animar a los usuarios a que se registren en un gimnasio, puedes utilizar este campo para hacer referencia a tu directriz motivacional predefinida en negrita.
- [Todo el contexto de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables): Analiza todos los datos de contexto de Canvas de un usuario cuando se invoque este agente, incluidas las variables que no se mencionan en la sección **Instrucciones**.

#### Paso 3.2: Añadir configuraciones opcionales

En la **configuración opcional**, puedes ajustar la [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/reference/#temperature) de la copia generada por el agente. Una temperatura más alta permite al agente utilizar la información proporcionada para ser más creativo.

También puedes establecer el límite de ejecución diario para tu agente. De forma predeterminada, este valor está establecido en 250 000, pero puede aumentarse hasta 1 000 000. Si estás interesado en aumentar el límite por encima de 1 000 000, ponte en contacto con tu administrador del éxito del cliente para obtener más información.

### Paso 4: Selecciona la salida {#select-output}

En la sección **Salida**, puedes organizar y definir la salida del agente mediante esquemas básicos o esquemas avanzados.

Para obtener los mejores resultados, asegúrate de que lo que especifiques en la sección **Salida** coincida con las instrucciones del agente que ingresaste en [el paso 3](#agent-instructions). Por ejemplo, si en las instrucciones del agente mencionaste que deseas un objeto con dos cadenas, asegúrate de especificar un objeto con dos cadenas en la sección **Salida**. Si las instrucciones del agente no coinciden con el resultado especificado, el agente puede confundirse, agotar el tiempo de espera o generar resultados no deseados.

#### Esquemas básicos

Los esquemas básicos son una salida simple que devuelve un agente. Puede ser una cadena, un número, un booleano, una matriz de cadenas o una matriz de números.

Por ejemplo, si deseas recopilar puntuaciones sobre la opinión de los usuarios a partir de un sencillo cuestionario de satisfacción para determinar el grado de satisfacción de tus clientes tras recibir un producto, puedes seleccionar **Número** como esquema básico para estructurar el formato de salida.

{% alert important %}
Las matrices solo están disponibles para los agentes Canvas, no para los agentes de catálogo.
{% endalert %}

![Consola de agente con el número seleccionado como esquema básico.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

#### Esquemas avanzados

Las opciones avanzadas del esquema incluyen la estructuración manual de campos o el uso de JSON.

- **Campos:** Una forma sin código de aplicar una salida de agente que puedes utilizar de forma coherente.
- **JSON:** Un enfoque de código para crear un formato de salida preciso, en el que puedes anidar variables y objetos dentro del esquema JSON. Solo disponible para agentes de Canvas, no para agentes de catálogo.

Recomendamos utilizar esquemas avanzados cuando desees que el agente devuelva una estructura de datos con múltiples valores definidos de forma estructurada, en lugar de una salida de un solo valor. Esto permite que la salida se formatee mejor como una variable de contexto coherente.

Por ejemplo, puedes utilizar un formato de salida dentro de un agente destinado a crear un itinerario de viaje de muestra para un usuario basándose en un formulario que haya enviado. El formato de salida permite definir que cada respuesta del agente debe devolver valores para `tripStartDate`,  `tripEndDate`y`destination`. Cada uno de estos valores se puede extraer de las variables de contexto y colocarse en un paso de mensaje para realizar la personalización con Liquid.

{% tabs %}
{% tab Fields %}

Si deseas dar formato a las respuestas de un cuestionario sencillo para determinar la probabilidad de que los encuestados recomienden el nuevo sabor de helado de tu restaurante, puedes configurar los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor |
| --- | --- |
| **likelihood_score** | Número |
| **explicación** | Cadena |
| **confidence_score** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Consola del agente que muestra tres campos de salida para la puntuación de probabilidad, la explicación y la puntuación de confianza.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON schema %}

Si deseas recopilar comentarios de los usuarios sobre su experiencia gastronómica más reciente en tu cadena de restaurantes, puedes seleccionar **JSON Schema** como formato de salida e insertar el siguiente JSON para devolver un objeto de datos que incluya una variable de opinión y una variable de razonamiento.

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

### Paso 5: Prueba y crea el agente.

El panel **de vista previa** es una instancia del agente que aparece como un panel lateral dentro de la experiencia de configuración. Puedes utilizarlo para probar el agente mientras lo creas o actualizas, con el fin de experimentarlo de forma similar a como lo harían los usuarios finales. Este paso te ayuda a confirmar que funciona como esperabas y te da la oportunidad de realizar ajustes antes de que entre en funcionamiento.

1. En el campo **Prueba tu agente**, introduce datos de clientes o respuestas de clientes de ejemplo, cualquier cosa que refleje situaciones reales que tu agente tendrá que gestionar.
2. Previsualiza la respuesta del agente para un usuario aleatorio, un usuario existente o un usuario personalizado.
3. Selecciona **Simular respuesta**. El agente se ejecutará según tu configuración y mostrará su respuesta. Las ejecuciones de prueba cuentan para tu límite de ejecución diario.

![Consola del agente que muestra el panel de vista previa para probar un agente personalizado. La interfaz muestra un campo de entradas de muestra con datos de clientes de ejemplo, un botón Ejecutar prueba y un área de respuesta donde aparece la salida del agente.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

Revisa el resultado con ojo crítico. Considera las siguientes preguntas:

- ¿El texto se ajusta a la imagen de marca?
- ¿La lógica de decisión dirige a los clientes según lo previsto?
- ¿Son precisos los valores calculados?

Si algo no funciona correctamente, actualiza la configuración del agente y vuelve a realizar la prueba. Ejecuta varias entradas diferentes para ver cómo se adapta el agente a distintos escenarios, especialmente en casos extremos como la ausencia de datos o respuestas no válidas.

{% alert tip %}
Evita decirle al agente exactamente lo que no quieres que haga. Los LLM pueden seguir generando ese contenido si lo mencionas en las instrucciones.
{% endalert %}

### Paso 6: Utiliza tu agente

¡Tu agente ya está listo para usar! Para obtener más información, consulta [Implementar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/).

## Artículos relacionados  

- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)

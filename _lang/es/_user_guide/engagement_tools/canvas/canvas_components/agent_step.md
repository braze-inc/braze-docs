---
nav_title: Agente
article_title: Paso de agente
alias: /agent_step/
page_order: 2
page_type: reference
description: "Este artículo de referencia explica cómo utilizar el paso Agente en Canvas para generar contenido o tomar decisiones inteligentes en tiempo real."
tool: Canvas
toc_headers: h2
---

# Paso del agente  

> El paso Agente te permite añadir la toma de decisiones y la generación de contenido basadas en IA directamente en tu flujo de trabajo de Canvas. Para obtener más información general, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Un paso de agente en el recorrido del usuario de Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Cómo funciona

Cuando un usuario llega a un paso de agente en un Canvas, Braze envía los datos de entrada que has configurado (contexto completo o campos seleccionados) al agente que hayas elegido. A continuación, el agente procesa la entrada utilizando su modelo y sus instrucciones, y devuelve una salida. Ese resultado se almacena en la variable de salida que has definido en el paso.

A continuación, puedes utilizar esta variable de tres formas principales:

- **Toma de decisiones:** Dirigir a los usuarios por diferentes rutas de Canvas en función de la respuesta del agente. Por ejemplo, un agente de puntuación de clientes potenciales podría devolver un número entre 1 y 10. Puedes utilizar esta puntuación para decidir si continuar con la mensajería hacia un usuario o eliminarlo del recorrido.
- **Personalización:** Inserta la respuesta del agente directamente en un mensaje. Por ejemplo, un agente podría analizar los comentarios de los clientes y generar un correo electrónico de seguimiento empático que haga referencia al comentario del cliente y sugiera una solución.
- **Tratamiento de los datos de usuario:** Analiza y estandariza los datos de usuario, luego guárdalos en el perfil de usuario o envíalos mediante un webhook. Por ejemplo, un agente podría devolver una puntuación de sentimiento o una asignación de afinidad con el producto. Puedes almacenar esos datos en un perfil de usuario para su uso futuro.

## Requisito previo

Los pasos del agente utilizan [variables de contexto de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) para incorporar el contexto relevante y generar una variable que se puede aprovechar en Canvas.

## Creación de un paso de agente

### Paso 1: Añadir un paso

Arrastrar y soltar el componente **Agente** desde la barra lateral, o selecciona el botón<i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Agente**.  

### Paso 2: Elige a tu agente  

Selecciona el agente que procesará los datos en este paso. Elige un agente existente. Para obtener orientación sobre la configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Paso 3: Configura la salida de tu agente {#define-the-output-variable}

Las salidas del agente se denominan «variables de salida» y se almacenan en una [variable de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) para facilitar su acceso. Para definir la variable de salida, asigna un nombre a la variable.

Nota: El tipo de datos de la variable de salida se configura desde la [consola del agente]({{site.baseurl}}/user_guide/brazeai/agents). Las salidas del agente se pueden guardar como cadenas, números, booleanos u objetos. Esto los hace flexibles tanto para la personalización de texto como para la lógica condicional en tu Canvas. A continuación, se indican algunos usos comunes para cada tipo:

| Tipo de datos | Usos comunes |
| --- | --- |
| Cadena | Personalización de mensajes (líneas del asunto, texto, respuestas) |
| Número | Puntuación, umbrales y enrutamiento en [rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booleano | Ramificación Sí/No en [divisiones de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objeto | Aprovecha uno o varios de los tipos de datos anteriores con una sola llamada LLM en una estructura de datos predecible. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puedes utilizar una variable de salida en todo Canvas utilizando la misma sintaxis de plantilla que utilizarías con una variable de contexto. Utiliza el filtro de segmento **Variable de contexto** o crea respuestas de agente directamente con Liquid:{% raw %}`{{context.${response_variable_name}}}` {% endraw %} .

Para utilizar una propiedad específica de una variable de salida de objeto, utiliza la notación de punto para acceder a esa propiedad mediante Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Paso de agente para Body HTML Writer con una salida de tipo de datos de objeto para la variable/assets/img/ai_agent/test_agent_step.pngimage_buster"agent_output".]({%%}){: style="max-width:80%;"}

### Paso 4: Añade cualquier contexto adicional (opcional)

Puedes decidir incluir valores de contexto adicionales para que el paso del agente los consulte cuando se ejecute. Puedes introducir cualquier valor de plantilla Liquid que utilizarías normalmente en un Canvas.

{% alert note %}
Nota: El agente ya está recibiendo automáticamente el contexto configurado en la sección **Instrucciones**. Las variables líquidas que ya estaban configuradas allí no es necesario volver a introducirlas aquí.
{% endalert %}

![La opción de añadir contexto adicional a un paso de agente utilizando Liquid.]({% image_buster /assets/img/ai_agent/agent_step_context.png %}){: style="max-width:80%;"}

### Paso 5: Prueba el agente

Después de configurar el paso Agente, puedes probar y obtener una vista previa del resultado de este paso.

![Realiza una vista previa de la salida del agente como un usuario aleatorio.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## Tratamiento de errores  

- Si el modelo conectado devuelve un error de límite de velocidad, Braze vuelve a intentarlo hasta cinco veces con retirada exponencial.  
- Si el agente falla por cualquier otro motivo (como un error de tiempo de espera o una clave de API no válida), la variable de salida se establece en `null`.
    - Si un agente alcanza su límite diario de invocaciones, la variable de salida se establece en `null`. Si utilizas la salida de un agente en un paso de mensaje, considera la posibilidad de utilizar [valores Liquid predeterminados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values).
- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en unos pocos minutos.
    - Las respuestas que utilizan valores almacenados en caché siguen contando para el total y las invocaciones diarias.

## Análisis  

Consulta las siguientes métricas para realizar el seguimiento del rendimiento de tus pasos de agente:  

| Métrica | Descripción |
| --- | --- |
| _El usuario ha entrado_ | El número de veces que los usuarios han accedido al paso Agente. |
| _Continúa con el paso siguiente_ | El número de usuarios que pasaron al siguiente paso del flujo después de pasar por el paso del agente. |
| _Has salido de Canvas_ | El número de usuarios que salieron del Canvas después de pasar por el paso del Agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas más frecuentes

### ¿Cuándo debo utilizar un paso de agente?

En general, recomendamos utilizar un paso de agente cuando se desea introducir datos contextuales concretos en un LLM y que este asigne de forma inteligente una variable de contexto de Canvas a una escala imposible para los seres humanos.

Supongamos que envías un mensaje personalizado para recomendar un nuevo sabor de helado a un usuario que anteriormente pidió chocolate y fresa. Esta es la diferencia entre utilizar un paso de agente y las recomendaciones de artículos basadas en IA:

- **Paso del agente:** Utiliza modelos de lenguaje grande (LLM) para tomar una decisión cualitativa sobre lo que el usuario podría querer basándose en las instrucciones y los puntos de datos contextuales proporcionados al agente. En este ejemplo, un paso del agente podría recomendar un nuevo sabor basándose en la posibilidad de que el usuario quiera probar diferentes sabores.
- **Recomendaciones de artículos basadas en IA:** Utiliza modelos de aprendizaje automático para predecir los productos que más probablemente te interesarán en función de tus acciones anteriores, como las compras. En este ejemplo, las recomendaciones de artículos de IA sugerirían un sabor (vainilla) basándose en los dos pedidos anteriores del usuario (chocolate y fresa) y en cómo estos se comparan con los comportamientos de otros usuarios de tu espacio de trabajo.

### ¿Cómo utilizan los pasos del agente los datos de entrada?

Un paso de agente analiza los datos de contexto que tú estás configurado para utilizar, así como cualquier contexto adicional que se [te proporcione](#step-4-add-any-additional-context-optional).

## Artículos relacionados  

- [Resumen de Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Implementar agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)  
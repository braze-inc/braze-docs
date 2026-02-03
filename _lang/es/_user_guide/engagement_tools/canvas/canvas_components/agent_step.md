---
nav_title: Agente
article_title: Paso de agente
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "Este artículo de referencia explica cómo utilizar el paso en Canvas del Agente para generar contenido o tomar decisiones inteligentes en tiempo real."
tool: Canvas
toc_headers: h2
---

# Paso de agente  

> El paso en Canvas te permite añadir la toma de decisiones y la generación de contenidos con IA directamente a tu flujo de trabajo en Canvas. Para más información general, consulta [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

![Un paso de Agente en un recorrido de usuario de Canvas.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Cómo funciona

Cuando un usuario llega a un paso en Canvas, Braze envía los datos de entrada que hayas configurado (contexto completo o campos seleccionados) al agente que hayas elegido. A continuación, el agente procesa la entrada utilizando su modelo e instrucciones, y devuelve una salida. Esa salida se almacena en la variable de salida que definiste en el paso.

A continuación, puedes utilizar esta variable de dos formas principales:

- **Toma de decisiones:** Dirige a los usuarios por diferentes rutas Canvas en función de la respuesta del agente. Por ejemplo, un agente de puntuación de clientes potenciales podría devolver un número entre 1 y 10. Puedes utilizar esta puntuación para decidir si continúas enviando mensajes a un usuario o lo abandonas del viaje.
- **Personalización:** Inserta la respuesta del agente directamente en un mensaje. Por ejemplo, un agente podría analizar la opinión de un cliente y generar un correo electrónico de seguimiento empático que haga referencia al comentario del cliente y sugiera una solución.

## Crear un paso de Agente

### Paso 1: Añade un paso

Arrastra y suelta el componente **Agente** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Agente**.  

### Paso 2: Selecciona tu agente  

Selecciona el agente que procesará los datos en este paso. Elige un agente existente, o crea uno nuevo directamente desde este paso. Para obtener instrucciones de configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Paso 3: Define la variable de salida

Las salidas de los agentes se denominan "variables de salida" y se almacenan en una [variable de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) para facilitar su acceso. Para definir la variable de salida:

1. Dale un nombre a la variable.
2. Selecciona un tipo de datos. 

Las salidas del agente pueden guardarse como cadenas, números, booleanos u objetos. Esto los hace flexibles tanto para la personalización del texto como para la lógica condicional en tu Canvas. He aquí algunos usos comunes de cada tipo:

| Tipo de datos | Usos comunes |
| --- | --- |
| Cadena | Personalización de mensajes (líneas del asunto, copia, respuestas) |
| Número | Puntuación, umbrales, enrutamiento en [Rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booleano | Sí/No ramificación en [divisiones de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
| Objeto | Aprovecha uno o varios de los tipos de datos anteriores con una sola llamada LLM en una estructura de datos predecible |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Una vez definida, puedes utilizar una variable de salida en todo el Canvas utilizando la misma sintaxis de plantilla que con una variable de contexto. Utiliza el filtro de segmentos **de la Variable de Contexto** o plantilla las respuestas de los agentes directamente con Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

Para utilizar una propiedad concreta de una variable de salida de un objeto, utiliza la notación con puntos para acceder a esa propiedad mediante Liquid: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![Paso de agente para Body HTML Writer con una salida de tipo de datos de objeto para la variable "agent_output".]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

Utiliza los patrones de sintaxis Liquid mostrados anteriormente para hacer referencia a campos concretos de la salida del agente en futuros pasos en Canvas.

### Paso 4: Decide qué contexto proporcionar al agente  

Debes decidir qué datos debe recibir el agente en tiempo de ejecución. Existen las siguientes opciones:  

- **Incluye todo el contexto Canvas:** Pasa todas las variables de contexto de Canvas disponibles (como las [propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) al paso en Agente. Puedes utilizar pasos de Contexto anteriores a los pasos de agente para añadir más datos a Contexto antes que él.
- **Proporciona valores:** Pasa sólo las propiedades seleccionadas, como el nombre o el color favorito de un usuario. Elige esta opción para que el agente sólo tenga acceso a los valores que asignes aquí. Para cada **Clave**, introduce la [etiqueta de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) que define el campo específico del perfil de usuario o la variable de contexto.  

{% alert note %}
Braze pasa los primeros 10 KB de contenido al agente. Proporcionar valores que tengan un valor total superior a 10 KB provoca el truncamiento.
{% endalert %}

### Paso 5: Prueba el agente

Después de configurar tu paso de Agente, puedes probar y previsualizar el resultado de este paso.

## Tratamiento de errores  

- Si el modelo conectado devuelve un error de límite de velocidad, Braze reintenta hasta cinco veces con retirada exponencial.  
- Si el agente falla por cualquier otro motivo (como una clave de API no válida), la variable de salida se establece en `null`.
    - Si un agente alcanza su límite diario de invocaciones, la variable de salida se establece en `null`. Si utilizas la salida de un agente en un paso de Mensaje, considera la posibilidad de utilizar la lógica de abortar de Liquid.
- Las respuestas se almacenan en caché para entradas idénticas y pueden reutilizarse para invocaciones idénticas repetidas en pocos minutos.
    - Las respuestas que utilizan valores almacenados en caché siguen contando para las invocaciones totales y diarias.

## Análisis  

Consulta las métricas siguientes para hacer un seguimiento del rendimiento de tus pasos de Agente:  

| Métrica | Descripción |
| --- | --- |
| _El usuario ha entrado_ | El número de veces que los usuarios entraron en el paso Agente. |
| _Continúa con el paso siguiente_ | El número de usuarios que pasaron al siguiente paso del flujo tras pasar por el paso Agente. |
| _Has salido de Canvas_ | Número de usuarios que salieron del Canvas tras pasar por el paso de Agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas más frecuentes

### ¿Cuándo debo utilizar un paso de Agente?

En general, recomendamos utilizar un paso en Canvas cuando quieras introducir datos contextuales concretos en un LLM y hacer que asigne de forma inteligente variables contextuales de Canvas a una escala imposible para los humanos.

Supongamos que envías un mensaje personalizado para recomendar un nuevo sabor de helado a un usuario que previamente pidió chocolate y fresa. He aquí la diferencia entre utilizar un paso de Agente frente a las recomendaciones de elementos de IA:

- **Paso de agente:** Utiliza los LLM para tomar una decisión cualitativa sobre lo que podría querer el usuario basándose en las instrucciones y los puntos de datos contextuales dados al agente. En este ejemplo, un paso del Agente podría recomendar un nuevo sabor basándose en la posibilidad de que el usuario quiera probar sabores diferentes.
- **Recomendaciones de elementos de IA:** Utiliza modelos de aprendizaje automático para predecir los productos que un usuario tiene más probabilidades de querer basándose en eventos pasados del usuario, como las compras. En este ejemplo, las recomendaciones de artículos de IA sugerirían un sabor (vainilla) basándose en los dos pedidos anteriores del usuario (chocolate y fresa) y en cómo se comparan con los comportamientos de otros usuarios de tu espacio de trabajo.

### ¿Cuándo debo utilizar un formato de salida estándar para un agente?

Te recomendamos que utilices el formato de salida cuando quieras que el agente devuelva una estructura de datos con múltiples valores definidos de forma estructurada, en lugar de una salida con un único valor. Esto permite formatear mejor la salida como una variable de contexto coherente.

Por ejemplo, puedes utilizar un formato de salida dentro de un agente destinado a crear un itinerario de viaje de muestra para un usuario basado en un formulario que haya enviado. El formato de salida te permite definir que la respuesta de cada agente incluya los valores `tripStartDate`, `tripEndDate` y `destination`. Cada uno de estos valores puede extraerse de las variables de contexto y colocarse en un paso de Mensaje para la personalización mediante Liquid.

### ¿Cómo utilizan los pasos del Agente los datos de entrada?

Los pasos del agente utilizan datos contextuales específicos que se [proporcionan al agente](#step-4-decide-what-context-to-provide-the-agent). 

Puedes elegir entre pasar la totalidad del contexto Canvas al agente como contexto, o pasar valores específicos utilizando etiquetas de Liquid al contexto de ese paso del agente. También puedes utilizar el Contenido conectado como valor de entrada en un paso del Agente.

## Artículos relacionados  

- [Resumen de los agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Despliega agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
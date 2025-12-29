---
nav_title: Agente
article_title: Agente Paso
alias: /agent_step/
page_order: 0.2
page_type: reference
description: "Este artículo de referencia explica cómo utilizar el paso en Canvas del Agente para generar contenido o tomar decisiones inteligentes en tiempo real."
tool: Canvas
---

# Agente Paso  

> El paso en Canvas te permite añadir la toma de decisiones y la generación de contenidos con IA directamente a tu flujo de trabajo en Canvas. Para más información general, consulta [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

\![Un paso en Canvas para un usuario.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## Cómo funciona

Cuando un usuario llega a un paso en Canvas, Braze envía los datos de entrada que hayas configurado (contexto completo o campos seleccionados) al agente que hayas elegido. A continuación, el agente procesa la entrada utilizando su modelo e instrucciones, y devuelve una salida. Esa salida se almacena en la variable de salida que definiste en el paso.

A continuación, puedes utilizar esta variable de dos formas principales:

- **Toma de decisiones:** Dirige a los usuarios por diferentes rutas Canvas en función de la respuesta del agente. Por ejemplo, un agente de puntuación de clientes potenciales podría devolver un número entre 1 y 10. Puedes utilizar esta puntuación para decidir si continúas enviando mensajes a un usuario o lo abandonas del viaje.
- **Personalización:** Inserta la respuesta del agente directamente en un mensaje. Por ejemplo, un agente podría analizar la opinión de un cliente y generar un correo electrónico de seguimiento empático que haga referencia al comentario del cliente y sugiera una solución.

## Crear un paso de Agente

### Paso 1: Añade un paso

Arrastra y suelta el componente **Agente** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Agente**.  

### Paso 2: Selecciona tu agente  

Selecciona el agente que procesará los datos en este paso. Elige un agente existente, o crea uno nuevo directamente desde este paso. Para obtener instrucciones de configuración, consulta [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/).

### Paso 3: Define la variable de salida

Las salidas de los agentes se denominan "variables de salida" y se almacenan en una [variable de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#context-variable-types) para facilitar su acceso. Para definir la variable de salida:

1. Dale un nombre a la variable.
2. Selecciona un tipo de datos. 

Las salidas del agente pueden guardarse como cadenas, números o booleanos. Esto los hace flexibles tanto para la personalización del texto como para la lógica condicional en tu Canvas. He aquí algunos usos comunes de cada tipo:

| Tipo de datos | Usos comunes |
| --- | --- |
| Cadena | Personalización de mensajes (líneas del asunto, copia, respuestas) |
| Número | Puntuación, umbrales, enrutamiento en [Rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) |
| Booleano | Sí/No ramificación en [divisiones de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Una vez definida, puedes utilizar una variable de salida en todo el Canvas utilizando la misma sintaxis de plantilla que con una variable de contexto. Utiliza el filtro de segmentos **de la Variable de Contexto** o plantilla las respuestas de los agentes directamente con Liquid: {% raw %}`{{context.${response_variable_name}}}` {% endraw %}.

### Paso 4: Decide qué contexto proporcionar al agente  

Debes decidir qué datos debe recibir el agente en tiempo de ejecución. Están disponibles las siguientes opciones:  

- **Incluye todo el contexto Canvas:** Pasa todas las variables de contexto de Canvas disponibles (como [las propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)) y cualquier otro contexto que se le haya dado a través de los pasos de Contexto.  
- **Proporciona valores:** Pasa sólo las propiedades seleccionadas, como el nombre o el color favorito de un usuario. Elige esta opción para que el agente sólo tenga acceso a los valores que asignes aquí. Para cada **Clave**, introduce la [etiqueta de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags) que define el campo específico del perfil de usuario o la variable de contexto.  

{% alert note %}
Braze sólo pasará los primeros 10 KB de contenido al agente. Proporcionar valores que tengan un valor total de más de 10 KB provocará el truncamiento. Para ayudar a ahorrar costes, los Agentes Braze en Canvas utilizan cachés de corta duración para respuestas LLM para entradas idénticas. Incluir todo el Contexto Canvas aumenta la probabilidad de que no se puedan utilizar los resultados almacenados en caché, lo que podría aumentar los costes de tu LLM.
{% endalert %}

## Tratamiento de errores  

- Si el modelo conectado devuelve un error de límite de velocidad, Braze reintenta hasta cinco veces con retirada exponencial.  
- Si el agente falla por cualquier otro motivo (como una clave de API no válida), la variable de salida se establece en `null`.  
- Las respuestas se almacenan en caché para entradas idénticas, con el fin de reducir las invocaciones repetidas.  

## Análisis  

Consulta las métricas siguientes para hacer un seguimiento del rendimiento de tus pasos de Agente:  

| Métrica | Descripción |
| --- | --- |
| _Entró en_ | El número de veces que los usuarios entraron en el paso Agente. |
| _Pasar al siguiente paso_ | El número de usuarios que pasaron al siguiente paso del flujo tras pasar por el paso Agente. |
| _Lienzo Exited_ | Número de usuarios que salieron del Canvas tras pasar por el paso de Agente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Artículos relacionados  

- [Resumen de los agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/)  
- [Crear agentes personalizados]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)  
- [Despliegue de agentes]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/)  
---
nav_title: Implementar agentes
article_title: Implementar agentes personalizados
description: "Aprende a utilizar los agentes personalizados en Braze después de crearlos."
alias: /deploying-agents/
page_order: 2
---

# Implementar agentes personalizados

> Aprende a utilizar los agentes personalizados en los pasos en Canvas o en los campos del catálogo después de crearlos. Para obtener una introducción, consulta [Agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Agentes en Canvas  

Puedes utilizar agentes como pasos en un proceso para realizar la personalización de mensajes u orientar la toma de decisiones en tiempo real. Para obtener información detallada sobre los pasos de configuración, consulta el [paso Agente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Ejemplos

| Casos de uso | Descripción |
| --- | --- |
| Puntuación y calificación de clientes potenciales | Utiliza un paso de agente para evaluar los clientes potenciales entrantes en una escala (por ejemplo, del 1 al 10). Dirigir a los usuarios con una puntuación superior a un umbral a rutas de captación, mientras que se descarta a los clientes potenciales menos adecuados. |
| Personalización dinámica de mensajes | Haz que un agente genere líneas del asunto, recomendaciones de productos o copias de mensajes basadas en los atributos de los usuarios o en sus comportamientos recientes. La respuesta se puede insertar directamente en un paso de mensaje. |
| Gestión de los comentarios de los clientes | Transmite los comentarios de los clientes a un agente para analizar su opinión y generar mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente podría escalar la respuesta o incluir ventajas adicionales. |
| Enrutamiento inteligente | Utiliza los resultados del agente (booleanos o numéricos) para dividir a los usuarios en diferentes rutas de Canvas. Por ejemplo, clasificar a los usuarios como «en riesgo» o «sanos» y ajustar la frecuencia de la mensajería en consecuencia. |
| Interpretación de cuestionarios o respuestas | Deja que un agente analice las respuestas abiertas de los cuestionarios o los campos de texto libre, y devuelva valores estructurados (por ejemplo, categorizando la intención o la necesidad) que impulsen las rutas posteriores. |
| Razonamiento en varios pasos | Configura un agente para combinar campos de contexto y tomar decisiones complejas, como recomendar la siguiente mejor acción (correo electrónico, SMS o contacto humano) en función de múltiples atributos del usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agentes en catálogos  

Puedes aplicar un agente a los campos del catálogo para que genere o calcule automáticamente los valores de cada fila. El agente también se ejecutará en las nuevas filas que se añadan al catálogo en el futuro. 

### Ejemplos

| Casos de uso | Descripción |
| --- | --- |
| Generar descripciones de productos | Crea automáticamente textos de marketing breves para las nuevas entradas del catálogo, por ejemplo, generando una descripción atractiva a partir de datos estructurados del producto, como el nombre, la categoría y las características. |
| Enriquece los atributos del producto. | Rellena los valores que falten, como la familia de colores, el estilo o la temporada, basándote en el nombre y los detalles del producto. Por ejemplo, si el nombre de un producto es «Gafas de sol polarizadas Laguna», el agente podría asignar el estilo como «deportivo» y la familia de colores como «azul». |
| Calcular campos derivados | Utiliza los campos existentes para generar nuevos datos, como una «puntuación de adecuación» basada en atributos o una «etiqueta de popularidad» a partir de las ventas y el número de reseñas. |
| Clasificar o etiquetar elementos | Asigna etiquetas para la lógica de recomendación, de modo que los modelos de personalización puedan realizar la segmentación de productos de forma más eficaz. Por ejemplo, etiqueta los productos como «para exterior», «para festivales» o «premium». |
| Realizar la localización del contenido | Traduce el texto del catálogo a otro idioma para campañas globales o ajusta el tono y la longitud para canales específicos de cada región. Por ejemplo, traduce «Classic Clubmaster Sunglasses» al español como «Gafas de sol Classic Clubmaster» o acorta las descripciones para las campañas de SMS. |
| Resume las reseñas o comentarios. | Resume las opiniones o comentarios en un nuevo campo, por ejemplo, asignando puntuaciones como «Positivo», «Neutro» o «Negativo», o creando un breve resumen de texto como «La mayoría de los clientes mencionan que el producto se ajusta muy bien, pero señalan que el envío es lento». |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Pasos

![Un paso de agente en un campo de catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para añadir un agente al campo del catálogo:

1. En tu catálogo, añade un nuevo campo.  
2. Selecciona **Aplicar agente de IA**.
3. Asigna un agente a este campo.  
4. Selecciona las columnas que deben pasarse como entrada. Si no se selecciona ninguna, el agente tendrá acceso a todas las columnas del catálogo.  
5. Decide si el agente debe volver a calcular los campos cuando se actualicen las filas del catálogo. Si no seleccionas esta opción, el agente solo se ejecutará una vez por fila.
6. Selecciona **Añadir campos** para implementar el agente y revisar las estimaciones de costes. El modal **Estimación de** **costes** muestra cuántas veces se ejecutará el agente en este catálogo, lo que equivale aproximadamente al número total de filas. Para continuar, selecciona **Confirmar**.

### Cómo funcionan los agentes de catálogo  

Tras su inicio, el agente ejecuta y evalúa cada fila, tomando las columnas seleccionadas en su contexto para generar un resultado. Los agentes se ejecutan en todas las filas nuevas añadidas después de implementar el agente. Si seleccionaste **Recalcular cuando se actualicen las filas del catálogo**, todos los valores de este campo se actualizarán si cambian los campos de origen existentes.

Puedes actualizar y editar los campos de tu catálogo que utilizan agentes. Para eliminar un agente de una columna, desmarca la casilla **Aplicar agente de IA**. Esto revierte la columna a una columna no agente, y los campos conservan los últimos valores que el agente aplicó la última vez que se ejecutó en el catálogo.

Las referencias circulares en los catálogos no son compatibles, lo que significa que no puede darse la siguiente situación:

- La columna 1 de Agentic utiliza la columna 2 de Agentic como entrada.
- La columna 2 de Agentic utiliza la columna 1 de Agentic como entrada.

![La opción de seleccionar «Aplicar agente de IA» para un campo del catálogo.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Los agentes de catálogo solo pueden procesar valores de entrada de hasta 25 KB por fila.
{% endalert %}

#### Definir campos de respuesta

Si tu agente utiliza [campos]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) como formato de salida, puedes seleccionar el campo correspondiente del agente para **el campo Respuesta** que se utilizará en el campo del catálogo. 

Supongamos que tienes un agente que añade descripciones de productos a un catálogo con los siguientes campos para estructurar el formato de salida:

| Nombre del campo | Valor |
| --- | --- |
| **descripción** | Texto |
| **confidence_score_out_of_ten** | Número |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Puedes añadir un campo llamado**product_description**  a un catálogo y seleccionar **descripción** como **campo** **de respuesta** para rellenar la columna con las descripciones del agente.

![Un campo"product_description"con el agente «Descriptor» aplicado. La salida «descripción» se selecciona como campo de respuesta.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

También puedes anular manualmente la celda generada por el agente seleccionando **Editar elemento** y actualizando la descripción generada por el agente con tus modificaciones. Para volver a la descripción generada por el agente, selecciona el símbolo de actualización en la celda.

### Gestión de errores en catálogos  

- Las invocaciones de catálogo fallidas no se vuelven a intentar.
- Si la llamada a la API del proveedor del modelo básico devuelve algún error, como un error de clave de API no válida o un error de límite de velocidad, el valor del campo no se actualiza.
- Puedes revisar los registros del agente para obtener detalles sobre las ejecuciones fallidas.

## Supervisa a tu agente

En la sección **Uso** de tu agente, puedes consultar y navegar hasta los lugares en los que el agente se utiliza activamente en catálogos y lienzos.

![Sección Uso de agentes que muestra dos agentes activos y un agente inactivo para Canvases.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

En la sección **Registros** de tu agente, puedes supervisar las llamadas reales de los agentes que se producen en tus lienzos y catálogos. Puedes filtrar por información como el intervalo de fechas, el resultado (éxito o fracaso) o la ubicación de la llamada. También puedes seleccionar **Exportar CSV** para exportar solo los registros que se muestran en la página actual.

{% alert tip %}
También puedes supervisar los errores de límite de invocaciones diarias en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).
{% endalert %}

![Registros para la puntuación de sentimiento de la IA de un agente.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Selecciona **Ver** para una llamada de agente específica y verás la entrada, la salida y el ID del usuario.

![El panel de detalles de una asignación deportiva aleatoria de un agente que muestra la solicitud de entrada, la respuesta de salida y un ID de usuario asociado.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Usar Currents

También puedes utilizar estos eventos de Currents para acceder a los esquemas de registros de Kafka:

- Eventos ejecutados por el agente
- Eventos de invocación de herramientas

Consulta el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) para obtener más detalles.

## Artículos relacionados  

- [Referencia para agentes]({{site.baseurl}}/user_guide/brazeai/agents/reference/)
---
nav_title: Despliegue de agentes
article_title: Despliegue de agentes personalizados
description: "Aprende a utilizar agentes personalizados en Braze después de crearlos."
alias: /deploying-agents/
---

# Despliegue de agentes personalizados

> Aprende a utilizar agentes personalizados en pasos en Canvas o campos de catálogo después de crearlos. Para una introducción, ver [Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

{% alert important %}
Los Agentes Braze están actualmente en fase beta. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}  

## Agentes en Canvas  

Puedes utilizar agentes como etapas de un recorrido para personalizar mensajes o guiar la toma de decisiones en tiempo real. Para conocer los pasos detallados de configuración, consulta [Paso Agente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Casos de uso

| Casos de uso | Descripción |
| --- | --- |
| Calificación y puntuación de clientes potenciales | Utiliza un paso de Agente para evaluar los clientes potenciales entrantes en una escala (por ejemplo, de 1 a 10). Dirige a los usuarios con una puntuación por encima de un umbral hacia rutas de nutrición, mientras descalificas a los clientes potenciales poco adecuados. |
| Personalización dinámica de mensajes | Haz que un agente genere líneas del asunto, recomendaciones de productos o mensajes basados en los atributos del usuario o en comportamientos recientes. La respuesta puede insertarse directamente en un paso de Mensaje. |
| Gestión de las opiniones de los clientes | Pasa los comentarios de los clientes a un agente para analizar el sentimiento y generar mensajes de seguimiento empáticos. Para los usuarios de alto valor, el agente puede intensificar la respuesta o incluir ventajas. |
| Encaminamiento inteligente | Utiliza salidas de agente (booleanas o numéricas) para dividir a los usuarios en diferentes rutas Canvas. Por ejemplo, clasifica a los usuarios como "de riesgo" o "sanos" y ajusta la cadencia de la mensajería en consecuencia. |
| Interpretación de cuestionarios o respuestas | Deja que un agente analice las respuestas abiertas de los cuestionarios o los campos de texto libre, devolviendo valores estructurados (por ejemplo, categorizando la intención o la necesidad) que impulsen las rutas descendentes. |
| Razonamiento en varios pasos | Configura un agente para que combine campos de contexto y tome decisiones complejas, como recomendar la siguiente mejor acción (correo electrónico, SMS o contacto humano) basándose en múltiples atributos del usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agentes en catálogos  

Puedes aplicar un agente a los campos del catálogo para que genere o calcule automáticamente valores para cada fila. El agente también se ejecutará en las nuevas filas que se añadan al catálogo en el futuro. 

### Casos de uso

| Casos de uso | Descripción |
| --- | --- |
| Generar descripciones de productos | Crea automáticamente textos breves de marketing para nuevas entradas en el catálogo, por ejemplo, generando una descripción pegadiza a partir de datos estructurados del producto, como el nombre, la categoría y las características. |
| Enriquece los atributos de los productos | Rellena los valores que faltan, como la familia de colores, el estilo o la temporada, basándote en el nombre y los detalles de un producto. Por ejemplo, si el nombre de un producto es "Gafas de sol polarizadas Laguna", el agente podría asignar el estilo como "deportivo" y la familia de colores como "azul". |
| Calcular campos derivados | Utiliza los campos existentes para generar nuevos datos, como una "puntuación de ajuste" basada en atributos o una "etiqueta de popularidad" a partir de los recuentos de ventas y reseñas. |
| Categorizar o etiquetar elementos | Asigna etiquetas a la lógica de recomendación para que los modelos de personalización puedan segmentar los productos con mayor eficacia. Por ejemplo, etiqueta los productos como "outdoor", "festival-ready" o "premium". |
| Localización de contenidos | Traduce el texto del catálogo a otro idioma para campañas globales, o ajusta el tono y la longitud para canales específicos de una región. Por ejemplo, traduce "Gafas de sol Classic Clubmaster" al español como "Gafas de sol Classic Clubmaster", o acorta las descripciones de las campañas por SMS. |
| Resume las opiniones o comentarios | Resume el sentimiento o las opiniones en un nuevo campo, como asignar puntuaciones de sentimiento como Positivo, Neutral o Negativo, o crear un breve resumen de texto como "La mayoría de los clientes mencionan un gran ajuste, pero notan lentitud en el envío". |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Pasos

\![Un paso de Agente en un campo del catálogo.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para añadir un agente al campo de tu catálogo

1. En tu catálogo, añade un nuevo campo.  
2. Selecciona **Aplicar agente IA**.
3. Asigna un agente a este campo.  
4. Selecciona qué columnas deben pasarse como entrada. Si no se selecciona ninguna, el agente tendrá acceso a todas las columnas del catálogo.  
5. Decide si el agente debe recalcular los campos cuando se actualicen las filas del catálogo. Si no seleccionas esta opción, el agente sólo se ejecutará una vez por fila.
6. Selecciona **Añadir campos** para desplegar el agente y revisar las estimaciones de costes. El modal **Estimación de costes** muestra cuántas veces se ejecutará el agente en este catálogo, aproximadamente igual al número total de filas. Para continuar, selecciona **Confirmar**.

### Cómo funcionan los agentes de catálogo  

Tras el lanzamiento, el agente se ejecutará y evaluará cada fila, tomando las columnas seleccionadas en su contexto para producir una salida. Los agentes se ejecutan en todas las nuevas filas añadidas después de desplegar el agente. Si seleccionaste **Recalcular cuando se actualizan las filas del catálogo**, todos los valores de este campo se actualizarán si cambian los campos fuente existentes.  

{% alert note %}
Durante el periodo beta, los agentes de catálogo están limitados a procesar valores de entrada de hasta 10 KB por fila, y sólo actualizarán las 10.000 primeras filas de un catálogo.
{% endalert %}

### Tratamiento de errores en los catálogos  

- Las invocaciones de catálogo fallidas no se reintentan.
- Si la llamada de la API al proveedor del modelo fundacional devuelve algún error, como un error de clave de API no válida o un error de límite de velocidad, el valor del campo no se actualizará.   
- Puedes revisar los registros del agente para ver los detalles de las ejecuciones fallidas.  

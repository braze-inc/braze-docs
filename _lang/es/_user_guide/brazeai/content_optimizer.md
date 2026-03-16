---
nav_title: Optimizador de contenidos
article_title: Optimizador de contenidos
alias: "/content_optimizer/"
description: "Content Optimizer es un agente que te ayuda a probar y optimizar el contenido de los mensajes a gran escala, utilizando la inteligencia artificial para generar y evaluar automáticamente grandes volúmenes de variantes de contenido."
page_type: reference
page_order: 3
---

# Optimizador de contenidos

> Content Optimizer es un agente que te ayuda a probar y optimizar el contenido de los mensajes a gran escala, utilizando la inteligencia artificial para generar y evaluar automáticamente grandes volúmenes de variantes de contenido.

{% alert important %}
Content Optimizer se encuentra actualmente en fase beta y solo está disponible para mensajes de correo electrónico. Para obtener ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Acerca del optimizador de contenido

Content Optimizer es un agente que se ejecuta en un paso en Canvas. Te ayuda a definir los componentes del mensaje que deseas probar, generar variantes mediante IA generativa o entrada manual, y optimizar automáticamente las combinaciones de contenido que se envían a los usuarios. Esta característica te ayuda a:

- Optimiza las líneas del asunto, el encabezado del cuerpo, el contenido del cuerpo o la llamada a la acción principal de los correos electrónicos.
- Mejora continuamente el rendimiento de los mensajes sin necesidad de configurar pruebas A/B manuales.
- Prueba rápidamente grandes volúmenes de variantes de contenido, aprovechando la inteligencia artificial para la ideación.
- Eliminar automáticamente el contenido de bajo rendimiento y ampliar el contenido más exitoso.

Aprende a crear un [paso de optimizador de contenido]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Ejemplos

### Correo electrónico

| Caso de uso de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones en la línea del asunto del correo electrónico | Aumentar la tasa de apertura | Tono de prueba, urgencia, personalización y uso de emojis. |
| Estilos de mensajes de encabezado de mensajería | Aumenta la interacción | Compara los mensajes emocionales, basados en valores y claros en el encabezado del cuerpo. | 
| Formato del contenido del cuerpo | Mejora la legibilidad y la interacción | Prueba la narración frente a las listas de características, las viñetas frente a los párrafos y la longitud del contenido. |
| Tono del& texto de la llamada a la acción (CTA) | Aumenta los click-throughs | Compara frases de llamada a la acción orientadas a la acción, centradas en los beneficios y en primera persona. |
| Combinaciones de contenidos temáticos | Descubre combinaciones de alto rendimiento en términos de rendimiento | Combina y mezcla los componentes temáticos del asunto, el cuerpo y la llamada a la acción para encontrar la mejor combinación global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cómo funciona

Content Optimizer utiliza un algoritmo [bandido multiarma](https://en.wikipedia.org/wiki/Multi-armed_bandit) no contextual para asignar más envíos a las variantes de alto rendimiento y reducir la asignación a las de bajo rendimiento. Con el tiempo, esto se traduce en una mejora continua del contenido de tus mensajes, con una intervención manual mínima.

El algoritmo de optimización bandit patentado por Braze se ha diseñado específicamente para la naturaleza combinatoria del paso del optimizador de contenido. Dado que cada mensaje se compone de varios elementos, el bandido aprende simultáneamente sobre el rendimiento de cada elemento (como la línea del asunto, el cuerpo del mensaje o la llamada a la acción) y sobre sus interacciones cuando se combinan en un mensaje. Más concretamente, cuando se envía una combinación determinada, todas las combinaciones que comparten los mismos componentes se benefician de los datos de ese envío. Esto permite que el bandido aprenda mucho más rápido con la misma cantidad de datos, en comparación con un algoritmo bandido estándar.

Cuando se inicia el paso por primera vez, Content Optimizer envía variantes aleatoriamente para recopilar datos de rendimiento iniciales. Tras este periodo inicial de exploración, el algoritmo comienza a desviar el tráfico hacia combinaciones de contenido con mejor rendimiento, reduciendo gradualmente la asignación a las opciones con peor rendimiento. Durante el periodo de exploración, el tráfico se distribuye generalmente entre las variantes disponibles para permitir que el algoritmo aprenda de su rendimiento relativo.

El optimizador de contenido es similar al paso Mensaje de Canvas, con características como horas tranquilas, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) y registro de eventos. Puedes configurar un paso de optimizador de contenido creando un mensaje base y definiendo qué componentes del contenido (como la línea del asunto, el cuerpo del texto o la llamada a la acción) deseas optimizar. Las variantes de cada componente pueden generarse con IA o introducirse manualmente, y deben añadirse etiquetas de Liquid al mensaje base para mapear los componentes al contenido del mensaje.

Cada usuario recibe un mensaje por cada entrada en el paso Optimizador de contenido. Las reentradas se tratan como nuevas, sin memoria de variantes anteriores.

Para obtener los mejores resultados, utiliza el Optimizador de contenido en lienzos en los que los usuarios entran gradualmente a lo largo del tiempo, como en lienzos recurrentes o siempre activos con un volumen diario constante. Si todos los usuarios entran en la etapa a la vez, el agente no tendrá tiempo para aprender de los primeros resultados. El paso se comportará más como una prueba A/B estática que como un motor de optimización en vivo.

Esto significa que todavía puedes utilizar Content Optimizer en lienzos de envío único o de corta duración, pero solo si los usuarios entran en el paso durante un periodo prolongado (por ejemplo, a través de un paso de retraso, una entrada programada o un flujo desencadenado por API). Asegúrate de que el paso tenga suficiente tráfico y tiempo para observar las diferencias de rendimiento antes de llegar a la mayoría de los usuarios.

### Conceptos clave

| Plazo                    | Descripción |
|-------------------------|-------------|
| Mensaje de base   | La plantilla del mensaje principal a partir de la cual se crean las variantes, incluyendo todas las configuraciones de envío. |
| Componentes de contenido  | Elementos dentro de un mensaje (por ejemplo, la línea del asunto o la llamada a la acción principal) que pueden probarse y optimizarse. Los especialistas en marketing deben insertar la etiqueta de Liquid correspondiente en el mensaje, en el lugar donde debe aparecer el componente. |
| Variantes de contenido    | Los diferentes valores que puede adoptar un componente de contenido. |
| Combinaciones de contenido| Mensajes únicos creados mediante la combinación y el emparejamiento de variantes de contenido. |
| Evento de optimización       | Determina cómo Content Optimizer evalúa el rendimiento y asigna el tráfico a combinaciones de contenido a lo largo del tiempo, como clics o aperturas de correos electrónicos. Se aplica a todos los componentes de contenido de un paso. Content Optimizer aprende continuamente de este evento y cambia automáticamente la entrega hacia combinaciones de contenido de mayor rendimiento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

- Content Optimizer se encuentra actualmente en fase beta y solo está disponible para mensajes de correo electrónico.
- El agente puede generar hasta 125 combinaciones por paso:
   - Hasta 3 componentes por paso
   - Hasta 5 variantes para cada componente
- Solo se envía un mensaje por usuario y por entrada. No hay memoria de envíos anteriores para reentradas.
- Los especialistas en marketing deben insertar manualmente etiquetas de Liquid para cada componente en el creador de mensajes donde deben mostrarse las variantes de contenido definidas.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Próximos pasos

- Ponte en contacto con tu administrador del éxito del cliente para unirte a la versión beta o para obtener asistencia para la incorporación.
- Aprende a crear un [paso de optimizador de contenido]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

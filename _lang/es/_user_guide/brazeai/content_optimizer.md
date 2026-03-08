---
nav_title: Optimizador de contenidos
article_title: Optimizador de contenidos
alias: "/content_optimizer/"
description: "El Optimizador de contenido es un agente que te ayuda a probar y optimizar el contenido de los mensajes a escala, utilizando la IA para generar y evaluar grandes volúmenes de variantes de contenido automáticamente."
page_type: reference
page_order: 4
---

# Optimizador de contenidos

> El Optimizador de contenido es un agente que te ayuda a probar y optimizar el contenido de los mensajes a escala, utilizando la IA para generar y evaluar grandes volúmenes de variantes de contenido automáticamente.

{% alert important %}
El Optimizador de Contenidos está actualmente en fase beta y sólo está disponible para mensajes de correo electrónico. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Acerca del Optimizador de Contenidos

El Optimizador de Contenidos es un agente que se ejecuta en un paso en Canvas. Te ayuda a definir los componentes de los mensajes a probar, a generar variantes utilizando IA Generativa o entradas manuales, y a optimizar automáticamente qué combinaciones de contenido se envían a los usuarios. Esta característica te ayuda a:

- Optimiza las líneas del asunto, el encabezado del cuerpo, el contenido del cuerpo o la CTA principal de los correos electrónicos.
- Mejora continuamente el rendimiento de los mensajes sin necesidad de configurar pruebas A/B manualmente.
- Prueba rápidamente grandes volúmenes de variantes de contenido, aprovechando la IA para la ideación.
- Elimina automáticamente los contenidos de bajo rendimiento y aumenta los ganadores.

Aprende a crear un [paso Optimizador de Contenidos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

## Ejemplos

### Correo electrónico

| Caso de uso de optimización | Objetivo | Descripción |
| --- | --- | --- |
| Variaciones de la línea del asunto | Aumenta la tarifa abierta | Prueba el tono, la urgencia, la personalización y el uso de emojis. |
| Estilos de mensajería de cabecera | Aumenta la interacción | Compara la mensajería emocional, basada en valores y clara en el encabezamiento del cuerpo. | 
| Formato del contenido del cuerpo | Mejora la legibilidad y la interacción | Prueba la narrativa frente a las listas de características, las viñetas frente a los párrafos y la longitud del contenido. |
| Copia del CTA & tono | Aumenta los click-throughs | Compara las frases CTA orientadas a la acción, centradas en los beneficios y en primera persona. |
| Combinaciones de contenidos temáticos | Descubre combinaciones de alto rendimiento | Mezcla y combina componentes temáticos de asunto, cuerpo y CTA para encontrar la mejor combinación global. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Cómo funciona

El Optimizador de Contenidos utiliza un algoritmo no contextual [de bandido de brazos múltiples](https://en.wikipedia.org/wiki/Multi-armed_bandit) para asignar más envíos a las variantes de alto rendimiento y reducir la asignación a las de bajo rendimiento. Con el tiempo, esto se traduce en una mejora continua del contenido de tus mensajes, con una intervención manual mínima.

Cuando el paso se lanza por primera vez, el Optimizador de Contenidos envía variantes aleatoriamente para recopilar los datos iniciales de rendimiento. Tras este periodo inicial de exploración, el algoritmo empieza a desplazar el tráfico hacia las combinaciones de contenidos de mayor rendimiento, reduciendo gradualmente la asignación a las opciones de menor rendimiento. Durante el periodo de exploración, el tráfico suele distribuirse entre las variantes disponibles para que el algoritmo aprenda de su rendimiento relativo.

El Optimizador de Contenidos es similar al paso en Canvas Mensajes, con características como horas tranquilas, [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing) y registro de eventos. Puedes configurar un paso del Optimizador de contenido creando un mensaje base y definiendo qué componentes del contenido (como la línea del asunto, el cuerpo del texto o la llamada a la acción) optimizar. Las variantes de cada componente pueden generarse con IA o introducirse manualmente, y deben añadirse etiquetas de Liquid al mensaje base para mapear los componentes en el contenido del mensaje.

Cada usuario recibe un mensaje por entrada en el paso Optimizador de Contenidos. Las reentradas se tratan como nuevas, sin memoria de las variantes anteriores.

Para obtener los mejores resultados, utiliza el Optimizador de Contenidos en Lienzos en los que los usuarios introduzcan el paso gradualmente a lo largo del tiempo, como en Lienzos recurrentes o siempre activos con un volumen diario constante. Si todos los usuarios entran en el paso a la vez, el agente no tendrá tiempo de aprender de los primeros resultados. El paso se comportará más como una prueba A/B estática que como un motor de optimización en vivo.

Esto significa que puedes seguir utilizando el Optimizador de Contenidos en Lienzos de un solo envío o de corta duración, pero sólo si los usuarios entran en el paso durante un periodo prolongado (por ejemplo, a través de un paso de retraso, una entrada programada o un flujo desencadenado por la API). Asegúrate de que el paso tiene suficiente tráfico y tiempo para observar las diferencias de rendimiento antes de llegar a la mayoría de los usuarios.


### Conceptos clave

| Plazo                    | Descripción |
|-------------------------|-------------|
| Mensaje de base   | La plantilla principal de mensajes a partir de la cual se construyen las variantes, incluyendo todas las configuraciones de envío. |
| Componentes de contenido  | Elementos de un mensaje (por ejemplo, la línea del asunto o la CTA principal) que pueden probarse y optimizarse. Los especialistas en marketing deben insertar la etiqueta de Liquid correspondiente en el mensaje donde debe aparecer el componente. |
| Variantes de contenido    | Los distintos valores que puede tomar un componente de contenido. |
| Combinaciones de contenidos| Mensajes únicos creados mezclando y combinando variantes de contenido. |
| Evento de optimización       | Determina cómo el Optimizador de Contenidos evalúa el rendimiento y asigna el tráfico a las combinaciones de contenido a lo largo del tiempo, como los clics o las aperturas de correo electrónico. Se aplica a todos los componentes de contenido de un paso. El Optimizador de Contenidos aprende continuamente de este evento y cambia automáticamente la entrega hacia combinaciones de contenidos de mayor rendimiento. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limitaciones

- El Optimizador de Contenidos está actualmente en fase beta y sólo está disponible para mensajes de correo electrónico.
- El agente puede generar hasta 125 combinaciones por paso:
   - Hasta 3 componentes por paso
   - Hasta 5 variantes para cada componente
- Sólo se envía un mensaje por usuario y por entrada. No hay memoria de los envíos anteriores para las reentradas.
- Los especialistas en marketing deben insertar manualmente etiquetas de Liquid para cada componente en el creador de mensajes, donde deben aparecer las variantes definidas del componente de contenido.

{% multi_lang_include brazeai/generative_ai/policy.md %}

## Próximos pasos

- Ponte en contacto con tu administrador del éxito del cliente para unirte a la versión beta o para obtener ayuda sobre la incorporación.
- Aprende a crear un [paso Optimizador de Contenidos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/content_optimizer_step/).

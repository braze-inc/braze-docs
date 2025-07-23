---
nav_title: Control de calidad del contenido con inteligencia artificial
article_title: Control de calidad del contenido con inteligencia artificial
page_order: 10
description: "Este artículo de referencia explica cómo realizar un control de calidad del contenido de tus mensajes con IA directamente desde el creador de mensajes."
---

# Control de calidad del contenido con inteligencia artificial

> Aprende a realizar el control de calidad del contenido de tus mensajes con IA directamente desde el creador de mensajes.

El control de calidad del contenido con IA utiliza las capacidades de GPT y OpenAI para realizar comprobaciones del contenido de tu mensaje, asegurándose de que cumple las normas de calidad mediante la identificación de elementos ineficaces, como errores ortográficos, problemas gramaticales, tono inadecuado y lenguaje ofensivo. Puedes acceder a esta característica desde la pestaña **Prueba** cuando redactes un mensaje push, SMS o dentro de la aplicación en una campaña o Canvas.

## Características principales

El control de calidad del contenido con IA ofrece las siguientes características clave para mejorar la calidad del contenido de tus mensajes:

- **Corrección ortográfica y gramatical:** Comprueba automáticamente si hay errores ortográficos y gramaticales en tu mensaje. Sugiere correcciones y proporciona recomendaciones para mejorar la exactitud general del contenido.
- **Análisis del tono:** Evalúa el tono del mensaje para identificar posibles problemas. Ayuda a garantizar que el tono pretendido se alinea con el estilo de comunicación deseado y ayuda a evitar malentendidos u ofensas involuntarias.
- **Detección de lenguaje ofensivo:** Analiza tu mensaje en busca de lenguaje potencialmente ofensivo o inapropiado, permitiéndote revisar el contenido y mantener una comunicación respetuosa.
- **Comprobación accidental del contenido:** Detecta cualquier inclusión de código, lenguaje de marcado o mensajes de prueba que puedan haberse añadido involuntariamente, incluido cualquier código Liquid que no se haya renderizado para un usuario de prueba.

## Acceder a la garantía de calidad de los contenidos con IA

{% alert note %}
Por el momento, el control de calidad del contenido con IA sólo está disponible para los canales push y SMS.
{% endalert %}

Para acceder al verificador de contenidos, sigue estos pasos:

1. Después de redactar un mensaje push o SMS, ve a la pestaña **Prueba**.
2. Localiza la sección **Control de calidad del contenido con IA**.
3. Haz clic en **Probar contenido**.

![Contenido QA con la sección AI de la pestaña Prueba.][1]{: style="max-width:60%"}

### Apoyo lingüístico

GPT es capaz de entender [varios idiomas](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages), aunque OpenAI no los admita oficialmente. Braze no pasa ninguna información adicional sobre el idioma o la localización de tu copia cuando el contenido del mensaje se envía a OpenAI, por lo que corresponde a GPT hacer esa determinación.

Los resultados pueden variar según la lengua en la que escribas.

## Consejos para un uso eficaz

Ten en cuenta los siguientes consejos para aprovechar al máximo la característica Control de calidad del contenido con IA:

- **Corrige tu mensaje:** Aunque el corrector de contenido puede ayudar a identificar errores, sigue siendo esencial corregir tu contenido manualmente. Confía en las sugerencias generadas por la IA como una guía útil, pero utiliza tu criterio para garantizar la precisión.
- **Comprende el análisis del tono:** Los resultados del análisis del tono son subjetivos y se basan en la comprensión del modelo de IA. Aunque pueden aportar información útil, ten en cuenta el tono que pretendes utilizar y el contexto de la conversación para hacer los ajustes oportunos.
- **Comprueba dos veces el lenguaje ofensivo marcado:** La detección de lenguaje ofensivo está diseñada para ser robusta, pero ocasionalmente puede marcar falsos positivos. Revisa detenidamente las secciones marcadas y haz los cambios necesarios.

## ¿Cómo se utilizan y envían mis datos a OpenAI?

Para comprobar el contenido de tu mensaje, Braze lo enviará a la Plataforma API de OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que incluyas información identificadora única en el contenido del mensaje que proporciones. Como se detalla en [los Compromisos de la Plataforma API de Open](https://openai.com/policies/api-data-usage-policies)AI, los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Por favor, asegúrate de que cumples las políticas de OpenAI relevantes para ti, que pueden incluir su [Política de Uso](https://openai.com/policies/usage-policies) y su [Política de Compartir y Publicar](https://openai.com/policies/sharing-publication-policy). Braze no ofrece garantías de ningún tipo con respecto a cualquier contenido generado por IA.

[1]: {% image_buster /assets/img/content_qa_ai.png %}

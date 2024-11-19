---
nav_title: Paso de IA
article_title: Paso de IA
permalink: /ai_step/
description: "Este artículo de referencia cubre el paso en Canvas AI."
Tool:
  - Canvas
hidden: true
---

# Paso AI

> El paso de IA dentro de Canvas aprovecha ChatGPT para automatizar el marketing personalizado interpretando las entradas generadas por el usuario (como los comentarios de los cuestionarios), determinando la respuesta adecuada y desencadenando mensajes, todo dentro de Braze. ChatGPT funciona con OpenAI, un tercero.

{% alert note %}
El paso de la IA está disponible actualmente como característica beta. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en esta prueba beta.
{% endalert %}

## Crear un paso de IA {#create-ai-step}
 
1. Añade un nuevo paso a tu Canvas y selecciona el **Paso de IA**. <br><br>![El paso de IA en el compositor de Canvas][1]{: style="max-width: 30%;"}<br><br>
2. Crea un aviso que indique a la IA cómo responder a las distintas acciones del usuario. Las respuestas pueden incluir la actualización de un atributo personalizado o el envío de un mensaje. Esta consulta puede utilizar Liquid para asignar diferentes salidas de respuesta en función de diferentes atributos o entradas de usuario. <br><br>Para asignar resultados que luego puedan utilizarse para personalizar futuros mensajes dentro del mismo Canvas, crea un indicador que guarde variables con nombres específicos (por ejemplo, "mensaje" y "puntuación de sentimiento"). <br><br> ![Ejemplo de mensaje de IA utilizado en la configuración del paso de IA para enviar un mensaje personalizado basado en una puntuación de sentimiento generada. Este ejemplo figura en la sección "Respuestas del sentimiento del cliente".][2] <br><br>
3. Utiliza la pestaña **Vista previa** para probar lo que la IA podría mostrar a determinados usuarios.<br><br> ![La pestaña Vista previa de la configuración del paso AI muestra un mensaje personalizado generado por AI para tres parámetros: un nombre de Cameron, un nombre de producto de zapatos y el texto "cómodo pero ya se me ha roto el cordón del zapato"][3]

## Hacer referencia a la salida de IA utilizando Liquid
Haz referencia a la salida AI en pasos posteriores insertando la lógica Liquid `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. Puedes configurar la dirección `key_name` en el paso de IA.

Por ejemplo, si utilizas las variables "mensaje" y "puntuación de sentimiento", puedes utilizar `{% raw %}{{ai_step_output.${message}}}{% endraw %}` para personalizar un mensaje posterior en ese mismo Canvas.

También puedes registrar la salida de cualquier paso de IA como un atributo personalizado utilizando el paso en Canvas de actualización de usuario, donde lees la salida del paso de IA (por ejemplo, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Si el resultado no se almacena como atributo personalizado, no se podrá utilizar en ningún otro lugar aparte de los pasos posteriores del mismo Canvas.

## Estadísticas de pasos AI

Los pasos de la IA tienen las siguientes estadísticas a nivel de paso:

- **Continúa con el siguiente paso:** Número de usuarios que procedieron al paso o pasos siguientes en Canvas
- **Lienzo Salido:** Número de usuarios que salieron del Canvas porque tu paso en AI era el último paso
- **Salida correcta:** Número de usuarios para los que el paso de IA generó resultados con éxito
- **Salida fallida:** Número de usuarios para los que el paso AI no generó resultados, en cuyo caso, los usuarios seguirán adelante con los pasos siguientes.

### Comprender los resultados de tus pasos de IA

Hay algunos casos en los que Braze descartará el resultado del paso AI y enviará al cliente al siguiente paso:
- Si la salida supera los 1.024 caracteres
- Si la salida no está en JSON
- Si el aviso no cumple los requisitos de [moderación](https://platform.openai.com/docs/guides/moderation/overview) de OpenAI, que marca el contenido inapropiado generado por el usuario

## Casos de uso del paso AI

### Respuestas sobre los sentimientos del cliente

Como se demuestra en el ejemplo [del paso Crear una IA](#create-ai-step), puedes pedir a la IA que envíe mensajes de seguimiento basados en puntuaciones de sentimiento generadas a partir de las opiniones de los clientes.
- Puntuaciones de sentimiento positivas - Desencadenar una notificación push que pida a los usuarios que dejen una opinión
- Puntuaciones medias de sentimiento - Desencadenar un correo electrónico que pregunte a los usuarios si desean ayuda adicional
- Puntuaciones de sentimiento bajas - Desencadenar un webhook que notifique al servicio de asistencia al usuario, para que un representante de asistencia pueda elaborar un seguimiento matizado.

#### Ejemplo de mensaje AI

Este ejemplo se utilizó en [Crear un paso de IA](#create-ai-step).

Un cliente ha comprado "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`", y ha dado su opinión sobre el producto: "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". Crea una puntuación de sentimiento como un número entero entre 0 y 100. A continuación, crea un mensaje personalizado. Esto debería devolver dos variables, "mensaje" y "puntuación de sentimiento".

### Seguimiento de los cuestionarios

Si realizas un cuestionario en la aplicación o en el navegador con una sección de respuesta libre, puedes utilizar pasos de IA para analizar las respuestas libres y hacer el seguimiento adecuado. 

Por ejemplo, si un comercio minorista de maquillaje tiene un cuestionario en el que pregunta: "¿Qué productos te gustaría nominar para los premios de belleza de este año?", podría utilizar una pregunta que identifique y asigne un atributo a los tipos de productos y marcas favoritos del usuario, y luego personalizar el contenido futuro basándose en estos datos.

#### Ejemplo de mensaje AI

Identifica la marca favorita del usuario utilizando su respuesta. A continuación, crea un mensaje de agradecimiento a los usuarios por rellenar el cuestionario y menciona que los Expertos en Belleza también adoran su marca favorita. Esto debería devolver dos variables, "mensaje" y "marca favorita".

![Pestaña de vista previa de la configuración de pasos de la IA que muestra un mensaje personalizado generado por la IA para el parámetro de respuesta del cuestionario "Me encantan las cremas faciales de Estee Lauder" que agradece al usuario que haya rellenado el cuestionario y, a continuación, le recomienda una crema facial.][4]

### Recomendaciones basadas en el comportamiento

Los clientes pueden pedir a la IA que analice los comportamientos del usuario y envíe mensajes de recomendación. 

Por ejemplo, puedes crear una consulta para analizar las 50 compras más recientes de los usuarios y establecer su categoría de compras más habituales como un nuevo atributo personalizado. Después, puedes enviar recomendaciones por correo electrónico personalizadas para la categoría favorita de cada usuario.

#### Ejemplo de mensaje AI

Un cliente ha comprado los siguientes productos: "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". Identifica la categoría de productos más comprados por el usuario. Esto debería devolver una nueva variable para la "categoría más comprada".

![Pestaña de vista previa de la configuración de pasos de la IA que muestra la variable generada por la IA de "libro" para el parámetro de categoría más comprada.][5]

## Límites de velocidad

Hay un límite de 10 solicitudes por minuto (RPM) por empresa. Esto significa que, para cualquier paso de la IA, hasta 10 usuarios pueden recibir ese paso durante un minuto determinado y cualquier usuario más allá de los 10 avanzará automáticamente al siguiente paso. Cuando comience el siguiente minuto, los usuarios podrán volver a recibir el paso de IA, pero los usuarios anteriores que desencadenaron el límite de velocidad no volverán a intentarlo.

## Limitaciones de los pasos de la IA

- Esta característica aprovecha la GPT-3.5.
- Esta característica utiliza la clave de API Braze OpenAI. No puedes utilizar tu propia clave de API de OpenAI.
- Hay un límite de 5 solicitudes por minuto (RPM) por espacio de trabajo y de 10 RPM por empresa.
- Esta característica no cumple la HIPAA y los clientes no deben enviar ninguna información personal identificable (PII) ni información sanitaria protegida (PHI).

## ¿Cómo se utilizan y envían mis datos a OpenAI?

Para analizar y crear el contenido de tus mensajes, Braze enviará tus mensajes a la Plataforma API de OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que incluyas información identificadora única en el contenido del mensaje que proporciones. Como se detalla en [los Compromisos de la Plataforma API de Open](https://openai.com/policies/api-data-usage-policies)AI, los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Asegúrate de que cumples las políticas de OpenAI relevantes para ti, incluida la [Política de uso](https://openai.com/policies/usage-policies). Braze no ofrece garantías de ningún tipo con respecto a cualquier contenido generado por IA. 

[1]: {% image_buster /assets/img/ai_step1.png %}
[2]: {% image_buster /assets/img/ai_step2.png %}
[3]: {% image_buster /assets/img/ai_step3.png %}
[4]: {% image_buster /assets/img/ai_step4.png %}
[5]: {% image_buster /assets/img/ai_step5.png %} 
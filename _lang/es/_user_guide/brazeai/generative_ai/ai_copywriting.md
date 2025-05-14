---
nav_title: Asistente de redacción AI
article_title: Asistente de redacción AI
page_order: 4
description: "Este artículo de referencia cubre el asistente de redacción de IA, característica que pasa un breve nombre o descripción del producto a la herramienta de generación de textos GPT de OpenAI para generar textos de marketing similares a los humanos para utilizarlos en tus mensajes."
---

# Asistente de redacción AI

> El asistente de redacción de IA pasa un breve nombre o descripción del producto a una herramienta de generación de textos GPT de un proveedor externo, propiedad de OpenAI, para generar textos de marketing similares a los humanos y utilizarlos en tus mensajes. Esta funcionalidad está disponible por defecto para la mayoría de los creadores de mensajes en el panel de Braze.

## Crear copia {#steps}

Para generar textos utilizando el asistente de redacción de IA, sigue estos pasos:

1. En tu creador de mensajes, selecciona <i class="fa-solid fa-wand-magic-sparkles"></i> **Lanzar AI Copywriter**.
   * En el editor de arrastrar y soltar para mensajes dentro de la aplicación, selecciona un bloque de texto y elige <i class="fa-solid fa-wand-magic-sparkles" title="Redactor AI"></i> en la barra de herramientas del bloque.
2. Introduce el nombre o la descripción del producto en el campo de entrada.
3. Selecciona una longitud de salida aproximada. Puedes elegir un canal específico para una longitud de salida basada en las mejores prácticas específicas del canal o seleccionar entre corto (1 frase), medio (2-3 frases) o largo (1 párrafo). 
4. (Opcional) Crea o aplica una directriz de marca para adaptar este texto a tu marca. Estas directrices se guardan en tu espacio de trabajo y son reutilizables una vez creadas. Para más información, consulta [Crear directrices de marca]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).
5. (Opcional) Elige un tono de mensaje de entre las opciones disponibles. Esto determinará el estilo de la copia generada.
6. (Opcional) Disponible para notificaciones push: Selecciona **Referencia a datos de campañas anteriores** para utilizar tus mensajes push para móvil anteriores (campañas y pasos en Canvas) como referencia estilística para generar una nueva copia. Cuando se selecciona, la salida imitará el estilo de tus mensajes anteriores.
7. Selecciona el idioma de salida. Puede ser diferente de tu lengua de entrada.
8. Seleccione **Generar**.

Utilizamos la información que nos proporcionas para pedir a GPT que escriba textos para ti. La respuesta se obtendrá de OpenAI y se te proporcionará. 

![Asistente de redacción AI modal que muestra varias características disponibles"][1]{: style="max-width:70%;"}

{% alert important %}
Filtramos las respuestas de contenido ofensivo que infringe la [política de contenidos](https://beta.openai.com/docs/usage-guidelines/content-policy) de OpenAI.
{% endalert %}

## Utilizar datos de campañas anteriores

Cuando utilices push como longitud de salida, si seleccionas **Datos de campañas anteriores de referencia**, se enviarán a OpenAI campañas móviles push anteriores seleccionadas al azar para que GPT pueda utilizarlas como base para su generación de copias. Deja esta casilla sin marcar si no quieres aprovechar esta capacidad. Consulta las secciones siguientes para obtener más información sobre cómo utilizan tus datos Braze y OpenAI. 

Si se utiliza junto con una directriz de [marca]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/), tanto la directriz de marca como los datos de la campaña anterior se incorporarán al resultado final.

## ¿Qué es la GPT?

[GPT](https://openai.com/product/gpt-4) es la herramienta de generación de lenguaje natural de última generación de OpenAI impulsada por inteligencia artificial. Puede realizar diversas tareas de lenguaje natural, como generar, completar y clasificar textos. Lo hemos integrado en el panel de Braze para ayudarte a inspirar y diversificar tu copia directamente mientras trabajas.

## ¿Cómo se utilizan y envían mis datos a OpenAI?

Para generar la copia, Braze enviará tu consulta a OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar de quién se envió la consulta a menos que incluyas información identificadora única en la entrada que proporciones o en los datos de tu campaña anterior al habilitar la opción denominada "Referencia a datos de campañas anteriores". Según [la política de OpenAI](https://openai.com/policies/api-data-usage-policies), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Entre tú y Braze, cualquier contenido generado utilizando GPT es de tu propiedad intelectual. Braze no hará valer ninguna reclamación de propiedad de derechos de autor sobre dicho contenido y no ofrece ninguna garantía de ningún tipo con respecto a cualquier contenido generado por IA.

## Más herramientas de IA

También puedes [generar una imagen utilizando IA]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai) de la biblioteca multimedia. Esto aprovecha [DALL-E 3](https://openai.com/index/dall-e-3/), un sistema de IA de OpenAI que puede crear imágenes y arte realistas a partir de una descripción en lenguaje natural.

[1]: {% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"

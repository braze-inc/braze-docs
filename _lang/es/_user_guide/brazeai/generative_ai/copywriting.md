---
nav_title: Redacción publicitaria
article_title: Asistente de redacción AI
page_order: 2.1
description: "Este artículo de referencia cubre el asistente de redacción de IA, característica que pasa un breve nombre o descripción del producto a la herramienta de generación de textos GPT de OpenAI para generar textos de marketing similares a los humanos para utilizarlos en tus mensajes."
---

# Generar copia con <sup>BrazeAITM</sup>

> El asistente de redacción de IA pasa un breve nombre o descripción del producto a una herramienta de generación de textos GPT de un proveedor externo, propiedad de OpenAI, para generar textos de marketing similares a los humanos y utilizarlos en tus mensajes. Esta funcionalidad está disponible por defecto para la mayoría de los creadores de mensajes en el panel de Braze.

## Generar copia

### Paso 1: Lanzamiento AI redactor

En tu creador de mensajes, selecciona <i class="fa-solid fa-wand-magic-sparkles"></i> **Lanzar AI Copywriter**.

En el editor de arrastrar y soltar para mensajes dentro de la aplicación, selecciona un bloque de texto y elige <i class="fa-solid fa-wand-magic-sparkles" title="Redactor AI"></i> en la barra de herramientas del bloque.

### Paso 2: Introduce los datos

Introduce el nombre o la descripción de un producto en el campo de entrada y, a continuación, selecciona una longitud de salida aproximada.

Puedes elegir un canal específico para una longitud de salida basada en las mejores prácticas específicas del canal o seleccionar entre corto (1 frase), medio (2-3 frases) o largo (1 párrafo).

### Paso 3: Personalízalo más (opcional)

Para personalizar aún más tu copia, puedes:

- **Aplica las directrices de la marca:** Después de [generar directrices de marca con <sup>BrazeAITM</sup>]({{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines), puedes utilizarlas como ayuda para generar tu texto.
- **Elige un tono:** Cada tono generará copia en un estilo diferente. Elige el tono que mejor se adapte a la voz de tu marca.
- **Consulta los datos de campañas anteriores**: Cuando están habilitadas, las notificaciones push móviles anteriores enviadas a través de tus campañas o pasos en Canvas se utilizan como referencia estilística para generar tu nueva copia. Para más información, consulta [Utilizar datos de campañas anteriores](#past-campaign-data).
- **Auto-traducir copia:** Puedes elegir un idioma de salida diferente para tu copia. El contenido generado saldrá en ese idioma.

### Paso 4: Genera tu copia

Cuando hayas terminado, selecciona **Generar**. Utilizaremos la información que nos proporciones para pedir a GPT que escriba un texto para ti. La respuesta se obtendrá de OpenAI y se te proporcionará. Para más información, consulta [¿Cómo se utilizan y envían mis datos a OpenAI?](#ai-policy)

![AI copywriting assistant modal showing various features available"]({% image_buster /assets/img/ai_copywriter/gpt3.png %} "GPT3"){: style="max-width:70%;"}

{% alert important %}
Filtramos las respuestas de contenido ofensivo que infringe la [política de contenidos](https://beta.openai.com/docs/usage-guidelines/content-policy) de OpenAI.
{% endalert %}

## Acerca de los datos de campañas anteriores {#past-campaign-data}

Cuando utilices push como longitud de salida, si seleccionas **Datos de campañas anteriores de referencia**, se enviarán a OpenAI campañas móviles push anteriores seleccionadas al azar para que GPT pueda utilizarlas como base para su generación de copias. Deja esta casilla sin marcar si no quieres aprovechar esta capacidad. Consulta las secciones siguientes para obtener más información sobre cómo utilizan tus datos Braze y OpenAI. 

Si se utiliza junto con una directriz de [marca]({{site.baseurl}}/user_guide/brazeai/generative_ai//brand_guidelines/), tanto la directriz de marca como los datos de la campaña anterior se incorporarán al resultado final.

{% multi_lang_include brazeai/generative_ai/policy.md %}

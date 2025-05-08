---
nav_title: Directrices de marca
article_title: Directrices de marca para la redacción de textos sobre IA
page_order: 1
description: "Este artículo de referencia cubre las directrices de marca para el asistente de redacción AI, una característica que te permite adaptar el estilo de la copia generada por el asistente de redacción AI a la voz y el estilo de tu marca."
---

# Directrices de marca para el asistente de redacción AI

> Adapta el estilo de tus textos generados por IA para que coincidan con la voz y la personalidad de tu marca con directrices de marca personalizadas.

## Crear directrices de marca {#steps}

Sigue estos pasos para crear directrices de marca en el asistente de redacción de IA. También puedes crear directrices de marca en la página de configuración de [Directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines/).

### Paso 1: Crear una directriz de marca

1. En tu creador de mensajes, selecciona <i class="fa-solid fa-wand-magic-sparkles"></i> **Lanzar AI Copywriter**.
   * En el editor de arrastrar y soltar para mensajes dentro de la aplicación, selecciona un bloque de texto y elige <i class="fa-solid fa-wand-magic-sparkles" title="Redactor AI"></i> en la barra de herramientas del bloque.
2. Selecciona **Aplicar directriz de marca** y luego **Crear una directriz de marca**.
3. Introduce un nombre para esta directriz. Será la etiqueta que ves en la selección anterior.
4. Para **¿Cuándo utilizarás estas directrices de marca?**, añade detalles para ayudar a tus colegas (y a ti en el futuro) a comprender el contexto de utilización de esta directriz.
5. Si quieres que ésta sea la directriz de marca predeterminada para el espacio de trabajo actual, marca **Usar como directriz de marca predeterminada**.

![Vista de la creación de la directriz de marca.][1]

### Paso 2: Describe la personalidad de tu marca

Para la **personalidad de** marca, piensa en lo que hace única a tu marca. Incluye rasgos, valores, voz y cualquier arquetipo que defina tu marca. Aquí tienes algunas características a tener en cuenta:

| **Característica**       | **Definición**                                                                       | **Ejemplo**                                                        |
|--------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Reputación               | Cómo quieres que se perciba tu marca en el mercado.                               | Somos conocidos por ser la marca más fiable y orientada al cliente de nuestro sector. |
| Rasgos de personalidad       | Características similares a las humanas que describen el carácter de tu marca.                     | Nuestra marca es amable, accesible y siempre optimista.          |
| Valores                   | Valores fundamentales que guían las acciones y decisiones de tu marca.                           | Valoramos la sostenibilidad, la transparencia y la comunidad.            |
| Diferenciación          | Cualidades únicas que diferencian tu marca de la competencia.                         | Nos distinguimos por ofrecer un servicio al cliente personalizado que va más allá. |
| Voz de marca              | El tono y el estilo de comunicación que utiliza tu marca.                                 | Nuestra voz es informal pero informativa, garantizando la claridad sin ser demasiado formal. |
| Arquetipo de marca          | El arquetipo que representa a la persona de tu marca (El Héroe, El Creador, etc.).    | Encarnamos el arquetipo del "Explorador", siempre en busca de nuevos retos y aventuras. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paso 3: Definir el lenguaje que debe evitarse (opcional)

En **Exclusiones**, enumera cualquier lenguaje o estilo que no se ajuste a tu marca. Por ejemplo, quizá quieras evitar el "sarcasmo", las "actitudes negativas" o los tonos "condescendientes".

### Paso 4: Prueba tus directrices

Pon a prueba tus directrices para ver cómo rinden. Amplía **Prueba tus directrices** para generar un texto de ejemplo y ajústalo según sea necesario.

### Paso 5: Guarda tus directrices

Cuando estés satisfecho con tus directrices, selecciona **Guardar directriz de marca**. Tus nuevas directrices se guardarán en tu espacio de trabajo para utilizarlas en el futuro.

{% alert important %}
Puedes cambiar el idioma de salida independientemente del idioma en que esté tu copia, pero ni Braze ni OpenAI garantizan la calidad de la traducción. Prueba y verifica siempre las traducciones antes de utilizarlas.
{% endalert %}

## Pautas de edición

Para editar tus directrices de marca existentes:

1. Abre el asistente de redacción AI.
2. Aplica las directrices de marca que quieras cambiar. Aparecerá un botón cerca del campo.
3. Selecciona **Editar directriz**.

## ¿Cómo se utilizan y envían mis datos a OpenAI?

Para generar copia utilizando una directriz de marca, Braze enviará tu consulta incluyendo el contenido de tu directriz a OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar de quién se envió la consulta a menos que incluyas información identificadora única en la entrada que proporciones o en los datos de tu campaña anterior al habilitar la opción denominada "Referencia a datos de campañas anteriores". Según [la política de OpenAI](https://openai.com/policies/api-data-usage-policies), los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Entre tú y Braze, cualquier contenido generado utilizando GPT es de tu propiedad intelectual. Braze no hará valer ninguna reclamación de propiedad de derechos de autor sobre dicho contenido y no ofrece ninguna garantía de ningún tipo con respecto a cualquier contenido generado por IA.


[1]: {% image_buster /assets/img/ai_copywriter/manual_brand_guidelines.png %} "Directrices de marca"

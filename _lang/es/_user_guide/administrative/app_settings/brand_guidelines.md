---
nav_title: Directrices de marca
article_title: Directrices de marca
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo crear, administrar y utilizar las directrices de marca que pueden aplicarse a tus mensajes a través del asistente de redacción de IA."
---

# Directrices de marca

> Adapta el estilo de tus textos generados por IA para que coincidan con la voz, el tono y la personalidad de tu marca con directrices de marca personalizadas.

Puedes crear y administrar tus directrices de marca yendo a **Configuración** > **Directrices de marca**. También puedes crearlos en el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/).

## Crear directrices de marca

### Paso 1: Crear una directriz de marca

En la página **Directrices de marca**, selecciona **Crear nuevo**. Si quieres que esta directriz de marca sea la predeterminada para el espacio de trabajo, marca **Usar como directriz de marca predeterminada**. Puedes tener un predeterminado por espacio de trabajo.

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

![La ventana "Crear directriz de marca" con campos para introducir el nombre, la descripción, la personalidad, las exclusiones y el tono.][1]

### Paso 4: Prueba tus directrices

Pon a prueba tus directrices para ver cómo rinden. Amplía **Prueba tus directrices** para generar un texto de ejemplo y ajústalo según sea necesario.

### Paso 5: Guarda tus directrices

Cuando estés satisfecho con tus directrices, selecciona **Guardar directriz de marca**. Tus nuevas directrices se guardarán en tu espacio de trabajo para utilizarlas en el futuro.

{% alert important %}
Puedes cambiar el idioma de salida independientemente del idioma en que esté tu copia, pero ni Braze ni OpenAI garantizan la calidad de la traducción. Prueba y verifica siempre las traducciones antes de utilizarlas.
{% endalert %}

## Gestión de las directrices de la marca

Puedes editar las directrices de marca seleccionándolas en la página **Directrices de marca**. Archiva una directriz de marca para hacerla inactiva y eliminarla del asistente de redacción AI. Para que vuelva a estar activa y seleccionable, puedes filtrar las directrices de marca archivadas y luego desarchivarlas.

![La página "Directrices de marca" filtró las directrices de marca archivadas.][4]

## Utilizar directrices de marca

Cuando redactes un mensaje, abre el [asistente de redacción de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/) y selecciona tu directriz de marca en el desplegable **Aplicar directriz de marca**. Si designas una pauta de marca concreta como predeterminada, se seleccionará automáticamente en el desplegable, pero puedes elegir una pauta diferente. 

!["AI copywriting assistant" con "Alertas importantes!!" seleccionada como directriz de la marca.][2]

## ¿Cómo se utilizan y envían mis datos a OpenAI?

Para generar copia utilizando una directriz de marca, Braze enviará tu consulta incluyendo el contenido de tu directriz a OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar de quién se envió la consulta a menos que incluyas información identificadora única en la entrada que proporciones o en los datos de tu campaña anterior al habilitar la opción denominada "Referencia a datos de campañas anteriores". Según [la política de OpenAI](https://openai.com/policies/api-data-usage-policies), los datos enviados a la API de OpenAI mediante Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Entre tú y Braze, cualquier contenido generado utilizando GPT es de tu propiedad intelectual. Braze no hará valer ninguna reclamación de propiedad de derechos de autor sobre dicho contenido y no ofrece ninguna garantía de ningún tipo con respecto a cualquier contenido generado por IA.

[1]: {% image_buster /assets/img/guidelines_create.png %}
[2]: {% image_buster /assets/img/guidelines_ai_assistant.png %}
[4]: {% image_buster /assets/img/unarchive_brand_guideline.png %}
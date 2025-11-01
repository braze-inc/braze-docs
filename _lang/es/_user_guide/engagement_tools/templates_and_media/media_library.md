---
nav_title: Mediateca
article_title: Mediateca
page_order: 0
page_type: reference
description: "Este artículo de referencia trata de la mediateca. Aquí puedes aprender a gestionar tus activos en una única ubicación centralizada, generar imágenes mediante IA, acceder a los medios en tu creador de mensajes."
tool: Media

---

# Mediateca

> La biblioteca multimedia te permite administrar tus activos en una única ubicación centralizada. 

## Mediateca vs. CDN

El uso de la biblioteca multimedia en lugar de una red de entrega de contenidos (CDN) proporciona un mejor almacenamiento en caché y rendimiento para los mensajes dentro de la aplicación. Todos los activos de la biblioteca multimedia que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la biblioteca multimedia está integrada con los compositores de Braze, lo que permite a los especialistas en marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar las URL de las imágenes.

## Acceder a la mediateca

Dentro de la biblioteca multimedia, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. Para acceder a tu biblioteca multimedia Braze, ve a ESTO > Plantillas **.** Aquí puedes hacerlo:

* Sube varias imágenes a la vez
* Cargar archivos de contactos virtuales (.vcf)
* Subir archivos de video para usarlos en mensajes de WhatsApp
* Sube una carpeta con tus imágenes (máximo 50 imágenes)
* [Genera una imagen utilizando IA](#generate-ai) y guárdala en la biblioteca multimedia
* Recorta una imagen existente para crear la proporción adecuada para tus mensajes
* Añade etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la parrilla de la biblioteca multimedia
* Arrastra y suelta las imágenes o carpetas que quieras subir
* Borrar imágenes

\![Página de la biblioteca multimedia que incluye una sección "Subir a la biblioteca" para arrastrar y soltar o subir archivos. También hay una lista de contenidos cargados en la biblioteca multimedia.]({% image_buster /assets/img_archive/media_library_main.png %})

Más tarde, cuando redactes un mensaje en Braze, podrás extraer tus imágenes de la biblioteca multimedia.

Dos formas habituales de acceder a la biblioteca multimedia en función del creador de mensajes. Uno muestra el editor de arrastrar y soltar del correo electrónico con el título "Imágenes y GIFs" y un botón para "Añadir desde la biblioteca multimedia". La otra muestra los editores estándar, como los mensajes push y dentro de la aplicación, con el título "Medios" y un botón para "Añadir imagen".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para obtener más ayuda con la biblioteca de medios, consulta nuestras [Plantillas & Preguntas frecuentes sobre medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificaciones de imagen

Todas las imágenes subidas a la biblioteca multimedia deben ocupar menos de 5 MB. Los tipos de archivo admitidos son PNG, JPEG, GIF y SVG. Para recomendaciones específicas de imágenes por canal de mensajería, consulta las secciones siguientes.

### Tarjetas de contenido

{% multi_lang_include image_specs.md variable_name='content cards' %}

### Correo electrónico

{% multi_lang_include image_specs.md variable_name="email"  %}

### Mensajes dentro de la aplicación

{% multi_lang_include image_specs.md variable_name="in-app messages"  %}

Para más información, consulta [Detalles creativos de los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="push notifications"  %}

{% alert note %}
Para obtener recursos adicionales, consulta [Especificaciones de imagen y texto push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Video

Por ahora, los videos que se suban a la biblioteca multimedia sólo podrán utilizarse en mensajes de WhatsApp. Para más información, consulta [Crear un mensaje de Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Generar imágenes con <sup>BrazeAITM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de utilizar esta característica, revisa [cómo se utilizan y envían tus datos a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}

---
nav_title: Mediateca
article_title: Mediateca
page_order: 0
page_type: reference
description: "Este artículo de referencia trata de la biblioteca multimedia. Aquí puedes aprender a administrar tus activos en una única ubicación centralizada, generar imágenes mediante IA y acceder a los medios en tu creador de mensajes."
tool: Media

---

# Mediateca

> La mediateca le permite gestionar sus activos en una única ubicación centralizada. 

## Biblioteca multimedia frente a CDN

El uso de la biblioteca multimedia en lugar de una CDN proporciona un mejor almacenamiento en caché y un mejor rendimiento para los mensajes dentro de la aplicación. Todos los recursos de la biblioteca multimedia que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la biblioteca multimedia está integrada con los compositores Braze, lo que permite a los profesionales del marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar URL de imágenes.

## Acceso a la biblioteca multimedia

En la biblioteca multimedia, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. Para acceder a tu biblioteca multimedia de Braze, ve a **Plantillas** > **Biblioteca multimedia**. Aquí puedes:

* Cargar varias imágenes a la vez
* Cargar archivos de contactos virtuales (.vcf)
* Subir archivos de video para utilizarlos en mensajes de WhatsApp
* Sube una carpeta con tus imágenes (hasta 50 imágenes).
* [Genera una imagen utilizando IA](#generate-ai) y guárdala en la biblioteca multimedia
* Recorta una imagen existente para crear la proporción adecuada para tus mensajes
* Añade etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la cuadrícula de la biblioteca multimedia
* Arrastre y suelte las imágenes o carpetas que desee cargar
* Borrar imágenes

![Página de biblioteca multimedia que incluye una sección "Cargar en biblioteca" para arrastrar y soltar o cargar archivos. También hay una lista de contenidos cargados en la biblioteca multimedia.]({% image_buster /assets/img_archive/media_library_main.png %})

Más adelante, al redactar un mensaje en Braze, podrás importar tus imágenes desde la biblioteca multimedia.

![Dos formas habituales de acceder a la mediateca en función del compositor del mensaje. Una muestra el Editor de arrastrar y soltar del correo electrónico con el título "Imágenes y GIFs" y un botón para "Añadir desde la biblioteca multimedia". El otro muestra los editores estándar, como los mensajes push y los mensajes dentro de la aplicación, con el título «Medios» y un botón para «Añadir imagen».]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para obtener más información sobre la biblioteca multimedia, consulta las [preguntas frecuentes sobre plantillas&multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificaciones de imagen

Todas las imágenes subidas a la biblioteca multimedia deben ocupar menos de 5 MB. Los tipos de archivo compatibles son PNG, JPEG, GIF, SVG y WebP. Para recomendaciones específicas de imágenes por canal de mensajería, consulte las secciones siguientes.

{% alert important %}
Es posible que los GIF con formas muy alargadas (por ejemplo, 3000 x 2 píxeles) o 300 o más fotogramas no se puedan cargar, incluso si el tamaño total del archivo es pequeño.
{% endalert %}

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
Para obtener recursos adicionales, consulta [las especificaciones de imágenes y texto para push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Video

Los videos subidos a la biblioteca multimedia solo se pueden utilizar en mensajes de WhatsApp. Para obtener más información, consulta [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Generación de imágenes con BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de utilizar esta característica, revisa [cómo se utilizan tus datos y cómo se envían a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}

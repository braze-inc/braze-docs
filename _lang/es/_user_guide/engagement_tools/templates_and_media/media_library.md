---
nav_title: Biblioteca de medios
article_title: Biblioteca de medios
page_order: 0
page_type: reference
description: "Este artículo de referencia trata de la biblioteca multimedia. Aquí podrá aprender a gestionar sus activos en una ubicación única y centralizada, generar imágenes mediante IA y acceder a los medios en el compositor de mensajes."
tool: Media

---

# Mediateca

> La mediateca le permite gestionar sus activos en una única ubicación centralizada. 

## Mediateca vs. CDN

El uso de la biblioteca multimedia en lugar de una red de entrega de contenidos (CDN) proporciona un mejor almacenamiento en caché y rendimiento para los mensajes dentro de la aplicación. Todos los recursos de la biblioteca multimedia que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la biblioteca multimedia está integrada con los compositores Braze, lo que permite a los profesionales del marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar URL de imágenes.

## Acceder a la mediateca

Dentro de la biblioteca multimedia, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. Para acceder a tu biblioteca multimedia Braze, ve a ESTO > Plantillas **.** Aquí puedes hacerlo:

* Cargar varias imágenes a la vez
* Cargar archivos de contactos virtuales (.vcf)
* Subir archivos de video para utilizarlos en mensajes de WhatsApp
* Sube una carpeta con tus imágenes (máximo 50 imágenes)
* [Genera una imagen utilizando IA](#generate-ai) y guárdala en la biblioteca multimedia
* Recorta una imagen existente para crear la proporción adecuada para tus mensajes
* Añade etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la cuadrícula de la biblioteca multimedia
* Arrastre y suelte las imágenes o carpetas que desee cargar
* Borrar imágenes

![Página de biblioteca multimedia que incluye una sección "Cargar en biblioteca" para arrastrar y soltar o cargar archivos. También hay una lista de contenidos cargados en la biblioteca multimedia.]({% image_buster /assets/img_archive/media_library_main.png %})

Más tarde, cuando redactes un mensaje en Braze, podrás extraer tus imágenes de la biblioteca multimedia.

![Dos formas habituales de acceder a la mediateca en función del compositor del mensaje. Una muestra el Editor de arrastrar y soltar del correo electrónico con el título "Imágenes y GIFs" y un botón para "Añadir desde la biblioteca multimedia". La otra muestra los editores estándar, como los mensajes push y dentro de la aplicación, con el título "Medios" y un botón para "Añadir imagen".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Si necesitas más ayuda con la mediateca, consulta nuestras [Preguntas frecuentes sobre plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificaciones de imagen

Todas las imágenes subidas a la biblioteca multimedia deben ocupar menos de 5 MB. Los tipos de archivo admitidos son PNG, JPEG, GIF y SVG. Para recomendaciones específicas de imágenes por canal de mensajería, consulte las secciones siguientes.

### Tarjetas de contenido

{% multi_lang_include image_specs.md variable_name='tarjetas de contenido' %}

### Correo electrónico

{% multi_lang_include image_specs.md variable_name="email"  %}

### Mensajes dentro de la aplicación

{% multi_lang_include image_specs.md variable_name="mensajes in-app"  %}

Para más información, consulta [Detalles creativos de los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

### Push

{% multi_lang_include image_specs.md variable_name="notificaciones push"  %}

{% alert note %}
Para obtener recursos adicionales, consulta [Especificaciones de imagen y texto push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)
{% endalert %}

### Video

Por ahora, los videos subidos a la biblioteca multimedia sólo pueden utilizarse en mensajes de WhatsApp. Para más información, consulta [Crear un mensaje de Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
La adición de videos a los mensajes de WhatsApp está actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Generar imágenes con <sup>BrazeAITM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de utilizar esta característica, revisa [cómo se utilizan y envían tus datos a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}

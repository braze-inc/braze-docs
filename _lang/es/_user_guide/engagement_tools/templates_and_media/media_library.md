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

Encontrará la **Mediateca** en **Plantillas**.

Puedes utilizar la **Mediateca** para:

* Cargar varias imágenes a la vez
* Cargar archivos de contactos virtuales (.vcf)
* Subir archivos de video para usarlos en mensajes de WhatsApp
* Sube una carpeta con tus imágenes (máximo 50 imágenes)
* [Genera una imagen utilizando IA](#generate-ai) y guárdala en la biblioteca multimedia
* Recorta una imagen existente para crear la proporción adecuada para tus mensajes
* Añade etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la cuadrícula de la biblioteca multimedia
* Arrastre y suelte las imágenes o carpetas que desee cargar
* Borrar imágenes

![Página de biblioteca multimedia que incluye una sección "Cargar en biblioteca" para arrastrar y soltar o cargar archivos. También hay una lista de contenidos cargados en la biblioteca multimedia.][1]

{% alert tip %} Si necesitas más ayuda con la mediateca, consulta nuestras [Preguntas frecuentes sobre plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Detalles de la imagen

Dentro de la biblioteca multimedia, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. 

### Utilizar la mediateca frente a una CDN

El uso de la biblioteca multimedia mejora el almacenamiento en caché y el rendimiento de los mensajes dentro de la aplicación. Todos los recursos de la biblioteca multimedia que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la biblioteca multimedia está integrada con los compositores Braze, lo que permite a los profesionales del marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar URL de imágenes.

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

##### Más recursos

- [Especificaciones de imagen y texto push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#image-and-text-specifications)

### Video

Por ahora, los videos que se suban a la biblioteca multimedia sólo podrán utilizarse en mensajes de WhatsApp. Para más información, consulta [Crear un mensaje de Whatsapp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

{% alert important %}
Añadir videos a los mensajes de WhatsApp se encuentra actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

## Acceso a la mediateca desde un compositor de mensajes

La mediateca actúa como ubicación centralizada de activos en el panel de control, ya que todas las imágenes se cargan directamente en ella. Esto te permite reutilizar imágenes en diferentes mensajes.

![Dos formas habituales de acceder a la mediateca en función del compositor del mensaje. Una muestra el Editor de arrastrar y soltar del correo electrónico con el título "Imágenes y GIFs" y un botón para "Añadir desde la biblioteca multimedia". La otra muestra los editores estándar, como los mensajes push y dentro de la aplicación, con el título "Multimedia" y un botón para "Añadir imagen".][1.5]{: style="border:none"}

## Generar una imagen utilizando IA {#generate-ai}

Puedes generar imágenes para tu biblioteca multimedia utilizando [DALL-E 3](https://openai.com/index/dall-e-3/), un sistema de IA de OpenAI, un proveedor externo de Braze. Este sistema puede crear imágenes y arte realistas a partir de una descripción en lenguaje natural. Cada solicitud genera cuatro variaciones de su mensaje, y su empresa puede generar imágenes 10 veces al día. Este total se aplica a todos los usuarios de su empresa.

1. En la biblioteca multimedia, seleccione <i class="fas fa-wand-magic-sparkles"></i> **AI Image Generator**.
2. Introduce una descripción de la imagen que quieres generar, de hasta 300 caracteres. Cuanto más detallada sea la descripción, mejor será el resultado. Esta característica sólo admite la introducción de texto: no es posible cargar una imagen como referencia.
3. Seleccione **Generar imágenes**. Las imágenes pueden tardar aproximadamente un minuto en generarse.
4. Selecciona <i class="fas fa-download" title="Añadir imagen a la biblioteca multimedia"></i> sobre las imágenes que quieras añadir a tu biblioteca multimedia.

![Modal de generador de imágenes con IA en la biblioteca multimedia.][6]{: style="max-width:75%"}

Entre tú y Braze, cualquier imagen generada utilizando DALL-E 3 es de tu propiedad intelectual. Braze no hará valer ningún derecho de propiedad intelectual sobre tales imágenes y no establecerá ningún tipo de garantía con respecto a los contenidos o las imágenes generados por IA.

Para generar imágenes, Braze enviará tu consulta a la Plataforma API de OpenAI. Todas las consultas enviadas a OpenAI desde Braze son anónimas, lo que significa que OpenAI no podrá identificar desde quién se envió la consulta a menos que usted incluya información identificable de forma única en la entrada que proporcione. Como se detalla en [los Compromisos de la Plataforma API de Open](https://openai.com/policies/api-data-usage-policies)AI, los datos enviados a la API de OpenAI a través de Braze no se utilizan para entrenar o mejorar sus modelos y se eliminarán al cabo de 30 días. Por favor, asegúrate de que cumples las políticas de OpenAI relevantes para ti, que pueden incluir su [Política de Uso](https://openai.com/policies/usage-policies) y su [Política de Compartir y Publicar](https://openai.com/policies/sharing-publication-policy). Braze no ofrece garantías de ningún tipo con respecto a cualquier contenido generado por IA. 


[1]: {% image_buster /assets/img_archive/media_library_main.png %}
[1,5]: {% image_buster /assets/img_archive/media_library_composers.png %}
[2]: {% image_buster /assets/img_archive/media_library_crop1.png %}
[3]: {% image_buster /assets/img_archive/media_library_crop2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[5]: https://imageoptim.com/mac
[6]: {% image_buster /assets/img_archive/media_library_dalle.png %}

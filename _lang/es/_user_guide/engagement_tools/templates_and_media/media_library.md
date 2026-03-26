---
nav_title: Mediateca
article_title: Mediateca
page_order: 0
page_type: reference
description: "Este artículo de referencia trata de la biblioteca multimedia. Aquí puedes aprender a administrar tus activos en una única ubicación centralizada, generar imágenes mediante IA y acceder a los medios en tu creador de mensajes."
tool: Media

---

# Mediateca

> La mediateca te permite administrar tus activos en una única ubicación centralizada. 

## Biblioteca multimedia frente a CDN

El uso de la biblioteca multimedia en lugar de una CDN proporciona un mejor almacenamiento en caché y un mejor rendimiento para los mensajes dentro de la aplicación. Todos los activos de la biblioteca multimedia que se encuentren en un mensaje dentro de la aplicación se almacenarán previamente en caché para una visualización más rápida y estarán disponibles para su visualización sin conexión. Además, la biblioteca multimedia está integrada con los compositores de Braze, lo que permite a los especialistas en marketing seleccionar o etiquetar imágenes en lugar de copiar y pegar URL de imágenes.

## Acceso a la biblioteca multimedia

En la biblioteca multimedia, puedes ver el tipo de activo, el tamaño, las dimensiones, la URL, la fecha en que se añadió a la biblioteca y otra información. Para acceder a tu biblioteca multimedia de Braze, ve a **Plantillas** > **Biblioteca multimedia**. Aquí puedes:

* Cargar varias imágenes a la vez
* Cargar archivos de contactos virtuales (.vcf)
* Cargar archivos de video para utilizarlos en mensajes de WhatsApp
* Cargar una carpeta con tus imágenes (hasta 50 imágenes)
* [Generar una imagen utilizando IA](#generate-ai) y guardarla en la biblioteca multimedia
* Recortar una imagen existente para crear la proporción adecuada para tus mensajes
* Añadir etiquetas o equipos para organizar mejor tus imágenes
* Buscar por etiquetas o equipos en la cuadrícula de la biblioteca multimedia
* Arrastrar y soltar imágenes o carpetas para cargarlas
* Eliminar imágenes

![Página de biblioteca multimedia que incluye una sección "Cargar en biblioteca" para arrastrar y soltar o cargar archivos. También hay una lista de contenidos cargados en la biblioteca multimedia.]({% image_buster /assets/img_archive/media_library_main.png %})

Más adelante, al redactar un mensaje en Braze, podrás importar tus imágenes desde la biblioteca multimedia.

![Dos formas habituales de acceder a la mediateca en función del creador de mensajes. Una muestra el editor de arrastrar y soltar del correo electrónico con el título "Imágenes y GIFs" y un botón para "Añadir desde la biblioteca multimedia". La otra muestra los editores estándar, como los mensajes push y los mensajes dentro de la aplicación, con el título "Medios" y un botón para "Añadir imagen".]({% image_buster /assets/img_archive/media_library_composers.png %}){: style="border:none"}

{% alert tip %} Para obtener más información sobre la biblioteca multimedia, consulta las [preguntas frecuentes sobre plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/faqs). {% endalert %}

## Especificaciones de imagen

Todas las imágenes cargadas en la biblioteca multimedia deben ocupar menos de 5&nbsp;MB. Los tipos de archivo compatibles son PNG, JPEG, GIF, SVG y WebP. Para recomendaciones específicas de imágenes por canal de mensajería, consulta las secciones siguientes.

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

#### Longitudes de mensaje recomendadas

Para obtener los mejores resultados, consulta las siguientes directrices de longitud de mensaje al redactar mensajes push. Puede haber cierta variación dependiendo de la presencia de una imagen, el estado de la notificación (iOS) y la configuración de visualización del dispositivo del usuario, así como del tamaño del dispositivo.

| Tipo de mensaje | Longitud recomendada (solo texto) | Longitud recomendada (enriquecido) |
| --- | --- | --- |
| Pantalla de bloqueo de iOS | 160 caracteres | 130 caracteres |
| Centro de notificaciones de iOS | 160 caracteres | 130 caracteres |
| Alerta de banner de iOS | 80 caracteres | 65 caracteres |
| Pantalla de bloqueo de Android | 49 caracteres | N/A |
| Panel de notificaciones de Android | 597 caracteres | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

Para más información sobre el conteo de caracteres en iOS, consulta las [directrices de conteo de caracteres en iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/#character-count).

#### Notificación push web

{% tabs %}
{% tab Imágenes %}

| Navegador | Tamaño de icono recomendado |
| --- | --- |
| Chrome | 192 x 192 px o mayor |
| Firefox | 192 x 192 px o mayor |
| Safari | 192 x 192 px o mayor (configurable por campaña con Safari 16 en macOS 13+) |
| Opera | 192 x 192 px o mayor |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

| Navegador | Plataforma | Tamaño de imagen grande |
| --- | --- | --- |
| Chrome | Android | Relación de aspecto 2:1 |
| Firefox | Android | N/A |
| Chrome | Windows | Relación de aspecto 2:1 |
| Edge | Windows | Relación de aspecto 2:1 |
| Firefox | Windows | N/A |
| Opera | Windows | Relación de aspecto 2:1 |
| Chrome | MacOS | N/A |
| Safari | MacOS | N/A |
| Firefox | MacOS | N/A |
| Opera | MacOS | N/A |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Texto %}

| Navegador | Plataforma | Longitud máxima del título | Longitud máxima del cuerpo |
| --- | --- | --- | --- |
| Chrome | Android | 35 | 50 |
| Firefox | Android | 35 | 50 |
| Chrome | Windows | 50 | 120 |
| Edge | Windows | 50 | 120 |
| Firefox | Windows | 54 | 200 |
| Opera | Windows | 50 | 120 |
| Chrome | MacOS | 35 | 50 |
| Safari | MacOS | 38 | 84 |
| Firefox | MacOS | 38 | 42 |
| Opera | MacOS | 38 | 42 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

#### Ejemplos de notificaciones push

{% tabs %}
{% tab iOS %}

![Notificación push de iOS con texto que dice: "¡Hola! Esta es una notificación push de iOS con una imagen" con un emoji. Hay una imagen pequeña junto al texto.]({% image_buster /assets/img_archive/braze_richpush1.png %}){: style="max-width:50%;"}
![Notificación push de iOS expandida con el mismo texto del mensaje anterior y una imagen ampliada que precede al texto.]({% image_buster /assets/img_archive/braze_richpush2.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Android %}

![Notificación push de Android con una imagen grande debajo del texto del mensaje.]({% image_buster /assets/img_archive/android_push_img2.png %})

{% alert note %}
Las notificaciones con imágenes grandes se muestran mejor cuando se utiliza una imagen de al menos 600 x 300 píxeles.
{% endalert %}

{% endtab %}
{% endtabs %}

### Video

Los videos cargados en la biblioteca multimedia solo se pueden utilizar en mensajes de WhatsApp. Para obtener más información, consulta [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#outbound-messages).

## Generación de imágenes con BrazeAI<sup>TM</sup> {#generate-ai}

{% multi_lang_include brazeai/generative_ai/about_images.md %}

{% alert important %}
Antes de utilizar esta característica, revisa [cómo se utilizan tus datos y cómo se envían a OpenAI]({{site.baseurl}}/user_guide/brazeai/generative_ai/images/#ai-policy).
{% endalert %}
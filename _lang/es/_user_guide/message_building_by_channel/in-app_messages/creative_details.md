---
nav_title: Detalles creativos
article_title: Detalles creativos
page_order: 3.5
layout: dev_guide
guide_top_header: "Detalles creativos"
guide_top_text: "Antes de ponerte creativo con nuestros mensajes dentro de la aplicación, debes conocer algunas de las directrices. Todas las plantillas de mensajes dentro de la aplicación están diseñadas para mostrar diferentes longitudes de texto y tamaños de imágenes en los dispositivos modernos. Para asegurarte de que tu mensaje se muestra bien en todos los teléfonos, tabletas y computadoras, te recomendamos que sigas estas directrices y que <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>pruebes</a> siempre <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>tus mensajes</a> antes de lanzarlos."
description: "Este núcleo de aterrizaje cubre los requisitos de diseño y contenido para los tres tipos de mensajes dentro de la aplicación: modal, deslizamiento hacia arriba y pantalla completa."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Especificaciones por tipo de mensaje"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Deslizamiento hacia arriba
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Pantalla completa"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Directrices de contenido

### Texto

Para los cuerpos o encabezados de los mensajes dentro de la aplicación, te recomendamos que seas breve y dulce: de una a dos líneas para los encabezados y hasta tres para los cuerpos. Después de tres líneas, es probable que el mensaje tenga que desplazarse verticalmente, y los usuarios podrían no interactuar con todo el contenido. El umbral que desencadena el desplazamiento puede variar según el tamaño del dispositivo del usuario final, el estilo personalizado o la presencia de imágenes en los mensajes, pero tres líneas suele ser seguro.

Si utilizas la generación más reciente de mensajes dentro de la aplicación (Generación 3), verás que los tipos de letra predeterminados son los Sans Serif por defecto del sistema operativo para iOS y Android. Los mensajes dentro de la aplicación Web estarán predeterminados en Helvética.

### Imágenes

Nuestras directrices para las imágenes son más estructuradas que las del texto, ya que queremos asegurarnos de que tus mensajes se muestren como se pretende, y de forma atractiva en teléfonos, tabletas y computadoras de todos los modelos y tamaños.

En general, Braze recomienda utilizar imágenes que quepan en una pantalla de 16:10.

- **Todas las imágenes deben pesar menos de 5 MB.**
- Sólo aceptamos los tipos de archivo PNG, JPEG y GIF.
- Recomendamos alojar imágenes en la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para habilitar el SDK de Braze para descargar activos de nuestra CDN para la visualización de mensajes sin conexión.
- Para los mensajes a pantalla completa, sigue nuestras directrices para la [zona segura de imágenes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes de mensajes dentro de la aplicación y superposiciones de zonas seguras están diseñadas para adaptarse a dispositivos de todos los tamaños. [Descargar plantillas de diseño ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Fullscreen %}

Mensaje dentro de la aplicación a pantalla completa ocupando una pantalla de la aplicación. El mensaje a pantalla completa incluye una imagen grande, una cabecera, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | --- |
| Imagen + Texto | Relación de aspecto 6:5<br>Alta resolución 1200 x 1000 px<br> Mínimo 600 x 500 px | El recorte puede producirse en todos los lados, pero la imagen siempre ocupará el 50% superior de la ventana. |
| Sólo imagen | Relación de aspecto 3:5<br>Alta resolución 1200 x 2000 px<br> Mínimo 600 x 1000 px | El recorte puede producirse en los bordes izquierdo y derecho en los dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Más detalles sobre las pantallas completas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

\![Mensaje modal dentro de la aplicación que aparece en el centro de una aplicación y sitio web como un diálogo. El modal incluye una imagen, una cabecera, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | ------ |
| Imagen + Texto | Relación de aspecto 29:10<br>Alta resolución 1450 x 500 px<br> Mínimo 600 x 205 px | Las imágenes altas se reducirán y se centrarán horizontalmente. Las imágenes anchas se recortarán por los bordes izquierdo y derecho. |
| Sólo imagen | Casi cualquier relación de aspecto<br>Alta resolución hasta 1200 x 2000 px<br> Mínimo 600 x 600 px | El mensaje cambiará de tamaño para adaptarse a imágenes de la mayoría de las relaciones de aspecto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Más detalles sobre los modales]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

\![Mensaje deslizamiento hacia arriba dentro de la aplicación que aparece desde la parte inferior de la pantalla de la aplicación. El deslizamiento hacia arriba incluye una imagen de icono y un mensaje breve.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | --- |
| Imagen + Texto | Relación de aspecto 1:1<br>Alta resolución 150 x 150 px<br> Mínimo 50 x 50 px | Las imágenes de distintas relaciones de aspecto cabrán en un contenedor de imágenes cuadrado, sin recorte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Más detalles sobre los deslizamientos hacia arriba]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIFs y videos

Braze admite actualmente GIFs para Web (incluido), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) e iOS (incluido) en mensajería dentro de la aplicación, dado que se ha habilitado durante la deseada integración de la plataforma. Para más información sobre el video en los mensajes dentro de la aplicación, consulta nuestra [documentación de Personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Consideraciones adicionales

Los mensajes dentro de la aplicación Braze tienen especificaciones creativas tanto globales como individuales. Para obtener más información sobre cómo personalizar completamente los mensajes dentro de la aplicación, ve a nuestra página de [Personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

<br>

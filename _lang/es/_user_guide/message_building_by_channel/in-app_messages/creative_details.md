---
nav_title: Detalles creativos
article_title: Detalles creativos
page_order: 3.5
layout: dev_guide
guide_top_header: "Detalles creativos"
guide_top_text: "Antes de dar rienda suelta a tu creatividad con nuestros mensajes in-app, debes conocer algunas de las directrices. Todas las plantillas de mensajes in-app están diseñadas para mostrar texto de distinta longitud e imágenes de distintos tamaños en los dispositivos modernos. Para asegurarte de que tu mensaje se muestra bien en todos los teléfonos, tabletas y ordenadores, te recomendamos que sigas estas directrices y que <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>pruebes siempre tus mensajes</a> antes de lanzarlos."
description: "Este landing hub cubre los requisitos de diseño y contenido para los tres tipos de mensajes in-app: modal, slideup y fullscreen."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Especificaciones por tipo de mensaje"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: deslizamiento hacia arriba
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Pantalla completa"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Directrices sobre contenidos

### Texto

Para los cuerpos o encabezados de los mensajes in-app, recomendamos que sean breves y concisos: una o dos líneas para los encabezados y hasta tres para los cuerpos. Después de tres líneas, es probable que el mensaje tenga que desplazarse verticalmente y que los usuarios no se interesen por todo el contenido. El umbral que activa el desplazamiento puede variar en función del tamaño del dispositivo del usuario final, el estilo personalizado o la presencia de imágenes en los mensajes, pero tres líneas suele ser seguro.

Si utilizas la última generación de mensajes in-app (Generación 3), verás que las fuentes por defecto son las Sans Serif por defecto del sistema operativo para iOS y Android. Los mensajes de la aplicación web se mostrarán por defecto en Helvetica.

### Imágenes

Nuestras directrices para las imágenes son más estructuradas que para el texto, ya que queremos asegurarnos de que sus mensajes se muestren correctamente en teléfonos, tabletas y ordenadores de todos los modelos y tamaños.

En general, Braze recomienda utilizar imágenes que quepan en una pantalla de 16:10.

- **Todas las imágenes deben ocupar menos de 5 MB.**
- Sólo aceptamos los tipos de archivo PNG, JPEG y GIF.
- Recomendamos alojar imágenes en la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para permitir que el SDK de Braze descargue activos de nuestra CDN para la visualización de mensajes sin conexión.
- Para los mensajes a pantalla completa, sigue nuestras directrices para la [zona segura de imágenes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes de mensajes in-app y superposiciones de zonas seguras están diseñadas para adaptarse a dispositivos de todos los tamaños. [Descargar plantillas de diseño ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Pantalla completa %}

![Mensaje en pantalla completa que ocupa la pantalla de una aplicación. El mensaje a pantalla completa incluye una imagen grande, la cabecera, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | --- |
| Imagen + Texto | Relación de aspecto 6:5<br>Alta resolución 1200 x 1000 px<br> Mínimo 600 x 500 px | La imagen puede recortarse por todos los lados, pero siempre ocupará el 50% superior de la ventana. |
| Solo imagen | Relación de aspecto 3:5<br>Alta resolución 1200 x 2000 px<br> Mínimo 600 x 1000 px | El recorte puede producirse en los bordes izquierdo y derecho en los dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Más información sobre las pantallas completas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

![Mensaje modal in-app que aparece en el centro de una aplicación y sitio web en forma de diálogo. El modal incluye una imagen, una cabecera, el cuerpo del mensaje y dos botones.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | ------ |
| Imagen + Texto | Relación de aspecto 29:10<br>Alta resolución 1450 x 500 px<br> Mínimo 600 x 205 px | Las imágenes altas se reducirán y se centrarán horizontalmente. Las imágenes anchas se recortarán por los bordes izquierdo y derecho. |
| Solo imagen | Casi cualquier relación de aspecto<br>Alta resolución de hasta 1200 x 2000 px<br> Mínimo 600 x 600 px | El mensaje cambiará de tamaño para adaptarse a imágenes de la mayoría de las relaciones de aspecto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Más detalles sobre los modales]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Deslizamiento hacia arriba %}

![Mensaje deslizamiento hacia arriba dentro de la aplicación que aparece desde la parte inferior de la pantalla de la aplicación. El slideup incluye una imagen de icono y un breve mensaje.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | --- |
| Imagen + Texto | Relación de aspecto 1:1<br>Alta resolución 150 x 150 px<br> Mínimo 50 x 50 px | Las imágenes de distintas relaciones de aspecto caben en un contenedor de imágenes cuadrado, sin recorte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Más información sobre las subidas de diapositivas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIF y vídeos

Braze admite actualmente GIF para mensajería dentro de la aplicación en Web (incluido), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) e iOS (incluido), dado que se habilitó durante la integración de plataforma deseada. Para obtener más información sobre el vídeo en los mensajes in-app, consulte nuestra [documentación de personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Consideraciones adicionales

Los mensajes dentro de la aplicación de Braze tienen especificaciones creativas tanto globales como individuales. Para obtener más información sobre la personalización completa de los mensajes integrados en la aplicación, visita nuestra página de [personalización]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

<br>

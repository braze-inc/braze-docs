---
nav_title: deslizamiento hacia arriba
article_title: Mensajes In-app de Slideup
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "Este artículo de referencia trata del mensaje y los requisitos de diseño de los mensajes dentro de la aplicación con deslizamiento hacia arriba."

---

# Mensajes de deslizamiento hacia arriba dentro de la aplicación

> Nuestros slideups suelen aparecer en la parte superior o inferior de la pantalla de la aplicación (puedes configurarlo al crear tu mensaje). Son ideales para alertar a los usuarios sobre nuevas condiciones de servicio, cookies y otros fragmentos de información. No son molestos y permiten a los usuarios seguir interactuando con la aplicación mientras se muestra el mensaje.

![Dos mensajes in-app deslizables, uno que aparece desde la parte superior de la pantalla y otro desde la inferior, en los que se detallan las recomendaciones de imagen y texto. Consulte las secciones siguientes para obtener más información.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportamiento de la imagen y la copia

Los mensajes de Slideup pueden contener hasta tres líneas de copia antes de ser truncados con elipses. Las imágenes de los slideups nunca se recortarán, siempre se reducirán para que quepan en el contenedor de imágenes de 50 x 50 píxeles.

- Todas las imágenes deben ocupar menos de 5 MB.
- Sólo aceptamos los tipos de archivo PNG, JPEG y GIF.
- Recomendamos que sus imágenes sean de 500 KB.

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes de mensajes in-app y superposiciones de zonas seguras están diseñadas para adaptarse a dispositivos de todos los tamaños. [Descargar plantillas de diseño ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | --- |
| Imagen + Texto | Relación de aspecto 1:1<br>Alta resolución 150 x 150 px<br> Mínimo 50 x 50 px | Las imágenes de distintas relaciones de aspecto caben en un contenedor de imágenes cuadrado, sin recorte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Siempre debe [previsualizar y probar sus mensajes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) en una variedad de dispositivos para asegurarse de que las áreas más importantes de su imagen y mensaje aparecen como se espera. Tenga en cuenta que al previsualizar su mensaje en el compositor, la representación real en los dispositivos puede diferir.

## Dispositivos móviles

En los dispositivos móviles, los slideups aparecen en la parte superior o inferior de la pantalla de la aplicación. Puedes especificarlo cuando crees tu mensaje. Los usuarios pueden deslizar el dedo para descartar el slideup, o tocar para abrirlo si se incluye una acción de clic. Si se añade una acción de clic al deslizamiento hacia arriba, se muestra un aspa ">".

## Pantallas más grandes

{% tabs %}
{% tab Escritorio %}

En un navegador de escritorio, un mensaje deslizable dentro de la aplicación se situará en la esquina de la pantalla como se muestra en la siguiente captura de pantalla (a menos que se indique lo contrario al crear el mensaje dentro de la aplicación). Los usuarios pueden pulsar el botón "X" para cerrar el menú.

![Mensaje in-app de Slideup tal y como aparece en un navegador de escritorio. El mensaje aparece en la esquina inferior derecha de la pantalla y no ocupa todo el ancho de la misma.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tableta %}

En una tableta, aparece un mensaje deslizamiento de hacia arriba dentro de la aplicación en la parte inferior de la pantalla. Al igual que en los dispositivos móviles, los usuarios pueden deslizar el dedo para descartar el slideup, o tocar para abrirlo si se incluye una acción de clic. Si se añade una acción de clic al deslizamiento hacia arriba, se muestra un aspa ">". El botón "X" de cierre no se muestra por defecto.

![Mensaje de deslizamiento hacia arriba dentro de la aplicación tal y como aparece en la pantalla de una tableta. El mensaje aparece en la parte inferior central de la pantalla y no ocupa todo el ancho de la misma.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}


---
nav_title: Deslizamiento hacia arriba
article_title: Slideup Mensajes dentro de la aplicación
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "Este artículo de referencia trata del mensaje y los requisitos de diseño de los mensajes dentro de la aplicación con deslizamiento hacia arriba."

---

# Mensajes de deslizamiento hacia arriba dentro de la aplicación

> Nuestros deslizamientos hacia arriba suelen aparecer en la parte superior o inferior de la pantalla de la aplicación (puedes configurarlo cuando crees tu mensaje). Son ideales para alertar a tus usuarios sobre nuevas condiciones de servicio, cookies y otros fragmentos de información. No son intrusivos y permiten a tus usuarios seguir interactuando con tu aplicación mientras se muestra el mensaje.

Dos mensajes dentro de la aplicación, uno que aparece en la parte superior de la pantalla y otro en la inferior, detallando las recomendaciones de imagen y texto. Para más detalles, consulta las secciones siguientes.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportamiento de la imagen y la copia

Los mensajes de deslizamiento hacia arriba pueden contener hasta tres líneas de copia antes de ser truncados con elipses. Las imágenes de los deslizamientos hacia arriba nunca se recortarán ni se recortarán: siempre se reducirán para que quepan en el contenedor de imágenes de 50 x 50 píxeles.

- Todas las imágenes deben pesar menos de 5 MB.
- Sólo aceptamos los tipos de archivo PNG, JPEG y GIF.
- Recomendamos que tus imágenes sean de 500 KB.

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes de mensajes dentro de la aplicación y superposiciones de zonas seguras están diseñadas para adaptarse a dispositivos de todos los tamaños. [Descargar plantillas de diseño ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Diseño | Tamaño de los activos | Notas |
|--- | --- | --- |
| Imagen + Texto | Relación de aspecto 1:1<br>Alta resolución 150 x 150 px<br> Mínimo 50 x 50 px | Las imágenes de distintas relaciones de aspecto cabrán en un contenedor de imágenes cuadrado, sin recorte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Siempre debes [previsualizar y probar tus mensajes]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) en diversos dispositivos para asegurarte de que las áreas más importantes de tu imagen y mensaje aparecen como se espera. Ten en cuenta que al previsualizar tu mensaje en el compositor, la representación real en los dispositivos puede diferir.

## Dispositivos móviles

En los dispositivos móviles, los deslizamientos hacia arriba o hacia abajo aparecen en la pantalla de la aplicación. Puedes especificarlo cuando crees tu mensaje. Los usuarios pueden deslizar para descartar el deslizamiento hacia arriba, o tocar para abrirlo si se incluye una acción de clic. Si se añade una acción de clic al deslizamiento hacia arriba, se muestra un aspa ">".

## Pantallas más grandes

{% tabs %}
{% tab Desktop %}

En un explorador de escritorio, un mensaje dentro de la aplicación deslizable se situará en la esquina de la pantalla, como se muestra en la siguiente captura (a menos que se indique lo contrario al crear el mensaje dentro de la aplicación). Los usuarios pueden hacer clic en el botón de cierre "X" para descartar el deslizamiento hacia arriba.

\![Mensaje deslizamiento dentro de la aplicación tal y como aparece en un explorador de escritorio. El mensaje aparece en la esquina inferior derecha de la pantalla y no ocupa todo el ancho de la misma.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

En una tableta, aparece un mensaje deslizamiento hacia arriba dentro de la aplicación en la parte inferior de la pantalla. Al igual que en los dispositivos móviles, los usuarios pueden deslizar el dedo para descartar el deslizamiento hacia arriba, o tocar para abrirlo si se incluye una acción de clic. Si se añade una acción de clic al deslizamiento hacia arriba, se muestra un aspa ">". El botón "X" de cerrar no aparece predeterminado.

\![Mensaje deslizamiento hacia arriba dentro de la aplicación tal y como aparece en la pantalla de una tableta. El mensaje aparece en la parte inferior central de la pantalla y no ocupa todo el ancho de la misma.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}


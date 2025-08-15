---
nav_title: "Pantalla completa"
article_title: Mensajes a pantalla completa en la aplicación
description: "Este artículo de referencia cubre los requisitos de diseño y mensaje de los mensajes in-app a pantalla completa."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# Mensajes a pantalla completa en la aplicación

> ¡Los mensajes a pantalla completa ocupan toda la pantalla del dispositivo! Este tipo de mensaje es ideal cuando realmente necesitas la atención de tu usuario, como en el caso de las actualizaciones obligatorias de la aplicación.

{% tabs %}
{% tab Retrato %}

![Dos mensajes a pantalla completa en la aplicación, uno al lado del otro en orientación vertical, detallando las recomendaciones de imagen y texto. Consulte las secciones siguientes para obtener más información.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Horizontal %}

![Dos mensajes a pantalla completa en la aplicación, uno al lado del otro en orientación horizontal, detallando las recomendaciones de imagen y texto. Consulte las secciones siguientes para obtener más información.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Imágenes

Los mensajes in-app a pantalla completa ocuparán toda la altura de un dispositivo y se recortarán horizontalmente (lados izquierdo y derecho) según sea necesario. Los mensajes de imagen y texto a pantalla completa ocuparán el 50% de la altura de un dispositivo. Todos los mensajes de la aplicación a pantalla completa llenarán la barra de estado en los dispositivos con "muesca".

- Todas las imágenes deben ocupar menos de 5 MB.
- Sólo aceptamos los tipos de archivo PNG, JPEG y [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs).
- Recomendamos que sus imágenes sean de 500 KB.

{% alert tip %} ¡Crea activos con confianza! Nuestras plantillas de imágenes de mensajes in-app y superposiciones de zonas seguras están diseñadas para adaptarse a dispositivos de todos los tamaños. [Descargar plantillas de diseño ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Vertical

| diseño | volumen de activos | notas |
|--- | --- | --- |
| Imagen y texto | Relación de aspecto 6:5<br> Alta resolución 1200 x 1000 px<br> Mínimo 600 x 500 px | La imagen puede recortarse por todos los lados, pero siempre ocupará el 50% superior de la ventana. |
| Solo imagen | Relación de aspecto 3:5<br> Alta resolución 1200 x 2000 px<br> Mínimo 600 x 1000 px | El recorte puede producirse en los bordes izquierdo y derecho en los dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Horizontal

| diseño | volumen de activos | notas |
|--- | --- | --- |
| Imagen y texto | Relación de aspecto 10:3<br> Alta resolución 2000 x 600px<br> Mínimo 1000 x 300 px | La imagen puede recortarse por todos los lados, pero siempre ocupará el 50% superior de la ventana. |
| Solo imagen | Relación de aspecto 5:3<br> Alta resolución 2000 x 1200px<br> Mínimo 1000 x 600 px | El recorte puede producirse en los bordes izquierdo y derecho en los dispositivos más altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Zona segura de imágenes

Al previsualizar un mensaje de la aplicación a pantalla completa en la plataforma Braze, puedes habilitar la zona segura de imagen en el área del mensaje que está a salvo de recortes cuando se muestra en otros dispositivos. Además de probar la zona segura de la imagen en el panel de vista previa, le recomendamos que [pruebe su mensaje]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) como siempre.

![Vista previa de un mensaje in-app en Braze con la opción "Mostrar zona segura de imágenes" activada. La zona segura de la imagen es una superposición sobre la imagen que visualiza qué partes de la imagen estarán a salvo del recorte.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Pantallas más grandes

En una tableta o en un navegador de escritorio, aparecerá un mensaje a pantalla completa en el centro de la pantalla de la aplicación, como se muestra en la siguiente captura de pantalla.

{% tabs %}
{% tab Retrato %}

![Mensaje in-app a pantalla completa tal y como aparecería en una pantalla grande en orientación vertical. El mensaje aparece como un modal grande que se sitúa en el centro de la pantalla.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Horizontal %}

![Mensaje in-app a pantalla completa tal y como aparecería en una pantalla grande en orientación horizontal. El mensaje aparece como un modal grande que se sitúa en el centro de la pantalla.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}


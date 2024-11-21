---
nav_title: Push de imagen en línea
article_title: Push de imagen incorporada para Android
platform: Android
page_order: 5.9
description: "Este artículo de referencia explica cómo implementar el push de imágenes en línea en tu aplicación Android."
channel:
  - push

---

# Push de imagen en línea

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> Muestra una imagen más grande dentro de tu notificación push de Android mediante la función de inserción de imágenes en línea. Con este diseño, los usuarios no tendrán que expandir manualmente el push para ampliar la imagen. 

No se requiere ninguna integración adicional ni cambios en el SDK para utilizar esta característica. Los dispositivos o SDK que no cumplan los requisitos mínimos de versión mostrarán en su lugar una notificación push estándar con una imagen grande.

## Requisitos de uso

- Este tipo de notificación requiere el SDK de Android Braze v10.0.0+ y dispositivos Android M+. 
- Los dispositivos o SDK no compatibles volverán a la notificación push de imagen grande estándar.
- A diferencia de las notificaciones push normales de Android, las imágenes push en línea tienen una relación de aspecto de 3:2.

{% alert note %}
Los dispositivos con Android 12 se mostrarán de forma diferente debido a los cambios en los estilos personalizados de las notificaciones push.
{% endalert %}

## Configuración del panel de control

Al crear un mensaje push de Android, esta característica está disponible en el desplegable **Tipo de notificación**.

![El editor de campañas push muestra la ubicación del desplegable "Tipo de notificación" (encima de la vista previa push estándar).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

---
nav_title: "Opciones de notificación"
article_title: Opciones de notificación de Android
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre varias opciones de notificación de Android y cómo utilizarlas mejor en las campañas Braze."

platform: Android
channel:
  - Push

---

# Opciones de notificación

> Estas son algunas de las opciones de notificación push específicas de Android disponibles a través de Braze.

## Notificaciones silenciosas

Cuando [redactas tu mensaje de notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/?tab=android#step-4-compose-your-push-message), **no puedes** enviar un mensaje push de Android sin un título; sin embargo, puedes introducir un solo espacio en su lugar. Ten en cuenta que si tu mensaje sólo contiene un espacio, se enviará como una notificación push silenciosa. Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android).

## Grupos de notificaciones

Si quieres clasificar tus mensajes y agruparlos en la bandeja de notificaciones de tu usuario, puedes utilizar la característica de canales de notificación de Android a través de Braze.

En primer lugar, crea tu campaña push de Android y, a continuación, busca en la parte superior de la pestaña **Redactar** el desplegable **Canal de notificaciones**.

\![]({% image_buster /assets/img_archive/notification_channel_dropdown.png %}){: style="max-width:60%;"}

Selecciona tu canal de notificación en el desplegable. También debes seleccionar un canal alternativo en caso de que la configuración de tu Canal de Notificación no funcione correctamente.

Si no tienes ningún [canal de notificación]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/) en esta lista, puedes añadir uno utilizando el ID del canal de notificación. Ponte en contacto con tus desarrolladores para identificar cuáles son los ID de tu canal de notificación o para crear nuevos ID según sea necesario. 

Para añadir un ID de notificación a tu canal de notificaciones, haz clic en **Gestionar canal de notificaciones** en el menú desplegable **Canal de notificaciones** y rellena los campos obligatorios. Los canales de notificación deben definirse en la aplicación antes de que puedan utilizarse en la plataforma Braze.

\![]({% image_buster /assets/img_archive/notification_channels.png %}){: style="max-width:80%;" }



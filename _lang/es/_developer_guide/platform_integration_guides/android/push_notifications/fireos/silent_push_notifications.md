---
nav_title: Notificaciones push silenciosas
article_title: Notificaciones push silenciosas para FireOS
platform: FireOS
page_order: 3

page_type: reference
description: "Este artículo de referencia describe cómo enviar notificaciones push silenciosas del FireOS, y los posibles casos de uso en los que las notificaciones push silenciosas pueden ser preferibles."
channel: push

---

# Notificaciones push silenciosas

> Las notificaciones silenciosas te permiten avisar a tu aplicación en segundo plano cuando se produzcan eventos importantes. Puede que tengas que entregar nuevos mensajes instantáneos, publicar nuevos números de una revista, enviar alertas de noticias de última hora o descargar el último episodio del programa de TV favorito de tu usuario para verlo sin conexión. Las notificaciones silenciosas son estupendas para contenidos esporádicos pero de importancia inmediata, en los que el retraso entre las búsquedas en segundo plano puede no ser aceptable.

Las notificaciones silenciosas están disponibles a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) Braze. Para aprovecharlos, debes establecer la bandera `send_to_sync` en `true` dentro del [objeto push de Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) y asegurarte de que no hay campos `title` o `alert` establecidos, ya que causará errores cuando se utilice junto a `send_to_sync`. Sin embargo, puedes incluir datos `extras` dentro del objeto.

Las notificaciones silenciosas también están disponibles en el panel. Para enviar una notificación silenciosa, asegúrate de que los campos de título y cuerpo de la notificación están en blanco, como se muestra en la imagen:

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Ejemplo de notificación push silenciosa -- Android")


{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Configuración de notificaciones push silenciosas

Las notificaciones silenciosas están disponibles a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) Braze. Para aprovecharlos, debes establecer la bandera `send_to_sync` en `true` dentro del [objeto push de Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) y asegurarte de que no hay campos `title` o `alert` establecidos, ya que causará errores cuando se utilice junto a `send_to_sync`. Sin embargo, puedes incluir datos `extras` dentro del objeto.

Las notificaciones silenciosas también están disponibles en el panel. Para enviar una notificación silenciosa, asegúrate de que los campos de título y cuerpo de la notificación están en blanco, como se muestra en la imagen:

![]({% image_buster /assets/img_archive/SilentPushExample.png %} "Silent Push Notification Example -- Android")

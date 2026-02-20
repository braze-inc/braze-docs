{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Configuración de notificaciones push silenciosas

Las notificaciones silenciosas están disponibles a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) Braze. Para aprovecharlos, tienes que establecer la bandera `send_to_sync` en `true` dentro del [objeto push de Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) y asegurarte de que no hay campos `title` o `alert` establecidos, ya que causarán errores cuando se utilicen junto a `send_to_sync`-no obstante, puedes incluir datos `extras` dentro del objeto.

---
nav_title: Notificaciones push silenciosas
article_title: Notificaciones push silenciosas para Android
platform: Android
page_order: 3
description: "Este artículo explica cómo implementar notificaciones push silenciosas en tu aplicación Android."
channel:
  - push

---

# Notificaciones push silenciosas para Android

> Las notificaciones silenciosas te permiten avisar a tu aplicación en segundo plano cuando se produzcan eventos importantes. Puede que tengas que entregar nuevos mensajes instantáneos, publicar nuevos números de una revista, enviar alertas de noticias de última hora o descargar el último episodio del programa de TV favorito de tu usuario para verlo sin conexión. Las notificaciones silenciosas son estupendas para contenidos esporádicos pero de importancia inmediata, en los que el retraso entre las búsquedas en segundo plano puede no ser aceptable.

## Configuración de notificaciones push silenciosas

Las notificaciones silenciosas están disponibles a través de la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/) Braze. Para aprovecharlos, tienes que establecer la bandera `send_to_sync` en `true` dentro del [objeto push de Android]({{site.baseurl}}/api/objects_filters/messaging/android_object/) y asegurarte de que no hay campos `title` o `alert` establecidos, ya que causarán errores cuando se utilicen junto a `send_to_sync`-no obstante, puedes incluir datos `extras` dentro del objeto.

{% alert tip %}
Cuando [redactes tu mensaje de notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message//?tab=android#step-4-compose-your-push-message), puedes enviar una notificación push silenciosa de Android enviando un mensaje con un solo espacio. Ten en cuenta que éste **no es** el método recomendado para enviar notificaciones push, pero puede ser útil en algunos casos.
{% endalert %}


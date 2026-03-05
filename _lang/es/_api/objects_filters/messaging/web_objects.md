---
nav_title: "Objeto web"
article_title: Objeto de mensajería web
page_order: 12
page_type: reference
channel: push
platform: Web
description: "Este artículo de referencia enumera y explica los diferentes objetos Web utilizados en Braze."

---
# Objeto de notificación push web

> El objeto `web_push` te permite definir o solicitar información relacionada con el contenido de las alertas push web y push web a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

## Objeto de notificación push web

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "custom_uri": (optional, string) a web URL,
   "image_url": (optional, string) URL for image to show,
   "large_image_url": (optional, string) URL for large image, supported on Chrome Windows/Android,
   "require_interaction": (optional, boolean) whether to require the user to dismiss the notification. for a list of supported platforms, see: "https://developer.mozilla.org/en-US/docs/Web/API/Notification/requireInteraction#browser_compatibility",
   "time_to_live": (optional, integer (seconds)),
   "send_to_most_recent_device_only" : (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used browser, rather than all eligibles browsers,
   "buttons" : (optional, array of Web push action button objects) push action buttons to display
}
```

El valor de `image_url` debe ser una URL que enlace a donde esté alojada tu imagen. Las imágenes deben recortarse a una relación de aspecto de 1:1.

## Objeto botón de acción para notificación push web

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```

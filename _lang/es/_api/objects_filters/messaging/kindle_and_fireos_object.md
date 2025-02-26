---
nav_title: "Objeto push para Kindle y FireOS"
article_title: Objeto de mensajería push para Kindle y FireOS
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "Este artículo de referencia explica los diferentes componentes del objeto push para Kindle y FireOS de Braze."

---

# Objeto push para Kindle y FireOS

> El objeto `kindle_push` te permite modificar o crear notificaciones push para Kindle y FireOS a través de nuestros [puntos finales de mensajería]({{site.baseurl}}/api/endpoints/messaging).

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Kindle/FireOS Push Message),
   "priority": (optional, integer) the notification priority value,
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI
}
```

El parámetro `priority` aceptará valores de `-2` a `2`, donde `-2` representa la prioridad más baja y `2` representa la prioridad más alta. `0` es el valor predeterminado. Cualquier valor enviado que esté fuera de ese rango de enteros será predeterminado a `0`.

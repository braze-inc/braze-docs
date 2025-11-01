---
nav_title: "Objet Notification push Kindle et FireOS"
article_title: Objet Messagerie de notifications push Kindle et FireOS
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "Cet article de référence explique les différents composants de l'objet push de Braze Kindle et FireOS."

---

# Objet Notification push Kindle et FireOS

> L'objet `kindle_push` vous permet de modifier ou de créer des notifications push Kindle et FireOS via nos [points d'extrémité de messages.]({{site.baseurl}}/api/endpoints/messaging)

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

Le paramètre `priority` accepte les valeurs entre `-2` et `2`, où `-2` représente la priorité la plus basse et `2` la priorité la plus élevée. `0` est la valeur par défaut. Toutes les valeurs envoyées en dehors de cette plage d’entiers seront par défaut à `0`.

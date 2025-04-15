---
nav_title: "Kindle und FireOS Push-Objekt"
article_title: Kindle und FireOS Push-Nachrichten Objekt
page_order: 7
page_type: reference
channel: push
platform:
  - Android
  - FireOS
description: "Dieser Referenzartikel erklärt die verschiedenen Komponenten des Braze Kindle und FireOS Push-Objekts."

---

# Kindle und FireOS Push-Objekt

> Mit dem Objekt `kindle_push` können Sie Kindle- und FireOS-Push-Benachrichtigungen über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) ändern oder erstellen.

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

Der Parameter `priority` akzeptiert Werte von `-2` bis `2`, wobei `-2` die niedrigste Priorität und `2` die höchste Priorität darstellt. `0` ist der Standardwert. Alle Werte, die außerhalb dieses Ganzzahlbereichs gesendet werden, werden standardmäßig auf `0` gesetzt.

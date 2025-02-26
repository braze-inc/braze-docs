---
nav_title: "Objet Web"
article_title: Objet Messagerie Web
page_order: 12
page_type: reference
channel: push
platform: Web
description: "Cet article de référence répertorie et explique les différents objets Web utilisés chez Braze."

---
# Objet Notification push Web

> L'objet `web_push` vous permet de définir ou de demander des informations relatives au contenu de web push et d'alertes web push via nos [points d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging)

## Objet Notification push Web

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

La valeur de `image_url` doit être une URL qui renvoie à l’emplacement où votre image est hébergée. Les images doivent être recadrées selon un rapport hauteur/largeur 1:1.

## Objet Bouton d’action push Web

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL
}
```

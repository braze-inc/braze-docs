---
nav_title: "Objet Web"
article_title: Objet de communication Web
page_order: 12
page_type: référence
channel: notification push
platform: Web
description: "Cet article répertorie et explique les différents objets Web utilisés chez Braze."

---
# Spécification de l’objet Notification push Web

L’objet `web_push` vous permet de définir ou de demander des informations relatives au contenu de notification push Web et de notification push Web pour les alertes via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Objet de notification push Web

```json
{
   "alert": (required, string) le message de notification,
   "title": (required, string) le titre qui apparaît dans la barre de notifications,
   "extra": (optional, object) clés et valeurs supplémentaires à envoyer dans la notification push,
   "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de notification push Kindle/FireOS),
   "custom_uri": (optional, string) une URL Web,
   "image_url": (optional, string) URL de l’image à afficher,
   "large_image_url": (optional, string) URL pour une grande image prise en charge par Chrome sur Windows/Android,
   "require_interaction": (optional, boolean) s’il est nécessaire ou non que l’utilisateur rejette la notification, pris en charge sur Mac Chrome,
   "time_to_live": (optional, integer (seconds)),
   "send_to_most_recent_device_only" : (optional, boolean) défini par défaut sur « false » ; si défini sur « true », Braze enverra cette notification push uniquement au dernier navigateur dont s’est servi l’utilisateur plutôt qu’à tous les navigateurs éligibles,
   "buttons" : (optional, array of Web Push Action Button Objects) boutons d’action push à afficher
}
```

La valeur de `image_url` doit être une URL qui renvoie à l’emplacement où votre image est hébergée. Les images doivent être recadrées au format 1:1.

## Objet Bouton d’action push Web

```json
{
  "text": (required, string) le texte du bouton,
  "action": (optional, string) « OPEN_APP », « URI » ou « CLOSE », défini par défaut sur « OPEN_APP »,
  "uri": (optional, string) une URL Web
}
```

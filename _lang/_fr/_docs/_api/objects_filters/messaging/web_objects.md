---
nav_title: "Objet Web"
article_title: Objet Messagerie Web
page_order: 12
page_type: Référence
channel: Pousser
platform: Web
description: "Cet article énumère et explique les différents objets Web utilisés au Brésil."
---

# Spécification de l'objet push Web

Ces objets sont utilisés pour définir ou demander des informations relatives au contenu Web Push et Web Push Alert.

## Objet push Web

```json
{
   "alert": (requis, chaîne) le message de notification,
   "titre" : (obligatoire, chaîne) le titre qui apparaît dans le tiroir de notification,
   "extra": (optionnel, objet) clés et valeurs supplémentaires à envoyer dans la push,
   "message_variation_id": (optionnel, string) utilisé lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message Kindle/FireOS Push Message),
   "custom_uri": (optionnel, chaîne) une URL web,
   "image_url": (optionnel, string) URL de l'image à afficher,
   "large_image_url": (optionnel, string) URL pour la grande image, prise en charge sur Chrome Windows/Android,
   "require_interaction": (optionnel, booléen) si l'utilisateur doit rejeter la notification, supporté sous Mac Chrome,
   "time_to_live": (optionnel, entier (secondes)),
   "send_to_most_recent_device_only" : (optionnel, booléen) par défaut à false, si défini à true, Braze enverra uniquement ce push à un utilisateur le plus récemment utilisé navigateur, plutôt que tous les navigateurs éligibles,
   "boutons" : (optionnel, tableau d'objets du bouton d'action Push Web) pour afficher
}
```

La valeur de `image_url` devrait être une URL qui se connecte à l'endroit où votre image est hébergée. Les images doivent être recadrées à un format 1:1.

## Objet de bouton d'action Web push

```json
{
  "text": (obligatoire, chaîne) le texte du bouton,
  "action": (optionnel, chaîne) un de "OPEN_APP", "URI", ou "CLOSE", la valeur par défaut est "OPEN_APP",
  "uri": (optionnel, chaîne) une URL web
}
```

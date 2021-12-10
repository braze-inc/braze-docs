---
nav_title: "Objet de carte de contenu"
article_title: Objet Messagerie de la carte de contenu
page_order: 4
page_type: Référence
channel: cartes de contenu
description: "Cet article explique les différents composants de l'objet Carte de Contenu de Brase."
---

# Spécification de l'objet de la carte de contenu

L'objet de la carte de contenu vous permet de modifier ou de créer des cartes de contenu via nos points de terminaison de messagerie.

## Corps

```json
{
  "type": (obligatoire, chaîne) un de "CLASSIC", "CAPTIONED_IMAGE", ou "BANNER",
  "title": (obligatoire, string) le titre de la carte,
  "description": (obligatoire, chaîne) la description de la carte,
  "message_variation_id": (optionnel, chaîne) utilisée lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message de carte de contenu),
  "épinglé" : (optionnel, booléen) si la carte est épinglée. Faux par défaut,
  "image_url": (optionnel, chaîne) l'URL de l'image de la carte. Requis pour "CAPTIONED_IMAGE" et "BANNER",
  "time_to_live": (optionnel, entier) le nombre de secondes avant l'expiration de la carte. Vous devez inclure soit "time_to_live" soit "expire_at",
  "expire_at": (optionnel, chaîne) ISO 8601 date quand la carte expire. Vous devez inclure "time_to_live" ou "expire_at", une durée d'expiration maximale de 30 jours
  "expire_in_local_time": (optionnel, booléen) si vous utilisez "expire_at", détermine si la carte doit expirer dans l'heure locale des utilisateurs. Faux par défaut,
  "ios_uri": (optionnel, chaîne) une URL web, ou un lien profond,
  "android_uri": (optionnel, chaîne) une URL web, ou un lien profond, URI,
  "web_uri": (optionnel, chaîne) une URL web, ou un lien profond,
  "ios_use_webview": (optionnel, booléen) si vous voulez ouvrir l'URL web dans l'application, par défaut à true,
  "android_use_webview": (optionnel, booléen) si vous voulez ouvrir l'URL web dans l'application, par défaut à true,
  "uri_text": (optionnel, chaîne) le texte de lien de la carte,
  "extra": (optionnel, objet) clés et valeurs supplémentaires envoyées avec la carte,
}
```

{% alert important %}
Actuellement, Braze prend en charge une durée d'expiration maximale de 30 jours.
{% endalert %}

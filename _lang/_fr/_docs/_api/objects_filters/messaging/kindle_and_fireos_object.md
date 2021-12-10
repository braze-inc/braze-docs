---
nav_title: "Objet Push Kindle et FireOS"
article_title: Objet Push Messaging Kindle et FireOS
page_order: 7
page_type: Référence
channel: Pousser
platform:
  - Android
  - Pare-feu
description: "Cet article explique les différents composants de l'objet Kindle et Push de FireOS."
---

# Spécification de l'objet poussé Kindle et FireOS

```json
{
   "alert": (requis, chaîne) le message de notification,
   "title": (requis, chaîne) le titre qui apparaît dans le panneau de notification,
   "extra": (optionnel, objet) des clés et des valeurs supplémentaires à envoyer dans la push,
   "message_variation_id": (optionnel, string) utilisé lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message Kindle/FireOS Push Message),
   "priorité" : (optionnel, entier) la valeur de priorité de notification,
   "collapse_key" : (optionnel, chaîne) la clé de masquage pour ce message,
   // Spécifier "default" dans le champ son jouera le son de notification standard
   "sound": (optionnel, chaîne) l'emplacement d'un son de notification personnalisé dans l'application,
   "custom_uri": (optionnel, chaîne) une URL web, ou URI du lien profond,
}
```

Le paramètre `priorité` acceptera des valeurs de `-2` à `2`, où `-2` représente la priorité "MIN" et `2` représente "MAX". `0` est la valeur "DEFAULT". Toute valeur envoyée en dehors de cette plage d'entier sera par défaut à `0`.

---
nav_title: "Objet Apple"
article_title: Objet Apple Messaging
page_order: 1
page_type: Référence
channel: Pousser
platform: iOS
description: "Cet article énumère et explique les différents objets Apple utilisés au Brésil."
---

# Spécification de l'objet push Apple

Ces objets sont utilisés pour définir ou demander des informations relatives au contenu Apple Push et Apple Push Alert.

## Objet push Apple

```json
{
   "badge": (optionnel, int) le nombre de badges après ce message,
   "alert": (requis sauf si le contenu disponible est true, string ou Apple Push Alert Object) le message de notification,
   // Spécifier "default" dans le champ son jouera le son de notification standard
   "sound": (optionnel, chaîne) l'emplacement d'un son de notification personnalisé dans l'application,
   "extra": (optionnel, objet) des clés et valeurs supplémentaires à envoyer,
   "content-available": (optionnel, booléen) si défini, Braze va ajouter le drapeau "content-available" au bloc push,
   "interruption_level": (optionnel, string: "passive", "active", "time-sensitive", ou "critical") spécifie le niveau d'interruption passé (iOS 15+),
   "relevance_score": (optionnel, float) spécifie le score de pertinence entre 0. et 1. utilisé pour regrouper les résumés de notification (iOS 15+),
   "expiration": (optionnel, La chaîne de date ISO 8601) si défini, les messages push expireront à la date spécifiée,
   "custom_uri": (optionnel, chaîne) une URL web, ou un lien profond,
   "message_variation_id": (optionnel, string) utilisée lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message Push iOS),
   "notification_group_thread_id": (optionnel, chaîne) l'ID du groupe de notification du thread avec lequel la notification sera envoyée,
   "asset_url": (optionnel, chaîne) URL de contenu pour les notifications riches pour les appareils utilisant iOS 10 ou supérieur,
   "asset_file_type": (requis si asset_url est présent, string) type de fichier de l'asset - un de "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", ou "wav",
   "collapse_id": (optionnel, Pour mettre à jour une notification sur l'appareil de l'utilisateur une fois que vous l'avez publié, envoyer une autre notification avec le même ID de masquage que vous avez utilisé précédemment
   "mutable_content": (optionnel, boolean) si vrai, Braze ajoutera le drapeau de contenu mutable au bloc et le définira à 1. L'indicateur de contenu mutable est automatiquement réglé sur 1 lors de l'envoi d'une notification riche, quelle que soit la valeur de ce paramètre.
   "send_to_most_recent_device_only": (optionnel, booléen) par défaut à false, si défini à true, Braze enverra uniquement ce push à un appareil iOS le plus récent utilisé, plutôt que tous les appareils iOS éligibles,
   "catégorie": (optionnel, string) l'identifiant de la catégorie de notification iOS pour afficher les boutons d'action push,
   "boutons" : (optionnel, tableau d'objets Apple Push Action Button Objects) pousser les boutons d'action pour afficher
}
```

Vous devez inclure un objet Push d'Apple dans `messages` si vous voulez que les utilisateurs que vous avez ciblés reçoivent une poussée sur leurs appareils iOS. Le nombre total d'octets dans votre chaîne `alerte` , l'objet `extra` et d'autres paramètres facultatifs ne doivent pas dépasser 1912. L'API Messaging retournera une erreur si vous dépassez la taille autorisée par Apple. Les messages qui incluent les clés `ab` ou `aps` dans l'objet `extra` seront rejetés.

### Objet d'alerte push Apple

Dans la plupart des cas, l'alerte `` peut être spécifiée comme une chaîne de caractères dans un objet `apple_push`.

```json
{
   "body": (requis sauf si le contenu disponible est vrai dans l'objet Push d'Apple, string) le texte du message d'alerte,
   "title": (optionnel, chaîne) une courte chaîne décrivant le but de la notification, affichée dans l'interface de notification d'Apple Watch,
   "title_loc_key": (optionnel, chaîne) la clé d'une chaîne de titre dans le `Localizable. fichier trings` pour la localisation courante,
   "title_loc_args": (optionnel, tableau de chaînes) des valeurs de chaîne variable à apparaître à la place des spécifieurs de format dans title_loc_key,
   "action_loc_key": (optionnel, chaîne) si une chaîne de caractères est spécifiée, le système affiche une alerte qui inclut les boutons Fermer et Afficher, la chaîne est utilisée comme clé pour obtenir une chaîne localisée dans la localisation courante à utiliser pour le titre du bouton droit au lieu de "View",
   "loc_key": (optionnelle, chaîne) une clé d'une chaîne alert-message dans un localisable. fichier de trings pour la localisation courante,
   "loc_args": (optionnel, tableau de chaînes) valeurs de chaîne variable à apparaître à la place des spécificateurs de format dans loc_key
}
```

## Objet de bouton d'action push Apple

Vous _devez_ inclure le champ `catégorie` dans l'Apple Push Object pour utiliser les boutons d'action push iOS. Inclure le champ `catégorie` affichera tous les boutons d'action push associés; inclure uniquement le champ `boutons` si vous voulez définir en plus les actions individuelles des boutons de clic. Le SDK Braze fournit un ensemble de boutons d'action push par défaut à utiliser (voir le tableau ci-dessous). Vous pouvez également utiliser vos propres boutons s'ils ont été enregistrés dans votre application.

### Objet de bouton d'action push d'Apple pour les boutons par défaut Braze

| Identifiant de la catégorie            | Texte du bouton | Identifiant de l'action du bouton | Actions autorisées             |
| -------------------------------------- | --------------- | --------------------------------- | ------------------------------ |
| `ab_cat_accept_decline`                | Accepter        | `Accepter ab_pb_accept`           | OUVRE_APP, URI, ou DEEP_LINK |
| `ab_cat_accept_decline`                | Refuser         | `ab_pb_decline`                   | FERMER                         |
| `Oui`                                  | Oui             | `format@@0 ab_pb_yes`             | OUVRE_APP, URI, ou DEEP_LINK |
| `Oui`                                  | Non             | `ab_pb_no`                        | FERMER                         |
| `Confirmation de l'annulation du chat` | Valider         | `Confirmer ab_pb_confirm`         | OUVRE_APP, URI, ou DEEP_LINK |
| `Confirmation de l'annulation du chat` | Abandonner      | `ab_pb_cancel`                    | FERMER                         |
| `format@@0 ab_cat_more`                | En savoir plus  | `ab_pb_plus`                      | OUVRE_APP, URI, ou DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```json
{
  "action_id": (obligatoire, chaîne) l'identifiant d'action du bouton,
  "action": (optionnel, chaîne) un de "OPEN_APP", "URI", "DEEP_LINK", ou "CLOSE". Par défaut, "OPEN_APP" ou "FERME" selon le bouton,
  "uri": (optionnel, chaîne) une URL web ou un lien profond,
  "use_webview": (optionnel, booléen) s'il faut ouvrir l'URL web dans l'application si l'action est "URI", par défaut à vrai
}
```

### Objet de bouton d'action push Apple pour les catégories définies par votre application

```json
{
  "action_id": (requis, chaîne) l'identifiant de l'action du bouton,
  "action" : (obligatoire, chaîne) une de "URI" ou "DEEP_LINK",
  "uri": (requis, string) une URL web ou un lien profond,
  "use_webview": (optionnel, booléen) si vous voulez ouvrir l'URL web dans l'application si l'action est "URI", par défaut à true
}
```

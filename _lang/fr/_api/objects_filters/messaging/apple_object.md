---
nav_title: "Objet Apple"
article_title: Objet de messagerie Apple
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "Cet article répertorie et explique les différents objets Apple utilisés chez Braze."

---

# Spécification de l’objet Notification push Apple

L’objet `apple_push` vous permet de définir ou de demander des informations relatives au contenu de notification push Apple et de notification push Apple pour les alertes via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

## Objet Notification push Apple

```json
{
   "badge": (optional, int) le décompte de badge après ce message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) le message de notification,
   // Spécifier « par défaut » dans le champ « son » jouera le son de notification par défaut
   "sound": (optional, string) l’emplacement du son de notification personnalisé dans l’appli,
   "extra": (optional, object) clés et valeurs supplémentaires à envoyer,
   "content-available": (optional, boolean) si défini, Braze ajoutera l’indicateur « content-available » (contenu disponible) à la charge utile de la notification push,
   "interruption_level": (optional, string: "passive", "active", "time-sensitive", or "critical") spécifie le passage du niveau d’interruption (iOS 15 et suivants),
   "relevance_score": (optional, float) spécifie la note de pertinence entre 0,0 et 1,0 utilisée pour regrouper les résumés de notification (iOS 15 et suivants),
   "expiry": (optional, ISO 8601 date string) si défini, les messages de notification push expireront à la date et à l’heure spécifiées,
   "custom_uri": (optional, string) une URL Web ou une URI de lien profond,
   "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de notification push iOS),
   "notification_group_thread_id": (optional, string) l’ID de fil de groupe de notification avec lequel la notification sera envoyée,
   "asset_url": (optional, string) l’URL de contenu pour les notifications enrichies pour les appareils utilisant iOS 10 ou ultérieur,
   "asset_file_type": (required if asset_url is present, string) types de fichier de l’actif ; un parmi « aif », « gif », « jpg », « m4a », « mp3 », « mp4 », « png », or « wav »,
   "collapse_id": (optional, string) Pour mettre à jour une notification sur l’appareil de l’utilisateur une fois que vous l’avez publiée, envoyez une autre notification avec le même ID de réduction que celui que vous avez utilisé précédemment.
   "mutable_content": (optional, boolean) si défini, Braze ajoutera l’indicateur « mutable-content » (contenu modifiable) à la charge utile et la règlera sur 1. L’indicateur de contenu changeant est automatiquement défini sur 1 lors de l’envoi d’une notification enrichie, quelle que soit la valeur de ce paramètre.
   "send_to_most_recent_device_only": (optional, boolean) défini par défaut sur « false » ; si défini sur « true », Braze enverra cette notification push uniquement au dernier appareil iOS dont s’est servi l’utilisateur plutôt qu’à tous les appareils iOS éligibles,
   "category": (optional, string) l’identifiant de catégorie de notification iOS pour afficher des boutons d’action push,
   "buttons" : (optional, array of Apple Push Action Button Objects) boutons d’action push à afficher
}
```

Vous devez inclure un objet de notification push Apple dans `messages` si vous voulez que les utilisateurs ciblés reçoivent une notification push sur leurs appareils iOS. Le nombre total d’octets dans votre chaîne de caractères `alert`, objet `extra` et vos autres paramètres facultatifs ne doit pas dépasser 1 912. L’API de messagerie renvoie une erreur si vous dépassez la taille de message autorisée par Apple. Les messages incluant les clés `ab` ou `aps` dans l’objet `extra` seront rejetés.

### Objet Notification push Apple pour les alertes

Dans la plupart des cas, l’`alert` peut être spécifiée comme une chaîne de caractères dans un objet `apple_push`.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) le texte du message d’alerte,
   "title": (optional, string) une chaîne de caractères courte décrivant l’objectif de la notification et affichée dans le cadre de l’interface de notification Apple Watch,
   "title_loc_key": (optional, string) la clé qui définit le string de titre pour la localisation actuelle du fichier `Localizable.strings` (chaîne de caractères localisable),
   "title_loc_args": (optional, array of strings) valeurs de string variables qui doivent apparaître à la place des formats spécifiés dans title_loc_key,
   "action_loc_key": (optional, string) si un string est spécifiée, le système affiche une alerte qui comprend les boutons « Fermer » et « Afficher ». Le string est utilisé comme clé pour obtenir un string localisé dans la localisation actuelle à utiliser pour les titres de boutons corrects à la place de « View »",
   "loc_key": (optional, string) une clé vers un string de message d’alerte dans le fichier « Localizable.strings » (chaîne de caractères localisable) pour la localisation actuelle,
   "loc_args": (optional, array of strings) valeurs de string variables qui doivent apparaître à la place des formats spécifiés dans loc_key
}
```

## Objet boutons d’action de notification push Apple

Vous devez inclure le champ `category` dans l’objet de notification push Apple pour utiliser les boutons d’action push iOS. Inclure le champ `category` affichera tous les boutons d’action push associés. N’ajoutez le champ `buttons` que si vous souhaitez définir en plus les actions de clic individuelles des boutons. Le SDK Braze fournit un ensemble de boutons d’action push par défaut que vous pouvez utiliser et qui sont présentés dans le tableau suivant. Vous pouvez également utiliser vos propres boutons s’ils ont été enregistrés dans votre application.

### Objet boutons d’action de notification push Apple pour les boutons par défaut de Braze

| Identifiant de catégorie   | Texte du bouton | Identifiant d’action du bouton | Actions autorisées         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Accepter      | `ab_pb_accept`             | OPEN_APP, URI, ou DEEP_LINK[`Retrait en magasin`]|
| `ab_cat_accept_decline` | Refuser     | `ab_pb_decline`            | FERMER                   |
| `ab_cat_yes_no`         | Oui         | `ab_pb_yes`                | OPEN_APP, URI, ou DEEP_LINK[`Retrait en magasin`]|
| `ab_cat_yes_no`         | Non          | `ab_pb_no`                 | FERMER                   |
| `ab_cat_confirm_cancel` | Confirmer     | `ab_pb_confirm`            | OPEN_APP, URI, ou DEEP_LINK[`Retrait en magasin`]|
| `ab_cat_confirm_cancel` | Annuler      | `ab_pb_cancel`             | FERMER                   |
| `ab_cat_more`           | Plus        | `ab_pb_more`               | OPEN_APP, URI, ou DEEP_LINK[`Retrait en magasin`]|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

```json
{
  "action_id": (required, string) l’identifiant d’action du bouton,
  "action": (optional, string) « OPEN_APP » « URI », « DEEP_LINK » ou « CLOSE ». Défini par défaut sur « OPEN_APP » ou « CLOSE » selon le bouton,
  "uri": (optional, string) une URL Web ou une URI de lien profond,
  "use_webview": (optional, boolean) si l’URL Web doit être ouverte dans l’app si l’action est « URI », « true » par défaut
}
```

### Objet boutons d’action de notification push Apple pour les catégories définies par votre application

```json
{
  "action_id": (required, string) l’identifiant d’action du bouton,
  "action": (required, string) « URI » ou « DEEP_LINK »,
  "uri": (required, string) une URL Web ou une URI de lien profond,
  "use_webview": (optional, boolean) si l’URL Web doit être ouverte dans l’app si l’action est « URI », « true » par défaut
}
```

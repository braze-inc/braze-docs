---
nav_title: "Objet Apple"
article_title: Objet de messagerie Apple
page_order: 1
page_type: reference
channel: push
platform: iOS
description: "Cet article de référence répertorie et explique les différents objets Apple utilisés chez Braze."

---

# Objet Notification push Apple

> L'objet `apple_push` vous permet de définir ou de demander des informations relatives au contenu Apple Push et Apple Push Alert par l'intermédiaire de nos [points d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging)

## Objet Notification push Apple

```json
{
   "badge": (optional, integer) the badge count after this message,
   "alert": (required unless content-available is true, string or Apple Push Alert Object) the notification message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "extra": (optional, object) additional keys and values to be sent,
   "content-available": (optional, boolean) if set, Braze will add the "content-available" flag to the push payload,
   "interruption_level": (optional, string: "passive", "active", "time-sensitive", or "critical") specifies the interruption level passed (iOS 15+),
   "relevance_score": (optional, float) specifies the relevance score between 0.0 and 1.0 used for grouping notification summaries (iOS 15+),
   "expiry": (optional, ISO 8601 date string) if set, push messages will expire at the specified datetime,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an iOS Push Message),
   "notification_group_thread_id": (optional, string) the notification group thread ID the notification will be sent with,
   "asset_url": (optional, string) content URL for rich notifications for devices using iOS 10 or higher,
   "asset_file_type": (required if asset_url is present, string) file type of the asset - one of "aif", "gif", "jpg", "m4a", "mp3", "mp4", "png", or "wav",
   "collapse_id": (optional, string) To update a notification on the user's device after you've issued it, send another notification with the same collapse ID you used previously
   "mutable_content": (optional, boolean) if true, Braze will add the mutable-content flag to the payload and set it to 1. The mutable-content flag is automatically set to 1 when sending a rich notification, regardless of the value of this parameter.
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used iOS device, rather than all eligible iOS devices,
   "category": (optional, string) the iOS notification category identifier for displaying push action buttons,
   "buttons" : (optional, array of Apple push action button objects) push action buttons to display,
   "apns_priority": (optional, integer) override the default apns_priority value using an integer between 1 and 10; use 10 for immediate delivery, 5 for power-aware delivery, and 1 to minimize power impact and avoid waking the device,
}
```

Vous devez inclure un objet Notification push Apple dans `messages` si vous souhaitez que les utilisateurs ciblés reçoivent une notification push sur leurs appareils iOS. Le nombre total d’octets dans votre chaîne de caractères `alert`, objet `extra` et vos autres paramètres facultatifs ne doit pas dépasser 1912. L’API de messagerie renvoie une erreur si vous dépassez la taille de message autorisée par Apple. Les messages incluant les clés `ab` ou `aps` dans l’objet `extra` seront rejetés.

{% alert note %}
Si vous envoyez l'objet Apple Push dans le cadre d'une ligne/en production/instantanée, veillez à inclure votre chaîne de caractères `sound` dans l'objet `alert`.
{% endalert %}

### Objet Notification push Apple pour les alertes

Dans la plupart des cas, l’`alert` peut être spécifiée comme une chaîne de caractères dans un objet `apple_push`.

```json
{
   "body": (required unless content-available is true in the Apple Push Object, string) the text of the alert message,
   "title": (optional, string) a short string describing the purpose of the notification, displayed as part of the Apple Watch notification interface,
   "title_loc_key": (optional, string) the key to a title string in the `Localizable.strings` file for the current localization,
   "title_loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in title_loc_key,
   "action_loc_key": (optional, string) if a string is specified, the system displays an alert that includes the Close and View buttons, the string is used as a key to get a localized string in the current localization to use for the right button's title instead of "View",
   "loc_key": (optional, string) a key to an alert-message string in a Localizable.strings file for the current localization,
   "loc_args": (optional, array of strings) variable string values to appear in place of the format specifiers in loc_key,
   "sound": (optional, string) the location of a custom notification sound within the app (live activities only),
}
```

#### Exemple

```json
{
  "broadcast": false,
  "external_user_ids": ["PushTest12"],
  "campaign_id": "9c2fefcd-9115-3932-f771-c7f43d18d6b6",
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "apple_push": {
      "alert": {
        "title": "Hello!",
        "body": "Message here"
      },
      "message_variation_id": "iosPush-640"
    }
  }
}
```

## Objet Boutons d’action de notification push Apple

Vous devez inclure le champ `category` dans l’objet Notification push Apple pour utiliser les boutons d’action push iOS. Inclure le champ `category` affichera tous les boutons d’action push associés. N’ajoutez le champ `buttons` que si vous souhaitez définir en plus les actions de clic individuelles des boutons. Le SDK Braze fournit un ensemble de boutons d’action push par défaut que vous pouvez utiliser et qui sont présentés dans le tableau suivant. Vous pouvez également utiliser vos propres boutons s’ils ont été enregistrés dans votre application.

### Objet Boutons d’action de notification push Apple pour les boutons par défaut de Braze

| Identifiant de catégorie   | Texte du bouton | Identifiant d’action du bouton | Actions autorisées         |
|-----------------------|-------------|--------------------------|-------------------------|
| `ab_cat_accept_decline` | Accepter      | `ab_pb_accept`             | OPEN_APP, URI, ou DEEP_LINK |
| `ab_cat_accept_decline` | Refuser     | `ab_pb_decline`            | FERMER                   |
| `ab_cat_yes_no`         | Oui         | `ab_pb_yes`                | OPEN_APP, URI, ou DEEP_LINK |
| `ab_cat_yes_no`         | Non          | `ab_pb_no`                 | FERMER                   |
| `ab_cat_confirm_cancel` | Confirmer     | `ab_pb_confirm`            | OPEN_APP, URI, ou DEEP_LINK |
| `ab_cat_confirm_cancel` | Annuler      | `ab_pb_cancel`             | FERMER                   |
| `ab_cat_more`           | Plus        | `ab_pb_more`               | OPEN_APP, URI, ou DEEP_LINK |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE". Defaults to either "OPEN_APP" or "CLOSE" depending on the button,
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

### Objet Boutons d’action de notification push Apple pour les catégories définies par votre application

```json
{
  "action_id": (required, string) the button's action identifier,
  "action": (required, string) one of "URI" or "DEEP_LINK",
  "uri": (required, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

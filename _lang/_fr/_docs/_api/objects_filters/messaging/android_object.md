---
nav_title: "Objets Android"
article_title: Objet Messagerie Android
page_order: 0
page_type: Référence
channel: Pousser
platform: Android
description: "Cet article liste et explique les différents objets Android utilisés à Braze."
---

# Spécification de l'objet Android

Ces objets sont utilisés pour définir ou demander des informations relatives au contenu Android Push et Android Push Alert.

## Objet push Android

Vous devez inclure un objet Push Android dans `messages` si vous voulez que les utilisateurs que vous avez ciblés reçoivent une poussée sur leurs appareils Android. Le nombre total d'octets dans votre chaîne `alerte` et l'objet `extra` ne doivent pas dépasser 4000. L'API Messaging retournera une erreur si vous dépassez la taille autorisée par Google.

### Corps

```json
{
   "alert": (requis, chaîne) le message de notification,
   "title": (requis, chaîne) le titre qui apparaît dans le panneau de notification,
   "extra": (optionnel, objet) des clés et des valeurs supplémentaires à envoyer dans la push,
   "message_variation_id": (optionnel, string) utilisé lors de la fourniture d'un campaign_id pour spécifier la variation de message sous laquelle ce message doit être suivi (doit être un message Push Android),
   "notification_channel_id" : (facultatif, chaîne) l'ID du canal avec lequel la notification sera envoyée,
   "priority": (optionnel, entier) la valeur de priorité de la notification,
   "send_to_sync" : (optionnel, si défini à true nous lancerons une erreur si "alert" ou "title" est définie),
   "collapse_key": (optionnel, chaîne) la clé de masquage pour ce message,
   // Spécifier "default" dans le champ son jouera le son de notification standard
   "sound": (optionnel, chaîne) l'emplacement d'un son de notification personnalisé dans l'application,
   "custom_uri": (optionnel, chaîne) une URL web, ou un lien profond,
   "summary_text": (optionnel, chaîne),
   "time_to_live": (optionnel, entier (secondes)),
   "notification_id": (optionnel, entier),
   "push_icon_image_url": (optionnel, chaîne) une URL d'image pour la grande icône,
   "accent_color": (optionnel, integer) la couleur d'accentuation à appliquer par les modèles de style standard lors de la présentation de cette notification, une valeur RVB entière,
   "send_to_most_recent_device_only": (optionnel, booléen) par défaut à false, si défini à true, Braze enverra uniquement ce push à l'appareil Android le plus récemment utilisé par un utilisateur plutôt que tous les appareils Android éligibles,
   "boutons" : (optionnel, tableau des objets du bouton de poussée d'action Android) pousser les boutons d'action pour afficher
   "conversation_data" : (facultatif, Android Conversation Push Object) les données à afficher via Conversation Push.
}
```


Vous pouvez envoyer des notifications "Big Picture" en spécifiant la clé `appboy_image_url` dans l'objet `extra`. La valeur de `appboy_image_url` devrait être une URL qui se connecte à l'endroit où votre image est hébergée. Les images doivent être recadrées à un ratio d'aspect 2:1 et doivent être d'au moins 600x300. Les images utilisées pour les notifications ne s'afficheront que sur les appareils fonctionnant avec Jelly Bean (Android 4.1) ou plus.

#### Détails du paramètre supplémentaire

| Paramètre                         | Détails du produit                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `priorité`                        | Ce paramètre acceptera les valeurs de `-2` à `2`, où `-2` représente la priorité "MIN" et `2` représente "MAX". `0` est la valeur "DEFAULT". <br> <br> Toute valeur envoyée qu'en dehors de cette plage d'entiers sera par défaut à 0. Pour plus d'informations sur le niveau de priorité à utiliser, veuillez consulter notre section sur [la priorité de notification Android][29]. |
| `Réduire la clé`                  | FCM peut stocker simultanément jusqu'à 4 clés réduites par appareil. Si vous utilisez plus de 4 clés réduites, FCM ne fait aucune garantie quant à celles qui seront conservées. Braze utilise l'un d'eux par défaut pour les campagnes, donc assurez-vous de ne spécifier que jusqu'à 3 clés de réduction supplémentaires pour les messages Android.                                             |
| `Ajouter une image à votre image` | La valeur du paramètre de la grande icône doit être une URL qui se connecte à l'endroit où votre image est hébergée. <br> <br> Les images doivent être recadrées à un ratio d'aspect 1:1 et doivent être d'au moins 40x40.                                                                                                                                                            |
| `Canal de notification`           | Si ce n'est pas spécifié, Braze tentera d'envoyer la charge utile de notification avec l'ID du canal [du tableau de bord][45]. Pour plus d'informations sur `notification_channel` veuillez consulter notre [documentation développeur][43] et notre [guide utilisateur sur les canaux de notification Android Push][44].                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

> Pour plus d'informations sur les messages `send_to_sync` veuillez consulter notre section sur ["Notifications Android silencieures"][28].

## Objet bouton d'action Android push

```json
{
  "text": (obligatoire, chaîne) le texte du bouton,
  "action": (facultatif, string) un de "OPEN_APP", "URI", "DEEP_LINK", ou "CLOSE", par défaut "OPEN_APP",
  "uri": (optionnel, string) une URL web ou un lien profond,
  "use_webview": (optionnel, booléen) si vous voulez ouvrir l'URL web dans l'application si l'action est "URI", par défaut à true
}
```

## Conversation Android push objet {##android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Les concepts de ce message correspondent à ceux de la [Documentation Push de conversation Android][46].

```json
{
  "shortcut_id" : (requis, chaîne) l'identifiant de raccourci de partage,
  "reply_person_id" : (requis, chaîne) l'identifiant de la Personne à laquelle ce push répond,
  "messages" : (obligatoire, tableau de l'objet message push de conversation Android),
  "personnes" : (requis, tableau d'objet de poussée de conversation Android)
}
```

### Objet message push de conversation Android

```json
{
  "text" : (obligatoire, chaîne) le texte de ce message,
  "timestamp" : (requis, entier) l'horodatage unix du moment où ce message a été envoyé,
  "person_id" : (obligatoire, chaîne) l'identifiant de la personne de l'expéditeur de ce message,
}
```

### Objet push personne de conversation Android

```json
{
  "id" : (obligatoire, chaîne) l'identifiant de cette personne,
  "name" : (obligatoire, chaîne) le nom d'affichage de cette personne
}
```

[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/silent_push_notifications/#silent-push-notifications
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[44]: {{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/
[43]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels
[45]: {{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/#notification-channels
[46]: https://developer.android.com/guide/topics/ui/conversations
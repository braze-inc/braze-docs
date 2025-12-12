---
nav_title: "Objets Android"
article_title: Objet Messagerie Android
page_order: 0
page_type: reference
channel: push
platform: Android
description: "Cet article de référence répertorie et explique les différents objets Android utilisés chez Braze."

---
# Objet Android

> L'objet `android_push` vous permet de définir ou de demander des informations relatives au contenu Android Push et Android Push Alert par le biais de nos [points d'extrémité de messages.]({{site.baseurl}}/api/endpoints/messaging)

## Objet Notification push Android

Vous devez inclure un objet Android push dans `messages` si vous voulez que les utilisateurs que vous avez ciblés reçoivent un push sur leurs appareils Android. Le nombre total d'octets de votre chaîne de caractères `alert` et de votre objet `extra` ne doit pas dépasser 4 000. L’API de messagerie renvoie une erreur si vous dépassez la taille de message autorisée par Google.

```json
{
   "alert": (required, string) the notification message,
   "title": (required, string) the title that appears in the notification drawer,
   "extra": (optional, object) additional keys and values to be sent in the push,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be an Android Push Message),
   "notification_channel_id": (optional, string) the channel ID the notification will be sent with,
   "priority": (optional, integer) the notification priority value,
   "android_priority": (optional, string) the FCM sender priority,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) the collapse key for this message,
   // Specifying "default" in the sound field will play the standard notification sound
   "sound": (optional, string) the location of a custom notification sound within the app,
   "custom_uri": (optional, string) a web URL, or Deep Link URI,
   "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to false,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (maximum of 2,419,200 seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) an image URL for the large icon,
   "accent_color": (optional, integer) accent color to be applied by the standard Style templates when presenting this notification, an RGB integer value,
   "send_to_most_recent_device_only": (optional, boolean) defaults to false, if set to true, Braze will only send this push to a user's most recently used Android device, rather than all eligible Android devices,
   "buttons" : (optional, array of Android push action button objects) push action buttons to display
   "conversation_data" : (optional, Android Conversation Push Object) the data to be displayed through Conversation Push
}
```

Vous pouvez envoyer des notifications « Big Picture » en spécifiant la clé `appboy_image_url` dans l’objet `extra`. La valeur de `appboy_image_url` doit être une URL qui renvoie à l’emplacement où votre image est hébergée. Les images doivent être recadrées à un rapport hauteur/largeur de 2:1 et doivent avoir une taille minimale de 600 x 300 px.

### Informations relatives aux paramètres supplémentaires

| Paramètre | Détails |
| --------- | ------- |
| `priority` | Ce paramètre accepte les valeurs entre `-2` et `2`, où `-2` représente la priorité « MIN » et `2` représente la priorité « MAX ». `0` est la valeur « PAR DÉFAUT ». <br> <br> Toutes les valeurs envoyées en dehors de cette plage prendront la valeur 0 par défaut. Pour plus d'informations sur le niveau de priorité à utiliser, voir [Priorité des notifications Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority). |
| `android_priority` | Ce paramètre accepte les valeurs `normal` ou `high` pour spécifier la priorité de l'expéditeur FCM. Par défaut, les messages sont envoyés avec la priorité par défaut du FCM configurée dans la page [Paramètres de poussée]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings/#default-fcm-priority-for-android-campaigns).<br><br> Pour plus d'informations sur l'impact des différentes valeurs sur la réception/distribution, voir [Priorité des messages Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority). |
| `collapse_key` | FCM peut stocker simultanément jusqu’à quatre clés de réduction par appareil. Si vous utilisez plus de quatre clés de réduction, FCM ne donne aucune garantie quant à celles qui seront conservées. Braze utilise l’un de ces éléments par défaut pour les campagnes, assurez-vous donc de ne spécifier que jusqu’à trois clés de réduction supplémentaires pour les messages Android. |
| `push_icon_image_url` | La valeur du paramètre des grandes icônes doit être une URL qui renvoie à l’emplacement où votre image est hébergée. <br> <br> Les images doivent être recadrées selon un apport hauteur/largeur  1:1 et mesurer au moins 40x40. |
| `notification_channel` | Si cela n'est pas spécifié, Braze tentera d'envoyer la charge utile de la notification avec l'ID du canal de [repli du tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel). Pour en savoir plus, consultez la section [Canaux de notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/) et reportez-vous aux étapes de [définition des canaux de notification]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels) lors de l'intégration. |
| `send_to_sync` | Pour plus d'informations sur les messages `send_to_sync`, consultez [les notifications Android silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Objet Bouton d’action push Android

```json
{
  "text": (required, string) the button's text,
  "action": (optional, string) one of "OPEN_APP", "URI", "DEEP_LINK", or "CLOSE", defaults to "OPEN_APP",
  "uri": (optional, string) a web URL or Deep Link URI,
  "use_webview": (optional, boolean) whether to open the web URL inside the app if the action is "URI", defaults to true
}
```

## Objet de notification push de conversation pour Android {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Les concepts présentés dans ce message correspondent à ceux de la documentation [Android People et Conversations](https://developer.android.com/guide/topics/ui/conversations) push.

```json
{
  "shortcut_id" : (required, string) the sharing shortcut identifier,
  "reply_person_id" : (required, string) the identifier of the Person this push is replying to,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Objet Notification push Android de conversation pour les messages

```json
{
  "text" : (required, string) the text of this message,
  "timestamp" : (required, integer) the unix timestamp of when this message was sent,
  "person_id" : (required, string) the Person identifier of this message's sender,
}
```

### Objet Notification push Android de conversation pour les personnes

```json
{
  "id" : (required, string) the identifier of this Person,
  "name" : (required, string) the display name of this Person
}
```


---
nav_title: "Objets Android"
article_title: Objet de messagerie Android
page_order: 0
page_type: reference
channel: push
platform: Android
description: "Cet article répertorie et explique les différents objets Android utilisés chez Braze."

---
# Spécification d’objet Android

L’objet `android_push` vous permet de définir ou de demander des informations relatives au contenu de notification push Android et de notification push Android pour les alertes via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging).

##  Objet de notification push Android

Vous devez inclure un objet de notification push Android dans `messages` si vous voulez que les utilisateurs ciblés reçoivent une notification push sur leurs appareils Android. Le nombre total d’octets dans votre chaîne de caractères `alert` et objet `extra` ne doit pas dépasser 4 000. L’API de messagerie renvoie une erreur si vous dépassez la taille de message autorisée par Google.

### Corps

```json
{
   "alert": (required, string) le message de notification,
   "title": (required, string) le titre qui apparaît dans la barre de notifications,
   "extra": (optional, object) clés et valeurs supplémentaires à envoyer dans la notification push,
   "message_variation_id": (optional, string) utilisé lorsqu’un campaign_id est fourni pour spécifier avec quelle variation du message ce message doit être suivi (il doit s’agir d’un message de notification push Android),
   "notification_channel_id": (optional, string) l’ID de canal avec lequel les notifications vont être envoyées,
   "priority": (optional, integer) la valeur de priorité de la notification,
   "send_to_sync": (optional, if set to true we will throw an error if "alert" or "title" is set),
   "collapse_key": (optional, string) la touche de réduction pour ce message,
   // Spécifier « par défaut » dans le champ « son » jouera le son de notification par défaut
   "sound": (optional, string) l’emplacement du son de notification personnalisé dans l’appli,
   "custom_uri": (optional, string) une URL Web ou une URI de lien profond,
   "summary_text": (optional, string),
   "time_to_live": (optional, integer (seconds)),
   "notification_id": (optional, integer),
   "push_icon_image_url": (optional, string) une URL d’image pour la grande icône,
   "accent_color": (optional, integer) couleur d’accentuation devant être appliquée par le modèle de style standard lorsque cette notification est transmise, une valeur entière RGB,
   "send_to_most_recent_device_only": (optional, boolean) défini par défaut sur « false » ; si défini sur « true », Braze enverra cette notification push uniquement au dernier appareil Android dont s’est servi l’utilisateur plutôt qu’à tous les appareils Android éligibles,
   "buttons" : (optional, array of Android Push Action Button Objects) boutons d’action push à afficher
   "conversation_data" : (optional, Android Conversation Push Object) les données à afficher via la notification push de conversion.
}
```


Vous pouvez envoyer des notifications « Big Picture » en spécifiant la clé `appboy_image_url` dans l’objet `extra`. La valeur de `appboy_image_url` doit être une URL qui renvoie à l’emplacement où votre image est hébergée. Les images doivent être recadrées au format 2:1 et mesurer au moins 600x300. Les images utilisées pour les notifications ne s’afficheront que sur les périphériques exécutant Jelly Bean (Android 4.1) ou une version supérieure.

#### Informations relatives aux paramètres supplémentaires

| Paramètre | Informations |
| --------- | ------- |
| `priority` | Ce paramètre accepte les valeurs entre `-2` et `2`, où `-2` représente la priorité « MIN » et `2` représente la priorité « MAX ». `0` est la valeur « PAR DÉFAUT ». <br> <br> Toutes les valeurs envoyées en dehors de cette plage d’entiers seront par défaut à 0. Pour plus d’informations sur le niveau de priorité à utiliser, consultez notre section sur la [priorité de notification Android][29]. |
| `collapse_key` | FCM peut stocker simultanément jusqu’à quatre clés de réduction par dispositif. Si vous utilisez plus de quatre clés de réduction, FCM ne donne aucune garantie quant à celles qui seront conservées. Braze utilise l’un de ces éléments par défaut pour les campagnes, assurez-vous donc de ne spécifier que jusqu’à trois clés de réduction supplémentaires pour les messages Android. |
| `push_icon_image_url` | La valeur du paramètre des grandes icônes doit être une URL qui renvoie à l’emplacement où votre image est hébergée. <br> <br> Les images doivent être recadrées au format 1:1 et mesurer au moins 40x40. |
| `notification_channel` | S’il n’est pas spécifié, Braze tentera d’envoyer la charge utile de notification avec l’ID de canal [de repli du tableau de bord][45]. Pour en savoir plus, consultez les [canaux de notification][44] et reportez-vous aux étapes de la [définition des canaux de notification][43] pendant l’intégration. |
| `send_to_sync` | Pour plus d’informations sur les messages `send_to_sync`, consultez les [notifications silencieuses Android][28]. |
{: .reset-td-br-1 .reset-td-br-2}


## Objet Bouton d’action push Android

```json
{
  "text": (required, string) le texte du bouton,
  "action": (optional, string) « OPEN_APP », « URI », « DEEP_LINK », ou « CLOSE », défini par défaut sur « OPEN_APP »,
  "uri": (optional, string) une URL Web ou une URI de lien profond,
  "use_webview": (optional, boolean) si l’URL Web doit être ouverte dans l’app si l’action est « URI », « true » par défaut
}
```

## Objet de notification push de conversation pour Android {#android-conversation-push-object}

{% sdk_min_versions android:15.0.0 %}

Les concepts de ce message correspondent à ceux dans la documentation de notification push [Utilisateurs et conversations Android][46].

```json
{
  "shortcut_id" : (required, string) l’identifiant de raccourci du partage,
  "reply_person_id" : (required, string) l’identifiant de la personne à qui cette notification push répond,
  "messages" : (required, array of Android Conversation Push Message Object),
  "persons" : (required, array of Android Conversation Push Person Object)
}
```

### Objet Notification push Android de conversation pour les messages

```json
{
  "text" : (required, string) le texte de ce message,
  "timestamp" : (required, integer) l’horodatage Unix de quand ce message a été envoyé,
  "person_id" : (required, string) l’identifiant de la personne qui a expédié ce message,
}
```

### Objet Notification push Android de conversation pour les personnes

```json
{
  "id" : (required, string) l’identifiant de cette personne,
  "name" : (required, string) le nom affiché de cette personne
}
```

[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/#silent-push-notifications
[29]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/
[44]: {{site.baseurl}}/user_guide/message_building_by_channel/push/notification_channels/
[43]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels
[45]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel
[46]: https://developer.android.com/guide/topics/ui/conversations
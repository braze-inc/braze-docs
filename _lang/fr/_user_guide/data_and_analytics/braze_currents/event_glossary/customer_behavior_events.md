---
nav_title: Comportement des clients et événements utilisateur
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportement des clients et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 7
---

Contactez votre conseiller Braze ou ouvrez un [ticket de support ]({{site.baseurl}}/braze_support/) si vous avez besoin d’accéder à des événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [Bibliothèque des Événements d’engagement sur les messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) ou notre [Exemples d’échantillons de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication du comportement des clients et de la structure des événements utilisateur et des valeurs de la plateforme %}

### Structure d’événement 

Cette ventilation des comportement des clients et des événements utilisateur montre le type d’informations généralement incluses dans un comportement des clients ou événement utilisateur. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe BI peuvent utiliser les données d’événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des précieux indicateurs de données fournis. 

![Décomposition d’un événement utilisateur montrant un événement d’achat avec les propriétés spécifiques à l’utilisateur, les propriétés spécifiques au comportement et les propriétés spécifiques à l’appareil]({% image_buster /assets/img/customer_engagement_event.png %})

Le comportement des clients et les événements utilisateur sont composés de propriétés **spécifique à l’utilisateur**, **spécifique au comportement** propriétés, et **spécifique à l’appareil**.. 

### Valeurs de la plateforme

Certains événements renvoient une valeur `platform` qui spécifie la plate-forme de l’appareil de l’utilisateur. 
<br>Le tableau suivant détaille les valeurs retournées possibles :

| Appareil de l’utilisateur | Valeur de la plateforme |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2}

{% enddetails %}

{% alert important %}
Notez que ces schémas ne s’appliquent qu’aux données d’événements de fichiers plats que nous envoyons aux partenaires d’entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage) et qu’ils ne sont pas disponibles pour les connecteurs de Segment.io. Pour les schémas applicables à d’autres partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) et vérifiez leurs pages respectives.<br><br>De plus, notez que Currents ignorera les événements avec des charges utiles excessivement importantes de plus de 900 Ko. 

{% endalert %}
{% api %}

## Événements personnalisés

{% apitags %}
Événements personnalisés
{% endapitags %}

Cet événement se produit lorsqu’un événement personnalisé spécifique est déclenché. Utilisez cette option pour suivre les événements personnalisés pour les utilisateurs dans votre application.

```json
// Custom Event: users.behaviors.CustomEvent
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_group_id": (required, string) BSON id of the app group this user belongs to, 
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "gender": (optional, string) [PII] gender of the user, 
  "country": (optional, string) [PII] country of the user, 
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "language": (optional, string) [PII] language of the user,
  "device_id": (optional, string) id of the device on which the event occurred,
  "sdk_version": (optional, string) version of the Braze SDK in use during the event, 
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "name": (required, string) name of the custom event,
  "properties": (string) JSON encoded string of the properties for this event,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```

#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.

{% endapi %}
{% api %}

## Événement d’achat

{% apitags %}
Achats
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur effectue un achat. Utilisez ces données pour suivre les utilisateurs qui achètent quelque chose dans l’application.

{% alert tip %}
Les achats sont des événements personnalisés spéciaux et sont accompagnés d’une string JSON encodée de propriétés d’événement personnalisé comme pour les événements personnalisés.
{% endalert %}

```json
// Purchase Event: users.behaviors.Purchase
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "app_id": (optional, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "device_id": (optional, string) id of the device on which the event occurred,
  "sdk_version": (optional, string) version of the Braze SDK in use during the purchase,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "product_id": (required, string) id of the product purchased,
  "price": (required, float) price of the purchase,
  "currency": (required, string) three letter alpha ISO 4217 currency code,
  "properties": (required, string) JSON encoded string of the custom properties for this event,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}


{% api %}

## Événement de première session

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur commence sa première session dans votre application. Utilisez ces données pour suivre quand les utilisateurs commencent les sessions. 

{% alert tip %}
Lorsqu’un utilisateur commence sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés.
{% endalert %}

```json
// Session Start: users.behaviors.app.FirstSession
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (optional, string) IANA time zone of the user at the time of the event,
  "session_id": (required, string) id of the session,
  "app_id": (required, string) id for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the session occurred,
  "gender": (optional, string) gender of the user,
  "country": (optional, string) country of the user,
  "language": (optional, string) language of the user,
  "sdk_version": (optional, string) version of the Braze SDK in use during the session
}
```
{% endapi %}

{% api %}

## Événement de début de session

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur démarre une session. Utilisez ces données pour suivre quand les utilisateurs commencent les sessions.

{% alert tip %}
Lorsqu’un utilisateur commence sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés.
{% endalert %}

```json
// Session Start: users.behaviors.app.SessionStart
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "session_id": (required, string) id of the session,
  "app_id": (required, string) id for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the session occurred
}
```

{% endapi %}

{% api %}

## Événement de fin de session

{% apitags %}
Sessions
{% endapitags %}

Cela se produit lorsqu’un utilisateur quitte votre application, ce qui termine sa session actuelle. Utilisez ces données pour suivre les sessions. Avec l’événement de début de session, il permet de calculer la durée des sessions des utilisateurs.

{% alert tip %}
Lorsqu’un utilisateur commence sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés.
{% endalert %}

```json
// Session End: users.behaviors.app.SessionEnd
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "session_id": (required, string) id of the session,
  "duration": (optional, float) seconds session lasted,
  "app_id": (required, string) id for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the session occurred
}
```
{% endapi %}

{% api %}

## Événement de localisation

{% apitags %}
Emplacements
{% endapitags %}

Cet événement est déclenché lorsqu’un utilisateur est à un endroit spécifié. Utilisez cette option pour suivre les utilisateurs qui déclenchent des événements de localisation dans votre application.

```json
// Location Event: users.behaviors.Location
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "app_group_id": (required, string) BSON id of the app group this user belongs to, 
  "app_id": (required, string) id for the app on which the user action occurred,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "longitude": (required, float) longitude of recorded location,
  "latitude": (required, float) latitude of recorded location,
  "altitude": (optional, float) altitude of recorded location,
  "ll_accuracy": (optional, float) latitude/longitude accuracy of recorded location,
  "alt_accuracy": (optional, float) altitude accuracy of recorded location,
  "device_id": (optional, string) id of the device on which the event occurred,
  "sdk_version": (optional, string) version of the Braze SDK in use when the location was recorded,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "ad_id": (optional, string) advertising identifier,
  "ad_id_type": (optional, string) One of 'ios_idfa', 'google_ad_id', OR 'roku_ad_id',
  "ad_tracking_enabled": (optional, boolean) whether advertising tracking is enabled for the device
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule de fonctionnalité pour envoyer un `ad_id`.
{% endapi %}

{% api %}

## Événement d’impression du Fil d'actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% apitags %}
Impression, Fil d’actualité
{% endapitags %}

Cet événement se produit lorsque l’utilisateur regarde l’intégralité du Fil d'actualité et non une carte de fil d'actualité spécifique. Utilisez cette option pour suivre les utilisateurs qui consultent le fil d’actualités.

{% alert tip %}
Nous suivons d’autres fils d'actualité ; ils sont situés dans [Événements d’engagement sur les messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/).
{% endalert %}

```json
// News Feed Impression: users.behaviors.app.NewsFeedImpression
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "time": (required, int) 10-digit UTC time of the event in seconds since the epoch,
  "app_id": (required, string) id for the app on which the user action occurred,
  "platform": (optional, string) platform of the device (one of 'ios', 'android', 'web', 'kindle', 'tvos', OR 'roku'),
  "os_version": (optional, string) os version of the device used for the action,
  "device_model": (optional, string) hardware model of the device,
  "device_id": (optional, string) id of the device on which the event occurred
}
```

{% endapi %}
{% api %}

## Événements d’attribution

{% apitags %}
Attribution
{% endapitags %}

Cet événement se produit lorsqu’une installation d’application est attribuée à une source. Utilisez cette option pour savoir d’où viennent les installations de votre application.

```json
// Install Attribution Event: users.behaviors.InstallAttribution
{
  "id": (required, string) unique id of this event,
  "user_id": (required, string) Braze user id of the user,
  "external_user_id": (optional, string) External ID of the user,
  "device_id": (optional, string) device_id that is tied to this user if user is anonymous,
  "app_group_id": (required, string) BSON id of the app group this user belongs to,
  "time": (requierd, int) 10-digit UTC time of the event in seconds since the epoch,
  "source": (required, string) the source of the attribution
}
```

{% endapi %}

{% api %}

## Événement de numéro de compartiment aléatoire

{% apitags %}
Numéro de compartiment aléatoire
{% endapitags %}

Cet événement utilisateur se produit chaque fois qu’un nouvel utilisateur est créé dans son groupe d’apps. Au cours de cet événement, chaque nouvel utilisateur reçoit un numéro de compartiment aléatoire que vous pouvez ensuite utiliser pour créer des segments  d’utilisateurs aléatoires distribués uniformément Utilisez cette option pour regrouper une série de valeurs de numéro de compartiment aléatoire et comparer les performances à travers vos campagnes et variantes de campagne. 

```json
// Random Bucket Number Event: users.RandomBucketNumberUpdate
{
  "id": (string) unique id of this event,
  "app_group_id": (string) AppGroup API id
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) UTC time of the event in milliseconds since the epoch,
  "random_bucket_number": (int) new random bucket number
  "prev_random_bucket_number":  (int) old random bucket number, optional
}
```

{% alert important %}
Notez que cet événement Currents est uniquement disponible pour les clients ayant acheté un « Connecteur de tous les événements » et qu’il est uniquement disponible pour les connecteurs d’événements de stockage (par ex. Amazon S3, Microsoft Azure, Google Cloud Storage).
<br><br>Pour que cet événement soit activé et pour programmer le réapprovisionnement des numéros de compartiment aléatoires des utilisateurs existants dans votre groupe d’apps, contactez votre gestionnaire du succès des clients.
{% endalert %}

{% endapi %}



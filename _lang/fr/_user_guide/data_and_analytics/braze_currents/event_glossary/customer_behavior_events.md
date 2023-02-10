---
nav_title: Comportement des clients et événements utilisateur
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportement des clients et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 3
---

Contactez votre conseiller Braze ou ouvrez un [ticket de support ]({{site.baseurl}}/braze_support/) si vous avez besoin d’accéder à des événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [Bibliothèque des Événements d’engagement sur les messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) ou notre [Exemples d’échantillons de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication du comportement des clients, de la structure d’un événement utilisateur, et des valeurs de plateforme %}

### Structure d’un événement 

Cette ventilation des comportement des clients et des événements utilisateur montre le type d’informations généralement incluses dans un comportement des clients ou événement utilisateur. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe BI peuvent utiliser les données d’événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des métriques de données fournies. 

![Décomposition d’un événement utilisateur montrant un événement d’achat avec les propriétés spécifiques à l’utilisateur, les propriétés spécifiques au comportement et les propriétés spécifiques à l’appareil]({% image_buster /assets/img/customer_engagement_event.png %})

Le comportement des clients et les événements utilisateur sont composés de propriétés **spécifique à l’utilisateur**, **spécifique au comportement** propriétés, et **spécifique à l’appareil**.. 

### Valeurs de la plateforme

Certains événements renvoient une valeur`platform` qui spécifie la plate-forme de l’appareil de l’utilisateur. 
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
// Custom Event : users.behaviors.CustomEvent
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "name": (string) nom de l’événement personnalisé,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel l’événement s’est produit,
  "properties": (string) chaîne de caractères codée en JSON des propriétés pour cet événement,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```

#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.

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
// Purchase Event : users.behaviors.Purchase
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "product_id": (string) identifiant du produit acheté,
  "price": (float) prix de l’achat,
  "currency": (string) code de devise ISO 4217 alphabétique à trois lettres,
  "properties": (string) chaîne de caractères codée en JSON des propriétés personnalisées pour cet événement,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}


{% api %}

## Événement de première session

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu’un utilisateur commence sa première session dans votre application. Utilisez ces données pour suivre quand les utilisateurs commencent les sessions. 

{% alert tip %}
Lorsqu’un utilisateur commence sa première session, les événements `FirstSession` et `SessionStart` sont déclenchés.
{% endalert %}

```json
// Démarrage de Session : users.behaviors.app.FirstSession
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "session_id": (string) identifiant de la session,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel la session s’est produite,
  "gender": (string) genre de l’utilisateur,
  "country": (string) pays de l’utilisateur,
  "language": (string) langue de l’utilisateur,
  "sdk_version": (string) version du SDK Braze utilisée pendant la session
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
Lorsqu’un utilisateur commence sa première session, les événements `FirstSession` et `SessionStart` sont déclenchés.
{% endalert %}

```json
// Démarrage de Session : users.behaviors.app.SessionStart
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "session_id": (string) identifiant de la session,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel la session s’est produite
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
Lorsqu’un utilisateur commence sa première session, les événements `FirstSession` et `SessionStart` sont déclenchés.
{% endalert %}

```json
// Fin de Session : users.behaviors.app.SessionEnd
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "session_id": (string) identifiant de la session,
  "duration": (float) durée de la session en secondes,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel la session s’est produite
}
```
{% endapi %}

{% api %}

## Événement de localisation

{% apitags %}
Locations
{% endapitags %}

Cet événement est déclenché lorsqu’un utilisateur est à un endroit spécifié. Utilisez cette option pour suivre les utilisateurs qui déclenchent des événements de localisation dans votre application.

```json
// Événement de position : users.behaviors.Location
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "longitude": (float) longitude du lieu enregistré,
  "latitude": (float) latitude du lieu enregistré,
  "altitude": (float) altitude du lieu enregistré,
  "ll_accuracy": (float) précision de la latitude et longitude du lieu enregistré,
  "alt_accuracy": (float) précision de l’altitude du lieu enregistré,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel l’événement s’est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un parmi 'ios_idfa', 'google_ad_id', 'windows_ad_id' OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l’appareil ou non
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez collecter explicitement les idfa iOS et les adid Android Google via les SDK natifs. Pour en savoir plus cliquez ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) , contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte pour activer la bascule Oui/Non pour l’envoi`ad_id`.
{% endapi %}

{% api %}

## Événement d’impression du Fil d'actualité

{% alert note %}
Les fils d’actualités deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% apitags %}
Impression, Fil d’actualité
{% endapitags %}

Cet événement se produit lorsque l’utilisateur regarde l’intégralité du Fil d'actualité et non une carte de fil d'actualité spécifique. Utilisez cette option pour suivre les utilisateurs qui consultent le fil d’actualités.

{% alert tip %}
Nous suivons d’autres fils d'actualité ; ils sont situés dans [Événements d’engagement sur les messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/).
{% endalert %}

```json
// Impression de fil d’actualité : users.behaviors.app.NewsFeedImpression
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "app_id": (string) identifiant de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (un parmi 'ios', 'android', 'web', 'kindle', 'tvos' OU 'roku'),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "device_id": (string) identifiant de l’appareil sur lequel l’événement s’est produit
}
```

{% endapi %}
{% api %}

## Événements d’attribution

{% apitags %}
Événements d’attribution
{% endapitags %}

Cet événement se produit lorsqu’une installation d’application est attribuée à une source. Utilisez cette option pour savoir d’où viennent les installations de votre application.

```json
// Événement d’attribution d’installation : users.behaviors.InstallAttribution
{
  "id": (string) identifiant unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "source": (string) la source de l’attribution
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
// Événement de numéro de compartiment aléatoire : users.RandomBucketNumberUpdate
{
  "id": (string) identifiant unique de cet événement,
  "app_group_id": (string) identifient API du groupe d’apps
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC de l’événement, en millisecondes, depuis la période,
  "random_bucket_number": (int) nouveau numéro de compartiment aléatoire
  "prev_random_bucket_number":  (int) ancien numéro de compartiment aléatoire, optionnel
}
```

{% alert important %}
Notez que cet événement Currents est uniquement disponible pour les clients ayant acheté un « Connecteur de tous les événements » et qu’il est uniquement disponible pour les connecteurs d’événements de stockage (par ex. Amazon S3, Microsoft Azure, Google Cloud Storage).
<br><br>Pour que cet événement soit activé et pour programmer le réapprovisionnement des numéros de compartiment aléatoires des utilisateurs existants dans votre groupe d’apps, contactez votre gestionnaire du succès des clients.
{% endalert %}

{% endapi %}


---
nav_title: Comportement du client et événements de l'utilisateur
layout: glossaire des événements du client
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire énumère les différents comportements des clients et les événements des utilisateurs que Braze peut suivre et envoyer aux entrepôts de données choisis à l'aide de Courants."
tool: Courants
---

Veuillez contacter votre représentant de Braze ou ouvrir un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événement supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin ci-dessous, Consultez notre [bibliothèque d'événements d'engagement de messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/) ou nos exemples de données [courants](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explanation of Customer Behavior and User Event Structure %}
<br>
Ce comportement du client et les événements de l'utilisateur indiquent quel type d'information est généralement inclus dans le comportement du client ou dans un événement de l'utilisateur. Grâce à une bonne compréhension de ses composants, vos développeurs et votre équipe de stratégie de renseignements commerciaux peuvent utiliser les données des événements entrants pour faire des rapports basés sur des données. et tirer parti d'autres indicateurs de données précieux.

![image]({% image_buster /assets/img/customer_engagement_event.png %})

Les événements de comportement client et d'événements utilisateur sont composés de __propriétés__ spécifiques à l'utilisateur, __propriétés__ spécifiques au comportement et __propriétés spécifiques au périphérique__.

{% enddetails %}

{% alert important %}
Veuillez noter que ces schémas ne s'appliquent qu'aux données d'événement de fichier à plat que nous envoyons aux partenaires de Data Warehouse (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage), et ne sont pas disponibles pour les connecteurs Segment. Pour le schéma qui s'applique à d'autres partenaires, veuillez consulter [leurs pages respectives]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/).<br><br>De plus, notez que les courants abandonneront les événements avec des charges excessivement grandes de plus de 900KB.

{% endalert %}
{% api %}

## Événements personnalisés

{% apitags %}
Événements personnalisés
{% endapitags %}

Cet événement se produit lorsqu'un événement personnalisé spécifique est déclenché. Utilisez ceci pour suivre lorsque les utilisateurs effectuent des événements personnalisés dans votre application.

```json
// Événement personnalisé: users.behaviors. ustomEvent
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "name": (chaîne) nom de l'événement personnalisé,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "properties": (string) chaîne de caractères encodée en JSON des propriétés pour cet événement,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```

#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.

{% endapi %}
{% api %}

## Événement d'achat

{% apitags %}
Achats
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur fait un achat. Utilisez ces données pour suivre lorsque les utilisateurs achètent quelque chose dans l'application.

{% alert tip %}
Les achats sont des événements spéciaux personnalisés et sont fournis avec une chaîne encodée en JSON de propriétés d'événements personnalisés de la même manière que les événements personnalisés le font.
{% endalert %}

```json
// Événement d'Achat: users.behaviors. urchase
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "product_id": (string) id du produit acheté,
  "prix" : (float) prix de l'achat,
  "devise" : (chaîne) alpha alpha de trois lettres ISO 4217 code de devise,
  "properties": (chaîne) chaîne encodée en JSON des propriétés personnalisées pour cet événement,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}


{% api %}

## Événement de la première session

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur démarre sa première session dans votre application. Utilisez ces données pour suivre lorsque les utilisateurs démarrent des sessions.

{% alert tip %}
Quand un utilisateur démarre sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés.
{% endalert %}

```json
// Début de la session: users.behaviors.app. irstSession
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "session_id" : (string) id de la session,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel la session s'est produite,
  "genre" : (chaîne) sexe de l'utilisateur,
  "pays": (chaîne) pays de l'utilisateur,
  "langue": (chaîne) langue de l'utilisateur,
  "sdk_version": (string) version du Braze SDK utilisée pendant la session
}
```
{% endapi %}

{% api %}

## Événement de début de session

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur démarre une session. Utilisez ces données pour suivre lorsque les utilisateurs démarrent des sessions.

{% alert tip %}
Quand un utilisateur démarre sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés.
{% endalert %}

```json
// Début de la session: users.behaviors.app. essionStart
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "session_id": (string) id de la session,
  "app_id": (string) id de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "platform": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel la session s'est produite
}
```

{% endapi %}

{% api %}

## Événement de fin de session

{% apitags %}
Sessions
{% endapitags %}

Cela se produit lorsqu'un utilisateur quitte votre application, mettant ainsi fin à sa session courante. Utilisez ces données pour suivre lorsque les sessions se terminent, et avec l'événement de début de session approprié, calculer la durée de leur temps dans une session.

{% alert tip %}
Quand un utilisateur démarre sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés.
{% endalert %}

```json
// Fin de session : users.behaviors.app. essionEnd
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "session_id": (string) id de la session,
  "duration": (float) secondes session durée,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel la session s'est produite
}
```
{% endapi %}

{% api %}

## Événement de localisation

{% apitags %}
Emplacements
{% endapitags %}

Cet événement est déclenché lorsqu'un utilisateur visite un emplacement spécifié. Utilisez ceci pour suivre les utilisateurs déclenchant des événements de localisation dans votre application.

```json
// Événement d'emplacement: users.behaviors. ocation
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "longitude": (flottant) longitude de l'emplacement enregistré,
  "latitude": (flottant) latitude de l'emplacement enregistré,
  "altitude": (float) altitude de l'emplacement enregistré,
  "ll_accuracy": précision de latitude/longitude (float) de l'emplacement enregistré,
  "alt_accuracy": (float) altitude précision de l'emplacement enregistré,
  "app_id": (string) id de l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme": (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version de l'appareil utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit,
  "ad_id": (string) identifiant publicitaire,
  "ad_id_type": (string) Un de 'ios_idfa', 'google_ad_id', 'windows_ad_id', OU 'roku_ad_id',
  "ad_tracking_enabled": (boolean) si le suivi publicitaire est activé pour l'appareil
}
```
#### Détails de la propriété
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devrez explicitement collecter l'idfa iOS et Android Google adid à travers les SDK natifs. En savoir plus à leur sujet ici : [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données de [courants]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) contactez votre Responsable de la Customer Success ou le Gestionnaire de comptes pour activer la fonction flipper pour envoyer `ad_id`.
{% endapi %}

{% api %}

## Événement "Infos"

{% apitags %}
Impression, Flux d'actualité
{% endapitags %}

Cet événement se produit lorsque l'utilisateur consulte le fil d'actualité en entier et non pas une fiche d'actualité spécifique. Utilisez ceci pour suivre les utilisateurs qui consultent le flux d'actualités.

{% alert tip %}
Nous suivons les autres événements du flux d'actualités ; ceux-ci se trouvent dans [Événements d'engagement de messages]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/).
{% endalert %}

```json
// Impression du flux d'actualités: users.behaviors.app. ewsFeedImpression
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "plate-forme" : (chaîne) plate-forme de l'appareil (iOS, Android, web, etc. ,
  "os_version": (string) os version du périphérique utilisé pour l'action,
  "device_model": (string) modèle matériel de l'appareil,
  "device_id": (string) id de l'appareil sur lequel l'événement s'est produit
}
```

{% endapi %}
{% api %}
## Désinstaller les événements

{% apitags %}
Désinstaller
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur désinstalle une application. Utilisez ces données pour suivre lorsque les utilisateurs désinstallent une application.

{% alert important %}
Veuillez noter que ceci n'est pas déclenché lorsque l'utilisateur désinstalle l'application, ce qui est impossible à suivre exactement. Braze envoie un push quotidien silencieux pour déterminer si l'application existe toujours sur l'appareil de votre utilisateur, et si nous obtenons une erreur sur cette poussée silencieuse, il est supposé que l'application a été désinstallée.
{% endalert %}

```json
// Désinstaller l'événement: users.behaviors. ninstall
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "app_id": (string) id pour l'application sur laquelle l'action de l'utilisateur s'est produite,
  "device_id" : (chaîne) id de l'appareil sur lequel la session s'est produite
}
```

{% endapi %}

{% api %}

## Événements d'attribution

{% apitags %}
Attribution
{% endapitags %}

Cet événement se produit lorsqu'une installation d'application est attribuée à une source. Utilisez ceci pour suivre d'où viennent les installations de votre application.

```json
// Installez Attribution Event: users.behaviors. nstallAttribution
{
  "id": (string) id unique de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "source": (chaîne) la source de l'attribution
}
```

{% endapi %}

{% api %}

## Événement numéro de bucket aléatoire

{% apitags %}
Nombre aléatoire de Seaux
{% endapitags %}

Cet événement utilisateur se produit chaque fois qu'un nouvel utilisateur est créé dans son groupe d'applications. Pendant cet événement, chaque nouvel utilisateur reçoit un numéro de segment aléatoire que vous pouvez utiliser pour créer des segments uniformément répartis entre des utilisateurs aléatoires. Utilisez ceci pour regrouper une gamme de valeurs aléatoires de numéros de bucket et comparer les performances entre vos campagnes et les variantes de campagne.

```json
// Événement aléatoire de nombre de Bucket: utilisateurs. andomBucketNumberUpdate
{
  "id": (string) id unique de cet événement,
  "app_group_id": (string) AppGroup API id
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) heure UTC de l'événement en millisecondes depuis l'époque,
  "random_bucket_number": (int) nouveau numéro de segment aléatoire
  "prev_random_bucket_number": (int) ancien numéro de segment aléatoire, facultatif
}
```

{% alert important %}
Notez que cet événement courant n'est disponible que pour les clients qui ont acheté un connecteur "tous les événements" et n'est disponible que pour les connecteurs d'événements de stockage (i. Amazon S3, Microsoft Azure, Google Cloud Storage). <br><br>Pour activer cet événement et planifier le remplissage pour les numéros de seau aléatoires des utilisateurs existants dans votre groupe d'applications, contactez votre Responsable Customer Success Manager.
{% endalert %}

{% endapi %}


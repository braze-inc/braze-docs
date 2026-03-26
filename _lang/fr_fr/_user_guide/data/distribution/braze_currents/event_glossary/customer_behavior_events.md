---
nav_title: Comportement des clients et événements utilisateurs
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportements des clients et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 7
---

{% alert tip %}
Ces événements sont également disponibles sous forme de tables SQL dans le [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/), les [extensions de segments SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) et le [partage de données Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/). Pour les schémas de tables SQL et les détails des colonnes, consultez la [référence des tables SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/sql_segments/sql_segments_tables/).
{% endalert %}

Contactez votre conseiller Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [bibliothèque des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou nos [exemples d'échantillons de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure des comportements des clients et des événements utilisateur, et des valeurs de plateforme %}

### Structure d'événement

Cette ventilation des comportements des clients et des événements utilisateur montre le type d'informations généralement incluses dans un comportement client ou un événement utilisateur. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe d'aide à la décision peuvent utiliser les données d'événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des précieux indicateurs fournis.

![Décomposition d'un événement utilisateur montrant un événement d'achat avec les propriétés répertoriées regroupées par propriétés spécifiques à l'utilisateur, propriétés spécifiques au comportement et propriétés spécifiques à l'appareil]({% image_buster /assets/img/customer_engagement_event.png %})

Les comportements des clients et les événements utilisateur se composent de propriétés **propres à l'utilisateur**, de propriétés **propres au comportement** et de propriétés **propres à l'appareil**.

### Valeurs de la plateforme

Certains événements renvoient une valeur `platform` qui spécifie la plateforme de l'appareil de l'utilisateur.
<br>Le tableau suivant détaille les valeurs retournées possibles :

| Appareil de l'utilisateur | Valeur de la plateforme |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Les schémas de stockage s'appliquent aux données d'événements sous forme de fichiers plats que nous envoyons à des partenaires de stockage d'entrepôt de données (tels que Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Certaines combinaisons d'événements et de destinations énumérées ici ne sont pas encore disponibles de manière générale. Pour savoir quels événements sont pris en charge par les différents partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et leurs pages respectives.<br><br>Notez également que Currents abandonnera les événements dont la charge utile est excessivement importante (plus de 900 Ko).
{% endalert %}

{% api %}
## Événements de mise à jour du numéro de compartiment aléatoire {#random-bucket-number-update-events}

{% apitags %}
Random Bucket Number
{% endapitags %}

Cet événement utilisateur se produit chaque fois qu'un nouvel utilisateur est créé dans son espace de travail. Au cours de cet événement, chaque nouvel utilisateur se voit attribuer un numéro de compartiment aléatoire que vous pouvez ensuite utiliser pour créer des segments d'utilisateurs aléatoires uniformément répartis. Utilisez cette fonctionnalité pour regrouper une série de numéros de compartiment aléatoires et comparer les performances de vos campagnes et de leurs variantes.

{% alert important %}
Cet événement Currents n'est disponible que pour les clients qui ont acheté un « connecteur tous événements » et n'est disponible que pour les connecteurs d'événements de stockage (tels que Amazon S3, Microsoft Azure et Google Cloud Storage).
<br><br>Pour activer cet événement et planifier le remplissage des numéros de compartiment aléatoire des utilisateurs existants dans votre espace de travail, contactez votre Customer Success Manager.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.RandomBucketNumberUpdate

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "prev_random_bucket_number" : "(optional, int) Previous random bucket number",
  "random_bucket_number" : "(required, int) New random bucket number",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements personnalisés {#custom-events}

{% apitags %}
Custom Events
{% endapitags %}

Cet événement se produit lorsqu'un événement personnalisé spécifique est déclenché. Utilisez-le pour suivre les événements personnalisés effectués par les utilisateurs dans votre application.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.CustomEvent

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "name" : "(required, string) Name of the custom event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// [Braze Custom Event] (users.behaviors.CustomEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// users.behaviors.CustomEvent

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "name" : "(required, string) Name of the custom event"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Détails de la propriété

- Pour les événements personnalisés, la charge utile sera également remplie avec toutes les [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events#custom-event-properties) associées à l'événement.
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devez collecter explicitement l'IDFA iOS et l'identifiant publicitaire Google Android via les SDK natifs. Pour en savoir plus : [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), contactez votre Customer Success Manager ou votre Account Manager afin d'activer la fonctionnalité permettant l'envoi de `ad_id`.
{% endapi %}

{% api %}
## Événements d'attribution d'installation {#install-attribution-events}

{% apitags %}
Attribution
{% endapitags %}

Cet événement se produit lorsqu'une installation d'application est attribuée à une source. Utilisez-le pour identifier la provenance des installations de votre application.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.InstallAttribution

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "source" : "(required, string) The source of the attribution",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "source" : "(optional, string) The source of the attribution"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "source" : "(optional, string) The source of the attribution",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Install Attribution (users.behaviors.InstallAttribution)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "source" : "(required, string) The source of the attribution"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements de localisation {#location-events}

{% apitags %}
Locations
{% endapitags %}

Cet événement est déclenché lorsqu'un utilisateur se rend à un emplacement spécifié. Utilisez-le pour suivre les utilisateurs qui déclenchent des événements de localisation dans votre application.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.Location

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
  "altitude" : "(optional, float) [PII] Altitude of recorded location",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "latitude" : "(required, float) [PII] Latitude of recorded location",
  "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
  "longitude" : "(required, float) [PII] Longitude of recorded location",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Location (users.behaviors.Location)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Location (users.behaviors.Location)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Location (users.behaviors.Location)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "alt_accuracy" : "(optional, float) Altitude accuracy of recorded location",
    "altitude" : "(optional, float) [PII] Altitude of recorded location",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "latitude" : "(required, float) [PII] Latitude of recorded location",
    "ll_accuracy" : "(optional, float) Accuracy of the latitude and longitude of recorded location",
    "longitude" : "(required, float) [PII] Longitude of recorded location"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Détails de la propriété

- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devez collecter explicitement l'IDFA iOS et l'identifiant publicitaire Google Android via les SDK natifs. Pour en savoir plus : [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), contactez votre Customer Success Manager ou votre Account Manager afin d'activer la fonctionnalité permettant l'envoi de `ad_id`.
{% endapi %}

{% api %}
## Événements d'achat {#purchase-events}

{% apitags %}
Purchases
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur effectue un achat. Utilisez ces données pour suivre les achats réalisés dans l'application.

{% alert tip %}
Les achats sont des événements personnalisés spéciaux et sont accompagnés d'une chaîne de caractères JSON encodée de propriétés d'événement personnalisé, tout comme les événements personnalisés classiques.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.Purchase

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "currency" : "(required, string) Currency of the purchase",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "price" : "(required, float) Price of the purchase",
  "product_id" : "(required, string) ID of the product purchased",
  "properties" : "(required, string) Custom properties stored as a JSON encoded string",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Purchase (users.behaviors.Purchase)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "price" : "(required, float) Price of the purchase",
  "productId" : "(required, string) ID of the product purchased",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Purchase (users.behaviors.Purchase)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Purchased (users.behaviors.Purchase)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "currency" : "(required, string) Currency of the purchase",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "price" : "(required, float) Price of the purchase",
    "product_id" : "(required, string) ID of the product purchased"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Détails de la propriété

- Pour les événements d'achat, la charge utile sera également remplie avec toutes les [propriétés d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#purchase-properties) associées à l'événement.
- Pour `ad_id`, `ad_id_type` et `ad_tracking_enabled`, vous devez collecter explicitement l'IDFA iOS et l'identifiant publicitaire Google Android via les SDK natifs. Pour en savoir plus : [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Si vous utilisez Kafka pour ingérer des données [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), contactez votre Customer Success Manager ou votre Account Manager afin d'activer la fonctionnalité permettant l'envoi de `ad_id`.
{% endapi %}

{% api %}
## Événements de première session {#first-session-events}

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur démarre sa première session dans votre application. Utilisez ces données pour suivre le démarrage des sessions.

{% alert tip %}
Lorsqu'un utilisateur démarre sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés simultanément.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.FirstSession

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "country" : "(optional, string) [DEPRECATED]",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [DEPRECATED]",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [DEPRECATED]",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "sdk_version" : "(optional, string) [DEPRECATED]",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// First Session (users.behaviors.app.FirstSession)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements de fin de session {#session-end-events}

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur quitte votre application, mettant ainsi fin à sa session en cours. Utilisez ces données pour suivre les fins de session et, en les combinant avec l'événement de début de session correspondant, calculer la durée passée dans une session.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionEnd

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "duration" : "(optional, float) Duration of the session in seconds",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "duration" : "(optional, float) Duration of the session in seconds",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Session End (users.behaviors.app.SessionEnd)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "duration" : "(optional, float) Duration of the session in seconds",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Ended (users.behaviors.app.SessionEnd)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "duration" : "(optional, float) Duration of the session in seconds",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements de début de session {#session-start-events}

{% apitags %}
Sessions
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur démarre une session. Utilisez ces données pour suivre le démarrage des sessions.

{% alert tip %}
Lorsqu'un utilisateur démarre sa première session, un événement `FirstSession` et un événement `SessionStart` sont déclenchés simultanément.
{% endalert %}

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.app.SessionStart

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "session_id" : "(required, string) UUID of the session",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_model" : "(optional, string) Model of the device",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Session Start (users.behaviors.app.SessionStart)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "session_id" : "(optional, string) UUID of the session",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Session Started (users.behaviors.app.SessionStart)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "session_id" : "(required, string) UUID of the session"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements de changement de jeton Push To Start pour les Live Activity {#live-activity-push-to-start-token-change-events}

{% apitags %}
Live Activity, Push To Start Token
{% endapitags %}

Cet événement se produit lorsque Braze synchronise le jeton Push To Start de la Live Activity avec l'utilisateur.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.PushToStartTokenChange

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Push To Start Token Change (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Push To Start Token Changed (users.behaviors.liveactivity.PushToStartTokenChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements de changement de jeton de mise à jour des Live Activity {#live-activity-update-token-change-events}

{% apitags %}
Live Activity, Update Token
{% endapitags %}

Cet événement se produit lorsque Braze synchronise le jeton de mise à jour de la Live Activity avec l'utilisateur.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.liveactivity.UpdateTokenChange

{
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Update Token Change (users.behaviors.liveactivity.UpdateTokenChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Update Token Changed (users.behaviors.liveactivity.UpdateTokenChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Événements de modification de l'état du jeton de notification push {#push-notification-token-state-change-events}

{% apitags %}
Push, Token State Change
{% endapitags %}

Cet événement se produit lorsqu'un jeton de notification push est inséré, mis à jour ou supprimé. Utilisez-le pour suivre l'état des jetons de notification push.

{% tabs %}
{% tab Cloud Storage %}
```json
// users.behaviors.pushnotification.TokenStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
  "platform" : "(optional, string) Platform of the device",
  "push_token" : "(optional, string) Push token of the event",
  "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
  "push_token_device_id" : "(optional, string) Device id of the push token",
  "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
  "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
  "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
  "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "time_ms" : "(optional, long) Time in millisecond when the event happened",
  "user_id" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
  "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
  "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
}
```
{% endtab %}

{% tab Amplitude %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in millisecond when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Token State Change (users.behaviors.pushnotification.TokenStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "platform" : "(optional, string) Platform of the device",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "time_ms" : "(optional, long) Time in millisecond when the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Token State Changed (users.behaviors.pushnotification.TokenStateChange)

{
  "anonymousId" : "(required, string) [PII] Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "ios_push_token_apns_gateway" : "(optional, int) APNS gateway of the push token, only applies to iOS push tokens, 1 for development, 2 for production",
    "push_token" : "(optional, string) Push token of the event",
    "push_token_created_at" : "(optional, int) UNIX timestamp at which the push token was created",
    "push_token_device_id" : "(optional, string) Device id of the push token",
    "push_token_foreground_push_disabled" : "(optional, boolean) Foreground push disabled flag of the push token",
    "push_token_provisionally_opted_in" : "(optional, boolean) Provisionally opted in flag of the push token",
    "push_token_state_change_type" : "(optional, string) A description of the push token state change type",
    "push_token_updated_at" : "(optional, int) UNIX timestamp at which the push token was last updated",
    "time_ms" : "(optional, long) Time in millisecond when the event happened",
    "web_push_token_public_key" : "(optional, string) Public key of the push token, only applies to web push tokens",
    "web_push_token_user_auth" : "(optional, string) User auth of the push token, only applies to web push tokens",
    "web_push_token_vapid_public_key" : "(optional, string) VAPID public key of the push token, only applies to web push tokens"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}
{% endtabs %}

#### Détails de la propriété

- Le champ `push_token_foreground_push_disabled` indique si le jeton de notification push peut recevoir des notifications push en avant-plan ou en arrière-plan.
  - Si l'utilisateur a explicitement autorisé les notifications push sur son appareil, la valeur sera `false`, et le jeton pourra recevoir des notifications push en avant-plan.
  - Si l'utilisateur a explicitement refusé l'autorisation de notification push sur son appareil, la valeur sera `true`, et le jeton ne pourra recevoir que des notifications push en arrière-plan.
  - Si l'autorisation push est inconnue, ce champ sera vide. Par défaut, Braze tentera d'envoyer des notifications push en avant-plan au jeton.
- Le champ `push_token_provisionally_opted_in` s'applique uniquement aux jetons de notification push iOS.
  - Si vous avez configuré l'[autorisation provisoire]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#provisional-push), ce champ sera défini sur `true` pour les jetons provisoires. Tous les autres jetons de notification push auront la valeur `false`.
- Le champ `sdk_version` ne sera rempli que si le changement d'état du jeton est initié par le SDK.
  - Si un événement SDK `changeUser` déclenche le transfert du jeton d'un utilisateur à un autre, le champ `sdk_version` sera rempli.
  - En cas de rebond push (par exemple, suite à une désinstallation), le champ `sdk_version` restera vide.
- Chaque fois qu'un jeton de notification push entre dans Braze, les événements de son cycle de vie sont enregistrés. Trois types d'événements de modification de jeton (« add », « update » et « remove ») sont enregistrés dans le champ `push_token_state_change_type`.

#### Types d'événements

##### Add

Un événement « add » est ingéré lorsqu'un nouveau jeton est enregistré. Cela se produit lorsqu'un utilisateur ouvre l'application pour la première fois sur un nouvel appareil, ou lorsqu'un jeton est défini via l'endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) avec `push_tokens` pour un utilisateur qui n'en avait pas auparavant.

##### Update

Un événement « update » est ingéré lorsqu'une propriété d'un jeton existant est modifiée sans que la chaîne de caractères du jeton elle-même ne change. Le jeton conserve la même chaîne de caractères, le même utilisateur et la même application, mais un ou plusieurs des champs suivants ont été modifiés : `foreground_push_disabled`, passerelle APNs, clés de notification push web, `provisionally_opted_in` ou `device_id`.

{% alert note %}
Dans la plupart des cas, la réinstallation d'une application ou la restauration d'une sauvegarde entraîne un nouvel événement « add » avec un nouveau `push_token` et un nouveau `device_id` (car le SDK génère un nouveau `device_id` et le système d'exploitation fournit une nouvelle chaîne de caractères de jeton de notification push). Cela crée deux entrées distinctes pour le jeton et l'appareil dans le profil utilisateur, et l'entrée la plus ancienne est supprimée ultérieurement via le suivi des désinstallations ou l'envoi de campagnes.

Il serait extrêmement rare que seul le `device_id` change sans que le `push_token` ne change (cela nécessiterait que le système d'exploitation renvoie la même chaîne de caractères après la réinstallation).
{% endalert %}

##### Remove

Un événement « remove » autonome est ingéré lorsque Braze supprime un jeton. Cela peut se produire pour plusieurs raisons :

- Rebond de notification push (APNs, FCM ou HMS signale le jeton comme non valide ou expiré)
- Détection de désinstallation via une notification push silencieuse
- Jeton supprimé via l'API REST ou le service de retour APNs

##### Paires add et remove

Les paires add et remove se répartissent en deux catégories :

**Actualisation de la chaîne de caractères du jeton (même utilisateur) :** Le système d'exploitation procède à la rotation de la chaîne de caractères du jeton sur le même appareil (par exemple, rotation des jetons APNs ou FCM). Les événements « add » (nouveau jeton) et « remove » (ancien jeton) ont les mêmes `user_id` et `device_id`, des `push_token` différents et des `time_ms` identiques.

**Transfert de jeton entre utilisateurs :** Un jeton passe d'un utilisateur à un autre. Les événements « add » (nouvel utilisateur) et « remove » (ancien utilisateur) ont des `user_id` différents, le même `device_id`, le même `push_token` et des `time_ms` différents (généralement moins de 100 millisecondes d'écart). Cela est déclenché par l'un des cas suivants :

- Le SDK appelle `changeUser` d'un profil anonyme vers un profil identifié. L'événement « remove » aura un `external_user_id` vide.
- Le SDK appelle `changeUser` d'un profil identifié à un autre. Les deux événements auront un `external_user_id` non vide.
- L'endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) ou le nettoyage des utilisateurs en double transfère les jetons de l'utilisateur orphelin vers l'utilisateur conservé.

{% alert note %}
Si un profil anonyme est identifié via l'endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), le `user_id` ne change pas et aucun événement de modification de l'état du jeton n'est émis.
{% endalert %}

#### Requête sur l'état actuel du jeton actif

Pour déterminer l'état actuel du jeton de notification push de chaque utilisateur, partitionnez les événements de changement d'état du jeton par `push_token`, `user_id` et `app_id`, puis ordonnez-les par `time_ms` décroissant et filtrez les événements « remove ». En interne, un jeton est identifié par sa chaîne de caractères et son `app_id` par utilisateur. Il n'est pas recommandé d'utiliser `device_id` comme clé de partition, car `device_id` est un attribut modifiable et le partitionnement selon cette clé pourrait diviser le cycle de vie d'un jeton unique entre plusieurs partitions.

La requête SQL suivante renvoie le dernier état actif du jeton par utilisateur dans Snowflake :

```sql
WITH latest_token_state AS (
  SELECT *,
    ROW_NUMBER() OVER (
      PARTITION BY PUSH_TOKEN, USER_ID, APP_ID
      ORDER BY COALESCE(TIME_MS, TIME * 1000) DESC
    ) AS rn
  FROM USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE
)
SELECT
  PUSH_TOKEN, USER_ID, EXTERNAL_USER_ID, PUSH_TOKEN_DEVICE_ID,
  PUSH_TOKEN_STATE_CHANGE_TYPE, PUSH_TOKEN_FOREGROUND_PUSH_DISABLED,
  TIME_MS, PLATFORM, APP_ID
FROM latest_token_state
WHERE rn = 1
  AND PUSH_TOKEN_STATE_CHANGE_TYPE != 'remove';
```

{% endapi %}
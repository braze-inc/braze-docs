---
nav_title: "POST : Exportation de profil utilisateur par segment"
article_title: "POST : Exportation de profil utilisateur par segment"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Utilisateurs par segment."

---
{% api %}
# Endpoint Utilisateurs par segment
{% apimethod post %}
/users/export/segment
{% endapimethod %}

Utilisez cet endpoint pour exporter tous les utilisateurs d’un segment. Les données utilisateur sont exportées sous forme de fichiers multiples d’objets utilisateur JSON séparés par de nouvelles lignes (c.-à-d. un objet JSON par ligne). 

Les données sont exportées vers une URL générée automatiquement ou vers un compartiment S3 si cette intégration est déjà configurée.

Cet endpoint n’est actuellement pas pris en charge par Google Cloud Storage.

Notez qu’une entreprise peut exécuter au maximum une exportation par segment à l’aide de cet endpoint à un moment donné. Attendez que votre exportation soit terminée avant de réessayer. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

{% alert important %}
En décembre 2021, les modifications suivantes ont été apportées à cette API :<br><br>1. Le champ `fields_to_export` dans cette demande API est **requis**. L’option par défaut sur Tous les champs a été supprimée.<br>2. Les champs pour `custom_events`, `purchases`, `campaigns_received`, et `canvases_received` contiennent uniquement les données des 90 derniers jours.
{% endalert %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Informations relatives à la réponse basée sur les informations d’identification

Si vous avez ajouté vos informations d’identification [S3][1] ou [Azure][2] à Braze, chaque fichier sera téléchargé dans votre compartiment en tant que fichier ZIP avec le format de clé qui ressemble à `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Si vous utilisez Azure, assurez-vous que la case **Faire de cette option la destination d’exportation des données par défaut** est cochée sur la page d’aperçu du partenaire Azure dans Braze. Nous allons généralement créer 1 fichier pour 5 000 utilisateurs pour optimiser le traitement. L’exportation de segments plus petits au sein d’un grand groupe d’apps peut entraîner la création de plusieurs fichiers. Vous pouvez alors décompresser les fichiers et concaténer tous les fichiers `json` dans un fichier unique si nécessaire. Si vous spécifiez un `output_format` de `gzip`, l’extension de fichier sera `.gz` au lieu de `.zip`.

{% details Répartition du chemin d’exportation du fichier ZIP %}
Format de fichier ZIP :
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

Exemple de fichier ZIP :
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Propriété | Informations | Illustré dans l’exemple comme... |
|---|---|
| `bucket-name` | Résolu en fonction du nom de votre compartiment. | `braze.docs.bucket`
| `segment-export` | Résolu. | `segment-export`
| `SEGMENT_ID` | Inclus dans la demande d’exportation. | `abc56c0c-rd4a-pb0a-870pdf4db07q`
| `YYYY-MM-dd` | Date à laquelle la fonction de rappel réussi est reçue. | `2019-04-25`
| `RANDOM_UUID` | Un UUID aléatoire généré par Braze au moment de la demande. | `d9696570-dfb7-45ae-baa2-25e302r2da27`
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Heure Unix (secondes depuis 2017-01-01:00:00:00Z) à laquelle l'exportation a été demandée. | `1556044807`
| `filename` | Aléatoire par fichier. | `114f0226319130e1a4770f2602b5639a`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% enddetails %}

Nous suggérons vivement aux clients qui utilisent cet endpoint de configurer leurs propres informations d’identification S3 ou Azure afin que les clients puissent appliquer leurs propres politiques de compartiment sur l’exportation. Si vous n’avez pas indiqué vos informations d’identification pour votre stockage cloud, la réponse à la demande fournit l’URL sur laquelle un fichier ZIP contenant tous les fichiers utilisateur peut être téléchargé. L’URL ne deviendra valide qu’une fois l’exportation prête. 

Sachez que si vous ne fournissez pas vos informations d’identification pour votre stockage cloud, il existe une limitation de la quantité de données que vous pouvez exporter à partir de cet endpoint. En fonction des champs que vous exportez et du nombre d’utilisateurs, le transfert de fichiers peut échouer si la demande est trop importante. Une meilleure pratique consiste à spécifier les champs que vous souhaitez exporter à l'aide de ‘fields_to_export' et à ne préciser que les champs dont vous avez besoin afin de réduire la taille du transfert. Si vous obtenez des erreurs en générant le fichier, envisagez de diviser votre base d’utilisateurs en plus de segments en fonction d’un numéro de compartiment aléatoire (par ex. créer un segment où le numéro de compartiment aléatoire est <1000, entre 1000 et 2000, etc.).

Dans l’un ou l’autre scénario, vous pouvez éventuellement fournir un `callback_endpoint` à notifier lorsque l’exportation est prête. Si le `callback_endpoint` est fourni, nous ferons une demande Post à l’adresse indiquée lorsque le téléchargement sera prêt. Le corps du Post sera "success":true. Si vous n’avez pas ajouté d’informations d’identification S3 à Braze, le corps du Post contiendra également l’attribut `url` avec l’URL de téléchargement comme valeur.

Les bases d’utilisateurs plus grandes entraîneront des temps d’exportation plus longs. Par exemple, une application avec 20 millions d’utilisateurs peut prendre une heure ou plus.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifiant du segment à exporter,
  "callback_endpoint" : (optional, string) endpoint auquel publier une URL de téléchargement lorsque l’exportation est disponible.,
  "fields_to_export" : (required, array of string) nom des champs de données utilisateur à exporter. Vous pouvez également exporter des attributs personnalisés. *À partir d’avril 2021, les nouveaux comptes doivent préciser des champs spécifiques à exporter.
  "output_format" : (optional, string) spécifie un format de fichier comme étant « zip » ou « gzip » lorsque vous utilisez votre propre compartiment S3. Le format de fichier ZIP est défini par défaut
}
```

{% alert warning %}
Les attributs personnalisés individuels ne peuvent pas être exportés. Cependant, tous les attributs personnalisés peuvent être exportés en incluant `custom_attributes` dans l’array `fields_to_export` (p. ex., [« first_name », « e-mail », « custom_attributes »]).
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
|`segment_id` | Requis | String | Identifiant du segment à exporter. Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/).<br><br>Le `segment_id` pour un segment donné se trouve dans votre **Console du développeur** sur votre compte Braze, sinon vous pouvez utiliser l'[endpoint Liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).|
|`callback_endpoint` | Facultatif | String | Endpoint auquel publier une URL de téléchargement lorsque l’exportation est disponible. |
|`fields_to_export` | Requis* | Array of Strings | Nom des champs de données utilisateur à exporter. Vous pouvez également exporter des attributs personnalisés. <br><br>*À partir d’avril 2021, les nouveaux comptes doivent préciser des champs spécifiques à exporter. |
|`output_format` | Facultatif | String | Le format de sortie de votre fichier. Format de fichier `zip` par défaut. Si vous utilisez votre propre compartiment S3, vous pouvez spécifier `zip` ou `gzip`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "output_format" : "code postal"
}'
```

## Champs à exporter

Voici une liste des `fields_to_export` valides. Utiliser `fields_to_export` pour minimiser les données renvoyées peut améliorer le temps de réponse de cet endpoint d’API :

| Champ à exporter | Type de données | Description |
|---|---|---|
| `apps` | Tableau | Les applications pour lesquelles l’utilisateur a enregistré des sessions ce qui comprend les champs :<br><br>- `name`: noms de l'application<br>- `platform`: plateforme de l'application comme iOS, Android ou Web<br>- `version`: numéro ou nom de version de l'application <br>- `sessions`: nombre total de sessions pour cette application<br>- `first_used`: date de la première session<br>- `last_used`: date de la dernière session<br><br>Tous les champs sont des chaînes de caractères. |
| `attributed_campaign` | String | Données des [intégrations d’attribution]({{site.baseurl}}/partners/message_orchestration/attribution) si définies. Identifiant d’une campagne donnée. |
| `attributed_source` | String | Données des [intégrations d’attribution]({{site.baseurl}}<br>/partners/message_orchestration/attribution<br>), si définies. Identifiant de la plateforme sur laquelle était l’annonce. |
| `attributed_adgroup` | String | Données des [intégrations d’attribution]({{site.baseurl}}<br>/partners/message_orchestration/attribution<br>), si définies. Identifiant pour un sous-groupe optionnel sous la campagne. |
| `attributed_ad` | String | Données des [intégrations d’attribution]({{site.baseurl}}<br>/partners/message_orchestration/attribution<br>), si définies. Identifiant pour un sous-groupe optionnel sous la campagne et le groupe d’annonce. |
| `braze_id` | String | Identifiant utilisateur unique spécifique à l’appareil défini par Braze pour cet utilisateur. |
| `country` | String | Pays de l’utilisateur en utilisant la norme [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| `created_at` | String | Date et heure de la création du profil utilisateur au format ISO 8601. |
| `custom_attributes` | Objet | Paires clé-valeur de l’attribut personnalisé de cet utilisateur. |
| `custom_events` | Tableau | Événements personnalisés attribués à cet utilisateur dans les derniers 90 jours. |
| `devices` | Tableau | Informations sur l’appareil de l’utilisateur qui devraient contenir les éléments suivants selon la plateforme :<br><br>- `model` : Nom du modèle de l'appareil<br>- `os` : Système d'exploitation de l'appareil<br>- `carrier` : Fournisseur de services de l'appareil, si disponible<br>- `idfv` : (iOS) Identifiant de l'appareil Braze, l'identifiant Apple pour le vendeur<br>- `idfa` : (iOS) Identifiant publicitaire, s'il existe<br>- `device_id` : (Android) Identifiant de l'appareil Braze<br>- `google_ad_id` : (Android) Identifiant publicitaire Google Play, s'il existe<br>- `roku_ad_id` : (Roku) Identifiant publicitaire Roku<br>- `ad_tracking_enabled` : Si le suivi des annonces est activé sur l'appareil, peut être True ou False |
| `dob` | String | Date de naissance de l'utilisateur au format `YYYY-MM-DD`. |
| `email` | String | Adresse e-mail de l’utilisateur. |
| `external_id` | String | Identifiant utilisateur unique pour les utilisateurs identifiés. |
| `first_name` | String | Prénom de l’utilisateur. |
| `gender` | String | Genre de l’utilisateur. Les valeurs possibles sont :<br><br>- `M`: masculin<br>- `F`: féminin<br>- `O`: autre<br>- `N`: sans objet<br>- `P`: préfère ne pas répondre<br>- `nil`: inconnu |
| `home_city` | String | Ville de résidence de l’utilisateur. |
| `language` | String | Langue de l’utilisateur à la norme ISO-639-1. |
| `last_coordinates` | Tableau de floats | Dernier emplacement de l'appareil de l'utilisateur, formaté en `[longitude, latitude]`. |
| `last_name` | String | Nom de famille de l’utilisateur. |
| `phone` | String | Numéro de téléphone de l’utilisateur au format E.164. |
| `purchase`s | Tableau | Achats réalisés par cet utilisateur au cours de 90 derniers jours. |
| `random_bucket` | Integer | [Numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) de l’utilisateur, utilisé pour créer des segments distribués uniformément d’utilisateurs aléatoires. |
| `time_zone` | String | Fuseau horaire de l’utilisateur au même format que la base de données de fuseaux horaires IANA. |
| `total_revenue` | Float | Revenus totaux attribués à cet utilisateur. Les revenus totaux sont calculés à partir des achats réalisés par l’utilisateur pendant la fenêtre de conversion pour les campagnes et les Canvas qu’il a reçu. |
| `uninstalled_at` | Horodatage | Date et heure de désinstallation de l’application par l’utilisateur. Absent si l’application n’a pas été désinstallée. |
| `user_aliases` | Objet | [Objet d’alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) contenant le `alias_name` et le `alias_label` s’ils existent. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Rappels importants

- Les champs pour `custom_events`, `purchases`, `campaigns_received`, et `canvases_received` contiennent uniquement les données des 90 derniers jours.
- `custom_events` et `purchases` contiennent tous les deux des champs pour `first` et `count`. Ces deux champs reflèteront les informations de tout le temps et ne seront pas limités aux données des 90 derniers jours. Par exemple, si un utilisateur particulier a effectué l’événement pour la première fois il y a plus de 90 jours, cela sera reflété avec précision dans le champ `first` et le champ `count` tiendra compte des événements qui ont eu lieu avant les 90 derniers jours également.
- Le nombre d’exportations de segments simultanées qu’une entreprise peut exécuter au niveau de l’endpoint est plafonné à 100. Les tentatives qui dépassent cette limite entraîneront une erreur.

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur,
    "object_prefix": (required, string) le préfixe du nom de fichier qui sera utilisé pour le fichier JSON produit par cette exportation, par ex., « bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599 »,
    "url" : (optional, string) l’URL où les données d’exportation du segment peuvent être téléchargées si vous n’avez pas vos propres informations d’identification S3
}
```

Une fois disponible, l’URL ne sera valide que quelques heures. Par conséquent, nous vous recommandons fortement d’ajouter vos propres informations d’identification S3 dans Braze.

## Exemple de sortie de fichier d’exportation utilisateur

Objet d’exportation utilisateur (nous inclurons le moins de données possible. S’il manque un champ de l’objet, il doit être considéré comme nul, faux ou vide) :

{% tabs %}
{% tab Tous les champs %}

```json
{
    "created_at": (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date de naissance de l’utilisateur,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "inscrit" | "désinscrit",
    "email_subscribe" : (string) "opted_in" | "inscrit" | "désinscrit",
    "custom_attributes" : (object) attribut personnalisé paires clé-valeur,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) inclus uniquement pour les appareils iOS lorsque le recueil d’IDFV est activé,
        "idfa" : (string) inclus uniquement pour les appareils iOS lorsque le recueil d’IDFA est activé,
        "google_ad_id" : (string) inclus uniquement pour les appareils Android lorsque le recueil d’identifiants publicitaires Google Play est activé,
        "roku_ad_id" : (string) inclus uniquement pour mes appareils Roku,
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) noms de l’application,
        "platform" : (string),
        "token" : (string)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" : 
         {
           "opened_email" : (bool),
           "opened_push" : (bool),
           "clicked_email" : (bool),
           "clicked_triggered_in_app_message" : (bool)
          },
          "converted" : (bool),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) n’existe que si la campagne est multivariée,
          "variation_api_id" : (optional, string) n’existe que si la campagne est multivariée,
          "in_control" : (optional, bool) n’existe que si la campagne est multivariée
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (bool),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
}
```

{% endtab %}
{% tab Exemple de sortie %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Heure de l’Est (États-Unis et Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in", 
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "abonné",
    "custom_attributes": 
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Remerciement de fidélité",
        "first": "2021-06-28T17:02:43.032Z",
        "last": "2021-06-28T17:02:43.032Z",
        "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
    "campaigns_received": [
      {
        "name": "Désinscription des e-mails",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged": 
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted": 
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variante 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Groupe litigieux non mondial 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variante 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Étape",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Promo. fidélité"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et de l'API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/

{% endapi %}

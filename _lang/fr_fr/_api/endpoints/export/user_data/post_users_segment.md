---
nav_title: "POST : Exporter le profil utilisateur par segmentation"
article_title: "POST : Exporter le profil utilisateur par segmentation"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les utilisateurs par segment."

---
{% api %}
# Exporter le profil utilisateur par segment
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> Utilisez cet endpoint pour exporter tous les utilisateurs d’un segment. 

{% alert important %}
Lors de l'utilisation de cet endpoint, notez les points suivants :<br><br>1\. Le champ `fields_to_export` de cette demande d'API est **obligatoire**.<br>2\. Les champs pour `custom_events`, `purchases`, `campaigns_received`, et `canvases_received` contiennent uniquement les données des 90 derniers jours.
{% endalert %}

Les données des utilisateurs sont exportées sous la forme de plusieurs fichiers d'objets JSON d'utilisateurs séparés par de nouvelles lignes (par exemple, un objet JSON par ligne). Les données sont exportées vers une URL générée automatiquement ou vers un compartiment S3 si cette intégration est déjà configurée.

Notez qu’une entreprise peut exécuter au maximum une exportation par segment à l’aide de cet endpoint à un moment donné. Attendez la fin de l'exportation avant de réessayer. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `users.export.segment`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Informations relatives à la réponse basée sur les informations d’identification

Si vous avez ajouté vos identifiants [S3][1], [Azure][2] ou [Google cloud storage][3] à Braze, alors chaque fichier sera téléchargé dans votre compartiment S3 sous la forme d'un fichier ZIP dont le format de clé ressemble à `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Si vous utilisez Azure, assurez-vous que la case **Faire de cette destination la destination par défaut de l'exportation de données est** cochée dans la page d'aperçu du partenaire Azure dans Braze. Nous allons généralement créer 1 fichier pour 5 000 utilisateurs pour optimiser le traitement. L'exportation de segments plus petits au sein d'un grand espace de travail peut donner lieu à plusieurs fichiers. Vous pouvez alors décompresser les fichiers et concaténer tous les fichiers `json` dans un fichier unique si nécessaire. Si vous spécifiez un `output_format` de `gzip`, l’extension de fichier sera `.gz` au lieu de `.zip`.

{% details Exportation de la répartition des chemins pour ZIP %}
**Format ZIP :**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**Exemple ZIP :**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Propriété                        | Détails                                                                              | Montré dans l'exemple comme                    |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| `bucket-name`                   | Résolu en fonction du nom de votre compartiment.                                                     | `braze.docs.bucket`                    |
| `segment-export`                | Résolu.                                                                               | `segment-export`                       |
| `SEGMENT_ID`                    | Inclus dans la demande d’exportation.                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | Date à laquelle la fonction de rappel réussi est reçue.                                        | `2019-04-25`                           |
| `RANDOM_UUID`                   | Un UUID aléatoire généré par Braze au moment de la demande.                         | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Heure Unix (secondes depuis 2017-01-01:00:00:00Z) à laquelle l'exportation a été demandée en UTC. | `1556044807`                           |
| `filename`                      | Aléatoire par fichier.                                                                     | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

Nous vous conseillons vivement de configurer vos propres identifiants S3 ou Azure lorsque vous utilisez cet endpoint afin d'appliquer vos propres politiques de compartiment sur l'exportation. Si vous n'avez pas vos identifiants de stockage en nuage, la réponse à la demande fournit l'URL où un fichier ZIP contenant tous les fichiers de l'utilisateur peut être téléchargé. L'URL ne deviendra un emplacement/localisation valide qu'une fois l'exportation prête. 

Sachez que si vous ne fournissez pas vos identifiants de stockage dans le cloud, la quantité de données que vous pouvez exporter depuis cet endpoint est limitée. En fonction des champs que vous exportez et du nombre d’utilisateurs, le transfert de fichiers peut échouer si la quantité de données demandées est trop importante. Une bonne pratique consiste à spécifier les champs que vous souhaitez exporter à l’aide de `fields_to_export` et à ne préciser que les champs dont vous avez besoin afin de réduire la taille du transfert. Si vous obtenez des erreurs lors de la génération du fichier, envisagez de diviser votre base d'utilisateurs en plusieurs segments sur la base d'un numéro de compartiment aléatoire (par exemple, créez un segment dans lequel le numéro de compartiment aléatoire est inférieur à 1 000 ou compris entre 1 000 et 2 000).

Dans l’un ou l’autre scénario, vous pouvez éventuellement fournir un `callback_endpoint` à notifier lorsque l’exportation est prête. Si le `callback_endpoint` est fourni, nous ferons une demande Post à l’adresse indiquée lorsque le téléchargement sera prêt. Le corps du Post sera "success":true. Si vous n’avez pas ajouté d’informations d’identification S3 à Braze, le corps du Post contiendra également l’attribut `url` avec l’URL de téléchargement comme valeur.

Les bases d’utilisateurs plus grandes entraîneront des temps d’exportation plus longs. Par exemple, une application avec 20 millions d’utilisateurs peut prendre une heure ou plus.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## Paramètres de demande

| Paramètre                     | Requis  | Type de données        | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `segment_id`                  | Requis  | Chaîne de caractères           | Identifiant du segment à exporter. Voir [identifiant de segmentation]({{site.baseurl}}/api/identifier_types/).<br><br>Vous trouverez le site `segment_id` pour un segment donné sur la page des [clés API de]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) votre compte Braze ou vous pouvez utiliser l'[endpoint de la liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). |
| `callback_endpoint`           | Facultatif  | Chaîne de caractères           | Endpoint auquel publier une URL de téléchargement lorsque l’exportation est disponible.                                                                                                                                                                                                                                                                                                                                             |
| `fields_to_export`            | Obligatoire* | Tableau de chaînes de caractères | Nom des champs de données utilisateur à exporter. Vous pouvez également exporter tous les attributs personnalisés en incluant `custom_attributes` dans ce paramètre. <br><br>\*À partir d’avril 2021, les nouveaux comptes doivent préciser des champs spécifiques à exporter.                                                                                                                                                                                        |
| `custom_attributes_to_export` | Facultatif  | Tableau de chaînes de caractères | Nom de l'attribut personnalisé spécifique à exporter. Il est possible d'exporter jusqu'à 500 attributs personnalisés. Pour créer et gérer des attributs personnalisés dans le tableau de bord, allez dans **Paramètres des données** > Attributs personnalisés.                                                                                                                                                                                                          |
| `output_format`               | Facultatif  | Chaîne de caractères           | Le format de sortie de votre fichier. Format de fichier `zip` par défaut. Si vous utilisez votre propre compartiment S3, vous pouvez spécifier `zip` ou `gzip`.                                                                                                                                                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Si `custom_attributes` est inclus dans le paramètre `fields_to_export`, tous les attributs personnalisés sont exportés, quel que soit le contenu de `custom_attributes_to_export`. Si votre objectif est d’exporter des attributs spécifiques, `custom_attributes` ne doit pas être inclus dans le paramètre `fields_to_export`. Utilisez plutôt le paramètre `custom_attributes_to_export`.
{% endalert %}

## Exemple de demande d'exportation de tous les attributs personnalisés
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## Exemple de demande d'exportation d'attributs personnalisés spécifiques
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
  "output_format" : "zip"
}'
```

## Champs à exporter

Voici une liste des `fields_to_export` valides. L'utilisation de `fields_to_export` pour minimiser les données renvoyées peut améliorer le temps de réponse de ce point de terminaison de l'API :

| Champ à exporter       | Type de données       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | Tableau           | Les applications pour lesquelles l’utilisateur a enregistré des sessions, ce qui comprend les champs :<br><br>- `name` : nom de l’application<br>- `platform` : plateforme de l’application telle qu’iOS, Android ou Web<br>- `version` : numéro ou nom de version de l’application <br>- `sessions` : nombre total de sessions pour cette application<br>- `first_used` : date de la première session<br>- `last_used` : date de la dernière session<br><br>Tous les champs sont des chaînes de caractères.                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | Chaîne de caractères          | Données provenant des [intégrations d'attribution]({{site.baseurl}}/partners/message_orchestration/), si elles sont configurées. Identifiant d’une campagne donnée.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | Chaîne de caractères          | Données provenant des [intégrations d'attribution]({{site.baseurl}}/partners/message_orchestration/), si elles sont configurées. Identifiant de la plateforme sur laquelle était l’annonce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | Chaîne de caractères          | Données provenant des [intégrations d'attribution]({{site.baseurl}}/partners/message_orchestration/), si elles sont configurées. Identifiant pour un sous-groupe optionnel sous la campagne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | Chaîne de caractères          | Données provenant des [intégrations d'attribution]({{site.baseurl}}/partners/message_orchestration/), si elles sont configurées. Identifiant d'un sous-groupement facultatif en dessous de la campagne et du groupe d'annonces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `push_subscribe`      | Chaîne de caractères          | Statut de l'abonnement push de l'utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | Chaîne de caractères          | Statut de l'abonnement à l'e-mail de l'utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `braze_id`            | Chaîne de caractères          | Identifiant utilisateur unique spécifique à l’appareil défini par Braze pour cet utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | Chaîne de caractères          | Pays de l'utilisateur selon la norme [ISO 3166-1 alpha-2.](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `created_at`          | Chaîne de caractères          | Date et heure de la création du profil utilisateur au format ISO 8601.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | Objet          | Paires clé-valeur de l’attribut personnalisé de cet utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | Tableau           | Événements personnalisés attribués à cet utilisateur dans les 90 derniers jours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | Tableau           | Informations sur l’appareil de l’utilisateur qui devraient contenir les éléments suivants selon la plateforme :<br><br>- `model` : Nom du modèle de l’appareil<br>- `os` : Système d’exploitation de l’appareil<br>- `carrier` : Fournisseur de services de l’appareil, si disponible<br>- `idfv`: (iOS) Identifiant de l'appareil Braze, l'identifiant Apple pour le vendeur, s'il existe.<br>- `idfa` : (iOS) Identifiant publicitaire, s’il existe<br>- `device_id` : (Android) Identifiant de l’appareil Braze<br>- `google_ad_id` : (Android) Identifiant publicitaire Google Play, s’il existe<br>- `roku_ad_id` : (Roku) Identifiant publicitaire Roku<br>- `ad_tracking_enabled` : Si le suivi des annonces est activé sur l’appareil, peut être vrai ou faux |
| `dob`                 | Chaîne de caractères          | Date de naissance de l’utilisateur au format `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | Chaîne de caractères          | Adresse e-mail de l’utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | Chaîne de caractères          | Identifiant utilisateur unique pour les utilisateurs identifiés.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | Chaîne de caractères          | Prénom de l’utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | Chaîne de caractères          | Genre de l’utilisateur. Les valeurs possibles sont :<br><br>- `M` : masculin<br>- `F` : féminin<br>- `O` : autre<br>- `N` : sans objet<br>- `P` : préfère ne pas répondre<br>- `nil` : inconnu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | Chaîne de caractères          | Ville de résidence de l’utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | Chaîne de caractères          | Langue de l’utilisateur à la norme ISO-639-1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | Tableau de floats | Dernier emplacement de l’appareil de l’utilisateur, au format `[longitude, latitude]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | Chaîne de caractères          | Nom de famille de l’utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | Chaîne de caractères          | Numéro de téléphone de l'utilisateur au format E.164.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchases`           | Tableau           | Achats réalisés par cet utilisateur au cours des 90 derniers jours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | Tableau           | Informations sur les jetons de poussée de l'utilisateur.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `random_bucket`       | Entier         | [Numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) de l'utilisateur, utilisé pour créer des segments uniformément distribués d'utilisateurs aléatoires.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | Chaîne de caractères          | Fuseau horaire de l’utilisateur au même format que la base de données de fuseaux horaires IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | Revenus totaux attribués à cet utilisateur. Les revenus totaux sont calculés à partir des achats réalisés par l’utilisateur pendant la fenêtre de conversion pour les campagnes et les Canvas qu’il a reçus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Date/heure       | Date et heure de désinstallation de l’application par l’utilisateur. Absent si l’application n’a pas été désinstallée.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objet          | [Objet aliasing de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) contenant les adresses `alias_name` et `alias_label`, si elles existent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rappels importants

- Les champs pour `custom_events`, `purchases`, `campaigns_received`, et `canvases_received` contiennent uniquement les données des 90 derniers jours.
- `custom_events` et `purchases` contiennent tous les deux des champs pour `first` et `count`. Ces deux champs reflèteront les informations de tout le temps et ne seront pas limités aux données des 90 derniers jours. Par exemple, si un utilisateur particulier a effectué l'événement pour la première fois il y a 90 jours, cela sera reflété avec précision dans le champ `first`, et le champ `count` prendra également en compte les événements qui se sont produits avant les 90 derniers jours.
- Le nombre d’exportations de segments simultanées qu’une entreprise peut exécuter au niveau de l’endpoint est plafonné à 100. Les tentatives qui dépassent cette limite entraîneront une erreur.
- Si vous tentez d’exporter un segment une deuxième fois alors que la première tâche d’exportation est toujours en cours d’exécution, une erreur 429 s’affiche.

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Après la mise à disposition de l'URL, celle-ci n'est valable que pour quelques heures. Par conséquent, nous vous recommandons fortement d’ajouter vos propres informations d’identification S3 dans Braze.

## Exemple de sortie d'un fichier d'exportation utilisateur

Objet d'exportation de l'utilisateur (nous inclurons le moins de données possible - si un champ est absent de l'objet, il doit être considéré comme nul ou vide) :

{% tabs %}
{% tab Tous les domaines %}

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
    "dob" : (string) date for the user's date of birth,
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
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key-value pairs,
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
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
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
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
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
        "in_control": (boolean),
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
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "push_subscribe" : "opted_in", 
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
    "custom_attributes": 
    {
      "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
      "loyaltyPoints": "321",
       "loyaltyPointsNumber": 107
    },
    "custom_events": [
      {
        "name": "Loyalty Acknowledgement",
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
        "name": "Email Unsubscribe",
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
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
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
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}

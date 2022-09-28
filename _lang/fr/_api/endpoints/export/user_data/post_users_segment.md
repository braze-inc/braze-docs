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

Cet endpoint vous permet d’exporter tous les utilisateurs d’un segment. Les données utilisateur sont exportées sous forme de fichiers multiples d’objets utilisateur JSON séparés par de nouvelles lignes (c.-à-d. un objet JSON par ligne). 

Les données sont exportées vers une URL générée automatiquement ou vers un compartiment S3 si cette intégration est déjà configurée.

Cet endpoint n’est actuellement pas pris en charge par Google Cloud Storage.

Notez qu’une entreprise peut exécuter au maximum une exportation par segment à l’aide de cet endpoint à un moment donné. Attendez que votre exportation soit terminée avant de réessayer. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

{% alert important %}
En décembre 2021, les modifications suivantes ont été apportées à cette API :<br>
<br>
1. Le champ `fields_to_export` dans cette demande API est **requis**. L’option par défaut sur Tous les champs a été supprimée.<br>
2. Les champs pour `custom_events`, `purchases`, `campaigns_received`, et `canvases_received` contiennent uniquement les données des 90 derniers jours.
{% endalert %}

## Limite de débit

{% include rate_limits.md endpoint='default' %}

## Informations relatives à la réponse basée sur les informations d’identification

Si vous avez ajouté vos informations d’identification S3 à Braze, chaque fichier sera téléchargé dans votre compartiment en tant que fichier ZIP avec le format de clé qui ressemble à `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`. Nous allons créer 1 fichier pour 5 000 utilisateurs pour optimiser le traitement. Vous pouvez alors décompresser les fichiers et concaténer tous les fichiers `json` dans un fichier unique si nécessaire. Si vous spécifiez un `output_format` de `gzip`, l’extension de fichier sera `.gz` au lieu de `.zip`.

{% details Export Pathing Breakdown for ZIP File %}
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
| `RANDOM_UUID` | Un UUID aléatoire prêt à l’emploi généré par Braze au moment de la demande. | `d9696570-dfb7-45ae-baa2-25e302r2da27`
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Heure Unix (secondes depuis 2017-01-01:00:00:00Z) à laquelle l’exportation a été demandée. | `1556044807`
| `filename` | Aléatoire par fichier. | `114f0226319130e1a4770f2602b5639a`
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% enddetails %}

Si vous n’avez pas d’informations d’identification S3 fournies mais que vous avez une intégration Azure mise en place avec Braze, les données peuvent y être exportées si où vous avez coché la case **Make this the default data export destination (Faire de cette destination la destination d’exportation de données par défaut)** dans la page d’aperçu Partenaire Azure dans Braze. Si ce n’est pas le cas, la réponse à la demande fournit une URL masquée sur laquelle un fichier ZIP contenant tous les fichiers utilisateur peut être téléchargé. L’URL ne deviendra valide qu’une fois l’exportation prête. Nous suggérons vivement aux clients qui utilisent cet endpoint de configurer leurs propres informations d’identification S3 afin que les clients puissent appliquer leurs propres politiques de compartiment S3 sur l’exportation.

Sachez que si vous ne disposez pas d’informations d’identification S3, il existe une limitation de la quantité de données que vous pouvez exporter à partir de cet endpoint. En fonction des champs que vous exportez et du nombre d’utilisateurs, le transfert de fichiers peut échouer si la demande est trop importante. Une meilleure pratique consiste à spécifier les champs que vous souhaitez exporter à l’aide de « champs_à_exporter » et à ne préciser que les champs dont vous avez besoin afin de réduire la taille du transfert. Si vous souhaitez exporter tous vos utilisateurs et que vous obtenez des erreurs en générant le fichier, envisagez de diviser votre base d’utilisateurs en plus de segments en fonction d’un numéro de compartiment aléatoire (par ex. créer un segment où le numéro de compartiment aléatoire est <1000, entre 1000 et 2000, etc.).

Dans l’un ou l’autre scénario, vous pouvez éventuellement fournir un `callback_endpoint` à notifier lorsque l’exportation est prête. Si le `callback_endpoint` est fourni, nous ferons une demande Post à l’adresse indiquée lorsque le téléchargement sera prêt. Le corps du Post sera "success":true. Si vous n’avez pas ajouté d’informations d’identification S3 à Braze, le corps du Post contiendra également l’attribut `url` avec l’URL de téléchargement comme valeur.

Les bases d’utilisateurs plus grandes entraîneront des temps d’exportation plus longs. Par exemple, une application avec 20 millions d’utilisateurs peut prendre une heure ou plus.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. *Beginning April 2021, new accounts must specify specific fields to export.
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
Les attributs personnalisés individuels ne peuvent pas être exportés. Cependant, tous les attributs personnalisés peuvent être exportés en incluant `custom_attributes` dans le tableau `fields_to_export` (par ex., ['first_name', 'email', 'custom_attributes']).
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
|`segment_id` | Requis | Chaîne de caractères | Identifiant du segment à exporter. Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/).<br>
<br>
Le `segment_id` pour un segment donné se trouve dans votre **Developer Console (Console du développeur)** sur votre compte Braze, sinon vous pouvez utiliser l’[endpoint Liste des segments]({{site.baseurl}}/api/endpoints/export/segments/get_segment/).|
|`callback_endpoint` | Facultatif | Chaîne de caractères | Endpoint auquel publier une URL de téléchargement lorsque l’exportation est disponible. |
|`fields_to_export` | Requis* | Tableau de chaînes de caractères | Nom des champs de données utilisateur à exporter. Vous pouvez également exporter des attributs personnalisés. <br>
<br>
*À partir d’avril 2021, les nouveaux comptes doivent préciser des champs spécifiques à exporter. |
|`output_format` | Facultatif | Chaîne de caractères | Lorsque vous utilisez votre propre compartiment S3, vous pouvez spécifier le format de fichier `zip` ou `gzip`. Le format de fichier ZIP est défini par défaut. |
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
  "output_format" : "zip"
}'
```

## Champs à exporter

Voici une liste des `fields_to_export` valides. Utiliser `fields_to_export` pour minimiser les données renvoyées peut améliorer le temps de réponse de cet endpoint d’API :

* `apps`
* `attributed_campaign`
* `attributed_source`
* `attributed_adgroup`
* `attributed_ad`
* `braze_id`
* `campaigns_received`
* `canvases_received`
* `cards_clicked`
* `country`
* `created_at`
* `custom_attributes`
* `custom_events`
* `devices`
* `dob`
* `email`
* `email_subscribe`
* `external_id`
* `first_name`
* `gender`
* `home_city`
* `language`
* `last_coordinates`
* `last_name`
* `phone`
* `purchases`
* `push_subscribe`
* `push_tokens`
* `random_bucket`
* `time_zone`
* `total_revenue`
* `uninstalled_at`
* `user_aliases`

## Rappels importants

- Les champs pour `custom_events`, `purchases`, `campaigns_received`, et `canvases_received` contiennent uniquement les données des 90 derniers jours.
- `custom_events` et `purchases` contiennent tous les deux des champs pour `first` et `count`. Ces deux champs reflèteront les informations de tout le temps et ne seront pas limités aux données des 90 derniers jours. Par exemple, si un utilisateur particulier a effectué l’événement pour la première fois il y a plus de 90 jours, cela sera reflété avec précision dans le champ `first` et le champ `count` tiendra compte des événements qui ont eu lieu avant les 90 derniers jours également.
- Le nombre d’exportations de segments simultanées qu’une entreprise peut exécuter au niveau de l’endpoint est plafonné à 100. Les tentatives qui dépassent cette limite entraîneront une erreur.

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, e.g., 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Une fois disponible, l’URL ne sera valide que quelques heures. Par conséquent, nous vous recommandons fortement d’ajouter vos propres informations d’identification S3 dans Braze.

## Exemple de sortie de fichier d’exportation utilisateur

Objet d’exportation utilisateur (nous inclurons le moins de données possible. S’il manque un champ de l’objet, il doit être considéré comme nul, faux ou vide) :

```json
{
    "created_at" : (date),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "random_bucket" : (int)
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639 ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" "push_opted_in_at" | "subscribed" | "unsubscribed" "push_unsubscribed_at",
    "email_subscribe" : (string) "opted_in" "email_opted_in_at" | "subscribed" | "unsubscribed" "email_unsubscribed_at",
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
            "idfv" : (string) only included for iOS devices,
            "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
            "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
            "roku_ad_id" : (string) only included for Roku devices,
            "windows_ad_id" : (string) only included for Windows devices,
            "ad_tracking_enabled" : (bool)
        },
        ...
    ],
    "push_tokens" : [
        {
            "app" : (string) app name,
            "platform" : (string),
            "token" : (string),
            "device_id": (string),
            "notifications_enabled": (bool)
        },
        ...
    ],
    "apps" : [
        {
            "name" : (string),
            "platform" : (string),
            "version" : (string),
            "sessions" : (string),
            "first_used" : (string) date,
            "last_used" : (string) date
        },
        ...
    ],
    "campaigns_received" : [
        {
            "name" : (string),
            "last_received" : (string) date,
            "engaged" : {
                "opened_email" : (bool),
                "opened_push" : (bool),
                "clicked_email" : (bool),
                "clicked_in_app_message" : (bool)
            },
            "converted" : (bool),
            "api_campaign_id" : (string),
            "variation_name" : (optional, string) exists only if it is a multivariate campaign,
            "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
            "in_control" : (optional, bool) exists only if it is a multivariate campaign
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

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

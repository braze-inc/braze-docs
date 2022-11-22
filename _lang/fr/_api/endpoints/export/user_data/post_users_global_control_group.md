---
nav_title: "POST : Exportation de profil utilisateur par groupe de contrôle global"
article_title: "POST : Exportation de profil utilisateur par groupe de contrôle global"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Utilisateurs des groupes de contrôle global."

---
{% api %}
# Utilisateurs par groupe de contrôle global
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

Cet endpoint vous permet d’exporter tous les utilisateurs du groupe de contrôle global. Les données utilisateur sont exportées sous forme de fichiers multiples d’objets utilisateur JSON séparés par de nouvelles lignes (c.-à-d. un objet JSON par ligne).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

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

Si vous n’avez pas indiqué d’informations d’identification S3, la réponse à la demande fournit l’URL sur laquelle un fichier ZIP contenant tous les fichiers utilisateur peut être téléchargé. L’URL ne deviendra valide qu’une fois l’exportation prête. Sachez que si vous ne disposez pas d’informations d’identification S3, il existe une limitation de la quantité de données que vous pouvez exporter à partir de cet endpoint. En fonction des champs que vous exportez et du nombre d’utilisateurs, le transfert de fichiers peut échouer si la demande est trop importante. Une meilleure pratique consiste à spécifier les champs que vous souhaitez exporter à l’aide de « champs_à_exporter » et à ne préciser que les champs dont vous avez besoin afin de réduire la taille du transfert. Si vous souhaitez exporter tous vos utilisateurs et que vous obtenez des erreurs en générant le fichier, envisagez de diviser votre base d’utilisateurs en plus de segments en fonction d’un numéro de compartiment aléatoire (par ex. créer un segment où le numéro de compartiment aléatoire est <1000, entre 1000 et 2000, etc.).

Dans l’un ou l’autre scénario, vous pouvez éventuellement fournir un `callback_endpoint` à notifier lorsque l’exportation est prête. Si le `callback_endpoint` est fourni, nous ferons une demande Post à l’adresse indiquée lorsque le téléchargement sera prêt. Le corps du Post sera "success":true. Si vous n’avez pas ajouté d’informations d’identification S3 à Braze, le corps du Post contiendra également l’attribut `url` avec l’URL de téléchargement comme valeur.

Les bases d’utilisateurs plus grandes entraîneront des temps d’exportation plus longs. Par exemple, une application avec 20 millions d’utilisateurs peut prendre une heure ou plus.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, e.g., ['first_name', 'email', 'purchases'],
  "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
Les attributs personnalisés individuels ne peuvent pas être exportés. Cependant, tous les attributs personnalisés peuvent être exportés en incluant custom_attributes dans le tableau fields_to_export (par ex., [‘first_name’, ‘email’, ‘custom_attributes’]).
{% endalert %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --- | ----------- | --------- | ------- |
|`callback_endpoint` | Facultatif | Chaîne de caractères | Endpoint auquel publier une URL de téléchargement lorsque l’exportation est disponible. |
|`fields_to_export` | Requis* | Tableau de chaînes de caractères | Nom des champs de données utilisateur à exporter. Vous pouvez également exporter des attributs personnalisés. <br><br>*À partir d’avril 2021, les nouveaux comptes doivent préciser des champs spécifiques à exporter. |
|`output_format` | Facultatif | Chaîne de caractères | Lorsque vous utilisez votre propre compartiment S3, vous pouvez spécifier le format de fichier `zip` ou `gzip`. Le format de fichier ZIP est défini par défaut. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "callback_endpoint" : "",
  "fields_to_export" : ["email", "braze_id"],
  "output_format" : "zip"
}'
```

## Champs à exporter

Voici une liste des fields_to_export valides. Utiliser fields_to_export pour minimiser les données renvoyées peut améliorer le temps de réponse de cet endpoint d’API :

* `apps`
* `attributed_campaign`
* `attributed_source`
* `attributed_adgroup`
* `attributed_ad`
* `braze_id`
* `country`
* `created_at`
* `custom_attributes`
* `custom_events`
* `devices`
* `dob`
* `email`
* `external_id`
* `first_name`
* `gender`
* `home_city`
* `language`
* `last_coordinates`
* `last_name`
* `phone`
* `purchases`
* `random_bucket`
* `time_zone`
* `total_revenue`
* `uninstalled_at`
* `user_aliases`

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, e.g.,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Une fois disponible, l’URL ne sera valide que quelques heures. Par conséquent, nous vous recommandons fortement d’ajouter vos propres informations d’identification S3 dans Braze.

### Exemple de sortie de fichier d’exportation utilisateur

Objet d’exportation utilisateur (nous inclurons le moins de données possible. S’il manque un champ de l’objet, il doit être considéré comme nul, faux ou vide) :

```json
{
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
    "country" : (string),
    "phone" : (string),
    "language" : (string) ISO-639 two letter code,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
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
}
```

{% endapi %}
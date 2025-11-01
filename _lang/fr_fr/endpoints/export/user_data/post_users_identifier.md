---
nav_title: "POST : Exporter le profil utilisateur par identifiant"
article_title: "POST : Exporter le profil utilisateur par identifiant"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les utilisateurs par identifiant."

---
{% api %}
# Exporter le profil utilisateur par identifiant
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> Utilisez cet endpoint pour exporter des données à partir de n’importe quel profil utilisateur en spécifiant un identifiant utilisateur.

Vous pouvez inclure jusqu’à 50 `external_ids` ou `user_aliases` dans une seule requête. Si vous souhaitez spécifier `device_id`, `email_address`, ou `phone`, un seul de ces identifiants peut être inclus par demande.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `users.export.ids`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (optional, array of strings) Name of user data fields to export
}
```

{% alert note %}
Pour les clients ayant onboardé avec Braze le 22 août 2024 ou après, le paramètre de demande `fields_to_export` est requis.
{% endalert %}

## Paramètres de demande

| Paramètre          | Requis | Type de données                                                     | Description                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids`     | Facultatif | Tableau de chaînes de caractères                                              | Identifiants externes des utilisateurs que vous souhaitez exporter.                                              |
| `user_aliases`     | Facultatif | Tableau d’objets Alias utilisateur                                    | [Alias de l']({{site.baseurl}}/api/objects_filters/user_alias_object/) utilisateur pour les utilisateurs à exporter. |
| `device_id`        | Facultatif | Chaîne de caractères                                                        | L’identifiant d’appareil, tel que renvoyé par diverses méthodes SDK, telles que `getDeviceId`.                 |
| `braze_id`         | Facultatif | Chaîne de caractères                                                        | Identifiant Braze d’un utilisateur particulier.                                                      |
| `email_address`    | Facultatif | Chaîne de caractères                                                        | Adresse e-mail de l’utilisateur.                                                                       |
| `phone`            | Facultatif | Chaîne de caractères dans [E.164](https://en.wikipedia.org/wiki/E.164) format | Numéro de téléphone de l’utilisateur.                                                                        |
| `fields_to_export` | En option* | Tableau de chaînes de caractères                                              | Nom des champs de données utilisateur à exporter.<br><br>\*Ce champ est obligatoire pour utiliser la limite de débit plus rapide de 40 requêtes par seconde. Si elle est omise, la limite de débit par défaut de 250 requêtes par minute sera utilisée à la place. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\*Nécessaire pour les clients ayant onboardé avec Braze à partir du 22 août 2024.

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
}'
```

## Champs à exporter

Voici une liste des `fields_to_export` valides. Utiliser `fields_to_export` pour minimiser les données renvoyées peut améliorer le temps de réponse de cet endpoint d’API :

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
| `push_tokens`         | Tableau           | Identifiant anonyme unique qui spécifie où envoyer les notifications d'une app.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `random_bucket`       | Entier         | [Numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) de l'utilisateur, utilisé pour créer des segments uniformément distribués d'utilisateurs aléatoires.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | Chaîne de caractères          | Fuseau horaire de l’utilisateur au même format que la base de données de fuseaux horaires IANA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Float           | Revenus totaux attribués à cet utilisateur. Les revenus totaux sont calculés à partir des achats réalisés par l’utilisateur pendant la fenêtre de conversion pour les campagnes et les Canvas qu’il a reçus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Date/heure       | Date et heure de désinstallation de l’application par l’utilisateur. Absent si l’application n’a pas été désinstallée.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objet          | [Objet aliasing de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) contenant les adresses `alias_name` et `alias_label`, si elles existent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sachez que l’endpoint `/users/export/ids` extraira l’intégralité du profil utilisateur de cet utilisateur, y compris les données telles que toutes les campagnes et les Canvas reçus, tous les événements personnalisés et tous les achats effectués, et tous les attributs personnalisés. Par conséquent, cet endpoint est plus lent que les autres endpoints d’API REST.

En fonction des données demandées, cet endpoint API peut ne pas suffire à répondre à vos besoins en raison de la limite de débit de 250 demandes par minute. Si vous prévoyez d’utiliser cet endpoint régulièrement pour exporter des utilisateurs, envisagez plutôt de le faire par segment, ce qui est asynchrone et plus optimisé pour les extractions de données plus importantes.

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

L'exemple suivant illustre les données accessibles via cet endpoint.

### Exemple de sortie d'un fichier d'exportation utilisateur

Objet d'exportation de l'utilisateur (nous inclurons le moins de données possible - si un champ est absent de l'objet, il doit être considéré comme nul ou vide) :

{% tabs %}
{% tab All fields %}

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
{% tab Sample output %}

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

{% endapi %}

---
nav_title: "POST : Suivi utilisateur"
article_title: "POST : Suivi utilisateur"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Suivi utilisateur."

---
{% api %}
# Suivi utilisateur
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/users/track
{% endapimethod %}

Utilisez cet endpoint pour enregistrer des événements personnalisés, des achats et mettre à jour les attributs de profil utilisateur.

{% alert note %}
Braze traite les données transmises via l’API à leur valeur nominale et les clients ne devraient transmettre des deltas (modification des données) que pour minimiser la consommation inutile de points de données. Pour en savoir plus, consultez [Points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#data-points). 
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users track' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "attributes" : (optional, array of attributes object),
  "events" : (optional, array of event object),
  "purchases" : (optional, array of purchase object),
}
```

Les clients utilisant l’API pour les appels de serveur à serveur peuvent avoir besoin d’ajouter à leur liste blanche `rest.iad-01.braze.com` s’ils se trouvent derrière un pare-feu.

### Paramètres de demande

{% alert important %}
Pour chacun des composants de la demande répertoriés dans le tableau suivant, l’`external_id`, le `user_alias`, ou le `braze_id` est nécessaire.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Facultatif | Tableau d’objets Attributs | Voir [Objet Attributs d’utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Facultatif | Tableau d’objets Événement | Voir [Objet Événements]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Facultatif | Tableau d’objets Achat | Voir [Objet Achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de corps de demande pour le suivi des événements

```json
{
  "events": [
    {
      "external_id": "string",
      "name": "string",
      "time": "string"
    }
  ]
}
```

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user_identifier",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "external_id": "user_identifier",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2022-12-06T19:20:45+01:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "2022"
                },
                "cast": [
                    {
                        "name": "Actor1"
                    },
                    {
                        "name": "Actor2"
                    }
                ]
            }
        },
        {
            "user_alias": {
                "alias_name": "device123",
                "alias_label": "my_device_identifier"
            },
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2013-07-16T19:20:50+01:00"
        }
    ],
    "purchases": [
        {
            "external_id": "user_identifier",
            "app_id": "your_app_identifier",
            "product_id": "product_name",
            "currency": "USD",
            "price": 12.12,
            "quantity": 6,
            "time": "2017-05-12T18:47:12Z",
            "properties": {
                "color": "red",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Large",
                "brand": "Backpack Locker"
            }
        }
    ]
}`
```

## Exemple de requête pour définir des groupes d’abonnement

Cet exemple montre comment vous pouvez créer un utilisateur et définir son groupe d’abonnement dans l’objet Attributs de l’utilisateur. 

La mise à jour du statut d’abonnement avec cet endpoint mettra à jour l’utilisateur spécifié par son `external_id` (comme User1) et mettre à jour le statut de l’abonnement de tous les utilisateurs ayant le même e-mail que cet utilisateur (Utilisateur1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups" : [{
      "subscription_group_id": "subscription_group_identifier_1",
      "subscription_state": "unsubscribed"
      },
      {
        "subscription_group_id": "subscription_group_identifier_2",
        "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}'
```

## Réponses

Lorsque vous utilisez l’une des demandes API susmentionnées, vous devriez recevoir l’une des trois réponses générales suivantes :

### Message réussi

Les messages réussis seront envoyés avec la réponse suivante :

```json
{
  "message" : "success",
  "attributes_processed" : (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed" : (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed" : (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### Message réussi sans erreurs fatales

Si votre message est réussi, mais qu’il y a des erreurs non fatales, comme un objet Événement non valide hors d’une longue liste d’événements, vous recevrez la réponse suivante :

```json
{
  "message" : "success",
  "errors" : [
    {
      <minor error message>
    }
  ]
}
```

Pour les messages de réussite, toutes les données qui n’ont pas été affectées par une erreur du tableau `errors` seront toujours traitées. 

### Message avec erreurs fatales

Si votre message contient une erreur fatale, vous recevrez la réponse suivante :

```json
{
  "message" : <fatal error message>,
  "errors" : [
    {
      <fatal error message>
    }
  ]
}
```

### Codes de réponse des erreurs fatales

Les codes d’état suivants et les messages d’erreur associés seront renvoyés si votre demande rencontre une erreur fatale. Les codes d’erreur suivants indiquent qu’aucune donnée ne sera traitée.

| Code d’erreur | Raison/Cause |
| ---------------------| --------------- |
| `400 Bad Request` | Syntaxe incorrecte. |
| `401 Unauthorized` | Clé API REST inconnue ou manquante. |
| `404 Not Found` | Clé API REST inconnue (si fournie). |
| `429 Rate Limited` | Limite de débit dépassée. |
| `5XX` | Erreur de serveur interne, vous devriez réessayer avec le délai exponentiel. |
{: .reset-td-br-1 .reset-td-br-2}

Si vous recevez l’erreur « Le external_id indiqué est sur la liste noire et est non autorisé », votre requête contient peut-être un « utilisateur factice ». Pour plus d’informations, consultez [Blocage des courriers indésirables]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking). 

## Créer un profil d’utilisateur alias uniquement

Vous pouvez utiliser l’endpoint `/users/track` pour créer un nouvel utilisateur alias uniquement en définissant la clé `_update_existing_only` avec une valeur `false` dans le corps de la requête. Si cette valeur est omise, le profil utilisateur alias uniquement ne sera pas créé. Un utilisateur alias uniquement permet de s’assurer qu’un seul profil avec cet alias existe. C’est notamment utile lorsque vous construisez une nouvelle intégration, car cela empêche la création de doublons de profil utilisateur

### Exemple de requête pour créer un utilisateur alias uniquement.
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
{
    "attributes": [
        {
            "_update_existing_only": false,
            "user_alias": {
                "alias_name": "example_name",
                "alias_label": "example_label"
            },
            "email": "email@example.com"
        }
    ],
}
```

## Importation de données utilisateur héritées

Vous pouvez soumettre des données via l’API Braze pour un utilisateur qui n’a pas encore utilisé votre application mobile afin de générer un profil utilisateur. Si l’utilisateur se sert ultérieurement de l’application, toutes les informations qui suivent son identification via le SDK seront fusionnées avec le profil utilisateur existant que vous avez créé via l’appel d’API. Tout comportement utilisateur enregistré de manière anonyme par le SDK avant l’identification sera perdu lors de la fusion avec le profil utilisateur existant généré par l’API.

L’outil de segmentation inclura ces utilisateurs, qu’ils aient utilisé l’application ou pas. Si vous souhaitez exclure les utilisateurs téléchargés via l’API utilisateur qui n’ont pas encore utilisé l’application, ajoutez simplement le filtre : `Session Count > 0`.

## Effectuer des mises à jour en masse

Si vous avez un cas d’utilisation où vous devez effectuer des mises à jour par lots dans l’endpoint `users/track`, nous vous recommandons d’ajouter l’en-tête de mise à jour en masse afin que Braze puisse identifier, observer et acheminer correctement votre demande.

Reportez-vous à la demande d’exemple suivante avec l’en-tête `X-Braze-Bulk` :

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'X-Braze-Bulk: true' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{ "attributes": [ ], "events": [ ], "purchases": [ ] }'
```

{% alert warning %}
Lorsque l’en-tête `X-Braze-Bulk` est présent avec des valeurs, Braze considère la demande comme une demande en masse. Définissez la valeur sur `true`. Actuellement, définir la valeur sur `false` ne désactive pas l’en-tête ; il sera toujours traité comme si c’était vrai.
{% endalert %}

### Cas d’utilisation

Examinez les cas d’utilisation suivants dans lesquels vous pouvez utiliser l’en-tête de mise à jour en masse :

- Une tâche quotidienne où les attributs personnalisés de plusieurs utilisateurs sont mis à jour via l’endpoint `/users/track`.
- Un script de backfill de données utilisateur ad hoc qui met à jour les informations utilisateur via l’endpoint `/users/track`.

{% endapi %}

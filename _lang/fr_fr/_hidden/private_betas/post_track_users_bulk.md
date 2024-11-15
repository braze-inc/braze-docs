---
nav_title: "POST : Suivi des utilisateurs (en vrac)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "Cet article présente les détails de l'endpoint Suivi des utilisateurs (en vrac)."
---

{% api %}
# Suivre les utilisateurs (en vrac)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Utilisez cet endpoint pour enregistrer des événements et des attributs personnalisés et mettre à jour les attributs du profil utilisateur en masse.

{% alert important %}
Cet endpoint est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Quand utiliser cet endpoint ?

Semblable à [POST : Track users endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites), vous pouvez utiliser cet endpoint pour mettre à jour les profils utilisateurs. Cependant, cet endpoint est mieux adapté pour effectuer des mises à jour en masse :

- **Demandes plus importantes :** Cet endpoint autorise 10 000 utilisateurs par demande, ce qui signifie que vous devez effectuer moins de demandes pour répondre à vos besoins de mise à jour en masse.
- **Établissement de priorités :** Lors des pics de trafic, les demandes provenant de `/users/track` seront traitées en priorité par rapport à celles provenant de `/users/track/bulk`. L'utilisation des deux endpoints vous permet de mieux contrôler l'ingestion des données.

Notez que les mises à jour de cet endpoint par les utilisateurs ne déclencheront pas de campagnes ou de vitrines basées sur des actions, ne déclencheront pas d'événements d'exception et n'assureront pas le suivi des indicateurs de conversion. Les mises à jour des utilisateurs de cet endpoint sont disponibles pour la segmentation et la personnalisation.

Pensez à utiliser cet endpoint lorsque vous remplissez de nombreux profils utilisateurs lors de l'onboarding ou lorsque vous synchronisez un grand nombre de profils utilisateurs dans le cadre d'une synchronisation quotidienne.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une clé API avec l'autorisation `users.track.bulk`.

Si vous utilisez l'API pour des appels de serveur à serveur, vous devrez peut-être autoriser l'endpoint (par exemple, `rest.iad-01.braze.com`) si vous êtes derrière un pare-feu. Reportez-vous aux [endpoints par instance]({{site.baseurl}}/api/basics#endpoints) pour plus d'informations.

## Limite de débit

Nous appliquons une limite de vitesse de base de 5 requêtes par seconde à cet endpoint pour tous les clients.

Chaque demande `/users/sync/bulk` est limitée à 4 Mo et peut contenir jusqu'à 10 000 objets d'événement, d'attribut ou d'achat.

Chaque objet (tableau d'événements, d'attributs et d'achats) peut mettre à jour un utilisateur chacun, ce qui signifie que jusqu'à 10 000 utilisateurs différents peuvent être mis à jour en une seule demande. Un profil utilisateur unique peut être mis à jour avec jusqu'à 100 objets en une seule demande.

{% alert note %}
Si vous avez besoin d'une augmentation de la limite de votre débit, contactez votre gestionnaire de satisfaction client.
{% endalert %}


## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Paramètres de demande

{% alert important %}
Pour chaque composant de requête répertorié dans le tableau suivant, l'un des éléments suivants est requis : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Facultatif | Tableau d’objets Attributs | Voir [objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Facultatif | Tableau d’objets Événement | Voir l'[objet "événements"]({{site.baseurl}}/api/objects_filters/event_object/). |
| `purchases` | Facultatif | Tableau d’objets Achat | Voir les [achats d'objets]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de requêtes

### Mise à jour en masse de 10 000 profils utilisateurs en une seule demande

Vous pouvez mettre à jour jusqu'à 10 000 profils utilisateurs. Voici un exemple tronqué où la demande consiste en 10 000 objets d'attributs :

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        },
        {
            "external_id": "user2",
            "string_attribute": "vegetables",
            "boolean_attribute_1": false,
            "integer_attribute": 25,
            "array_attribute": [
                "broccoli",
                "asparagus",	
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Voici un exemple où la demande est constituée à la fois d'objets d'attributs et d'objets d'événements :

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "user1",
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
            "external_id": "user2",
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
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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
        }
    ]
}'
```

## Réponses

### Envois de messages réussis

Les messages réussis seront envoyés avec la réponse suivante :

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Message réussi sans erreurs fatales

Si votre message est réussi, mais qu’il y a des erreurs non fatales, comme un objet Événement non valide hors d’une longue liste d’événements, vous recevrez la réponse suivante :

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### Message avec erreurs fatales

Si votre message contient une erreur fatale, vous recevrez la réponse suivante :

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

#### Codes de réponse des erreurs fatales

Pour connaître les codes d'état et les messages d'erreur associés qui seront renvoyés si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs fatales et réponses.]({{site.baseurl}}/api/errors/#fatal-errors)

Si vous recevez l'erreur `provided external_id is blacklisted and disallowed`, il se peut que votre demande ait inclus un "utilisateur fictif". Pour plus d'informations, consultez la section [Filtrage du spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Foire aux questions

### Dois-je utiliser cet endpoint ou le site `/users/track`?

Nous vous recommandons d'utiliser les deux.

Pour les remplissages et les synchronisations de profils d'utilisateurs importants où le déclenchement de campagnes basées sur l'action et de Canvases, le suivi des conversions et les événements d'exception ne sont pas nécessaires, utilisez `/users/track/bulk`. 

Pour les cas d'utilisation en temps réel, utilisez l'endpoint `/users/track`.

### Quels identifiants puis-je utiliser dans /users/track/bulk?

L'une des adresses suivantes est requise : `external_id`, `braze_id`, `user_alias`, `email`, ou `phone`. Pour plus d'exemples, reportez-vous à notre documentation sur l'[objet attributs utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/), l'[objet événements]({{site.baseurl}}/api/objects_filters/event_object/) ou l'[objet achats]({{site.baseurl}}/api/objects_filters/purchase_object/). 

### Puis-je inclure des attributs, des événements et des achats dans une seule demande ?

Oui. Vous pouvez construire votre demande avec n'importe quel nombre d'attributs, d'événements et d'objets d'achat jusqu'à 10 000 objets par demande.


{% endapi %}

---
nav_title: "POST : Suivre les utilisateurs"
article_title: "POST : Suivre les utilisateurs"
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

> Utilisez cet endpoint pour enregistrer les événements et les achats personnalisés et mettre à jour les attributs du profil utilisateur.

{% alert note %}
Braze traite les données transmises par l'API à leur valeur nominale, et les clients ne doivent transmettre que des deltas (données changeantes) afin de minimiser la consommation inutile de points de données. Pour en savoir plus, consultez la rubrique [Points de données]({{site.baseurl}}/user_guide/data/data_points/).
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4cf57ea9-9b37-4e99-a02e-4373c9a4ee59 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.track`.

Les clients utilisant l'API pour les appels de serveur à serveur devront peut-être inscrire `rest.iad-01.braze.com` dans la liste des autorisations s'ils sont derrière un pare-feu.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='users track' %}

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

### Mise à jour d'un profil utilisateur par adresse e-mail

Vous pouvez mettre à jour un profil utilisateur par adresse e-mail en utilisant l'endpoint `/users/track`. 

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 26,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
    "events": [
        {
            "email": "test@braze.com",
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
            "email": "test@braze.com",
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
}'
```

### Mise à jour d'un profil utilisateur par numéro de téléphone

Vous pouvez mettre à jour un profil utilisateur par numéro de téléphone en utilisant l’endpoint `/users/track`. Cet endpoint ne fonctionne que si vous indiquez un numéro de téléphone valide.

{% alert important %}
Si vous incluez une demande avec `email` et `phone`, Braze utilisera l'e-mail comme identifiant.
{% endalert %}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "phone": "+15043277269",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ],
}'
```
### Définir les groupes d'abonnement

Cet exemple montre comment créer un utilisateur et définir son groupe d'abonnement dans l'objet attributs de l'utilisateur. 

La mise à jour de l'état de l'abonnement avec cet endpoint mettra à jour l'utilisateur spécifié par son `external_id` (par exemple User1) et mettra à jour l'état de l'abonnement de tous les utilisateurs ayant le même e-mail que cet utilisateur (User1).

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
  {
    "external_id": "user_identifier",
    "email": "example@email.com",
    "email_subscribe": "subscribed",
    "subscription_groups": [{
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

### Exemple de requête pour créer un utilisateur alias uniquement.

Vous pouvez utiliser l’endpoint `/users/track` pour créer un nouvel utilisateur alias uniquement en définissant la clé `_update_existing_only` avec une valeur `false` dans le corps de la requête. Si cette valeur est omise, le profil utilisateur alias uniquement ne sera pas créé. Un utilisateur alias uniquement permet de s’assurer qu’un seul profil avec cet alias existe. C’est notamment utile lorsque vous construisez une nouvelle intégration, car cela empêche la création de doublons de profil utilisateur

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
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
}'
```


## Réponses

Lorsque vous utilisez l'une des requêtes API susmentionnées, vous devriez recevoir l'une des trois réponses générales suivantes : un [message de réussite](#successful-message), un [message de réussite avec des erreurs non fatales](#successful-message-with-non-fatal-errors) ou un [message avec des erreurs fatales](#message-with-fatal-errors).

### Message réussi

Les messages réussis seront envoyés avec la réponse suivante :

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

### Message réussi sans erreurs fatales

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

Pour les messages de réussite, toutes les données non affectées par une erreur dans le tableau `errors` continueront d’être traitées. 

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

### Codes de réponse des erreurs fatales

Pour connaître les codes d'état et les messages d'erreur associés qui seront renvoyés si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs fatales et réponses.]({{site.baseurl}}/api/errors/#fatal-errors)

Si vous recevez le message d'erreur "provided external_id is blacklistted and disallowed", il se peut que votre demande contienne un "utilisateur fictif". Pour plus d'informations, reportez-vous à la section [Blocage des spams.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking) 

## Foire aux questions

{% multi_lang_include email-via-sms-warning.md %}

### Que se passe-t-il lorsque plusieurs profils avec la même adresse e-mail sont trouvés ?
Si l’`external_id` existe, le profil le plus récemment mis à jour avec un ID externe sera utilisé en priorité pour les mises à jour. Si l’`external_id` n’existe pas, le profil le plus récemment mis à jour sera utilisé en priorité pour les mises à jour.

### Que se passe-t-il si aucun profil avec l’adresse e-mail n’existe actuellement ?
Un nouveau profil sera créé, ainsi qu'un utilisateur exclusivement par e-mail. Aucun alias ne sera créé. Le champ e-mail sera défini sur test@braze.com, comme indiqué dans l'exemple de demande de mise à jour d'un profil utilisateur par l'adresse e-mail.

### Comment utiliser `/users/track` pour importer des données utilisateur héritées ?
Vous pouvez soumettre des données via l'API de Braze pour un utilisateur qui n'a pas encore utilisé votre application mobile afin de générer un profil utilisateur. Si l'utilisateur utilise ensuite l'application, toutes les informations relatives à son identification à l'aide du SDK seront fusionnées avec le profil utilisateur existant que vous avez créé à l'aide de l'appel API. Tout comportement de l'utilisateur enregistré de manière anonyme par le SDK avant l'identification sera perdu lors de la fusion avec le profil utilisateur existant généré par l'API.

L’outil de segmentation inclura ces utilisateurs, qu’ils aient utilisé l’application ou pas. Si vous souhaitez exclure les utilisateurs téléchargés à l'aide de l'API utilisateur qui n'ont pas encore utilisé l'application, ajoutez le filtre `Session Count > 0`.

### Comment `/users/track` gère-t-il les événements en double ?

Chaque objet d'événement du tableau d'objets représente une occurrence unique d'un événement personnalisé par un utilisateur à un moment donné. Cela signifie que chaque événement intégré dans Braze possède son propre ID, de sorte que les événements "dupliqués" sont traités comme des événements distincts et uniques.

### Comment `/users/track` gère-t-il les attributs personnalisés imbriqués non valides ?

Lorsqu'un attribut personnalisé imbriqué contient des valeurs non valides (telles que des formats d'heure non valides ou des valeurs nulles), toutes les mises à jour de l'attribut personnalisé imbriqué dans la demande seront exclues du traitement. Cela s'applique à toutes les structures imbriquées dans cet attribut spécifique. Pour garantir un traitement réussi, vérifiez que toutes les valeurs des attributs personnalisés imbriqués sont valides avant l'envoi.

## Utilisateurs actifs par mois CY 24-25
Pour les clients qui ont acheté Utilisateurs actifs par mois - CY 24-25, Braze gère différentes limites de débit sur son endpoint `/users/track`:
- Les limites de débit horaire sont fixées en fonction de l'activité d'ingestion de données prévue sur votre compte, qui peut correspondre au nombre d'utilisateurs actifs par mois que vous avez achetés, au secteur d'activité, à la saisonnalité ou à d'autres facteurs.
- En plus de la limite horaire, Braze applique une limite de rafale sur le nombre de demandes qui peuvent être envoyées toutes les trois secondes.
- Chaque demande peut comporter jusqu'à 50 mises à jour combinées pour des attributs, des événements ou des objets d'achat.

Les limites actuelles basées sur l'ingestion prévue peuvent être trouvées dans le tableau de bord sous **Paramètres** > **API et identifiants** > **Tableau de bord de l'utilisation de l'API**. Nous pouvons modifier les limites de débit pour protéger la stabilité du système ou permettre une augmentation du débit de données sur votre compte. Veuillez contacter l'assistance Braze ou votre gestionnaire satisfaction client pour toute question ou préoccupation concernant la limite de demande horaire ou par seconde et les besoins de votre entreprise.



{% endapi %}

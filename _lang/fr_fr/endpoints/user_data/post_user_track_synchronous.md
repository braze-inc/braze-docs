---
nav_title: "POST : Suivi des utilisateurs (synchrone)"
article_title: "POST : Suivi des utilisateurs (synchrone)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "Cet article présente en détail l’endpoint synchrone Suivi utilisateur de Braze."

---
{% api %}
# Suivi des utilisateurs (synchrone)
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Utilisez cet endpoint pour enregistrer les événements personnalisés et les achats et pour mettre à jour les attributs de profil utilisateur de manière synchrone. Cet endpoint fonctionne de la même manière que l’[endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), qui met à jour les profils utilisateurs de manière asynchrone.

{% alert important %}
Cet endpoint est actuellement en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cette version bêta.
{% endalert %}

## Appels d'API synchrones et asynchrones

Dans le cas d'un appel asynchrone, l'API renvoie le code d'état `201`, indiquant que votre demande a été reçue, comprise et acceptée avec succès. Toutefois, cela ne signifie pas que votre requête a été entièrement exécutée.

Dans le cas d'un appel synchrone, l'API renvoie un code d'état `201`, indiquant que votre requête a été reçue, comprise, acceptée et exécutée avec succès. La réponse à l'appel indiquera les champs du profil utilisateur sélectionnés à la suite de l'opération.

La limite de débit de cet endpoint est inférieure à celle de l'endpoint `/users/track` (voir [Limite de débit](#rate-limit) ci-dessous). Chaque demande `/users/track/sync` ne peut contenir qu'un seul objet d'événement, un seul objet d'attribut **ou** un seul objet d'achat. Cet endpoint doit être réservé aux mises à jour du profil utilisateur pour lesquelles un appel synchrone est nécessaire. Pour une implémentation saine, nous vous recommandons d'utiliser `/users/track/sync` et `/users/track` ensemble.

Par exemple, si vous envoyez des requêtes consécutives pour le même utilisateur sur une courte période, des conditions de concurrence sont possibles avec l’endpoint `/users/track` asynchrone, mais avec l’endpoint `/users/track/sync`, vous pouvez envoyer ces requêtes en séquence, chacune après avoir reçu une réponse `2XX`.

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key/) avec l’autorisation `users.track.sync`.

Les clients utilisant l'API pour les appels de serveur à serveur devront peut-être inscrire `rest.iad-01.braze.com` dans la liste des autorisations s'ils sont derrière un pare-feu.

## Limite de débit

Nous appliquons une limite de vitesse de base de 500 requêtes par minute à cet endpoint pour tous les clients. Chaque requête `/users/track/sync` peut contenir jusqu'à un objet d'événement, un objet d'attribut ou un objet d'achat. Chaque objet (événement, attribut et tableau d’achat) peut mettre à jour un utilisateur chacun.

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Paramètres de demande

{% alert important %}
Pour chaque composant de requête répertorié dans le tableau suivant, l'un des éléments suivants est requis : `external_id`, `user_alias`, `braze_id`, `email` ou `phone`.
{% endalert %}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Facultatif | Un objet à attributs | Voir [objet attributs de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Facultatif | Un objet d'événement | Voir l'[objet "événements"]({{site.baseurl}}/api/objects_filters/event_object/). |
| `purchases` | Facultatif | Un objet d'achat | Voir [Objet Achats]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Réponses

Lorsque vous utilisez les [paramètres de requête](#request-parameters) de cet endpoint, vous devriez recevoir l'une des réponses suivantes : un message de réussite ou un message contenant des erreurs fatales.

### Message réussi

Les messages réussis renvoient la réponse suivante, qui contient des informations sur les données du profil utilisateur qui ont été mises à jour.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Only custom attributes from the request will be listed,
        "custom_events": (optional, object), the custom events as a result of the request. Only custom events from the request will be listed,
        "purchase_events": (optional, object), the purchase events as a result of the request. Only purchase events from the request will be listed,
    },
    "message": "success"
```

### Message avec erreurs fatales

Si votre message comporte une erreur fatale, vous recevrez la réponse suivante :

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

## Exemples de demandes et de réponses

### Mise à jour d'un attribut personnalisé par ID externe

#### Requête

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Réponse

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
} 
```

### Mise à jour d'un événement personnalisé par e-mail

#### Requête

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
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
        }
    ]
}'
```

#### Réponse

```
{
    "users": [
        {
            "email": "test@braze.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
} 
```

### Mise à jour d'un événement d'achat par alias d'utilisateur

#### Requête

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : { 
          "alias_name" : "device123", 
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [ 
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            { 
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Réponse

```
{
    "users": [
        {
          "user_alias" : { 
            "alias_name" : "device123", 
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
} 
```

## Foire aux questions

### Dois-je utiliser l'endpoint asynchrone ou synchrone ?

Pour la plupart des mises à jour de profil, l'endpoint `/users/track` est le plus adapté en raison de sa limite de débit plus élevée et de sa flexibilité qui vous permet de regrouper les requêtes. Cependant, l'endpoint `/users/track/sync` est utile si vous rencontrez des conditions de concurrence dues à des demandes rapides et consécutives pour le même utilisateur.

### Le temps de réponse diffère-t-il de l'endpoint `/users/track`?

Dans le cas d'un appel synchrone, l'API attend que la requête soit terminée pour renvoyer une réponse. Par conséquent, les requêtes synchrones prendront en moyenne plus de temps que les requêtes asynchrones à `/users/track`. Pour la majorité des requêtes, vous pouvez vous attendre à une réponse en quelques secondes.

### Puis-je envoyer plusieurs demandes en même temps ?

Oui, à condition que les demandes concernent des utilisateurs différents, ou que chaque demande mette à jour des attributs, des événements ou des achats différents pour un même utilisateur.

Si vous envoyez plusieurs demandes pour un utilisateur, pour le même attribut, le même événement ou le même achat, Braze recommande d'attendre une réponse positive entre chaque demande afin d'éviter les conditions de concurrence.

### Pourquoi la valeur de la réponse ne correspond-elle pas à celle de ma demande initiale ?

Bien que votre demande soit terminée, il est possible que la valeur de votre attribut personnalisé n'ait pas été mise à jour. Cela peut se produire lorsque la mise à jour de votre attribut personnalisé dépasse le nombre maximum de caractères, dépasse les limites du tableau ou si l'utilisateur n'existe pas dans Braze et que vous avez `_update_existing_only = true`.

Dans ces cas, considérez la réponse comme une indication que, même si votre requête a bien été complétée, la mise à jour n’a pas été effectuée. Procédez à la résolution des problèmes en vous référant aux raisons susmentionnées.

{% endapi %}

---
nav_title: "POST : Envoyez des messages canvas à l'aide de la réception/distribution déclenchée par l'API"
article_title: "POST : Envoi de messages canvas à l'aide de la réception/distribution déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Braze Send Canvases using API-triggered delivery (Envoyer des toiles à l'aide d'une réception/distribution déclenchée par l'API)."

---
{% api %}
# Envoyez des messages canvas à l'aide de la réception/distribution déclenchée par l'API
{% apimethod postcore_endpoint|https://www.braze.com/docs/core_endpoints  %}
/canvas/trigger/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages canvas avec réception/distribution déclenchée par l'API.

La réception/distribution déclenchée par l'API vous permet de stocker le contenu des messages dans le tableau de bord de Braze tout en dictant quand un message est envoyé, et à qui, à l'aide de votre API.

Avant de pouvoir envoyer des messages avec cet endpoint, vous devez disposer d'un [ID Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (qui est créé lorsque vous créez un Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `canvas.trigger.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "context": (optional, object) personalization key-value pairs that apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message sends to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "context": (optional, object) personalization key-value pairs that apply to this user (these key-value pairs override any keys that conflict with the parent `context`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
    }],
    ...
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Requis | Chaîne de caractères | Voir [Identifiant Canvas]({{site.baseurl}}/api/identifier_types/). |
|`context`| Facultatif | Objet | Cela inclut les propriétés d'entrée canvas. Les paires clé-valeur de personnalisation s'appliquent à tous les utilisateurs concernés par cette requête. L'objet contextuel peut atteindre une taille maximale de 50 Ko. |
|`broadcast`| Facultatif | Valeur booléenne | Il est nécessaire de définir`broadcast`la valeur sur « true » lorsque vous envoyez un message à l'ensemble du segment configuré comme public cible du canvas dans le tableau de bord de Braze. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Toutefois, soyez prudent lorsque vous définissez `broadcast: true`, car en activant involontairement cet indicateur, vous risquez d'envoyer votre message à une audience plus large que prévu. |
|`audience`| Facultatif| Objet Audience connectée | Voir l'[audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). Lorsque vous incluez `audience`, le message est envoyé uniquement aux utilisateurs qui correspondent aux filtres définis, tels que les attributs personnalisés et les statuts d'abonnement. |
|`recipients`| Facultatif | Tableau | Voir l'[objet Destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/). <br><br>Si cette option n'est pas fournie et que`broadcast`  est défini sur `true`, le message est envoyé à l'ensemble du segment configuré comme audience cible du canvas dans le tableau de bord de Braze.<br><br> Le tableau d'objets `recipients` peut contenir jusqu'à 50 objets, chaque objet contenant une chaîne de caractères `external_user_id` et un objet `canvas_entry_properties`. Cet appel nécessite un `external_user_id`, `user_alias`, ou `email`. Les demandes ne doivent en spécifier qu’un seul des deux. <br><br>Si `email` est l'identifiant, vous devez inclure [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) dans l'objet destinataire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "context": {"product_name" : "shoes", "product_price" : 79.99},
  "broadcast": false,
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "equals",
          "value": "blue"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparison": "includes_value",
          "value": "pizza"
        }
      },
      {
        "OR": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparison": "less_than_x_days_ago",
              "value": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "value": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "value": "subscribed"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "recipients": [
    {
      "user_alias": {
        "alias_name" : "example_name",
        "alias_label" : "example_label"
      },
      "external_user_id": "user_identifier",
      "send_to_existing_only": true,
      "attributes": {
          "first_name" : "Alex"
      }
    }
  ]
}'
```

## Informations relatives à la réponse

Les réponses des points de terminaison d'envoi de messages incluent le message`dispatch_id`pour référence à l'envoi du message. Le `dispatch_id` est l’ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Consultez [Comportement du Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/) pour plus d’informations.

### Exemple de réponse réussie

Le code de statut `201` pourrait renvoyer le corps de réponse suivant. Si le canvas est archivé, arrêté ou mis en pause, il n'est pas envoyé via cet endpoint.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Si votre canvas est archivé, le message`notice` suivant s'affiche : "The Canvas" est archivé. Désarchivez le Canvas pour vous assurer que les demandes de déclencheurs prendront effet." Si votre canvas n'est pas actif, le message`notice` suivant s'affiche : "La toile est en pause. Reprenez le Canvas pour vous assurer que les demandes de déclencheurs prendront effet."

Si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs et réponses]({{site.baseurl}}/api/errors/#fatal-errors) pour connaître le code d'erreur et sa description.

## Considérations

Veuillez tenir compte des éléments suivants lorsque vous effectuez des appels API pour envoyer des messages Canvas à l'aide de la réception/distribution déclenchée par API :

- **Envoi aux utilisateurs existants** : Lorsque`send_to_existing_only`  est défini sur`true`  (valeur par défaut), le message est envoyé uniquement aux utilisateurs existants dans Braze.
- **Création de nouveaux utilisateurs** : Lorsque`send_to_existing_only`  est défini sur `false`, il est nécessaire d'inclure un`attributes`objet . Si un utilisateur avec l'ID spécifié n'existe pas, Braze crée un utilisateur avec cet ID et ces attributs avant d'envoyer le message.
- **Limitation des alias d'utilisateur** : Le`send_to_existing_only`drapeau ne peut pas être utilisé avec les alias d'utilisateur. Pour envoyer un message à un utilisateur disposant uniquement d'un alias d'utilisateur, celui-ci doit déjà exister dans Braze.
- **Ciblage par segment** : Le`segment_id`paramètre n'est pas pris en charge pour cet endpoint. Pour cibler un segment, veuillez configurer le segment dans les paramètres de l'audience du canvas dans le tableau de bord de Braze et utiliser `broadcast: true`, ou utiliser le`audience`paramètre avec les filtres [d'audience Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience/).
- **Ciblage combiné** : Lorsque vous incluez à la fois le`recipients`paramètre et configurez un segment cible dans le tableau de bord, le message est envoyé uniquement aux profils utilisateurs spécifiés dans l'appel API et qui correspondent également aux filtres du segment.
- **Appels de serveur à serveur** : Si vous effectuez des appels de serveur à serveur, il peut être nécessaire d'ajouter l'URL de l'API appropriée à la liste blanche si vous êtes derrière un pare-feu.

## Objet Attributes pour Canvas

Utilisez l'objet de message `attributes` pour ajouter, créer ou mettre à jour les attributs et les valeurs d'un utilisateur avant de lui envoyer un canvas déclenché par l'API à l'aide de l'endpoint `canvas/trigger/send`. Cet appel API traite l'objet des attributs de l'utilisateur avant de traiter et d'envoyer le canvas. Cela permet de minimiser le risque de problèmes causés par des [conditions de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/). Toutefois, par défaut, les groupes d'abonnement ne peuvent pas être mis à jour de cette manière.

{% alert note %}
Vous cherchez la version campagne de cet endpoint ? Consultez la rubrique [Envoi de messages de campagne à l'aide de la réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}

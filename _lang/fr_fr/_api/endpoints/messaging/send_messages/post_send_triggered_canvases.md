---
nav_title: "POST : Envoyer des messages Canvas via la livraison déclenchée par API"
article_title: "POST : Envoyer des messages Canvas via la livraison déclenchée par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Envoyer des Canvas via une livraison déclenchée par API."

---
{% api %}
# Envoyer des messages Canvas via une livraison déclenchée par API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages Canvas via la livraison déclenchée par API.

La livraison déclenchée par API vous permet de stocker le contenu d’un message dans le tableau de bord de Braze, tout en indiquant quand et à qui un message est envoyé via votre API.

Avant de pouvoir envoyer des messages avec cet endpoint, vous devez disposer d'un [ID Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (qui est créé lorsque vous créez un Canvas).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `canvas.trigger.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see Broadcast -- defaults to false on 8/31/17, must be set to true if `recipients` is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas)
    [{
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Requis | Chaîne de caractères | Voir [identifiant de Canvas]({{site.baseurl}}/api/identifier_types/). |
|`canvas_entry_properties`| Facultatif | Objet | Voir [Propriétés de l'entrée dans le canevas.]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) Les paires clé-valeur de personnalisation qui s’appliquent à tous les utilisateurs de cette demande. La limite maximale de taille de l’objet Propriétés d’entrées de Canvas est de 50 Ko. |
|`broadcast`| Facultatif | Valeur booléenne | Vous devez définir `broadcast` sur « true » lorsque vous envoyez un message à un segment entier qui est ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, faites attention lors de la configuration de `broadcast: true` car en configurant involontairement cet indicateur, vous pourriez envoyer votre message à une audience plus importante que prévue. |
|`audience`| Facultatif| Objet Audience connectée | Voir l'[audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Facultatif | Tableau | Voir l'[objet Destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/). Si non renseigné et que `broadcast` est défini sur Vrai, le message sera envoyé au segment entier ciblé par Canvas.<br><br> Le tableau `recipients` peut contenir jusqu’à 50 objets, avec chaque objet contenant une seule chaîne de caractères `external_user_id` et objet `canvas_entry_properties`. `external_user_id` ou `user_alias` est requis pour cet appel. Les demandes ne doivent en spécifier qu’un seul des deux. <br><br> Quand `send_to_existing_only` est défini sur `true`, Braze envoie uniquement le message aux utilisateurs existants, mais cet indicateur ne peut pas être utilisé avec les alias utilisateur. Quand `send_to_existing_only` est défini sur `false` et qu’un utilisateur avec l’`id` donné n’existe pas, Braze crée un utilisateur avec cet ID et cet attribut avant d’envoyer le message.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Les clients qui utilisent l'API pour des appels de serveur à serveur peuvent avoir besoin d'autoriser l'URL API appropriée s'ils sont derrière un pare-feu.

{% alert important %}
La spécification d'un destinataire par son adresse e-mail est actuellement en accès anticipé. Contactez votre gestionnaire de satisfaction client si vous souhaitez participer à cet accès anticipé.
{% endalert %}

{% alert note %}
Si vous incluez des utilisateurs spécifiques dans votre appel d’API et un segment cible dans le tableau de bord, le message sera envoyé spécifiquement aux profils d’utilisateur qui sont dans l’appel d’API et qui correspondent aux filtres de segment.
{% endalert %}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79.99},
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

Les réponses des endpoints d’envoi de messages incluront le `dispatch_id` du message pour y faire référence lors de l’envoi. Le `dispatch_id` est l’ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Consultez [Comportement du Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/) pour plus d’informations.

### Exemple de réponse réussie

Le code de statut `201` pourrait renvoyer le corps de réponse suivant. Si le Canvas est archivé, arrêté ou en pause, le Canvas ne sera pas envoyé via ce point de terminaison.

```
{
  "notice": "The Canvas is paused. Resume the Canvas to ensure trigger requests will take effect.",
  "dispatch_id": "example_dispatch_id",
  "message": "success"
}
```

Si votre Canvas est archivé, vous verrez ce message `notice`: "The Canvas" est archivé. Désarchivez le Canvas pour vous assurer que les demandes de déclencheurs prendront effet." Si votre Canvas n'est pas actif, vous verrez ce message `notice`: "La toile est en pause. Reprenez le Canvas pour vous assurer que les demandes de déclencheurs prendront effet."

Si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs et réponses]({{site.baseurl}}/api/errors/#fatal-errors) pour connaître le code d'erreur et sa description.

## Objet d'attributs pour Canvas

Utilisez l'objet de message `attributes` pour ajouter, créer ou mettre à jour les attributs et les valeurs d'un utilisateur avant de lui envoyer un canvas déclenché par l'API à l'aide de l'endpoint `canvas/trigger/send`. Cet appel API traite l'objet des attributs de l'utilisateur avant de traiter et d'envoyer le canvas. Cela permet de minimiser le risque de problèmes causés par des [conditions de concurrence]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert note %}
Vous recherchez la version des campagnes de cet endpoint ? Consultez la rubrique [Envoi de messages de campagne via la réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}

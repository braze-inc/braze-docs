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

Avant de pouvoir envoyer des messages avec ce point de terminaison, tu dois avoir un [identifiant Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier) (qui est créé lorsque tu construis un Canvas).

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
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "canvas_entry_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent `canvas_entry_properties`)
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }],
    ...
}
```

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
|`canvas_id`| Obligatoire | Chaîne de caractères | Voir [Identifiant Canvas]({{site.baseurl}}/api/identifier_types/). |
|`canvas_entry_properties`| Facultatif | Objet | Voir les [propriétés de l'entrée Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Les paires clé-valeur de personnalisation qui s’appliquent à tous les utilisateurs de cette demande. La limite maximale de taille de l’objet Propriétés d’entrées de Canvas est de 50 Ko.
|`broadcast`| Facultatif | Booléen | Tu dois donner la valeur true à `broadcast` lorsque tu envoies un message à un segment entier ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, fais attention lorsque tu définis `broadcast: true`, car si tu définis ce drapeau sans le vouloir, tu risques d'envoyer ton message à un public plus large que prévu. |
|`audience`| Facultatif| Objet d’audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Facultatif | Tableau | Voir l'[objet Recipients]({{site.baseurl}}/api/objects_filters/recipient_object/). Si non renseigné et que `broadcast` est défini sur Vrai, le message sera envoyé au segment entier ciblé par Canvas.<br><br> Le tableau `recipients` peut contenir jusqu’à 50 objets, avec chaque objet contenant une seule chaîne de caractères `external_user_id` et objet `canvas_entry_properties`. `external_user_id` ou `user_alias` est requis pour cet appel. Les demandes ne doivent en spécifier qu’un seul des deux. <br><br> Quand `send_to_existing_only` est défini sur `true`, Braze envoie uniquement le message aux utilisateurs existants, mais cet indicateur ne peut pas être utilisé avec les alias utilisateur. Quand `send_to_existing_only` est défini sur `false` et qu’un utilisateur avec le paramètre `id` donné n’existe pas, Braze crée un utilisateur avec cet ID et cet attribut avant d’envoyer le message.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Les clients utilisant l’API pour les appels de serveur à serveur peuvent avoir besoin d’ajouter à leur liste blanche l’URL d’API appropriée s’ils se trouvent derrière un pare-feu.

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
      "trigger_properties": "",
      "canvas_entry_properties": "",
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

## Endpoint Créer un envoi

**Utilisation de l'objet Attributs dans Canvas**

Braze dispose d’un objet Messagerie appelé `Attributes` qui vous permet d’ajouter, de créer ou de mettre à jour les attributs et les valeurs d’un utilisateur avant de lui envoyer un Canvas déclenché par API en utilisant l’endpoint `canvas/trigger/send`, car cet appel d’API traitera l’objet Attributs utilisateur avant qu’il ne traite et envoie le Canvas. Cela permet de minimiser le risque de problèmes causés par des [conditions de concurrence]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert important %}
Vous recherchez la version des campagnes de cet endpoint ? Jette un coup d'œil à l'article [Envoi de messages de campagne via une livraison déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

{% endapi %}


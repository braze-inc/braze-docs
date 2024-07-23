---
nav_title: "POST :  : Envoyer des campagnes via une livraison déclenchée par API"
article_title: "POST :  : Envoyer des campagnes via une livraison déclenchée par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Envoyer des campagnes via une livraison déclenchée par API."

---
{% api %}
# Envoyer des messages de campagne via une livraison déclenchée par API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Utilisez ce point de terminaison pour envoyer des messages immédiats et ponctuels à des utilisateurs désignés via une livraison déclenchée par l'API. 

La livraison déclenchée par API vous permet de stocker le contenu d’un message dans le tableau de bord de Braze, tout en indiquant quand et à qui un message est envoyé via votre API.

Si vous souhaitez cibler un segment, un enregistrement de votre demande sera stocké dans la [](https://dashboard.braze.com/app_settings/developer_console/activitylog/)console de développement . Pour envoyer des messages avec ce point de terminaison, vous devez disposer d'un [ID de campagne](https://www.braze.com/docs/api/identifier_types/) créé lorsque vous créez une [campagne déclenchée par l'API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `campaigns.trigger.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "trigger_properties": (optional, object) personalization key-value pairs that will apply to all users in this request,
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted,
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  "recipients": (optional, array; if not provided and broadcast is not set to `false`, message will send to the entire segment targeted by the campaign)
    [
      {
      // Either "external_user_id" or "user_alias" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
  ]
}
```

## Paramètres de demande

| Paramètre | Obligatoire | Type de données | Descriptif |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Obligatoire|Chaîne de campagne|Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Facultatif | Chaîne de caractères | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/). |
|`trigger_properties`| Facultatif | Objet | Voir [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Les paires clé-valeur de personnalisation qui s’appliquent à tous les utilisateurs de cette demande.
|`broadcast`| Facultatif | Booléen | Vous devez définir `broadcast` sur true lors de l'envoi d'un message à un segment entier ciblé par une campagne ou un canevas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Soyez toutefois prudent lors du réglage `broadcast: true`, car l'activation involontaire de cet indicateur peut vous amener à envoyer votre message à un public plus large que prévu. |
|`audience`| Facultatif | Objet d’audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Facultatif | Tableau | Voir [objet destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/).<br><br>Si `send_to_existing_only` est `false`, un objet Attribut doit être inclus.<br><br>Si `recipients` n'est pas fourni et `broadcast` est défini sur true, le message sera envoyé à l'ensemble du segment ciblé par la campagne. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

- Le tableau des destinataires peut contenir jusqu’à 50 objets, avec chaque objet contenant une seule chaîne de caractères `external_user_id` et objet `trigger_properties`.
- Quand `send_to_existing_only` est défini sur `true`, Braze envoie uniquement le message aux utilisateurs existants. Cependant, cet indicateur ne peut pas être utilisé avec les alias utilisateur. 
- Quand `send_to_existing_only` est `false`, un attribut doit être inclus. Braze créera un utilisateur avec le `id` et les attributs avant d'envoyer le message.

Le statut du groupe d'abonnement d'un utilisateur peut être mis à jour en incluant un paramètre `subscription_groups` dans l’objet `attributes`. Pour plus de détails, consultez [Objet Attributs d’utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "trigger_properties": "",
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
      "external_user_id": "external_user_identifier",
      "trigger_properties": "",
      "send_to_existing_only": true,
      "attributes": {
        "first_name" : "Alex"
      }
    }
  ]
}'
```

## Informations relatives à la réponse

Les réponses des endpoints d’envoi de messages incluront le `dispatch_id` du message pour y faire référence lors de l’envoi. Un  est l’identifiant de la transmission du message, c’est un ID unique pour chaque « dispatch » envoyé par Braze. Lorsque vous utilisez cet endpoint, vous recevez un seul `dispatch_id` pour un ensemble complet d’utilisateurs regroupés. Pour plus d'informations sur `dispatch_id`, consultez notre documentation sur le [comportement du Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

## Endpoint Créer un envoi

**Utiliser l'objet Attributs dans les campagnes**

Braze a un objet de messagerie appelé `attributes` qui vous permettra d'ajouter, de créer ou de mettre à jour les attributs et les valeurs d'un utilisateur avant de lui envoyer une campagne déclenchée par l'API. En utilisant l’endpoint `campaign/trigger/send` car cet appel d'API traitera l'objet Attributs d’utilisateur avant de traiter et d'envoyer la campagne. Cela permet de minimiser le risque de problèmes causés par des conditions de concurrence. 

{% alert important %}
Vous recherchez la version Canvas de cet endpoint ? Consultez [Envoi de messages Canvas via une livraison déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint).
{% endalert %}

{% endapi %}

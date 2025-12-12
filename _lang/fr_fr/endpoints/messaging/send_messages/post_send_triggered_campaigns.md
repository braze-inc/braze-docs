---
nav_title: "POST : Envoyez des campagnes à l'aide de la réception/distribution déclenchée par l'API"
article_title: "POST : Envoyez des campagnes à l'aide de la réception/distribution déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails du point de terminaison Braze d'envoi de campagnes à l'aide d'une réception/distribution déclenchée par API."

---
{% api %}
# Envoyez des messages de campagne à l'aide de la réception/distribution déclenchée par l'API.
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/trigger/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages immédiats et ponctuels à des utilisateurs désignés en utilisant la réception/distribution déclenchée par l'API.

La réception/distribution déclenchée par l'API vous permet d'héberger le contenu des messages dans le tableau de bord de Braze tout en dictant quand un message est envoyé, et à qui, à l'aide de votre API.

Si vous ciblez un segmentation, un enregistrement de votre demande sera stocké dans la [console de développement.](https://dashboard.braze.com/app_settings/developer_console/activitylog/) Pour envoyer des messages avec cet endpoint, vous devez disposer d'un [ID de campagne](https://www.braze.com/docs/api/identifier_types/) créé lorsque vous créez une [campagne déclenchée par l'API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `campaigns.trigger.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='send messages endpoints' %}

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
      // Either "external_user_id" or "user_alias" or "email" is required. Requests must specify only one.
      "user_alias": (optional, user alias object) user alias of user to receive message,
      "external_user_id": (optional, string) external identifier of user to receive message,
      "email": (optional, string) email address of user to receive message,
      "prioritization": (optional, array) prioritization array; required when using email,
      "trigger_properties": (optional, object) personalization key-value pairs that will apply to this user (these key-value pairs will override any keys that conflict with the parent trigger_properties),
      "send_to_existing_only": (optional, boolean) defaults to true, can't be used with user aliases; if set to `false`, an attributes object must also be included,
      "attributes": (optional, object) fields in the attributes object will create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values will be overwritten
    }
  ],
  "attachments": (optional, array) array of JSON objects that define the files you need attached, defined by "file_name" and "url",
    [
      {  
       "file_name": (required, string) the name of the file you want to attach to your email, excluding the extension (for example, ".pdf"). Attach files up to 2 MB. This is required if you use "attachments",
       "url": (required, string) the corresponding URL of the file you want to attach to your email. The file name's extension will be detected automatically from the URL defined, which should return the appropriate "Content-Type" as a response header. This is required if you use "attachments",
      }
    ]
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Requis|Chaîne de caractères|Voir [identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
|`send_id`| Facultatif | Chaîne de caractères | Voir [identifiant d'envoi]({{site.baseurl}}/api/identifier_types/). |
|`trigger_properties`| Facultatif | Objet | Voir les [propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Les paires clé-valeur de personnalisation s'appliqueront à tous les utilisateurs de cette demande. |
|`broadcast`| Facultatif | Valeur booléenne | Vous devez définir `broadcast` sur « true » lorsque vous envoyez un message à un segment entier qui est ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Toutefois, soyez prudent lorsque vous définissez `broadcast: true`, car en activant involontairement cet indicateur, vous risquez d'envoyer votre message à une audience plus large que prévu. |
|`audience`| Facultatif | Objet Audience connectée| Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`recipients`| Facultatif | Tableau | Voir [objet destinataire]({{site.baseurl}}/api/objects_filters/recipient_object/).<br><br>Si `send_to_existing_only` est `false`, un objet Attribut doit être inclus.<br><br>Si `recipients` n'est pas fourni et que `broadcast` a la valeur "true", le message sera envoyé à l'ensemble du segment ciblé par la campagne. <br><br> Si `email` est l'identifiant, vous devez inclure [`prioritization`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email) dans l'objet destinataire. |
|`attachments`| Facultatif | Tableau | Si `broadcast` est défini comme vrai, la liste `attachments` ne peut pas être incluse. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

- Le tableau d'objets peut contenir jusqu'à 50 objets, chaque objet contenant une chaîne de caractères `external_user_id` et un objet `trigger_properties`.
- Quand `send_to_existing_only` est défini sur `true`, Braze envoie uniquement le message aux utilisateurs existants. Cependant, cet indicateur ne peut pas être utilisé avec les alias utilisateur.
- Lorsque `send_to_existing_only` est `false`, un attribut doit être inclus. Braze créera un utilisateur avec le site `id` et les attributs avant d'envoyer le message.

Le statut du groupe d'abonnement d'un utilisateur peut être mis à jour en incluant un paramètre `subscription_groups` dans l'objet `attributes`. Pour plus de détails, consultez [Objet Attributs d’utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object).

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
  ],
  "attachments": [
    {
      "file_name" : "YourFileName",
      "url" : "https://exampleurl.com/YourFileName.pdf"
    }
  ]
}'
```

## Informations relatives à la réponse

Les réponses des points d'extrémité d'envoi de messages incluront le site `dispatch_id` afin de renvoyer à l'envoi du message. Le `dispatch_id` est l'ID de l'envoi de messages, un ID unique pour chaque transmission envoyée depuis Braze. Lorsque vous utilisez cet endpoint, vous recevez un seul `dispatch_id` pour un ensemble complet d’utilisateurs regroupés. Pour plus d'informations sur `dispatch_id`, consultez notre documentation sur le [comportement du Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

Si votre demande rencontre une erreur fatale, reportez-vous à la section [Erreurs et réponses]({{site.baseurl}}/api/errors/#fatal-errors) pour connaître le code d'erreur et sa description.

## Objet d'attributs pour les campagnes

Braze dispose d'un objet d'envoi de messages appelé `attributes` qui vous permettra d'ajouter, de créer ou de mettre à jour les attributs et les valeurs d'un utilisateur avant de lui envoyer une campagne déclenchée par l'API. En utilisant l’endpoint `campaign/trigger/send` car cet appel d'API traitera l'objet Attributs d’utilisateur avant de traiter et d'envoyer la campagne. Cela permet de minimiser le risque de problèmes causés par des [conditions de concurrence]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/).

{% alert tip %}
Vous recherchez la version Canvas de cet endpoint ? Consultez la rubrique [Envoi de messages canvas à l'aide de la réception/distribution déclenchée par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint).
{% endalert %}

{% endapi %}

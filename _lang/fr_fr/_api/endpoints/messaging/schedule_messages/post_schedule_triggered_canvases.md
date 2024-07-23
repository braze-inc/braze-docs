---
nav_title: "POST : Planifier des Canvas déclenchés par API"
article_title: "POST : Planifier des Canvas déclenchés par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Planifier des Canvas déclenchés par API."

---
{% api %}
# Planifier des Canvas déclenchés par API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/create
{% endapimethod %}

> Utilisez ce point de terminaison pour planifier des messages Canvas via une remise déclenchée par l’API, ce qui vous permet de décider quelle action doit déclencher l’envoi du message. 

Vous pouvez indiquer les `canvas_entry_properties` qui seront modélisées dans les messages envoyés dès les premières étapes du Canvas.

Notez que pour envoyer des messages avec cet endpoint, vous devez avoir un ID Canvas créé lorsque vous élaborez un []({{site.baseurl}}/api/identifier_types/#canvas-api-identifier)Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4bc75890-b807-405d-b226-5aca284e6b7d {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.trigger.schedule.create`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  // Including 'recipients' will send only to the provided user ids if they are in the campaign's segment
  "recipients": (optional, array of recipients object),
  // for any keys that conflict between these trigger properties and those in a Recipients Object, the value from the
  // Recipients Object will be used
  "audience": (optional, connected audience object) see connected audience,
  // Including 'audience' will only send to users in the audience
  // If 'recipients' and 'audience' are not provided and broadcast is not set to 'false',
  // the message will send to entire segment targeted by the Canvas
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted,
  "canvas_entry_properties": (optional, object) personalization key-value pairs for the first step for all users in this send; see trigger properties,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```

## Paramètres de demande

| Paramètre | Obligatoire | Type de données | Descriptif |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Obligatoire|Chaîne| Voir [Identifiant de canvas]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Facultatif | Tableau d’objets destinataires | Voir [l’objet recipients]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Facultatif | Objet d’audience connectée | Voir [l’audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Facultatif | Booléen | Vous devez définir `broadcast` sur « true » lorsque vous envoyez un message à un segment entier qui est ciblé par une campagne ou un canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, soyez prudent lors de la définition `broadcast: true`de , car le réglage involontaire de cet indicateur peut vous amener à envoyer votre message à un public plus large que prévu. |
| `canvas_entry_properties` | Facultatif | Objet | Paires clé-valeur de personnalisation pour tous les utilisateurs de cet envoi. Voir [Objet Propriétés d’entrée de canevas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object). |
| `schedule` | Obligatoire | Objet Planification | Voir [objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties": {}
    }
  ],
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
  "broadcast": false,
  "canvas_entry_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```

## Réponse

### Exemple de réponse réussie

```
Content-Type: application/json
Authorization: Bearer YOUR-API-KEY-HERE
{
{
    "dispatch_id": "dispatch_identifier",
    "schedule_id": "schedule_identifier",
    "message": "success"
}
```

{% endapi %}
---
nav_title: "POST : Planifier des messages de campagne déclenchés par API"
article_title: "POST : Planifier des messages de campagne déclenchés par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Braze Planifier des campagnes déclenchées par API."

---
{% api %}
# Planifier des campagnes déclenchées par API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/campaigns/trigger/schedule/create
{% endapimethod %}

Utilisez cet endpoint pour envoyer des messages de campagne crées sur le tableau de bord (jusqu’à 90 jours à l’avance) via une livraison déclenchée par API, ce qui vous permet de décider quelle action doit déclencher le message à envoyer. Vous pouvez indiquer les `trigger_properties` qui seront modélisés dans le message lui-même.

Notez que pour envoyer des messages avec cet endpoint, vous devez avoir un ID de campagne créé lorsque vous élaborez une [campagne déclenchée par API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b7e61de7-f2c2-49c9-9e46-b85a0aa01bba {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) voir Identifiant de campagne,
  "send_id": (optional, string) voir Identifiant d’envoi,
  // En incluant les « destinataires », les messages seront envoyés aux identifiants d’utilisateur fournis s’ils sont dans le segment de la campagne.
  "recipients": (optional, array of recipients object),
  // pour toute clé qui entre en conflit entre ces propriétés de déclencheur et celles dans un objet destinataire, la valeur de l’objet destinataire sera utilisée
  "audience": (optional, connected audience object) voir Audience connectée,
  // En incluant l’« audience », les messages seront uniquement envoyés aux utilisateurs de l’audience en question.
  // Si « Destinataires » et « Audience » ne sont pas fournis et que la diffusion n’est pas définie sur « faux ».,
  // le message sera envoyé au segment entier ciblé par la campagne
  "broadcast": (optional, boolean) voir diffusion ; défini par défaut sur « faux » le 31/8/17, doit être défini sur « vrai » si l’objet « destinataires » est absent,
  "trigger_properties": (optional, object) paire clé-valeur de personnalisation pour tous les utilisateurs de l’envoi ; voir les propriétés de déclencheur,
  "schedule": {
    "time": (required, datetime as ISO 8601 string) moment d’envoi du message (jusqu’à 90 jours dans le futur),
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  }
}
```
## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Requis|String| Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/)|
| `send_id` | Facultatif | String | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/). | 
| `recipients` | Facultatif | Tableau des objets de destinataire | Voir [Objet de destinataire]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `audience` | Facultatif | Objet Audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`broadcast`| Facultatif | Boolean | Voir [Diffusion]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `recipients` est omis, `broadcast` doit être défini sur Vrai. Cependant, faites attention lors de la configuration de `broadcast: true` car en configurant involontairement cet indicateur, vous pourriez envoyer votre message à une audience plus importante que prévue. |
| `trigger_properties` | Facultatif | Objet | Personnalisation des paires clé-valeur pour tous les utilisateurs de cet envoi. Voir [Propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). |
| `schedule` | Requis | Objet de planification | Voir [Objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "recipients": [
    {
      "user_alias": "example_alias",
      "external_user_id": "external_user_identifier",
      "trigger_properties": {}
    }
  ],
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "eye_color",
          "comparison": "égal à",
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
          "value": "abonné"
        }
      },
      {
        "last_used_app": {
          "comparison": "Ensuite…",
          "value": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "broadcast": false,
  "trigger_properties": {},
  "schedule": {
    "time": "",
    "in_local_time": false,
    "at_optimal_time": false
  }
}'
```


{% endapi %}

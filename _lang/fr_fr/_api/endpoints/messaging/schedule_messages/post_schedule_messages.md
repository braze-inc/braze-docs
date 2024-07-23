---
nav_title: "POST : Créer des messages planifiés"
article_title: "POST : Créer des messages planifiés"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer des messages planifiés."

---
{% api %}
# Créer des messages planifiés
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/schedule/create
{% endapimethod %}

> Utilise ce point de terminaison pour programmer l'envoi d'une campagne, d'un Canvas ou d'un autre message à une heure désignée et te fournit un identifiant pour référencer ce message pour les mises à jour. 

Si vous souhaitez cibler un segment, un enregistrement de votre demande sera stocké dans la [](https://dashboard.braze.com/app_settings/developer_console/activitylog/)Console de développement après l’envoi de tous les messages planifiés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `messages.schedule.create`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' category='message endpoints' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
  // Including 'segment_id' will send to members of that segment
  // Including 'external_user_ids' and/or 'user_aliases' will send to those users
  // Including both a Segment and users will send to the provided users if they are in the segment
  "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if users are not specified,
  "external_user_ids": (optional, array of strings) see external user identifier,
  "user_aliases": (optional, array of user alias object) see user alias,
  "audience": (optional, connected audience object) see connected audience,
  "segment_id": (optional, string) see segment identifier,
  "campaign_id": (optional, string) see campaign identifier,
  "send_id": (optional, string) see send identifier,
  "override_messaging_limits": (optional, bool) ignore frequency capping rules, defaults to false,
  "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
  "schedule": { 
    "time": (required, datetime as ISO 8601 string) time to send the message,
    "in_local_time": (optional, bool),
    "at_optimal_time": (optional, bool),
  },
  "messages": {
    "apple_push": (optional, apple push object),
    "android_push": (optional, android push object),
    "kindle_push": (optional, kindle/fireOS push object),
    "web_push": (optional, web push object),
    "email": (optional, email object),
    "webhook": (optional, webhook object),
    "content_card": (optional, content card object),
    "sms": (optional, SMS object)
  }
}
```

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
|`broadcast`| Facultatif | Booléen | Tu dois donner la valeur true à `broadcast` lorsque tu envoies un message à un segment entier ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, fais attention lorsque tu définis `broadcast: true`, car si tu définis ce drapeau sans le vouloir, tu risques d'envoyer ton message à un public plus large que prévu. |
| `external_user_ids` | Facultatif | Tableau de chaînes de caractères | Voir l'[identifiant de l'utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Facultatif | Tableau d'objets d'alias d'utilisateur | Voir [objet d'alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Facultatif | Objet d’audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Facultatif | Chaîne de caractères | Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Optionnel|Chaîne| Voir l'[identifiant de la campagne]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Facultatif | Tableau d'objets destinataires | Voir l'[objet destinataire]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `send_id` | Facultatif | Chaîne de caractères | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Facultatif | Booléen | Ignorer les limites de taux globales pour les campagnes, la valeur par défaut est false |
|`recipient_subscription_state`| Facultatif | Chaîne de caractères | Cette option permet d'envoyer des messages uniquement aux utilisateurs qui ont choisi de participer (`opted_in`), uniquement aux utilisateurs qui se sont abonnés ou qui ont choisi de participer (`subscribed`) ou à tous les utilisateurs, y compris les utilisateurs qui ne se sont pas abonnés (`all`). <br><br>Appliquer l’option `all` pour les utilisateurs est utile pour les e-mails transactionnels. La valeur par défaut est `subscribed`. |
| `schedule` | Requis | Objet de planification | Voir [objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Facultatif | Objet de messagerie | Voir les [objets de messagerie disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/schedule/create' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name" : "example_name",
    "alias_label" : "example_label"
  },
  "segment_id": "segment_identifiers",
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
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier",
  "override_messaging_limits": false,
  "recipient_subscription_state": "subscribed",
  "schedule": {
    "time": "",
    "in_local_time": true,
    "at_optimal_time": true
  },
  "messages": {
    "apple_push": (optional, Apple Push Object),
    "android_push": (optional, Android Push Object),
    "kindle_push": (optional, Kindle/FireOS Push Object),
    "web_push": (optional, Web Push Object),
    "email": (optional, Email object)
    "webhook": (optional, Webhook object)
    "content_card": (optional, Content Card Object)
  }
}'
```

## Réponse

### Exemple de réponse réussie

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}


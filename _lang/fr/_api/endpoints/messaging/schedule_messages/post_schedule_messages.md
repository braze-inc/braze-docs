---
nav_title: "POST : planifier les messages"
article_title: "POST : planifier les messages"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Planifier les messages."

---
{% api %}
# Créer des messages planifiés
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/messages/schedule/create
{% endapimethod %}

Utilisez cet endpoint pour planifier une campagne, un Canvas ou un autre message à envoyer à un moment donné (jusqu’à 90 jours à l’avance) et obtenir un identifiant permettant de référencer ce message pour les mises à jour. Si vous souhaitez cibler un segment, un enregistrement de votre demande sera stocké dans la [console du développeur (Developer Console)](https://dashboard.braze.com/app_settings/developer_console/activitylog/) après l’envoi de tous les messages planifiés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#25272fb8-bc39-41df-9a41-07ecfd76cb1d {% endapiref %}

## Limites de débit

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
    "time": (required, datetime as ISO 8601 string) time to send the message, (up to 90 days in the future),
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

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Facultatif | Boolean | Vous devez définir `broadcast` sur « true » lorsque vous envoyez un message à un segment entier qui est ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, faites attention lors de la configuration de `broadcast: true`, car en configurant involontairement cet indicateur, vous pourriez envoyer votre message à une audience plus importante que prévue. |
| `external_user_ids` | Facultatif | Tableau de chaînes de caractères | Voir [Identifiant utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Facultatif | Tableau des objets Alias utilisateur | Voir [Objet Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Facultatif | Objet Audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Facultatif | Chaîne de caractères | Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Optional|String| Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Facultatif | Tableau des objets Destinataires | Voir [Objet Destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `send_id` | Facultatif | Chaîne de caractères | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/). | 
| `override_messaging_limits` | Facultatif | Boolean | Ignorer les limites de débit globales pour les campagnes, défini sur Faux par défaut |
|`recipient_subscription_state`| Facultatif | Chaîne de caractères | Utilisez cette option pour envoyer des messages uniquement aux utilisateurs qui ont confirmé l’abonnement (`opted_in`), aux utilisateurs qui ont souscrit à ou confirmé l’abonnement (`subscribed`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`all`). <br><br>Appliquer l’option `all` pour les utilisateurs est utile pour les e-mails transactionnels. Par défaut, `subscribed`. |
| `schedule` | Requis | Objet Planification | Voir [Objet Planification]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Facultatif | Objet Messagerie | Voir [Objets Messagerie disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
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

```json
{
    "dispatch_id": (string) the dispatch identifier,
    "schedule_id": (string) the schedule identifier,
    "message": "success"
}
```

{% endapi %}


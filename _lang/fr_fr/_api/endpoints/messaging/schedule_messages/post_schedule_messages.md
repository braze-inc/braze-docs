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

> Cet endpoint permet de planifier l'envoi d'une campagne, d'un Canvas ou d'un autre message à une heure donnée et fournit un identifiant permettant de référencer ce message pour les mises à jour.

Si vous ciblez un segment, un enregistrement de votre demande sera stocké dans la [console de développement](https://dashboard.braze.com/app_settings/developer_console/activitylog/) après l'envoi de tous les messages planifiés.

{% alert tip %}
Si vous souhaitez envoyer des messages immédiatement à des utilisateurs désignés, utilisez plutôt l' [endpoint`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages).
{% endalert %}

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
    "time": (required, datetime as ISO 8601 string) time to send the message in UTC,
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
|`broadcast`| Facultatif | Valeur booléenne | Vous devez définir `broadcast` sur « true » lorsque vous envoyez un message à un segment entier qui est ciblé par une campagne ou un Canvas. La valeur par défaut de ce paramètre est `false`. <br><br> Si `broadcast` est défini sur `true`, il n'est pas possible d'inclure une liste de destinataires. Toutefois, soyez prudent lorsque vous définissez `broadcast: true`, car en activant involontairement cet indicateur, vous risquez d'envoyer votre message à une audience plus large que prévu. |
| `external_user_ids` | Facultatif | Tableau de chaînes de caractères | Voir [identifiant d'utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
| `user_aliases` | Facultatif | Tableau des objets Alias utilisateur | Voir l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Facultatif | Objet Audience connectée | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Facultatif | Chaîne de caractères | Voir [identifiant de segmentation]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Facultatif|Chaîne de caractères| Voir [identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Facultatif | Chaîne de caractères | Voir [identifiant d'envoi]({{site.baseurl}}/api/identifier_types/). |
| `override_messaging_limits` | Facultatif | Valeur booléenne | Ignorer la limite de fréquence pour les campagnes, la valeur par défaut est false. |
|`recipient_subscription_state`| Facultatif | Chaîne de caractères | Utilisez cette option pour envoyer des messages uniquement aux utilisateurs qui ont confirmé l’abonnement (`opted_in`), aux utilisateurs qui ont souscrit à ou confirmé l’abonnement (`subscribed`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`all`). <br><br>Appliquer l’option `all` pour les utilisateurs est utile pour les e-mails transactionnels. Par défaut, `subscribed`. |
| `schedule` | Requis | Objet Planification | Voir [objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Facultatif | Objet Messagerie | Voir [les objets de messagerie disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

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

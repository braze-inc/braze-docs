---
nav_title: "POST : Envoyez des messages immédiatement en utilisant uniquement l'API"
article_title: "POST : Envoyez des messages immédiatement en utilisant uniquement l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'envoi de messages immédiatement à l'aide de l'API, uniquement l'endpoint Braze."

---
{% api %}
# Envoyez des messages immédiatement en utilisant uniquement l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> Utilisez cet endpoint pour envoyer des messages immédiats aux utilisateurs désignés à l'aide de l'API de Braze.

Si vous souhaitez cibler un segment, un enregistrement de votre requête sera stocké dans la [console de développement](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% multi_lang_include api/payload_size_alert.md %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `messages.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

## Corps de la demande

{% alert tip %}
Veillez à inclure des [objets de messages]({{site.baseurl}}/api/objects_filters/#messaging-objects) dans votre corps pour compléter vos demandes.
{% endalert %}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   // You will need to include at least one of 'segment_id', 'external_user_ids', and 'audience'
   // Including 'segment_id' will send to members of that segment
   // Including 'external_user_ids' and/or 'user_aliases' will send to those users
   // Including both will send to the provided users if they are in the segment
   "broadcast": (optional, boolean) see broadcast -- defaults to false on 8/31/17, must be set to true if no external_user_ids or aliases are provided,
   "external_user_ids": (optional, array of strings) see external user identifier,
   "user_aliases": (optional, array of user alias object) see user alias,
   "segment_id": (optional, string) see segment identifier,
   "audience": (optional, connected audience object) see connected audience,
   "campaign_id": (optional*, string) *required if you wish to track campaign stats (for example, sends, clicks, bounces, etc). see campaign identifier,
   "send_id": (optional, string) see send identifier,
   "override_frequency_capping": (optional, bool) ignore frequency_capping for campaigns, defaults to false,
   "recipient_subscription_state": (optional, string) use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed',
   "messages": {
     "android_push": (optional, android push object),
     "apple_push": (optional, apple push object),
     "content_card": (optional, content card object),
     "email": (optional, email object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "webhook": (optional, webhook object),
     "whats_app": (optional, WhatsApp object),
     "sms": (optional, SMS object)
   }
 }
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`broadcast`| Facultatif | Valeur booléenne | Vous devez définir `broadcast` sur « true » lorsque vous envoyez un message à un segment entier qui est ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, faites attention lors de la configuration de `broadcast: true` car en configurant involontairement cet indicateur, vous pourriez envoyer votre message à une audience plus importante que prévue. |
|`external_user_ids` | Facultatif | Tableau de chaînes de caractères | Voir [ID externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Facultatif | Tableau des objets Alias utilisateur| Voir l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Facultatif | Chaîne de caractères | Voir [identifiant de segmentation]({{site.baseurl}}/api/identifier_types/#segment-identifier). |
|`audience`| Facultatif | Objet Audience connectée | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| En option* | Chaîne de caractères | Pour plus d'informations, voir l'[identifiant de la campagne]({{site.baseurl}}/api/identifier_types/#campaign-identifier/). <br><br>\*Nécessaire si vous souhaitez suivre les indicateurs de la campagne (tels que les _envois_, les _clics_ ou les _rebonds_) sur le tableau de bord de Braze. |
|`send_id`| Facultatif | Chaîne de caractères | Voir [identifiant d'envoi]({{site.baseurl}}/api/identifier_types/#send-identifier). |
|`override_frequency_capping`| Facultatif | Valeur booléenne | Ignorez `frequency_capping` pour les campagnes, la valeur par défaut est `false`. |
|`recipient_subscription_state`| Facultatif | Chaîne de caractères | Utilisez cette option pour envoyer des messages uniquement aux utilisateurs qui ont confirmé l’abonnement (`opted_in`), aux utilisateurs qui ont souscrit à ou confirmé l’abonnement (`subscribed`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`all`). <br><br>Appliquer l’option `all` pour les utilisateurs est utile pour les e-mails transactionnels. Par défaut, `subscribed`. |
|`messages`| Facultatif | Objets Messagerie | Voir les [objets d'envoi de messages disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/messages/send' \
--data-raw '{
  "broadcast": "false",
  "external_user_ids": "external_user_identifiers",
  "user_aliases": {
    "alias_name": "example_name",
    "alias_label": "example_label"
  },
  "segment_id": "segment_identifier",
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
  "override_frequency_capping": "false",
  "recipient_subscription_state": "all",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optional, Web Push Object)"
  }
}'
```

## Informations relatives à la réponse

Les réponses des endpoints d’envoi de messages incluront le `dispatch_id` du message pour y faire référence lors de l’envoi. Le `dispatch_id` est l’identifiant de la transmission du message, c’est un ID unique pour chaque « dispatch » envoyé par Braze. Pour plus d'informations, consultez [Comportement du Dispatch ID]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}

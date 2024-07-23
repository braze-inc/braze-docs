---
nav_title: "POST : Envoyer des messages immédiatement via API uniquement"
article_title: "POST : Envoyer des messages immédiatement via API uniquement"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Envoyer des messages immédiatement via API uniquement."

---
{% api %}
# Envoyer des messages immédiatement via API uniquement
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/messages/send
{% endapimethod %}

> Utilise ce point de terminaison pour envoyer des messages immédiats aux utilisateurs désignés via l'API de Braze. 

Veillez à inclure les objets Messagerie dans votre corps pour finaliser vos demandes.

Si vous souhaitez cibler un segment, un enregistrement de votre requête sera stocké dans la [console de développement](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez générer une clé API avec l’autorisation `messages.send`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message send endpoint' %}

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
     "apple_push": (optional, apple push object),
     "android_push": (optional, android push object),
     "kindle_push": (optional, kindle/fireOS push object),
     "web_push": (optional, web push object),
     "email": (optional, email object),
     "webhook": (optional, webhook object),
     "content_card": (optional, content card object),
     "sms": (optional, SMS object),
     "whats_app": (optional, WhatsApp object)
   }
 }
```

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
| --------- | ---------| --------- | ----------- |
|`broadcast`| Facultatif | Booléen | Tu dois donner la valeur true à `broadcast` lorsque tu envoies un message à un segment entier ciblé par une campagne ou un Canvas. Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `broadcast` est défini sur « true », une liste `recipients` ne peut pas être incluse. Cependant, faites attention lors de la configuration de `broadcast: true`car en configurant involontairement cet indicateur, vous pourriez envoyer votre message à une audience plus importante que prévue.
|`external_user_ids` | Facultatif | Tableau de chaînes de caractères | Voir l'[ID de l'utilisateur externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). |
|`user_aliases`| Facultatif | Tableau d'objets d'alias d'utilisateur| Voir l'[objet d'alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Facultatif | Chaîne de caractères | Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/). |
| `audience` | Facultatif | Objet d’audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Facultatif* | Chaîne de caractères | Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/) pour plus d'informations. <br><br>\*Nécessaire si tu souhaites suivre les statistiques de la campagne (par exemple, les envois, les clics, les rebonds, etc.) sur le tableau de bord de Braze. |
|`send_id`| Facultatif | Chaîne de caractères | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/) |
|`override_frequency_capping`| Facultatif | Booléen | Ignorer `frequency_capping` pour les campagnes, la valeur par défaut est `false`. |
Utilisez cette option pour envoyer des messages uniquement aux utilisateurs qui ont confirmé l’abonnement (), aux utilisateurs qui ont souscrit à ou confirmé l’abonnement () ou à tous les utilisateurs, y compris les utilisateurs désabonnés (). <br><br>Appliquer l’option `all` pour les utilisateurs est utile pour les e-mails transactionnels. La valeur par défaut est `subscribed`. |
|`messages`| Facultatif | Objets de messagerie | Voir les [objets de messagerie disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

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


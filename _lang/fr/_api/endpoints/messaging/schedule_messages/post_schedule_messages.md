---
nav_title: "POST : Planifier les messages"
article_title: "POST : Planifier les messages"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Planifier des messages."

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
  // Vous devrez inclure au moins un « segment_id », « external_user_ids » et une « audience ».
  // En incluant « segment_id » les messages seront envoyés aux membres de ce segment.
  // En incluant « external_user_ids » et/ou « user_aliases », les messages seront envoyés à ces utilisateurs.
  // En incluant un segment et des utilisateurs, les messages seront envoyés aux utilisateurs stipulés s’ils sont dans le segment.
  "broadcast": (optional, boolean) voir Diffusion ; défini par défaut sur « faux » le 31/8/17, doit être défini sur « vrai » si les utilisateurs ne sont pas spécifiés,
  "external_user_ids": (optional, array of strings) voir Identifiant utilisateur externe.,
  "user_aliases": (optional, array of user alias object) voir Alias d’utilisateur,
  "audience": (optional, connected audience object) voir Audience connectée,
  "segment_id": (optional, string) voir Identifiant de segment,
  "campaign_id": (optional, string) voir Identifiant de campagne,
  "send_id": (optional, string) voir Identifiant d’envoi,
  "override_messaging_limits": (optional, bool) ignore les règles de limite de fréquence, définir par défaut sur « faux »,
  "recipient_subscription_state": (optional, string) utilisez-le pour envoyer des messages uniquement aux utilisateurs qui se sont abonnés (« opted_in »), uniquement aux utilisateurs abonnés ou qui se sont inscrits (« subscribed ») ou à tous les utilisateurs, y compris aux utilisateurs désinscrits (« all »), cette dernière option étant utile pour l’envoi de messages de transaction par e-mail. Défini par défaut sur « subscribed » (inscrit),
  "schedule": { 
    "time": (required, datetime as ISO 8601 string) moment d’envoi du message (jusqu’à 90 jours dans le futur),
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
|`broadcast`| Facultatif | Boolean | Voir [Diffusion]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `recipients` est omis, `broadcast` doit être défini sur Vrai. Cependant, faites attention lors de la configuration de `broadcast: true` car en configurant involontairement cet indicateur, vous pourriez envoyer votre message à une audience plus importante que prévue. |
| `external_user_ids` | Facultatif | Array of strings | Voir [Identifiant utilisateur externe]({{site.baseurl}}/api/parameters/#external-user-id). |
| `user_aliases` | Facultatif | Tableau des objets alias utilisateur | Voir [Objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
| `audience` | Facultatif | Objet Audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
| `segment_id` | Facultatif | String | Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/). |
| `campaign_id`|Facultatif|String| Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/). |
| `recipients` | Facultatif | Tableau des objets de destinataire | Voir [Objet de destinataire]({{site.baseurl}}/api/objects_filters/recipient_object/). |
| `send_id` | Facultatif | String | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/). | 
| `override_messaging_limits` | Facultatif | Boolean | Ignorer les limites de débit globales pour les campagnes, défini sur Faux par défaut |
|`recipient_subscription_state`| Facultatif | String | Utilisez cette option pour envoyer des messages uniquement aux utilisateurs qui ont confirmé l’abonnement (`opted_in`), aux utilisateurs qui ont souscrit à ou confirmé l’abonnement (`subscribed`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`all`). <br><br>Appliquer l’option `all` les utilisateurs est utile pour les e-mails transactionnels. Par défaut, `Abonné`. |
| `schedule` | Requis | Objet de planification | Voir [Objet de planification]({{site.baseurl}}/api/objects_filters/schedule_object/) |
| `messages` | Facultatif | Objet de messagerie | Voir [Objets de messagerie disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
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
    "dispatch_id": (string) l’identifiant d’expédition,
    "schedule_id": (string) l’identifiant de planification,
    "message": "success"
}
```

{% endapi %}


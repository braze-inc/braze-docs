---
nav_title: "POST : Envoyer des messages immédiatement via API uniquement"
article_title: "POST : Envoyer des messages immédiatement via API uniquement"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Envoyer des messages immédiatement."

---
{% api %}
# Envoi immédiat des messages via API uniquement
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %} 
/messages/send
{% endapimethod %}

Utilisez cet endpoint pour envoyer des messages instantanés et ad hoc aux utilisateurs désignés via l’API Braze. Veillez à inclure les objets de messagerie dans votre corps pour finaliser vos demandes.

Si vous souhaitez cibler un segment, un enregistrement de votre demande sera stocké dans la [Developer Console (Console du développeur)](https://dashboard.braze.com/app_settings/developer_console/activitylog/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#946cb701-96e3-48d7-868c-f079785b6d24 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

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
   // En incluant les deux, les messages seront envoyés aux utilisateurs stipulés s’ils sont dans le segment.
   "broadcast": (optional, boolean) voir diffusion ; défini par défaut sur « faux » le 31/8/17, doit être défini sur « vrai » si aucun external_user_ids ou alias n’est fourni,
   "external_user_ids": (optional, array of strings) voir Identifiant utilisateur externe.,
   "user_aliases": (optional, array of user alias object) voir Alias d’utilisateur,
   "segment_id": (optional, string) voir Identifiant de segment,
   "audience": (optional, connected audience object) voir Audience connectée,
   "campaign_id": (optional*, string) *obligatoire si vous désirez suivre les statistiques d’une campagne (par ex., envois, clics, rebonds, etc.). Voir identifiant de campagne.,
   "send_id": (optional, string) voir Identifiant d’envoi,
   "override_frequency_capping": (optional, bool) ignorer frequency_capping pour les campagnes, défini sur « faux » par défaut.,
   "recipient_subscription_state": (optional, string) utilisez-le pour envoyer des messages uniquement aux utilisateurs qui se sont abonnés (« opted_in »), uniquement aux utilisateurs abonnés ou qui se sont inscrits (« subscribed ») ou à tous les utilisateurs, y compris aux utilisateurs désinscrits (« all »), cette dernière option étant utile pour l’envoi de messages de transaction par e-mail. Défini par défaut sur « subscribed » (inscrit),
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
|`broadcast`| Facultatif | Boolean | Voir [Diffusion]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre est défini sur Faux par défaut (au 31 août 2017). <br><br> Si `recipients` est omis, `broadcast` doit être défini sur Vrai. Cependant, faites attention lors de la configuration de `broadcast: true` car en configurant involontairement cet indicateur, vous pourriez envoyer votre campagne ou Canvas à une audience plus importante que prévue. |
|`external_user_ids` | Facultatif | Array of strings | Voir [ID utilisateur externe]({{site.baseurl}}/api/parameters/#external-user-id). |
|`user_aliases`| Facultatif | Tableau des objets alias utilisateur| Voir [Objet alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/). |
|`segment_id `| Facultatif | String | Voir [Identifiant de segment]({{site.baseurl}}/api/identifier_types/). |
|`audience`| Facultatif | Objet Audience connectée | Voir [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
|`campaign_id`| Facultatif* | String | Voir [Identifiant de campagne]({{site.baseurl}}/api/identifier_types/) pour plus d’informations. <br><br>*Obligatoire si vous souhaitez suivre les statistiques de campagne (par ex., le nombre d’envois, de clics, de rebonds, etc.) sur le tableau de bord de Braze. |
|`send_id`| Facultatif | String | Voir [Identifiant d’envoi]({{site.baseurl}}/api/identifier_types/) |
|`override_frequency_capping`| Facultatif | Boolean | Ignorer frequency_capping pour les campagnes, défini sur Faux par défaut. |
|`recipient_subscription_state`| Facultatif | String | Utilisez cette option pour envoyer des messages uniquement aux utilisateurs qui ont confirmé l’abonnement (`opted_in`), aux utilisateurs qui ont souscrit à ou confirmé l’abonnement (`subscribed`) ou à tous les utilisateurs, y compris les utilisateurs désabonnés (`all`). <br><br>Appliquer l’option `all` les utilisateurs est utile pour les e-mails transactionnels. Par défaut, `Abonné`. |
|`messages`| Facultatif | Objets de messagerie | Voir [Objets de messagerie disponibles]({{site.baseurl}}/api/objects_filters/#messaging-objects). |
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
  "recipient_subscription_state": "tous",
  "messages": {
    "android_push": "(optional, Android Push Object)",
    "apple_push": "(optional, Apple Push Object)",
    "content_card": "(optional, Content Card Object)",
    "email": "(optional, Email Object)",
    "kindle_push": "(optional, Kindle/FireOS Push Object)",
    "web_push": "(optionnel, objet de notification push Web)"
  }
}'
```

## Informations relatives à la réponse

Les réponses des endpoints d’envoi de messages incluront le `dispatch_id` du message pour y faire référence lors de l’envoi. Le `dispatch_id` est l’ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Pour plus d'informations, consultez [Comportement de l'ID de distribution]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

{% endapi %}


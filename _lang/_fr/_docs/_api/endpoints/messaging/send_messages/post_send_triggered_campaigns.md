---
nav_title: "POST: Envoyer des messages de campagne via la distribution déclenchée par l'API"
article_title: "POST: Envoyer des messages de campagne via la distribution déclenchée par l'API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur l'envoi de messages de campagne via le point de terminaison de la livraison Braze déclenché par l'API."
---

{% api %}
# Envoi de messages de campagne via une livraison déclenchée par l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/campaigns/trigger/send
{% endapimethod %}

La livraison déclenchée par l'API vous permet d'héberger le contenu des messages dans le tableau de bord Braze tout en dictant quand un message est envoyé, et à qui via votre API.

Le point de terminaison d'envoi vous permet d'envoyer immédiatement des messages ad hoc à des utilisateurs désignés. Si vous visez un segment, un enregistrement de votre requête sera stocké dans la [Console développeur](https://dashboard.braze.com/app_settings/developer_console/activitylog/). Veuillez noter que pour envoyer des messages avec ce terminal, vous devez avoir un ID de campagne créé lorsque vous construisez une [campagne déclenchée par l'API]({{site.baseurl}}/api/api_campaigns/).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aef185ae-f591-452a-93a9-61d4bc023b05 {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (requis, chaîne) voir l'identifiant de la campagne,
  "send_id": (optionnel, chaîne) voir l'identifiant d'envoi,
  "trigger_properties": (optionnel, objet) personnalisation paires clé-valeur qui s'appliqueront à tous les utilisateurs de cette requête,
  "broadcast": (optionnel, boolean) see broadcast -- false par défaut sur 8/31/17, doit être défini à true si "destinataires" est omis,
  "audience": (optionnel, objet auditif connecté) voir le public connecté,
  // Inclure 'audience' n'enverra aux utilisateurs que dans l'auditoire
  "destinataires": (optionnel, tableau; si non fourni et que la diffusion n'est pas définie à `false`, message enverra à tout le segment ciblé par la campagne)
    [{
      // "external_user_id" ou "user_alias" est requis. Les requêtes ne doivent spécifier qu'une seule fois.
      "user_alias": (optionnel, objet alias utilisateur) alias de l'utilisateur pour recevoir le message,
      "external_user_id": (optionnel, string) identificateur externe de l'utilisateur à recevoir le message,
      "trigger_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à cet utilisateur (ces paires clé-valeur remplaceront toutes les clés qui entrent en conflit avec trigger_properties ci-dessus),
      "send_to_existing_only": (optionnel, booléen) par défaut à true, ne peut pas être utilisé avec les alias de l'utilisateur ; si défini à `false`, un objet d'attributs doit également être inclus,
      "attributs": (optionnel, objet) les champs dans l'objet attributs créeront ou mettront à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié avant l'envoi du message et les valeurs existantes seront écrasées
    }]
}
```

## Paramètres de la requête

| Paramètre                      | Requis    | Type de données       | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------ | --------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `campaign_id`                  | Requis    | Chaîne de caractères  | Voir [l'identifiant de la campagne]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                        |
| `id_expéditeur`                | Optionnel | Chaîne de caractères  | Voir [l'identifiant d'envoi]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                               |
| `format@@0 trigger_properties` | Optionnel | Objet                 | Voir [les propriétés du déclencheur]({{site.baseurl}}/api/objects_filters/trigger_properties_object/). Paires clé-valeur de personnalisation qui s'appliqueront à tous les utilisateurs de cette requête.                                                                                                                                                                                                                           |
| `Diffusion`                    | Optionnel | Boolean               | Voir la diffusion [de]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre par défaut est false (à partir du 31 août 2017). <br><br> Si `destinataires` est omis, `envoyer à tous` doit être défini à vrai. Cependant, faites preuve de prudence lorsque vous définissez `broadcast: true`, comme paramétrage involontaire de ce drapeau peut vous faire envoyer votre campagne à un public plus grand que prévu. |
| `public`                       | Optionnel | Objet public connecté | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/).                                                                                                                                                                                                                                                                                                                                                |
| `Destinataires`                | Optionnel | Tableau               | Voir l'objet [destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/). Si non fourni et `broadcast` est défini à true, le message enverra à l'ensemble du segment ciblé par la campagne.                                                                                                                                                                                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Demander des composants
- [Identifiant de la campagne]({{site.baseurl}}/api/identifier_types/)
- [Envoyer l'identifiant]({{site.baseurl}}/api/identifier_types/)
- [Diffusion]({{site.baseurl}}/api/parameters/#broadcast)
- [Audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/)
- [Destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/)
- [Objet Alias de l'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/)
- [Objet Attribut Utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/)
- [Paramètres API]({{site.baseurl}}/api/parameters) <br><br> La table de destinataires peut contenir jusqu'à 50 objets, avec chaque objet contenant une seule chaîne `external_user_id` et `trigger_properties` objet. <br><br> Lorsque `send_to_existing_only` est `vrai`, Braze n'enverra le message qu'aux utilisateurs existants. Cependant, ce drapeau ne peut pas être utilisé avec les alias utilisateurs. Quand `send_to_existing_only` est `false` et qu'un utilisateur avec l'identifiant `donné n'existe pas,` Braze créera un utilisateur avec l' `id` et les attributs avant d'envoyer le message.

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/campaigns/trigger/send' \
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
          "comparaison": "égal",
          "valeur": "bleu"
        }
      },
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_foods",
          "comparaison": "includes_valeur",
          "valeur": "pizza"
        }
      },
      {
        "OU": [
          {
            "custom_attribute": {
              "custom_attribute_name": "last_purchase_time",
              "comparaison": "less_than_x_days_ago",
              "valeur": 2
            }
          },
          {
            "push_subscription_status": {
              "comparison": "is",
              "valeur": "opted_in"
            }
          }
        ]
      },
      {
        "email_subscription_status": {
          "comparison": "is_not",
          "valeur": "abonné"
        }
      },
      {
        "last_used_app": {
          "comparison": "after",
          "valeur": "2019-07-22T13:17:55+0000"
        }
      }
    ]
  },
  "destinataires": [{
    "user_alias": {
      "alias_name" : "exemple_name",
      "alias_label" : "example_label"
    },
  "external_user_id": "external_user_identifier",
  "trigger_properties": "",
  "send_to_existing_only": true,
    "attributes": {
        "prénom" : "Alex"
    }
  }]
}'
```

## Détails de la réponse
Les réponses aux points de terminaison du message incluront le message `dispatch_id` pour être référencé à l'envoi du message. Le `dispatch_id` est l'id de l'envoi de message (id unique pour chaque « transmission» envoyée depuis la plate-forme Braze). Pour plus d'informations sur `dispatch_id` , consultez notre [documentation]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

## Créer un point de terminaison d'envoi

__Utilisation de l'objet Attributes dans les campagnes__

Braze a un objet de messagerie appelé `Attributs` qui vous permettra d'ajouter, de créer, ou mettez à jour les attributs et les valeurs d'un utilisateur avant de leur envoyer une campagne déclenchée par l'API en utilisant le point de terminaison `campagne/déclencher/envoyer` car cet appel à l'API traitera l'objet Attributs utilisateur avant qu'il ne traite et n'envoie la campagne. Cela permet de minimiser le risque de problèmes causés par les [conditions de course]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert important %}
À la recherche de créer un point d’extrémité pour les toiles ? Consultez la documentation [ici]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#create-send-endpoint).
{% endalert %}

{% endapi %}
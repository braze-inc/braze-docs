---
nav_title: "POST: Envoyer des messages sur Canvas via API-Triggered Delivery"
article_title: "POST: Envoyer des messages sur Canvas via API-Triggered Delivery"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur l'envoi de messages Canvas via le point de terminaison de la livraison Braze déclenchée par l'API."
---

{% api %}
# Envoi de messages sur Canvas via une livraison déclenchée par l'API
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/fr/canvas/trigger/send
{% endapimethod %}

La distribution déclenchée par l'API vous permet d'héberger le contenu des messages dans le tableau de bord Braze tout en dictant quand un message est envoyé, et à qui via votre API.

Ce point de terminaison vous permet d'envoyer des messages Canvas via une livraison déclenchée par API, vous permettant de décider quelle action doit déclencher le message à envoyer. Veuillez noter que pour envoyer des messages avec ce terminal, vous devez avoir un identifiant Canvase, créé lorsque vous construisez un [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c9a8a5fe-a101-4755-99f2-73aa8fc146fe {% endapiref %}

## Limite de taux

{% include rate_limits.md endpoint='send endpoints' category='message endpoints' %}

## Corps de la requête

```
Type de contenu : application/json
Autorisation : Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (requis, chaîne) voir Identifiant Canvas,
  "canvas_entry_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à tous les utilisateurs de cette requête,
  "broadcast": (optionnel, booléen) voir Broadcast -- false par défaut sur 8/31/17, doit être défini à true si `recipients` est omis,
  "audience": (optionnel, objet public connecté) voir le public connecté,
  // Inclure 'audience' n'enverra aux utilisateurs que dans l'auditoire
  "destinataires": (optionnel, tableau; si non fourni et diffusé n'est pas défini à 'false', sera envoyé à l'ensemble du segment ciblé par le Canvas)
    [{
      // "external_user_id" ou "user_alias" est requis. Les requêtes ne doivent spécifier qu'une seule fois.
      "user_alias": (optionnel, objet alias utilisateur) alias de l'utilisateur pour recevoir le message,
      "external_user_id": (optionnel, string) identificateur externe de l'utilisateur à recevoir le message,
      "canvas_entry_properties": (optionnel, objet) la personnalisation des paires clé-valeur qui s'appliqueront à cet utilisateur (ces paires clé-valeur remplaceront toutes les clés qui entrent en conflit avec `canvas_entry_properties` ci-dessus)
      "send_to_existing_only": (optionnel, booléen) par défaut à true, ne peut pas être utilisé avec les alias d'utilisateurs
      "attributs": (optionnel, objet) les champs dans l'objet attributs créeront ou mettront à jour un attribut de ce nom avec la valeur donnée sur le profil utilisateur spécifié avant l'envoi du message et les valeurs existantes seront écrasées
    }],
...
}
```

## Paramètres de la requête

| Paramètre                | Requis    | Type de données       | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | --------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_toile`               | Requis    | Chaîne de caractères  | Voir [identificateur de toile]({{site.baseurl}}/api/identifier_types/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Propriétés de la toile` | Optionnel | Objet                 | Voir [les propriétés d'entrée du canevas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/). Paires clé-valeur de personnalisation qui s'appliqueront à tous les utilisateurs de cette requête.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Diffusion`              | Optionnel | Boolean               | Voir la diffusion [de]({{site.baseurl}}/api/parameters/#broadcast). Ce paramètre par défaut est false (à partir du 31 août 2017). <br><br> Si `destinataires` est omis, `envoyer à tous` doit être défini à vrai. Cependant, faites preuve de prudence lorsque vous définissez `broadcast: true`, comme paramétrage involontaire de ce drapeau peut vous faire envoyer votre Canvas à un public plus grand que prévu.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `public`                 | Optionnel | Objet public connecté | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `Destinataires`          | Optionnel | Tableau               | Voir l'objet [destinataires]({{site.baseurl}}/api/objects_filters/recipient_object/). Si non fourni et `broadcast` est défini à true, le message enverra à l'ensemble du segment ciblé par le Canvas.<br><br> Le tableau `destinataires` peut contenir jusqu'à 50 objets, avec chaque objet contenant un seul objet `external_user_id` chaîne et `canvas_entry_properties`. Un `external_user_id` ou `user_alias` est requis pour cet appel. Les requêtes ne doivent spécifier qu'une seule fois. <br><br> Quand `send_to_existing_only` est `vrai`, Braze enverra uniquement le message aux utilisateurs existants, mais ce drapeau ne peut pas être utilisé avec les alias de l'utilisateur. Quand `send_to_existing_only` est `false` et qu'un utilisateur avec l'identifiant `donné n'existe pas,` Braze créera un utilisateur avec cet ID et les attributs avant d'envoyer le message. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Les clients qui utilisent l'API pour les appels de serveur à serveur peuvent avoir besoin de mettre en liste blanche l'URL de l'API appropriée s'ils sont derrière un pare-feu.

{% alert note %}
Si vous incluez à la fois des utilisateurs spécifiques dans votre appel API et un segment cible dans le tableau de bord, le message enverra spécifiquement aux profils d'utilisateurs qui sont à la fois dans l'appel API et qualifiés pour les filtres de segments.
{% endalert %}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze. om/canvas/trigger/send' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "canvas_entry_properties": {"product_name" : "shoes", "product_price" : 79. 9},
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
    "external_user_id": "user_identifier",
    "trigger_properties": "",
    "canvas_entry_properties": "",
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

__Utilisation de l'objet Attributes dans Canvas__

Braze a un objet de messagerie appelé `Attributs` qui vous permet d'ajouter, de créer, ou mettre à jour les attributs et les valeurs d'un utilisateur avant de leur envoyer une Canvas déclenchée par l'API en utilisant le point de terminaison `canvas/trigger/send` car cet appel API traitera l'objet Attribut Utilisateur avant qu'il ne traite et envoie le Canvas. Cela permet de minimiser le risque de problèmes causés par les [conditions de course]({{site.baseurl}}/help/best_practices/race_conditions/).

{% alert important %}
Vous recherchez Create Send Endpoint pour les Campagnes ? Consultez la documentation [ici]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#create-send-endpoint).
{% endalert %}

{% endapi %}


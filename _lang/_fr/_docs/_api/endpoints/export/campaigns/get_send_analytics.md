---
nav_title: "GET : Envoyer des analyses"
article_title: "GET : Envoyer des analyses"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: Référence
description: "Cet article décrit les détails sur les statistiques quotidiennes de la campagne de Braze par le point de terminaison Envoyer l'ID."
---

{% api %}
# Envoyer le point de terminaison analytique
{% apimethod get %}
/fr/sends/data_series
{% endapimethod %}

Ce point de terminaison vous permet de récupérer une série quotidienne de statistiques différentes pour un `send_id` suivi. Les magasins Braze envoient des analytiques pendant 14 jours après l'envoi.

Les conversions de campagne seront attribuées à l'identifiant d'envoi le plus récent qu'un utilisateur a reçu de la campagne.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Paramètres de la requête

| Paramètre        | Requis    | Type de données                                                                | Libellé                                                                                                                    |
| ---------------- | --------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| `campaign_id`    | Requis    | Chaîne de caractères                                                           | Voir [l'identifiant API de la campagne]({{site.baseurl}}/api/identifier_types/).                                           |
| `id_expéditeur`  | Requis    | Chaîne de caractères                                                           | Voir [Envoyer l'identifiant API]({{site.baseurl}}/api/identifier_types/).                                                  |
| `Longueur`       | Requis    | Nombre entier                                                                  | Nombre maximum de jours avant `ending_at` pour inclure dans la série retournée. Doit être compris entre 1 et 100 (inclus). |
| `finalisation_à` | Optionnel | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) chaîne) | Date à laquelle la série de données doit se terminer. Par défaut, l'heure de la requête.                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer VOTRE REST-API-KEY'
```
{% endraw %}

## Réponse

### Envoyer une réponse analytics endpoint API

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
            "variation_name": (string) nom de variante,
            "envoyé": (int) le nombre d'envois,
            "livré": (int) le nombre de messages livrés avec succès,
            "non livré" : (int) le nombre de non livrés,
            "delivery_failed": (int) le nombre de rejetés,
            "direct_opens": (int) le nombre d'ouvertures directes,
            "total_opens": (int) le nombre total d'ouvertures,
            "bounces": (int) le nombre de bounces,
            "body_clicks": (int) le nombre de clics du corps,
            "recettes": (flottant) le nombre de dollars de revenus (USD),
            "unique_destinataires": (int) le nombre de destinataires uniques,
            "conversions": (int) le nombre de conversions,
            "conversions_by_send_time": (int) le nombre de conversions,
            "conversions1": (int, optionnel) le nombre de conversions pour le deuxième événement de conversion,
            "conversions1_by_send_time": (int, optional) the number of conversions for the second conversion event by send time,
            "conversions2": (int, optionnel) le nombre de conversions pour le troisième événement de conversion,
            "conversions2_by_send_time": (int, optional) the number of conversions for the third conversion event by send time,
            "conversions3": (int, optionnel) le nombre de conversions pour l'événement de quatrième conversion,
            "conversions3_by_send_time": (int, optional) the number of conversions for the fourth conversion event by send time
          }
        ]
      },
      "conversions_by_send_time": 0,
      "conversions1_by_send_time": 0,
      "conversions2_by_send_time": 0,
      "conversions3_by_send_time": 0,
      "conversions": 0,
      "conversions1": 0,
      "conversions2": 0,
      "conversions3": 0,
      "unique_destinataires": 1,
      "revenus": 0
    }
  ],
  "message": "success"
}
```
{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, visitez notre article de dépannage [ici]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

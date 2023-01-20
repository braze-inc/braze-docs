---
nav_title: "GET : Envoyer des analyses"
article_title: "GET : Envoyer des analyses"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Statistiques quotidiennes de campagne par ID d’envoi de Braze."

---
{% api %}
# Endpoint Envoyer des analyses
{% apimethod get %}
/sends/data_series
{% endapimethod %}

Utilisez cet endpoint pour récupérer une série quotidienne de diverses statistiques pour un `send_id` suivi. Braze stocke les envois d’analyse pendant 14 jours après l’envoi.

Les conversions de campagne seront attribuées à l’ID d’envoi le plus récent qu’un utilisateur donné a reçu de la campagne.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#76f822a8-a13b-4bfb-b20e-72b5013dfe86 {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- |------------ |
| `campaign_id` | Requis | String | Voir [Identifiant API de campagne]({{site.baseurl}}/api/identifier_types/). |
| `send_id` | Requis | String | Voir [Identifiant Send API (API d’envoi)]({{site.baseurl}}/api/identifier_types/). .|
| `length` | Requis | Integer | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l’heure de la demande. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande 
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sends/data_series?campaign_id={{campaign_identifier}}&send_id={{send_identifier}}&length=30&ending_at=2014-12-10T23:59:59-05:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

### Réponse API de l’endpoint Envoyer des analyses

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
            "variation_name": (string) nom de la variation,
            "sent": (int) le nombre d’envois,
            "delivered": (int) le nombre de messages livrés avec succès,
            "undelivered": (int) le nombre de messages qui n’ont pas été livrés,
            "delivery_failed": (int) le nombre de messages rejetés,
            "direct_opens": (int) le nombre d’ouvertures directes,
            "total_opens": (int) le nombre total d’ouvertures,
            "bounces": (int) le nombre de rebonds,
            "body_clicks": (int) le nombre de clics sur le corps,
            "revenue": (float) le nombre de dollars de revenus (USD),
            "unique_recipients": (int) le nombre de destinataires uniques,
            "conversions": (int) le nombre de conversions,
            "conversions_by_send_time": (int) le nombre de conversions attribuées à la date à laquelle la campagne a été envoyée,
            "conversions1": (optional, int) le décompte de conversions pour le deuxième événement de conversion,
            "conversions1_by_send_time": (optional, int) le décompte de conversions pour le deuxième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
            "conversions2": (optional, int) le décompte de conversions pour le troisième événement de conversion,
            "conversions2_by_send_time": (optional, int) le décompte de conversions pour le troisième événement de conversion attribué à la date à laquelle la campagne a été envoyée,
            "conversions3": (optional, int) le décompte de conversions pour le quatrième événement de conversion,
            "conversions3_by_send_time": (optional, int) le décompte de conversions pour le quatrième événement de conversion attribué à la date à laquelle la campagne a été envoyée
          }
        ]
      },
      "conversions_by_send_time": (optional, int),
      "conversions1_by_send_time": (optional, int),
      "conversions2_by_send_time": (optional, int),
      "conversions3_by_send_time": (optional, int),
      "conversions": (int),
      "conversions1": (optional, int),
      "conversions2": (optional, int),
      "conversions3": (optional, int),
      "unique_recipients": (int),
      "revenue": (optional, float)
    }
  ],
  "message": "réussite"
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)..
{% endalert %}

{% endapi %}

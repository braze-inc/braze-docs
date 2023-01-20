---
nav_title: "GET : Résumé de l’analyse des données de Canvas"
article_title: "GET : Résumé de l’analyse des données de Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Analyse globale des données de Canvas."

---
{% api %}
# Endpoint du résumé des données de Canvas
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

Utilisez cet endpoint pour exporter des cumuls de données de série temporelles pour un Canvas, fournissant ainsi un résumé concis des résultats de Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Requis | String | Voir [Identifiant API Canvas]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Requis | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l’exportation de données doit se terminer. Par défaut, l’heure de la demande. |
| `starting_at` | Facultatif* | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l’exportation de données doit commencer. <br><br>* `length` ou `starting_at` est nécessaire. |
| `length` | Facultatif* | String | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 14 (inclus). <br><br>* `length` ou `starting_at` est nécessaire. |
| `include_variant_breakdown` | Facultatif | Boolean | S’il faut inclure ou non des statistiques de variante (par défaut sur Faux).  |
| `include_step_breakdown`    | Facultatif | Boolean | S’il faut inclure ou non des statistiques d’étape (par défaut sur Faux). |
| `include_deleted_step_data` | Facultatif | Boolean | S’il faut inclure ou non des statistiques d’étape pour les étapes supprimées (par défaut sur Faux). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) le nom du Canvas,
    "total_stats": {
      "revenue": (float) le nombre de dollars de revenus (USD),
      "conversions": (int) le nombre de conversions,
      "conversions_by_entry_time": (int) le décompte de conversions pour l’événement de conversion par date d’entrée,
      "entries": (int) le nombre d’entrées
    },
    "variant_stats": (facultatif) {
      "00000000-0000-0000-0000-0000000000000": (string) l’identifiant API pour la variante {
        "name": (string) le nom de la variante,
        "revenue": (float) le nombre de dollars de revenus (USD),
        "conversions": (int) le nombre de conversions,
        "entries": (int) le nombre d’entrées
      },
      ... (plus de variantes)
    },
    "step_stats": (facultatif) {
      "00000000-0000-0000-0000-0000000000000": (string) l’identifiant API pour l’étape {
        "name": (string) le nom de l’étape,
        "revenue": (float) le nombre de dollars de revenus (USD),
        "conversions": (int) le nombre de conversions,
        "conversions_by_entry_time": (int) le décompte de conversions pour l’événement de conversion par date d’entrée,
        "messages": {
          "android_push": (nom du canal) [
            {
              "sent": (int) le nombre d’envois,
              "opens": (int) le nombre d’ouvertures,
              "influenced_opens": (int) le nombre d’ouvertures influencées,
              "bounces": (int) le nombre de rebonds
              ... (plus de stats. pour le canal)
            }
          ],
          ... (plus de canaux)
        }
      },
      ... (plus d’étapes)
    }
  },
  "message": (required, string) le statut de l’exportation, renvoie « réussite » lorsqu’elle s’achève sans erreur
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/)..
{% endalert %}

{% endapi %}

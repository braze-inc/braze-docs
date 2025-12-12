---
nav_title: "GET : Exporter l’analyse des séries de données de Canvas"
article_title: "GET : Exportation de la série de données Canvas Analytics (si utilisée en tant qu'adjectif)"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter l’analyse des séries de données de Canvas."

---
{% api %}
# Exporter l’analyse des séries de données de Canvas
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

> Utilisez cet endpoint pour exporter des données de série temporelles pour un Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.data_series`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Requis | Chaîne de caractères | Voir l'[identifiant de l'API Canvas]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Requis | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l’exportation de données doit se terminer. Par défaut, l’heure de la demande. |
| `starting_at` | En option* | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l’exportation de données doit commencer. <br><br>\* L'adresse `length` ou `starting_at` est requise. |
| `length` | En option* | Chaîne de caractères | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 14 (inclus). <br><br>\* L'adresse `length` ou `starting_at` est requise. |
| `include_variant_breakdown` | Facultatif | Valeur booléenne | S’il faut inclure ou non des statistiques de variante (par défaut sur `false`).  |
| `include_step_breakdown` | Facultatif | Valeur booléenne | S’il faut inclure ou non des statistiques d’étape (par défaut sur `false`). |
| `include_deleted_step_data` | Facultatif | Valeur booléenne | S’il faut inclure ou non des statistiques d’étape pour les étapes supprimées (par défaut sur `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) the Canvas name,
    "stats": [
      {
        "time": (string) the date as ISO 8601 date,
        "total_stats": {
          "revenue": (float) the number of dollars of revenue (USD),
          "conversions": (int) the number of conversions,
          "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
          "entries": (int) the number of entries
        },
        "variant_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
            "name": (string) the name of variant,
            "revenue": (float) the number of dollars of revenue (USD),
            "conversions": (int) the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "entries": (int) the number of entries
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
            "name": (string) the name of step,
            "revenue": (float) the the number of dollars of revenue (USD),
            "conversions": (int) the the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "messages": {
              "email": [
                {
                  "sent": (int) the number of sends,
                  "opens": (int) the number of opens,
                  "unique_opens": (int) the number of unique opens,
                  "clicks": (int) the number of clicks
                  ... (more stats)
                }
              ],
              "sms" : [
                {
                  "sent": (int) the number of sends,
                  "sent_to_carrier" : (int) the number of messages sent to the carrier,
                  "delivered": (int)the number of delivered messages,
                  "rejected": (int) the number of rejected messages,
                  "delivery_failed": (int) the number of failed deliveries,
                  "clicks": (int) the number of clicks on shortened links,
                  "opt_out" : (int) the number of opt outs,
                  "help" : (int) the number of help messages received
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

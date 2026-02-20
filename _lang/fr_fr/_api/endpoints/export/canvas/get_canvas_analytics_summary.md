---
nav_title: "GET : Exporter le résumé analyse des données de Canvas"
article_title: "GET : Exporter les données du canvas Résumé des analyses"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article décrit le point de terminaison Export Canvas data summary analytics Braze."

---
{% api %}
# Exporter le résumé analyse des données de Canvas
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> Utilisez cet endpoint pour exporter des rollups de données de séries temporelles pour un Canvas, fournissant un résumé concis des résultats du Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `canvas.data_summary`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Requis | Chaîne de caractères | Voir l'[identifiant de l'API Canvas]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Requis | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date de fin de l'exportation des données. La valeur par défaut est l'heure de la demande. |
| `starting_at` | En option* | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date de début de l'exportation des données. <br><br>\* L'adresse `length` ou `starting_at` est requise. |
| `length` | En option* | Chaîne de caractères | Nombre maximal de jours avant `ending_at` inclus dans la série renvoyée. Doit être compris entre 1 et 14 (inclus). <br><br>\* L'adresse `length` ou `starting_at` est requise. |
| `include_variant_breakdown` | Facultatif | Valeur booléenne | Indique s'il faut inclure des statistiques sur les variantes (par défaut : `false`).  |
| `include_step_breakdown` | Facultatif | Valeur booléenne | Indique s'il faut inclure des statistiques sur les étapes (par défaut : `false`). |
| `include_deleted_step_data` | Facultatif | Valeur booléenne | Inclure ou non les statistiques des étapes supprimées (valeur par défaut : `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
**Alignement des fuseaux horaires :** Les analyses/analytiques du tableau de bord de Braze sont agrégées quotidiennement dans le fuseau horaire configuré de votre entreprise dans le tableau de bord. Assurez-vous que vos horodatages s'alignent sur le fuseau horaire de votre entreprise afin que vos statistiques correspondent au tableau de bord. Par exemple, si l'heure de votre entreprise est UTC+2, l'horodatage doit être 12AM UTC+2.
{% endalert %}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "conversions": (int) the number of conversions,
      "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
      "entries": (int) the number of entries
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' on successful completion
}
```

{% alert important %}
**`influenced_opens` champ :** Dans la réponse de l'API, le champ `influenced_opens` représente le nombre total d'ouvertures (ouvertures directes et influencées combinées). Dans le tableau de bord de Braze, les " ouvertures influencées " se réfèrent uniquement aux ouvertures influencées, à l'exclusion des ouvertures directes. Cela est dû à une convention de dénomination héritée de l'API.
{% endalert %}

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

---
nav_title: "GET : Exporter les KPI pour les désinstallations quotidiennes d'applications par date"
article_title: "GET : Exporter les KPI pour les désinstallations quotidiennes d'applications par date"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les désinstallations quotidiennes d’application par date."

---
{% api %}
# Exporter les KPI pour les désinstallations quotidiennes d’application par date
{% apimethod get %}
/kpi/uninstalls/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer quotidiennement une série du nombre total de désinstallations à chaque date.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `kpi.uninstalls.data_series`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre| Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l’heure de la demande. |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant de l'API de l'application récupéré à partir de la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Si exclu, les résultats de toutes les applications dans l'espace de travail seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/uninstalls/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "uninstalls" : (int) the number of uninstalls
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

---
nav_title: "GET : Exporter les sessions d'application par heure"
article_title: "Get : Exporter les sessions d'application par heure"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter les analyses de sessions d'application par heure."

---
{% api %}
# Exporter les sessions d'application par heure
{% apimethod get %}
/sessions/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer une série du nombre de sessions de votre application sur une période donnée.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#79efb6a9-62ec-4b8a-bf4a-e96313aa4be1 {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre| Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `length` | Requis | Entier | Nombre maximum d’unités (jours ou heures) avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `unit` | Facultatif | String | Unité de temps entre les points de données. Peut être `day` ou `hour`, valeur par défaut `day`.  |
| `ending_at` | Facultatif | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, l’heure de la demande. |
| `app_id` | Facultatif | String | Identifiant API de l’application extrait de la **console du développeur (Developer Console)** pour limiter l’analyse à une application spécifique. |
| `segment_id` | Facultatif | String | Voir [Identifiant API de segment]({{site.baseurl}}/api/identifier_types/). ID de segment indiquant le segment à analyser pour lequel les sessions doivent être renvoyées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/sessions/data_series?length=14&unit=day&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}&segment_id={{segment_identifier}}' \
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
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

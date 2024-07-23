---
nav_title: "GET : Exporter des données de revenus"
article_title: "GET : Exporter des données de revenus"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter des données de revenus."

---
{% api %}
# Exporter les données de revenus par période
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> Utilise ce point de terminaison pour renvoyer l'argent total dépensé dans ton appli sur une plage de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `purchases.revenue_series`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Paramètres de demande

| Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description - Paramètre - Requis - Type de données - Description
|---|---|---|---|
| `ending_at` | Facultatif | Horodatage (chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l'exportation des données doit se terminer. Par défaut, l’heure de la demande.
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus).
| `unit` | Facultatif | Chaîne de caractères | Unité de temps entre les points de données. Peut être le jour ou l'heure, la valeur par défaut est le jour. |
| `app_id` | Facultatif | Chaîne | Identifiant de l'API de l'application récupéré à partir de la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). En cas d’exclusion, les résultats de toutes les applications d’un espace de travail seront renvoyés. |
| `product` | Facultatif | Chaîne | Nom du produit par lequel filtrer la réponse. En cas d'exclusion, les résultats de toutes les applications seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "revenue" : (int) amount of revenue for the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consulte la rubrique [Dépannage des exportations]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

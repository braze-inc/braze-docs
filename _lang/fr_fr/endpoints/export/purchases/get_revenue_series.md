---
nav_title: "GET : Données sur les chiffres d'affaires à l'exportation"
article_title: "GET : Exporter des données de revenus"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter des données de revenus."

---
{% api %}
# Exporter les données des chiffres d'affaires par période
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer l'argent total dépensé dans votre application sur une plage de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `purchases.revenue_series`.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `ending_at` | Facultatif | Datetime[(](https://en.wikipedia.org/wiki/ISO_8601) chaîne de caractères[ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) ) | Date à laquelle l’exportation de données doit se terminer. Par défaut, l’heure de la demande. |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `unit` | Facultatif | Chaîne de caractères | Unité de temps entre les points de données. Il peut s'agir d'un jour ou d'une heure, la valeur par défaut étant le jour. |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant de l'API de l'application récupéré à partir de la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). En cas d'exclusion, les résultats de toutes les applications d'un espace de travail seront renvoyés. |
| `product` | Facultatif | Chaîne de caractères | Nom du produit par lequel filtrer les réponses. En cas d'exclusion, les résultats de toutes les applications seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

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
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

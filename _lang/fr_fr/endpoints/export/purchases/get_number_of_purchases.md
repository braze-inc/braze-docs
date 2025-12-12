---
nav_title: "GET : Nombre d'achats à l'exportation"
article_title: "GET : Exportation Nombre d'achats"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Exporter le nombre d’achats."

---
{% api %}
# Nombre d'achats à l'exportation
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer le nombre total d'achats dans votre appli sur une plage de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l’autorisation `purchases.quantity_series`.

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
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
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
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Pour obtenir de l’aide sur les exportations CSV et de l’API, consultez la section [Résolution des problèmes d’exportation]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

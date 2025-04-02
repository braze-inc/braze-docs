---
nav_title: "GET: Produkt-IDs exportieren"
article_title: "GET: Produkt-IDs exportieren"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze Endpunkt Export product IDs."

---
{% api %}
# Produkt-IDs exportieren
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine paginierte Liste von Produkt-IDs zurückzugeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `purchases.product_list`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `page` | Optional | String | Die Seite Ihrer Produktliste, die Sie anzeigen möchten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

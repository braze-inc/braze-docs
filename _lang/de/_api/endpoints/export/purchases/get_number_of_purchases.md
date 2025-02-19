---
nav_title: "GET: Export Anzahl der Käufe"
article_title: "GET: Export Anzahl der Käufe"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zu den Exportnummern der Käufe von Braze-Endpunkten."

---
{% api %}
# Anzahl der Käufe exportieren
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Gesamtzahl der Käufe in Ihrer App über einen bestimmten Zeitraum zu ermitteln.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `purchases.quantity_series`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `ending_at` | Optional | Datetime[(ISO-8601-String](https://en.wikipedia.org/wiki/ISO_8601) ) | Datum, an dem der Datenexport enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `length` | Erforderlich | Integer | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `unit` | Optional | String | Zeiteinheit zwischen Datenpunkten. Kann Tag oder Stunde sein, die Voreinstellung ist Tag. |
| `app_id` | Optional | String | App-API-Kennung, die von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird. Wenn Sie diese Option ausschließen, werden die Ergebnisse für alle Anwendungen in einem Arbeitsbereich zurückgegeben. |
| `product` | Optional | String | Name des Produkts, nach dem die Antwort gefiltert werden soll. Wenn Sie diese Option ausschließen, werden die Ergebnisse für alle Anwendungen angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

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
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

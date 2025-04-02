---
nav_title: "GET: Täglich aktive Benutzer nach Datum exportieren"
article_title: "GET: Täglich aktive Benutzer nach Datum exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt Export täglich aktiver Benutzer."

---
{% api %}
# Täglich aktive Benutzer nach Datum exportieren
{% apimethod get %}
/kpi/dau/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine tägliche Reihe der Gesamtzahl der eindeutigen aktiven Benutzer an jedem Datum abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#90a64560-65aa-4f71-a8ef-1edf49321986 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `kpi.dau.data_series`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter| Erforderlich | Daten Typ | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `length` | Erforderlich | Integer | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `ending_at` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `app_id` | Optional | String | App-API-Kennung, die von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird. Wenn Sie diese Option ausschließen, werden die Ergebnisse für alle Anwendungen im Arbeitsbereich zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/dau/data_series?length=10&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "dau" : (int) the number of daily active users
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

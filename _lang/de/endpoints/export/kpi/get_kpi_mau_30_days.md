---
nav_title: "GET: Monatlich aktive Nutzer:innen der letzten 30 Tage exportieren"
article_title: "GET: Monatlich aktive Nutzer:innen für die letzten 30 Tage exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export monatlich aktive Nutzer:innen."

---
{% api %}
# Monatlich aktive Nutzer:innen der letzten 30 Tage exportieren
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine tägliche Reihe der Gesamtzahl eindeutiger aktiver Nutzer:innen über ein rollierendes 30-Tage-Fenster abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `kpi.mau.data_series`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter| Erforderlich | Datentyp | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `length` | Erforderlich | Integer | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 100 (einschließlich) liegen. |
| `ending_at` | Optional | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Datum, an dem die Datenreihe enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `app_id` | Optional | String | Bezeichner der App API, der von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) abgerufen wird. Wenn ausgeschlossen, werden die Ergebnisse für alle Apps im Workspace zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
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
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

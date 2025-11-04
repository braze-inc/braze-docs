---
nav_title: "GET: Export Canvas Daten Zusammenfassung Analytics"
article_title: "GET: Export Canvas Daten Zusammenfassung Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export Canvas Daten Zusammenfassung Analytics Braze."

---
{% api %}
# Exportieren von Canvas Daten Zusammenfassung Analytics
{% apimethod get %}
/canvas/daten_zusammenfassung
{% endapimethod %}

> Mit diesem Endpunkt ist es zulässig, Rollups von Zeitreihendaten für ein Canvas zu exportieren, die eine übersichtliche Zusammenfassung der Canvas-Ergebnisse liefern.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.data_summary`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas API Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Erforderlich | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Datum, an dem der Export der Daten enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `starting_at` | Fakultativ* | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) String) | Datum, an dem der Export der Daten beginnen soll. <br><br>\* Entweder `length` oder `starting_at` ist erforderlich. |
| `length` | Fakultativ* | String | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 14 (einschließlich) liegen. <br><br>\* Entweder `length` oder `starting_at` ist erforderlich. |
| `include_variant_breakdown` | Optional | Boolesch | Ob Variantenstatistiken einbezogen werden sollen oder nicht (Standard ist `false`).  |
| `include_step_breakdown` | Optional | Boolesch | Ob Schrittstatistiken einbezogen werden sollen oder nicht (Standard ist `false`). |
| `include_deleted_step_data` | Optional | Boolesch | Ob die Schrittstatistiken für gelöschte Schritte berücksichtigt werden sollen oder nicht (Standard: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
        "name": (string) the name of variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the number of influenced opens,
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
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

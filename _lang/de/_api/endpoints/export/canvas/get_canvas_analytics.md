---
nav_title: "GET: Exportieren von Canvas-Datenreihen Analytics"
article_title: "GET: Exportieren von Canvas-Datenreihen Analytics"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "In diesem Artikel finden Sie Einzelheiten über den Braze Endpunkt Export Canvas data series analytics."

---
{% api %}
# Exportieren Sie Canvas-Datenreihenanalysen
{% apimethod get %}
/canvas/data_series
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Zeitreihendaten für ein Canvas zu exportieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0fd61e93-7edf-4d87-a8dc-052420aefb73 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.data_series`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas API-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Erforderlich | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Datum, an dem der Datenexport enden soll. Standardmäßig wird die Zeit der Anfrage verwendet. |
| `starting_at` | Fakultativ* | Datetime <br>[(ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Zeichenfolge) | Datum, an dem der Datenexport beginnen soll. <br><br>\* Entweder `length` oder `starting_at` ist erforderlich. |
| `length` | Fakultativ* | String | Maximale Anzahl der Tage vor `ending_at`, die in der zurückgegebenen Serie enthalten sein sollen. Muss zwischen 1 und 14 (einschließlich) liegen. <br><br>\* Entweder `length` oder `starting_at` ist erforderlich. |
| `include_variant_breakdown` | Optional | Boolesche | Ob Variantenstatistiken einbezogen werden sollen oder nicht (Standardwert ist `false`).  |
| `include_step_breakdown` | Optional | Boolesche | Ob Schrittstatistiken einbezogen werden sollen oder nicht (Standardwert: `false`). |
| `include_deleted_step_data` | Optional | Boolesche | Ob die Schrittstatistiken für gelöschte Schritte berücksichtigt werden sollen oder nicht (Standardwert: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_series?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-5:00&starting_at=2018-05-28T23:59:59-5:00&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
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
    "stats": [
      {
        "time": (string) the date as ISO 8601 date,
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
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "entries": (int) the number of entries
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
            "name": (string) the name of step,
            "revenue": (float) the the number of dollars of revenue (USD),
            "conversions": (int) the the number of conversions,
            "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
            "messages": {
              "email": [
                {
                  "sent": (int) the number of sends,
                  "opens": (int) the number of opens,
                  "unique_opens": (int) the number of unique opens,
                  "clicks": (int) the number of clicks
                  ... (more stats)
                }
              ],
              "sms" : [
                {
                  "sent": (int) the number of sends,
                  "sent_to_carrier" : (int) the number of messages sent to the carrier,
                  "delivered": (int)the number of delivered messages,
                  "rejected": (int) the number of rejected messages,
                  "delivery_failed": (int) the number of failed deliveries,
                  "clicks": (int) the number of clicks on shortened links,
                  "opt_out" : (int) the number of opt outs,
                  "help" : (int) the number of help messages received
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

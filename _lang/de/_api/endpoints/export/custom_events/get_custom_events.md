---
nav_title: "GET: Benutzerdefinierte Ereignisliste exportieren"
article_title: "GET: Benutzerdefinierte Ereignisliste exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Benutzerdefinierte Ereignisliste exportieren."

---
{% api %}
# Benutzerdefinierte Ereignisliste exportieren
{% apimethod get %}
/events/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der benutzerdefinierten Ereignisse zu exportieren, die für Ihre App aufgezeichnet wurden. Die Ereignisnamen werden in Gruppen von 250 zurückgegeben, alphabetisch sortiert.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#93ecd8a5-305d-4b72-ae33-2d74983255c1 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `events.list`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='events list' %}

## Parameter anfordern

| Parameter| Erforderlich | Daten Typ | Beschreibung |
| -------- | -------- | --------- | ----------- |
| `page` | Optional | Integer | Die Seite mit den Ereignisnamen, die zurückgegeben werden soll. Der Standardwert ist 0 (gibt den ersten Satz von bis zu 250 zurück). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request GET 'https://rest.iad-01.braze.com/events/list?page=3' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A", (string) the event name,
        "Event B", (string) the event name,
        "Event C", (string) the event name,
        ...
    ]
}
```

### Antwortcodes für schwerwiegende Fehler {#fatal-export}

Statuscodes und zugehörige Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

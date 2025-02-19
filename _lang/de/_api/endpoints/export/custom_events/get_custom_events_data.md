---
nav_title: "GET: Benutzerdefinierte Ereignisse exportieren"
article_title: "GET: Benutzerdefinierte Ereignisse exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt Exportieren von benutzerdefinierten Ereignissen."

---
{% api %}
# Benutzerdefinierte Ereignisse exportieren
{% apimethod get %}
/events
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der für Ihre App aufgezeichneten benutzerdefinierten Ereignisse zu exportieren. Die Ereignisse werden in Gruppen von 50, alphabetisch sortiert, zurückgegeben.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `events.get`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='events' %}

## Parameter abfragen

Beachten Sie, dass jeder Aufruf dieses Endpunkts 50 Ereignisse zurückgibt. Bei mehr als 50 Ereignissen verwenden Sie die Kopfzeile `Link`, um die Daten auf der nächsten Seite abzurufen, wie in der folgenden Beispielantwort gezeigt.

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung der benutzerdefinierten Ereignisse. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfragen

### Ohne Cursor

```
curl --location --request GET 'https://rest.iad-01.braze.com/events' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/events?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        {
            "name": "The event name", (string) the event name,
            "description": "The event description", (string) the event description,
            "included_in_analytics_report": false, (boolean) the analytics report inclusion,
            "status": "Active", (string) the event status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the event formatted as strings,
        },
        ...
    ]
}
```

### Antwortcodes für schwerwiegende Fehler {#fatal-export}

Statuscodes und zugehörige Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, finden Sie unter [Schwerwiegende Fehler]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

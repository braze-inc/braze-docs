---
nav_title: "GET: Angepasste Attribute exportieren"
article_title: "GET: Angepasste Attribute exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Export angepasster Attribute Braze."

---
{% api %}
# Angepasste Attribute exportieren
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der angepassten Attribute zu exportieren, die für Ihre App erfasst wurden. Die Attribute werden in Gruppen von 50, alphabetisch sortiert, zurückgegeben.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `custom_attributes.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## Abfrageparameter

Beachten Sie, dass jeder Aufruf dieses Endpunkts 50 Attribute zurückgibt. Bei mehr als 50 Attributen verwenden Sie die Kopfzeile `Link`, um die Daten auf der nächsten Seite abzurufen, wie in der folgenden Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung der angepassten Attribute. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel-Anfragen

### Ohne Cursor

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### Schwerwiegende Fehler Antwortcodes {#fatal-export}

Für Statuscodes und zugehörige Nachrichten, die zurückgegeben werden, wenn Ihre Anfrage auf einen schwerwiegenden Fehler stößt, referenzieren Sie [Schwerwiegende Fehler]({{site.baseurl}}/api/errors/#fatal-errors).

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

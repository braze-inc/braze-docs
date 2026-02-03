---
nav_title: "GET: Spezifische Übersetzung und Lokalisierung für E-Mail Template anzeigen"
article_title: "GET: Spezifische Übersetzung und Lokalisierung für E-Mail Template anzeigen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details der anzeigenspezifischen Übersetzung und Lokalisierung für den Endpunkt von E-Mail Templates."
---

{% api %}
# Anzeigen einer bestimmten Übersetzung und Lokalisierung für den Endpunkt der E-Mail-Vorlage
{% apimethod get %}
/templates/uebersetzungen/email
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine bestimmte Übersetzung und Lokalisierung für eine [E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates) anzuzeigen. Weitere Informationen zu den Features für die Übersetzung finden Sie unter [Lokalisierung in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `templates.translations.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter

| Parameter     | Erforderlich | Datentyp | Beschreibung                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Erforderlich | String    | Die ID für Ihr E-Mail Template. |
| `locale_id`   | Optional | String    | Die ID (UUID) des Gebietsschemas.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Alle Übersetzungs-IDs werden als universelle eindeutige Bezeichner (UUIDs) betrachtet, die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        }
    ]
}
```

### Beispiel einer Fehlerantwort

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}

---
nav_title: "GET: View source translations for email template"
article_title: "GET: View Source Translations for E-Mail Template"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "In diesem Artikel erfahren Sie mehr über die Quelltextübersetzungen für einen E-Mail Template Endpunkt."
---

{% api %}
# Anzeigen der Quellübersetzungen für eine E-Mail-Vorlage
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Quellübersetzungen für eine [E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates) einzusehen. Weitere Informationen zu den Features für die Übersetzung finden Sie unter [Lokalisierung in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `templates.email.info`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter

| Parameter     | Erforderlich | Datentyp | Beschreibung                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Erforderlich | String    | Die ID für Ihr E-Mail Template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
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

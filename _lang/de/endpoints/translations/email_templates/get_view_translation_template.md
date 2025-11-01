---
nav_title: "GET: Alle Übersetzungen und Lokalisierungen für E-Mail Template anzeigen"
article_title: "GET: Alle Übersetzungen und Lokalisierungen für E-Mail Template anzeigen"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Alle Übersetzungen und Lokalisierungen für E-Mail Template anzeigen."
---

{% api %}
# Alle Übersetzungen und Lokalisierungen für eine E-Mail-Vorlage anzeigen
{% apimethod get %}
/templates/email/translations/
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Übersetzungen und Lokalisierungen für eine [E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates) anzuzeigen.

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie, dass alle Übersetzungs-IDs als universelle eindeutige Bezeichner (UUIDs) gelten, die Sie in den Einstellungen für **die Mehrsprachenunterstützung** oder in der Antwort auf die Anfrage finden.

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
--- template_id: "6ad1507f-ca10-44c4-95bf-6e4gay901kc5"
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
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
        },
        {
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            },
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
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

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehlermeldung                           | Fehlersuche                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `MULTI_LANGUAGE_NOT_ENABLED`            | Die Mehrspracheneinstellungen sind für Ihren Workspace nicht aktiviert.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Nur E-Mail-Templates und E-Mail-, Push- und In-App-Nachricht-Kampagnen oder Canvas-Nachrichten mit E-Mails können übersetzt werden.             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

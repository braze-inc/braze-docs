---
nav_title: "GET: Alle Übersetzungen für eine Kampagne anzeigen"
article_title: "GET: Alle Übersetzungen für eine Kampagne anzeigen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Funktion Alle Übersetzungen für einen Endpunkt einer Kampagne anzeigen."
---

{% api %}
# Alle Übersetzungen für eine Kampagne anzeigen
{% apimethod get %}
/kampagnen/übersetzungen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Übersetzungen für jede Variante einer Nachricht in einer Kampagne anzuzeigen.

{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.translations.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Für die Übersetzung einer Kampagne erforderlich | String | Die ID Ihrer Kampagne. |
| `message_variation_id` | Erforderlich | String | Die ID Ihrer Nachrichtenvariation. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Beachten Sie, dass alle Übersetzungs-IDs als universelle eindeutige Bezeichner (UUIDs) gelten, die Sie in den Einstellungen für **die Mehrsprachenunterstützung** oder in der Antwort auf die Anfrage finden.
{% endalert %}

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehlermeldung                           | Fehlersuche                                                                    |
|-----------------------------------------|------------------------------------------------------------------------------------|
| `INVALID_CAMPAIGN_ID`                   | Bestätigen Sie, dass die ID der Kampagne mit der Kampagne übereinstimmt, die Sie übersetzen.                   |
| `INVALID_MESSAGE_VARIATION_ID`          | Bestätigen Sie, dass Ihre ID für Nachrichten korrekt ist.                                                |
| `MESSAGE_NOT_FOUND`                     | Prüfen Sie, ob die Nachricht übersetzt werden soll.                                           |
| `MULTI_LANGUAGE_NOT_ENABLED`            | Die Mehrspracheneinstellungen sind für Ihren Workspace nicht aktiviert.                       |
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Es können nur E-Mails, Push- und In-App-Nachricht-Kampagnen oder Canvas-Nachrichten mit E-Mails übersetzt werden.             |
| `UNSUPPORTED_CHANNEL`                   | Es können nur E-Mails, Push- oder In-App-Nachricht-Kampagnen oder Canvas-Nachrichten übersetzt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

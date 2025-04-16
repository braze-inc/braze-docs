---
nav_title: "GET: Übersetzungen für eine Kampagne anzeigen"
article_title: "GET: Übersetzungen für eine Kampagne anzeigen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "In diesem Artikel erfahren Sie mehr über die Ansicht von Übersetzungen für einen Endpunkt einer Kampagne."
---

{% api %}
# Übersetzungen für eine Kampagne ansehen
{% apimethod get %}
/kampagnen/übersetzungen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Übersetzungen für jede Variante einer Nachricht in einer Kampagne anzuzeigen.

{% alert important %}
Die Anzeige von Übersetzungen für Kampagnen-Nachrichten über die API befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.translations.get`.

## Rate-Limit

Dieser Endpunkt hat ein Rate-Limits von 250.000 Anfragen pro Stunde.

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`campaign_id`| Für die Übersetzung einer Kampagne erforderlich | String | Die ID Ihrer Kampagne. |
| `message_variation_id` | Erforderlich | String | Die ID Ihrer Nachricht. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie, dass alle Übersetzungs-IDs als universelle eindeutige Bezeichner (UUIDs) gelten, die Sie in den Einstellungen für **die Mehrsprachenunterstützung** oder in der Antwort auf die Anfrage finden.

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaign/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404`, und `429`.

## Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
	"translations": [
		{
			"locale": {
 				"name": "zh-HK",
 				"country": "Hong Kong",
 				"language": "Chinese (Traditional)",
			},
			"translation_map": {
				"id_0": "Hello",
				"id_1": "My name is Jacky",
				"id_2": "Where is the library?"
			}
		}
	]
}
```

## Beispiel einer Fehlerantwort

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
| `MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE` | Nur E-Mail Kampagnen oder Canvas Nachrichten mit E-Mails können übersetzt werden.             |
| `UNSUPPORTED_CHANNEL`                   | Nur Nachrichten in E-Mail-Kampagnen oder Canvas-Nachrichten mit E-Mails können übersetzt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

---
nav_title: "PUT: Update der Übersetzung in einem Canvas"
article_title: "PUT: Update der Übersetzung in einem Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zur Update-Übersetzung in einem Canvas-Endpunkt."
---

{% api %}
# Update der Übersetzung in einem Canvas
{% apimethod put %}
/canvas/uebersetzungen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für ein Canvas zu aktualisieren.

{% alert important %}
Das Update einer Übersetzung für Canvas Nachrichten über die API befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.translations.update`.

## Rate-Limit

Dieser Endpunkt hat ein Rate-Limits von 250.000 Anfragen pro Stunde.

## Pfad-Parameter

Für diesen Endpunkt gibt es keine Pfadparameter.

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`step_id`| Erforderlich | String | Die ID Ihres Canvas-Schrittes. |
|`message_variation_id`| Erforderlich | String | Die ID Ihrer Nachricht. |
|`locale_id`| Erforderlich | String | Die ID des Gebietsschemas. |
|`workflow_id` | Erforderlich | String | Die ID des Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie, dass alle Übersetzungs-IDs als universelle eindeutige Bezeichner (UUIDs) gelten, die Sie in den Einstellungen für **die Mehrsprachenunterstützung** oder in der Antwort auf die GET-Anfrage finden.

## Beispiel Anfrage

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "canvas_id": "9a0ba932-11c0-4c33-b529-e79aafc12409",
    "message_variation_id": "f5896eec-847d-4c0d-a4b6-7695e67520d7",
    "locale_id": "3fa10d31-83ae-4ff4-9631-f52cea9ec8fa",
    "translation_map": {
        "id_4": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "subject_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "id_1": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca.",
        "image": "¿Dónde está la biblioteca? Me llamo T-Bone, La araña discoteca."
    }
}
```

## Beispiel für eine erfolgreiche Antwort

```json
{
	"message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die bei Ihnen auftreten können.

```json
{
	"errors": [
		{
			"message": "Something went wrong. Translation IDs are mismatched or translated text exceeds limits."
		}
	]
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehlermeldung | Fehlersuche |
| --- | --- |
|`INVALID_CAMPAIGN_ID`|Bestätigen Sie, dass die ID der Kampagne mit der Kampagne übereinstimmt, die Sie übersetzen.|
|`INVALID_LOCALE_ID`|Vergewissern Sie sich, dass Ihre Lokalisierungs-ID in der Übersetzung Ihrer Nachrichten vorhanden ist.|
|`INVALID_MESSAGE_VARIATION_ID`|Bestätigen Sie, dass Ihre ID für Nachrichten korrekt ist.|
|`INVALID_TRANSLATION_OBJECT`|Die IDs der Übersetzungen stimmen nicht überein oder der übersetzte Text überschreitet die Grenzen.|
|`MESSAGE_NOT_FOUND`|Prüfen Sie, ob die Nachricht übersetzt werden soll.|
|`LOCALE_NOT_FOUND`| Vergewissern Sie sich, dass das Gebietsschema in Ihren mehrsprachigen Einstellungen vorhanden ist. |
|`MISSING_TRANSLATIONS`|Die IDs der Übersetzungen müssen mit der Nachricht übereinstimmen.|
|`MULTI_LANGUAGE_NOT_ENABLED`|Die Mehrspracheneinstellungen sind für Ihren Workspace nicht aktiviert.|
|`MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE`|Nur E-Mail Kampagnen oder Canvas Nachrichten mit E-Mails können übersetzt werden.|
|`UNSUPPORTED_CHANNEL`| Nur Nachrichten in E-Mail-Kampagnen oder Canvas-Nachrichten mit E-Mails können übersetzt werden.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


          INVALID_CAMPAIGN_ID = "Invalid campaign or step ID"
          INVALID_LOCALE_ID = "Invalid locale ID"
          INVALID_MESSAGE_VARIATION_ID = "Invalid message ID"
          INVALID_TRANSLATION_OBJECT = "Invalid translation object"
          MESSAGE_NOT_FOUND = "Message not found"
          LOCALE_NOT_FOUND = "Locale not found"
          MISSING_TRANSLATIONS = "Missing translations from the request body"
          MULTI_LANGUAGE_NOT_ENABLED = "Multi-language feature is not enabled on this company"
          MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE = "This message does not have multi-language setup"
          UNSUPPORTED_CHANNEL = "This message type does not support multi-language"

{% endapi %}

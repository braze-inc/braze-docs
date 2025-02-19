---
nav_title: "PUT: Übersetzung in einem Canvas aktualisieren"
article_title: "PUT: Übersetzung in einem Canvas aktualisieren"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details der Update-Übersetzung in einem Canvas-Endpunkt."
---

{% api %}
# Übersetzung in einem Canvas aktualisieren
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für ein Canvas zu aktualisieren.

{% alert important %}
Die Aktualisierung einer Übersetzung für Canvas-Nachrichten über die API befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Kundenbetreuer, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.translations.update`.

## Preisgrenze

Dieser Endpunkt hat ein Ratenlimit von 250.000 Anfragen pro Stunde.

## Pfad-Parameter

Für diesen Endpunkt gibt es keine Pfadparameter.

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`step_id`| Erforderlich | String | Die ID Ihres Canvas-Schrittes. |
|`message_variation_id`| Erforderlich | String | Die ID Ihrer Nachricht. |
|`locale_id`| Erforderlich | String | Die ID des Gebietsschemas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie, dass alle Übersetzungs-IDs als universelle eindeutige Bezeichner (UUIDs) gelten, die Sie in den Einstellungen für **die Mehrsprachenunterstützung** oder in der Antwort auf die GET-Anfrage finden können.

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

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. Weitere Informationen zu Fehlern, die auftreten können, finden Sie unter [Fehlersuche](#troubleshooting).

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
|`INVALID_CAMPAIGN_ID`|Stellen Sie sicher, dass die Kampagnen-ID mit der Kampagne übereinstimmt, die Sie übersetzen möchten.|
|`INVALID_LOCALE_ID`|Bestätigen Sie, dass Ihre Gebietsschema-ID in Ihrer Nachrichtenübersetzung vorhanden ist.|
|`INVALID_MESSAGE_VARIATION_ID`|Bestätigen Sie, dass Ihre Nachrichten-ID korrekt ist.|
|`INVALID_TRANSLATION_OBJECT`|Die Übersetzungs-IDs stimmen nicht überein oder der übersetzte Text überschreitet die Grenzen.|
|`MESSAGE_NOT_FOUND`|Prüfen Sie, ob die Nachricht übersetzt werden soll.|
|`LOCALE_NOT_FOUND`| Vergewissern Sie sich, dass das Gebietsschema in Ihren mehrsprachigen Einstellungen vorhanden ist. |
|`MISSING_TRANSLATIONS`|Die Übersetzungs-IDs müssen mit der Nachricht übereinstimmen.|
|`MULTI_LANGUAGE_NOT_ENABLED`|Die Mehrspracheneinstellungen sind für Ihren Arbeitsbereich nicht aktiviert.|
|`MULTI_LANGUAGE_NOT_ENABLED_ON_MESSAGE`|Nur E-Mail-Kampagnen oder Canvas-Nachrichten mit E-Mails können übersetzt werden.|
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

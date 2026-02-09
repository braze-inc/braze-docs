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

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für ein Canvas zu aktualisieren. Weitere Informationen zu den Features für die Übersetzung finden Sie unter [Lokalisierung in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

Wenn Sie Übersetzungen aktualisieren möchten, nachdem ein Canvas gestartet wurde, müssen Sie zunächst [Ihre Nachricht als Entwurf speichern]({{site.baseurl}}/post-launch_edits/).

{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.translations.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfad-Parameter

Für diesen Endpunkt gibt es keine Pfadparameter.

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`workflow_id` | Erforderlich | String | Die ID des Canvas. |
|`step_id`| Erforderlich | String | Die ID Ihres Canvas-Schrittes. |
|`message_variation_id`| Erforderlich | String | Die ID Ihrer Nachrichtenvariation. |
|`locale_id`| Erforderlich | String | Die ID (UUID) des Gebietsschemas. |
|`translation_map` | Erforderlich | Objekt | Objekt, das die neuen Übersetzungen enthält. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Alle Übersetzungs-IDs werden als universelle eindeutige Bezeichner (UUIDs) betrachtet, die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispiel Anfrage

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort

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
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}

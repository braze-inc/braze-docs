---
nav_title: "PUT: Übersetzung in einem Content-Block aktualisieren"
article_title: "PUT: Übersetzung in einem Content-Block aktualisieren"
search_tag: Endpunkt
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel enthält detaillierte Informationen zum Update der Übersetzung in einem Content-Block-Endpunkt."
---

{% api %}
# Übersetzung in einem Content-Block aktualisieren
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für einen [Content-Block]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) zu Update. Weitere Informationen zu den Übersetzungsfeatures finden Sie unter [„Locales in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)“.

{% include early_access_beta_alert.md feature='This endpoint' %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `content_blocks.translations.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfad-Parameter

Für diesen Endpunkt gibt es keine Pfadparameter.

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Erforderlich | String | Die ID Ihres Content-Blocks. |
| `locale_id`| Erforderlich | String | Die ID (UUID) der Locale. |
| `translation_map` | Erforderlich | Objekt | Objekt, das die neuen Übersetzungen enthält. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispiel Anfrage

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
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

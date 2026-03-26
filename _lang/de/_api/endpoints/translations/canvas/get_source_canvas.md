---
nav_title: "GET: Standardquellwerte für Canvas-Übersetzungstags anzeigen"
article_title: "GET: Standardquellwerte für Canvas-Übersetzungstags anzeigen"
search_tag: Endpunkt
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel enthält detaillierte Informationen zum Canvas-Übersetzungsquellen-Endpunkt."
---

{% api %}
# Standardquellwerte für die Übersetzungstags eines Canvases anzeigen
{% apimethod get %}
/Canvas/Übersetzungen/Quelle
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Standardübersetzungsquellen für die Übersetzungstags einer Canvas anzuzeigen. Dies sind die Werte mit dem {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Weitere Informationen zu den Übersetzungsfeatures finden Sie unter [„Locales in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)“.

{% multi_lang_include early_access_beta_alert.md feature='This endpoint' %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.translations.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter

| Parameter              | Erforderlich | Datentyp | Beschreibung                        |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id`          | Erforderlich | String    | Die ID des Canvas.              |
| `step_id`              | Erforderlich | String    | Die ID Ihres Canvas-Schrittes.        |
|`message_variation_id`| Erforderlich | String | Die ID Ihrer Nachrichtenvariation. |
| `locale_id`            | Optional | String    | Die ID (UUID) der Locale.              |
| `post_launch_draft_version`| Optional | Boolesch | Wenn die neueste Entwurfsversion anstelle der `true`zuletzt veröffentlichten Live-Version zurückgegeben wird. Standardmäßig`false`wird die aktuellste Live-Version zurückgegeben.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}

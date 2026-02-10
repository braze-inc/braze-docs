---
nav_title: "GET: Standard-Quellwerte für Tags zur Übersetzung von Kampagnen anzeigen"
article_title: "GET: Standard-Quellwerte für Tags zur Übersetzung von Kampagnen anzeigen"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt der Kampagnen-Übersetzungsquelle."
---

{% api %}
# Standard-Quellwerte für die Übersetzungstags einer Kampagne anzeigen
{% apimethod get %}
/kampagnen/uebersetzungen/quelle
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Standard-Übersetzungsquellen für die Übersetzungstags einer Kampagne anzuzeigen. Dies sind die Werte innerhalb der {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Weitere Informationen zu den Features für die Übersetzung finden Sie unter [Lokalisierung in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

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
|`campaign_id`| Erforderlich | String | Die ID Ihrer Kampagne. |
|`message_variation_id`| Erforderlich | String | Die ID Ihrer Nachrichtenvariation. |
|`locale_id`| Optional | String | Eine Lokalisierungs-UUID zum Filtern der Antworten. |
|`post_launch_draft_version`| Optional | Boolesch | Wenn `true` die letzte Entwurfsversion anstelle der letzten live veröffentlichten Version zurückgibt. Der Standardwert ist `false`, der die letzte Live-Version zurückgibt.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Alle Übersetzungs-IDs werden als universelle eindeutige Bezeichner (UUIDs) betrachtet, die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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

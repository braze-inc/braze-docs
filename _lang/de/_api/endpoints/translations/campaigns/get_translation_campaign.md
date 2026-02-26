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

> Verwenden Sie diesen Endpunkt, um alle Übersetzungen für jede Variante einer Nachricht in einer Kampagne anzuzeigen. Weitere Informationen zu den Features für die Übersetzung finden Sie unter [Lokalisierung in Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/).

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
| `post_launch_draft_version`| Optional | Boolesch | Wenn `true` die letzte Entwurfsversion anstelle der letzten live veröffentlichten Version zurückgibt. Der Standardwert ist `false`, der die letzte Live-Version zurückgibt.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Alle Übersetzungs-IDs werden als universelle eindeutige Bezeichner (UUIDs) betrachtet, die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispiel Anfrage

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

Es gibt vier Status Code Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Response Header und Body zurückgeben.

```json
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

Der Status Code `400` könnte den folgenden Antwortkörper zurückgeben.

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

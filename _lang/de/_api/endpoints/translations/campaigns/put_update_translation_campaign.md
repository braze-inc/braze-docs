---
nav_title: "PUT: Übersetzung in einer Kampagne aktualisieren"
article_title: "PUT: Update der Übersetzung in einer Kampagne"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "In diesem Artikel erfahren Sie mehr über die Update-Übersetzung in einem Endpunkt einer Kampagne."
---

{% api %}
# Update der Übersetzung in einer Kampagne
{% apimethod put %}
/kampagnen/übersetzungen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Übersetzungen für eine Kampagne zu aktualisieren.

Wenn Sie Übersetzungen aktualisieren möchten, nachdem eine Kampagne gestartet wurde, müssen Sie zunächst [Ihre Nachricht als Entwurf speichern]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/).

{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.translations.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Pfad-Parameter

Für diesen Endpunkt gibt es keine Pfadparameter.

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Die ID Ihrer Kampagne. |
| `message_variation_id` | Erforderlich | String | Die ID Ihrer Nachrichtenvariation. |
| `locale_name` | Erforderlich | String | Der Name des Gebietsschemas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Beachten Sie, dass alle Übersetzungs-IDs als universelle eindeutige Bezeichner (UUIDs) gelten, die Sie in den Einstellungen für **die Mehrsprachenunterstützung** oder in der Antwort auf die GET-Anfrage finden.

## Beispiel Anfrage

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "campaign_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab", // CAMPAIGNS ONLY
    "message_variation_id": "f14404b3-3626-4de0-bdec-06935f3aa0ad",
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


## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehlermeldung  | Fehlersuche |
|----|----------|
| `The provided translations yielded errors when parsing. Please contact Braze for more information.` | Tritt auf, wenn der Drittanbieter-Übersetzer Übersetzungen mit Ausnahmen liefert, die Liquid-Fehler erzeugen. Wenden Sie sich an den Braze Support für weitere Unterstützung. |
| `The provided translations are missing 'id_1', 'id_2'` | Die IDs der Übersetzungen stimmen nicht überein oder der übersetzte Text überschreitet die Grenzen. Dies könnte zum Beispiel bedeuten, dass der Nutzlastform Felder im Übersetzungsobjekt fehlen. Jede Nachricht (bei Enablement für Mehrsprachigkeit) sollte eine bestimmte Anzahl von "Übersetzungsblöcken" mit einer zugehörigen ID haben. Fehlt in der bereitgestellten Nutzlast eine der IDs, so wird dies als unvollständiges Objekt betrachtet und führt zu einem Fehler. |
| `The provided locale code does not exist.` | Die Nutzlast des Drittanbieter-Übersetzers enthält einen Code für die Lokalisierung, der in Braze nicht vorhanden ist. |
| `The provided translations have exceeded the maximum of 20MB.` | Die angegebene Nutzlast überschreitet die Größenbeschränkung. |
| `You have exceeded the maximum number of requests. Please try again later.` | Alle Braze APIs verfügen über ein eingebautes Rate-Limiting. Dieser Fehler wird automatisch zurückgegeben, wenn die Rate den zugewiesenen Betrag für dieses Authentifizierungs-Token überschritten hat. |
| `This message does not support multi-language.` | Dies kann vorkommen, wenn eine Message ID noch keine mehrsprachigen Nachrichten unterstützt. Es können nur Nachrichten in den folgenden Kanälen übersetzt werden: Push, In-App-Nachrichten und E-Mail. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

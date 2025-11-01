---
nav_title: "GET: Integrationen auflisten"
article_title: "GET: Listen-Integrationen"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_integration_list/
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten über den Endpunkt List integrations Braze."

---
{% api %}
# Integrationen auflisten
{% apimethod get %}
/cdi/integrationen
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der vorhandenen Integrationen zurückzugeben.


{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_list` erstellen.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='cdi list integrations' %}

## Abfrageparameter

Jeder Aufruf dieses Endpunkts gibt 10 Artikel zurück. Bei einer Liste mit mehr als 10 Integrationen verwenden Sie die Kopfzeile `Link`, um die Daten auf der nächsten Seite abzurufen, wie in der Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung der Integrationsliste. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

### Ohne Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Antwortkörper zurückgeben.

{% alert note %}
Die Kopfzeile `Link` gibt es nicht, wenn es insgesamt weniger als oder gleich 10 Integrationen gibt. Bei Anrufen ohne Cursor wird `prev` nicht angezeigt. Wenn Sie sich die letzte Seite der Artikel ansehen, wird `next` nicht angezeigt.
{% endalert %}

```
Link: </cdi/integrations?cursor=c2tpcDow>; rel="prev",</cdi/integrations?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
      "integration_id": (string) integration ID,
      "app_group_id": (string) app group ID,
      "integration_name": (string) integration name,
      "integration_type": (string) integration type,
      "integration_status": (string) integration status,
      "contact_emails": (string) contact email(s),
      "last_updated_at": (string) last timestamp that was synced in ISO 8601,
      "warehouse_type": (string) data warehouse type,
      "last_job_start_time": (string) timestamp of the last sync run in ISO 8601,
      "last_job_status": (string) status of the last sync run,
      "next_scheduled_run": (string) timestamp of the next scheduled sync in ISO 8601,
    },
  ],
  "message": "success"
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `400 Invalid cursor` | Prüfen Sie, ob Ihre `cursor` gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Statuscodes und zugehörige Nachrichten finden Sie unter [Schwerwiegende Fehler & Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}

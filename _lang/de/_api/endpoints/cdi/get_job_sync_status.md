---
nav_title: "GET: Job-Synchronisationsstatus auflisten"
article_title: "GET: Job-Synchronisationsstatus auflisten"
search_tag: Endpoint
page_order: 1
alias: /api/cdi/get_job_sync/
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze Endpunkt Job-Synchronisierungsstatus auflisten."

---
{% api %}
# Status der Auftragssynchronisation auflisten
{% apimethod get %}
/cdi/integrations/{integration_id}/job_sync_status
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der vergangenen Synchronisierungsstatus für eine bestimmte Integration zurückzugeben.

{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_job_status` erstellen.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='cdi job sync status' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `integration_id` | Erforderlich | String | Integration ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Abfrageparameter

Jeder Aufruf dieses Endpunkts gibt 10 Artikel zurück. Bei einer Integration mit mehr als 10 Synchronisierungen verwenden Sie die Kopfzeile `Link`, um die Daten auf der nächsten Seite abzurufen, wie in der folgenden Beispielantwort gezeigt.

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `cursor` | Optional | String | Bestimmt die Paginierung des Synchronisationsstatus. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

### Ohne Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### Mit Cursor

```
curl --location --request GET 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

Der Status Code `200` könnte den folgenden Antwortkörper zurückgeben.

{% alert note %}
Die Kopfzeile `Link` existiert nicht, wenn es insgesamt weniger als oder gleich 10 Synchronisierungen gibt. Bei Anrufen ohne Cursor wird `prev` nicht angezeigt. Wenn Sie sich die letzte Seite der Artikel ansehen, wird `next` nicht angezeigt.
{% endalert %}

```
Link: </cdi/integrations/00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDow>; rel="prev",</cdi/integrations00000000-0000-0000-0000-000000000000/job_sync_status?cursor=c2tpcDoxMDA=>; rel="next"
```

```json
{
  "results": [
    {
        "job_status": (string) status of the sync, see below for explanation of different statuses,
        "sync_start_time": (string) time the sync started in ISO 8601,
        "sync_finish_time": (string) time the sync finished in ISO 8601,
        "last_timestamp_synced": (string) last UPDATED_AT timestamp processed by the sync in ISO 8601,
        "rows_synced": (integer) number of rows successfully synced to Braze,
        "rows_failed_with_errors": (integer) number of rows failed because of errors,
    },
  ],
  "message": "success"
}
```

| job_status | Erklärung |
| --- | --- |
| `running` | Der Auftrag wird gerade ausgeführt. |
| `success` | Alle Zeilen wurden erfolgreich synchronisiert. |
| `partial` | Einige Zeilen konnten aufgrund von Fehlern nicht synchronisiert werden. |
| `error` | Es wurden keine Zeilen synchronisiert. |
| `config_error` | Es ist ein Fehler in der Konfiguration der Integration aufgetreten. Überprüfen Sie Ihre Integrationseinstellungen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `400 Invalid cursor` | Prüfen Sie, ob Ihre `cursor` gültig ist. |
| `400 Invalid integration ID` | Prüfen Sie, ob Ihre `integration_id` gültig ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Statuscodes und zugehörige Nachrichten finden Sie unter [Schwerwiegende Fehler & Antworten.]({{site.baseurl}}/api/errors/#fatal-errors)

{% endapi %}

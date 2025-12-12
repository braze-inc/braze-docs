---
nav_title: "POST: Synchronsignal triggern"
article_title: "POST: Synchronsignal triggern"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt Trigger sync Braze."

---
{% api %}
# Eine Synchronisation triggern
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Synchronisierung für eine bestimmte Integration zu triggern.

{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_sync` erstellen.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Pfad-Parameter

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `integration_id` | Erforderlich | String | Integration ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

Der Status Code `202` könnte den folgenden Antwortkörper zurückgeben:

```json
{
  "message": "success"
}
```

## Fehlerbehebung

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `400 Invalid integration ID` | Prüfen Sie, ob Ihre `integration_id` gültig ist. |
| `404 Integration not found` | Für die angegebene Integration ID existiert keine Integration. Vergewissern Sie sich, dass Ihre Integration ID gültig ist. |
| `429 Another job is in progress` | Für diese Integration wird derzeit eine Synchronisierung durchgeführt. Versuchen Sie es erneut, nachdem die Synchronisierung abgeschlossen ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Statuscodes und zugehörige Nachrichten finden Sie unter [Schwerwiegende Fehler & Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}

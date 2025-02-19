---
nav_title: "POST: Sync auslösen"
article_title: "POST: Sync auslösen"
search_tag: Endpoint
page_order: 2
alias: /api/cdi/post_trigger_sync/
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Trigger sync Braze Endpunkt."

---
{% api %}
# Eine Synchronisation auslösen
{% apimethod post %}
/cdi/integrations/{integration_id}/sync
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Synchronisierung für eine bestimmte Integration auszulösen.

{% alert note %}
Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `cdi.integration_sync` erstellen.
{% endalert %}

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='cdi job sync' %}

## Pfad-Parameter

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| `integration_id` | Erforderlich | String | Integrations-ID. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/cdi/integrations/00000000-0000-0000-0000-000000000000/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben:

```json
{
  "message": "success"
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlersuche |
| --- | --- |
| `400 Invalid integration ID` | Prüfen Sie, ob Ihre `integration_id` gültig ist. |
| `404 Integration not found` | Es existiert keine Integration für die angegebene Integrations-ID. Stellen Sie sicher, dass Ihre Integrations-ID gültig ist. |
| `429 Another job is in progress` | Derzeit läuft eine Synchronisierung für diese Integration. Versuchen Sie es erneut, nachdem die Synchronisierung abgeschlossen ist. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Statuscodes und zugehörige Fehlermeldungen finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

{% endapi %}

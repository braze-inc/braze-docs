---
nav_title: "POST: Katalogfelder erstellen"
article_title: "POST: Katalogfelder erstellen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Katalogfelder erstellen."

---
{% api %}
# Katalogfelder erstellen
{% apimethod post %}
/catalogs/{catalog_name}/fields
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um mehrere Felder in Ihrem Katalog zu erstellen.
{% alert important %}
Dieser Endpunkt befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an diesem frühen Zugang interessiert sind.
{% endalert %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `catalogs.create_fields`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog fields' %}

## Pfad-Parameter

| Parameter      | Erforderlich | Daten Typ | Beschreibung          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Erforderlich | String    | Name des Katalogs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung                                                                                                  |
| --------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------ |
| `fields`  | Erforderlich | Array     | Ein Array, das Feldobjekte enthält. Die Feldobjekte sollten den Namen und den Typ der neuen Felder enthalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispiel Anfrage

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/fields' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "fields": [
    {
      "name": "Name",
      "type": "string"
    },
    {
      "name": "Ratings",
      "type": "number"
    },
    {
      "name": "Loyalty_Program",
      "type": "boolean"
    },
    {
      "name": "Created_At",
      "type": "time"
    }
  ]
}'
```

## Antwort

Es gibt drei Statuscode-Antworten für diesen Endpunkt: `202`, `400`, und `404`.

### Beispiel für eine erfolgreiche Antwort

Der Statuscode `202` könnte den folgenden Antwortkörper zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel einer Fehlerantwort

Der Statuscode `400` könnte den folgenden Antwortkörper zurückgeben. Weitere Informationen zu Fehlern, die auftreten können, finden Sie unter [Fehlersuche](#troubleshooting).

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler                                | Fehlersuche                                                                                        |
|--------------------------------------|--------------------------------------------------------------------------------------------------------|
| `arbitrary-error`                    | Es ist ein willkürlicher Fehler aufgetreten. Bitte versuchen Sie es erneut oder kontaktieren Sie den [Support]({{site.baseurl}}/support_contact/). |
| `catalog-not-found`                  | Prüfen Sie, ob der Katalogname gültig ist.                                                                  |
| `company-size-limit-already-reached` | Das Limit für die Katalogspeichergröße ist erreicht.                                                             |
| `request-includes-too-many-fields`   | Jede Anfrage kann bis zu 50 neue Felder enthalten.                                                          |
| `catalog-exceeds-fields-limit`       | Der Katalog kann nicht mehr als 500 Felder haben.                                                              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}

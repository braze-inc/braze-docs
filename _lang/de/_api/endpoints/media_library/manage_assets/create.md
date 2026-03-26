---
nav_title: "POST: Bitte laden Sie eine Datei in die Medienbibliothek hoch."
article_title: "POST: Bitte laden Sie eine Datei in die Medienbibliothek hoch."
search_tag: Endpunkt
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält detaillierte Informationen zum Endpunkt „POST /media_library/create“."
---

{% api %}
# Bitte laden Sie eine Datei in die Medienbibliothek hoch.
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um ein Asset zur [Braze-Medienbibliothek](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library) hinzuzufügen, entweder über eine extern gehostete URL (`asset_url`) oder über Binärdaten, die in der Anfrage (`asset_file`) gesendet werden. Dieser Endpunkt unterstützt Bilder und ZIP-Dateien, die Bilder enthalten.

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `media_library.create`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

Wenn Sie einfügen`asset_url`, lädt der Endpunkt die Datei von der URL herunter. Wenn Sie einfügen`asset_file`, verwendet der Endpunkt die Binärdaten in der Anfrage.

Beispiel für einen Body einer Anfrage für`asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Beispiel für einen Body einer Anfrage für`asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

Die Anfrage enthält die folgenden Parameter:

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Optional | String | Eine öffentlich zugängliche URL für die Ressource, die in Braze hochgeladen werden soll. |
| `asset_file` | Optional | Binär | Binärdatei-Daten. |
| `name` | Optional | String | Ein Name, der in der Medienbibliothek für dieses Asset angezeigt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url` und`asset_file`  schließen sich gegenseitig aus, daher sollten Sie nur eines davon in Ihre API-Anfrage aufnehmen.
{% endalert %}

### Namen der hochgeladenen Dateien

In diesem Abschnitt wird erläutert, wie der Endpunkt hochgeladenen Dateien Namen zuweist, je nachdem, ob Sie den`name`Parameter einfügen.

#### Einzelne Datei-Uploads

| Szenario | Ergebnis |
| --- | --- |
| `name` zur Verfügung gestellt | Der`name`Wert wird als Name des Assets in der Bibliothek für Medien verwendet. |
| `name` ausgeschlossen | Der ursprüngliche Dateiname aus der URL oder der hochgeladenen Datei wird verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### Hochladen von ZIP-Dateien

| Szenario | Ergebnis |
| --- | --- |
| `name` zur Verfügung gestellt | Der`name`Wert wird als Präfix verwendet, wobei eine aufsteigende Zahl als Suffix angehängt wird (z. B. „Meine Datei 1“, „Meine Datei 2“, „Meine Datei 3“). |
| `name` ausgeschlossen | Jede Datei behält ihren ursprünglichen Dateinamen aus der ZIP-Datei bei. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## Beispiel Anfrage

Dieser Abschnitt enthält zwei `curl`Beispielanfragen, eine zum Hinzufügen einer Ressource über eine URL und eine weitere über Binärdaten.

Diese Anfrage veranschaulicht ein Beispiel für das Hinzufügen eines Assets zur Medienbibliothek mithilfe einer `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Diese Anfrage veranschaulicht ein Beispiel für das Hinzufügen eines Assets zur Medienbibliothek mithilfe einer `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Fehlermeldungen

In diesem Abschnitt werden mögliche Fehler sowie die entsprechenden Nachrichten und Beschreibungen aufgeführt. 

#### Validierungsfehler

Validierungsfehler geben eine Struktur wie die folgende zurück:

```json
{
  "message": (String) Human-readable error description
}
```

Diese Tabelle listet mögliche Validierungsfehler auf.

| HTTP-Status | Nachricht | Beschreibung |
| --- | --- | --- |
| 400 | Entwederasset_url  oderasset_file  muss bereitgestellt werden. | In der Anfrage wurde kein Asset-Parameter angegeben. |
| 400 | Wederasset_url  nochasset_file  können bereitgestellt werden. Bitte geben Sie nur eine Antwort an. | Beide Asset-Parameter wurden angegeben; es ist jedoch nur einer zulässig. |
| 403 | Für dieses Unternehmen sind öffentliche APIs der Medienbibliothek nicht aktiviert. | Das Feature der Medienbibliothek ist für diesen Workspace nicht aktiviert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Verarbeitungsfehler

Verarbeitungsfehler führen zu einer abweichenden Antwort mit Fehlercodes:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Diese Tabelle listet mögliche Verarbeitungsfehler auf.

| Fehlercode | HTTP-Status | Beschreibung |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | Der hochgeladene Dateityp wird nicht unterstützt. Das`meta`Objekt enthält das Objekt`file_type`, das abgelehnt wurde. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | Die Datei überschreitet die maximal zulässige Größe. Bilder dürfen maximal 5 MB groß sein. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | Der Workspace hat die maximale Anzahl an Assets erreicht (Standard: 200 für Unternehmen mit kostenloser Demo, ansonsten unbegrenzt). Das`meta`Objekt enthält das aktuelle `limit`. |
| `ASSET_UPLOAD_FAILED` | 400 | Das Asset konnte aufgrund von Verarbeitungsproblemen nicht hochgeladen werden. |
| `ZIP_UPLOAD_ERROR` | 400 | Die ZIP-Datei ist beschädigt oder es kam zu einer Fehlermeldung bei der Öffnung. Das`meta`Objekt enthält die`original_error`Nachricht. |
| `ZIP_FILE_TOO_LARGE` | 400 | Die Gesamtgröße der ZIP-Datei ohne Komprimierung überschreitet die Grenze von 5 MB. Das`meta`Objekt umfasst die Elemente`zip_file_name`und `zip_file_size`. |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Ein Dateieintrag innerhalb der ZIP-Datei hat keinen Namen. Bitte stellen Sie sicher, dass die ZIP-Datei nicht beschädigt ist, und benennen Sie alle unbenannten Dateieinträge. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | Die ZIP-Datei enthält verschachtelte Verzeichnisse, die nicht unterstützt werden. Alle Dateien müssen sich im Stammverzeichnis der ZIP-Datei befinden. |
| `GENERIC_ERROR` | (500 %) | Beim Hochladen ist ein unerwarteter Fehler aufgetreten. Das`meta`Objekt enthält die`original_error`Nachricht für die Fehlerbehebung. Bitte versuchen Sie es erneut oder wenden Sie sich an [den Support]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Antwort

Für diesen Endpunkt gibt es fünf Statuscode-Antworten: `200`, `400`,`403` `429`, und `500`.

Die folgende JSON-Datei zeigt die erwartete Form der Antwort.

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}

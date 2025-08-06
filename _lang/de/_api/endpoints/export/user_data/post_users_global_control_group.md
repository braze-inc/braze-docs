---
nav_title: "POST: Nutzerprofil nach globaler Kontrollgruppe exportieren"
article_title: "POST: Nutzerprofil nach globaler Kontrollgruppe exportieren"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt Nutzer:innen exportieren in globale Kontrollgruppen Braze."

---
{% api %}
# Nutzerprofil nach globaler Kontrollgruppe exportieren
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Nutzer:innen innerhalb einer globalen Kontrollgruppe zu exportieren.

Nutzerdaten werden als mehrere Dateien mit Nutzer:innen JSON-Objekten exportiert, die durch neue Zeilen getrennt sind (z.B. ein JSON-Objekt pro Zeile). Alle Nutzer:innen einer globalen Kontrollgruppe werden bei jeder Generierung der Dateien berücksichtigt. Braze speichert keinen Verlauf darüber, wann Nutzer:innen zu einer globalen Kontrollgruppe hinzugefügt oder aus ihr entfernt werden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `users.export.global_control_group`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Auf Zugangsdaten basierende Antwortdetails

Wenn Sie Ihre [S3-][1] oder [Azure-Zugangsdaten][2] zu Braze hinzugefügt haben, wird jede Datei in Ihrem Bucket als ZIP-Datei mit einem Schlüsselformat hochgeladen, das wie `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` aussieht. Wenn Sie Azure verwenden, vergewissern Sie sich, dass Sie auf der Übersichtsseite für Azure Partner in Braze das Kontrollkästchen **Dies zum Standardziel für den Datenexport machen** aktiviert haben. In der Regel erstellen wir 1 Datei pro 5.000 Nutzer:innen, um die Verarbeitung zu optimieren. Das Exportieren kleinerer Segmente innerhalb eines großen Workspace kann zu mehreren Dateien führen. Sie können dann die Dateien extrahieren und bei Bedarf alle `json` Dateien zu einer einzigen Datei zusammenfügen. Wenn Sie eine `output_format` von `gzip` angeben, lautet die Dateierweiterung `.gz` statt `.zip`.

{% details Aufschlüsselung des Exportpfads für ZIP %}
**ZIP-Format:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**Beispiel ZIP:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Eigenschaft                        | Details                                                                              | Im Beispiel dargestellt als                    |
| ------------------------------- | ------------------------------------------------------------------------------------ |
| `bucket-name`                   | Basierend auf Ihrem Bucket-Namen festgelegt.                                                     | `braze.docs.bucket`                    |
| `segment-export`                | Behoben.                                                                               | `segment-export`                       |
| `SEGMENT_ID`                    | In der Anfrage für den Export enthalten.                                                      | `abc56c0c-rd4a-pb0a-870pdf4db07q`      |
| `YYYY-MM-dd`                    | Das Datum, an dem der erfolgreiche Callback eingegangen ist.                                        | `2019-04-25`                           |
| `RANDOM_UUID`                   | Eine zufällige UUID, die von Braze zum Zeitpunkt der Anfrage generiert wurde.                         | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Unix-Zeit (Sekunden seit 2017-01-01:00:00:00Z), zu der der Export in UTC angefragt wurde. | `1556044807`                           |
| `filename`                      | Zufällig pro Datei.                                                                     | `114f0226319130e1a4770f2602b5639a`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

Wir empfehlen dringend, Ihre eigenen S3- oder Azure-Zugangsdaten einzurichten, wenn Sie diesen Endpunkt verwenden, um Ihre eigenen Bucket-Richtlinien für den Export durchzusetzen. Wenn Sie Ihre Zugangsdaten für den Cloud-Speicher nicht zur Verfügung stellen können, finden Sie in der Antwort auf die Anfrage die URL, unter der Sie ein ZIP mit allen Nutzer:innen-Dateien herunterladen können. Die URL wird erst dann zu einem gültigen Standort, wenn der Export abgeschlossen ist.

Beachten Sie, dass die Menge der Daten, die Sie von diesem Endpunkt exportieren können, begrenzt ist, wenn Sie Ihre Zugangsdaten für den Cloud-Speicher nicht angeben. Je nach den Feldern, die Sie exportieren, und der Anzahl der Nutzer:innen kann die Dateiübertragung fehlschlagen, wenn sie zu groß ist. Am besten legen Sie fest, welche Felder Sie exportieren möchten, indem Sie `fields_to_export` verwenden und nur die Felder angeben, die Sie benötigen, um die Größe der Übertragung gering zu halten. Wenn Sie bei der Generierung der Datei Fehler erhalten, sollten Sie Ihre Nutzer:innen auf der Grundlage einer zufälligen Bucket-Nummer in mehrere Segmente aufteilen (z.B. ein Segment erstellen, bei dem die zufällige Bucket-Nummer kleiner als 1.000 oder zwischen 1.000 und 2.000 ist).

In beiden Szenarien können Sie optional eine `callback_endpoint` angeben, um benachrichtigt zu werden, wenn der Export fertig ist. Wenn Sie die Adresse `callback_endpoint` angeben, senden wir Ihnen eine Anfrage per Post an die angegebene Adresse, sobald der Download fertig ist. Der Text der Nachricht lautet "Erfolg":true. Wenn Sie Ihre Zugangsdaten für den Cloud-Speicher nicht zu Braze hinzugefügt haben, enthält der Body des Beitrags zusätzlich das Attribut `url` mit der Download-URL als Wert.

Größere Nutzer:innen haben längere Exportzeiten zur Folge. Eine App mit 20 Millionen Nutzer:innen könnte zum Beispiel eine Stunde oder länger dauern.

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "callback_endpoint" : (optional, string) endpoint to post a download URL to when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, for example, ['first_name', 'email', 'purchases'],
  "output_format" : (optional, string) When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format
}
```

{% alert warning %}
Individuelle angepasste Attribute können nicht exportiert werden. Es können jedoch alle angepassten Attribute exportiert werden, indem Sie custom_attributes in das fields_to_export-Array aufnehmen (z.B. `['first_name', 'email', 'custom_attributes']`).
{% endalert %}

## Parameter der Anfrage

| Parameter           | Erforderlich  | Datentyp        | Beschreibung                                                                                                                                                    |
| ------------------- | --------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_endpoint` | Optional  | String           | Endpunkt, an den eine Download-URL gesendet wird, wenn der Export verfügbar ist.                                                                                               |
| `fields_to_export`  | Erforderlich* | String-Array | Name der zu exportierenden Nutzerdatenfelder. Sie können auch angepasste Attribute exportieren. <br><br>\*Ab April 2021 müssen neue Konten bestimmte Felder für den Export angeben. |
| `output_format`     | Optional  | String           | Wenn Sie Ihr eigenes S3-Bucket verwenden, ist es zulässig, das Dateiformat `zip` oder `gzip` anzugeben. Standardmäßig ist das ZIP-Dateiformat eingestellt.                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/global_control_group' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "callback_endpoint" : "",
  "fields_to_export" : ["email", "braze_id"],
  "output_format" : "zip"
}'
```

## Zu exportierende Felder

Im Folgenden finden Sie eine Liste der gültigen `fields_to_export`. Die Verwendung von `fields_to_export` zur Minimierung der zurückgegebenen Daten kann die Reaktionszeit dieses API-Endpunkts verbessern:

| Zu exportierendes Feld       | Datentyp       | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `apps`                | Array           | Apps, für die dieser Nutzer:innen Sitzungen angemeldet hat, einschließlich der Felder:<br><br>- `name`: Name der App<br>- `platform`: App-Plattform, wie iOS, Android oder Internet<br>- `version`: Versionsnummer oder Name der App <br>- `sessions`: Gesamtzahl der Sitzungen für diese App<br>- `first_used`: Datum der ersten Sitzung<br>- `last_used`: Datum der letzten Sitzung<br><br>Alle Felder sind Strings.                                                                                                                                                                                                                                                                                       |
| `attributed_campaign` | String          | Daten aus [Attribution Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für eine bestimmte Kampagne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `attributed_source`   | String          | Daten aus [Attribution Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für die Plattform, auf der die Anzeige geschaltet wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `attributed_adgroup`  | String          | Daten aus [Attribution Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb der Kampagne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `attributed_ad`       | String          | Daten aus [Attribution Integrationen]({{site.baseurl}}/partners/message_orchestration/), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb von Kampagne und Anzeigengruppe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `braze_id`            | String          | Gerätespezifischer eindeutiger Bezeichner, der von Braze für diesen Nutzer:innen festgelegt wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `country`             | String          | Das Land des Nutzers:in unter Verwendung des [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) Standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `created_at`          | String          | Datum und Uhrzeit der Erstellung des Nutzerprofils, im Format ISO 8601.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `custom_attributes`   | Objekt          | Angepasste Attribut-Schlüssel-Wert-Paare für diesen Nutzer:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `custom_events`       | Array           | Angepasste Events, die diesem Nutzer:in den letzten 90 Tagen zugeordnet wurden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `devices`             | Array           | Informationen über das Gerät des Nutzers:innen, die je nach Plattform Folgendes umfassen können:<br><br>- `model`: Modellname des Geräts<br>- `os`: Betriebssystem des Geräts<br>- `carrier`: Dienst des Geräts, falls verfügbar<br>- `idfv`: (iOS) Bezeichner des Braze Geräts, der Apple Identifier für Vendor, falls vorhanden<br>- `idfa`: (iOS) Bezeichner für Werbung, falls vorhanden<br>- `device_id`: (Android) Braze Gerät Bezeichner<br>- `google_ad_id`: (Android) Google Play Advertising Bezeichner, falls vorhanden<br>- `roku_ad_id`: (Roku) Roku Werbe-Bezeichner<br>- `ad_tracking_enabled`: Ob Ad Tracking auf dem Gerät aktiviert ist, kann true oder false sein. |
| `dob`                 | String          | Das Geburtsdatum des Nutzers:in im Format `YYYY-MM-DD`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `email`               | String          | E-Mail Adresse des Nutzers:innen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `external_id`         | String          | Eindeutiger Bezeichner für identifizierte Nutzer:innen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `first_name`          | String          | Der Vorname des Nutzers:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `gender`              | String          | Geschlecht des Nutzers:in. Mögliche Werte sind:<br><br>- `M`: männlich<br>- `F`: weiblich<br>- `O`: Sonstiges<br>- `N`: nicht anwendbar<br>- `P`: lieber nicht sagen<br>- `nil`: unbekannt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `home_city`           | String          | Der Heimatort des Nutzers:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `language`            | String          | Nutzer:in in der ISO-639-1-Norm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `last_coordinates`    | Array von Gleitkommazahlen | Der letzte Standort des Geräts des Nutzers, formatiert als `[longitude, latitude]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `last_name`           | String          | Der Nachname des Nutzers:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `phone`               | String          | Die Telefonnummer der Nutzer:in im Format E.164.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `purchase`s           | Array           | Einkäufe, die dieser Nutzer:innen in den letzten 90 Tagen getätigt hat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `random_bucket`       | Integer         | [Zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) des Nutzers, mit der gleichmäßig verteilte Segmente aus zufälligen Nutzer:innen erstellt werden.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | String          | Die Zeitzone des Nutzers:in im gleichen Format wie in der IANA-Zeitzonendatenbank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Gleitkommazahl           | Gesamteinnahmen, die diesem Nutzer:innen zugerechnet werden. Der Gesamtumsatz wird auf der Grundlage der Käufe berechnet, die die Nutzer:innen während der Konversionsfenster für die Kampagnen und Canvase, die sie erhalten haben, getätigt haben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Zeitstempel       | Datum und Uhrzeit der Deinstallation der App durch den Nutzer:innen. Entfällt, wenn die App nicht deinstalliert wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objekt          | [User-Aliases Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification), das die `alias_name` und `alias_label` enthält, falls vorhanden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example,'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Nachdem die URL zur Verfügung gestellt wurde, ist sie nur für einige Stunden gültig. Wir empfehlen Ihnen daher dringend, Ihre eigenen S3-Anmeldedaten zu Braze hinzuzufügen.

### Beispiel für die Ausgabe der Nutzer:innen-Exportdatei

Nutzer:in (wir nehmen so wenig Daten wie möglich auf - wenn ein Feld im Objekt fehlt, wird angenommen, dass es null oder leer ist):

{% tabs %}
{% tab Alle Felder %}

```json
{
    "created_at" : (string),
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string) ISO-3166-1 alpha-2 standard,
    "phone" : (string),
    "language" : (string) ISO-639-1 standard,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "custom_attributes" : (object) custom attribute key-value pairs,
    "custom_events" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
        "count" : (int)
      },
      ...
    ],
    "purchases" : [
      {
        "name" : (string),
        "first" : (string) date,
        "last" : (string) date,
         "count" : (int)
      },
      ...
    ],
    "devices" : [
      {
        "model" : (string),
        "os" : (string),
        "carrier" : (string),
        "idfv" : (string) only included for iOS devices when IDFV collection is enabled,
        "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
        "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
        "roku_ad_id" : (string) only included for Roku devices,
        "ad_tracking_enabled" : (bool)
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (string),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
}
```

{% endtab %}
{% tab Beispielhafte Ausgabe %}

```json
{
    "created_at" : "2020-07-10 15:00:00.000 UTC",
    "external_id" : "A8i3mkd99",
    "user_aliases" : [
      {
        "alias_name" : "user_123",
        "alias_label" : "amplitude_id"
      }
    ],
    "braze_id": "5fbd99bac125ca40511f2cb1",
    "random_bucket" : 2365,
    "first_name" : "Jane",
    "last_name" : "Doe",
    "email" : "example@braze.com",
    "dob" : "1980-12-21",
    "home_city" : "Chicago",
    "country" : "US",
    "phone" : "+442071838750",
    "language" : "en",
    "time_zone" : "Eastern Time (US & Canada)",
    "last_coordinates" : [41.84157636433568, -87.83520818508256],
    "gender" : "F",
    "total_revenue" : 65,
    "attributed_campaign" : "braze_test_campaign_072219",
    "attributed_source" : "braze_test_source_072219",
    "attributed_adgroup" : "braze_test_adgroup_072219",
    "attributed_ad" : "braze_test_ad_072219",
    "custom_attributes":
      {
        "loyaltyId": "37c98b9d-9a7f-4b2f-a125-d873c5152856",
        "loyaltyPoints": "321",
        "loyaltyPointsNumber": 107
      },
    "custom_events": [
      {
          "name": "Loyalty Acknowledgement",
          "first": "2021-06-28T17:02:43.032Z",
          "last": "2021-06-28T17:02:43.032Z",
          "count": 1
      },
      ...
    ],
    "purchases": [
      {
        "name": "item_40834",
        "first": "2021-09-05T03:45:50.540Z",
        "last": "2022-06-03T17:30:41.201Z",
        "count": 10
      },
      ...
    ],
    "devices": [
      {
        "model": "Pixel XL",
        "os": "Android (Q)",
        "carrier": null,
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "ad_tracking_enabled": true
      },
      ...
    ],
    "apps": [
      {
        "name": "MovieCannon",
        "platform": "Android",
        "version": "3.29.0",
        "sessions": 1129,
        "first_used": "2020-02-02T19:56:19.142Z",
        "last_used": "2021-11-11T00:25:19.201Z"
      },
      ...
    ],
}
```

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/

{% endapi %}

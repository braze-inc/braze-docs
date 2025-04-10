---
nav_title: "POST: Benutzerprofil nach globaler Kontrollgruppe exportieren"
article_title: "POST: Benutzerprofil nach globaler Kontrollgruppe exportieren"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts Benutzer exportieren in Globale Kontrollgruppen."

---
{% api %}
# Benutzerprofil nach Globaler Kontrollgruppe exportieren
{% apimethod post %}
/users/export/global_control_group
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Benutzer innerhalb einer globalen Kontrollgruppe zu exportieren.

Die Benutzerdaten werden als mehrere Dateien mit Benutzer-JSON-Objekten exportiert, die durch neue Zeilen getrennt sind (z.B. ein JSON-Objekt pro Zeile). Alle Benutzer in einer Globalen Kontrollgruppe werden jedes Mal, wenn die Dateien generiert werden, einbezogen. Braze speichert keine Historie darüber, wann Benutzer zu einer Globalen Kontrollgruppe hinzugefügt oder aus ihr entfernt werden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#aa3d8b90-d984-48f0-9287-57aa30469de2 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `users.export.global_control_group`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Details zur Credentials-basierten Antwort

Wenn Sie Ihre [S3-][1] oder [Azure-Zugangsdaten][2] zu Braze hinzugefügt haben, wird jede Datei in Ihrem Bucket als ZIP-Datei mit einem Schlüsselformat hochgeladen, das wie `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` aussieht. Wenn Sie Azure verwenden, vergewissern Sie sich, dass Sie auf der Azure-Partner-Übersichtsseite in Braze das Kontrollkästchen **Dies als Standardziel für den Datenexport festlegen** aktiviert haben. In der Regel erstellen wir 1 Datei pro 5.000 Benutzer, um die Verarbeitung zu optimieren. Das Exportieren kleinerer Segmente innerhalb eines großen Arbeitsbereichs kann zu mehreren Dateien führen. Sie können dann die Dateien extrahieren und bei Bedarf alle `json` Dateien zu einer einzigen Datei zusammenfügen. Wenn Sie eine `output_format` von `gzip` angeben, lautet die Dateierweiterung `.gz` statt `.zip`.

{% details Aufschlüsselung der Exportpfade für ZIP %}
**ZIP-Format:**
`bucket-name/segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip`

**Beispiel ZIP:**
`braze.docs.bucket/segment-export/abc56c0c-rd4a-pb0a-870pdf4db07q/2019-04-25/d9696570-dfb7-45ae-baa2-25e302r2da27-1556044807/114f0226319130e1a4770f2602b5639a.zip`

| Eigentum | Details | Im Beispiel dargestellt als |
|---|---|
| `bucket-name` | Basierend auf dem Namen Ihres Eimers festgelegt. | `braze.docs.bucket` |
| `segment-export` | Behoben. | `segment-export` |
| `SEGMENT_ID` | In der Exportanfrage enthalten. | `abc56c0c-rd4a-pb0a-870pdf4db07q` |
| `YYYY-MM-dd` | Das Datum, an dem der erfolgreiche Rückruf empfangen wurde. | `2019-04-25` |
| `RANDOM_UUID` | Eine zufällige UUID, die von Braze zum Zeitpunkt der Anfrage generiert wird. | `d9696570-dfb7-45ae-baa2-25e302r2da27` |
| `TIMESTAMP_WHEN_EXPORT_STARTED` | Unix-Zeit (Sekunden seit 2017-01-01:00:00:00Z), zu der der Export in UTC angefordert wurde. | `1556044807` |
| `filename` | Zufällig pro Datei. | `114f0226319130e1a4770f2602b5639a` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% enddetails %}

Wir empfehlen dringend, Ihre eigenen S3- oder Azure-Anmeldedaten einzurichten, wenn Sie diesen Endpunkt verwenden, um Ihre eigenen Bucket-Richtlinien für den Export durchzusetzen. Wenn Sie keine Anmeldedaten für Ihren Cloud-Speicher haben, wird in der Antwort auf die Anfrage die URL angegeben, unter der Sie eine ZIP-Datei mit allen Benutzerdateien herunterladen können. Die URL wird erst dann ein gültiger Speicherort, wenn der Export abgeschlossen ist.

Beachten Sie, dass die Menge der Daten, die Sie von diesem Endpunkt aus exportieren können, begrenzt ist, wenn Sie Ihre Anmeldedaten für den Cloud-Speicher nicht angeben. Je nach den Feldern, die Sie exportieren, und der Anzahl der Benutzer kann die Dateiübertragung fehlschlagen, wenn sie zu groß ist. Am besten legen Sie fest, welche Felder Sie exportieren möchten, indem Sie `fields_to_export` verwenden und nur die Felder angeben, die Sie benötigen, um die Größe der Übertragung gering zu halten. Wenn Sie bei der Generierung der Datei Fehler erhalten, sollten Sie in Erwägung ziehen, Ihre Benutzerbasis auf der Grundlage einer zufälligen Bereichsnummer in mehrere Segmente aufzuteilen (erstellen Sie z.B. ein Segment, bei dem die zufällige Bereichsnummer kleiner als 1.000 oder zwischen 1.000 und 2.000 ist).

In beiden Szenarien können Sie optional eine `callback_endpoint` angeben, um benachrichtigt zu werden, wenn der Export fertig ist. Wenn Sie die Adresse `callback_endpoint` angeben, werden wir eine Postanforderung an die angegebene Adresse senden, sobald der Download fertig ist. Der Text des Beitrags lautet "Erfolg":true. Wenn Sie Ihre Cloud-Speicheranmeldedaten nicht zu Braze hinzugefügt haben, enthält der Textkörper des Beitrags zusätzlich das Attribut `url` mit der Download-URL als Wert.

Größere Benutzerbasen führen zu längeren Exportzeiten. Eine App mit 20 Millionen Nutzern könnte zum Beispiel eine Stunde oder länger dauern.

## Körper der Anfrage

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
Einzelne benutzerdefinierte Attribute können nicht exportiert werden. Sie können jedoch alle benutzerdefinierten Attribute exportieren, indem Sie custom_attributes in das Array fields_to_export aufnehmen (zum Beispiel `['first_name', 'email', 'custom_attributes']`).
{% endalert %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --- | ----------- | --------- | ------- |
|`callback_endpoint` | Optional | String | Endpunkt, an den eine Download-URL gesendet wird, wenn der Export verfügbar ist. |
|`fields_to_export` | Erforderlich* | Array von Zeichenketten | Name der zu exportierenden Benutzerdatenfelder. Sie können auch benutzerdefinierte Attribute exportieren. <br><br>\*Ab April 2021 müssen neue Konten bestimmte Felder für den Export angeben. |
|`output_format` | Optional | String | Wenn Sie Ihren eigenen S3-Bucket verwenden, können Sie das Dateiformat als `zip` oder `gzip` angeben. Standardmäßig ist das ZIP-Dateiformat eingestellt. |
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

Im Folgenden finden Sie eine Liste der gültigen `fields_to_export`. Die Verwendung von `fields_to_export` zur Minimierung der zurückgegebenen Daten kann die Antwortzeit dieses API-Endpunkts verbessern:

| Zu exportierendes Feld | Datentyp | Beschreibung |
|---|---|---|
| `apps` | Array | Apps, für die dieser Benutzer Sitzungen angemeldet hat, mit den Feldern:<br><br>- `name`: Name der Anwendung<br>- `platform`: App-Plattform, wie iOS, Android oder Web<br>- `version`: Versionsnummer oder Name der App <br>- `sessions`: Gesamtzahl der Sitzungen für diese App<br>- `first_used`: Datum der ersten Sitzung<br>- `last_used`: Datum der letzten Sitzung<br><br>Alle Felder sind Zeichenketten. |
| `attributed_campaign` | String | Daten aus [Attributionsintegrationen]({{site.baseurl}}/partners/message_orchestration/attribution), falls eingerichtet. Kennung für eine bestimmte Anzeigenkampagne. |
| `attributed_source` | String | Daten aus [Attributionsintegrationen]({{site.baseurl}}/partners/message_orchestration/attribution), falls eingerichtet. Kennung für die Plattform, auf der die Anzeige geschaltet wurde. |
| `attributed_adgroup` | String | Daten aus [Attributionsintegrationen]({{site.baseurl}}/partners/message_orchestration/attribution), falls eingerichtet. Identifikator für eine optionale Untergruppierung unterhalb der Kampagne. |
| `attributed_ad` | String | Daten aus [Attributionsintegrationen]({{site.baseurl}}/partners/message_orchestration/attribution), falls eingerichtet. Bezeichner für eine optionale Untergruppierung unterhalb von Kampagne und Anzeigengruppe. |
| `braze_id` | String | Gerätespezifischer eindeutiger Benutzeridentifikator, der von Braze für diesen Benutzer festgelegt wurde. |
| `country` | String | Das Land des Benutzers unter Verwendung des [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) Standards. |
| `created_at` | String | Datum und Uhrzeit, zu der das Benutzerprofil erstellt wurde, im Format ISO 8601. |
| `custom_attributes` | Objekt | Benutzerdefinierte Attribut-Schlüssel-Wert-Paare für diesen Benutzer. |
| `custom_events` | Array | Benutzerdefinierte Ereignisse, die diesem Benutzer in den letzten 90 Tagen zugewiesen wurden. |
| `devices` | Array | Informationen über das Gerät des Benutzers, die je nach Plattform Folgendes umfassen können:<br><br>- `model`: Name des Gerätemodells<br>- `os`: Das Betriebssystem des Geräts<br>- `carrier`: Serviceanbieter des Geräts, falls verfügbar<br>- `idfv`: (iOS) Braze-Gerätekennung, die Apple-Kennung für Vendor, falls vorhanden<br>- `idfa`: (iOS) Identifikator für Werbung, falls vorhanden<br>- `device_id`: (Android) Kennung des Braze-Geräts<br>- `google_ad_id`: (Android) Google Play Advertising Identifier, falls vorhanden<br>- `roku_ad_id`: (Roku) Roku Werbekennzeichen<br>- `ad_tracking_enabled`: Wenn die Anzeigenverfolgung auf dem Gerät aktiviert ist, kann true oder false sein. |
| `dob` | String | Das Geburtsdatum des Benutzers im Format `YYYY-MM-DD`. |
| `email` | String | Die E-Mail-Adresse des Benutzers. |
| `external_id` | String | Eindeutiger Benutzeridentifikator für identifizierte Benutzer. |
| `first_name` | String | Der Vorname des Benutzers. |
| `gender` | String | Das Geschlecht des Benutzers. Mögliche Werte sind:<br><br>- `M`: männlich<br>- `F`: weiblich<br>- `O`: Sonstiges<br>- `N`: nicht anwendbar<br>- `P`: lieber nicht sagen<br>- `nil`: unbekannt |
| `home_city` | String | Die Heimatstadt des Benutzers. |
| `language` | String | Benutzersprache im ISO-639-1 Standard. |
| `last_coordinates` | Array von Floats | Der letzte Standort des Geräts des Benutzers, formatiert als `[longitude, latitude]`. |
| `last_name` | String | Der Nachname des Benutzers. |
| `phone` | String | Die Telefonnummer des Benutzers im Format E.164. |
| `purchase`s | Array | Einkäufe, die dieser Benutzer in den letzten 90 Tagen getätigt hat. |
| `random_bucket` | Integer | Die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) des Benutzers, die verwendet wird, um gleichmäßig verteilte Segmente von zufälligen Benutzern zu erstellen. |
| `time_zone` | String | Die Zeitzone des Benutzers im gleichen Format wie die IANA-Zeitzonendatenbank. |
| `total_revenue` | Schwimmer | Gesamteinnahmen, die diesem Benutzer zugerechnet werden. Der Gesamtumsatz wird auf der Grundlage der Käufe berechnet, die der Nutzer während der Conversion-Fenster für die Kampagnen und Canvases, die er erhalten hat, getätigt hat. |
| `uninstalled_at` | Zeitstempel | Datum und Uhrzeit der Deinstallation der App durch den Benutzer. Entfällt, wenn die App nicht deinstalliert wurde. |
| `user_aliases` | Objekt | [Benutzer-Aliasobjekt]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification), das die `alias_name` und `alias_label` enthält, falls vorhanden. |
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

Nachdem die URL zur Verfügung gestellt wurde, ist sie nur für einige Stunden gültig. Wir empfehlen Ihnen daher dringend, Ihre eigenen S3-Zugangsdaten zu Braze hinzuzufügen.

### Beispiel für die Ausgabe einer Benutzer-Exportdatei

Benutzerexportobjekt (wir werden so wenig Daten wie möglich einfügen - wenn ein Feld im Objekt fehlt, sollte es als null, falsch oder leer angenommen werden):

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

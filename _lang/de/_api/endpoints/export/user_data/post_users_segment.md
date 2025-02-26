---
nav_title: "POST: Benutzerprofil nach Segment exportieren"
article_title: "POST: Benutzerprofil nach Segment exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details über den Braze-Endpunkt Benutzer nach Segment exportieren."

---
{% api %}
# Benutzerprofil nach Segment exportieren
{% apimethod post %}
/users/export/segment
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um alle Benutzer innerhalb eines Segments zu exportieren. 

{% alert important %}
Wenn Sie diesen Endpunkt verwenden, beachten Sie Folgendes:<br><br>1\. Das Feld `fields_to_export` in dieser API-Anfrage ist **erforderlich**.<br>2\. Die Felder für `custom_events`, `purchases`, `campaigns_received` und `canvases_received` enthalten nur Daten der letzten 90 Tage.
{% endalert %}

Die Benutzerdaten werden als mehrere Dateien mit Benutzer-JSON-Objekten exportiert, die durch neue Zeilen getrennt sind (z.B. ein JSON-Objekt pro Zeile). Die Daten werden in eine automatisch generierte URL oder in einen S3-Bucket exportiert, wenn diese Integration bereits eingerichtet ist.

Beachten Sie, dass ein Unternehmen zu einem bestimmten Zeitpunkt höchstens einen Export pro Segment über diesen Endpunkt durchführen kann. Warten Sie, bis Ihr Export abgeschlossen ist, bevor Sie es erneut versuchen. 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#cfa6fa98-632c-4f25-8789-6c3f220b9457 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `users.export.segment`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Details zur Credentials-basierten Antwort

Wenn Sie Ihre [S3-][1], [Azure-][2] oder [Google Cloud Storage-Zugangsdaten][3] zu Braze hinzugefügt haben, wird jede Datei in Ihrem Bucket als ZIP-Datei mit einem Schlüsselformat hochgeladen, das wie `segment-export/SEGMENT_ID/YYYY-MM-dd/RANDOM_UUID-TIMESTAMP_WHEN_EXPORT_STARTED/filename.zip` aussieht. Wenn Sie Azure verwenden, vergewissern Sie sich, dass Sie auf der Azure-Partner-Übersichtsseite in Braze das Kontrollkästchen **Dies als Standardziel für den Datenexport festlegen** aktiviert haben. In der Regel erstellen wir 1 Datei pro 5.000 Benutzer, um die Verarbeitung zu optimieren. Das Exportieren kleinerer Segmente innerhalb eines großen Arbeitsbereichs kann zu mehreren Dateien führen. Sie können die Dateien dann extrahieren und bei Bedarf alle `json` Dateien zu einer einzigen Datei zusammenfügen. Wenn Sie eine `output_format` von `gzip` angeben, lautet die Dateierweiterung `.gz` statt `.zip`.

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

Wir empfehlen dringend, Ihre eigenen S3- oder Azure-Anmeldedaten einzurichten, wenn Sie diesen Endpunkt verwenden, um Ihre eigenen Bucket-Richtlinien für den Export durchzusetzen. Wenn Sie keine Zugangsdaten für Ihren Cloud-Speicher haben, enthält die Antwort auf die Anfrage die URL, unter der Sie eine ZIP-Datei mit allen Benutzerdateien herunterladen können. Die URL wird erst dann ein gültiger Speicherort, wenn der Export abgeschlossen ist. 

Beachten Sie, dass die Menge der Daten, die Sie von diesem Endpunkt aus exportieren können, begrenzt ist, wenn Sie Ihre Anmeldedaten für den Cloud-Speicher nicht angeben. Je nach den Feldern, die Sie exportieren, und der Anzahl der Benutzer kann die Dateiübertragung fehlschlagen, wenn sie zu groß ist. Am besten legen Sie fest, welche Felder Sie mit `fields_to_export` exportieren möchten und geben nur die Felder an, die Sie benötigen, um den Umfang der Übertragung gering zu halten. Wenn Sie bei der Generierung der Datei Fehler erhalten, sollten Sie in Erwägung ziehen, Ihre Benutzerbasis in mehrere Segmente zu unterteilen, die auf einer zufälligen Bucket-Nummer basieren (erstellen Sie beispielsweise ein Segment, bei dem die zufällige Bucket-Nummer kleiner als 1.000 oder zwischen 1.000 und 2.000 ist).

In beiden Szenarien können Sie optional eine `callback_endpoint` angeben, um benachrichtigt zu werden, wenn der Export fertig ist. Wenn Sie die Adresse `callback_endpoint` angeben, werden wir eine Postanforderung an die angegebene Adresse senden, sobald der Download fertig ist. Der Text des Beitrags lautet "Erfolg":true. Wenn Sie Braze keine S3-Anmeldeinformationen hinzugefügt haben, enthält der Textkörper des Beitrags zusätzlich das Attribut `url` mit der Download-URL als Wert.

Größere Benutzerbasen führen zu längeren Exportzeiten. Eine App mit 20 Millionen Nutzern könnte zum Beispiel eine Stunde oder länger dauern.

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "segment_id" : (required, string) identifier for the segment to be exported,
  "callback_endpoint" : (optional, string) endpoint to post a download URL when the export is available,
  "fields_to_export" : (required, array of string) name of user data fields to export, you may also export custom attributes. New accounts must specify specific fields to export,
  "output_format" : (optional, string) when using your own S3 bucket,  specifies file format as 'zip' or 'gzip'. Defaults to ZIP file format
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
|`segment_id` | Erforderlich | String | Bezeichner für das zu exportierende Segment. Siehe [Segmentbezeichner]({{site.baseurl}}/api/identifier_types/).<br><br>Die `segment_id` für ein bestimmtes Segment finden Sie auf der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) in Ihrem Braze-Konto oder Sie können den [Endpunkt Segmentliste]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) verwenden.|
|`callback_endpoint` | Optional | String | Endpunkt, an den eine Download-URL gesendet wird, wenn der Export verfügbar ist. |
|`fields_to_export` | Erforderlich* | Array von Zeichenketten | Name der zu exportierenden Benutzerdatenfelder. Sie können auch alle benutzerdefinierten Attribute exportieren, indem Sie `custom_attributes` in diesem Parameter angeben. <br><br>\*Ab April 2021 müssen neue Konten bestimmte Felder für den Export angeben. |
| `custom_attributes_to_export` | Optional | Array von Zeichenketten | Name des spezifischen benutzerdefinierten Attributs, das exportiert werden soll. Es können bis zu 500 benutzerdefinierte Attribute exportiert werden. Um benutzerdefinierte Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > **Benutzerdefinierte Attribute**. |
|`output_format` | Optional | String | Das Ausgabeformat Ihrer Datei. Standardmäßig ist das Dateiformat `zip` eingestellt. Wenn Sie Ihren eigenen S3-Bucket verwenden, können Sie `zip` oder `gzip` angeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Wenn `custom_attributes` im Parameter `fields_to_export` enthalten ist, werden alle benutzerdefinierten Attribute exportiert, unabhängig davon, was in `custom_attributes_to_export` steht. Wenn Ihr Ziel darin besteht, bestimmte Attribute zu exportieren, sollte `custom_attributes` nicht in den Parameter `fields_to_export` aufgenommen werden. Verwenden Sie stattdessen den Parameter `custom_attributes_to_export`.
{% endalert %}

## Beispielanfrage zum Export aller benutzerdefinierten Attribute
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases", "custom_attributes"],
  "output_format" : "zip"
}'
```

## Beispielanfrage zum Export bestimmter benutzerdefinierter Attribute
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/segment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "segment_id" : "segment_identifier",
  "callback_endpoint" : "example_endpoint",
  "fields_to_export" : ["first_name", "email", "purchases"],
  "custom_attributes_to_export" : ["allergies", "favorite_food"],
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
| `purchases` | Array | Einkäufe, die dieser Benutzer in den letzten 90 Tagen getätigt hat. |
| `push_tokens` | Array | Informationen über die Push-Tokens des Benutzers. |
| `random_bucket` | Integer | Die [zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) des Benutzers, die verwendet wird, um gleichmäßig verteilte Segmente von zufälligen Benutzern zu erstellen. |
| `time_zone` | String | Die Zeitzone des Benutzers im gleichen Format wie die IANA-Zeitzonendatenbank. |
| `total_revenue` | Schwimmer | Gesamteinnahmen, die diesem Benutzer zugerechnet werden. Der Gesamtumsatz wird auf der Grundlage der Käufe berechnet, die der Nutzer während der Conversion-Fenster für die Kampagnen und Canvases, die er erhalten hat, getätigt hat. |
| `uninstalled_at` | Zeitstempel | Datum und Uhrzeit der Deinstallation der App durch den Benutzer. Entfällt, wenn die App nicht deinstalliert wurde. |
| `user_aliases` | Objekt | [Benutzer-Aliasobjekt]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification), das die `alias_name` und `alias_label` enthält, falls vorhanden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Wichtige Mahnungen

- Die Felder für `custom_events`, `purchases`, `campaigns_received` und `canvases_received` enthalten nur die Daten der letzten 90 Tage.
- Sowohl `custom_events` als auch `purchases` enthalten Felder für `first` und `count`. Beide Felder werden Informationen aus der gesamten Zeit widerspiegeln und nicht nur auf die Daten der letzten 90 Tage beschränkt sein. Wenn zum Beispiel ein bestimmter Benutzer das Ereignis vor 90 Tagen zum ersten Mal durchgeführt hat, wird dies im Feld `first` genau wiedergegeben, und das Feld `count` berücksichtigt auch Ereignisse, die vor den letzten 90 Tagen stattgefunden haben.
- Die Anzahl der gleichzeitigen Segmentexporte, die ein Unternehmen auf Endpunktebene durchführen kann, ist auf 100 begrenzt. Versuche, die dieses Limit überschreiten, führen zu einem Fehler.
- Der Versuch, ein Segment ein zweites Mal zu exportieren, während der erste Exportauftrag noch läuft, führt zu einem Fehler 429.

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, for example, 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Nachdem die URL zur Verfügung gestellt wurde, ist sie nur für einige Stunden gültig. Wir empfehlen Ihnen daher dringend, Ihre eigenen S3-Zugangsdaten zu Braze hinzuzufügen.

## Beispiel für die Ausgabe einer Benutzer-Exportdatei

Benutzerexportobjekt (wir werden so wenig Daten wie möglich einfügen - wenn ein Feld im Objekt fehlt, sollte es als null, falsch oder leer angenommen werden):

{% tabs %}
{% tab Alle Felder %}

```json
{
    "created_at": (string),
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
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
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
        "ad_tracking_enabled" : (boolean)
      },
      ...
    ],
    "push_tokens" : [
      {
        "app" : (string) app name,
        "platform" : (string),
        "token" : (string),
        "device_id": (string),
        "notifications_enabled": (boolean) whether the user's push notifications are turned on or turned off
      },
      ...
    ],
    "apps" : [
      {
        "name" : (string),
        "platform" : (string),
        "version" : (string),
        "sessions" : (integer),
        "first_used" : (string) date,
        "last_used" : (string) date
      },
      ...
    ],
    "campaigns_received" : [
      {
        "name" : (string),
        "last_received" : (string) date,
        "engaged" : 
         {
           "opened_email" : (boolean),
           "opened_push" : (boolean),
           "clicked_email" : (boolean),
           "clicked_triggered_in_app_message" : (boolean)
          },
          "converted" : (boolean),
          "api_campaign_id" : (string),
          "variation_name" : (optional, string) exists only if it is a multivariate campaign,
          "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
          "in_control" : (optional, boolean) exists only if it is a multivariate campaign
        },
      ...
    ],
    "canvases_received": [
      {
        "name": (string),
        "api_canvas_id": (string),
        "last_received_message": (string) date,
        "last_entered": (string) date,
        "variation_name": (string),
        "in_control": (boolean),
        "last_exited": (string) date,
        "steps_received": [
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          },
          {
            "name": (string),
            "api_canvas_step_id": (string),
            "last_received": (string) date
          }
        ]
      },
      ...
    ],
    "cards_clicked" : [
      {
        "name" : (string)
      },
      ...
    ]
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
    "push_subscribe" : "opted_in", 
    "push_opted_in_at": "2020-01-26T22:45:53.953Z",
    "email_subscribe" : "subscribed",
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
    "push_tokens": [
      {
        "app": "MovieCanon",
        "platform": "Android",
        "token": "12345abcd",
        "device_id": "312ef2c1-83db-4789-967-554545a1bf7a",
        "notifications_enabled": true
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
    "campaigns_received": [
      {
        "name": "Email Unsubscribe",
        "api_campaign_id": "d72fdc84-ddda-44f1-a0d5-0e79f47ef942",
        "last_received": "2022-06-02T03:07:38.105Z",
        "engaged": 
        {
           "opened_email": true
        },
        "converted": true,
        "multiple_converted": 
        {
          "Primary Conversion Event - A": true
        },
        "in_control": false,
        "variation_name": "Variant 1",
        "variation_api_id": "1bddc73a-a134-4784-9134-5b5574a9e0b8"
      },
      ...
    ],
    "canvases_received": [
      {
        "name": "Non Global  Holdout Group 4/21/21",
        "api_canvas_id": "46972a9d-dc81-473f-aa03-e3473b4ed781",
        "last_received_message": "2021-07-07T20:46:24.136Z",
        "last_entered": "2021-07-07T20:45:24.000+00:00",
        "variation_name": "Variant 1",
        "in_control": false,
        "last_entered_control_at": null,
        "last_exited": "2021-07-07T20:46:24.136Z",
        "steps_received": [
          {
            "name": "Step",
            "api_canvas_step_id": "43d1a349-c3c8-4be1-9fbe-ce708e4d1c39",
            "last_received": "2021-07-07T20:46:24.136Z"
          },
          ...
        ]
      }
      ...
    ],    
    "cards_clicked" : [
      {
        "name" : "Loyalty Promo"
      },
      ...
    ]
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Hilfe zum CSV- und API-Export finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %}

[1]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3
[2]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents/
[3]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/google_cloud_storage_for_currents/

{% endapi %}

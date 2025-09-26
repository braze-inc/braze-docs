---
nav_title: "POST: Nutzerprofil nach Bezeichner exportieren"
article_title: "POST: Nutzerprofil nach Bezeichner exportieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Endpunkt Nutzer:innen nach Bezeichner exportieren von Braze."

---
{% api %}
# Nutzerprofil nach Bezeichner exportieren
{% apimethod post %}
/users/export/ids
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Daten aus einem beliebigen Nutzerprofil zu exportieren, indem Sie einen Bezeichner für den Benutzer angeben.

Bis zu 50 `external_ids` oder `user_aliases` können in einer einzigen Anfrage enthalten sein. Wenn Sie `device_id`, `email_address` oder `phone` angeben möchten, kann nur einer der Bezeichner pro Anfrage angegeben werden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#b9750447-9d94-4263-967f-f816f0c76577 {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `users.export.ids`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='users export ids' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids": (optional, array of strings) External identifiers for users you wish to export,
  "user_aliases": (optional, array of user alias objects) user aliases for users to export,
  "device_id": (optional, string) Device identifier as returned by various SDK methods such as `getDeviceId`,
  "braze_id": (optional, string) Braze identifier for a particular user,
  "email_address": (optional, string) Email address of user,
  "phone": (optional, string) Phone number of user,
  "fields_to_export": (required, array of strings) Name of user data fields to export
}
```

{% alert note %}
Für Kund:in, die am oder nach dem 22\. August 2024 mit Braze Onboarding betrieben haben, ist der Anfrageparameter `fields_to_export` erforderlich.
{% endalert %}

## Parameter der Anfrage

| Parameter          | Erforderlich | Datentyp                                                     | Beschreibung                                                                                  |
| ------------------ | -------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `external_ids`     | Optional | String-Array                                              | Externe Bezeichner für Nutzer:innen, die Sie exportieren möchten.                                              |
| `user_aliases`     | Optional | Array des Nutzer:in-Alias-Objekts                                    | [User-Aliasing]({{site.baseurl}}/api/objects_filters/user_alias_object/) für Nutzer:innen zum Exportieren. |
| `device_id`        | Optional | String                                                        | Bezeichner des Geräts, wie er von verschiedenen SDK-Methoden wie `getDeviceId` zurückgegeben wird.                 |
| `braze_id`         | Optional | String                                                        | Braze-Bezeichner für einen bestimmten Nutzer:in.                                                      |
| `email_address`    | Optional | String                                                        | E-Mail Adresse des Nutzers:innen.                                                                       |
| `phone`            | Optional | String in [E.164](https://en.wikipedia.org/wiki/E.164) Format | Telefonnummer des Nutzers:innen.                                                                        |
| `fields_to_export` | Erforderlich | String-Array                                              | Name der zu exportierenden Nutzerdatenfelder.                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/export/ids' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids": ["user_identifier1", "user_identifier2"],
  "user_aliases": [
    {
      "alias_name": "example_alias",
      "alias_label": "example_label"
    }
  ],
  "device_id": "1234567",
  "braze_id": "braze_identifier",
  "email_address": "example@braze.com",
  "phone": "11112223333",
  "fields_to_export": ["first_name", "email", "purchases"]
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
| `push_subscribe`      | String          | Status des Push-Abos des Nutzers:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `email_subscribe`     | String          | Status des E-Mail-Abos des Nutzers:in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
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
| `purchases`           | Array           | Einkäufe, die dieser Nutzer:innen in den letzten 90 Tagen getätigt hat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `push_tokens`         | Array           | Eindeutiger anonymer Bezeichner, der angibt, wohin die Benachrichtigungen einer App gesendet werden sollen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `random_bucket`       | Integer         | [Zufällige Bucket-Nummer]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events#random-bucket-number-event) des Nutzers, mit der gleichmäßig verteilte Segmente aus zufälligen Nutzer:innen erstellt werden.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `time_zone`           | String          | Die Zeitzone des Nutzers:in im gleichen Format wie in der IANA-Zeitzonendatenbank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `total_revenue`       | Gleitkommazahl           | Gesamteinnahmen, die diesem Nutzer:innen zugerechnet werden. Der Gesamtumsatz wird auf der Grundlage der Käufe berechnet, die die Nutzer:innen während der Konversionsfenster für die Kampagnen und Canvase, die sie erhalten haben, getätigt haben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `uninstalled_at`      | Zeitstempel       | Datum und Uhrzeit der Deinstallation der App durch den Nutzer:innen. Entfällt, wenn die App nicht deinstalliert wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `user_aliases`        | Objekt          | [User-Aliases Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification), das die `alias_name` und `alias_label` enthält, falls vorhanden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Beachten Sie, dass der Endpunkt `/users/export/ids` das gesamte Benutzerprofil dieses Benutzers zusammenfasst, einschließlich Daten wie alle erhaltenen Kampagnen und Canvase, alle angepassten Events, alle getätigten Käufe und alle angepassten Attribute. Infolgedessen ist dieser Endpunkt langsamer als andere REST API Endpunkte.

Abhängig von den angefragten Daten reicht dieser API Endpunkt aufgrund des Rate-Limits von 250 Anfragen pro Minute möglicherweise nicht aus, um Ihre Anforderungen zu erfüllen. Wenn Sie diesen Endpunkt regelmäßig zum Exportieren von Nutzern verwenden möchten, sollten Sie stattdessen den Export von Nutzer:innen nach Segmenten in Erwägung ziehen, der asynchron erfolgt und für größere Datenabrufe optimiert ist.

## Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

Ein Beispiel für die Daten, die über diesen Endpunkt zugänglich sind, finden Sie im folgenden Beispiel.

### Beispiel für die Ausgabe der Nutzer:innen-Exportdatei

Nutzer:in (wir nehmen so wenig Daten wie möglich auf - wenn ein Feld im Objekt fehlt, wird angenommen, dass es null oder leer ist):

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
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}

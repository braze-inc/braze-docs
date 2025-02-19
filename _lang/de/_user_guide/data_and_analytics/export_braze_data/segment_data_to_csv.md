---
nav_title: Daten der Segmente in CSV exportieren
article_title: Daten der Segmente in CSV exportieren
page_order: 2
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Segmentdaten in eine CSV-Datei exportieren können."

---

# Exportieren von Segmentdaten nach CSV

> Auf dieser Seite erfahren Sie, wie Sie einen CSV-Export von Nutzer:innen eines Segments anfragen können und welche Daten im Export enthalten sind.

Um Segmentdaten in eine CSV-Datei zu exportieren, wählen Sie bei der Bearbeitung eines Segments das Dropdown-Menü **Nutzerdaten** aus und wählen Sie, ob Sie die Nutzerdaten oder die E-Mail-Adressen für das Segment exportieren möchten.

![Abschnitt Segmente Details mit Nutzerdaten-Dropdown mit Exportoptionen.][1]

Sie können einen CSV-Export auch von der Hauptseite **Segmente** aus anfragen, indem Sie das Dropdown-Menü <i class="fas fa-gear"></i> **Einstellungen** für ein Segment auswählen:

![Dropdown-Menü Einstellungen auf der Hauptseite Segmente.][2]

{% alert tip %}
Um Daten aus all Ihren Nutzerprofilen zu exportieren, erstellen Sie ein Segment ohne Filter und fordern dann einen CSV-Export an.
{% endalert %}

Die CSV-Ausgabe enthält die Daten der einzelnen Nutzerprofile, die zum Zeitpunkt des Exports im Segment erfasst wurden. Sie können jedes Segment exportieren, indem Sie das Zahnradsymbol und CSV-Export auswählen. Braze erstellt den Bericht im Hintergrund und mailt ihn an die Nutzer:innen, die gerade angemeldet sind.

{% alert important %}
Aufgrund von Dateigrößenbeschränkungen kann Ihr Export fehlschlagen, wenn die geschätzte Größe Ihres Segments über 500.000 Nutzer:innen liegt. Beachten Sie, dass diese Einschränkung die geschätzte Größe Ihres Segments verwendet und nicht die genaue Berechnung. Weitere Einzelheiten finden Sie unter [Exportieren großer Segmente]({{site.baseurl}}/help/help_articles/segments/exporting_large_segments/).
{% endalert %}

Wenn Sie Ihre [Amazon S3-Zugangsdaten][26] mit Braze verknüpft haben, wird die CSV stattdessen in Ihrem S3-Bucket unter dem Schlüssel `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` hochgeladen. Der Link, der Ihnen per E-Mail zugeschickt wurde, läuft nach einem Tag ab und erfordert, dass Sie für den Zugriff im Dashboard angemeldet sind.

## Im Export enthaltene Daten

Abhängig von Ihrer Auswahl ist Folgendes in Ihrem Export enthalten.

### Nutzerdaten als CSV exportieren

| Feldname                  | Beschreibung                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | Interne ID (kann nicht geändert werden)                           |
| Land                     | Land                                    |
| erstellt_am                  | Datum und Uhrzeit, zu der das Nutzerprofil erstellt wurde                   |
| Geräte                     | Informationen zum Gerät                           |
| date_of_birth               | Geburtsdatum                                            |
| E-Mail                       | E-Mail-Adresse                                            |
| unsubscribed_from_emails_at | Datum der Abmeldung von E-Mails                            |
| user_id                     | Externe ID                                              |
| first_name                  | Vorname                                               |
| first_session               | Datum und Uhrzeit der ersten Sitzung                           |
| Geschlecht                      | Geschlecht                                                   |
| google_ad_ids               | Mit dem Nutzer:innen verbundene Google-Werbe-IDs                      |
| Ort                        | Ort                                     |
| IDFAs (Identifier for Advertisers)                       | Identifier for Advertisers (IDFA) Werte                 |
| IDFVs (Identifier for Vendors)                       | Identifier for Vendors (IDFV) Werte                      |
| Sprache                    | Sprache im ISO-639-1-Standard                                        |
| last_app_version_used       | Zuletzt verwendete Version der App                             |
| last_name                   | Nachname                                                |
| last_session                | Datum und Uhrzeit der letzten Sitzung                            |
| number_of_google_ad_ids     | Anzahl der zugehörigen Google Werbe-IDs               |
| number_of_IDFAs             | Anzahl der zugehörigen IDFAs (Identifier for Advertisers)                                |
| number_of_IDFVs             | Anzahl der zugehörigen IDFVs (Identifier for Vendors)                                |
| number_of_push_tokens       | Anzahl der zugehörigen Token für Push-Benachrichtigungen             |
| number_of_roku_ad_ids       | Anzahl der zugehörigen Roku Werbe IDs                 |
| number_of_windows_ad_ids    | Anzahl der zugehörigen Windows-Werbe-IDs              |
| phone_number                | Telefonnummer                                             |
| opted_into_push_at          | Datum, an dem Sie für Push-Benachrichtigungen optiert haben                       |
| unsubscribed_from_push_at   | Datum, an dem Sie sich von Push-Benachrichtigungen abgemeldet haben                |
| random_bucket               | Zufällige Bucket-Nummer                                 |
| roku_ad_ids                 | Roku Werbung IDs                          |
| session_count               | Gesamtzahl der Sitzungen                                 |
| Zeitzone                    | Nutzer:in Zeitzone im gleichen Format wie in der IANA-Zeitzonendatenbank                                         |
| in_app_purchase_total       | Gesamtbetrag, der für In-App-Käufe ausgegeben wurde                   |
| user_aliases                | Nutzer:in, falls vorhanden                                          |
| windows_ad_ids              | Windows Werbe-IDs                       |
| Angepasste Events               | Basierend auf der Auswahl beim Export                             |
| Angepasste Attribute           | Basierend auf der Auswahl beim Export                             |
{: .reset-td-br-1 .reset-td-br-2 }

### E-Mail-Adressen als CSV exportieren

| Feldname                  | Beschreibung            |
| --------------------------- | ---------------------- |
| user_id                     | Externe ID des Nutzers:in     |
| first_name                  | Vorname             |
| last_name                   | Nachname              |
| E-Mail                       | E-Mail                  |
| unsubscribed_from_emails_at | Datum der Abmeldung von E-Mails |
| opted_in_to_emails_at       | Datum des Opt-in per E-Mail      |
| user_aliases                | Nutzer:in, falls vorhanden   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie in unserem Artikel zur [Fehlerbehebung]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_troubleshooting/).
{% endalert %} 

[1]: {% image_buster /assets/img_archive/csvexport.png %}
[2]: {% image_buster /assets/img_archive/csvexport2.png %}
[26]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration

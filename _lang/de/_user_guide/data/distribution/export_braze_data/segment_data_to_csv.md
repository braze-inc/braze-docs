---
nav_title: Daten für Segmente nach CSV exportieren
article_title: Daten der Segmente in CSV exportieren
page_order: 2
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Daten aus Segmenten nach CSV exportieren."

---

# Exportieren von Segmentdaten nach CSV

> Auf dieser Seite erfahren Sie, wie Sie einen CSV-Export von Nutzer:innen eines Segments anfragen können und welche Daten im Export enthalten sind.

Um Segmentdaten in eine CSV-Datei zu exportieren, wählen Sie bei der Bearbeitung eines Segments das Dropdown-Menü **Nutzerdaten** aus und wählen Sie, ob Sie die Nutzerdaten oder die E-Mail-Adressen für das Segment exportieren möchten.

![Abschnitt Segmente Details mit Nutzerdaten-Dropdown mit Exportoptionen.]({% image_buster /assets/img_archive/csvexport.png %})

Sie können einen CSV-Export auch von der Hauptseite **Segmente** aus anfragen, indem Sie das Dropdown-Menü <i class="fas fa-gear"></i> **Einstellungen** für ein Segment auswählen:

![Dropdown-Menü Einstellungen auf der Hauptseite Segmente.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Um Daten aus all Ihren Nutzerprofilen zu exportieren, erstellen Sie ein Segment ohne Filter und fragen dann einen CSV-Export an.
{% endalert %}

Die CSV-Ausgabe enthält die Daten der einzelnen Nutzerprofile, die zum Zeitpunkt des Exports im Segment erfasst wurden. Sie können jedes Segment exportieren, indem Sie das Zahnradsymbol und CSV-Export auswählen. Braze erstellt den Bericht im Hintergrund und mailt ihn an die Nutzer:innen, die gerade angemeldet sind.

{% alert important %}
Aufgrund von Dateigrößenbeschränkungen kann Ihr Export fehlschlagen, wenn die geschätzte Größe Ihres Segments über 500.000 Nutzer:innen liegt. Beachten Sie, dass diese Einschränkung die geschätzte Größe Ihres Segments verwendet und nicht die genaue Berechnung. Weitere Einzelheiten finden Sie unter [Exportieren großer Segmente](#exporting-large-segments).
{% endalert %}

Wenn Sie Ihre [Amazon S3-Anmeldedaten]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) mit Braze verknüpft haben, wird die CSV stattdessen in Ihrem S3-Bucket unter dem Schlüssel `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip` hochgeladen. Sie müssen im Dashboard eingeloggt sein, um auf den Download-Link zuzugreifen, der Ihnen per E-Mail zugesandt wurde.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Daten im Export enthalten

Abhängig von Ihrer Auswahl ist Folgendes in Ihrem Export enthalten.

### CSV-Export von Nutzer:innen-Daten

| Feldname                  | Beschreibung                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | Interne ID (kann nicht geändert werden)                           |
| Land                     | Land                                    |
| created_at                  | Datum und Uhrzeit, zu der das Nutzerprofil erstellt wurde                   |
| Geräte                     | Informationen zum Gerät                           |
| date_of_birth               | Geburtsdatum                                            |
| E-Mail                       | E-Mail-Adresse                                            |
| unsubscribed_from_emails_at | Datum, an dem Sie sich von E-Mails abgemeldet haben                            |
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
Hilfe zu CSV- und API-Exporten finden Sie in unserem Artikel zur [Fehlerbehebung]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %} 

## Exportieren großer Segmente

Es gibt mehrere Methoden, um ein großes Segment von Nutzern:innen mit mehr als 500.000 Nutzern zu exportieren.

{% tabs %}
{% tab Multiple segments %}

Sie können ein großes Segment in kleinere Segmente aufteilen und dann jedes der kleineren Segmente aus Braze exportieren. 

{% endtab %}
{% tab Random bucket numbers %}

Sie können auch [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) verwenden, um Ihre Nutzer:innen in mehrere Segmente aufzuteilen, die Sie dann nach dem Export kombinieren können. Wenn Sie zum Beispiel Ihr Segment in zwei verschiedene Segmente aufteilen möchten, können Sie dies mit den folgenden Filtern tun:
- Segment:  Zufällige Bucket-Nummer ist kleiner als 5000 (umfasst 0-4999)
- Segment 2: Zufällige Bucket-Nummer ist größer als 4999 (umfasst 5000-9999)

{% endtab %}
{% tab Endpoints %}

Sie können auch die folgenden Endpunkte nutzen, um Nutzerdaten für ein bestimmtes Segment zu exportieren. Beachten Sie, dass für diese Endpunkte Datenbeschränkungen gelten.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}

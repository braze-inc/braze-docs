---
nav_title: Versionshinweise
article_title: Versionshinweise
page_order: 4
layout: dev_guide
guide_top_header: "Versionshinweise"
guide_top_text: "Hier finden Sie alle Updates für die Braze-Plattform, darunter die folgenden <a href='/docs/help/release_notes/#most-recent'>neuesten Plattform-Updates</a>."
page_type: landing
search_rank: 1
description: "Auf dieser Landing Page finden Sie die Versionshinweise zu Braze. Hier finden Sie alle Updates für die Braze Plattform und SDKs sowie eine Liste veralteter Features."

guide_featured_title: "Anmerkungen zur Veröffentlichung"
guide_featured_list:
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Abwertungen
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK-Changelogs
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Neueste Braze Versionshinweise {#most-recent}

> Braze veröffentlicht Informationen zu Produkt-Updates in monatlichen Abständen, die sich an den großen Produkt-Releases orientieren. Das Produkt wird jedoch von Woche zu Woche mit verschiedenen Verbesserungen aktualisiert.
> <br>
> <br>

> Weitere Informationen zu den in diesem Abschnitt aufgeführten Updates erhalten Sie von Ihrem Account Manager:in oder [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). In [unseren SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) finden Sie weitere Informationen zu unseren monatlichen SDK Releases, Updates und Verbesserungen.
 
## 1\. April 2025 Veröffentlichung

### Updates für die Braze-Navigation

Die aktualisierte Navigation in Braze wurde entwickelt, um Ihnen den effizienten Zugriff auf Features und Inhalte über verschiedene Geräte hinweg zu ermöglichen. Beachten Sie, dass die Option, zwischen den Navigationsversionen zu wechseln, nicht mehr verfügbar ist. Erfahren Sie mehr in unserem Artikel [über die Navigation in Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation).

### Entwickler:in entwirren

Zuvor waren viele Aufgaben auf Plattformebene auf mehrere Seiten aufgeteilt, wie z.B. die Integration des Swift SDK, die auf sechs Seiten verteilt war. Darüber hinaus wurden gemeinsame Features für jede Plattform einzeln dokumentiert, was bedeutet, dass die Suche nach einem Thema wie "Einrichten von Push-Benachrichtigungen" 10 verschiedene Seiten ergeben würde.

**Vorher:**

![Die vorherige Swift-Dokumentation, die sich im Abschnitt Platform Integration Guides befindet.]({% image_buster /assets/img/before_swift.png %})

Jetzt wurden die Aufgaben auf Plattformebene in einzelnen Seiten zusammengefasst und gemeinsame SDK Features befinden sich jetzt auf derselben Seite (mit Hilfe unseres neuen SDK-Tabbing Features). Zum Beispiel gibt es jetzt nur noch eine Seite für die Integration des Braze SDK, auf der Sie zwischen den Plattformen wechseln können, indem Sie einen Tab am oberen Rand der Seite auswählen. Wenn Sie dies tun, wird sogar das Inhaltsverzeichnis auf der Seite aktualisiert, um den aktuell ausgewählten Tab wiederzugeben.

**Danach:**

![Die aktualisierte Swift-Dokumentation befindet sich auf dem Tab Swift des Artikels Integration des SDK.]({% image_buster /assets/img/after_swift.png %})

![Die aktualisierte Android-Dokumentation befindet sich auf dem Tab Android des Artikels Integration des SDK.]({% image_buster /assets/img/after_android.png %})

### Zur Braze-Dokumentation beitragen

Falls Sie es noch nicht wussten: Unsere Dokumente sind vollständig Open Source! Wie das geht, erfahren Sie in unserem [Contributing Guide]({{site.baseurl}}/contributing/home). Diesen Monat haben wir einige Funktionen der Website dokumentiert, z. B. die [automatische Erweiterung von Abschnitten]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) und die [Darstellung von API-generierten Inhalten]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Flexibilität der Daten

#### Update auf die Eigenschaften des Canvas-Eingangs

Die Eingangs-Eigenschaften von Canvas sind jetzt Teil der [Canvas-Kontextvariablen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Jede Kontextvariable enthält einen Namen, einen Datentyp und einen Wert, der Liquid enthalten kann. Weitere Informationen finden Sie in der [Komponente Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Updates der Segmentierungsfilter für Telefonnummernfilter

Die Segmentierungsfilter wurden aktualisiert, um Änderungen an zwei Filtern für Telefonnummern zu berücksichtigen:

- [Unformatierte Rufnummer]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (früher **Telefonnummer**): Segmentiert Ihre Nutzer:innen nach ihrer unformatierten Telefonnummer.
- [Telefonnummer]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (früher **: Absender-Telefonnummer**): Segmentiert Ihre Nutzer:innen nach dem für E.164 formatierten Rufnummernfeld.

#### Angepasste Daten löschen

Wenn Sie zielgerichtete Kampagnen und Segmente erstellen, werden Sie vielleicht feststellen, dass Sie kein angepasstes Event oder angepasstes Attribut mehr benötigen. Jetzt können Sie [diese angepassten Daten löschen]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) und ihre Referenzen aus Ihrer App entfernen.

#### Nutzer:innen mit E-Mail-Adressen und Telefonnummern importieren

Sie können jetzt eine E-Mail Adresse oder Telefonnummer verwenden, um [Nutzer:innen zu importieren]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) und eine externe ID oder einen Nutzer-Alias weglassen.

#### Vom Dienstanbieter initiierte Fehlerbehebung bei der Anmeldung

Die vom SP (Service Provider) initiierte Anmeldung verfügt jetzt über eine [Fehlerbehebung]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting), die Ihnen hilft, Probleme mit SAML und Single Sign-on zu lösen.

#### Nutzer:in-Fehlerbehebung beim Nutzerimport

Der [Abschnitt Fehlerbehebung beim Nutzerimport]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) enthält neue und aktualisierte Einträge, u.a. wie Sie fehlende Zeilen in Ihren importierten CSV-Dateien beheben können.

#### Häufig gestellte Fragen zu Segment-Erweiterungen

Sehen Sie sich unsere [häufig gestellten Fragen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) zu Segment-Erweiterungen an, z.B. wie Sie eine Segment-Erweiterung erstellen können, die mehrere angepasste Events verwendet.

#### Personalisierte und erweiterte Verzögerungen

{% multi_lang_include release_type.md release="Früher Zugang" %}

Sie können eine [personalisierte Verzögerung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) für Ihre Nutzer:innen einrichten und diese mit einem Kontextschritt verwenden, um die Kontextvariable auszuwählen, nach der die Verzögerung erfolgen soll.

Sie können jetzt auch Verzögerungsstufen bis zu zwei Jahre verlängern. Wenn Sie z.B. neue Nutzer:innen für Ihre App onboarding, können Sie eine längere Verzögerung von zwei Monaten einfügen, bevor Sie eine Nachricht senden, um die Nutzer:innen, die noch keine Sitzung begonnen haben, anzustupsen.

#### Standardattribute des Nutzerprofils für Snowflake

{% multi_lang_include release_type.md release="Beta" %}

Es gibt jetzt drei [Standardattribute für Nutzerprofile]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/user_attributes) in Snowflake. Jede Ansicht ist für einen bestimmten Anwendungsfall mit eigenen Performance-Überlegungen konzipiert. So können Sie zum Beispiel einen regelmäßigen Snapchat der Standardattribute eines Nutzerprofils erhalten.

### Robuste Kanäle

#### Grundlagen des Messaging

[Messaging Fundamentals]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) ist ein neuer Bereich in Engagement Tools, der die gemeinsamen Konzepte und Begriffe für Kampagnen und Canvase enthält, wie z.B. die Archivierung und Lokalisierung von Nachrichten.

#### WhatsApp angepasste Domains

Sie können jetzt [angepasste Domains]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) einer oder mehreren Abo-Gruppen von WhatsApp zuweisen.

#### Getriggerte In-App-Nachrichten für Canvas

Sie können jetzt einen [Auslöser für Ihre In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) auswählen, der bei Sitzungsbeginn oder durch angepasste Events und Käufe getriggert wird. Nachdem alle Verzögerungen verstrichen sind und die Optionen für die Zielgruppe aktiviert wurden, werden In-App-Nachrichten aktiviert, sobald ein Nutzer:innen den Schritt Nachricht erreicht. Wenn ein Nutzer eine Sitzung startet und das Trigger-Ereignis für die In-App-Nachricht ausführt, sieht der Nutzer:in die In-App-Nachricht. 

#### Eingangsvolumen für Canvas begrenzen

Sie können die Anzahl der Personen, die dieses Canvas betreten können, durch eine ausgewählte Kadenz begrenzen (täglich, Lifetime des Canvas oder jedes Mal, wenn das Canvas geplant ist). Sie können zum Beispiel [die Eingangskontrollen so einstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience), dass der Canvas nur an 5.000 Nutzer:innen pro Tag senden darf.

#### Neuer Anwendungsfall: Buchungserinnerung per E-Mail

Erfahren Sie, wie Sie die Features von Braze nutzen können, um [einen E-Mail Messaging-Dienst für Buchungserinnerungen aufzubauen]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). Der Dienst erlaubt es Nutzern:innen, Termine zu buchen, und sendet ihnen Nachrichten, um sie an ihre Termine zu erinnern. Obwohl in diesem Anwendungsfall E-Mail-Nachrichten verwendet werden, können Sie Nachrichten in einem beliebigen oder mehreren Kanälen auf der Grundlage eines einzigen Updates eines Nutzerprofils versenden.

#### Tracking von Klicks für bestimmte Links

Sie können [das Tracking von Klicks für bestimmte Links deaktivieren]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis), indem Sie Ihrer E-Mail Nachricht im HTML-Editor oder den Komponenten im Drag-and-Drop-Editor HTML-Code hinzufügen.

#### Dynamischer Apple Push-Benachrichtigungsdienst - Gateway-Verwaltung

Die [dynamische APN-Gateway-Verwaltung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) verbessert die Zuverlässigkeit und Effizienz von iOS Push-Benachrichtigungen, indem sie automatisch die richtige APN-Umgebung erkennt. Früher mussten Sie die APN-Umgebungen (Entwicklung oder Produktion) für Ihre Push-Benachrichtigungen manuell auswählen, was manchmal zu falschen Gateway-Konfigurationen, Zustellungsfehlern und BadDeviceToken-Fehlern führte.

#### Flutter Unterstützung für Bannerkarten

{% multi_lang_include release_type.md release="Früher Zugang" %}

Bannerkarten unterstützen jetzt Flutter. Außerdem wurde die gesamte Dokumentation von Banner Card überarbeitet, um die Benutzerfreundlichkeit zu erhöhen. Lesen Sie die folgenden Artikel, um loszulegen:

- [Über Banner Cards]({{site.baseurl}}/developer_guide/banner_cards)
- [Erstellen von Banner Card Kampagnen]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns)
- [Bannerkarten in Ihre App einbinden]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards)

#### WhatsApp Klick Tracking

{% multi_lang_include release_type.md release="Früher Zugang" %}

Mit [dem Tracking von Klicks]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) können Sie messen, wann jemand auf einen Link in Ihrer WhatsApp Nachricht tippt. So haben Sie einen klaren Überblick darüber, welche Inhalte das Engagement fördern. Braze verkürzt Ihre URLs, fügt im Hintergrund Tracking hinzu und protokolliert Klicks, sobald sie stattfinden.

#### Häufig gestellte Fragen zu Push

Lesen Sie unseren neuen [Push-FAQ-Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq), der einige der am häufigsten gestellten Fragen beim Einrichten von Push-Kampagnen beantwortet.

#### Push-Fehlerbehebung

Die [Fehlerbehebung für Push-Benachrichtigungen]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) enthält eine Reihe von Schritten, die Ihnen helfen, Probleme bei der Zustellung von Push-Benachrichtigungen zu bewältigen. Wenn Sie beispielsweise Probleme mit der Zustellung von Push-Benachrichtigungen haben, haben wir Schritte zur Fehlerbehebung für Sie zusammengestellt.

### Neue Braze Partnerschaften

#### Movable Ink Da Vinci - Dynamische Inhalte

Die Integration von Braze und Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) ermöglicht es Marken, hochgradig personalisiertes Messaging zu liefern, indem sie die KI-gesteuerte Content Decisioning Engine von Da Vinci nutzen. Da Vinci kuratiert die relevantesten Inhalte für jeden Nutzer:innen und stellt die Nachrichten nahtlos über Braze bereit.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Aktualisiert die native Android-Bridge von [Braze Android SDK 33.0.0 auf 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Die erforderliche Android SDK-Version ist mindestens 25. Weitere Einzelheiten finden Sie [hier](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Internet SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## März 4, 2025 Veröffentlichung

### Aufschübe

Braze hat seine Definition von "Soft Bounce" aktualisiert und sendet ab dem 25\. Februar 2025 um 10 Uhr EST ein neues Ereignis namens " [Deferrals"]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance).

Für SendGrid Kund:in haben wir eine Änderung vorgenommen, um Aufschub-Events von unseren Soft Bounce Events zu trennen. Wir zählen aufgeschobene Ereignisse als Soft Bounce-Ereignis. Dies betrifft alle SendGrid Kund:innen, die Currents, Query Builder, SQL Extension, Snowflake Data Sharing oder unser Produkt Transaktions-E-Mails verwenden.

#### Vorheriges Verhalten

Vor dem 25\. Februar 2025 wird bei einem verschobenen Ereignis für eine E-Mail Adresse in einer Kampagne oder Canvas jedes Mal ein Soft Bounce-Ereignis protokolliert. Daher sind Aufschübe als Teil der Soft Bounce Daten enthalten. Dies kann dazu führen, dass ein Nutzer:innen oder eine Kampagne mehr Soft Bounce-Ereignisse meldet als erwartet. 

#### Neues Verhalten

Ab dem 25\. Februar 2025 wird ein verschobenes Ereignis nicht mehr jedes Mal als Soft Bounce-Ereignis protokolliert. Stattdessen protokollieren wir ein Soft Bounce-Ereignis einmal pro Sendevorgang für die E-Mail Adresse, egal wie oft die E-Mail erneut versucht oder zurückgestellt wird.

#### Was das bedeutet

Ab dem 25\. Februar 2025 werden Sie einen deutlichen Rückgang der Soft Bounce-Ereignisse feststellen, was zu den folgenden möglichen Änderungen führt:

- Weniger Soft Bounces bei allen Berichten, die mit Query Builder erstellt wurden
- Kleinere Segmente mit SQL-Erweiterungen, wenn Sie Nutzer:innen, die in einem Zeitraum von Y X-mal geprellt wurden, als Targeting verwenden
- Rückgang der Anzahl von Soft Bounce-Ereignissen, die über Currents und eines unserer Features über Snowflake zugestellt werden
- Rückgang der Anzahl von Soft Bounces für das Produkt Transaktions-E-Mails

Für Sparkpost-Kunden gibt es keine Auswirkungen auf Ihre Soft Bounce Event-Daten, stattdessen erhalten Sie in Currents und Snowflake ein neues E-Mail-Ereignis, den Aufschub.

### Entwickler:in entwirren

Identische Inhalte, die über mehrere SDKs verteilt sind, werden jetzt mit dem neuen SDK Tabbing Feature der Docs Site zusammengeführt. Diesen Monat wurden [SDK-Integration]({{site.baseurl}}/developer_guide/sdk_integration/), [SDK-Initialisierung]({{site.baseurl}}/developer_guide/sdk_initialization/) und [Content-Cards]({{site.baseurl}}/developer_guide/content_cards/) zusammengefasst. Bleiben Sie dran für weitere Updates in den kommenden Monaten.

### Flexibilität der Daten
 
#### Braze IDs für Nutzer:innen-Profile

Ein Nutzerprofil enthält jetzt eine [Braze ID]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). Sie können dies bei der Suche nach Nutzer:innen-Profilen verwenden.

#### Aufschübe

Braze hat seine Definition für einen Soft Bounce aktualisiert und sendet ein neues Ereignis mit der Bezeichnung " [Aufschub"]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance). Dies bedeutet, dass eine E-Mail nicht sofort zugestellt wurde, Braze die E-Mail jedoch bis zu 72 Stunden nach diesem vorübergehenden Zustellungsfehler erneut versucht, um die Chancen auf eine erfolgreiche Zustellung zu maximieren, bevor die Versuche für diese spezifische Kampagne eingestellt werden.

#### Snowflake Entitätsbeziehungen
 
Wir haben die [rohen Tabellenschemata](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) für Snowflake- und Braze-Entity-Beziehungen auf einer neuen [, Nutzer:innen-freundlichen Doku-Seite](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships) abgebildet. Sie enthält eine Aufschlüsselung der `USER_MESSAGES` Tabellen, die zu den einzelnen Kanälen gehören, sowie Beschreibungen der Primär-, Fremd- und nativen Schlüssel der einzelnen Tabellen.

#### Identitätsmanagement für externe IDs

Die Verwendung einer E-Mail-Adresse oder einer gehashten E-Mail-Adresse als externe ID von Braze kann die Identitätsverwaltung über Ihre Datenquellen hinweg vereinfachen. Es ist jedoch wichtig, die [potenziellen Risiken]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) für den Datenschutz und die Datensicherheit zu berücksichtigen.
 
### Kreativität entfesseln

#### Liquid-Tutorials

Drei [Liquid-Tutorials]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) zur Verwendung von Operatoren in den folgenden Szenarien hinzugefügt.

<table border="1">
  <tr>
    <td>Auswahl einer Nachricht mit einem ganzzahligen, angepassten Attribut.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="Der Kompositionsschritt in Braze zeigt eine Nachricht mit einem ganzzahligen angepassten Attribut." /></td>
  </tr>
  <tr>
    <td>Auswahl einer Nachricht mit einem String angepassten Attribut.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="Der Kompositionsschritt in Braze zeigt eine Nachricht mit einem String angepassten Attribut." /></td>
  </tr>
  <tr>
    <td>Abbrechen einer Nachricht aufgrund des Standorts.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="Der Kompositionsschritt in Braze zeigt, dass eine Nachricht aufgrund des Standorts abgebrochen wird." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Kontextuelle Schritte für Canvas
 
{% multi_lang_include release_type.md release="Früher Zugang" %}
 
Verwenden Sie [Kontext-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), um eine Reihe von Variablen zu erstellen oder zu aktualisieren, die den Kontext eines Nutzers:innen (oder Insights über das Verhalten dieses Nutzers) darstellen, während er sich durch ein Canvas bewegt.

#### Personalisierte Verzögerung

{% multi_lang_include release_type.md release="Früher Zugang" %}

Sie können eine [personalisierte Verzögerung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) für Ihre Nutzer:innen einrichten, indem Sie den Schalter **Verzögerung personalisieren** in Ihrem Schritt Verzögerung auswählen. Sie können dies mit einem Kontextschritt verwenden, um eine Kontextvariable für die Verzögerung auszuwählen.

Wenn Sie einen Verzögerungsschritt in Ihrer Canvas Nutzer:in einrichten, können Sie jetzt eine Verzögerung von bis zu 2 Jahren festlegen.

#### Automatische Synchronisierung rückgängig machen

Beim [Verfassen einer E-Mail Nachricht]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email) können Sie auf dem Tab Klartext zur automatischen Synchronisierung zurückkehren, indem Sie das Symbol Aus HTML neu generieren auswählen, das nur erscheint, wenn der Klartext nicht synchronisiert wird.

![Der Revert Button für die automatische Synchronisierung in Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Robuste Kanäle

#### Android Live Updates

Obwohl die Live Updates offiziell erst ab dem
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), zeigen wir Ihnen auf unserer Seite [Live Updates für Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local), wie Sie deren Verhalten emulieren können, so dass Sie interaktive Sperrbildschirm-Benachrichtigungen anzeigen können, ähnlich wie bei den [Live Activities für das Swift Braze SDK]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). Im Gegensatz zu offiziellen Live Updates kann diese Funktion auch für ältere Android-Versionen implementiert werden.

#### Kopieren von Kampagnen mit Feature-Flags zwischen Workspaces

Sie können jetzt [Kampagnen mit Feature-Flags über Workspaces hinweg kopieren]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags). Stellen Sie dazu sicher, dass der Ziel-Workspace ein Feature-Flag Experiment mit einer ID konfiguriert hat, die mit dem Feature-Flag übereinstimmt, auf das in der ursprünglichen Kampagne referenziert wird.

#### Neue Typen von WhatsApp Nachrichten werden unterstützt

WhatsApp Messaging unterstützt jetzt [ausgehende Nachrichten in den Bereichen Video, Audio und Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.

#### Nachrichten von rechts nach links

[Erstellen von Nachrichten von rechts nach links]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) behandelt bewährte Verfahren für die Gestaltung von Nachrichten in Sprachen, die von rechts nach links gelesen werden, damit Ihre Nachrichten so genau wie möglich angezeigt werden.
 
### KI und ML Automatisierung
 
#### Artikel-Empfehlungen

[Die Verwendung von Artikel-Empfehlungen im Messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) deckt das Objekt `product_recommendation` Liquid ab und enthält ein Tutorial, das Ihnen hilft, dieses Wissen in die Praxis umzusetzen.

### Neue Braze Partnerschaften
 
#### E-Mail Liebe - Kanal Erweiterungen
 
Die Partnerschaft zwischen Braze und [Email Love]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates) nutzt das Feature Export to Braze von Email Love und die Braze API, um Ihre E-Mail Templates nahtlos in Braze hochzuladen.

#### VWO - A/B-Tests
 
Die Integration von Braze und [VWO]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/vwo) erlaubt es Ihnen, VWO-Experimentdaten zu nutzen, um gezielte Segmente zu erstellen und personalisierte Kampagnen zu liefern.
 
### SDK Updates
 
Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Erhöht die Mindestanforderung für React Native auf Version [0.71.0](https://reactnative.dev/blog/2023/01/12/version-071). Weitere Informationen finden Sie in der [Richtlinie zur Unterstützung von Releases](https://github.com/reactwg/react-native-releases#releases-support-policy) in der React Working Group.
    - Erhöht die minimal erforderliche iOS-Version auf 12.0.
    - Update der nativen iOS-Versionsbindungen von [Braze Swift SDK 7.5.0 auf 8.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen Android-Versionsbindungen von [Braze Android SDK 29.0.1 auf 30.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## Februar 4, 2025 Veröffentlichung

### Braze Docs Verbesserungen

#### Leitfaden zum Thema
Unsere jüngsten Updates des [Contributing Guide]({{site.baseurl}}/contributing/your_first_contribution) machen es auch für nicht-technische Nutzer:innen einfacher, zu Braze Docs beizutragen.

#### DATEN UND ANALYSEN neu gestaltet
Um Ihnen die Suche zu erleichtern, haben wir die Artikel, die früher unter "Daten & Analytics" zusammengefasst waren, in [Daten]({{site.baseurl}}/user_guide/data) und [Analytics]({{site.baseurl}}/user_guide/analytics) aufgeteilt. 

#### Entwicklerhandbuch
Wir haben alle Dokumente im [Braze Entwickler:in]({{site.baseurl}}/developer_guide/home) aufgeräumt und dabei auch die auf mehrere Seiten verteilten Anleitungen auf einer Seite zusammengefasst.

Außerdem gibt es eine neue [SDK-Referenzseite]({{site.baseurl}}/developer_guide/references), auf der alle Referenzdokumentationen und Repositories für jedes Braze SDK aufgelistet sind.

##### Unreal Engine Braze SDK
Wir haben alle Inhalte aus dem Unreal Engine Braze SDK GitHub Repository README in den [entsprechenden Abschnitt auf Braze Docs]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine) migriert und umgeschrieben.

### Flexibilität der Daten

#### Dashboard für die API-Nutzung

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Mit dem [Dashboard zur API-Nutzung]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) können Sie den bei Braze eingehenden REST API-Verkehr überwachen, um Trends bei der Nutzung unserer REST APIs zu erkennen und mögliche Probleme zu beheben.

#### Hinzufügen von Tags zu angepassten Attributen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können [Tags zu einem angepassten Attribut hinzufügen]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags), nachdem es erstellt wurde, wenn Sie die Berechtigung "Events, Attribute, Käufe verwalten" haben. Die Tags können dann zum Filtern der Liste der Attribute verwendet werden.

#### Endpunkte für Katalogauswahlen und asynchrone Katalogfelder 

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Die folgenden Endpunkte sind jetzt allgemein verfügbar:
* [POST: Katalogfelder erstellen]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [LÖSCHEN: Katalogfeld löschen]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [LÖSCHEN: Katalogauswahl löschen]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST: Katalogauswahl erstellen]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Eine E-Mail Adresse verwenden, um Kampagnen oder Canvase zu triggern

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt einen Empfänger:in per E-Mail angeben, um Ihre [Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users) und [Canvase]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience) zu triggern.

#### Verwendung einer Telefonnummer zur Identifizierung eines Nutzer:innen über die API

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt zusätzlich zu einem Alias und einer E-Mail Adresse eine Telefonnummer verwenden, um einen Nutzer:innen über den [Endpunkt der`/users/identify` API]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) zu identifizieren.

#### Abrufen einer SAML-Ablaufverfolgung
Wir haben Schritte hinzugefügt, wie [Sie einen SAML-Trace erhalten]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), der Ihnen hilft, Probleme mit SAML SSO mit dem Support effizienter zu lösen.
 
#### Regionale Datenzentren
Da Braze wächst und neue Bereiche bedient, haben wir einen [Artikel über die Datenzentren von Braze]({{site.baseurl}}/user_guide/data/data_centers) hinzugefügt, um unseren operativen Ansatz zu erläutern.
 
### Kreativität entfesseln
 
#### Benachrichtigungen über Preissenkungen und Wiederverfügbarkeitsmeldungen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt Kunden:in benachrichtigen, wenn ein Artikel wieder vorrätig ist, indem Sie über ein Canvas und einen Katalog eine [Benachrichtigung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications) einrichten, wenn ein Artikel wieder vorrätig ist.

Sie können auch [Preissenkungsbenachrichtigungen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) erstellen, um Kund:in zu benachrichtigen, wenn der Preis eines Artikels gesunken ist, indem Sie Preissenkungsbenachrichtigungen in einem Katalog und Canvas einrichten.

#### Vorschau zum Auswählen 

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Nachdem Sie eine Auswahl erstellt haben, können Sie sehen, was eine [Auswahl]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview) für einen zufälligen Nutzer:innen oder einen bestimmten Nutzer:innen ergeben würde.

#### Template für Katalogartikel einschließlich Liquid 

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können [Templates für Katalogartikel erstellen, die Liquid enthalten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### Canvas-Templates
Wir haben neue Canvas Templates für das [Onboarding von Nutzer:innen mit einer Umfrage zu den Präferenzen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) und für die [Erstellung einer E-Mail Registrierung mit doppeltem Opt-in]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup) hinzugefügt.

#### Leads verwalten mit Salesforce Sales Cloud für B2B
Eine Möglichkeit, wie B2B Marketer Braze nutzen können, ist eine Integration mit der Salesforce Sales Cloud. Lesen Sie mehr darüber, wie Sie diesen [Anwendungsfall]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud) implementieren können.
 
### Robuste Kanäle

#### Unterdrückungslisten

{% multi_lang_include release_type.md release="Beta" %}
 
[Unterdrückungslisten]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) geben Gruppen von Nutzer:innen an, die niemals Nachrichten erhalten werden. Administratoren können Unterdrückungslisten mit Segmentfiltern erstellen, um eine Nutzer:innen-Gruppe auf die gleiche Weise einzugrenzen, wie Sie es bei der Segmentierung tun würden.

### Neue Braze Partnerschaften

#### Konstrukteur - Dynamischer Content
[Constructor]({{site.baseurl}}/partners/message_personalization/dynamic_content/constructor) ist eine Such- und Produktentdeckungsplattform, die KI und maschinelles Lernen nutzt, um personalisierte Suchanfragen, Empfehlungen und Browsing-Erlebnisse für E-Commerce- und Einzelhandels-Websites bereitzustellen.
 
#### Trustpilot - Dynamische Inhalte
[Trustpilot]({{site.baseurl}}/partners/message_personalization/dynamic_content/trustpilot) ist eine Online-Bewertungsplattform, die es Ihren Kunden ermöglicht, Feedback zu geben, und die es Ihnen erlaubt, Bewertungen zu verwalten und darauf zu reagieren.

### SDK Updates
 
Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - Update der minimalen SDK-Version von 21 (Lollipop) auf 25 (Nougat).

## Januar 7, 2025 Veröffentlichung

### Kreativität entfesseln

#### Templates für In-App-Nachrichten

Wir haben [Templates]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/) für In-App-Nachrichten per Drag-and-Drop hinzugefügt.

#### B2B Salesforce Sales Cloud Lead Management

[Die Verwaltung von Leads mit Salesforce Sales Cloud]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/) zeigt Ihnen, wie Sie mit Braze-to-Braze-Webhooks Leads in Salesforce Sales Cloud über eine von der Community vorgeschlagene Integration erstellen und aktualisieren können.

### Robuste Kanäle

#### Canvas-Templates

Wir haben Braze-Canvas Templates für [E-Mail-Registrierungen mit doppeltem Opt-in]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) und [Onboarding mit Umfragen zu den Präferenzen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/) hinzugefügt.

#### Änderung der Einwilligungsrichtlinie von WhatsApp

Meta hat kürzlich seine [Einwilligungsrichtlinie](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) geändert. Weitere Informationen finden Sie in den [Updates für WhatsApp-Produkte]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/).

#### Breitenwerkzeug für Content-Blöcke im E-Mail Drag-and-Drop-Editor

Im Drag-and-Drop-Editor für E-Mails können Sie für Ihren Content-Block [die Breite anpassen]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block). Die Standardbreite ist 100 %.

### Flexibilität der Daten

#### Filter für weich geprellte Segmente

Segmentieren Sie Ihre Nutzer:innen danach, ob sie X-mal in Y Tagen einen Soft Bounce hatten. Weitere Informationen finden Sie unter [Segmentierungsfilter - Glossar]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Übersicht der anonymen Nutzer:innen

[Anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) bietet eine Übersicht über anonyme Nutzer:innen und User-Aliasing und zeigt auf, welche Bedeutung sie haben und wie sie in Ihren Nachrichten genutzt werden können.

#### Mitgliedschaft in der globalen Kontrollgruppe

Sie können [die Mitgliedschaft in der globalen Kontrollgruppe einsehen]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group), indem Sie im Profil eines einzelnen Nutzers:in den Tab **Engagement** gehen und zum Abschnitt **Verschiedenes** scrollen.

### Neue Braze Partnerschaften

#### Justuno - Leads erfassen

[Justuno]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/justuno/) ermöglicht es Ihnen, mit dynamischen Segmenten ein vollständig optimiertes Besuchererlebnis für alle Ihre Zielgruppen zu schaffen und bietet das fortschrittlichste Targeting, das es gibt - und das alles, ohne die Geschwindigkeit der Website zu beeinträchtigen oder die Entwicklungsarbeit zu erhöhen.

#### Odicci - Customer Data Platform (CDP) - Kundendaten

Integrieren Sie Braze mit [Odicci]({{site.baseurl}}/partners/message_personalization/dynamic_content/odicci/), einer Plattform, die es Unternehmen ermöglicht, Kunden durch loyalitätsorientierte Omnichannel-Erlebnisse zu gewinnen, zu engagieren und zu binden.

#### Optimizely - A/B-Tests

Die Integration von Braze und [Optimizely]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/optimizely/) ist eine bidirektionale Integration, die es Ihnen erlaubt:

- Synchronisieren Sie Ihre Braze Kundensegmente und Events mit der Optimizely Data Platform (ODP) über Nacht, um Optimizelys Kundenprofile, Berichte und Segmentierung zu bereichern.
- Senden Sie Braze-Currents-Ereignisse von Braze an das Berichtstool von Optimizely.
- Synchronisieren Sie ODP Kundendaten und Events mit Braze, um Ihre Kundendaten in Braze anzureichern und Messaging auf der Grundlage von Kundenevents in ODP zu triggern.

## Veröffentlichung im Dezember 10, 2024

### SDK-Benutzerstandort nach IP-Adresse

Ab dem 26\. November 2024 wird Braze die Standorte der Nutzer:innen anhand der IP-Adresse ab dem Beginn der ersten SDK-Sitzung ermitteln. Braze verwendet die IP-Adresse, um den Länderwert für Nutzer:innen-Profile festzulegen, die über das SDK erstellt werden, und diese IP-basierte Ländereinstellung ist während und nach der ersten Sitzung verfügbar. Weitere Informationen finden Sie unter [Standort-Tracking]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Einstellung "Erhöhter Zugang

[Elevated Access]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) bietet eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze-Dashboard. Wenn Sie aktiv sind, müssen Nutzer:innen ihr Konto erneut überprüfen, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen können. Um den erweiterten Zugriff zu verwenden, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie die Option ein.

### Erlaubnis zur Einsichtnahme in persönlich identifizierbare Informationen (PII)

Als Administrator können Sie [Nutzern:innen erlauben]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions), die von Ihrem Unternehmen im Dashboard definierten PII in der Vorschau von Nachrichten anzuzeigen, die Liquid-Variablen für den Zugriff auf die Eigenschaften der Nutzer:innen verwenden. 

Für Workspaces können Sie Nutzern:innen erlauben, die von Ihrem Unternehmen definierten PII im Dashboard anzuzeigen, oder Nutzerprofile anzeigen, aber Felder, die Ihr Unternehmen als PII identifiziert hat, schwärzen.

### Flexibilität der Daten

#### Schemata für den Datensee

Die folgenden Schemata wurden zu den Rohtabellenschemata hinzugefügt:
- `USERS_CANVASSTEP_PROGRESSION_SHARED`: Verlaufsereignisse für einen Nutzer:innen in einem Canvas
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`: Bezeichner der zufälligen Bucket-Nummern in der aktuellen und vorherigen globalen Kontrollgruppe
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`: Impressions-Ereignisse, wenn ein Nutzer:in ein Feature-Flag blickt

#### Kontobasierte Segmentierung

Je nachdem, wie Sie Ihr [B2B-Datenmodell einrichten]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/), können Sie eine kontenbasierte Segmentierung auf zwei Arten vornehmen:

- Wenn Sie Kataloge für Ihre Geschäftsobjekte verwenden
- Wenn Sie verbundene Quellen für Ihre Geschäftsobjekte verwenden

#### Segmentierungsfilter

Unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) finden Sie die vollständige Liste der Segmentierungsfilter und ihre Beschreibungen.

##### Nutzerprofil erstellt bei

Segmentieren Sie Ihre Nutzer:innen danach, wann ihr Nutzerprofil erstellt wurde. Wenn ein:e Nutzer:in per CSV oder API hinzugefügt wurde, zeigt dieser Filter das Datum an, an dem er hinzugefügt wurde. Wenn der oder die Nutzer:in nicht per CSV oder API hinzugefügt wurde und seine erste Sitzung durch das SDK getrackt wurde, spiegelt dieser Filter das Datum dieser ersten Sitzung wider.

##### Rufnummer senden

Segmentieren Sie Ihre Nutzer:innen nach dem Telefonnummernfeld e.164. Mit diesem Filter können Sie reguläre Ausdrücke verwenden, um nach Telefonnummern mit einem bestimmten Ländercode zu segmentieren.

### Neue Braze Partnerschaften

#### Narvar - E-Commerce

Die Integration von Braze und [Narvar](https://corp.narvar.com/) ermöglicht es Marken, die Benachrichtigungsereignisse von Narvar zu nutzen, um Nachrichten direkt von Braze zu triggern und die Kund:innen mit zeitnahen Updates auf dem Laufenden zu halten.

#### Zeotap for Currents - Customer Data Platform (CDP)

Mit der Integration von Braze und [Zeotap](https://zeotap.com/) können Sie den Umfang und die Reichweite Ihrer Kampagnen erweitern, indem Sie die Segmente von Zeotap-Kunden mit den Nutzerprofilen von Braze synchronisieren. Mit [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) können Sie Daten auch mit Zeotap verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen.

#### Benachrichtigen - Dynamische Inhalte

Die Integration von Braze und [Notify](https://notifyai.io/) ermöglicht es Marketern, das Engagement über verschiedene Plattformen hinweg effektiv zu fördern. Anstatt sich auf herkömmliche Marketing-Methoden zu verlassen, kann eine durch die Braze API ausgelöste Kampagne die Möglichkeiten von Notify nutzen, um personalisiertes Messaging über mehrere Kanäle zuzustellen, einschließlich E-Mail, SMS, Push-Benachrichtigungen und mehr.

#### Contentful - Dynamische Inhalte

Die Integration von Braze und [Contentful](https://www.contentful.com/) erlaubt es Ihnen, Connected-Content dynamisch zu nutzen, um Inhalte aus Contentful in Ihre Kampagnen in Braze zu ziehen.

#### Outgrow - Leads erfassen 

Mit der Integration von Braze und [Outgrow](https://outgrow.co/) können Sie Nutzerdaten aus Outgrow automatisch in Braze übertragen und so hochgradig personalisierte und zielgerichtete Kampagnen ermöglichen.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Internet SDK 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Update der nativen iOS-Bridge [von Braze Swift SDK 10.3.1 auf 11.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Update der nativen Android Bridge [von Braze Android SDK 32.1.0 auf 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## Veröffentlichung am 12\. November 2024
 
### Flexibilität der Daten
 
#### Geschwindigkeitsbegrenzung für `/users/track`

Das Geschwindigkeitslimit für den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) wurde auf 3.000 pro 3 Sekunden aktualisiert.
 
### Kreativität entfesseln

#### Canvas Anwendungsfälle

Wir haben einige Anwendungsfälle zusammengestellt, die Ihnen zeigen, wie Sie ein Braze-Canvas nutzen können. Wenn Sie auf der Suche nach Inspiration sind, wählen Sie unten einen Anwendungsfall aus, um loszulegen.

- [Warenkorb-Abbruch]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [Wieder auf Lager]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Übernahme von Features]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Passive Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Feedback nach dem Kauf]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Robuste Kanäle

#### LINE

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Die LINE-Integration von Braze ist jetzt allgemein verfügbar! LINE ist mit über 95 Millionen monatlich aktiven Nutzer:innen die beliebteste Messaging App in Japan. Zusätzlich zum Messaging bietet LINE seinen Nutzern eine "All-in-One"-Plattform für soziale Medien, Spiele, Shopping und Zahlungen.

Weitere Informationen finden Sie in unserer [LINE-Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### LinkedIn Zielgruppe Sync

{% multi_lang_include release_type.md release="Beta" %}

Sie können LinkedIn jetzt mit [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/) nutzen, einem Tool, mit dem Sie die Reichweite Ihrer Kampagnen auf viele der wichtigsten sozialen und Werbetechnologien ausweiten können. Um an der Beta teilzunehmen, wenden Sie sich an Ihren Braze Success Manager:in.
 
### Verbesserte Anleitung für Entwickler:in
 
Wir sind gerade dabei, das [Braze Entwickler:in Handbuch zu]({{site.baseurl}}/developer_guide/home/) verbessern. In einem ersten Schritt haben wir die Navigation vereinfacht und die Anzahl der verschachtelten Abschnitte reduziert. 

|Vor|Nach|
|------|-----|
|!["Die alte Navigation für das Braze Entwickler:in."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["Die neue Navigation für das Braze Entwickler:in Handbuch"]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Neue Braze Partnerschaften
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), eine weltweit führende App für Postkarten, ermöglicht es Ihnen, Direkt-Mailing Kampagnen mit Leichtigkeit durchzuführen und bietet eine nahtlose und gewinnbringende Möglichkeit, mit Ihren Kund:in in Kontakt zu treten. Die ersten Schritte finden Sie unter [Integration von MyPostcard mit Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### SDK Updates
 
Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Diese Version erfordert 13.1.0 des Braze React Native SDK.
    - Ersetzt den iOS BrazeAppDelegate Methodenaufruf von BrazeReactUtils.populateInitialUrl durch BrazeReactUtils.populateInitialPayload.
        - Dieses Update behebt ein Problem, bei dem Push-Öffnungs-Ereignisse nicht ausgelöst werden, wenn Sie auf eine Benachrichtigung klicken, während sich die Anwendung in einem beendeten Zustand befindet.
        - Um dieses Update vollständig zu nutzen, ersetzen Sie in Ihrem JavaScript Code alle Aufrufe von Braze.getInitialURL durch Braze.getInitialPushPayload. Auf die ursprüngliche URL kann nun über die Eigenschaft url der ursprünglichen Push-Nutzlast zugegriffen werden.
- [Braze Segment Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Update der Braze Swift SDK Bindungen, um Versionen ab der 11.1.1+ SemVer Bezeichnung zu benötigen.
    - Dies erlaubt die Kompatibilität mit jeder Version des Braze SDK von 11.1.1 bis zu, aber nicht einschließlich, 12.0.0.
    - Weitere Informationen zu möglichen Änderungen finden Sie im Changelog-Eintrag für 11.1.1.

## Veröffentlichung am 15\. Oktober 2024

### Flexibilität der Daten

#### Kampagnen und Canvase

Bei der Erstellung von Kampagnen und Canvase können Sie die genaue Anzahl der erreichbaren Nutzer:innen Ihrer Zielgruppe anstelle der Standard-Schätzung berechnen, indem Sie [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size) auswählen.

#### API Android Objekte

Der [Parameter`android_priority` ]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) akzeptiert entweder die Werte "normal" oder "hoch", um die Priorität des FCM Senders festzulegen. Standardmäßig werden Benachrichtigungsnachrichten mit hoher Priorität und Nachrichten mit normaler Priorität gesendet.

Weitere Informationen darüber, wie sich unterschiedliche Werte auf die Zustellung auswirken, finden Sie unter [Android Nachrichtenpriorität](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Verwenden Sie [den integrierten Debugger des Braze SDK]({{site.baseurl}}/developer_guide/debugging/) zur Fehlerbehebung für Ihre SDK-gestützten Kanäle, ohne dass Sie die ausführliche Protokollierung in Ihrer App aktivieren müssen.

#### Live-Aktivitäten

Wir haben die [häufig gestellten Fragen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) zu Swift Live Activities mit einigen neuen Fragen und Antworten aktualisiert.

#### Angepasste Events

[Objekte mit Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties), die Array- oder Objektwerte enthalten, können jetzt eine Nutzlast für Event-Eigenschaften von bis zu 100 KB haben.

#### Zufällige Bucket-Nummern

Nutzen Sie den [zufälligen Wiedereintritt von Zielgruppen mit zufälligen Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) für A/B-Tests oder das Targeting bestimmter Nutzer:innen in Ihren Kampagnen.

#### Segmenterweiterungen

Sie können [Segment-Erweiterungen in einem wiederkehrenden Zeitplan aktualisieren]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh), indem Sie die Häufigkeit der Aktualisierung (täglich, wöchentlich oder monatlich) und die genaue Uhrzeit der Aktualisierung auswählen.

### Robuste Kanäle

#### SMS

Wir haben [UTM-Parameter]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) hinzugefügt, um Ihnen zu zeigen, wie Sie UTM-Parameter in einer SMS-Nachricht verwenden können, damit Sie die Performance von Kampagnen in Analytics-Tools von Drittanbietern, wie z.B. Google Analytics, verfolgen können.

#### Landing Pages

[Verbinden Sie Ihre eigene Domain]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/customizing_urls/) mit Ihrem Braze Workspace, um die URLs Ihrer Landing Page an Ihre Marke anzupassen.

#### LINE und Braze

{% multi_lang_include release_type.md release="Beta" %}

Wir haben eine neue Dokumentation hinzugefügt:

- [LINE Nachrichtentypen]({{site.baseurl}}/line/create/message_types/) behandelt die LINE Nachrichtentypen, die Sie verfassen können, einschließlich der Aspekte und Einschränkungen, und ist Teil der LINE Beta-Sammlung.
- [Die Verknüpfung von Nutzerkonten]({{site.baseurl}}/line/line_setup/#user-account-linking) ermöglicht es Nutzern:innen, ihr LINE-Konto mit dem Nutzerkonto Ihrer App zu verknüpfen. Sie können dann Liquid in Braze verwenden, z. B. {% raw %}`{{line_id}}`{% endraw %}, um eine personalisierte URL für den Benutzer zu erstellen, die die LINE-ID des Benutzers an Ihre Website oder App weiterleitet, die dann mit einem bekannten Benutzer verknüpft werden kann.

#### WhatsApp und Braze

[WhatsApp Business Accounts (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) können jetzt mit mehreren Anbietern von Business Lösungen geteilt werden.

### Neue Braze Partnerschaften

#### Future Anthem - Dynamische Inhalte

Die Partnerschaft von Braze und [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) nutzt Amplifier AI, um Personalisierung von Inhalten, Realtime-Erlebnisse und dynamische Zielgruppen bereitzustellen. Amplifier AI funktioniert in allen Sportarten, Casinos und Lotterien und erlaubt es Ihnen, die Profile von Braze-Spielern um branchenspezifische Attribute zu erweitern, wie z.B. Lieblingsspiel, Engagement-Score, erwarteter nächster Einsatz und mehr.

### Einstellungen

#### Verschlüsselung auf Indentifier-Feld-Ebene

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Mit der [Verschlüsselung auf Bezeichnerfeld-Ebene]({{site.baseurl}}/user_guide/analytics/field_level_encryption/) können Sie E-Mail-Adressen nahtlos mit dem AWS Key Management Service (KMS) verschlüsseln, um die in Braze freigegebenen personenbezogenen Daten (PII) zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Unterstützung für die [strikte Gleichzeitigkeitsprüfung in Swift 6](https://developer.apple.com/documentation/swift/adoptingswift6)
        - Relevante öffentliche Braze-Klassen und -Datentypen sind jetzt konform mit dem `Sendable` -Protokoll und können sicher in verschiedenen Gleichzeitigkeitskontexten verwendet werden.
        - APIs, die nur für den Hauptthread gedacht sind, werden jetzt mit dem Attribut `@MainActor` gekennzeichnet.
        - Wir empfehlen die Verwendung von Xcode 16.0 oder höher, um die Vorteile dieser Features zu nutzen und gleichzeitig die Anzahl der vom Compiler generierten Warnungen zu minimieren. Frühere Versionen von Xcode können weiterhin verwendet werden, aber einige Features können Warnungen erzeugen.
    - Bei der manuellen Integration der Push-Benachrichtigung müssen Sie möglicherweise die Konformität von `UNUserNotificationCenterDelegate` aktualisieren, um das Attribut `@preconcurrency` zu verwenden und Warnungen zu vermeiden.
        - Die Anwendung des Attributs `@preconcurrency` auf die Protokollkonformität ist nur in Xcode 16.0 oder höher verfügbar. Referenzieren Sie [hier](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual) unseren beispielhaften Integrationscode.
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Update der nativen Android-Versionsbindungen von [Braze Android SDK 31.1.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen iOS-Versionsbindungen von [Braze Swift SDK 10.3.0 auf 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Update von Kotlin 1.8 auf Kotlin 2.0.
- [Internet SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## Veröffentlichung am 17\. September 2024

### Flexibilität der Daten

#### Braze Cloud Data Ingestion für S3

Sie können [Cloud Data Ingestion (CDI) für S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) verwenden, um einen oder mehrere S3-Buckets in Ihrem AWS-Konto direkt in Braze zu integrieren. Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an SQS gesendet, und Braze Cloud Data Ingestion nimmt diese neuen Dateien auf.

#### Monatlich aktive Nutzer:innen CY 24-25

Für Kunden, die monatlich aktive:r Nutzer:innen - CY 24-25 erworben haben, verwaltet Braze verschiedene Rate-Limits auf seinem Endpunkt `/users/track`. Einzelheiten finden Sie unter [POST: Nutzer:innen tracken]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Kreativität entfesseln

#### Template für Katalogartikel einschließlich Liquid

{% multi_lang_include release_type.md release="Früher Zugang" %}

Verwenden Sie das Flag `:rerender` in einem Liquid-Tag, um [den Liquid-Inhalt eines Artikels darzustellen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Wenn Sie zum Beispiel den folgenden Liquid-Inhalt wiedergeben:

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Dies wird wie folgt angezeigt:

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Robuste Kanäle

#### WhatsApp Nachrichten als Antwort

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können [responsive Messaging]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) verwenden, um auf eingehende WhatsApp Nachrichten Ihrer Nutzer:innen zu antworten. Sie werden in Braze erstellt und können jederzeit bearbeitet werden. Sie können Liquid verwenden, um die Formulierung der responsiven Nachrichten anzupassen.

#### Canvas-Templates

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Erstellen Sie [Canvas-Templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/), um Ihr Messaging zu verfeinern, indem Sie einen konsistenten Rahmen schaffen, der sich leicht an Ihre spezifischen Ziele auf Ihren Canvase anpassen lässt.

#### Landing Pages

{% multi_lang_include release_type.md release="Beta" %}

Braze [Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) sind eigenständige Webseiten, die Ihre Strategie zur Gewinnung von Nutzer:innen und zum Engagement vorantreiben können.

#### Änderungen seit der letzten Ansicht

Sie können die Anzahl der Updates an Ihren [Canvase]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), Kampagnen und [Segmenten]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) durch andere Mitglieder Ihres Teams einsehen, indem Sie auf die Metrik *Änderungen seit der letzten Ansicht* auf den jeweiligen Übersichtsseiten referenzieren (z. B. auf der Übersichtsseite für eine [E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Fehlerbehebung bei Webhook- und Connected-Content-Anfragen 

[In diesem Artikel]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) erfahren Sie, wie Sie Fehlercodes von Webhooks und Connected-Content beheben können. Sie erfahren, um welche Fehler es sich handelt und wie Sie sie beheben können.

### Neue Braze Partnerschaften

#### Posteingang Monster - Analytics

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) ist eine Plattform für Posteingangssignale, die Unternehmensmarken dabei hilft, jeden Posteingang zu erreichen. Es handelt sich um eine integrierte Suite von Lösungen für Zustellbarkeit, kreatives Rendering und SMS-Überwachung, die moderne Teams im Bereich Customer Relationship Management (CRM) befähigt und die Angst vor dem Versand beendet.

#### SessionM - Loyalität

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) ist eine Plattform für Customer-Engagement und Kundentreue, die Marketern Features für das Kampagnenmanagement und Lösungen für das Loyalitätsmanagement zur Verfügung stellt, um das Engagement und den Gewinn durch gezielte Ansprache zu steigern.

### KI und ML Automatisierung

#### Empfehlungen zu aktuellen Artikeln

Zusätzlich zum „KI-Personalisierung“-Modell umfasst die Funktion [KI-Artikelempfehlungen]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) auch ein Empfehlungsmodell für „Trending“, das Artikel mit der positivsten Dynamik in Bezug auf die jüngsten Interaktionen der Nutzer:innen anzeigt.

### Einstellungen

#### Rollen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

[Rollen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) ermöglichen eine bessere Strukturierung, indem sie Ihre individuell angepassten Berechtigungen mit den Zugriffskontrollen für den Workspace bündeln. Das ist besonders nützlich, wenn Sie viele Marken oder regionale Workspaces in einem Dashboard haben. Mit Rollen können Sie Dashboard-Benutzer zu den richtigen Arbeitsbereichen hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. 

#### Bericht über Sicherheitsereignisse

Wir haben eine vollständige Liste der [Sicherheitsereignisse]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) hinzugefügt, die in Ihrem heruntergeladenen Sicherheitsbericht erscheinen können.

#### Bericht über die Nutzung von Nachrichten

{% multi_lang_include release_type.md release="Früher Zugang" %}

Das [Dashboard für die Nutzung von Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/message_usage/) bietet Ihnen Insights über die Nutzung Ihres SMS- und WhatsApp-Guthabens im Self-Service-Verfahren. So erhalten Sie einen umfassenden Überblick über die historische und aktuelle Nutzung im Vergleich zu den vertraglich festgelegten Kontingenten. Diese Insights können Unklarheiten ausräumen und Ihnen helfen, Anpassungen vorzunehmen, um Überschussrisiken zu vermeiden.

### SDK

#### Verzögerte Initialisierung für das Braze Swift SDK

Richten Sie eine [verzögerte Initialisierung]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) ein, um Ihr Braze Swift SDK asynchron zu initialisieren und gleichzeitig sicherzustellen, dass die Handhabung von Push-Benachrichtigungen erhalten bleibt. Dies kann nützlich sein, wenn Sie vor der Initialisierung des SDK andere Dienste einrichten müssen, wie z. B. das Abrufen von Konfigurationsdaten von einem Server oder das Warten auf die Nutzerzustimmung.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segmente Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Diese Version benötigt jetzt Cordova Android 13.0.0.
    - Eine vollständige Liste der Anforderungen an die Projektabhängigkeit finden Sie in der [Cordova Release-Ankündigung](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html). - Update der nativen Android Bridge [von Braze Android SDK 30.3.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen iOS-Bridge [von Braze Swift SDK 9.2.0 auf 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Update der nativen Android Bridge [von Braze Android SDK 30.3.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen iOS-Bridge [von Braze Swift SDK 9.0.0 auf 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Segment Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Update der Braze Swift SDK Bindungen, um Versionen der `10.2.0+` SemVer Bezeichnung zu benötigen.
        - Dies erlaubt die Kompatibilität mit jeder Version des Braze SDK von `10.2.0` bis hin zu, aber nicht einschließlich, `11.0.0`.
        - Lesen Sie den Eingang des Changelogs für [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) für weitere Informationen über mögliche Änderungen.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Aktualisiert die native Android-Bridge [von Braze Android SDK 30.4.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Ändert das Verhalten von `wipeData()` auf Android, um externe Abos (wie `subscribeToContentCards()`) nach dem Aufruf beizubehalten.
    - Update der nativen iOS-Bridge [von Braze Swift SDK 9.0.0 auf 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

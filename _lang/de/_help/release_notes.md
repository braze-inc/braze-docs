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

> Braze veröffentlicht Informationen zu Produkt-Updates in monatlichen Abständen, die sich an den großen Produkt-Releases orientieren. Das Produkt wird jedoch von Woche zu Woche mit verschiedenen Verbesserungen aktualisiert.<br><br>Weitere Informationen zu den in diesem Abschnitt aufgeführten Updates erhalten Sie von Ihrem Account Manager:in oder [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). In [unseren SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) finden Sie weitere Informationen zu unseren monatlichen SDK Releases, Updates und Verbesserungen.

## Juni 24, 2025 Veröffentlichung

### OfferFit von Braze

[OfferFit](https://www.offerfit.ai/) ersetzt A/B-Tests durch KI-Entscheidungen, die alles personalisieren und jede Metrik maximieren: Treiben Sie Dollars an, nicht Klicks - mit OfferFit können Sie jeden geschäftlichen KPI optimieren. In unserem speziellen Bereich [OfferFit by Braze]({{site.baseurl}}/user_guide/offerfit) finden Sie Beispiele für Anwendungsfälle und wichtige Features.

### Neue SDK-Tutorials

Jedes Braze SDK-Tutorial bietet eine Schritt-für-Schritt-Anleitung mit vollständigem Code-Beispiel. Wählen Sie unten ein Tutorial, um loszulegen:

- [Anzeigen von Bannern]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Anpassen des Stils von In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Bedingte Anzeige von In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Aufschieben von getriggerten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilität der Daten

#### SAML Just-in-Time-Bereitstellung

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Verwenden Sie [SAML Just-in-Time Provisioning]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit), damit neue Nutzer:innen des Dashboards bei ihrer ersten Anmeldung ein Braze-Konto erstellen können. Dadurch müssen Administratoren nicht mehr manuell ein Konto für einen neuen Dashboard-Benutzer erstellen, seine Berechtigungen auswählen, ihn einem Arbeitsbereich zuweisen und darauf warten, dass er sein Konto aktiviert.

#### Filter pro Auswahl

Sie können jetzt bis zu 10 Filter pro [Auswahl]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections) hinzufügen.

#### Katalogspeicher

Die Speichergröße für die kostenlose Version der [Kataloge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage) beträgt bis zu 100 MB. Sie können eine unbegrenzte Anzahl von Artikeln haben, solange sie weniger als 100 MB groß sind.

#### Anzahl der mit der Cloud-Datenaufnahme synchronisierten Zeilen

Standardmäßig können bei der Datenaufnahme in der Cloud pro Lauf bis zu 500 Millionen Zeilen synchronisiert werden. Alle Synchronisierungen mit mehr als 500 Millionen neuen Zeilen werden gestoppt.

Weitere Informationen finden Sie unter [Einschränkungen des Produkts Cloud Datenaufnahme]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations).

### Robuste Kanäle

#### Zugänglichkeitstests in Inbox Vision

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Verwenden Sie die [Zugänglichkeitstests]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) in Inbox Vision, um Probleme mit der Zugänglichkeit Ihrer E-Mails aufzuzeigen. 

Bei den Zugänglichkeitstests wird Ihr E-Mail-Inhalt anhand einiger Anforderungen der [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA analysiert. Dies kann Insights darüber liefern, welche Elemente nicht den Zugänglichkeitsstandards entsprechen.

#### Klick Tracking für WhatsApp

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können das [Tracking von Klicks]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) sowohl in Response- als auch in Template-Nachrichten aktivieren, um die Daten von Klicks in Ihren WhatsApp Performance-Berichten zu sehen und die Nutzer:innen anhand der Klicks zu segmentieren.

#### Videos für WhatsApp

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können bei ausgehenden WhatsApp Nachrichten in den Text [Videos einbetten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features). Diese Dateien müssen über eine URL oder in der [Bibliothek von Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) gehostet werden.

### Neue Braze Partnerschaften

#### Stripe - E-Commerce

Die Intergation zwischen Braze und [Stripe]({{site.baseurl}}/partners/stripe) ermöglicht es Ihnen, Messaging in Braze auf der Grundlage von Stripe-Ereignissen zu triggern, wie z.B. Beginn der Testphase, Aktivierung des Abos, Kündigung des Abos und mehr.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Update der nativen Android Bridge [von Braze Android SDK 35.0.0 auf 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen iOS-Bridge [von Braze Swift SDK 11.6.1 auf 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segmente Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Update des Braze Android SDK [von 35.0.0 auf 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## Mai 27, 2025 Veröffentlichung

### Flexibilität der Daten

#### Kopieren von Canvase über Workspaces hinweg

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können Canvase jetzt über Workspaces hinweg kopieren. Auf diese Weise können Sie mit dem Verfassen von Nachrichten beginnen, indem Sie mit einer Kopie eines Canvas in einem anderen Workspace beginnen. Weitere Informationen darüber, was kopiert wird, finden Sie unter [Kopieren von Kampagnen und Canvase über Workspaces hinweg]({{site.baseurl}}/copying_to_workspaces/).

#### Messaging-Regeln für den Genehmigungs-Workflow 

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Verwenden Sie [Messaging-Regeln]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) in Ihrem Genehmigungs-Workflow, um die Anzahl der erreichbaren Nutzer:innen zu begrenzen, bevor eine zusätzliche Genehmigung erforderlich ist. Auf diese Weise können Sie Ihre Kampagnen und Canvase überprüfen, bevor Sie eine größere Zielgruppe zusammenstellen.

#### Entity-Relationship-Diagramme für Snowflake und Braze

Zu Beginn dieses Jahres haben wir Tabellen mit Entitätsbeziehungen für Daten erstellt, die von Snowflake und Braze gemeinsam genutzt werden. Diesen Monat haben wir [neue interaktive Diagramme]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) hinzugefügt, in denen Sie die Details der einzelnen Tabellen schwenken, greifen und zoomen können. So erhalten Sie eine bessere Idee davon, wie Ihre Daten mit Braze interagieren.

### Kreativität entfesseln

#### Empfohlene Ereignisse

{% multi_lang_include release_type.md release="Früher Zugang" %}

Die [empfohlenen Ereignisse]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) sind den häufigsten E-Commerce-Anwendungsfällen zugeordnet. Durch die Verwendung von empfohlenen Events können Sie vorgefertigte Canvas-Templates, Dashboards zur Berichterstellung, die an den Kundenlebenszyklus angepasst sind, und vieles mehr freischalten.

### Robuste Kanäle

#### Banner-Kanal

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Mit [Bannern]({{site.baseurl}}/user_guide/message_building_by_channel/banners) können Sie personalisierte Nachrichten für Ihre Nutzer:innen erstellen und gleichzeitig die Reichweite Ihrer anderen Kanäle, wie E-Mail oder Push-Benachrichtigungen, erhöhen. Sie können Banner direkt in Ihre App oder Website einbetten, wodurch Sie sich mit den Nutzer:innen durch ein natürliches Erlebnis verbinden können.

#### Kanal für Rich Communication Serviceleistungen; Dienste (RCS)

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

[Rich Communication Serviceleistungen; Dienste (RCS)]({{site.baseurl}}/about_rcs/) verbessern die traditionelle SMS, indem sie Marken in die Lage versetzen, Nachrichten zuzustellen, die nicht nur informativ sind, sondern auch ein weitaus größeres Engagement bieten. RCS wird jetzt sowohl von Android als auch von iOS unterstützt und bringt Features wie hochwertige Medien, interaktive Buttons und gebrandete Absenderprofile direkt in die vorinstallierten Messaging-Apps der Nutzer:innen, so dass der Download einer separaten App entfällt.

#### Seite Push-Einstellungen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Auf der [Seite **Push-Einstellungen**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) können Sie die wichtigsten Einstellungen für Ihre Push-Benachrichtigungen konfigurieren, darunter die Push-Time-to-Live (TTL) und die Standard FCM-Priorität für Android Kampagnen. Mit diesen Einstellungen können Sie die Zustellung und Effektivität Ihrer Push-Benachrichtigungen optimieren und so ein besseres Erlebnis für Ihre Nutzer:innen gewährleisten.

#### Aktionscodes für In-App-Nachricht-Kampagnen

{% multi_lang_include release_type.md release="Früher Zugang" %}

Sie können [Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) in In-App-Nachricht-Kampagnen verwenden, indem Sie ein [Snippet mit einer Aktionscode-Liste]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) in den Nachrichtentext Ihrer In-App-Nachricht-Kampagne einfügen.

#### Umgang mit Webhook-Fehlern und Rate-Limiting

[Über Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting) enthält einen neuen Abschnitt, der beschreibt, wie Braze mit Webhook-Fehlern und Rate-Limiting umgeht.

#### Lokalisierung von In-App-Nachricht

Nachdem Sie Ihrem Workspace [Lokalisierungen hinzugefügt haben]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales), können Sie Nutzer:innen in verschiedenen Sprachen in einer einzigen In-App-Nachricht zusammenstellen.

#### Amazon SES als Anbieter für den E-Mail-Versand (ESP)

Sie können jetzt Amazon SES als ESP verwenden, ähnlich wie Sie SendGrid und SparkPost verwenden würden. Siehe [SSL bei Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) und [Universal Links und App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) für die Feinheiten der SSL-Einrichtung und des Trackings von Klicks auf einer Link-zu-Link-Basis.

### Neue Braze Partnerschaften

#### Eagle Eye - Loyalität

Die bidirektionale Integration von Braze und [Eagle Eye]({{site.baseurl}}/partners/eagle_eye/) ermöglicht es Ihnen, Treue- und Aktionsdaten direkt in Braze zu aktivieren, was es Marketern erlaubt, das Customer-Engagement anhand von Echtzeitdaten wie Punktesalden, Aktionen und Belohnungsaktivitäten anzupassen.

#### Eppo - A/B-Tests

Die Integration von Braze und [Eppo]({{site.baseurl}}/partners/eppo/) erlaubt es Ihnen, A/B-Tests in Braze einzurichten und die Ergebnisse in Eppo zu analysieren, um Insights zu gewinnen und die Performance der Nachrichten mit langfristigen Metriken wie Umsatz oder Bindung zu verknüpfen.

#### Mention Me - Empfehlungen

Gemeinsam können [Mention Me](https://www.mention-me.com/) und Braze Ihr Tor zur Gewinnung von Premium-Kund:innen und zur Förderung einer unerschütterlichen Markentreue sein. Durch die nahtlose Integration von First-Party-Daten für Empfehlungen in Braze können Sie hoch personalisierte Omnichannel-Erlebnisse liefern, die auf Ihre Markenfans zugestellt sind. Weitere Informationen finden Sie unter [Technologiepartner: Erwähnen Sie mich]({{site.baseurl}}/partners/mention_me).

#### Shopify - E-Commerce

[Verbinden Sie mehrere Shopify Domains]({{site.baseurl}}/shopify_connecting_multiple_stores/) mit einem einzigen Workspace, um einen ganzheitlichen Überblick über Ihre Kund:innen in allen Märkten zu erhalten. Erstellen und starten Sie Automatisierungsprogramme und Journeys in einem einzigen Workspace, ohne doppelte Arbeit in den regionalen Shops.

### Sonstiges

#### Update auf Building accessible messages in Braze

Wir haben unseren Artikel [Erstellen von barrierefreien Nachrichten in Braze]({{site.baseurl}}/help/accessibility/) mit einer klareren, genaueren Anleitung zum Erstellen von barrierefreien Nachrichten aktualisiert. Dieser Artikel enthält jetzt erweiterte Best Practices für Inhaltsstruktur, Alt-Text, Buttons und Farbkontrast sowie einen neuen Abschnitt über die ARIA-Behandlung angepasster HTML-Nachrichten. 

Dieses Update ist Teil unserer umfassenderen Bemühungen, Messaging-Erlebnisse in Braze zugänglicher zu machen. Wir wissen, dass Barrierefreiheit ein Bereich ist, der sich ständig weiterentwickelt, und wir werden unsere Erkenntnisse weitergeben.

{% multi_lang_include accessibility/feedback.md %}

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Diese Version macht die Erhöhung der Mindestversion des Android SDK von Braze von API 21 auf API 25 rückgängig, die in 34.0.0 eingeführt wurde. Damit ist es zulässig, dass das SDK wieder in Apps kompiliert wird, die bereits API 21 unterstützen. Bitte beachten Sie, dass wir zwar die Kompilierbarkeit wieder einführen, aber keine formale Unterstützung für < API 25\. Wir können nicht garantieren, dass das SDK auf Geräten mit diesen Versionen wie vorgesehen funktioniert.
    - Wenn Ihre App diese Versionen unterstützt, sollten Sie das tun:
        - Überprüfen Sie, ob Ihre Integration des SDK auf physischen Geräten (nicht nur Emulatoren) für diese API-Versionen wie vorgesehen funktioniert.
        - Wenn Sie das erwartete Verhalten nicht überprüfen können, müssen Sie entweder [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) aufrufen oder das SDK auf diesen Versionen nicht initialisieren. Andernfalls kann es auf den Geräten Ihrer Endnutzer:innen zu unbeabsichtigten Nebeneffekten oder einer verminderten Performance kommen.
    - Ein Problem wurde behoben, bei dem In-App-Nachrichten einen Lesezugriff auf den Hauptthread verursachten.
    `BrazeInAppMessageManager.displayInAppMessage` ist jetzt eine Kotlin Suspend-Funktion.
        - Wenn Sie diese Funktion nicht direkt aufrufen, müssen Sie keine Änderungen vornehmen.
    - AndroidX Compose BOM aktualisiert auf 2025.04.01, um Updates in den Jetpack Compose APIs zu verarbeiten.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Aktualisiert die native Android-Bridge von Braze Android SDK 35.0.0 auf 36.0.0.
    - Update der nativen iOS-Versionsbindungen von Braze Swift SDK 11.9.0 auf 12.0.0.
    - Update der Einheit von PushNotificationEvent.timestamp auf Millisekunden unter iOS.
        - Zuvor wurde dieser Wert unter iOS in Sekunden angegeben. Dies entspricht nun der bestehenden Android-Implementierung.
- [Internet SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Diese Version macht die Erhöhung der Mindestversion des Android SDK von Braze von API 21 auf API 25 rückgängig, die in 34.0.0 eingeführt wurde. Damit ist es zulässig, dass das SDK wieder in Apps kompiliert wird, die bereits API 21 unterstützen. Wir werden jedoch keine formale Unterstützung für < API 25 wieder einführen. Lesen Sie [hier](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600) mehr.
    - Aktualisiert die native Android-Bridge von Braze Android SDK 35.0.0 auf 36.0.0.
    - Update der nativen iOS-Bridge von Braze Swift SDK 11.9.0 auf 12.0.0.

## April 29, 2025 Veröffentlichung

### Fehlerbehebung Braze Zugang

[Die Fehlerbehebung für den Braze-Zugang]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/) hilft Ihnen bei Problemen, die beim Zugriff auf Braze auftreten können, z. B. wenn Sie aus Ihrem Konto ausgesperrt werden oder mit einem Braze-Dashboard arbeiten, das nicht die erwartete Performance aufweist.

### Flexibilität der Daten

#### Häufig gestellte Fragen zu Currents

Antworten auf einige häufig gestellte Fragen zu Currents finden Sie auf der neuen Seite [Häufig gestellte Fragen]({{site.baseurl}}/user_guide/data/braze_currents/faq/).

#### Anonyme Nutzer:innen

In den folgenden Abschnitten unter [Anonyme Nutzer:innen]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) erfahren Sie mehr darüber, wie anonyme Nutzer:innen funktionieren und warum Sie ihnen möglicherweise User-Alias zuweisen sollten:
- [Funktionsweise]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [User-Aliasing für Nutzer:innen zuweisen]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### Entwürfe für Kampagnen

[Das Speichern von Entwürfen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts) kann Ihnen helfen, umfangreiche Änderungen an aktiven Kampagnen vorzunehmen. Wenn Sie einen Entwurf erstellen, können Sie geplante Änderungen vor der nächsten Veröffentlichung testen.

#### Identifizierung und Zusammenführung von Nutzer:innen

Bei der [Identifizierung]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) oder [Zusammenführung von Nutzer:innen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) können Sie jetzt den Parameter `least_recently_updated` im Array `prioritization` verwenden, um den am wenigsten aktualisierten Nutzer zu priorisieren.

#### Zeitplan für die Zusammenführung von Nutzer:innen

Mit [dem Zeitplan für die Zusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging) können Sie die Zusammenführung von Nutzerprofilen auf täglicher Basis anhand vorkonfigurierter Regeln automatisieren. Braze benachrichtigt die Administratoren Ihres Workspace 24 Stunden vor der geplanten Zusammenführung und gibt Ihnen eine Erinnerung und Zeit, um die Konfiguration zu überprüfen.

#### Empfänger:innen Objekt

Sie können jetzt `braze_id` in das [Empfänger:in-Objekt]({{site.baseurl}}/api/objects_filters/recipient_object/) aufnehmen, was es Ihnen erlaubt, Informationen in unseren Endpunkten anzufragen oder zu schreiben.

#### Neue Datenzentren

Braze hat zwei neue [Datenzentren]({{site.baseurl}}/user_guide/data/data_centers/) in Betrieb genommen: US-10 und ID-01. Sie können sich bei der Einrichtung Ihres Braze-Kontos für regionsspezifische Datenzentren registrieren. 

### Kreativität entfesseln

#### Landing Page Templates

Verwenden Sie [Landing Page Templates]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates), um Vorlagen für Ihre nächsten Kampagnen zu erstellen. Diese Templates können sowohl im Landing Page Editor als auch im Bereich **Templates** des Dashboards aufgerufen und verwaltet werden.

#### Landing Page Formularfeld

Wenn Sie Ihre Landing Page anpassen, können Sie wählen, ob ein Formularfeld [erforderlich oder optional]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) ist. Erforderliche Felder müssen ausgefüllt werden, bevor das Formular abgeschickt werden kann. Optionale Felder können leer bleiben oder von einem Nutzer:innen nicht ausgewählt werden.

#### Vorgefertigte Canvas Templates

Braze-Canvas bietet mehrere [vorgefertigte Templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/), die speziell auf E-Commerce Marketer zugeschnitten sind und die Umsetzung wichtiger Strategien erleichtern. Auf dieser Seite finden Sie einige wichtige Templates, die Sie verwenden können, um Ihre Customer Journey zu verbessern.

### Robuste Kanäle

#### WhatsApp Videos

{% multi_lang_include release_type.md release="Früher Zugang" %}

[WhatsApp Videos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages) können jetzt entweder über eine URL oder in der Bibliothek von Braze gehostet werden.

#### WhatsApp Liste Nachrichten

[Nachrichten in der Liste]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/) erscheinen als Nachricht mit einer Liste von anklickbaren Optionen. Jede Liste kann mehrere Abschnitte haben, und jede Liste kann bis zu 10 Zeilen haben.

#### Vorschau-Link kopieren

Verwenden Sie den **Link Vorschau kopieren** in Ihren HTML- und [Drag-and-Drop-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information), [E-Mail-Templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message) und [Content-Blöcken]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), um einen Link zum Teilen zu generieren, der zeigt, wie Ihre Inhalte für einen zufälligen Nutzer:innen aussehen.

#### Push-Registrierungsdiagramm

Wir haben unsere Dokumentation zur Push-Benachrichtigung im Benutzerhandbuch überarbeitet und ein neues Diagramm hinzugefügt, um zu veranschaulichen [, wie die Push-Registrierung in größerem Maßstab aussieht]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale).

### Neue Braze Partnerschaften

#### Update der Partner-Kategorien

Wir haben den [Bereich Technologiepartner]({{site.baseurl}}/partners/home/) mit neuen Kategorien und Unterkategorien aktualisiert, um Ihre Navigation zu verbessern.

#### Shopify (neue Version) - E-Commerce

Eine neue Version der Shopify Integration wird ab April schrittweise veröffentlicht, abhängig von der Art des Shopify Shops und der externen ID, die zur Einrichtung der ersten Integration verwendet wurde.

**Die ältere Version der Integration wird am 28\. August 2025 veraltet sein. Sie müssen vor dem 28\. August 2025 auf die neuere Version der Integration aktualisieren.**

Neue Braze Kund:in: Ab April 2025 wird Braze den neuen Shopify Konnektor schrittweise für neue Onboardings und Upgrades von bestehenden Kund:in einführen. Um mehr über die neue Standard Integration zu erfahren, lesen Sie [Shopify Standard Integration]({{site.baseurl}}/shopify_standard_integration/).

#### Just Words - Dynamische Inhalte

[Just Words]({{site.baseurl}}/partners/just_words/) personalisiert Nachrichten in großem Umfang auf Lifecycle-Marketing-Kanälen und ermöglicht es Ihnen, Hunderte von Variationen dynamisch zu testen und unterdurchschnittliche Inhalte automatisch zu aktualisieren.

#### Tapcart - E-Commerce

[Tapcart]({{site.baseurl}}/partners/ecommerce/tapcart/) ist eine führende Mobile-Commerce-Plattform für Shopify-basierte Marken, die es Händlern ermöglicht, angepasste mobile Apps zu erstellen, die personalisierte, engagierte Einkaufserlebnisse liefern, die ihre Kunden lieben.

### SDKs

#### Braze SDK Versionsverwaltung

Sie können sich jetzt über die [Versionsverwaltung]({{site.baseurl}}/developer_guide/sdk_integration/version_management/) für das Braze SDK informieren, so dass Ihre App mit den neuesten Features und Qualitätsverbesserungen auf dem neuesten Stand bleiben kann.

#### SDK-Dokumente prüfen

Wir überprüfen derzeit alle unsere [SDK-Inhalte für Entwickler:innen]({{site.baseurl}}/developer_guide/), um sicherzustellen, dass alle unsere Code-Beispiele hilfreich und korrekt sind. Bislang haben wir eine Reihe von Updates für unsere Android- und Swift-Dokumente vorgenommen, und weitere sind in Vorbereitung.

### Zur Braze-Dokumentation beitragen

#### Offline-Unterstützung für Braze-Mitarbeiter

Wenn Sie zu Braze Docs beitragen, können Sie Ihre lokale Docs-Website jetzt vollständig offline erstellen. Um damit zu beginnen, lesen Sie bitte [Beitrag zu Braze Docs]({{site.baseurl}}/contributing/home/).

#### Fehlerbehebung für Ihren Braze Docs Fork

Für Braze Docs-Mitwirkende, die Probleme beim Targeting unseres Repository von ihrem Fork aus haben, haben wir eine [Fehlerbehebung]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository) erstellt, die Sie wieder auf den richtigen Weg bringt.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Braze Unity SDK 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - Update der nativen iOS-Bridge von [Braze Swift SDK 10.3.0 auf 11.9.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen Android Bridge von [Braze Android SDK 32.1.0 auf 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Die erforderliche Android SDK-Version ist mindestens 25. Weitere Einzelheiten finden Sie [hier](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Segmente Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Update des Braze Android SDK [von 32.1.0 auf 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Die erforderliche Android SDK-Version ist mindestens 25. Weitere Einzelheiten finden Sie [hier](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - Die verteilten statischen XCFrameworks binden ihre Ressourcen nun direkt ein, anstatt sich auf externe Ressourcen-Bundles zu verlassen.
        - Wenn Sie die statischen XCFrameworks manuell integrieren, müssen Sie für jedes XCFramework die Option *Einbetten & Signieren* im Abschnitt *Frameworks, Bibliotheken und eingebettete Inhalte* in den *allgemeinen Einstellungen* Ihres Targetings auswählen.
        - Für Swift-Paketmanager- oder CocoaPods-Integrationen sind keine Änderungen erforderlich.
- [Braze Segmente Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Update der Braze Swift SDK Bindungen, um Versionen der `12.0.0`+ SemVer Bezeichnung zu benötigen.
        - Dies erlaubt die Kompatibilität mit jeder Version des Braze SDK von `12.0.0` bis hin zu, aber nicht einschließlich, `13.0.0`.
        - Lesen Sie den Eingang des Changelogs für [`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) für weitere Informationen über mögliche Änderungen.

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

Wenn Sie zielgerichtete Kampagnen und Segmente erstellen, werden Sie vielleicht feststellen, dass Sie kein angepasstes Event oder angepasstes Attribut mehr benötigen. Sie können jetzt [diese angepassten Daten löschen]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) und ihre Referenzen aus Ihrer App entfernen.

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

Es gibt jetzt drei [Standardattribute für Nutzerprofile]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/) in Snowflake. Jede Ansicht ist für einen bestimmten Anwendungsfall mit eigenen Performance-Überlegungen konzipiert. So können Sie zum Beispiel einen regelmäßigen Snapchat der Standardattribute eines Nutzerprofils erhalten.

### Robuste Kanäle

#### Grundlagen des Messaging

[Messaging Fundamentals]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) ist ein neuer Bereich in Engagement Tools, der die gemeinsamen Konzepte und Begriffe für Kampagnen und Canvase enthält, wie z.B. die Archivierung und Lokalisierung von Nachrichten.

#### WhatsApp angepasste Domains

Sie können jetzt [angepasste Domains]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) einer oder mehreren Abo-Gruppen von WhatsApp zuweisen.

#### Getriggerte In-App-Nachrichten für Canvas

Sie können jetzt einen [Auslöser für Ihre In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) auswählen, der bei Sitzungsbeginn oder durch angepasste Events und Käufe getriggert wird. Nachdem alle Verzögerungen verstrichen sind und die Optionen für die Zielgruppe aktiviert wurden, werden In-App-Nachrichten aktiviert, sobald ein Nutzer:innen den Schritt Nachricht erreicht. Wenn ein Nutzer eine Sitzung startet und das Trigger-Ereignis für die In-App-Nachricht ausführt, sieht der Nutzer:in die In-App-Nachricht. 

#### Eingangsvolumen für Canvas begrenzen

Sie können die Anzahl der Personen, die dieses Canvas betreten können, durch eine ausgewählte Kadenz begrenzen (täglich, Lifetime des Canvas oder jedes Mal, wenn das Canvas geplant ist). Sie können zum Beispiel [die Eingangskontrollen anpassen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience), sodass der Canvas nur an 5.000 Nutzer:innen pro Tag senden darf.

#### Neuer Anwendungsfall: Buchungserinnerung per E-Mail

Erfahren Sie, wie Sie die Features von Braze nutzen können, um [einen E-Mail Messaging-Dienst für Buchungserinnerungen aufzubauen]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). Der Dienst erlaubt es Nutzern:innen, Termine zu buchen, und sendet ihnen Nachrichten, um sie an ihre Termine zu erinnern. Obwohl in diesem Anwendungsfall E-Mail-Nachrichten verwendet werden, können Sie Nachrichten in einem beliebigen oder mehreren Kanälen auf der Grundlage eines einzigen Updates eines Nutzerprofils versenden.

#### Tracking von Klicks für bestimmte Links

Sie können für bestimmte Links [das Tracking von Klicks]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) deaktivieren, indem Sie Ihrer E-Mail Nachricht im HTML-Editor oder den Komponenten im Drag-and-Drop-Editor HTML-Code hinzufügen.

#### Dynamischer Apple Push-Benachrichtigungsdienst - Gateway-Verwaltung

Die [dynamische APN-Gateway-Verwaltung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) verbessert die Zuverlässigkeit und Effizienz von iOS Push-Benachrichtigungen, indem sie automatisch die richtige APN-Umgebung erkennt. Früher mussten Sie die APN-Umgebungen (Entwicklung oder Produktion) für Ihre Push-Benachrichtigungen manuell auswählen, was manchmal zu falschen Gateway-Konfigurationen, Zustellungsfehlern und BadDeviceToken-Fehlern führte.

#### Flutter Unterstützung für Banner

{% multi_lang_include release_type.md release="Früher Zugang" %}

Banner unterstützen jetzt Flutter. Außerdem wurde die gesamte Dokumentation von Banner überarbeitet, um die Benutzerfreundlichkeit zu verbessern. Lesen Sie die folgenden Artikel, um loszulegen:

- [Über Banner]({{site.baseurl}}/developer_guide/banners/)
- [Erstellen von Banner-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [Banner in Ihre App einbetten]({{site.baseurl}}/developer_guide/banners/creating_placements/)

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

[Die Verwendung von Artikel-Empfehlungen im Messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) deckt das Liquid Objekt `product_recommendation` ab und enthält ein Tutorial, das Ihnen hilft, dieses Wissen in die Praxis umzusetzen.

### Neue Braze Partnerschaften
 
#### E-Mail Liebe - Kanal Erweiterungen
 
Die Partnerschaft zwischen Braze und [Email Love]({{site.baseurl}}/partners/message_orchestration/) nutzt das Feature Export to Braze von Email Love und die Braze API, um Ihre E-Mail Templates nahtlos in Braze hochzuladen.

#### VWO - A/B-Tests
 
Die Integration von Braze und [VWO]({{site.baseurl}}/partners/data_and_analytics/ab_testing/vwo/) erlaubt es Ihnen, VWO-Experimentdaten zu nutzen, um gezielte Segmente zu erstellen und personalisierte Kampagnen zu liefern.
 
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

Sie können jetzt einen Empfänger:in per E-Mail angeben, um Ihre [Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) und [Canvase]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience) zu triggern.

#### Verwendung einer Telefonnummer zur Identifizierung eines Nutzer:innen über die API

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt zusätzlich zu einem Alias und einer E-Mail Adresse eine Telefonnummer verwenden, um einen Nutzer:innen über den [Endpunkt der`/users/identify` API]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) zu identifizieren.

#### Abrufen einer SAML-Ablaufverfolgung
Wir haben [Schritte zum Erhalten eines SAML-Trace]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace) hinzugefügt, der Ihnen hilft, Probleme mit SAML SSO mit dem Support effizienter zu lösen.
 
#### Regionale Datenzentren
Da Braze wächst und neue Bereiche bedient, haben wir einen [Artikel über die Datenzentren von Braze]({{site.baseurl}}/user_guide/data/data_centers) hinzugefügt, um unseren operativen Ansatz zu erläutern.
 
### Kreativität entfesseln
 
#### Benachrichtigungen über Preissenkungen und Wiederverfügbarkeitsmeldungen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt Kunden:in benachrichtigen, wenn ein Artikel wieder vorrätig ist, indem Sie über ein Canvas und einen Katalog eine [Benachrichtigung über wieder vorrätige Artikel einrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications).

Sie können auch [Preissenkungsbenachrichtigungen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) erstellen, um Kund:in zu benachrichtigen, wenn der Preis eines Artikels gesunken ist, indem Sie Preissenkungsbenachrichtigungen in einem Katalog und Canvas einrichten.

#### Vorschau zum Auswählen 

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Nachdem Sie eine Auswahl erstellt haben, können Sie sehen, was eine Auswahl für einen zufälligen Nutzer:innen oder einen bestimmten Nutzer:innen [ergeben würde]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview).

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
[Constructor]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/constructor/) ist eine Such- und Produktentdeckungsplattform, die KI und maschinelles Lernen nutzt, um personalisierte Suchanfragen, Empfehlungen und Browsing-Erlebnisse für E-Commerce- und Einzelhandels-Websites bereitzustellen.
 
#### Trustpilot - Dynamische Inhalte
[Trustpilot]({{site.baseurl}}/partners/trustpilot/) ist eine Online-Bewertungsplattform, die es Ihren Kunden ermöglicht, Feedback zu geben, und die es Ihnen erlaubt, Bewertungen zu verwalten und darauf zu reagieren.

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

[Justuno]({{site.baseurl}}/partners/data_and_analytics/leads_capture/justuno/) ermöglicht es Ihnen, mit dynamischen Segmenten ein vollständig optimiertes Besuchererlebnis für alle Ihre Zielgruppen zu schaffen und bietet das fortschrittlichste Targeting, das es gibt - und das alles, ohne die Geschwindigkeit der Website zu beeinträchtigen oder die Entwicklungsarbeit zu erhöhen.

#### Odicci - Customer Data Platform (CDP) - Kundendaten

Integrieren Sie Braze mit [Odicci]({{site.baseurl}}/partners/odicci/), einer Plattform, die es Unternehmen ermöglicht, Kunden durch loyalitätsorientierte Omnichannel-Erlebnisse zu gewinnen, zu engagieren und zu binden.

#### Optimizely - A/B-Tests

Die Integration von Braze und [Optimizely]({{site.baseurl}}/partners/data_and_analytics/ab_testing/optimizely/) ist eine bidirektionale Integration, die es Ihnen erlaubt:

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

Segmentieren Sie Ihre Nutzer:innen nach dem e.164 Telefonnummernfeld. Mit diesem Filter können Sie reguläre Ausdrücke verwenden, um nach Telefonnummern mit einem bestimmten Ländercode zu segmentieren.

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

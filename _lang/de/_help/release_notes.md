---
nav_title: Anmerkungen zur Veröffentlichung
article_title: Anmerkungen zur Veröffentlichung
page_order: 4
layout: dev_guide
guide_top_header: "Anmerkungen zur Veröffentlichung"
guide_top_text: "Hier finden Sie alle Aktualisierungen der Braze-Plattform, mit den folgenden <a href='/docs/help/release_notes/#most-recent'>neuesten Plattform-Updates</a>."
page_type: landing
search_rank: 1
description: "Auf dieser Landing Page finden Sie die Versionshinweise von Braze. Hier finden Sie alle Updates für die Braze-Plattform und SDKs sowie eine Liste veralteter Funktionen."

guide_featured_title: "Anmerkungen zur Veröffentlichung"
guide_featured_list:
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
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Die neuesten Braze Versionshinweise {#most-recent}

> Braze veröffentlicht Informationen zu Produkt-Updates in monatlichen Abständen, die sich an den großen Produkt-Releases orientieren, obwohl das Produkt von Woche zu Woche mit verschiedenen Verbesserungen aktualisiert wird.
> <br>
> <br>
> Wenn Sie weitere Informationen zu den in diesem Abschnitt aufgeführten Updates wünschen, wenden Sie sich an Ihren Kundenbetreuer oder [eröffnen Sie ein Support-Ticket]({{site.baseurl}}/help/support/). In [unseren SDK-Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) finden Sie weitere Informationen zu unseren monatlichen SDK-Versionen, Updates und Verbesserungen.

## Veröffentlichung im Dezember 10, 2024

### SDK-Benutzerstandort nach IP-Adresse

Ab dem 26\. November 2024 wird Braze den Standort des Nutzers anhand der IP-Adresse vom Beginn der ersten SDK-Sitzung an ermitteln. Braze verwendet die IP-Adresse, um den Länderwert in Benutzerprofilen festzulegen, die über das SDK erstellt werden, und diese IP-basierte Ländereinstellung ist während und nach der ersten Sitzung verfügbar. Weitere Einzelheiten finden Sie unter [Standortverfolgung]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Einstellung "Erhöhter Zugang

[Elevated Access]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) bietet eine zusätzliche Sicherheitsebene für sensible Aktionen in Ihrem Braze Dashboard. Wenn sie aktiv sind, müssen Benutzer ihr Konto erneut verifizieren, bevor sie ein Segment exportieren oder einen API-Schlüssel anzeigen können. Um den erweiterten Zugriff zu verwenden, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Sicherheitseinstellungen** und schalten Sie die Option ein.

### Erlaubnis zur Einsichtnahme in persönlich identifizierbare Informationen (PII)

Für Administratoren können Sie [Benutzern erlauben, die]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) von Ihrem Unternehmen im Dashboard definierten [PII]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) in Nachrichtenvorschauen [anzuzeigen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions), die Liquid-Variablen für den Zugriff auf Benutzereigenschaften verwenden. 

Für Arbeitsbereiche können Sie Benutzern erlauben, die von Ihrem Unternehmen definierten PII im Dashboard anzuzeigen, oder Benutzerprofile anzuzeigen, aber Felder, die Ihr Unternehmen als PII identifiziert hat, zu schwärzen.

### Flexibilität der Daten

#### Data Lake Schemata

Die folgenden Schemata wurden zu den Rohtabellenschemata hinzugefügt:
- `USERS_CANVASSTEP_PROGRESSION_SHARED`: Fortschrittsereignisse für einen Benutzer in einem Canvas
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`: Identifizieren Sie, welche zufälligen Eimernummern sich in der aktuellen und der vorherigen globalen Kontrollgruppe befinden.
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`: Impressionsereignisse, wenn ein Benutzer ein Feature-Flag ansieht

#### Kontobasierte Segmentierung

Je nachdem, wie Sie Ihr [B2B-Datenmodell]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) einrichten, können Sie [die kontobasierte Segmentierung]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) auf zwei Arten vornehmen:

- Wenn Sie Kataloge für Ihre Geschäftsobjekte verwenden
- Wenn Sie verbundene Quellen für Ihre Geschäftsobjekte verwenden

#### Segmentierungsfilter

Unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) finden Sie eine vollständige Liste der Segmentierungsfilter und ihrer Beschreibungen.

##### Benutzerprofil erstellt bei

Segmentieren Sie Ihre Benutzer danach, wann ihr Benutzerprofil erstellt wurde. Wenn ein Benutzer per CSV oder API hinzugefügt wurde, zeigt dieser Filter das Datum an, an dem er hinzugefügt wurde. Wenn der Benutzer nicht per CSV oder API hinzugefügt wurde und seine erste Sitzung vom SDK aufgezeichnet wurde, spiegelt dieser Filter das Datum dieser ersten Sitzung wider.

##### Rufnummer senden

Segmentieren Sie Ihre Nutzer nach dem Feld e.164 Telefonnummer. Sie können mit diesem Filter reguläre Ausdrücke verwenden, um nach Telefonnummern mit einer bestimmten Landesvorwahl zu segmentieren.

### Neue Lötpartnerschaften

#### Narvar - Ökologischer Handel

Die Integration von Braze und [Narvar](https://corp.narvar.com/) ermöglicht es Marken, die Benachrichtigungsereignisse von Narvar zu nutzen, um Nachrichten direkt von Braze auszulösen und Kunden mit zeitnahen Updates auf dem Laufenden zu halten.

#### Zeotap für Currents - Plattform für Kundendaten

Die Integration von Braze und [Zeotap](https://zeotap.com/) ermöglicht es Ihnen, den Umfang und die Reichweite Ihrer Kampagnen zu vergrößern, indem Sie die Kundensegmente von Zeotap mit den Benutzerprofilen von Braze synchronisieren. Mit [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) können Sie die Daten auch mit Zeotap verbinden, um sie für das gesamte Wachstumsprogramm nutzbar zu machen.

#### Benachrichtigen - Dynamischer Inhalt

Die Integration von Braze und [Notify](https://notifyai.io/) ermöglicht es Marketingfachleuten, das Engagement über verschiedene Plattformen hinweg effektiv zu steigern. Anstatt sich auf herkömmliche Marketingmethoden zu verlassen, kann eine durch die Braze API ausgelöste Kampagne die Funktionen von Notify nutzen, um personalisierte Nachrichten über mehrere Kanäle zu versenden, darunter E-Mail, SMS, Push-Benachrichtigungen und mehr.

#### Contentful - Dynamischer Inhalt

Die Integration von Braze und [Contentful](https://www.contentful.com/) ermöglicht es Ihnen, dynamisch Connected Content zu verwenden, um Inhalte aus Contentful in Ihre Braze-Kampagnen zu ziehen.

#### Outgrow - Leads erfassen 

Mit der Integration von Braze und [Outgrow](https://outgrow.co/) können Sie automatisch Benutzerdaten aus Outgrow in Braze übertragen und so hochgradig personalisierte und zielgerichtete Kampagnen ermöglichen.

### SDK Aktualisierungen

Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Web SDK 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Aktualisiert die native iOS-Bridge [von Braze Swift SDK 10.3.1 auf 11.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Aktualisiert die native Android-Bridge [von Braze Android SDK 32.1.0 auf 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## Veröffentlichung am 12\. November 2024
 
### Flexibilität der Daten
 
#### Geschwindigkeitsbegrenzung für `/users/track`

Die Geschwindigkeitsbegrenzung für den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) wurde auf 3.000 pro 3 Sekunden aktualisiert.
 
### Kreativität entfesseln

#### Canvas Anwendungsfälle

Wir haben einige Anwendungsfälle zusammengestellt, die zeigen, wie Sie ein Braze Canvas nutzen können. Wenn Sie nach Inspiration suchen, wählen Sie unten einen Anwendungsfall aus, um loszulegen.

- [Abgebrochener Wagen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [Wieder auf Lager]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Merkmal Adoption]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Verfallener Benutzer]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Feedback nach dem Kauf]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Robuste Kanäle

#### LINE

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Die LINE-Integration von Braze ist jetzt allgemein verfügbar! LINE ist mit über 95 Millionen monatlich aktiven Nutzern die beliebteste Messaging-App in Japan. Zusätzlich zum Messaging bietet LINE seinen Nutzern eine "All-in-One"-Plattform für soziale Medien, Spiele, Shopping und Zahlungen.

Um loszulegen, lesen Sie unsere [LINE-Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### LinkedIn Audience Sync

{% multi_lang_include release_type.md release="Beta" %}

Sie können LinkedIn jetzt mit [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/) nutzen, einem Tool, mit dem Sie die Reichweite Ihrer Kampagnen auf viele der wichtigsten sozialen und Werbetechnologien ausweiten können. Um an der Beta teilzunehmen, wenden Sie sich an Ihren Braze Success Manager.
 
### Verbesserung des Entwicklerhandbuchs
 
Wir sind dabei, das [Braze-Entwicklerhandbuch]({{site.baseurl}}/developer_guide/home/) umfassend zu verbessern. In einem ersten Schritt haben wir die Navigation vereinfacht und die Anzahl der verschachtelten Abschnitte reduziert. 

|Vor|Nach|
|------|-----|
|!["Die alte Navigation für das Braze Entwicklerhandbuch."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["Die neue Navigation für den Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Neue Lötpartnerschaften
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), eine weltweit führende Postkarten-App, ermöglicht Ihnen die einfache Durchführung von Direktmailing-Kampagnen und bietet eine nahtlose und profitable Möglichkeit, mit Ihren Kunden in Kontakt zu treten. Die ersten Schritte finden Sie unter [Integration von MyPostcard mit Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### SDK Aktualisierungen
 
Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Diese Version erfordert 13.1.0 des Braze React Native SDK.
    - Ersetzt den iOS BrazeAppDelegate Methodenaufruf von BrazeReactUtils.populateInitialUrl durch BrazeReactUtils.populateInitialPayload.
        - Dieses Update behebt ein Problem, bei dem Push-Öffnungsereignisse nicht ausgelöst werden, wenn Sie auf eine Benachrichtigung klicken, während sich die Anwendung in einem beendeten Zustand befindet.
        - Um dieses Update voll auszunutzen, ersetzen Sie alle Aufrufe von Braze.getInitialURL durch Braze.getInitialPushPayload in Ihrem JavaScript-Code. Auf die ursprüngliche URL kann nun über die Eigenschaft url der ursprünglichen Push-Nutzlast zugegriffen werden.
- [Braze Segment Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Aktualisiert die Braze Swift SDK Bindungen, so dass sie Versionen ab der 11.1.1+ SemVer Bezeichnung erfordern.
    - Dies ermöglicht die Kompatibilität mit jeder Version des Braze SDK von 11.1.1 bis zu 12.0.0, aber nicht einschließlich.
    - Im Changelog-Eintrag für 11.1.1 finden Sie weitere Informationen zu möglichen Änderungen.

## Veröffentlichung am 15\. Oktober 2024

### Flexibilität der Daten

#### Kampagnen und Canvase

Bei der Erstellung von Kampagnen und Canvases können Sie die genaue Anzahl der erreichbaren Nutzer in Ihrer Zielgruppe anstelle der standardmäßigen Schätzung berechnen, indem Sie die Option [Exakte Statistik berechnen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size) wählen.

#### API Android-Objekte

Der [Parameter`android_priority` ]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) akzeptiert die Werte "normal" oder "hoch", um die Priorität des FCM-Senders festzulegen. Standardmäßig werden Benachrichtigungen mit hoher Priorität und Datennachrichten mit normaler Priorität gesendet.

Weitere Informationen darüber, wie sich unterschiedliche Werte auf die Zustellung auswirken, finden Sie unter [Android Nachrichtenpriorität](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Verwenden Sie [den integrierten Debugger des Braze SDK]({{site.baseurl}}/developer_guide/platform_wide/debugging/), um Probleme bei Ihren SDK-gesteuerten Channels zu beheben, ohne dass Sie die ausführliche Protokollierung in Ihrer Anwendung aktivieren müssen.

#### Live-Aktivitäten

Wir haben die [häufig gestellten Fragen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) zu Swift Live Activities mit einigen neuen Fragen und Antworten aktualisiert.

#### Angepasste Events

[Ereignis-Eigenschaftsobjekte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties), die Array- oder Objektwerte enthalten, können jetzt eine Ereignis-Eigenschaftsnutzlast von bis zu 100 KB haben.

#### Zufällige Eimernummern

Nutzen Sie die [zufällige Wiedereingabe von Zielgruppen mit zufälligen Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) für A/B-Tests oder die gezielte Ansprache bestimmter Nutzergruppen in Ihren Kampagnen.

#### Segment-Erweiterungen

Sie können [die Segmenterweiterungen nach einem wiederkehrenden Zeitplan aktualisieren]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh), indem Sie die Häufigkeit der Aktualisierung (täglich, wöchentlich oder monatlich) und die genaue Uhrzeit der Aktualisierung auswählen.

### Robuste Kanäle

#### SMS

Wir haben [UTM-Parameter]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) hinzugefügt, um Ihnen zu zeigen, wie Sie UTM-Parameter in einer SMS-Nachricht verwenden können, damit Sie die Leistung von Kampagnen in Analysetools von Drittanbietern, wie Google Analytics, verfolgen können.

#### Landing Pages

[Verbinden Sie Ihre eigene Domain]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/) mit Ihrem Braze-Arbeitsbereich, um die URLs Ihrer Landing Pages an Ihre Marke anzupassen.

#### LINE und Hartlöten

{% multi_lang_include release_type.md release="Beta" %}

Wir haben eine neue Dokumentation hinzugefügt:

- [LINE-Nachrichtentypen]({{site.baseurl}}/line/create/message_types/) behandelt die LINE-Nachrichtentypen, die Sie verfassen können, einschließlich der Aspekte und Einschränkungen, und ist Teil der LINE-Betasammlung.
- [Die Verknüpfung von Benutzerkonten]({{site.baseurl}}/line/line_setup/#user-account-linking) ermöglicht es Benutzern, ihr LINE-Konto mit dem Benutzerkonto Ihrer App zu verknüpfen. Sie können dann Liquid in Braze verwenden, z. B. {% raw %}`{{line_id}}`{% endraw %}, um eine personalisierte URL für den Benutzer zu erstellen, die die LINE-ID des Benutzers an Ihre Website oder App weiterleitet, die dann mit einem bekannten Benutzer verknüpft werden kann.

#### WhatsApp und Braze

[WhatsApp Business Accounts (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) können jetzt mit mehreren Business Solution Providern geteilt werden.

### Neue Lötpartnerschaften

#### Zukunftshymne - Dynamischer Inhalt

Die Partnerschaft zwischen Braze und [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) nutzt Amplifier AI, um die Personalisierung von Inhalten, Echtzeit-Erlebnisse und dynamische Zielgruppen zu ermöglichen. Amplifier AI funktioniert in allen Sportarten, Casinos und Lotterien und ermöglicht es Ihnen, Braze-Spielerprofile mit branchenspezifischen Spielerattributen zu erweitern, wie z.B. Lieblingsspiel, Engagement-Score, erwarteter nächster Einsatz und mehr.

### Einstellungen

#### Verschlüsselung auf Indentifier-Feld-Ebene

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Mit der [Verschlüsselung auf Identifizierungsfeldebene]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/) können Sie E-Mail-Adressen nahtlos mit AWS Key Management Service (KMS) verschlüsseln, um die in Braze freigegebenen personenbezogenen Daten zu minimieren. Bei der Verschlüsselung werden sensible Daten durch Chiffretext ersetzt, d.h. durch unlesbare verschlüsselte Informationen.

### SDK Aktualisierungen

Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Unterstützung für die [strikte Gleichzeitigkeitsprüfung in Swift 6](https://developer.apple.com/documentation/swift/adoptingswift6) hinzugefügt
        - Relevante öffentliche Braze-Klassen und -Datentypen entsprechen jetzt dem `Sendable` -Protokoll und können sicher in verschiedenen Gleichzeitigkeitskontexten verwendet werden.
        - Main-Thread-Only-APIs sind jetzt mit dem Attribut `@MainActor` gekennzeichnet.
        - Wir empfehlen die Verwendung von Xcode 16.0 oder höher, um die Vorteile dieser Funktionen zu nutzen und gleichzeitig die Anzahl der vom Compiler generierten Warnungen zu minimieren. Frühere Versionen von Xcode können weiterhin verwendet werden, aber einige Funktionen können Warnungen erzeugen.
    - Wenn Sie die Unterstützung für Push-Benachrichtigungen manuell integrieren, müssen Sie möglicherweise die `UNUserNotificationCenterDelegate` Konformität aktualisieren, um das `@preconcurrency` Attribut zu verwenden, um Warnungen zu vermeiden.
        - Die Anwendung des Attributs `@preconcurrency` auf die Protokollkonformität ist nur in Xcode 16.0 oder höher verfügbar. [Hier](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual) finden Sie unseren Beispiel-Integrationscode.
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Aktualisiert die Bindungen der nativen Android-Version von [Braze Android SDK 31.1.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Aktualisiert die Bindungen der nativen iOS-Version von [Braze Swift SDK 10.3.0 auf 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Kotlin von 1.8 auf Kotlin 2.0 aktualisiert.
- [Web SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## Veröffentlichung am 17\. September 2024

### Flexibilität der Daten

#### Braze Cloud Data Ingestion für S3

Sie können [Cloud Data Ingestion (CDI) für S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) verwenden, um einen oder mehrere S3-Buckets in Ihrem AWS-Konto direkt mit Braze zu integrieren. Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an SQS gesendet, und Braze Cloud Data Ingestion nimmt diese neuen Dateien auf.

#### Monatlich aktive Nutzer CY 24-25

Für Kunden, die Monthly Active Users - CY 24-25 erworben haben, verwaltet Braze auf seinem Endpunkt `/users/track` verschiedene Tarifgrenzen. Einzelheiten finden Sie unter [POST: Benutzer verfolgen]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Kreativität entfesseln

#### Vorlage von Katalogartikeln einschließlich Liquid

{% multi_lang_include release_type.md release="Früher Zugang" %}

Verwenden Sie das Flag `:rerender` in einem Liquid-Tag, um [den Liquid-Inhalt eines Katalogartikels darzustellen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Wenn Sie zum Beispiel den folgenden Liquid-Inhalt wiedergeben:

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

#### WhatsApp Antwortnachrichten

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können [Antwortnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) verwenden, um auf eingehende WhatsApp-Nachrichten Ihrer Benutzer zu antworten. Diese Nachrichten werden auf Braze während Ihrer Kompositionserfahrung in-app erstellt und können jederzeit bearbeitet werden. Sie können Liquid verwenden, um die Sprache der Antwortnachrichten an die entsprechenden Benutzer anzupassen.

#### Canvas-Templates

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Erstellen Sie [Canvas-Vorlagen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/), um Ihre Botschaften zu verfeinern, indem Sie einen konsistenten Rahmen schaffen, der leicht an Ihre spezifischen Ziele in Ihren Canvases angepasst werden kann.

#### Landing Pages

{% multi_lang_include release_type.md release="Beta" %}

[Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) von Braze sind eigenständige Webseiten, die Ihre Strategie zur Benutzergewinnung und -bindung vorantreiben können.

#### Änderungen seit der letzten Ansicht

Sie können die Anzahl der Aktualisierungen Ihrer [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), Kampagnen und [Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) durch andere Mitglieder Ihres Teams einsehen, indem Sie die Metrik *Änderungen seit letzter Ansicht* auf den jeweiligen Übersichtsseiten (z. B. der Übersichtsseite für eine [E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)) betrachten. 

#### Fehlerbehebung bei Webhook- und Connected Content-Anfragen 

[In diesem Artikel]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) erfahren Sie, wie Sie Fehlercodes für Webhooks und Connected Content beheben können. Sie erfahren, um welche Fehler es sich handelt und wie Sie diese beheben können.

### Neue Lötpartnerschaften

#### Posteingangsmonster - Analytik

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) ist eine Plattform für Posteingangssignale, die Unternehmensmarken dabei hilft, jede Sendung zu erhalten. Es handelt sich um eine integrierte Suite von Lösungen für Zustellbarkeit, kreative Gestaltung und SMS-Überwachung, die moderne Customer Relationship Management (CRM)-Teams unterstützt und die Angst vor dem Versand beendet.

#### SessionM - Loyalität

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) ist eine Plattform für Kundenbindung und -loyalität, die Funktionen für das Kampagnenmanagement und Lösungen für das Loyalitätsmanagement bietet, um Marketingfachleuten dabei zu helfen, gezielte Kontakte zu knüpfen, um das Engagement und die Rentabilität zu steigern.

### KI und ML Automatisierung

#### Empfehlungen zu aktuellen Artikeln

Neben dem "AI Personalized"-Modell umfasst die Funktion [für KI-Artikel-Empfehlungen]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) auch ein Empfehlungsmodell für "Trending", das Artikel enthält, die bei den jüngsten Nutzerinteraktionen die größte positive Resonanz hatten.

### Einstellungen

#### Rollen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

[Rollen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) sorgen für mehr Struktur, indem sie Ihre individuellen Berechtigungen mit den Zugriffskontrollen für den Arbeitsbereich zusammenfassen. Dies ist besonders nützlich, wenn Sie viele Marken oder regionale Arbeitsbereiche in einem Dashboard haben. Mit Rollen können Sie Dashboard-Benutzer zu den richtigen Arbeitsbereichen hinzufügen und ihnen direkt die entsprechenden Berechtigungen erteilen. 

#### Bericht über Sicherheitsereignisse

Wir haben eine vollständige Liste der [Sicherheitsereignisse]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) hinzugefügt, die in Ihrem heruntergeladenen Sicherheitsbericht erscheinen können.

#### Bericht über die Nutzung von Nachrichten

{% multi_lang_include release_type.md release="Früher Zugang" %}

Das [Nachrichtennutzungs-Dashboard]({{site.baseurl}}/message_usage/) bietet Ihnen einen Self-Service-Einblick in die Nutzung Ihres SMS- und WhatsApp-Guthabens und gibt Ihnen einen umfassenden Überblick über die historische und aktuelle Nutzung im Vergleich zu den vertraglich festgelegten Kontingenten. Diese Erkenntnisse können Ihre Verwirrung verringern und Ihnen helfen, Anpassungen vorzunehmen, um Überschussrisiken zu vermeiden.

### SDK

#### Verzögerte Initialisierung für das Braze Swift SDK

Richten Sie eine [verzögerte Initialisierung]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) ein, um Ihr Braze Swift SDK asynchron zu initialisieren und gleichzeitig sicherzustellen, dass die Handhabung von Push-Benachrichtigungen erhalten bleibt. Dies kann nützlich sein, wenn Sie vor der Initialisierung des SDK andere Dienste einrichten müssen, z. B. Konfigurationsdaten von einem Server abrufen oder auf die Zustimmung des Benutzers warten.

### SDK Aktualisierungen

Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segment Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Diese Version erfordert jetzt Cordova Android 13.0.0.
    - Eine vollständige Liste der Anforderungen an die Projektabhängigkeit finden Sie in der [Cordova Release-Ankündigung](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html). - Die native Android-Bridge wurde [von Braze Android SDK 30.3.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Die native iOS-Bridge wurde [von Braze Swift SDK 9.2.0 auf 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Die native Android-Bridge wurde [von Braze Android SDK 30.3.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Die native iOS-Bridge wurde [von Braze Swift SDK 9.0.0 auf 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
- [Braze Segment Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Aktualisiert die Bindungen des Braze Swift SDK, um Versionen der `10.2.0+` SemVer Bezeichnung zu erfordern.
        - Dies ermöglicht die Kompatibilität mit jeder Version des Braze SDK von `10.2.0` bis hin zu, aber nicht einschließlich, `11.0.0`.
        - Lesen Sie den Changelog-Eintrag für [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) für weitere Informationen über mögliche Änderungen.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Aktualisiert die native Android-Bridge [von Braze Android SDK 30.4.0 auf 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Ändert das Verhalten von `wipeData()` auf Android, um externe Abonnements (wie `subscribeToContentCards()`) nach dem Aufruf beizubehalten.
    - Aktualisiert die native iOS-Bridge [von Braze Swift SDK 9.0.0 auf 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## Veröffentlichung am 20\. August 2024

### Neue Anwendungsfälle

#### Kataloge

Sie können jede Art von Daten in einen Katalog einbringen. In der Regel handelt es sich bei den Daten um Metadaten über Angebote wie Produkte, Rabatte, Werbeaktionen, Veranstaltungen und ähnliches. Lesen Sie unsere [Anwendungsfälle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) und erfahren Sie, wie Sie diese Daten nutzen können, um Nutzer mit hochrelevanten Nachrichten anzusprechen.

#### Intelligence Suite

Die Intelligence Suite bietet leistungsstarke Funktionen zur Analyse des Nutzerverlaufs und der Kampagnen- und Canvas-Performance und nimmt dann automatische Anpassungen vor, um Engagement, Zuschauerzahlen und Konversionen zu steigern. Einige Beispiele dafür, wie diese Funktionen verschiedenen Branchen zugute kommen können, finden Sie in unseren [Anwendungsfällen]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Update für das Dashboard zu Hause

Sie können im Braze-Dashboard [dort weitermachen, wo Sie aufgehört haben,]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) und haben einfachen Zugriff auf die Dateien, die Sie kürzlich bearbeitet oder erstellt haben. Dieser Bereich erscheint oben auf der **Startseite** des Braze Dashboards.

### Flexibilität der Daten

#### Datenumwandlungsvorlagen und neues Ziel

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Erstellen Sie Ihre Datenumwandlung mit unserer speziellen [Vorlagenbibliothek]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation), um Ihnen den Einstieg in bestimmte externe Plattformen zu erleichtern, statt mit Standardcode. Sie können nun **POST auswählen: Senden Sie Nachrichten sofort über API Nur** als Ihr Ziel, um Webhooks von einer Quellplattform umzuwandeln und sofortige Nachrichten an Ihre Benutzer zu senden.

#### Benutzer in Massen zusammenführen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Wenn Sie auf doppelte Benutzerprofile stoßen, können Sie diese Benutzer [zusammenführen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging), um Ihre Daten zu rationalisieren.

#### Benutzerdefinierte Attribute exportieren

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können [die Liste der benutzerdefinierten Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) als CSV-Datei [exportieren]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data), indem Sie auf der Seite **Benutzerdefinierte Attribute** die Option **Alle exportieren** wählen. Die CSV-Datei wird generiert, und Sie erhalten einen Download-Link per E-Mail.

#### Aktuelle IP-Zulassungsliste

Braze sendet Currents-Daten von den aufgelisteten IPs, die automatisch und dynamisch zu allen API-Schlüsseln hinzugefügt werden, die für das [Zulassen der Auflistung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents) optiert wurden.

### Robuste Kanäle

#### Neue Segmenterstellung Erfahrung

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Erstellen Sie ein Segment mit unserer [aktuellen Erfahrung]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Die Segmente werden in Echtzeit aktualisiert, wenn sich die Daten ändern, und Sie können so viele Segmente erstellen, wie Sie für Ihre Zielgruppenansprache und Ihr Messaging benötigen.

#### Metriken nach Segmenten

Verwenden Sie die Berichtsvorlagen [des Query Builders]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/), um Leistungskennzahlen für Kampagnen, Canvas, Varianten und Schritte nach Segmenten aufzuschlüsseln.

#### Akquisition von Telefonnummern

Um den WhatsApp-Nachrichtenkanal nutzen zu können, benötigen Sie eine Telefonnummer, die den Anforderungen von WhatsApp für die [Cloud-API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) oder die [On-Premises-API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) entspricht. 

Sie müssen Ihre Telefonnummer selbst beschaffen, da Braze die Nummer nicht für Sie bereitstellt. Sie können entweder ein physisches Telefon mit einer SIM-Karte über Ihren geschäftlichen Telefonanbieter erwerben oder einen unserer Partner nutzen: Twilio oder Infoblip. **Sie müssen über ein eigenes Twilio- oder Infobip-Konto verfügen, da dies nicht über Braze möglich ist.**

### Neue Lötpartnerschaften

#### Zendesk Chat - Sofortiger Chat

Die Integration von Braze und [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) verwendet Webhooks von jeder Plattform, um eine zweiseitige SMS-Konversation einzurichten. Wenn ein Benutzer Support anfordert, wird ein Ticket in Zendesk erstellt. Die Antworten der Agenten werden über eine durch die API ausgelöste SMS-Kampagne an Braze weitergeleitet, und die Antworten der Benutzer werden an Zendesk zurückgesendet.

### SDK Aktualisierungen

Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Die folgenden Änderungen wurden beim Abonnieren von Push-Ereignissen mit [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - Die Schließung von `update` wird nun standardmäßig durch die Ereignisse "Push geöffnet" und "Push empfangen" ausgelöst. Zuvor wurde sie nur durch "Push Opened"-Ereignisse ausgelöst.
            - Um weiterhin nur "Push Opened"-Ereignisse zu abonnieren, geben Sie `[.opened]` für den Parameter `payloadTypes` ein. Alternativ können Sie Ihre `update` Schließung implementieren, um zu überprüfen, ob `type` aus `Braze.Notifications.Payload` `.opened` ist.
        - Wenn Sie eine Push-Benachrichtigung mit `content-available: true` empfangen, wird die [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) nun `.received` anstelle von `.opened` sein.
    - Markiert die folgenden veralteten APIs als nicht mehr verfügbar:
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - Entfernt die veralteten APIs:
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - Entfernt die veraltete Klasse `BrazeLocation` zu Gunsten von `BrazeLocationProvider`.
- [Xamarin SDK Version 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Unterstützung für .NET 8.0 für die iOS- und Android-Bindings wurde hinzugefügt, da .NET 7.0 das Ende der Unterstützung erreicht hat.
        - Dadurch wird die Unterstützung für .NET 7.0 entfernt.
    - Die Android-Bindung wurde von [Braze Android 30.4.0 auf 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Die iOS-Bindung wurde von [Braze Swift SDK 9.0.0 auf 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
        - Beim Abonnieren von Push-Benachrichtigungsereignissen wird das Abonnement auf iOS sowohl für "Push empfangen" als auch für "Push geöffnet" ausgelöst, statt nur für "Push geöffnet".
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Aktualisiert die Bindungen der nativen iOS-Version von [Braze Swift SDK 9.0.0 auf 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Beim Abonnieren von Push-Benachrichtigungsereignissen wird das Abonnement auf iOS sowohl für `push_received` als auch für `push_opened` ausgelöst, anstatt nur für `push_opened` Ereignisse.

## Veröffentlichung am 23\. Juli 2024

### Braze Docs Aktualisierungen

#### Diátaxis und Braze Docs

Wir sind dabei, unsere Dokumentation mithilfe eines Frameworks namens [Diátaxis](https://diataxis.fr/) zu standardisieren. Um unseren Redakteuren und Autoren bei der Erstellung von Inhalten zu helfen, die in diesen neuen Rahmen passen, haben wir [Vorlagen für jeden Inhaltstyp]({{site.baseurl}}/contributing/content_types) erstellt.

#### Neue Pull-Request-Vorlage für Braze Docs

Wir haben uns die Zeit genommen, unsere Vorlage für Pull-Requests (PR) zu verbessern, damit es einfacher und weniger verwirrend ist, [zu Braze Docs beizutragen]({{site.baseurl}}/contributing/home/). Wenn Sie immer noch der Meinung sind, dass es Raum für Verbesserungen gibt, öffnen Sie einen PR oder [reichen Sie ein Problem ein](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). Was auch immer einfacher ist!
 
### Flexibilität der Daten

#### Exportieren Sie benutzerdefinierte Ereignisse und Attribute

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt benutzerdefinierte Ereignisse und benutzerdefinierte Attribute exportieren, indem Sie die [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) und [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) Endpunkte exportieren.

#### Neue Currents-Berechtigungen für Benutzer

Es gibt zwei neue Berechtigungseinstellungen für Benutzer: **Currents-Integrationen ansehen** und **Currents-Integrationen bearbeiten**. Erfahren Sie mehr über [Benutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions). 

#### Aktualisierung der Snowflake-Richtlinie zur Datenspeicherung
 
Ab dem 27\. August 2024 werden personenbezogene Daten (PII) aus allen Snowflake Secure Data Sharing-Ereignissen, die älter als zwei Jahre sind, entfernt. Wenn Sie Snowflake verwenden, können Sie die vollständigen Ereignisdaten in Ihrer Umgebung aufbewahren, indem Sie eine Kopie in Ihrem Snowflake-Konto speichern, bevor die Aufbewahrungsrichtlinie angewendet wird. Erfahren Sie mehr über die [Datenspeicherung in Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/).
 
### Kreativität entfesseln

#### Mehrseitige In-App-Nachrichten

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Durch das Hinzufügen von Seiten zu Ihrer In-App-Nachricht können Sie die Benutzer durch einen sequentiellen Ablauf führen, z. B. einen Onboarding-Flow oder eine Willkommensreise. Weitere Informationen finden Sie unter [Erstellen einer In-App-Nachricht per Drag-and-Drop]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page).

#### Linkverkürzung mit Liquid

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Verwenden Sie [Liquid zur Personalisierung von URLs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening), um die in SMS-Nachrichten enthaltenen URLs automatisch zu verkürzen und die Klickraten zu analysieren. Um es auszuprobieren, siehe [Link shortening]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).

#### API-Beispiele für Kataloge

Wir haben Beispiele für den Endpunkt `/catalogs` mit Array-Feldern hinzugefügt. Um die Beispiele zu sehen, schauen Sie sich das Folgende an:

- [Mehrere Katalogartikel bearbeiten]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [Mehrere Katalogartikel erstellen]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [Katalogartikel aktualisieren]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [Katalogartikel bearbeiten]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [Katalogartikel erstellen]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [Katalogartikel aktualisieren]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [Katalog erstellen]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### Robuste Kanäle

### Mehrere WhatsApp Business-Konten

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt mehrere WhatsApp Business-Konten und Abonnementgruppen (und Telefonnummern) zu jedem Arbeitsbereich hinzufügen. Details finden Sie unter [Mehrere WhatsApp Business-Konten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups). 

#### SMS Geografische Berechtigungen

Die geografischen SMS-Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem SMS-Verkehr, indem sie die Länder kontrollieren, in die Sie SMS-Nachrichten senden können. Wie Sie eine Liste der zulässigen Länder festlegen, damit Sie sicherstellen können, dass SMS-Nachrichten nur an zugelassene Regionen gesendet werden, erfahren Sie unter [Konfigurieren Ihrer SMS-Länderzulassungsliste]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist).

#### LINE und Hartlöten

{% multi_lang_include release_type.md release="Beta" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) ist mit über 95 Millionen monatlich aktiven Nutzern die beliebteste Messaging-App in Japan. Sie können Ihre LINE-Konten mit Braze integrieren, um Ihre Zero- und First-Party-Kundendaten zu nutzen, um ansprechende LINE-Nachrichten an die richtigen Kunden zu senden, die auf deren Vorlieben, Verhalten und kanalübergreifenden Interaktionen basieren. Um loszulegen, siehe [LINE]({{site.baseurl}}/line).

#### Shopify: Preisreduzierungen und Wiederauffüllung der Lagerbestände

{% multi_lang_include release_type.md release="Früher Zugang" %}

Mit Shopify können Sie jetzt benutzerdefinierte Benachrichtigungen für [Preissenkungen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) und [nicht vorrätige Artikel]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications) erstellen.
 
### KI und ML Automatisierung
 
#### Regelbasierte Zusammenführung für doppelte Benutzer

Bisher konnten Sie in Braze doppelte Benutzer einzeln oder in großen Mengen finden und zusammenführen. Jetzt können Sie Regeln erstellen, um zu steuern, wie Duplikate aufgelöst werden, damit der relevanteste Benutzer beibehalten wird. Mehr dazu erfahren Sie unter [Regelbasierte Zusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

#### KI Flüssiger Assistent

{% multi_lang_include release_type.md release="Beta" %}

Der AI Liquid Assistant ist ein Chat-Assistent auf der Basis von <sup>BrazeAITM</sup>, der Ihnen hilft, das Liquid zu generieren, das Sie zur Personalisierung von Nachrichteninhalten benötigen. Sie können Liquid aus Vorlagen generieren, personalisierte Liquid-Vorschläge erhalten und bestehendes Liquid mit der Unterstützung von <sup>BrazeAITM</sup> optimieren. Der KI-Liquid-Assistent liefert auch Kommentare, die das verwendete Liquid erklären, so dass Sie Ihr Verständnis von Liquid verbessern und lernen können, Ihr eigenes zu schreiben.

Um loszulegen, siehe [AI Liquid Assistent]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid).
 
### SDK
 
#### Android SDK-Protokolle

Wir haben die [Logging-Dokumente für das Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging) überarbeitet, damit sie leichter zu lesen und in Ihrer App zu verwenden sind. Wir haben auch Beschreibungen für jede Protokollstufe hinzugefügt.

#### iOS SDK Push-Benachrichtigungen für den Vordergrund

Die Methode `subscribeToUpdates` im Braze iOS SDK kann jetzt erkennen, ob eine Push-Benachrichtigung im Vordergrund empfangen wurde. Weitere Informationen finden Sie unter [Integration von iOS-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration).
 
#### Aktualisierung der Xamarin-Dokumente
 
Seit [Version 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0) verwendet das Braze Xamarin SDK die Swift SDK-Bindung, daher haben wir die Codeschnipsel und das Referenzmaterial aktualisiert. Außerdem haben wir den Abschnitt umstrukturiert, damit er leichter zu lesen und zu verstehen ist. Um dies zu überprüfen, sehen Sie sich [die Xamarin-Dokumente]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup) an.

#### SDK Aktualisierungen

Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.
 
- [Swift SDK 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [Web SDK 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - Ein in 5.2.0 eingeführter Fehler wurde behoben, der dazu führen konnte, dass HTML-In-App-Nachrichten nicht korrekt dargestellt wurden, wenn ein externes Skript synchron geladen wurde.
- [Web SDK 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## Veröffentlichung am 25\. Juni 2024

### Japanische Dokumente

Wir unterstützen jetzt die japanische Sprache für Braze Docs!

![Die Braze Docs Seite zeigt die japanische Benutzeroberfläche]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### Flexibilität der Daten

#### Anhänge für API-ausgelöste Kampagnen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Der [Endpunkt`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) unterstützt jetzt Anhänge (so wie der Endpunkt `/messages/send` Anhänge für E-Mails unterstützt). 

#### Zusätzliche Data Warehouse-Unterstützung

{% multi_lang_include release_type.md release="Früher Zugang" %}

Braze [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources) unterstützt jetzt BigQuery, Databricks, Redshift und Snowflake.

#### WhatsApp Telefonnummern Migration

Migrieren Sie Ihre WhatsApp-Telefonnummer zwischen WhatsApp Business-Konten, indem Sie Meta's Embedded Signup verwenden. Lesen Sie mehr über die [Migration von WhatsApp-Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration).
 
### Kreativität entfesseln

#### Engagement nach Gerät

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Der neue Bericht **Engagement nach Gerät** bietet eine Aufschlüsselung der Geräte, mit denen Ihre Nutzer auf Ihre E-Mails zugreifen. Diese Daten verfolgen das E-Mail-Engagement über Mobil-, Desktop-, Tablet- und andere Gerätetypen. Erfahren Sie mehr über [den Bericht und das E-Mail Performance Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard).

#### WhatsApp und SMS Flüssige Eigenschaften im Canvas-Fluss

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Wir haben Unterstützung für [WhatsApp und SMS Liquid Eigenschaften im Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) hinzugefügt. Wenn ein Aktionspfad-Schritt einen Auslöser "Eingehende SMS-Nachricht gesendet" oder "Eingehende WhatsApp-Nachricht gesendet" enthält, können die nachfolgenden Canvas-Schritte jetzt eine SMS- oder WhatsApp Liquid-Eigenschaft enthalten. Dies spiegelt wider, wie die Ereigniseigenschaften in Canvas Flow funktionieren. Auf diese Weise können Sie Ihre Nachrichten nutzen, um First-Party-Daten zu Nutzerprofilen und Conversational Messaging zu speichern und zu referenzieren.
 
#### Personalisierte Pfade in wiederkehrenden Leinwänden

{% multi_lang_include release_type.md release="Früher Zugang" %}

Mit personalisierten Pfaden in Canvases können Sie jeden Punkt einer Canvas-Reise für einzelne Benutzer auf der Grundlage der Konversionswahrscheinlichkeit personalisieren. Jetzt sind personalisierte Pfade für wiederkehrende Leinwände verfügbar. Erfahren Sie mehr über [Personalisierte Varianten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths).

#### Segmente Fehlerbehebung

Arbeiten Sie mit Segmenten? Im Folgenden finden Sie einige [Schritte zur Fehlerbehebung und Überlegungen]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting), die Sie beachten sollten.

#### Flüssiges Hervorheben

Wir haben die [Farbkodierung von Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) verbessert, um die Richtlinien für Barrierefreiheit besser zu unterstützen.

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### Robuste Kanäle

#### Geografische Berechtigungen für SMS

{% multi_lang_include release_type.md release="Früher Zugang" %}

Geografische SMS-Berechtigungen erhöhen die Sicherheit und schützen vor betrügerischem SMS-Verkehr, indem sie die Länder kontrollieren, in die Sie SMS-Nachrichten senden können. Administratoren können jetzt eine Liste der zulässigen Länder festlegen, um sicherzustellen, dass SMS-Nachrichten nur an zugelassene Regionen gesendet werden. Weitere Informationen finden Sie unter [SMS-Geografische Berechtigungen]({{site.baseurl}}/sms_geographic_permissions). 

![Das Dropdown-Menü "Länderliste", wobei die gängigsten Länder oben angezeigt werden.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### Bewährte Verfahren für SMS/MMS

Erfahren Sie mehr über die [besten Praktiken für SMS/MMS mit Braze]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices), einschließlich unserer Empfehlungen für Opt-Out-Überwachung und Traffic-Pumping. 

#### Verfolgung von Push-Abbestellungen

In unserem neuen [Hilfeartikel]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) finden Sie einige Tipps zum Verfolgen von Push-Abmeldungen.

#### Shopify `checkout.liquid` Verwerfung

Bitte beachten Sie, dass die Unterstützung für Shopify `checkout.liquid` im August 2024 abläuft und im August 2025 endet. Lesen Sie mehr darüber, wie Braze [diesen Übergang bewältigen]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout) wird. 

### SDK Aktualisierungen
 
Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - Veraltet die bestehenden Feature Flag APIs, die in einer zukünftigen Version entfernt werden sollen:
        - `Braze.FeatureFlag.jsonStringProperty(key:)` wurde veraltet.
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` wurde zu Gunsten von `Braze.FeatureFlag.jsonProperty(key:)` veraltet.
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo Plugin 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOS Dokumentation

Vor ein paar Monaten wurden die Artikel für [tvOS Content Cards]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) und [In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos) versehentlich veraltet. Diese Dokumente wurden jetzt unter dem Abschnitt Swift in Braze Docs neu veröffentlicht.

{% alert note %}
[Autoren, die]({{site.baseurl}}/contributing/home) zu Braze Docs [beitragen]({{site.baseurl}}/contributing/home), sollten beachten, dass die Website jetzt mit Ruby 3.3.0 läuft. Bitte aktualisieren Sie bei Bedarf Ihre Ruby-Version.
{% endalert %}

## Veröffentlichung am 28\. Mai 2024

### Visuelle Aktualisierungen der Dokumentationsseite

Vielleicht haben Sie schon bemerkt, dass unsere Dokumentations-Website ein schickes neues Aussehen hat! Wir haben sie überarbeitet, um die neue, lebendige Markenidentität von Braze widerzuspiegeln. Wenn Sie einen Blick hinter die Kulissen unserer neuen Marke werfen möchten, lesen Sie mehr unter [Unveiling Our New Brand: Ein Gespräch mit Greg Erdelyi, Executive Creative Director von Braze](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### Unterstützung für Portugiesisch und Spanisch

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Braze ist jetzt sowohl auf Portugiesisch als auch auf Spanisch verfügbar. Wie Sie die Sprache ändern, in der das Braze-Dashboard angezeigt wird, erfahren Sie unter [Spracheinstellungen]({{site.baseurl}}/user_guide/administrative/access_braze/language/).

### Robuste Kanäle

#### Mehrsprachige Einstellungen

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Wenn Sie die [Einstellungen für die Mehrsprachigkeit]({{site.baseurl}}/multi_language_support/) anpassen, können Sie Nutzer in verschiedenen Sprachen und an verschiedenen Orten mit unterschiedlichen Nachrichten in einer einzigen E-Mail-Nachricht ansprechen. Um die Mehrsprachenunterstützung zu bearbeiten und zu verwalten, müssen Sie über die Benutzerberechtigung "Mehrsprachige Einstellungen verwalten" verfügen. Um das Gebietsschema zu einer Nachricht hinzuzufügen, benötigen Sie die Berechtigung zum Bearbeiten von Kampagnen.

#### Kopfzeile für das Abbestellen der Liste auf Nachrichtenebene mit einem Klick

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Die Ein-Klick-Abmeldung für den list-unsubscribe-Header[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) bietet den Empfängern eine einfache Möglichkeit, sich von E-Mails abzumelden. Sie können diese Kopfzeileneinstellung so anpassen, dass sie auf Nachrichtenebene in Ihren E-Mails angewendet wird. Weitere Informationen zu dieser Einstellung finden Sie unter [Kopfzeile für die Abmeldung von E-Mails in Arbeitsbereichen]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces).

#### Über E-Mail-Säuberung

In unserem neuen Artikel zur [Bereinigung]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) erfahren Sie mehr über den Prozess, der abläuft, wenn Braze eine bestimmte Art von JavaScript in Ihrer E-Mail-Nachricht erkennt. Sein Hauptzweck besteht darin, böswillige Akteure daran zu hindern, auf die Sitzungsdaten anderer Braze Dashboard-Benutzer zuzugreifen.

#### Anzahl der Einschlüsse für Inhaltsblöcke

Nachdem Sie einen Inhaltsblock in einer aktiven Kampagne oder einem Canvas hinzugefügt haben, können Sie [eine Vorschau dieses Inhaltsblocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) in der Inhaltsblock-Bibliothek anzeigen, indem Sie den Mauszeiger über den Inhaltsblock bewegen und das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** auswählen.

#### Canvas-Status

Auf dem Braze-Dashboard sind Ihre Canvases nach ihrem Status gruppiert. Sehen Sie sich die verschiedenen [Canvas-Status und Beschreibungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) an, um zu erfahren, was sie bedeuten.

### KI und ML Automatisierung

#### Markenrichtlinien für KI-Texterassistenten

{% multi_lang_include release_type.md release="Allgemeine Verfügbarkeit" %}

Sie können jetzt [Markenrichtlinien]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) erstellen und anwenden, um den Stil der vom KI-Texterstellungsassistenten generierten Texte an die Stimme Ihrer Marke anzupassen. Richten Sie mehrere Richtlinien für verschiedene Szenarien ein, um sicherzustellen, dass Ihr Ton immer zum jeweiligen Kontext passt.
 
### Neue Lötpartnerschaften

#### Adikteev - Analytik

Die Integration von Braze und [Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) ermöglicht es Ihnen, die Benutzerbindung zu erhöhen, indem Sie die Technologie von Adikteev zur Vorhersage der Abwanderung innerhalb von Braze CRM-Kampagnen nutzen, um Benutzersegmente mit hohem Risiko prioritär anzusprechen.
 
#### Celebrus - Analytik
 
Die Integration von Braze und [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) lässt sich nahtlos mit dem Braze SDK über Web- und mobile App-Kanäle hinweg integrieren und erleichtert die Belegung von Braze mit Kanalaktivitätsdaten. Dazu gehören umfassende Einblicke in den Besucherverkehr über digitale Assets in bestimmten Zeiträumen.
 
#### IAM Studio - Nachrichtenvorlagen
 
Mit der Integration von Braze und [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/) können Sie ganz einfach anpassbare In-App-Nachrichtenvorlagen in Ihre Braze-In-App-Nachrichten einfügen, die Bilder ersetzen, Text ändern, Deep-Link-Einstellungen, benutzerdefinierte Attribute und Ereigniseinstellungen bieten. Mit IAM Studio können Sie die Produktionszeit für Nachrichten reduzieren und mehr Zeit für die Planung von Inhalten aufwenden.
 
#### Regal - Sofortiger Chat

Durch die Integration von Braze und [Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/) können Sie ein konsistentes und personalisiertes Erlebnis über alle Ihre Kundenkontaktpunkte hinweg schaffen.

#### Schatzdaten - Kohorten-Import
 
Mit der Integration von Braze und [Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/) können Sie Benutzerkohorten aus Treasure Data in Braze importieren, um gezielte Kampagnen auf der Grundlage von Daten zu versenden, die möglicherweise nur in Ihrem Warehouse vorhanden sind.
 
#### Zapier - Workflow-Automatisierung
 
Die Partnerschaft von Braze und [Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) nutzt die Braze-API und die Braze-Webhooks, um sich mit Anwendungen von Drittanbietern zu verbinden und verschiedene Aktionen zu automatisieren.

### SDK Aktualisierungen
 
Die folgenden SDK-Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze Segment Swift Plugin 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Aktualisiert die Bindungen des Braze Swift SDK, so dass sie Versionen ab 9.2.0+ SemVer benötigen.
        - Dies ermöglicht die Kompatibilität mit jeder Version des Braze SDK von 9.2.0 bis 10.0.0, aber nicht einschließlich.
        - In den Changelog-Einträgen für [7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700), [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) und [9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900) finden Sie weitere Informationen zu möglichen Änderungen.
    - Die Unterstützung von Push-Benachrichtigungen erfordert nun einen Aufruf der statischen Methode `BrazeDestination.prepareForDelayedInitialization()` so früh wie möglich im Lebenszyklus der App, in der Methode `AppDelegate.application(_:didFinishLaunchingWithOptions:)` Ihrer Anwendung.
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Die native iOS-Bridge wurde [von Braze Swift SDK 7.7.0 auf 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
- [Expo Plugin 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - Die native iOS-Bridge wurde [von Braze Swift SDK 7.7.0 auf 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
    - Die native Android-Bridge wurde [von Braze Android SDK 29.0.1 auf 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK Version 5.0.0
    - Die iOS-Bindung wurde [von Braze Swift SDK 8.4.0 auf 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) aktualisiert.

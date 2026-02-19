---
nav_title: Home
article_title: Was ist neu in Braze
description: "Die Braze Versionshinweise werden monatlich veröffentlicht, damit Sie immer auf dem neuesten Stand sind, was wichtige Produkte, laufende Produktverbesserungen, Braze Partnerschaften, Änderungen am SDK und veraltete Features betrifft."
page_order: 0
search_rank: 1
page_type: reference

---

# Was ist neu in Braze

{% alert tip %}
Weitere Informationen zu den auf dieser Seite aufgeführten Updates erhalten Sie von Ihrem Account Manager:in oder [öffnen Sie ein Support-Ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). In unseren [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) finden Sie weitere Informationen über unsere monatlichen SDK-Versionen, Verbesserungen und Änderungen.
{% endalert %}

{% details February 5, 2026 %}

## Veröffentlichung am 5\. Februar 2026

### BrazeAI<sup>TM</sup>

#### Content Optimizer

{% multi_lang_include release_type.md release="Beta" %}

[Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) ist ein kontinuierlicher Canvas-Schritt zum Testen hochvariabler Inhalte, der eine automatisierte Optimierung des Engagements zustellt. Über eine Schnittstelle, die per Drag-and-Drop bedient werden kann, ähnlich wie beim Nachrichtenschritt, können Sie die Komponenten, die Sie testen möchten, definieren, mithilfe von KI Varianten generieren (oder sie manuell eingeben) und diese Komponenten mithilfe von Liquid-Tags auf den Inhalt Ihrer Nachricht abbilden.

Auf der Grundlage eines kontextlosen Multi-Armed-Bandit-Optimierers sendet Content Optimizer eine einzelne Nachricht pro Nutzer:innen und bestimmt auf der Grundlage von Prognosen, welche Kombination von Varianten der Komponenten zugestellt werden soll. Da der Schritt im Laufe der Zeit Daten sammelt, steigt die Sendezuweisung für Varianten mit hoher Performance natürlich an, während die Varianten mit schlechter Performance abnehmen. Content Optimizer funktioniert am besten mit Canvase, die wiederholt versendet werden und ein konstantes tägliches Nutzer:innen-Volumen aufweisen (mindestens ein paar tausend Nutzer:innen pro Tag), um eine kontinuierliche Optimierung zu ermöglichen.

### Kanäle & Touchpoints

#### Lokalisierungen in Bannern übersetzen

{% multi_lang_include release_type.md release="Early access" %}

Nachdem Sie Ihrem Workspace Gebietsschemata hinzugefügt haben, können Sie [Nutzer:innen in verschiedenen Sprachen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales) innerhalb eines einzigen Banners [zusammenstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales).

#### Konfigurieren Sie die Breite für Drag-and-Drop Content-Blöcke

[Passen Sie die Breite Ihres Content-Blocks an]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block), indem Sie den Button im Navigationsmenü auswählen. Der Standardwert für die Breite ist 100%, wenn Sie in den globalen Einstellungen für den E-Mail-Stil nichts angegeben haben. Andernfalls werden die globalen Einstellungen beachtet.

![Ein doppelseitiger Pfeil mit einer Option zur Bearbeitung der Breite.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Verwenden Sie automatisiertes IP-Warming

{% multi_lang_include release_type.md release="Early access" %}

Mit der [Automatisierung des IP-Warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming) können Sie Ihr tägliches Sendevolumen allmählich erhöhen, so dass die Posteingangsprovider Ihre Sendemuster lernen und ihnen vertrauen können. Braze sendet zuerst an die Abonnent:innen mit dem größten Engagement, so dass das tägliche Volumen in einem Tempo wachsen kann, das den besten Praktiken entspricht.

### Partnerschaften:

#### LinkedIn - Canvas Audience Sync

Mit der [Braze Audience Sync to LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) können Sie Nutzerdaten aus Ihrer Braze-Integration zu LinkedIn-Kundenlisten hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zuzustellen. Alle Kriterien, die Sie normalerweise zum Triggern einer Nachricht (z.B. Push, E-Mail, SMS und Webhook) in einem Braze-Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, können jetzt eine Anzeige an diesen Benutzer in Ihren LinkedIn-Kundenlisten triggern.

#### Oracle Crowdtwist - Daten & analytics

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) ist eine führende Cloud-native Lösung zur Kundenbindung, mit der Marken personalisierte Kundenerlebnisse anbieten können. Die Lösung bietet mehr als 100 sofort einsatzbereite Engagement-Pfade, die Marketern eine schnellere Wertschöpfung ermöglichen, um eine umfassendere Sicht auf den Kunden zu entwickeln.

#### Fullstory - Dynamische Inhalte

[Die]({{site.baseurl}}/partners/fullstory/) Plattform für Verhaltensdaten [von Fullstory]({{site.baseurl}}/partners/fullstory/) hilft Technologieführern, bessere und fundiertere Entscheidungen zu treffen. Durch das Einspeisen digitaler Verhaltensdaten in ihren Analytics Stack erschließt die patentierte Technologie von Fullstory die Leistungsfähigkeit hochwertiger Verhaltensdaten im großen Maßstab und verwandelt jeden digitalen Besuch in umsetzbare Insights. 

#### Open Loyalty - Daten & analytics

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) ist eine cloudbasierte Plattform für Kundenbindungsprogramme, mit der Sie Kundenbindungs- und Rewards-Programme erstellen und verwalten können. Die Integration von Braze und Open Loyalty synchronisiert Loyalitätsdaten wie Punktestand, Tier-Änderungen und Ablaufwarnungen direkt mit Braze in Realtime. Damit können Sie personalisierte Nachrichten (E-Mail, Push, SMS) triggern, wenn sich der Treuestatus eines Nutzers:innen ändert.

#### Erweiterungen

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) können Sie Nutzer:innen mit nachvollziehbaren digitalen Zertifikaten für ihren realen Umwelteinfluss belohnen. Jedes Zertifikat kann Metadaten wie die URL des Zertifikats und die URL des Bildes enthalten, so dass Nutzer:innen ihren Wirkungsnachweis einsehen (und wieder aufrufen) können.

### Mailizio - Orchestrierung von Nachrichten

[Mailizio]({{site.baseurl}}/partners/mailizio/) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte mit einem intuitiven visuellen Editor erstellen können. Mit der Integration von Mailizio in Braze können Sie Ihre Content-Blöcke und E-Mail-Templates exportieren und dann automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Bereitstellung von Kampagnen ermöglicht.

### APIs

#### Medienbibliothek POST APIs

{% multi_lang_include release_type.md release="General availability" %}

Assets aus der Medienbibliothek können jetzt über APIs hinzugefügt werden, so dass Kunden, Partner und Agenturen einen größeren Teil ihrer Workflows zur Erstellung von Nachrichten automatisieren können. Sie können die [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) verwenden, um eine Asset-Datei direkt hochzuladen oder eine Datei von einer bestehenden URL zu kopieren. Dieses Feature schaltet die Funktionen zur Integration und Automatisierung frei.

### Currents und Datashare

#### Ereignisse der Agentenkonsole für Speicherziele und Datashare

{% multi_lang_include release_type.md release="General availability" %}

Zwei neue [Ereignisse](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) sind jetzt für Speicherziele (AWS S3, GCS und Azure Blob Storage) und Snowflake Datashare verfügbar: `agentconsole.AgentExecuted` und `agentconsole.ToolInvocation`. Anhand dieser Ereignisse können Sie die Nutzung der Agentenkonsole und die Details in Ihren nachgelagerten Systemen analysieren, so dass Sie Ihre Agentennutzung besser verstehen und nutzen können. Agenten erlauben es Ihnen, intelligente Agenten zu erstellen und einzusetzen, die bestimmte Aufgaben in Braze ausführen können, z. B. die Generierung von Inhalten in Canvases oder Katalogen und die Weiterleitung von Nutzer:innen auf der Grundlage intelligenter Entscheidungen. Weitere Informationen finden Sie im [Changelog zu Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Neue 'Wiederholungsereignisse' für einzelne Kanäle

{% multi_lang_include release_type.md release="General availability" %}

Neue [Wiederholungsereignisse](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) sind jetzt für E-Mail, LINE, Push-Benachrichtigungen, SMS, Webhooks und WhatsApp-Kanäle verfügbar. Diese Ereignisse geben Aufschluss darüber, wann Frequency-Capping dazu führt, dass eine geplante Nachricht verzögert und nicht abgebrochen wird. Wenn eine Nachricht depriorisiert oder mit einem Frequency-Capping versehen wird, kann sie jetzt innerhalb eines konfigurierten Wiederholungsfensters erneut versucht werden. So erhalten Sie einen besseren Insight über die Zustellung von Nachrichten und die Auswirkungen des Frequency-Cappings. Weitere Informationen finden Sie im [Changelog zu Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Neues Feld 'time_ms' zum Ereignis TokenStateChange hinzufügen

{% multi_lang_include release_type.md release="General availability" %}

Dem Ereignis wurde ein neues `time_ms` Feld hinzugefügt. [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) Ereignis hinzugefügt, das das Tracking von Änderungen des Push-Token-Status auf Millisekunden-Ebene ermöglicht. Diese verbesserte Präzision hilft Ihnen, den neuesten Status eines Push-Tokens zu verstehen, wenn innerhalb derselben Sekunde mehrere Änderungen auftreten. So können Sie sich in nachgelagerten Systemen darauf verlassen, dass Sie den korrekten Status eines Abos haben. Weitere Informationen finden Sie im [Changelog zu Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Anonyme Nutzer:in an Tealium Ziele senden

{% multi_lang_include release_type.md release="General availability" %}

Ereignisse, für die keine externe ID definiert wurde, können jetzt zu [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents) Zielen gestreamt werden. Wenn Sie in Ihrer Currents-Integration das Kontrollkästchen "Ereignisse von anonymen Nutzer:innen einschließen" auswählen, werden Ereignisse ohne externe ID an das Ziel gesendet, anstatt unterdrückt zu werden. Diese Fähigkeit ist entscheidend für nachgelagerte Analytics und Anwendungsfälle mit nicht identifizierten und anonymen Nutzer:innen.

##### Anonyme Nutzer:in an CustomHTTP-Ziele senden

{% multi_lang_include release_type.md release="Beta" %}

Ereignisse, für die keine externe ID definiert wurde, können jetzt zu CustomHTTP-Zielen gestreamt werden. Wenn Sie in Ihrer Currents-Integration das Kontrollkästchen "Ereignisse von anonymen Nutzer:innen einschließen" auswählen, werden Ereignisse ohne externe ID an das Ziel gesendet, anstatt unterdrückt zu werden. Diese Fähigkeit ist entscheidend für nachgelagerte Analytics und Anwendungsfälle mit nicht identifizierten und anonymen Nutzer:innen.

#### Ereignis E-Mail Öffnung - "machine_open" Feld

Das [Ereignis Öffnung einer E-Mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) generiert jetzt den Wert des Feldes "machine_open", so dass Sie Berichte über die [_Maschine geöffnet_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens) Metrik berichten können. 

### SDK

Die folgenden SDK Updates wurden veröffentlicht. Swift SDK v14.0.1 behebt ein Problem mit der Handhabung von universellen Links. Android SDK v40.2.0 behebt ein potenzielles Speicherleck und behebt ein Problem mit mehreren geöffneten Sitzungen, wenn transparente Aktivitäten vorhanden sind. Expo SDK v3.2.0 fügt die Option `forwardUniversalLinks` hinzu (Standard: false), um die native Swift SDK Handhabung von universellen Links zu konfigurieren.

#### SDK-Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Benennen Sie `BrazeConfig.Builder.setIsLocationCollectionEnabled()` in `setIsAutomaticLocationCollectionEnabled()` um.
    - Benennen Sie `BrazeConfig.isLocationCollectionEnabled` in `isAutomaticLocationCollectionEnabled` um.
    - Benennen Sie `BrazeConfigurationProvider.isLocationCollectionEnabled` in `isAutomaticLocationCollectionEnabled` um.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo Plugin 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## Januar 8, 2026 Veröffentlichung

### Daten & Berichterstattung

#### E-Commerce empfohlene Veranstaltungen

{% multi_lang_include release_type.md release="Early access" %}

Um die vom E-Commerce empfohlenen Ereignisse mit dem bestehenden Kauf-Event abzustimmen, haben wir das [ Konversions-Event "Places Order"]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report) hinzugefügt, das dem Event "Makes Purchase" ähnelt.

#### Updates zu Currents Veranstaltungen

{% multi_lang_include release_type.md release="General availability" %}

Die folgenden Änderungen wurden an Currents in Version 4 vorgenommen:

* Das Feld wechselt zum Ereignistyp `users.behaviors.pushnotification.TokenStateChange`:
    * Neues Feld `string` hinzugefügt `push_token`: Push-Token des Ereignisses
* Das Feld wechselt zum Ereignistyp `users.messages.pushnotification.Bounce`:
    * Neues Feld `string` hinzugefügt `push_token`: Push-Token des Ereignisses
* Das Feld wechselt zum Ereignistyp `users.messages.pushnotification.Send`:
    * Neues Feld `string` hinzugefügt `push_token`: Push-Token des Ereignisses
* Das Feld wechselt zum Ereignistyp `users.messages.rcs.Click`:
    * Neues Feld `string` hinzugefügt `canvas_variation_name`: Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
    * Das Feld `user_phone_number` ist jetzt *optional*.
* Das Feld wechselt zum Ereignistyp `users.messages.rcs.InboundReceive`:
    * Das Feld `user_id` ist jetzt *optional*.
* Das Feld wechselt zum Ereignistyp `users.messages.rcs.Rejection`:
    * Neues Feld `string` hinzugefügt `canvas_step_message_variation_id`: API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat

Im [Currents Changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) finden Sie die Ereignisänderungen für jede Version.

#### Synchronisationsprotokolle nach allen Zeilen exportieren

{% multi_lang_include release_type.md release="Early access" %}

Im [Dashboard Cloud Data Ingestion **Sync Log**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs) können Sie wählen, ob Sie die Protokolle auf Zeilenebene für eine Synchronisierung exportieren möchten, die von:

* Zeilen mit Fehlern Lädt eine Datei herunter, die nur die Zeilen enthält, die einen **Fehlerstatus** hatten.
* Alle Zeilen Lädt eine Datei herunter, die alle in diesem Lauf verarbeiteten Zeilen enthält.

### Kanäle & Touchpoints

#### Bring Your Own (BYO) WhatsApp Konnektor

Der [Bring Your Own (BYO) WhatsApp Konnektor]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) bietet eine Partnerschaft zwischen Braze und Infobip, bei der Sie Braze Zugriff auf Ihren Infobip WhatsApp Business Manager (WABA) geben. Dies erlaubt es Ihnen, die Kosten für Messaging direkt mit Infobip zu verwalten und zu bezahlen und gleichzeitig Braze für die Segmentierung, Personalisierung und Orchestrierung von Kampagnen zu nutzen. 

#### Banner in Canvas

{% multi_lang_include release_type.md release="Early access" %}

Sie können **Banner** als Messaging-Kanal in einem [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) für Canvas auswählen. Sie können den Drag-and-Drop-Editor verwenden, um personalisierte Inline-Nachrichten zu erstellen, die nicht aufdringliche, kontextuell relevante Erlebnisse bieten, die zu Beginn jeder Nutzer:innen-Sitzung automatisch aktualisiert werden. 

#### Dynamische BCC

{% multi_lang_include release_type.md release="General availability" %}

Mit [dynamischem BCC]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc) können Sie Liquid in Ihrer BCC-Adresse verwenden. Beachten Sie, dass dieses Feature nur in den **E-Mail-Voreinstellungen** verfügbar ist und nicht in der Kampagne selbst eingestellt werden kann. Pro E-Mail-Empfänger:in ist nur eine BCC-Adresse zulässig.

#### Kanalbasierte Rate-Limits

Als Alternative zu einem Rate-Limit, das für die gesamte Multichannel-Kampagne oder den Canvas gilt, können Sie ein bestimmtes Rate-Limit pro Kanal auswählen. In diesem Fall gilt das Rate-Limits für jeden von Ihnen ausgewählten Kanal. Sie können Ihre Kampagne oder Ihr Canvas beispielsweise so einstellen, dass Sie maximal 5.000 Webhooks und 2.500 SMS-Nachrichten pro Minute über die Kampagne oder das Canvas versenden. Weitere Einzelheiten finden Sie unter [Rate-Limiting und Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Partnerschaften:

#### LILT - Lokalisierung

[LILT]({{site.baseurl}}/partners/lilt/) ist die komplette KI-Lösung für die Übersetzung und Inhaltserstellung in Unternehmen. Mit KI-Agenten und vollautomatisierten Workflows ermöglicht LILT globalen Unternehmen die Skalierung und Optimierung ihres Inhalts-, Produkt-, Kommunikations- und Supportbetriebs.

### SDK-Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Entfernt Newsfeed.
        - Dadurch werden alle UI-Elemente, Datenmodelle und Aktionen, die mit Newsfeed verbunden sind, vollständig entfernt.
- [Internet SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## Dezember 9, 2025

### Daten & Berichterstattung

#### Hinzufügen von Google Tag Manager zu einer Landing Page

Um Google Tag Manager zu Ihren Landing Pages hinzuzufügen, fügen Sie Ihrer Landing Page im Drag-and-Drop-Editor einen Custom Code-Block hinzu und [fügen]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) dann [den Tag Manager-Code]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) in den Block [ein]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page).

### Orchestrierung

#### SMS Liquid Anwendungsfall

Der Anwendungsfall [Reagieren Sie mit verschiedenen Nachrichten auf der Basis eingehender SMS-Schlüsselwörter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) beinhaltet eine dynamische SMS-Schlüsselwortverarbeitung, um auf bestimmte eingehende Nachrichten mit unterschiedlichen Nachrichtentexten zu reagieren. Sie können zum Beispiel unterschiedliche Antworten senden, wenn jemand "START" oder "JOIN" schreibt.

#### Auflistung für Connected-Content zulassen

Sie können zulassen, dass bestimmte URLs für [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) verwendet werden. Um auf dieses Feature zuzugreifen, wenden Sie sich an Ihren Customer-Success-Manager:in.

### Kanäle & Touchpoints

#### SMS-Zeichenkodierung

Unser [SMS Segmente-Rechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) verfügt jetzt über eine Zeichenkodierung! Wählen Sie **Zeichenkodierung anzeigen** aus, um die Zeichen auszuwählen, die als GSM-7 oder UCS-2 kodiert sind. 

![SMS-Segment-Rechner mit einer in das Textfeld eingegebenen Beispiel-SMS-Nachricht und eingeschalteter Zeichenkodierung.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### WhatsApp Nachrichten mit Optimierung

Da die MM API für WhatsApp keine 100%ige Zustellbarkeit bietet, ist es wichtig zu wissen, wie Sie Nutzer:innen, die Ihre Nachricht auf anderen Kanälen nicht erhalten haben, retargeten können. 

Für das Retargeting von Nutzern:innen empfehlen wir die Erstellung eines Segments von Nutzern:innen, die eine bestimmte Nachricht nicht erhalten haben. Filtern Sie dazu nach dem Fehlercode `131049`, der anzeigt, dass eine Nachricht mit einem Marketing Template nicht gesendet wurde, weil WhatsApp das Limit für Marketing-Templates pro Nutzer:innen nicht einhält. Sie können dies mit [Braze-Currents oder SQL Segment-Erweiterungen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels) tun.

### Partnerschaften:

#### OtherLevels - Dynamische Inhalte

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) ist eine Erlebnisplattform, die generative KI einsetzt, um die Art und Weise zu verändern, wie Sportmarken, Verlage und Operatoren mit ihren Kunden in Kontakt treten, indem sie herkömmliche Inhalte in markengerechte, personalisierte Video- und Rich-Media-Erlebnisse im großen Maßstab umwandelt.

### SDK

#### SDK-Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Internet SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## November 11, 2025

### Flexibilität der Daten

#### `Live Activities Push to Start Registered for App` Filter für die Segmentierung

Der Filter `Live Activities Push to Start Registered for App` segmentiert Ihre Nutzer:in danach, ob sie für den Start einer Live-Aktivität über iOS Push-Benachrichtigungen für eine bestimmte App registriert sind.

#### RFM SQL Segment-Erweiterung

Sie können eine [RFM (recency, frequency, monetary) Segment-Erweiterung]({{site.baseurl}}/rfm_segments/) erstellen, um Ihre besten Nutzer:innen durch Messung ihrer Kaufgewohnheiten zu targetieren.

Die RFM-Analyse ist eine Marketing-Technik, die Ihre besten Nutzer:innen identifiziert, indem sie Nutzer:innen auf einer Skala von 0-3 für jede Kategorie (Häufigkeit, Häufigkeit, Geldwert) bewertet, wobei 3 der beste Wert und 0 der schlechteste ist. Häufigkeit, Häufigkeit und monetäre Werte basieren alle auf Daten aus einem von Ihnen gewählten Zeitraum.

#### Angepasste Attribute - Werte 

Wählen Sie beim Anzeigen eines Nutzungsberichts den [Tab**Werte**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) aus, um die Spitzenwerte der angepassten Attribute auf der Grundlage einer Stichprobe von ca. 250.000 Nutzer:innen zu sehen.

#### Sync-Protokolle und Beobachtbarkeit für die Datenaufnahme in der Cloud

{% multi_lang_include release_type.md release="General availability" %}

Mit dem [Dashboard]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) Cloud Data Ingestion (CDI) [Sync Log]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) können Sie alle von CDI verarbeiteten Daten überwachen, überprüfen, ob die Daten erfolgreich synchronisiert wurden, und eventuelle Probleme mit "falschen" oder fehlenden Daten diagnostizieren.

#### Multi-Regel Feature-Flags Rollouts

Verwenden Sie [Rollouts von Feature-Flags mit mehreren Regeln]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts), um eine Abfolge von Regeln für die Bewertung von Nutzer:innen zu definieren, was eine präzise Segmentierung und kontrollierte Freigabe von Features ermöglicht. Diese Methode ist ideal für die Bereitstellung desselben Features für verschiedene Zielgruppen.

#### Abbildung auf Katalogfelder für Drag-and-Drop-Produktblöcke

In Ihren Katalogeinstellungen können Sie die **Produktblöcke** auswählen, um [sie bestimmten Feldern]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) und Informationen in Ihrem Katalog [zuzuordnen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup). Hier können Sie auswählen, welche Felder als Produkttitel, Produkt-URL und Bild-URL verwendet werden sollen.

#### Frequency-Capping Abbruchereignisse in Currents

Bei der Verwendung von Currents können Sie jetzt `abort_type` in den Kanalabbruchereignissen referenzieren. Bezeichnet, dass eine Nachricht aufgrund von Frequency-Capping abgebrochen wurde und gibt an, welche Frequency-Capping-Regel den Abbruch verursacht hat. Dies hilft Ihnen bei der Festlegung Ihrer Frequency-Capping-Regeln. Weitere Informationen zu Currents-Ereignissen finden Sie unter [Engagement bei Nachrichten]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).

### Robuste Kanäle

#### Bilder der Hintergrundreihe 

{% multi_lang_include release_type.md release="General availability" %}

Im Panel **Zeileneigenschaften** können Sie einer In-App-Nachricht oder Landing Page [ein Hintergrundbild für die Zeile hinzufügen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image). Schalten Sie auf **Hintergrundbild** um, und geben Sie eine Bild-URL an oder wählen Sie ein Bild aus der [Bibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) aus. Schließlich konfigurieren Sie den Alt-Text, die Größe, die Position und ob das Bild wiederholt werden soll, um Muster in der Reihe zu erzeugen.

![Ein Zeilenhintergrundbild einer Pizza, das ein horizontales Wiederholungsmuster aufweist.]({% image_buster /assets/img_archive/background_row.png %})

#### Vorschau-Link kopieren

Verwenden Sie den **Link Vorschau kopieren** in Ihren [Bannern]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [angepassten E-Mail-Fußzeilen]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) und [E-Mail-Opt-in und -Abmeldeseiten]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers), um einen Link zum Teilen zu generieren, der zeigt, wie Ihre Inhalte für einen zufälligen Nutzer:innen aussehen werden.

#### WhatsApp Nachrichten mit optimierter Zustellung

Nutzen Sie die fortschrittlichen KI-Systeme von Meta, um Ihre Marketing Nachrichten mehr Nutzern:innen zuzustellen, die sich am ehesten mit ihnen beschäftigen, und so die Zustellbarkeit und das Engagement der Nachrichten deutlich zu erhöhen.

[WhatsApp Nachrichten mit optimierter Zustellung]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) werden über die neue [Marketing Messages Lite API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) von Meta versendet, die im Vergleich zur herkömmlichen Cloud API eine bessere Performance bietet. Mit dieser neuen Sendepipeline können Sie Nutzer:innen besser erreichen, die Ihre Nachrichten wertschätzen und empfangen möchten.

#### WhatsApp-Flows

Wenn Sie eine WhatsApp Flow Nachricht in ein Braze-Canvas oder eine Kampagne einbinden, möchten Sie vielleicht bestimmte Informationen, die Nutzer:innen über den Flow übermitteln, erfassen und nutzen. Braze benötigt zusätzliche Informationen über die Struktur der Nutzer:innen-Antwort, insbesondere die erwartete Form der JSON-Antwort, um das erforderliche Schema für die angepassten Attribute (NCA) zu erstellen.

Jetzt können Sie Braze die Informationen über die Antwortstruktur geben, indem Sie [die Flow-Antwort als angepasstes Attribut speichern]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) und einen Testversand durchführen.

#### Bearbeitbare Nutzer:innen-Vorschau

Sie können [einzelne Felder eines zufälligen oder bestehenden Nutzers bearbeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user), um dynamische Inhalte in Ihrer Nachricht zu testen. Wählen Sie **Bearbeiten**, um den ausgewählten Nutzer:innen in einen angepassten Nutzer umzuwandeln, den Sie ändern können.

![Der Tab "Vorschau als Nutzer:in" mit einem Button "Bearbeiten".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### KI und ML Automatisierung

#### BrazeAI Decisioning Studio™ Go

Sie können nun Ihre Integration mit [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) einrichten, indem Sie sich auf diese Konfigurationsartikel für beziehen:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Neue Features für Braze-Agenten

{% multi_lang_include release_type.md release="Beta" %}

Sie können Ihren [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) jetzt anpassen, indem Sie:

- Anwendung von [Markenrichtlinien]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines), an die sich Ihr Agent bei seiner Antwort halten muss. 
- Verweis auf einen Katalog, um Ihre Nachricht weiter zu personalisieren.
- Strukturierung der Ausgabe eines Agenten durch Angabe des [Ausgabeformats]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Justieren Sie die [Temperatur]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) für den Grad der Abweichung für die Leistung Ihres Agenten.

### ChatGPT Modelle mit <sup>BrazeAITM</sup> Operator

{% multi_lang_include release_type.md release="Beta" %}

Sie können aus diesen GPT-Modellen auswählen, um sie für verschiedene Arten von Anfragen mit [Operator]({{site.baseurl}}/user_guide/brazeai/operator) zu verwenden:

- GPT-5 Nano
- GPT-5 mini (Standard)
- GPT-5

### Neue Braze Partnerschaften

#### StackAdapt - Werbung

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) ist eine KI-gestützte Marketing-Plattform, die zielgerichtete Performance-gesteuerte Werbung zustellt. Es erlaubt Ihnen, Nutzerprofil-Daten aus Braze mit dem StackAdapt Data Hub zu synchronisieren. Durch die Verbindung der beiden Plattformen können Sie eine einheitliche Sicht auf Ihre Kund:innen schaffen und First-Party-Daten aktivieren, um die Performance von Anzeigen zu verbessern.

#### Cloudinary - Dynamische Inhalte

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) ist eine Bild- und Videoplattform, mit der Sie Bilder und Videos in großem Umfang für jede Kampagne über alle Kanäle und Customer Journeys hinweg verwalten, bearbeiten, optimieren und zustellen können. Nach der Integration und dem Enablement wird das Medienmanagement von Cloudinary die dynamische, kontextuelle und personalisierte Zustellung von Assets für Ihre Kampagnen und Canvase von Braze ermöglichen.

#### Kameleoon - A/B-Tests

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) ist eine Optimierungslösung mit experimentellen, KI-gestützten Personalisierungs- und Feature-Management-Funktionen in einer einzigen, einheitlichen Plattform.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Korrigiert den Typescript-Typ für den Callback von `subscribeToInAppMessage` und `addListener` für `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Diese Listener geben jetzt korrekt einen Callback mit dem neuen Typ `InAppMessageEvent` zurück. Zuvor wurden die Methoden so kommentiert, dass sie einen Typ `BrazeInAppMessage` zurückgeben, aber in Wirklichkeit wurde ein `String` zurückgegeben.
         - Wenn Sie eine der beiden Abo-APIs verwenden, stellen Sie sicher, dass das Verhalten Ihrer In-App-Nachrichten nach dem Update auf diese Version unverändert bleibt. Sehen Sie sich unseren Beispiel Code in `BrazeProject.tsx` an.
    - Die APIs `logInAppMessageClicked`, `logInAppMessageImpression` und `logInAppMessageButtonClicked` akzeptieren jetzt nur noch ein `BrazeInAppMessage` Objekt, um der bestehenden öffentlichen Schnittstelle zu entsprechen.
        - Zuvor akzeptierte es sowohl ein `BrazeInAppMessage` Objekt als auch ein `String`.
    - `BrazeInAppMessage.toString()` gibt jetzt einen menschenlesbaren String anstelle der JSON-String-Darstellung zurück.
        - Um die JSON-String-Darstellung einer In-App-Nachricht zu erhalten, verwenden Sie `BrazeInAppMessage.inAppMessageJsonString`.
    - Unter iOS wurde `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` nach `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]` verschoben.
        - Diese neue Methode ist jetzt eine Klassenmethode anstelle einer Instanzmethode.
    - Fügt Nullbarkeits-Anmerkungen zu `BrazeReactUtils` Methoden hinzu.
    - Entfernt die folgenden veralteten Methoden und Eigenschaften aus der API:
        - `getInstallTrackingId(callback:)` zu Gunsten von `getDeviceId`.
        - `registerAndroidPushToken(token:)` zu Gunsten von `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` zu Gunsten von `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` zu Gunsten von `payload_type`.
        - `PushNotificationEvent.deeplink` zu Gunsten von `url`.
        - `PushNotificationEvent.content_text` zu Gunsten von `body`.
        - `PushNotificationEvent.raw_android_push_data` zu Gunsten von `android`.
        - `PushNotificationEvent.kvp_data` zu Gunsten von `braze_properties`.
    - Update der nativen Android SDK Versionsbindungen [von Braze Android SDK 39.0.0 auf 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Update der iOS-Bindung von [Braze Swift SDK 12.1.0 auf 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Dazu gehört auch die Unterstützung von Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Aktualisiert die native Android-Bridge von Braze Android SDK 39.0.0 auf 40.0.0.
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Internet SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Oktober 14, 2025 Veröffentlichung

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) ersetzt A/B-Tests durch KI-Entscheidungen, die alles personalisieren und jede Metrik maximieren: Treiben Sie Dollars an, nicht Klicks. Mit BrazeAI Decisioning Studio™ können Sie jeden geschäftlichen KPI optimieren. In unserem Abschnitt [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) finden Sie Beispiele für Anwendungsfälle und wichtige Features.

### Flexibilität der Daten

#### Neue Currents Veranstaltungen

Diese neuen Ereignisse wurden dem [Currents-Glossar]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) hinzugefügt:

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Diese neuen Felder wurden zu den folgenden Currents Ereignissen hinzugefügt:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- ``in_reply_to``message_id` 
  - `users.messages.whatsapp.InboundReceive`
- ``flow_id``message_id` 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Unterdrückungslisten

{% multi_lang_include release_type.md release="General availability" %}

[Unterdrückungslisten]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) sind Gruppen von Nutzer:innen, die automatisch keine Kampagnen oder Canvase erhalten. Unterdrückungslisten werden durch Segmente definiert, und Nutzer:innen betreten und verlassen Unterdrückungslisten, wenn sie die Filterkriterien erfüllen.

#### Null-Kopie-Personalisierung

{% multi_lang_include release_type.md release="Early access" %}

Synchronisieren Sie Canvas-Trigger mit der Datenaufnahme in der Cloud für eine [Personalisierung ohne Kopien]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Dieses Feature greift auf benutzerspezifische Daten aus Ihrer Lösung zur Datenspeicherung zu und gibt sie an ein Ziel-Canvas weiter. Canvas-Schritte können optional Personalisierungsfelder enthalten, die nicht auf Braze-Nutzerprofilen persistent sind.

#### Canvas-Kontextvariablen für Zielgruppen-Pfade und Decision-Split-Schritte

{% multi_lang_include release_type.md release="Early access" %}

Sie können [Kontextvariablen-Filter erstellen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters), die zuvor deklarierte Kontextvariablen in [Zielgruppen-Pfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) und [Decision-Split-Schritten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) verwenden.

### Kreativität entfesseln

#### Deal Cards für E-Mails

Verwenden Sie [Deal Cards]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab), um wichtige Informationen direkt am Anfang von E-Mails bereitzustellen. Dies erlaubt es Empfängern:in, die Details des Angebots schnell zu verstehen und zu handeln.

#### Templates für Banner

Bei der [Erstellung Ihres Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create) können Sie nun mit einer leeren Vorlage beginnen, eine Braze-Vorlage verwenden oder eine gespeicherte Banner-Vorlage auswählen.

### Robuste Kanäle

#### Unterdrückungslisten

{% multi_lang_include release_type.md release="General availability" %}
 
[Unterdrückungslisten]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/) geben Gruppen von Nutzer:innen an, die niemals Nachrichten erhalten werden. Administratoren können Unterdrückungslisten mit Segmentfiltern erstellen, um eine Nutzer:innen-Gruppe auf die gleiche Weise einzugrenzen, wie Sie es bei der Segmentierung tun würden.

#### LINE click tracking

{% multi_lang_include release_type.md release="General availability" %}

Wenn das [LINE-Klick-Tracking]({{site.baseurl}}/line/click_tracking/) aktiviert ist, verkürzt Braze automatisch Ihre URLs, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Realtime auf. Während LINE aggregierte Daten über Klicks bietet, liefert Braze granulare Nutzer:innen-Daten, die zeitnah und umsetzbar sind. Mit diesen Daten können Sie gezieltere Segmentierungs- und Retargeting-Strategien entwickeln, z. B. die Segmentierung von Nutzern auf der Grundlage ihres Klickverhaltens und das Auslösen von Nachrichten als Reaktion auf bestimmte Klicks.

#### SMS- und RCS-Bot-Klick-Filterung

{% multi_lang_include release_type.md release="General availability" %}

[Das Filtern von SMS- und RCS-Bot-Klicks]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) verbessert die Analytics von Kampagnen und Workflows, indem es verdächtige Bot-Klicks ausschließt. Ein "Bot-Klick" bezieht sich auf automatisierte Klicks auf verkürzte Links in SMS- und RCS-Nachrichten, z. B. von Web-Crawlern, Android- und iOS-Linkvorschauen oder CPaaS-Sicherheitssoftware. Dieses Feature erleichtert die genaue Berichterstattung, Segmentierung und Orchestrierung, um echte Nutzer:innen zu engagieren.

#### WhatsApp-Telefonnummern übertragen

Übertragen Sie eine WhatsApp Business Account (WABA)-Telefonnummer und die zugehörige Abo-Gruppe [von einem Workspace zu einem anderen]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) innerhalb von Braze.

#### WhatsApp Flows Antwort Nachrichten und Vorschau

In einem Canvas können Sie einen WhatsApp-Schritt erstellen, der eine [Antwortnachricht]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) und eine Flussnachricht verwendet. Sie können auch **Flussvorschau** auswählen, um eine Vorschau des Flusses direkt in Braze zu sehen und zu bestätigen, dass er sich wie erwartet verhält.

#### WhatsApp Nachrichten zum Produkt

Mit Messaging können Sie interaktive WhatsApp Nachrichten versenden, in denen Produkte direkt aus Ihrem Meta-Katalog vorgestellt werden.

#### Integration von Braze und WhatsApp mit einem externen System

[Nutzen Sie die leistungsstarken KI-Chatbots und Live-Agentenübergaben]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) auf dem WhatsApp-Kanal, um Ihre Kund:in zu rationalisieren. Durch die Automatisierung von Routineanfragen und den nahtlosen Übergang zu menschlichen Agenten, wenn dies erforderlich ist, können Sie die Antwortzeiten erheblich verbessern und das Kundenerlebnis insgesamt steigern.

### KI und ML Automatisierung

#### Braze-Agenten

{% multi_lang_include release_type.md release="Beta" %}

[Braze-Agenten]({{site.baseurl}}/user_guide/brazeai/agents/) sind KI-gestützte Helfer, die Sie innerhalb von Braze erstellen können. Agenten können Inhalte generieren, intelligente Entscheidungen treffen und Ihre Daten anreichern, so dass Sie personalisiertere Kundenerlebnisse zustellen können.

### Neue Braze Partnerschaften

#### Jaspis - Templates

Die Integration von [Jasper]({{site.baseurl}}/partners/jasper/) in Braze ermöglicht es Ihnen, die Erstellung von Inhalten und die Durchführung von Kampagnen zu optimieren. Mit Jasper können Ihre Marketing Teams in wenigen Minuten hochwertige, markengerechte Texte erstellen. Braze erleichtert dann die Zustellung dieser Nachrichten an die richtige Zielgruppe zum optimalen Zeitpunkt. Diese Integration fördert nahtlose Arbeitsabläufe, reduziert den manuellen Aufwand und sorgt für bessere Ergebnisse beim Engagement.

#### Swym - Loyalität und Retargeting

[Swym]({{site.baseurl}}/partners/swym/) unterstützt E-Commerce-Marken bei der Erfassung von Kaufabsichten mit Wunschlisten, Speichern für später, Geschenkelisten und Back-in-Stock-Warnungen. Mithilfe umfangreicher Daten, die auf Berechtigungen basieren, können Sie zielgerichtete Kampagnen erstellen und personalisierte Einkaufserlebnisse bieten, die das Engagement fördern, die Konversion steigern und die Loyalität erhöhen.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt. Alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Update der nativen Android Bridge von [Braze Android SDK 37.0.0 auf 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Die minimal erforderliche GradlePluginKotlinVersion ist jetzt 2.1.0.
    - Update der nativen iOS-Bridge von [Braze Swift SDK 12.0.0 auf 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Dazu gehört auch die Unterstützung von Xcode 26.
    - Entfernt die Unterstützung für Newsfeed. Die folgenden APIs wurden entfernt:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Update der nativen Android SDK Versionsbindungen [von Braze Android SDK 37.0.0 auf 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Entfernt die Unterstützung für Newsfeed. Die folgenden APIs wurden entfernt:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Internet SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Update der nativen iOS-Bridge von [Braze Swift SDK 12.0.0 auf 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Dazu gehört auch die Unterstützung von Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## September 16, 2025 Veröffentlichung

### Flexibilität der Daten

#### Braze-Datenplattform

Braze Data Platform ist ein umfassender, zusammensetzbarer Satz von Datensätzen und Partnerintegrationen, der es Ihnen ermöglicht, personalisierte, wirkungsvolle Erlebnisse über den gesamten Kundenlebenszyklus hinweg zu schaffen. Erfahren Sie mehr über die drei datenbezogenen Aufgaben, die zu erledigen sind: 

- [Daten Vereinheitlichung]({{site.baseurl}}/user_guide/data/unification)
- [Aktivierung der Daten]({{site.baseurl}}/user_guide/data/activation)
- [Verteilung der Daten]({{site.baseurl}}/user_guide/data/distribution)

#### Angepasste Eigenschaften des Banners

{% multi_lang_include release_type.md release="Early access" %}

Sie können angepasste Eigenschaften aus Ihrer Banner-Kampagne verwenden, um Key-Value-Daten über das SDK abzurufen und das Verhalten oder Aussehen Ihrer App zu ändern. Weitere Informationen finden Sie unter [Angepasste Eigenschaften von Bannern]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Token-Authentifizierung

{% multi_lang_include release_type.md release="General availability" %}

Bei der Verwendung von Braze Connected Content kann es vorkommen, dass Sie für bestimmte APIs ein Token anstelle eines Benutzernamens und eines Passworts benötigen. Braze kann Zugangsdaten speichern, die [Token-Authentifizierungs-Headerwerte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication) enthalten.

#### Aktionscodes

Sie können Aktionscodes im Profil eines Nutzers:innen über den Schritt User Update speichern. Weitere Informationen finden Sie unter [Aktionscodes in Nutzerprofilen speichern]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Kreativität entfesseln

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) ist eine öffentlich verfügbare App für Android und iOS, die es Ihnen erlaubt, Nachrichten von Ihrem Braze-Dashboard auf Ihr Telefon zu senden. Unter [Erste Schritte mit Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) können Sie nachlesen, wie Sie die App herunterladen, die Verbindung zu Ihrem Braze-Dashboard initialisieren und die Einrichtung abschließen.

### Neue Braze Partnerschaften

#### Blings - Visuelle und interaktive Inhalte

[Blings]({{site.baseurl}}/partners/blings/) ist eine personalisierte Videoplattform der nächsten Generation, die es Ihnen ermöglicht, interaktive und datengestützte Video-Erlebnisse in Echtzeit über alle Kanäle hinweg zuzustellen.

#### Shopify Standard-Integration mit Drittanbieter-Tool

Für Shopify Online-Shops empfehlen wir die Verwendung der Standard-Integrationsmethode von Braze, um die Braze SDKs auf Ihrer Website zu unterstützen.

Wir wissen jedoch, dass Sie vielleicht lieber ein Tool eines Drittanbieters wie Google Tag Manager verwenden möchten. Deshalb haben wir eine Anleitung zusammengestellt, wie Sie das tun können. Um loszulegen, besuchen Sie [Shopify: Tagging von Drittanbietern]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Update der nativen Android-Bridge von Braze Android SDK `36.0.0` auf `39.0.0`.
    - Update der nativen iOS-Bridge von Braze Swift SDK `12.0.0` auf `13.2.0`. Dazu gehört auch die Unterstützung von Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Update der Braze Swift SDK Bindungen, um Versionen der `13.0.0+` SemVer Bezeichnung zu benötigen. Dies erlaubt die Kompatibilität mit jeder Version des Braze SDK von `13.0.0` bis hin zu, aber nicht einschließlich, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Veröffentlichung am 19\. August 2025

### Standardisierung der Zeitzonenkonsistenz in Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

Wenn Sie am [Canvas-Kontext-Schritt "Early Access"]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) teilnehmen, werden alle Zeitstempel mit dem Typ datetime von Event-Eigenschaften in aktionsbasierten Canvase immer auf [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) normalisiert. Um mehr darüber zu erfahren, referenzieren Sie auf [Standardisierung der Zeitzonenkonsistenz]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilität der Daten

#### Angepasste Domains zur Selbstbedienung

{% multi_lang_include release_type.md release="General access" %}

Mit [angepassten Domains zur Selbstbedienung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) können Sie Ihre eigenen angepassten Domains für SMS, RCS und WhatsApp konfigurieren und verwalten - direkt von Ihrem Braze-Dashboard aus. Sie können ganz einfach bis zu 10 angepasste Domains an einem Ort hinzufügen, überwachen und verwalten.

#### Segmente Funnel Statistik

Wählen Sie [Trichterstatistiken anzeigen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) aus, um die Statistiken für diese Filtergruppe anzuzeigen und zu sehen, wie sich jeder hinzugefügte Filter auf Ihre Segmentierungsstatistiken auswirkt. Sie sehen die geschätzte Anzahl und den Prozentsatz der Nutzer:innen, die bis zu diesem Zeitpunkt von allen Filtern targetiert wurden. Sobald die Statistiken für eine Filtergruppe angezeigt werden, werden sie automatisch aktualisiert, sobald Sie die Filter ändern. 

#### Neue Antwortfelder für den `/campaigns/details` Endpunkt für Push-Benachrichtigungen

Die Antwort `messages` für Push-Benachrichtigungen enthält jetzt zwei neue Felder:

- `image_url`: Eine Bild-URL für ein Android-Benachrichtigungsbild, ein iOS-Benachrichtigungsbild oder ein Web-Push-Symbolbild.
- `large_image_url`: Eine Web-Benachrichtigungsbild-URL für Android Chrome und Windows Web-Push-Aktionen.

#### Definieren von PII-Feldern

Das Auswählen und [Definieren bestimmter Felder als PII-Felder]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) wirkt sich nur darauf aus, was Nutzer:innen auf dem Braze-Dashboard sehen können und hat keinen Einfluss darauf, wie die Daten der Endnutzer:innen in solchen PII-Feldern behandelt werden.

Wenden Sie sich an Ihr juristisches Team, um die Einstellungen Ihres Dashboards mit den für Ihr Unternehmen geltenden Datenschutzbestimmungen und -richtlinien abzustimmen, einschließlich derjenigen, die sich auf die [Bindung von Daten]({{site.baseurl}}/api/data_retention/) beziehen.

#### Freigabe eines Berichts-Builders Download-Links

Sie können [einen Dashboard-Link]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) zum Bericht [freigeben]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report), indem Sie **Freigeben** auswählen und dann **einen Link freigeben** oder **eine E-Mail senden oder einen Zeitplan erstellen**.

### Kreativität entfesseln

#### Angepasste Head Tags für Drag-and-Drop-E-Mails

Verwenden Sie `<head>` Tags, um CSS und Metadaten in Ihrer E-Mail Nachricht hinzuzufügen. Sie können diese Tags beispielsweise verwenden, um ein Stylesheet oder ein Favicon hinzuzufügen. Liquid wird in `<head>` Tags unterstützt.

### Robuste Kanäle

#### Unscharfe Out-Out-Best-Practices

Wir haben einen [Abschnitt mit bewährten Verfahren]({{site.baseurl}}) hinzugefügt, der Ihnen dabei hilft, Ihre unscharfe Opt-out Nachricht sorgfältig zu konfigurieren und eine klare, konforme und positive Nachricht für Ihre Abonnenten zu erstellen.

#### WhatsApp-Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) ist eine Erweiterung des bestehenden WhatsApp-Kanals, die es Ihnen erlaubt, interaktive und dynamische Messaging-Erlebnisse zu erstellen. 

#### Eingehende Fragen zu Produkten per WhatsApp

Nutzer:innen können auf Ihre Nachrichten zu Produkten oder Katalogen mit [Fragen zum Produkt]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions) antworten. Diese gehen als eingehende Nachrichten ein, die dann mit einem Aktions-Pfad sortiert werden können.

Außerdem extrahiert Braze die ID des Produkts und des Katalogs aus diesen Fragen. Wenn Sie also Antworten automatisieren oder Fragen an ein anderes Team (z.B. den Kundensupport) senden möchten, können Sie diese Details mit einbeziehen.

### KI und ML Automatisierung

#### Neue BrazeAI™ Artikel über Anwendungsfälle

Wir haben neue Artikel zu Anwendungsfällen hinzugefügt, die Ihnen helfen, das Beste aus BrazeAI™ herauszuholen. Diese Leitfäden zeigen praktische Möglichkeiten auf, wie Sie KI für Ihre Strategien zum Engagement einsetzen können, darunter:

- Voraussichtliche Abwanderung Identifizieren Sie abwandernde Kund:innen und ergreifen Sie frühzeitig Maßnahmen.
- Voraussichtliche Events Antizipieren Sie wichtige Nutzer:innen-Aktionen und gestalten Sie Erlebnisse in Realtime.
- [Empfehlungen]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Liefern Sie relevantere Inhalte und Produkte auf der Grundlage des Kundenverhaltens.

#### MCP Server

{% multi_lang_include release_type.md release="Beta" %}

Der [Braze MCP Server]({{site.baseurl}}/user_guide/brazeai/mcp_server/), eine sichere und schreibgeschützte Verbindung, ermöglicht KI-Tools wie Claude und Cursor den Zugriff auf nicht PII-geschützte Daten von Braze, um Fragen zu beantworten, Trends zu analysieren und Insights zu liefern, ohne die Daten zu verändern.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Erweitert die Funktionalität von `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`, um bei "Optionalen" Authentifizierungsfehlern ausgelöst zu werden.
        - Die Delegate-Methode `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` wird jetzt sowohl bei "Erforderlichen" als auch bei "Optionalen" Authentifizierungsfehlern ausgelöst.
        - Wenn Sie nur "Erforderliche" SDK-Authentifizierungsfehler behandeln möchten, fügen Sie in Ihrer Implementierung dieser Delegate-Methode eine Prüfung hinzu, die sicherstellt, dass `BrazeSDKAuthError.optional` falsch ist.
    - Korrigiert die Verwendung von `Braze.Configuration.sdkAuthentication`, damit sie bei Enablement wirksam wird.
        - Zuvor wurde der Wert dieser Konfiguration vom SDK nicht verbraucht und das Token wurde immer an Anfragen angehängt, wenn es vorhanden war.
        - Jetzt fügt das SDK das SDK-Authentifizierungstoken nur dann an ausgehende Netzwerkanfragen an, wenn diese Konfiguration Enablement aktiviert ist.
    - Die Setter für alle Eigenschaften von `Braze.FeatureFlag` und alle Eigenschaften von `Braze.Banner` wurden zu `private`. Die Eigenschaften dieser Klassen sind jetzt schreibgeschützt.
    - Entfernt die Eigenschaft `Braze.Banner.id`, die in der Version `11.4.0` veraltet ist.
        - Verwenden Sie stattdessen `Braze.Banner.trackingId`, um die Tracking ID eines Banners zu lesen.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Update der nativen Android SDK Versionsbindungen von [Braze Android SDK 36.0.0 auf 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen Swift SDK Versionsbindungen von [Braze Swift SDK 12.0.0 auf 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Das Ereignis `sdkAuthenticationError` triggert jetzt sowohl für "Erforderliche" als auch für "Optionale" Authentifizierungsfehler.
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Unterstützung für .NET 9.0 für die iOS- und Android-Bindings wurde hinzugefügt.
        - Dadurch wird die Unterstützung für .NET 8.0 entfernt.
        - Dies erfordert eine [Mindestversion von iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Update der Android-Bindung von [Braze Android 32.0.0 auf 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der iOS-Bindung von [Braze Swift SDK 10.0.0 auf 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Diese Version enthält APIs für das Feature Banner, wird aber derzeit von diesem SDK nicht vollständig unterstützt. Wenn Sie Banner in Ihrer .NET MAUI App verwenden möchten, wenden Sie sich an Ihren Kunden:in, bevor Sie die Integration in Ihre Anwendung vornehmen.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Update der internen iOS-Implementierung der Methode `enableSdk`, um `setEnabled`: statt `_requestEnableSDKOnNextAppRun` zu verwenden, die im Swift SDK veraltet war.
    - Wenn Sie diese Methode aufrufen, muss die App nicht mehr neu gestartet werden, um wirksam zu werden. Das SDK wird nun aktiviert, sobald diese Methode ausgeführt wird.
    - Update der nativen Android-Bridge von [Braze Android SDK `36.0.0` auf `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Veröffentlichung am 22\. Juli 2025

### Export von Sicherheitsereignissen mit Amazon S3

Sie können Sicherheitsereignisse mit einem täglichen Job, der um Mitternacht UTC ausgeführt wird, automatisch zu Amazon S3, einem Cloud-Speicheranbieter, exportieren. Einmal eingerichtet, müssen Sie die Sicherheitsereignisse nicht mehr manuell aus dem Dashboard exportieren.

### Flexibilität der Daten

#### CSV-Import

{% multi_lang_include release_type.md release="General availability" %}

Sie können den CSV-Nutzerimport verwenden, um Nutzer:innen-Attribute und angepasste Events in Braze zu erfassen und zu aktualisieren, z.B. `first_name`, `last_destination_searched`, und `trip_booked`. Um loszulegen, siehe [CSV-Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### API-Nutzungsmeldungen

{% multi_lang_include release_type.md release="General availability" %}

API-Nutzungswarnungen bieten einen wichtigen Einblick in Ihre API-Nutzung und ermöglichen es Ihnen, unerwarteten Datenverkehr proaktiv zu erkennen. Indem Sie diese Warnmeldungen einrichten, um das Volumen wichtiger API-Anfragen zu verfolgen, können Sie Realtime-Benachrichtigungen erhalten und Probleme angehen, bevor sie sich auf Ihre Kampagnen auswirken.

#### Workspace API Rate-Limits

Mit Rate-Limits für Workspace-APIs können Sie eine maximale Anzahl von API-Anfragen festlegen, die ein Workspace an einen bestimmten Endpunkt für die Datenaufnahme stellen kann, z. B. `/users/track` oder SDK-Daten. Sie können Rate-Limits auch auf eine Gruppe von Workspaces anwenden, d.h. das Limit wird auf alle Workspaces in dieser Gruppe angewendet.

#### Neue Currents Veranstaltungen

Diese neuen Ereignisse wurden in das Currents-Glossar aufgenommen:

- [Banner Abbruchereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Banner Klick-Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Banner Impressionen Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Banner Gesehene Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook-Ausfallereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Standard-Zeitspanne für Kampagnen-Analytics

Standardmäßig ist der Zeitbereich für [**Kampagnen Analytics**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) die letzten 90 Tage ab dem aktuellen Zeitpunkt an. Das heißt, wenn die Kampagne vor mehr als 90 Tagen gestartet wurde, werden die Analytics für den angegebenen Zeitraum als "0" angezeigt. Um alle Analytics für ältere Kampagnen anzuzeigen, passen Sie den Berichtszeitraum an.

#### Aktualisiertes Verhalten für den Schritt Canvas-Experiment-Pfade

Wenn Ihr Canvas ein aktives oder laufendes Experiment enthält und Sie das aktive Canvas aktualisieren (auch wenn es sich nicht um den Experiment-Pfad-Schritt handelt), wird das laufende Experiment beendet. Um das Experiment neu zu starten, können Sie den bestehenden Experiment-Pfad trennen und einen neuen starten, oder Sie duplizieren das Canvas und starten ein neues Canvas. 

Weitere Informationen finden Sie unter [Bearbeiten von Leinwänden nach dem Start]({{site.baseurl}}/post-launch_edits/).

#### Schnelleres Rate-Limit für `/users/export/ids` Endpunkt verfügbar

Sie können auch das [Rate-Limits für den Endpunkt /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) auf 40 Anfragen pro Sekunde erhöhen, wenn Sie die folgenden Voraussetzungen erfüllen:

- In Ihrem Workspace ist das Standard Rate-Limits (250 Anfragen pro Minute) aktiviert. Wenden Sie sich an Ihren Braze-Konto Manager:in, um weitere Unterstützung bei der Aufhebung eines bereits bestehenden Rate-Limits zu erhalten.
- Ihre Anfrage enthält den Parameter fields_to_export, um alle Felder aufzulisten, die Sie erhalten möchten.

#### Neue Übersetzung für E-Mail Templates an Endpunkten

{% multi_lang_include release_type.md release="Early access" %}

Verwenden Sie diese Endpunkte, um Übersetzungen und Lokalisierungen für E-Mail Templates anzuzeigen und zu aktualisieren:

- [GET / Sehen Sie sich die Quellübersetzungen an]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET / Anzeigen einer bestimmten Übersetzung und Lokalisierung für den Endpunkt der E-Mail-Vorlage
- [GET / Alle Übersetzungen und Lokalisierungen für eine E-Mail-Vorlage anzeigen
- [PUT: Update der Übersetzungen für ein E-Mail Template

### Kreativität entfesseln

#### Landing Pages

Sie können Ihre Landing Page [responsiv an die Größe des Geräts eines Nutzers]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page): [innen]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) anpassen, indem Sie die Spalten auf kleineren Bildschirmen vertikal stapeln. Um dies zu aktivieren, fügen Sie eine Spalte in die Zeile ein, die responsiv sein soll, und schalten Sie dann im Bereich **Spalten anpassen** die Option **Vertikal stapeln auf kleineren Bildschirmen** um.

### Robuste Kanäle

#### Bot-Filter für E-Mails

{% multi_lang_include release_type.md release="General availability" %}

Richten Sie in Ihren [E-Mail-Einstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) einen Bot-Filter ein, um alle mutmaßlichen Maschinen- oder Bot-Klicks auszuschließen. Ein "Bot-Klick" in E-Mails bezieht sich auf einen Klick auf Hyperlinks innerhalb einer E-Mail, die von einem automatisierten Programm generiert wurde. Indem Sie diese Bot-Klicks filtern, können Sie Nachrichten absichtlich triggern und an Empfänger:in zustellen, die engagiert sind.

#### Produktblöcke per Drag-and-Drop verschieben

{% multi_lang_include release_type.md release="Early access" %}

Mit dem Drag-and-Drop-Editor können Sie Ihren Nachrichten schnell Produktblöcke hinzufügen und konfigurieren, um Produkte nahtlos zu präsentieren, ohne dass Sie angepassten Liquid Code erstellen müssen. Das Drag-and-Drop Feature für Produktblöcke ist derzeit nur für E-Mails verfügbar.

#### Textbereich für Landing Pages und In-App-Nachrichten

Mit Span Text können Sie Textblöcke ohne angepassten Code für Ihre [Landing Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) und [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks) mit einem speziellen Stilelement versehen. Markieren Sie dazu den Text, den Sie formatieren möchten, und wählen Sie **Umbruch mit Spanne als Stil** aus. 

#### Anzeige Klick auf WhatsApp

[Ads That Click to WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) sind ein effizienter Weg, um neue und bestehende Kund:innen über Meta-Anzeigen auf Facebook, Instagram oder anderen Plattformen zu gewinnen. Nutzen Sie diese Anzeigen, um für Ihre Produkte und Serviceleistungen zu werben und Nutzer:innen auf Ihre WhatsApp-Präsenz aufmerksam zu machen. 

### Neue Braze Partnerschaften

#### Shopify Visitory API - E-Commerce

Braze sammelt über In-Browser-Nachrichten Informationen über Besucher, wie z.B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden dann an Shopify gesendet. Diese Daten helfen Händlern, die Besucher ihres Shops zu erkennen und ein personalisiertes Einkaufserlebnis zu schaffen.

#### Okendo - E-Commerce

Die Integration von Braze und [Okendo]({{site.baseurl}}/partners/okendo/) funktioniert über mehrere Produkte der Okendo-Plattform, darunter Bewertungen, Loyalität, Empfehlungen, Umfragen und Quizze. Okendo sendet angepasste Events und Nutzer-Attribute an Braze, die zur Personalisierung und zum Triggern von Nachrichten verwendet werden können.

#### Lemnisk - Customer Data Platform

Die Integration von Braze und [Lemnisk]({{site.baseurl}}/partners/lemnisk/) erlaubt es Marken und Unternehmen, das volle Potenzial von Braze auszuschöpfen, indem sie als CDP-geführte Intelligenzschicht fungiert, die Nutzerdaten plattformübergreifend in Realtime zusammenführt und die gesammelten Nutzer:innen-Informationen und Verhaltensdaten in Echtzeit an Braze sendet.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [Internet SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Die Eigenschaft `Banner.html` sowie die Methoden `logBannerClick` und `logBannerImpressions` wurden entfernt. Verwenden Sie stattdessen [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) das automatisch das Tracking von Impressionen und Klicks übernimmt.
    - Die Unterstützung für das alte Feature Newsfeed wurde entfernt. Dazu gehört das Entfernen der Klasse Feed und der zugehörigen Methoden.
    - Die Felder Erstellt und Kategorien, die von den alten Newsfeed-Karten verwendet wurden, wurden aus den [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) Unterklassen entfernt.
    - Das Feld linkText wurde auch aus der Unterklasse [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) Card Unterklasse und ihrem Konstruktor entfernt.
    - Die Definitionen wurden geklärt und die Typen aktualisiert, um zu vermerken, dass bestimmte SDK-Methoden explizit undefiniert zurückgeben, wenn das SDK nicht initialisiert ist, wodurch die Typisierungen an das tatsächliche Laufzeitverhalten angepasst wurden. Dies könnte zu neuen TypeScript-Fehlern in Projekten führen, die sich auf die früheren (unvollständigen) Typisierungen verlassen.
    - Die Bilder von In-App-Nachrichten mit `cropType` von `CENTER_CROP` (wie z.B. `FullScreenMessage` standardmäßig) werden jetzt über einen `<img>` Tag anstelle von `<span>` wiedergegeben, um die Zugänglichkeit zu verbessern. Dies kann dazu führen, dass bestehende CSS-Anpassungen für die Klasse `.ab-center-cropped-img` oder ihre Unterklassen nicht mehr funktionieren.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Update der internen iOS-Implementierung der Methode `enableSdk` zur Verwendung von setEnabled: anstelle von `_requestEnableSDKOnNextAppRun`, die im Swift SDK veraltet war.
        - Wenn Sie diese Methode aufrufen, muss die App nicht mehr neu gestartet werden, um wirksam zu werden. Das SDK wird nun aktiviert, sobald diese Methode ausgeführt wird.
    - Update der nativen Android Bridge von [Braze Android SDK 36.0.0 auf 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
{% details June 24, 2025 %}

## Juni 24, 2025 Veröffentlichung

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) ersetzt A/B-Tests durch KI-Entscheidungen, die alles personalisieren und jede Metrik maximieren: Treiben Sie Dollars an, nicht Klicks - mit BrazeAI Decisioning Studio™ können Sie jeden geschäftlichen KPI optimieren. In unserem Abschnitt [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) finden Sie Beispiele für Anwendungsfälle und wichtige Features.

### Neue SDK-Tutorials

Jedes Braze SDK-Tutorial bietet eine Schritt-für-Schritt-Anleitung mit vollständigem Code-Beispiel. Wählen Sie unten ein Tutorial, um loszulegen:

- [Anzeigen von Bannern]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Anpassen des Stils von In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Bedingte Anzeige von In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Aufschieben von getriggerten In-App-Nachrichten]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilität der Daten

#### SAML Just-in-Time-Bereitstellung

{% multi_lang_include release_type.md release="General availability" %}

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

{% multi_lang_include release_type.md release="General availability" %}

Verwenden Sie die [Zugänglichkeitstests]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) in Inbox Vision, um Probleme mit der Zugänglichkeit Ihrer E-Mails aufzuzeigen. 

Bei den Zugänglichkeitstests wird Ihr E-Mail-Inhalt anhand einiger Anforderungen der [Web Content Accessibility Guidelines](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA analysiert. Dies kann Insights darüber liefern, welche Elemente nicht den Zugänglichkeitsstandards entsprechen.

#### Klick Tracking für WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Sie können das [Tracking von Klicks]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) sowohl in Response- als auch in Template-Nachrichten aktivieren, um die Daten von Klicks in Ihren WhatsApp Performance-Berichten zu sehen und die Nutzer:innen anhand der Klicks zu segmentieren.

#### Videos für WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Sie können bei ausgehenden WhatsApp Nachrichten in den Text [Videos einbetten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features). Diese Dateien müssen über eine URL oder in der [Bibliothek von Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library) gehostet werden.

### Neue Braze Partnerschaften

#### Stripe - E-Commerce

Die Integration von Braze und [Stripe]({{site.baseurl}}/partners/stripe) erlaubt es Ihnen, Messaging in Braze auf der Grundlage von Stripe-Ereignissen zu triggern, wie z.B. Beginn der Testphase, Aktivierung des Abos, Kündigung des Abos und mehr.

### SDK Updates

Die folgenden SDK Updates wurden veröffentlicht. Die wichtigsten Updates sind unten aufgeführt; alle anderen Updates finden Sie in den entsprechenden SDK Changelogs.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Update der nativen Android Bridge [von Braze Android SDK 35.0.0 auf 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Update der nativen iOS-Bridge [von Braze Swift SDK 11.6.1 auf 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segmente Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Update des Braze Android SDK [von 35.0.0 auf 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

{% enddetails %}
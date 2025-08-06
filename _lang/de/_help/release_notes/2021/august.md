---
nav_title: August
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für August 2021."
---

# August 2021

## Google Audience Sync

Die Braze [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) Integration ermöglicht es Marken, die Reichweite ihrer kanalübergreifenden Customer Journeys auf Google Search, Google Shopping, Gmail, YouTube und Google Display auszudehnen. Mithilfe Ihrer First-Party-Daten von Kund:in können Sie Anzeigen auf der Grundlage von dynamischen Verhaltenstriggern, Segmentierung und mehr sicher zustellen. Jedes Kriterium, das Sie normalerweise zum Triggern einer Nachricht (z. B. Push, E-Mail, SMS usw.) im Rahmen eines Braze-Canvas verwenden, kann verwendet werden, um eine Anzeige für diesen Nutzer:innen über Googles Customer Match auszulösen.

## Leitfaden für die iOS SDK-Integration

Dieser optionale [SDK-Leitfaden für die iOS-Integration]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk) führt Sie Schritt für Schritt durch die besten Vorgehensweisen bei der ersten Integration des iOS SDK und seiner Kernkomponenten in Ihre Anwendung. Diese Anleitung hilft Ihnen bei der Erstellung einer `BrazeManager.swift`-Hilfsdatei, die alle Abhängigkeiten vom Braze iOS SDK vom Rest Ihres produktiven Codes entkoppelt, was eine gemeinsamen `import AppboyUI` in Ihrer gesamten Anwendung bewirkt. Dieser Ansatz vermeidet Probleme, die durch übermäßige SDK-Importe entstehen, und erleichtert das Tracking, Debugging und Ändern von Code. 

## voraussichtliche Käufe

Voraussichtliche Käufe geben Marketern ein leistungsstarkes Tool zur Identifizierung und zum Messaging von Nutzern:innen auf der Grundlage ihrer Kaufwahrscheinlichkeit. Wenn Sie eine Prognose für einen Kauf erstellen, trainiert Braze ein Modell des maschinellen Lernens mit Hilfe von [gradientenverstärkten Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um aus früheren Käufen zu lernen und zukünftige Käufe vorherzusagen. Besuchen Sie unser Dokument [Voraussichtliche Käufe]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/), um mehr zu erfahren. 

## Drag-and-Drop-Editor

Mit Braze Email können Sie mithilfe unserer neuen [Drag-and-Drop-Bearbeitungsfunktion]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/) vollständig angepasste und personalisierte Nachrichten in Kampagnen oder Canvase erstellen. Nutzer:innen können jetzt Editor-Blöcke in ihre E-Mails ziehen, was eine intuitivere Anpassung ermöglicht. 

## Nutzer:in alias import

Um Nutzer:innen zusammenzustellen, die keinen `external_id` haben, können Sie [eine Liste von Nutzer:innen mit User-Aliasing importieren]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias). Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Es kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer:innen zu vermarkten, die sich nicht bei Ihrer App registriert oder ein Konto erstellt haben. 

## iOS 15 upgraden Anleitung

Diese [iOS 15 Upgrade-Anleitung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) beschreibt die Änderungen, die mit iOS 15 (WWDC21) eingeführt wurden, sowie die erforderlichen Upgrade-Schritte für Ihre Braze iOS SDK-Integration.

## Android 12 Upgrade-Anleitung

Diese [Android 12-Upgrade-Anleitung]({{site.baseurl}}/developer_guide/platforms/android/android_13/) beschreibt die relevanten Änderungen, die mit Android 12 (2021) eingeführt wurden, sowie die erforderlichen Upgrade-Schritte für Ihre Braze Android SDK-Integration.

## A2P 10DLC

A2P 10DLC bezieht sich auf ein System in den Vereinigten Staaten, das es Unternehmen ermöglicht, Nachrichten vom Typ Application-to-Person (A2P) über einen standardmäßigen 10-stelligen langen Code (10DLC) zu versenden. 10-stellige lange Codes wurden traditionell für den Person-to-Person (P2P)-Verkehr entwickelt, was dazu führte, dass Unternehmen durch einen begrenzten Durchsatz und verstärkte Filterung behindert wurden. Dieser Dienst trägt dazu bei, diese Probleme zu lösen, indem er die Zustellbarkeit von Nachrichten insgesamt verbessert, es Marken erlaubt, Nachrichten in großem Umfang zu versenden, einschließlich Links und Aufforderungen zum Handeln, und Verbraucher:in vor unerwünschten Nachrichten schützt. 

Alle Kund:innen, die derzeit US-Langcodes haben und/oder verwenden, um an US-Kund:innen zu versenden, müssen ihre Langcodes für 10DLC registrieren. Wenn Sie mehr über die Besonderheiten von 10DLC erfahren möchten und warum es erforderlich ist, besuchen Sie unseren speziellen [10DLC-Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Zwei-Faktor-Authentifizierung zurücksetzen

Nutzer:innen, die Probleme bei der Anmeldung über die Zwei-Faktor-Authentifizierung haben, können sich an die Administratoren ihres Unternehmens wenden, um [ihre Zwei-Faktor-Authentifizierung zurückzusetzen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset).

## Neue Braze Partnerschaften

### Hightouch - Automatisierung von Arbeitsabläufen

Die Integration von Braze und [Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/) erlaubt es Ihnen, bessere Kampagnen auf Braze mit aktuellen Kundendaten aus Ihrem Data Warehouse zu erstellen. Sie möchten Ihren Kunden relevante, zeitnahe Interaktionen bieten, und dies hängt in hohem Maße davon ab, dass die Daten in Ihrem Braze-Konto genau und aktuell sind. Durch die automatische Synchronisierung von Kundendaten aus Ihrem Data Warehouse mit Braze müssen Sie sich nicht mehr um die Datenkonsistenz kümmern und können sich auf den Aufbau von Kundenerlebnissen von Weltklasse konzentrieren.

### Transcend - Datenschutz & Compliance

Die Partnerschaft von Braze und [Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/) hilft Nutzern:innen bei der Automatisierung von Anfragen zum Datenschutz durch Orchestrierung von Daten in Dutzenden von Datensystemen. Letztendlich hilft dies den Teams bei der Einhaltung von Vorschriften wie DSGVO und CCPA und gibt dem Einzelnen die Kontrolle über seine Daten.

### Tinyclues - Kohorten-Import

[Tinyclues]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/) ist ein Feature zum Aufbau von Zielgruppen, das die Möglichkeit bietet, die Anzahl der Kampagnen und den Umsatz zu erhöhen, ohne das Kundenerlebnis zu beeinträchtigen, sowie Analytics, um die Performance von CRM-Kampagnen sowohl online als auch offline zu verfolgen. Gemeinsam bietet die Integration von Braze und Tinyclues Nutzern:innen einen Weg zu einer besseren CRM-Planung und -Strategie, die es ihnen erlaubt, mehr Targeting-Kampagnen zu versenden, neue Produkt Opportunitäten zu finden und den Umsatz zu steigern, indem sie ein unglaublich benutzerfreundliches UI verwendet.

### optilyz - Direkt-Mailing

[optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/) ist eine Plattform für die Automatisierung von Direkt-Mailings, mit der Sie kundenorientierte, nachhaltige und profitable Direkt-Mailing-Kampagnen durchführen können. optilyz wird von Hunderten von Unternehmen in ganz Europa eingesetzt und ermöglicht es Ihnen, Briefe, Postkarten und Selfmailer in Ihr kanalübergreifendes Marketing zu integrieren und Kampagnen zu automatisieren und besser zu personalisieren. Nutzen Sie die Integration von Optilyz und Braze-Webhooks, um Direkt-Mailings an Ihre Kund:in zu versenden.
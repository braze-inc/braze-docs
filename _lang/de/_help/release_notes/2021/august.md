---
nav_title: August
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für August 2021."
---

# August 2021

## Google Audience Sync

Die Braze [Audience Sync to Google-Integration]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) ermöglicht es Marken, die Reichweite ihrer kanalübergreifenden Customer Journeys auf Google Search, Google Shopping, Gmail, YouTube und Google Display auszudehnen. Mithilfe Ihrer Erstkunden-Daten können Sie auf sichere Weise Anzeigen auf der Grundlage dynamischer verhaltensbezogener Auslöser, Segmentierung und mehr schalten. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (z. B. Push, E-Mail, SMS usw.) im Rahmen eines Braze Canvas verwenden, kann zum Auslösen einer Anzeige für diesen Nutzer über Googles Customer Match verwendet werden.

## Anleitung zur Integration des iOS SDK

Dieser optionale [Leitfaden für die Integration des iOS SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewios_sdk_integration/) führt Sie Schritt für Schritt durch die besten Vorgehensweisen bei der ersten Integration des iOS SDK und seiner Kernkomponenten in Ihre Anwendung. Diese Anleitung hilft Ihnen bei der Erstellung einer `BrazeManager.swift` Hilfedatei, die alle Abhängigkeiten vom Braze iOS SDK vom Rest Ihres Produktionscodes entkoppelt, was zu einer `import AppboyUI` in Ihrer gesamten Anwendung führt. Dieser Ansatz schränkt Probleme ein, die durch übermäßige SDK-Importe entstehen, und erleichtert die Nachverfolgung, Fehlersuche und Änderung von Code. 

## Prädiktive Käufe

Mit Predictive Purchases erhalten Marketingspezialisten ein leistungsfähiges Tool zur Identifizierung und Ansprache von Nutzern auf der Grundlage ihrer Kaufwahrscheinlichkeit. Wenn Sie eine Kaufvorhersage erstellen, trainiert Braze ein maschinelles Lernmodell mit [Gradient-Boosted-Entscheidungsbäumen](https://en.wikipedia.org/wiki/Gradient_boosting), um aus früheren Kaufaktivitäten zu lernen und zukünftige Kaufaktivitäten vorherzusagen. Besuchen Sie unser Dokument über [vorausschauende Einkäufe]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/), um mehr zu erfahren. 

## Drag-and-Drop-Editor

Mit Braze Email können Sie völlig individuelle und personalisierte E-Mail-Nachrichten entweder in Kampagnen oder Canvases erstellen, indem Sie unsere neue [Drag-and-Drop-Bearbeitungsfunktion]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/) nutzen. Benutzer können jetzt Editorblöcke in ihre E-Mails ziehen, was eine intuitivere Anpassung ermöglicht. 

## Benutzer-Alias-Import

Um Benutzer anzusprechen, die keinen `external_id` haben, können Sie [eine Liste von Benutzern mit Benutzer-Alias importieren]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias). Ein Alias dient als alternativer eindeutiger Benutzeridentifikator. Das kann hilfreich sein, wenn Sie versuchen, anonyme Nutzer anzusprechen, die sich nicht bei Ihrer App angemeldet oder ein Konto erstellt haben. 

## iOS 15 Upgrade Anleitung

Diese [iOS 15 Upgrade-Anleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/) beschreibt die Änderungen, die mit iOS 15 (WWDC21) eingeführt wurden, und die erforderlichen Upgrade-Schritte für Ihre Braze iOS SDK-Integration.

## Android 12 Upgrade-Anleitung

Diese [Android 12 Upgrade-Anleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/) beschreibt die relevanten Änderungen, die mit Android 12 (2021) eingeführt wurden, und die erforderlichen Upgrade-Schritte für Ihre Braze Android SDK-Integration.

## A2P 10DLC

A2P 10DLC bezieht sich auf ein System in den Vereinigten Staaten, das es Unternehmen ermöglicht, Nachrichten vom Typ Application-to-Person (A2P) über eine standardmäßige 10-stellige lange Vorwahlnummer (10DLC) zu versenden. 10-stellige lange Codes wurden traditionell für den Person-to-Person (P2P)-Verkehr entwickelt, was dazu führte, dass Unternehmen durch einen begrenzten Durchsatz und verstärkte Filterung behindert wurden. Dieser Service trägt dazu bei, diese Probleme zu lösen, indem er die Zustellbarkeit von Nachrichten insgesamt verbessert, es Marken ermöglicht, Nachrichten in großem Umfang zu versenden, einschließlich Links und Aufforderungen zum Handeln, und dazu beiträgt, die Verbraucher vor unerwünschten Nachrichten zu schützen. 

Alle Kunden, die derzeit US-Langcodes haben und/oder verwenden, um an US-Kunden zu senden, müssen ihre Langcodes für 10DLC registrieren. Wenn Sie mehr über die Besonderheiten von 10DLC erfahren möchten und warum es erforderlich ist, besuchen Sie unseren speziellen [10DLC-Artikel]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).

## Zurücksetzen der Zwei-Faktor-Authentifizierung

Benutzer, die Probleme bei der Anmeldung über die Zwei-Faktor-Authentifizierung haben, können sich an die Administratoren ihres Unternehmens wenden, um [die Zwei-Faktor-Authentifizierung zurückzusetzen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset).

## Neue Lötpartnerschaften

### Hightouch - Automatisierung von Arbeitsabläufen

Die Integration von Braze und [Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) ermöglicht es Ihnen, bessere Kampagnen auf Braze mit aktuellen Kundendaten aus Ihrem Data Warehouse zu erstellen. Sie möchten Ihren Kunden relevante, zeitnahe Interaktionen bieten, und dies hängt in hohem Maße davon ab, dass die Daten in Ihrem Braze-Konto korrekt und aktuell sind. Durch die automatische Synchronisierung von Kundendaten aus Ihrem Data Warehouse mit Braze müssen Sie sich nicht mehr um die Datenkonsistenz kümmern und können sich auf den Aufbau erstklassiger Kundenerlebnisse konzentrieren.

### Transcend - Datenschutz & Compliance

Die Partnerschaft von Braze und [Transcend]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/) hilft Anwendern, Datenschutzanfragen zu automatisieren, indem sie Daten über Dutzende von Datensystemen hinweg orchestrieren. Letztendlich hilft dies den Teams bei der Einhaltung von Vorschriften wie GDPR und CCPA und gibt dem Einzelnen die Möglichkeit, die Kontrolle über seine Daten zu behalten.

### Tinyclues - Kohortenimport

[Tinyclues]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/) ist eine Funktion zum Aufbau von Zielgruppen, die es ermöglicht, die Anzahl der Kampagnen und den Umsatz zu erhöhen, ohne die Kundenerfahrung zu beeinträchtigen, sowie Analysen, um die Leistung von CRM-Kampagnen sowohl online als auch offline zu verfolgen. Zusammen bietet die Integration von Braze und Tinyclues den Benutzern einen Weg zu einer besseren CRM-Planung und -Strategie. So können die Benutzer mithilfe einer unglaublich benutzerfreundlichen Benutzeroberfläche zielgerichtetere Kampagnen versenden, neue Produktmöglichkeiten finden und den Umsatz steigern.

### optilyz - Direktwerbung

[optilyz]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/) ist eine Direktmailing-Automatisierungsplattform, mit der Sie kundenorientiertere, nachhaltigere und profitablere Direktmailing-Kampagnen durchführen können. optilyz wird von Hunderten von Unternehmen in ganz Europa genutzt und ermöglicht es Ihnen, Briefe, Postkarten und Selfmailer in Ihr kanalübergreifendes Marketing zu integrieren und Kampagnen zu automatisieren und besser zu personalisieren. Verwenden Sie die Webhook-Integration von optilyz und Braze, um Direktmailings an Ihre Kunden zu senden.
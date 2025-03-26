---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2020."
---

# September

## Trichter-Berichterstattung

Funnel Reporting bietet einen visuellen Bericht, mit dem Sie die Reise Ihrer Kunden nach Erhalt einer [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/campaign_funnel_report/) oder eines [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports) analysieren können.

## iOS 14 Upgrade Anleitung

In Übereinstimmung mit den Änderungen, die in Apples neuem iOS 14 angekündigt wurden, gibt es einige Braze-bezogene Änderungen und Maßnahmen, die für Braze iOS SDK-Integrationen erforderlich sind. Weitere Informationen finden Sie in dieser [Upgrade-Anleitung]({{site.baseurl}}/ios_14/).

## Änderungen an IDFA und IDFV für iOS 14

In iOS 14 müssen Benutzer entscheiden, ob sie dem Anzeigen-Tracking zustimmen und Apps und Werbenetzwerke ihre IDFA lesen lassen möchten, wenn sie eine App besuchen. Daher besteht die Strategie von Braze darin, stattdessen den "Identifikator für Anbieter" (wie IDFV) zu verwenden, damit Sie die Benutzer weiterhin über verschiedene Geräte hinweg verfolgen können. Weitere Informationen finden Sie in der [iOS 14 Upgrade-Anleitung]({{site.baseurl}}/ios_14/).

## E-Mail-Überprüfung

Dieser neue Prozess zur Überprüfung der E-Mail-Syntax ist ein Upgrade des bestehenden Prozesses von Braze. Dies ist eine Überprüfung, um sicherzustellen, dass die in Braze aktualisierten oder importierten E-Mails korrekt sind. Weitere Informationen finden Sie in [diesen Richtlinien und Hinweisen]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/email_validation).

## Zufälliges Eimer-Benutzer-Ereignis in Currents

Die zufällige Bucket-Nummer (z.B. RBN) kommt jedes Mal vor, wenn ein neuer Benutzer in seinem Arbeitsbereich erstellt wird. Während dieses Ereignisses wird jedem neuen Benutzer eine zufällige Bucket-Nummer zugewiesen, die Sie dann verwenden können, um gleichmäßig verteilte Segmente von zufälligen Benutzern zu erstellen. Verwenden Sie dies, um eine Reihe von zufälligen Bucket-Nummern zu gruppieren und die Leistung Ihrer Kampagnen und Kampagnenvarianten zu vergleichen. Um zu sehen, ob dieses Ereignis für Sie verfügbar ist, werfen Sie einen Blick in das [Glossar der Currents-Veranstaltungen zum Kundenverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/).

## Leinwand-Komponenten - Demnächst erhältlich!

Braze hat vier neue Canvas-Komponenten hinzugefügt, mit denen Sie die Flexibilität und Funktionalität Ihrer Canvases erhöhen können. Diese neuen Komponenten umfassen: [Entscheidungsschritt]({{site.baseurl}}/decision_split/), [Verzögerungsschritt]({{site.baseurl}}/delay_step/), [Messaging-Schritte]({{site.baseurl}}/message_step/) und [Audience Sync mit Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Canvas-Entscheidungsaufteilung, Verzögerung und Benachrichtigungsschritte**<br>Entscheidungs-Splits können verwendet werden, um Canvas-Zweige zu erstellen, je nachdem, ob ein Benutzer einer bestimmten Abfrage entspricht. Mit Verzögerungsschritten können Sie eine eigenständige Verzögerung zu Ihrem Canvas hinzufügen, ohne dass eine entsprechende Nachricht erforderlich ist. Mit den Nachrichtenschritten können Sie eine eigenständige Nachricht an der gewünschten Stelle in Ihrem Canvas-Fluss einfügen.
- **Audience Sync mit Facebook**<br>Mit der Braze Audience Sync to Facebook können Marken die Daten ihrer eigenen Nutzer aus ihrer eigenen Braze-Integration zu Facebook Custom Audiences hinzufügen, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten. Alle Kriterien, die Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze Canvas auf der Grundlage Ihrer Benutzerdaten verwenden, können jetzt dazu verwendet werden, über Custom Audiences eine Anzeige für diesen Benutzer in Facebook auszulösen.

## Empfangene SMS-Ereignisse

Currents wurde eine neue Veranstaltung zum Thema Messaging hinzugefügt. Dieses Ereignis tritt ein, wenn einer Ihrer Benutzer eine SMS an eine Rufnummer in einer Ihrer Braze SMS-Abonnementgruppen sendet. Weitere Informationen finden Sie in unserem [Currents-Glossar zu Nachrichten und Engagement-Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).

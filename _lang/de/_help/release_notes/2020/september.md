---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2020."
---

# September

## Funnel-Berichte

Funnel Reporting bietet einen visuellen Bericht, mit dem Sie die Reisen Ihrer Kund:in nach dem Erhalt einer [Kampagne]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) oder eines [Canvas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) analysieren können.

## iOS 14 upgraden Anleitung

In Übereinstimmung mit den Änderungen, die in Apples neuem iOS 14 angekündigt wurden, gibt es einige Braze-bezogene Änderungen und Artikel, die für Braze iOS SDK-Integrationen erforderlich sind. Weitere Informationen finden Sie in dieser [Anleitung zum Upgraden]({{site.baseurl}}/ios_14/).

## Änderungen an IDFA und IDFV für iOS 14

In iOS 14 müssen Nutzer:innen entscheiden, ob sie dem Tracking von Anzeigen zustimmen und Apps und Werbenetzwerke ihre IDFA lesen lassen wollen, wenn sie eine App besuchen. Daher besteht die Strategie von Braze darin, stattdessen den "Identifier for Vendors" (z.B. IDFV) zu verwenden, damit Sie weiterhin Nutzer:innen über verschiedene Geräte hinweg tracken können. Weitere Informationen finden Sie in der [Anleitung zum Upgrade von iOS 14]({{site.baseurl}}/ios_14/).

## E-Mail-Validierung

Dieser neue Prozess zur Validierung der E-Mail-Syntax ist ein Upgrade des bestehenden Prozesses von Braze. Mit dieser Funktion können Sie überprüfen, ob die in Braze aktualisierten oder importierten E-Mails korrekt sind. Weitere Informationen finden Sie in [diesen Richtlinien und Hinweisen]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

## Zufälliges Bucket Nutzer:innen Ereignis in Currents

Die zufällige Bucket-Nummer (z.B. RBN) erscheint jedes Mal, wenn ein neuer Nutzer:innen in seinem Workspace angelegt wird. Dabei wird jedem neuen Nutze oder jeder neuen Nutzerin eine zufällige Bucket-Nummer zugewiesen, mit der Sie dann gleichmäßig verteilte Segmente aus zufälligen Nutzer:innen erstellen können. Verwenden Sie dies, um eine Reihe von zufälligen Bucket-Nummern zu gruppieren und die Leistung Ihrer Kampagnen und Kampagnenvarianten zu vergleichen. Um zu sehen, ob dieses Event für Sie verfügbar ist, werfen Sie einen Blick in das Currents [Glossar der Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

## Canvas-Komponenten - Demnächst erhältlich!

Braze hat vier neue Canvas-Komponenten hinzugefügt, mit denen Sie die Flexibilität und Funktionalität Ihrer Canvase erhöhen können. Diese neuen Komponenten umfassen: [Decision-Split-Schritt]({{site.baseurl}}/decision_split/), [Verzögerungsschritt]({{site.baseurl}}/delay_step/), [Messaging-Schritte]({{site.baseurl}}/message_step/) und [Audience Sync mit Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Canvas Decision-Split, Verzögerung und Messaging-Schritte**<br>Decision-Splits können verwendet werden, um Canvas-Zweige zu erstellen, je nachdem, ob ein Nutzer:innen einer definierten Abfrage entspricht. Mit Verzögerungsschritten können Sie eine eigenständige Verzögerung zu Ihrem Canvas hinzufügen, ohne dass eine entsprechende Nachricht erforderlich ist. Messaging-Schritte erlauben es Ihnen, eine eigenständige Nachricht an der gewünschten Stelle in Ihrem Canvas-Ablauf einzufügen.
- **Zielgruppe Synchronisierung mit Facebook**<br>Mit der Braze Audience Sync to Facebook können Marken die Daten ihrer eigenen Nutzer:in ihrer eigenen Braze Integration zu Facebook Custom Audiences hinzufügen, um Anzeigen auf der Grundlage von Verhaltenstriggern, Segmentierung und mehr zu liefern. Jedes Kriterium, das Sie normalerweise zum Auslösen einer Nachricht (Push, E-Mail, SMS, Webhook usw.) in einem Braze-Canvas auf der Grundlage Ihrer Nutzerdaten verwenden, kann jetzt dazu verwendet werden, über Custom Audiences eine Anzeige für diesen Nutzer in Facebook auszulösen.

## Eingehende SMS-Ereignisse

Currents wurde ein neues Messaging-Engagement-Ereignis hinzugefügt. Dieses Ereignis tritt ein, wenn einer Ihrer Nutzer:innen eine SMS an eine Rufnummer in einer Ihrer Abo-Gruppen von Braze sendet. Weitere Informationen finden Sie in unserem [Currents-Glossar zu Messaging und Engagement-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

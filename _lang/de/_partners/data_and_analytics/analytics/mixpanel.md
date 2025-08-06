---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel/
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Mixpanel, einer Business Analytics-Plattform, die es Ihnen erlaubt, Mixpanel Kohorten in Braze zu importieren, um Segmente zu erstellen, die für das Targeting von Nutzern:innen in zukünftigen Kampagnen oder Canvase verwendet werden können."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Braze Lernkurse] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/) ist eine Analytics-Plattform für Unternehmen, die es Ihnen erlaubt, Ereignisse aus Mixpanel in andere Plattformen zu exportieren, um tiefere Analysen durchzuführen. Die gesammelten Daten können dann dazu verwendet werden, angepasste Berichte zu erstellen und das Engagement und die Bindung der Nutzer:innen zu messen.

Die Integration von Braze und Mixpanel erlaubt es Ihnen, [Mixpanel Kohorten in Braze zu importieren]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel/mixpanel_cohort_import/), um Braze Segmente zu erstellen, die für das Targeting von Nutzern:innen in zukünftigen Kampagnen oder Canvase verwendet werden können. Sie können Braze-Currents auch nutzen, um [Ihre Braze-Events nach Mixpanel zu exportieren](#data-export-integration) und so tiefere Analytics zu Konversionen, Bindung und Produktnutzung zu erhalten. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Mixpanel Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Mixpanel-Konto](https://mixpanel.com/). |
| Currents | Um Daten zurück in Mixpanel zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Datenexport Integration

Eine vollständige Liste der Ereignisse, die von Braze nach Mixpanel exportiert werden können, finden Sie unten. Alle Ereignisse, die an Mixpanel gesendet werden, enthalten die `external_user_id` des Nutzers:innen als Mixpanel Distinct ID. Zur Zeit sendet Braze keine Ereignisdaten für Nutzer:innen, die ihre `external_user_id` nicht eingestellt haben.

Sie können zwei Arten von Ereignissen in Mixpanel exportieren: [Message-Engagement-Events](#supported-currents-events), bestehend aus den Braze-Events, die direkt mit dem Versand von Nachrichten zusammenhängen, und [Customerverhalten-Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und Käufe, die über die Plattform getrackt werden. Allen angepassten Events ist das Präfix `[Braze Custom Event]` vorangestellt. Angepassten Event-Eigenschaften und Kauf-Event-Eigenschaften wird das Präfix `[Custom event property]` bzw. `[Purchase property]` vorangestellt.

Wenden Sie sich an Ihren Account Manager:in oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Veranstaltungsberechtigungen benötigen.

### Schritt 1: Zugangsdaten für Mixpanel abrufen

Klicken Sie in Ihrem Mixpanel Dashboard in einem neuen oder bestehenden Projekt auf die **Projekteinstellungen**. Hier finden Sie das Geheimnis der Mixpanel API und das Mixpanel Token. Diese Zugangsdaten werden im nächsten Schritt verwendet, um Ihre Currents-Verbindung herzustellen. 

### Schritt 2: Braze-Currents erzeugen

Navigieren Sie in Braze zu \*\*Currents > **\+ Create Current** > **Create Mixpanel Export**. Geben Sie einen Namen für die Integration, eine Kontakt-E-Mail, das Mixpanel API-Geheimnis und das Mixpanel Token in den aufgeführten Feldern an. Als nächstes wählen Sie die Ereignisse aus, die Sie tracken möchten; eine Liste der verfügbaren Ereignisse wird angezeigt. Klicken Sie abschließend auf **Strom starten**.

![Die Braze Mixpanel Currents Seite. Diese Seite enthält Felder für den Namen der Integration, die E-Mail des Kontakts, das API-Geheimnis und das Mixpanel Export-Token. In der unteren Hälfte der Currents-Seite werden die verfügbaren Currents-Ereignisse aufgelistet, die Sie senden können.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab Notiz %}
Lesen Sie die [Dokumente zur Integration](https://help.mixpanel.com/hc/en-us/articles/360001243663) von Mixpanel, um mehr zu erfahren.
{% endtab %}

## Unterstützte Currents Ereignisse

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren zum [Nutzer:innen-Verhalten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) und zum [Engagement für Nachrichten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach Mixpanel:

### Verhaltensweisen
- Angepasstes Event: `users.behaviors.CustomEvent`
- Install-Attribution: `users.behaviors.InstallAttribution`
- Standort: `users.behaviors.Location`
- Kaufen: `users.behaviors.Purchase`
- Deinstallieren: `users.behaviors.Uninstall`
- App (erste Sitzung, Sitzungsende, Sitzungsbeginn)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Abo (globale Statusänderung): `users.behaviors.subscription.GlobalStateChange`
- Abo-Gruppe (Statusänderung): `users.behaviors.subscriptiongroup.StateChange`
  
### Kampagnen
- Abbrechen: `users_campaigns_abort`
- Konversion: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canvas
- Abbrechen: `users_canvas_abort`
- Konversion: `users.canvas.Conversion`
- Eingang: `users.canvas.Entry`
- Exit (angepasste Zielgruppe, aufgeführtes Ereignis)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Experiment Schritt (Konversion, getrennter Eingang)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Nachrichten
- Content-Card (Abbrechen, Klicken, Ablehnen, Impression, Senden)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-Mail (Abbruch, Bounce, Klick, Zustellung, Markasspam, Öffnen, Senden, Softbounce, Abmelden)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- In-App-Nachricht (Abbruch, Klick, Impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Push-Benachrichtigung (Abbruch, Bounce, iOSforeground, Öffnen, Senden)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (Abbruch, Träger senden, Zustellung, Zustellungsfehler, eingehender Empfang, Ablehnung, Senden, Klick auf Kurzlink)
  - `users.messages.sms.Abort`
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.InboundReceive`
  - `users.messages.sms.Rejection`
  - `users.messages.sms.Send`
  - `users.messages.sms.ShortLinkClick`
- Webhook (Abbruch, Senden)
  - `users.messages.webhook.Abort`
  - `users.messages.webhook.Send`
- WhatsApp (Abbruch, Zustellung, Fehlschlag, eingehender Empfang, Lesen, Senden)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  

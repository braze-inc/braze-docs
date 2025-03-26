---
nav_title: Mixpanel
article_title: Mixpanel
alias: /partners/mixpanel_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Mixpanel, einer Plattform für Geschäftsanalysen, die es Ihnen ermöglicht, Mixpanel-Kohorten in Braze zu importieren, um Braze-Segmente zu erstellen, die für die Ausrichtung von Benutzern in zukünftigen Braze-Kampagnen oder Canvases verwendet werden können."
page_type: partner
search_tag: Partner
tool: Currents

---
 
# [![Braze Learning Kurs]](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel

> [Mixpanel](https://mixpanel.com/) ist eine Plattform für Geschäftsanalysen, mit der Sie Ereignisse aus Mixpanel in andere Plattformen exportieren können, um tiefere Analysen durchzuführen. Die gesammelten Daten können dann verwendet werden, um benutzerdefinierte Berichte zu erstellen und das Engagement und die Bindung der Benutzer zu messen.

Die Integration von Braze und Mixpanel ermöglicht es Ihnen, [Mixpanel-Kohorten in Braze zu importieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/mixpanel/), um Braze-Segmente zu erstellen, die für die Ausrichtung von Nutzern in zukünftigen Braze-Kampagnen oder Canvases verwendet werden können. Sie können Braze Currents auch dazu nutzen, [Ihre Braze-Ereignisse nach Mixpanel zu exportieren](#data-export-integration), um tiefere Analysen zu Konversionen, Kundenbindung und Produktnutzung zu erhalten. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Mixpanel-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Mixpanel-Konto](https://mixpanel.com/). |
| Currents | Um Daten zurück in Mixpanel exportieren zu können, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integration des Datenexports

Eine vollständige Liste der Ereignisse, die von Braze zu Mixpanel exportiert werden können, finden Sie unten. Alle Ereignisse, die an Mixpanel gesendet werden, enthalten die `external_user_id` des Benutzers als Mixpanel Distinct ID. Zur Zeit sendet Braze keine Ereignisdaten für Benutzer, die ihre `external_user_id` nicht eingestellt haben.

Sie können zwei Arten von Ereignissen in Mixpanel exportieren: [Message Engagement Events](#supported-currents-events), bestehend aus den Braze Events, die direkt mit dem Versand von Nachrichten zusammenhängen, und [Customer Behavior Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, benutzerdefinierte Ereignisse und Käufe, die über die Plattform verfolgt werden. Allen benutzerdefinierten Ereignissen ist das Kürzel `[Braze Custom Event]` vorangestellt. Benutzerdefinierten Ereigniseigenschaften und Kaufereigniseigenschaften wird das Präfix `[Custom event property]` bzw. `[Purchase property]` vorangestellt.

Wenden Sie sich an Ihren Kundenbetreuer oder eröffnen Sie ein [Support-Ticket][support], wenn Sie Zugang zu weiteren Veranstaltungsberechtigungen benötigen.

### Schritt 1: Mixpanel-Anmeldeinformationen erhalten

Klicken Sie in Ihrem Mixpanel-Dashboard in einem neuen oder bestehenden Projekt auf die **Projekteinstellungen**. Hier finden Sie das Mixpanel-API-Geheimnis und das Mixpanel-Token. Diese Anmeldedaten werden im nächsten Schritt verwendet, um Ihre Currents-Verbindung herzustellen. 

### Schritt 2: Lötstrom erzeugen

Navigieren Sie in Braze zu \*\*Currents > **\+ Create Current** > **Create Mixpanel Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, das Mixpanel-API-Geheimnis und das Mixpanel-Token in die aufgeführten Felder ein. Wählen Sie als nächstes die Ereignisse aus, die Sie verfolgen möchten; eine Liste der verfügbaren Ereignisse wird angezeigt. Klicken Sie abschließend auf **Aktuell starten**.

![Die Seite Braze Mixpanel Currents. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail, das API-Geheimnis und das Mixpanel-Export-Token. In der unteren Hälfte der Seite Currents sind die verfügbaren Currents-Ereignisse aufgeführt, die Sie senden können.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab Notiz %}
In den [Mixpanel-Integrationsdokumenten](https://help.mixpanel.com/hc/en-us/articles/360001243663) erfahren Sie mehr.
{% endtab %}

## Unterstützte Currents-Veranstaltungen

Braze unterstützt den Export der folgenden Daten, die in den Glossaren zu Currents [Benutzerverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) und Ereignissen [zum Nachrichtenverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach Mixpanel:

### Verhaltensweisen
- Benutzerdefiniertes Ereignis: `users.behaviors.CustomEvent`
- Attribution installieren: `users.behaviors.InstallAttribution`
- Standort: `users.behaviors.Location`
- Kaufen: `users.behaviors.Purchase`
- Deinstallieren: `users.behaviors.Uninstall`
- App (erste Sitzung, Sitzungsende, Sitzungsbeginn)
  - `users.behaviors.app.FirstSession`
  - `users.behaviors.app.SessionEnd`
  - `users.behaviors.app.SessionStart`
- Abonnement (globale Zustandsänderung): `users.behaviors.subscription.GlobalStateChange`
- Abonnementgruppe (Statusänderung): `users.behaviors.subscriptiongroup.StateChange`
  
### Kampagnen
- Abbrechen: `users_campaigns_abort`
- Umwandlung: `users.campaigns.Conversion`
- EnrollinControl: `users.campaigns.EnrollInControl`
  
### Canvas
- Abbrechen: `users_canvas_abort`
- Umwandlung: `users.canvas.Conversion`
- Eintrag: `users.canvas.Entry`
- Exit (abgestimmtes Publikum, durchgeführtes Ereignis)
  - `users.canvas.exit.MatchedAudience`
  - `users.canvas.exit.PerformedEvent`
- Experiment Schritt (Umwandlung, Splitterfassung)
  - `users.canvas.experimentstep.Conversion`
  - `users.canvas.experimentstep.SplitEntry`

### Nachrichten
- Inhaltskarte (Abbrechen, Klicken, Verwerfen, Abdruck, Senden)
  - `users.messages.contentcard.Abort`
  - `users.messages.contentcard.Click`
  - `users.messages.contentcard.Dismiss`
  - `users.messages.contentcard.Impression`
  - `users.messages.contentcard.Send`
- E-Mail (Abbruch, Bounce, Klick, Zustellung, Markasspam, Öffnen, Senden, Softbounce, Abbestellen)
  - `users.messages.email.Abort`
  - `users.messages.email.Bounce`
  - `users.messages.email.Click`
  - `users.messages.email.Delivery`
  - `users.messages.email.MarkAsSpam`
  - `users.messages.email.Open`
  - `users.messages.email.Send`
  - `users.messages.email.SoftBounce`
  - `users.messages.email.Unsubscribe`
- In-App-Nachricht (Abbruch, Klick, Eindruck)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Push-Benachrichtigung (Abbruch, Bounce, iOSforeground, Öffnen, Senden)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
  - `users.messages.pushnotification.IosForeground`
  - `users.messages.pushnotification.Open`
  - `users.messages.pushnotification.Send`
- SMS (Abbruch, Träger senden, Zustellung, Zustellungsfehler, eingehender Empfang, Ablehnung, Senden, kurzer Linkklick)
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
- WhatsApp (Abbruch, Zustellung, Fehler, eingehender Empfang, Lesen, Senden)
  - `users.messages.whatsapp.Abort`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.InboundReceive`
  - `users.messages.whatsapp.Read`
  - `users.messages.whatsapp.Send`
  
[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}

---
nav_title: Segmente für Currents
article_title: Segmente für Currents
page_order: 2
alias: /partners/segment_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Segment, einer Customer Data Platform, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segmente für Currents  

> [Segmente](https://segment.com) ist eine Customer Data Platform (CDP), mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. Dieser referenzierte Artikel gibt eine Übersicht über die Verbindung zwischen Braze-Currents und Segmenten und beschreibt die Anforderungen und Prozesse für die richtige Implementierung und Verwendung.

Die Integration von Braze und Segment erlaubt es Ihnen, Braze-Currents zu nutzen, um Ihre Braze-Events nach Segment zu exportieren und so tiefgreifendere Analytics zu Konversionen, Bindung und Produktnutzung zu ermöglichen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segmente Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Braze Ziel | Sie müssen [Braze bereits als Ziel]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) in Ihrer Segment Integration eingerichtet haben.<br><br>Dazu gehört die Angabe des richtigen Braze Datenzentrums und des REST API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Um Daten zurück in Segmente zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Schreibschlüssel für Segmente abrufen

Wählen Sie in Ihrem Dashboard für Segmente Ihre Segmentquelle aus. Gehen Sie dann zu **Einstellungen > API-Schlüssel**. Hier finden Sie den **Schreibschlüssel für Segmente**.

{% alert warning %}
Es ist wichtig, dass Sie Ihren Schreibschlüssel für Segmente auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Erstellen Sie einen neuen Currents Konnektor

1. Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Klicken Sie auf **\+ Neuen Strom erstellen** > **Segment Daten exportieren**.
3. Als nächstes geben Sie den Namen der Integration, die E-Mail des Kontakts, den Schreibschlüssel des Segments und die Region des Segments an.

![Die Seite Segment Currents in Braze. Hier finden Sie Felder für den Namen der Integration, die E-Mail des Kontakts, die Region des Segments und den API-Schlüssel.]({% image_buster /assets/img/segment/segment_currents_integration_config.png %})

### Schritt 3: Nachrichten Engagement Ereignisse exportieren

Wählen Sie dann die Ereignisse für das Engagement in Nachrichten aus, die Sie exportieren möchten. Referenzieren Sie die nachfolgend aufgelisteten Exportereignisse und Eigenschaften. Alle Ereignisse, die an Segmente gesendet werden, enthalten die `external_user_id` des Nutzers:innen als `userId` und die `braze_id` des Nutzers als `anonymousId`.

Denken Sie daran, dass Braze nur dann Ereignisdaten für Nutzer:innen ohne `external_user_id` sendet, wenn die Option **Ereignisse von anonymen Nutzer:innen einbeziehen** aktiviert ist.

{% alert important %}
Der anonyme Nutzer:in-Export befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

![Liste aller verfügbaren Messaging-Ereignisse auf der Seite Segment Currents in Braze.]({% image_buster /assets/img/segment/segment_currents_data_config.png %})

Und schließlich wählen Sie **Launch Current**.

{% alert warning %}
Wenn Sie mehr als einen der gleichen Currents Konnektoren erstellen möchten (z.B. zwei Konnektoren für das Engagement von Nachrichten), müssen sich diese in verschiedenen Workspaces befinden. Da die Braze Segment Currents-Integration Ereignisse von verschiedenen Apps nicht in einem einzigen Workspace isolieren kann, führt dies zu unnötiger Daten-Deduplizierung und Datenverlust.
{% endalert %}

Um mehr zu erfahren, besuchen Sie die [Dokumentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/) Segmentierung.

## Update Ihres Currents

{% multi_lang_include updating_currents.md %}

## Unterstützte Currents Ereignisse

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren zum [Nutzer:innen-Verhalten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) und zum [Messaging-Engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) in Segmente aufgeführt sind:
 
### Verhaltensweisen
- Deinstallieren: `users.behaviors.Uninstall`
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


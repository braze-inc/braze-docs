---
nav_title: Segment für Ströme
article_title: Segment für Ströme
page_order: 2
alias: /partners/segment_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Segment, einer Plattform für Kundendaten, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing-Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# Segment für Ströme  

> [Segment](https://segment.com) ist eine Plattform für Kundendaten, mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. Dieser Referenzartikel gibt einen Überblick über die Verbindung zwischen Braze Currents und Segment und beschreibt die Anforderungen und Prozesse für die ordnungsgemäße Implementierung und Verwendung.

Die Integration von Braze und Segment ermöglicht es Ihnen, Braze Currents zu nutzen, um Ihre Braze-Ereignisse nach Segment zu exportieren und so tiefgreifendere Analysen zu Konversionen, Kundenbindung und Produktnutzung durchzuführen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Ziel löten | Sie müssen [Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) bereits [als Ziel]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) in Ihrer Segment-Integration [eingerichtet]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) haben.<br><br>Dazu gehört die Angabe des richtigen Braze-Rechenzentrums und des REST-API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Um Daten zurück nach Segment zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Segment-Schreibschlüssel abrufen

Wählen Sie in Ihrem Segment-Dashboard Ihre Segment-Quelle aus. Als nächstes gehen Sie zu **Einstellungen > API-Schlüssel**. Hier finden Sie den **Segment Write Key**.

{% alert warning %}
Es ist wichtig, dass Sie Ihren Segment-Schreibschlüssel auf dem neuesten Stand halten. Wenn die Anmeldeinformationen Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Erstellen Sie einen neuen Currents-Anschluss

1. Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**.
2. Klicken Sie auf **\+ Neuen Strom erstellen** > **Segmentdatenexport**.
3. Als nächstes geben Sie einen Integrationsnamen, eine Kontakt-E-Mail, einen Segment-Schreibschlüssel und eine Segment-Region an.

![Die Seite Segment Currents in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, die Segmentregion und den API-Schlüssel.][3]

### Schritt 3: Exportieren von Ereignissen zur Einbindung von Nachrichten

Wählen Sie dann die Ereignisse aus, die Sie exportieren möchten. Beziehen Sie sich auf die nachfolgend aufgelisteten Export-Ereignisse und Eigenschaften. Alle Ereignisse, die an Segment gesendet werden, enthalten die `external_user_id` des Benutzers als `userId`. Zur Zeit sendet Braze keine Ereignisdaten für Benutzer, die ihre `external_user_id` nicht eingestellt haben.

![Liste aller verfügbaren Nachrichtenereignisse auf der Seite Segment Currents in Braze.][2]

Wählen Sie schließlich **Aktuelles starten**.

{% alert warning %}
Wenn Sie mehr als einen der gleichen Currents-Konnektoren erstellen möchten (z. B. zwei Konnektoren für Nachrichten-Ereignisse), müssen sie sich in verschiedenen Arbeitsbereichen befinden. Da die Braze Segment Currents-Integration Ereignisse von verschiedenen Anwendungen in einem einzigen Arbeitsbereich nicht isolieren kann, führt dies zu unnötiger Datenreduzierung und Datenverlust.
{% endalert %}

Um mehr zu erfahren, besuchen Sie die [Segment-Dokumentation](https://segment.com/docs/connections/sources/catalog/cloud-apps/braze/).

## Aktualisieren Ihrer aktuellen

{% multi_lang_include updating_currents.md %}

## Unterstützte Currents-Veranstaltungen

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren zum [Benutzerverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) und zu den Ereignissen [bei der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach Segment:
 
### Verhaltensweisen
- Deinstallieren: `users.behaviors.Uninstall`
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

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}

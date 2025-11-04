---
nav_title: mParticle für Currents
article_title: mParticle für Currents
alias: /partners/mparticle_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und mParticle, einer Kundendaten-Plattform, die Informationen sammelt und zwischen Quellen in Ihrem Marketing Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle für Currents

> [mParticle](https://www.mparticle.com) ist eine Customer Data Platform (CDP), die Daten aus verschiedenen Quellen sammelt und an eine Vielzahl anderer Standorte in Ihrem Marketing Stack weiterleitet.

Die Integration von Braze und mParticle erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern. Mit [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) können Sie auch Daten mit mParticle verbinden, um sie über den gesamten Growth Stack hinweg nutzbar zu machen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in mParticle zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| mParticle Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| mParticle Server-zu-Server Schlüssel und Geheimnis | Diese erhalten Sie, indem Sie zu Ihrem mParticle-Dashboard navigieren und die [erforderlichen Daten-Feeds](#step-1-create-feeds) erstellen, die es mParticle ermöglichen, Braze-Interaktionsdaten für iOS-, Android- und Internet-Plattformen zu empfangen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Über mParticle Zugangsdaten

mParticle verfügt über Zugangsdaten auf App- und Workspace-Ebene, die sich darauf auswirken, wie Ihre Ereignisse gesendet werden.

- **App-Ebene:** mParticle trennt die Ereignisse nach den einzelnen Apps. Das bedeutet, dass die Zugangsdaten, die Sie Ihrer iOS-App geben, nur zum Senden von iOS-spezifischen Ereignissen verwendet werden können.
- **Workspace-Ebene:** mParticle fasst alle Ereignisse zusammen (die **nicht** App-spezifisch sind). Das bedeutet, dass die Zugangsdaten, die Sie Ihrer App-Gruppe auf Workspace-Ebene geben, zum Senden aller nicht App-spezifischen Ereignisse verwendet werden.

Sie können sich das so vorstellen, dass mParticle einen "Feed" für jede einzelne App aufnimmt. Wenn Sie z.B. eine App für iOS, eine für Android und eine für das Internet haben, werden Ihre Ereignisse unzusammenhängend sein. Das heißt, wenn Sie für jede App dieselben Zugangsdaten angeben, wird ein mParticle-Feed verwendet, um alle Daten für alle Ihre Apps zu empfangen, ohne dass es zu Doppelungen kommt.

## Integration

### Schritt 1: Feeds erstellen

Navigieren Sie in Ihrem mParticle-Administratorkonto zu **Einrichtung > Eingaben**. Suchen Sie **Braze** im mParticle **Verzeichnis** und fügen Sie die Feed Integration hinzu.

Die Braze Feed Integration unterstützt vier verschiedene Feeds: iOS, Android, Internet und Unbound. Der ungebundene Feed kann für Ereignisse wie E-Mails verwendet werden, die nicht mit einer Plattform verbunden sind. Sie müssen für jeden Hauptplattform-Feed eine Eingabe erstellen. Sie können unter **Einrichtung > Eingänge** auf dem Tab **Zufuhrkonfigurationen** zusätzliche Eingänge erstellen.

![]({% image_buster /assets/img/braze-feed-inputs.png %})

Wählen Sie für jeden Feed unter **Als Plattform handeln** die passende Plattform aus der Liste aus. Wenn Sie keine Option zum Auswählen eines **act-as-Feeds** sehen, werden die Daten als ungebunden behandelt, können aber dennoch an Data Warehouse-Ausgaben weitergeleitet werden.

![Das erste Dialogfeld für die Integration, in dem Sie aufgefordert werden, einen Konfigurationsnamen anzugeben, einen Feed-Status zu bestimmen und eine Plattform auszuwählen, als die Sie agieren möchten.]({% image_buster /assets/img/braze-feed-act1.png %}){: style="max-width:40%;"}  ![Das zweite Dialogfeld für die Integration, in dem der Server-zu-Server-Schlüssel und das Server-zu-Server-Geheimnis angezeigt werden.]({% image_buster /assets/img/braze-feed-act2.png %}){: style="max-width:37%;"}

Bei der Erstellung jeder Eingabe stellt mParticle Ihnen einen Schlüssel und ein Geheimnis zur Verfügung. Kopieren Sie diese Zugangsdaten und vermerken Sie dabei, für welchen Feed jedes Paar Zugangsdaten bestimmt ist.

### Schritt 2: Currents erzeugen

Navigieren Sie in Braze zu **Currents > + Create Current > Create mParticle Export**. Geben Sie einen Namen für die Integration, eine E-Mail und den mParticle API-Schlüssel und den geheimen mParticle-Schlüssel für jede Plattform an. Als nächstes wählen Sie die Ereignisse aus, die Sie tracken möchten; eine Liste der verfügbaren Ereignisse wird angezeigt. Klicken Sie abschließend auf **Launch Current**

![Die mParticle-Currents Seite in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und den geheimen Schlüssel.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Es ist wichtig, dass Sie Ihren mParticle API-Schlüssel und Ihren mParticle-Geheimschlüssel immer auf dem neuesten Stand halten. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

Alle Ereignisse, die an mParticle gesendet werden, enthalten die `external_user_id` des Nutzers:innen als `customerid`. Zur Zeit sendet Braze keine Ereignisdaten für Nutzer:innen, die ihre `external_user_id` nicht eingestellt haben. Wenn Sie die `external_user_id` einer anderen ID in mParticle zuordnen möchten, die nicht dem Standard `customerid` entspricht, wenden Sie sich bitte an Ihren CSM von Braze. 

## Unterstützte Currents Ereignisse

Braze unterstützt den Export der folgenden Daten, die in den Currents Glossaren zum [Nutzer:innen-Verhalten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) und zum [Engagement für Nachrichten]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach mParticle:

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
- In-App-Nachricht (Abbruch, Klick, Impression)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Push-Benachrichtigung (Abbruch, Bounce, Öffnung, Senden)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


Wenn Sie mehr über die mParticle Integration erfahren möchten, besuchen Sie die Dokumentation [hier](http://docs.mparticle.com/integrations/braze/feed).


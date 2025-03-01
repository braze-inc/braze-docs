---
nav_title: mParticle für Currents
article_title: mParticle für Currents
alias: /partners/mparticle_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und mParticle, einer Plattform für Kundendaten, die Informationen sammelt und zwischen Quellen in Ihrem Marketing-Stack weiterleitet."
page_type: partner
tool: Currents
search_tag: Partner

---

# mParticle für Currents

> [mParticle](https://www.mparticle.com) ist eine Plattform für Kundendaten, die Informationen aus verschiedenen Quellen sammelt und an eine Vielzahl von anderen Stellen in Ihrem Marketing-Stack weiterleitet.

Die Integration von Braze und mParticle ermöglicht Ihnen die nahtlose Steuerung des Informationsflusses zwischen den beiden Systemen. Mit [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) können Sie auch Daten mit mParticle verbinden, um sie über den gesamten Wachstumsstapel hinweg nutzbar zu machen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Currents | Um Daten zurück in mParticle zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
| mParticle Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| mParticle Server-zu-Server Schlüssel und Geheimnis | Diese können Sie erhalten, indem Sie zu Ihrem mParticle-Dashboard navigieren und die [notwendigen Feeds](#step-1-create-feeds) erstellen, die es mParticle ermöglichen, Braze-Interaktionsdaten für iOS-, Android- und Web-Plattformen zu empfangen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Über mParticle Anmeldeinformationen

mParticle verfügt über Anmeldeinformationen auf App- und Arbeitsbereichsebene, die sich darauf auswirken, wie Ihre Ereignisse gesendet werden.

- **App-Ebene:** mParticle trennt die Ereignisse nach jeder einzelnen App. Das bedeutet, dass die Anmeldeinformationen, die Sie Ihrer iOS-App geben, nur zum Senden von iOS-spezifischen Ereignissen verwendet werden können.
- **Arbeitsbereichsebene:** mParticle fasst alle Ereignisse zusammen (die **nicht** app-spezifisch sind), d.h. die Anmeldeinformationen auf Arbeitsbereichsebene, die Sie Ihrer App-Gruppe geben, werden verwendet, um alle Ihre nicht app-spezifischen Ereignisse zu senden.

Sie können sich das so vorstellen, dass mParticle einen "Feed" für jede einzelne App aufnimmt. Wenn Sie z.B. eine App für iOS, eine für Android und eine für das Web haben, werden Ihre Ereignisse unzusammenhängend sein. Das heißt, wenn Sie für jede App dieselben Anmeldedaten angeben, wird ein mParticle-Feed verwendet, um alle Daten für alle Ihre Apps zu empfangen, ohne dass es zu einer Duplizierung kommt.

## Integration

### Schritt 1: Feeds erstellen

Navigieren Sie in Ihrem mParticle-Administratorkonto zu **Einrichtung > Eingaben**. Suchen Sie **Braze** im **mParticle-Verzeichnis** und fügen Sie die Feed-Integration hinzu.

Die Braze-Feed-Integration unterstützt vier verschiedene Feeds: iOS, Android, Web und Unbound. Der ungebundene Feed kann für Ereignisse wie E-Mails verwendet werden, die nicht mit einer Plattform verbunden sind. Sie müssen für jeden Hauptplattform-Feed eine Eingabe erstellen. Sie können zusätzliche Eingänge unter **Einrichtung > Eingänge** auf der Registerkarte **Feed-Konfigurationen** erstellen.

![][1]

Wählen Sie für jeden Feed unter **Als Plattform handeln** die passende Plattform aus der Liste aus. Wenn Sie keine Option zur Auswahl eines **act-as-Feeds** sehen, werden die Daten als ungebunden behandelt, können aber dennoch an Data Warehouse-Ausgaben weitergeleitet werden.

![Das erste Integrationsdialogfeld, in dem Sie aufgefordert werden, einen Konfigurationsnamen anzugeben, einen Feed-Status zu bestimmen und eine Plattform auszuwählen, als die Sie agieren möchten.][2]{: style="max-width:40%;"}  ![Das zweite Integrationsdialogfeld, das den Server-zu-Server-Schlüssel und das Server-zu-Server-Geheimnis anzeigt.][3]{: style="max-width:37%;"}

Bei der Erstellung jeder Eingabe erhalten Sie von mParticle einen Schlüssel und ein Geheimnis. Kopieren Sie diese Zugangsdaten und notieren Sie sich, für welchen Feed jedes Paar von Zugangsdaten gilt.

### Schritt 2: Aktuell erstellen

Navigieren Sie in Braze zu **Currents > + Create Current > Create mParticle Export**. Geben Sie einen Integrationsnamen, eine Kontakt-E-Mail sowie den mParticle API-Schlüssel und den mParticle Geheimschlüssel für jede Plattform an. Wählen Sie als nächstes die Ereignisse aus, die Sie verfolgen möchten; eine Liste der verfügbaren Ereignisse wird angezeigt. Klicken Sie abschließend auf **Aktuelles starten**

![Die Seite mParticle Currents in Braze. Hier finden Sie Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und den geheimen Schlüssel.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Es ist wichtig, dass Sie Ihren mParticle-API-Schlüssel und Ihren mParticle-Geheimschlüssel immer auf dem neuesten Stand halten. Wenn die Anmeldeinformationen Ihres Connectors ablaufen, sendet der Connector keine Ereignisse mehr. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

Alle Ereignisse, die an mParticle gesendet werden, enthalten die `external_user_id` des Benutzers als `customerid`. Zur Zeit sendet Braze keine Ereignisdaten für Benutzer, die ihre `external_user_id` nicht eingestellt haben. Wenn Sie die `external_user_id` einer anderen ID in mParticle zuordnen möchten, die nicht die Standard-ID `customerid` ist, wenden Sie sich bitte an Ihren Braze CSM. 

## Unterstützte Currents-Veranstaltungen

Braze unterstützt den Export der folgenden Daten, die in den Glossaren zum [Currents-Benutzerverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) und zu den Ereignissen [bei der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach mParticle:

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
- In-App-Nachricht (Abbruch, Klick, Eindruck)
  - `users.messages.inappmessage.Abort`
  - `users.messages.inappmessage.Click`
  - `users.messages.inappmessage.Impression`
- Push-Benachrichtigung (Abbruch, Bounce, Öffnen, Senden)
  - `users.messages.pushnotification.Abort`
  - `users.messages.pushnotification.Bounce`
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


Um mehr über die mParticle-Integration zu erfahren, besuchen Sie die Dokumentation [hier](http://docs.mparticle.com/integrations/braze/feed).

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}

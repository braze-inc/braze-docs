---
nav_title: Amplitude für Ströme
article_title: Amplitude für Ströme
page_order: 0
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Amplitude, einer Plattform für Produktanalyse und Business Intelligence."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze Learning Kurs]](https://learning.braze.com/amplitude-integration-with-braze) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude für Ströme

> [Amplitude](https://amplitude.com/) ist eine Plattform für Produktanalytik und Business Intelligence.

Die bidirektionale Integration von Braze und Amplitude ermöglicht es Ihnen, [Ihre Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/), Benutzereigenschaften und Ereignisse mit Braze [zu synchronisieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/) und Braze Currents zu nutzen, um [Ihre Braze-Ereignisse nach Amplitude zu exportieren](#data-export-integration), damit Sie tiefere Analysen Ihrer Produkt- und Marketingdaten durchführen können.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Amplitude Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amplitude-Konto](https://amplitude.com/). |
| Currents | Damit Sie Daten zurück nach Amplitude exportieren können, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integration des Datenexports

Eine vollständige Liste der Ereignisse und Ereigniseigenschaften, die von Braze nach Amplitude exportiert werden können, finden Sie in den folgenden Abschnitten. Alle Ereignisse, die an Amplitude gesendet werden, enthalten die `external_user_id` des Benutzers als Amplitude-Benutzer-ID. Braze-spezifische Ereigniseigenschaften werden unter dem Schlüssel `event_properties` in den an Amplitude gesendeten Daten gesendet.

{% alert important %}
Um diese Funktion zu nutzen, muss Ihre Amplitude-Benutzer-ID mit der externen ID von Braze übereinstimmen.
{% endalert %}

Braze sendet nur Ereignisdaten für Benutzer, die ihre `external_user_id` eingestellt haben, oder anonyme Benutzer, die ihre `device_id` eingestellt haben. Für die anonymen Benutzer müssen Sie Ihre Amplitude-Geräte-ID mit der Braze-Geräte-ID im SDK synchronisieren. Zum Beispiel:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Sie können zwei Arten von Ereignissen nach Amplitude exportieren: [Message Engagement Events](#supported-currents-events), bestehend aus den Braze Events, die direkt mit dem Versand von Nachrichten zusammenhängen, und [Customer Behavior Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, benutzerdefinierte Ereignisse und Käufe, die über die Plattform verfolgt werden. Allen regulären Ereignissen ist das Präfix `[Appboy]` vorangestellt, und allen benutzerdefinierten Ereignissen ist das Präfix `[Appboy] [Custom Event]` vorangestellt. Den Eigenschaften von benutzerdefinierten Ereignissen und Kaufereignissen wird das Präfix `[Custom event property]` bzw. `[Purchase property]` vorangestellt.

Alle Kohorten, die benannt und in Braze importiert werden, werden mit dem Präfix `[Amplitude]` und dem Suffix `cohort_id` versehen. Das bedeutet, dass eine Kohorte mit dem Namen "TEST_COHORT" mit der `cohort_id` "abcd1234" in den Braze-Filtern als `[Amplitude] TEST_COHORT: abcd1234` bezeichnet wird.

Wenden Sie sich an Ihren Kundenbetreuer oder eröffnen Sie ein [Support-Ticket][support], wenn Sie Zugang zu weiteren Veranstaltungsberechtigungen benötigen.

### Schritt 1: Konfigurieren Sie die Amplitudenintegration in Braze 

Suchen Sie in Amplitude nach Ihrem Amplitude Export-API-Schlüssel.

{% alert warning %}
Halten Sie Ihren Amplitude API-Schlüssel auf dem neuesten Stand. Wenn die Anmeldeinformationen Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Lötstrom erzeugen

Navigieren Sie in Braze zu **Ströme > + Strom erstellen > Amplitudenexport erstellen**. Geben Sie in den aufgeführten Feldern einen Integrationsnamen, eine Kontakt-E-Mail, einen Amplitude-Export-API-Schlüssel und eine Amplitude-Region an. Wählen Sie als nächstes die Ereignisse aus, die Sie verfolgen möchten; eine Liste der verfügbaren Ereignisse wird angezeigt. Klicken Sie abschließend auf **Aktuelles starten**

{% alert note %}
Ereignisse, die von Braze Currents an Amplitude gesendet werden, werden auf Ihr Amplitude-Ereigniskontingent angerechnet.
{% endalert %}

![Die Seite Braze Amplitude Currents. Diese Seite enthält Felder für den Integrationsnamen, die Kontakt-E-Mail, den API-Schlüssel und die US-Region. In der unteren Hälfte der Seite Currents sind die verfügbaren Currents-Ereignisse aufgeführt, die Sie senden können.]({% image_buster /assets/img/amplitude4.png %})

{% tab Notiz %}
Lesen Sie die [Integrationsdokumente](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) von Amplitude, um mehr zu erfahren.
{% endtab %}

## Preisgrenzen

Currents stellen eine Verbindung zur HTTP-API von Amplitude her, die eine [Geschwindigkeitsbegrenzung](https://developers.amplitude.com/docs/http-api-v2#upload-limit) von 30 Ereignissen/Sekunde pro Gerät und eine undokumentierte Grenze von 500K Ereignissen/Tag pro Gerät hat. Wenn diese Schwellenwerte überschritten werden, drosselt Amplitude die über Currents protokollierten Ereignisse. Wenn ein Gerät in Ihrer Integration diesen Grenzwert überschreitet, kann es zu einer Verzögerung kommen, wenn Ereignisse von allen Geräten in Amplitude angezeigt werden.

Geräte sollten unter normalen Umständen nicht mehr als 30 Ereignisse/Sekunde oder 500K Ereignisse/Tag melden, und dieses Ereignismuster sollte nur aufgrund einer falsch konfigurierten Integration auftreten. Um diese Art von Verzögerung zu vermeiden, stellen Sie sicher, dass Ihre SDK-Integration Ereignisse in einem normalen Rhythmus meldet, wie in unseren SDK-Integrationsanweisungen angegeben, und verzichten Sie auf automatisierte Tests, die viele Ereignisse für ein einzelnes Gerät erzeugen.

## Unterstützte Currents-Veranstaltungen

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren zum [Benutzerverhalten]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) und zu den Ereignissen [bei der Nachrichtenübermittlung]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach Amplitude:

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

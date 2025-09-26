---
nav_title: Amplitude für Currents
article_title: Amplitude für Currents
page_order: 0
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Amplitude, einer Analytics-Plattform für Produkte und Business-Intelligence."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze-Lernkurs] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude für Currents

> [Amplitude](https://amplitude.com/) ist eine Plattform für Produkt-Analytik und Business-Intelligence.

Die bidirektionale Integration von Braze und Amplitude erlaubt es Ihnen, Ihre [Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/), Benutzermerkmale und Ereignisse mit Braze zu synchronisieren und Braze-Currents zu nutzen, um [Ihre Braze-Ereignisse nach Amplitude zu exportieren](#data-export-integration) und so tiefere Analysen Ihrer Produkt- und Marketingdaten durchzuführen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Amplitude Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amplitude-Konto](https://amplitude.com/). |
| Currents | Um Daten zurück nach Amplitude zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Datenexport Integration

Eine vollständige Liste der Ereignisse und Event-Eigenschaften, die von Braze nach Amplitude exportiert werden können, finden Sie in den folgenden Abschnitten. Alle Ereignisse, die an Amplitude gesendet werden, enthalten die `external_user_id` des Nutzers als Amplitude-Nutzer:in. Braze-spezifische Event-Eigenschaften werden in den Daten, die an Amplitude gesendet werden, unter dem Schlüssel `event_properties` gesendet.

{% alert important %}
Um dieses Feature zu nutzen, muss Ihre Amplitude-Nutzer:in ID mit der externen ID von Braze übereinstimmen.
{% endalert %}

Braze sendet nur Ereignisdaten für Nutzer:in, die ihre `external_user_id` eingestellt haben oder anonyme Nutzer:innen, die ihre `device_id` eingestellt haben. Für anonyme Nutzer:innen müssen Sie Ihre Amplitude-Geräte-ID mit der Braze-Geräte-ID im SDK synchronisieren. Zum Beispiel:

```java
amplitude.setDeviceId(Appboy.getInstance(context).getDeviceId();)
```

Sie können zwei Arten von Ereignissen in Amplitude exportieren: [Message-Engagement-Events](#supported-currents-events), bestehend aus den Braze-Events, die direkt mit dem Versand von Nachrichten zusammenhängen, und [Customerverhalten-Events](#supported-currents-events), einschließlich anderer App- oder Website-Aktivitäten wie Sitzungen, angepasste Events und Käufe, die über die Plattform getrackt werden. Allen regulären Events ist das Präfix `[Appboy]` vorangestellt, allen angepassten Events das Präfix `[Appboy] [Custom Event]`. Angepassten Event- und Kauf-Event-Eigenschaften wird das Präfix `[Custom event property]` bzw. `[Purchase property]` vorangestellt.

Alle Kohorten, die benannt und in Braze importiert werden, werden mit dem Präfix `[Amplitude]` und dem Suffix `cohort_id` versehen. Das bedeutet, dass eine Kohorte mit dem Namen "TEST_COHORT" mit der `cohort_id` "abcd1234" in den Filtern von Braze als `[Amplitude] TEST_COHORT: abcd1234` bezeichnet wird.

Wenden Sie sich an Ihren Account Manager:in oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Veranstaltungsberechtigungen benötigen.

### Schritt 1: Konfigurieren Sie die Amplitude Integration in Braze 

Suchen Sie in Amplitude nach Ihrem API-Schlüssel für den Export von Amplitude.

{% alert warning %}
Halten Sie Ihren Amplitude API-Schlüssel auf dem neuesten Stand. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

### Schritt 2: Braze-Currents erzeugen

Navigieren Sie in Braze zu **Currents > + Create Current > Create Amplitude Export**. Geben Sie den Namen der Integration, eine Kontakt-E-Mail, den API-Schlüssel für den Amplitude-Export und die Amplitude-Region in die aufgeführten Felder ein. Als nächstes wählen Sie die Ereignisse aus, die Sie tracken möchten; eine Liste der verfügbaren Ereignisse wird angezeigt. Klicken Sie abschließend auf **Launch Current**

{% alert note %}
Ereignisse, die von Braze-Currents an Amplitude gesendet werden, werden auf Ihr Amplitude-Ereignisvolumen angerechnet.
{% endalert %}

![Die Seite Braze Amplitude Currents. Diese Seite enthält Felder für den Namen der Integration, die E-Mail des Kontakts, den API-Schlüssel und die US-Region. In der unteren Hälfte der Currents-Seite werden die verfügbaren Currents-Ereignisse aufgelistet, die Sie senden können.]({% image_buster /assets/img/amplitude4.png %})

{% tab Notiz %}
Lesen Sie die [Dokumente zur Integration](https://amplitude.zendesk.com/hc/en-us/articles/115000217351-Appboy-Amplitude-Integration#how-to-set-up-and-use-the-integration) von Amplitude, um mehr zu erfahren.
{% endtab %}

## Rate-Limits

Currents verbindet sich mit der HTTP API von Amplitude, die ein [Rate-Limit](https://developers.amplitude.com/docs/http-api-v2#upload-limit) von 30 Ereignissen/Sekunde pro Gerät und ein undokumentiertes Limit von 500K Ereignissen/Tag pro Gerät hat. Wenn diese Schwellenwerte überschritten werden, drosselt Amplitude die über Currents protokollierten Ereignisse. Wenn ein Gerät in Ihrer Integration dieses Rate-Limits überschreitet, kann es zu einer Verzögerung kommen, wenn Ereignisse von allen Geräten in Amplitude erscheinen.

Geräte sollten unter normalen Umständen nicht mehr als 30 Ereignisse/Sekunde oder 500K Ereignisse/Tag melden, und dieses Ereignismuster sollte nur aufgrund einer falsch konfigurierten Integration auftreten. Um diese Art von Verzögerung zu vermeiden, stellen Sie sicher, dass Ihre SDK-Integration Ereignisse in einem normalen Rhythmus meldet, wie in unseren SDK-Integrationsanweisungen angegeben, und verzichten Sie auf die Durchführung automatisierter Tests, die viele Ereignisse für ein einzelnes Gerät erzeugen.

## Unterstützte Currents Ereignisse

Braze unterstützt den Export der folgenden Daten, die in den Currents-Glossaren zu [Nutzer:innen]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) und [Messaging-Ereignissen]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) aufgeführt sind, nach Amplitude:

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
  

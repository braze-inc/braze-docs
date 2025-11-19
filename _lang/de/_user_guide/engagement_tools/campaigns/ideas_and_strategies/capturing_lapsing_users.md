---
nav_title: "Erfassen von passiven Nutzer:innen"
article_title: "Erfassen von passiven Nutzer:innen"
page_order: 1
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Braze-Kampagnen effektiv einsetzen können, um diese Nutzer:innen wieder einzubinden."
tool:
  - Segments
  - Campaigns

---

# Erfassen von passiven Nutzer:innen

> Wenn Ihre Zielgruppe schrumpft, ist es wichtig, sie zurückzugewinnen. Mit Braze können Sie automatisierte, wiederkehrende Kampagnen zur erneuten Interaktion einrichten, um passive Nutzer:innen zurückzugewinnen. Sie können den Zeitrahmen und die Häufigkeit der erneuten Interaktion wählen, die am besten zu Ihrer App passen. Zur Veranschaulichung beginnen wir mit einem 14-tägigen Plan zur erneuten Interaktion.

Wenn Sie mehr über das Targeting von Benutzern erfahren möchten, besuchen Sie unseren [Braze Learning-Kurs](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) zur Einrichtung von Kampagnen!

## Schritt 1: Nutzer:innen segmentieren

Zunächst erstellen wir ein Segment, um Nutzer anzusprechen, die Ihre App in den letzten zwei Wochen nicht genutzt haben, und verwenden dazu die folgenden Filter:

- **Zuletzt verwendet App** vor mehr als 2 Wochen
- **Zuletzt verwendet App** vor weniger als 3 Wochen

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Benennen Sie das Segment mit einem einprägsamen Namen, z.B. "Verlorene Nutzer - 2 Wochen". Da wir die Kampagne so einrichten, dass sie wöchentlich wiederholt wird, wollen wir sicherstellen, dass mindestens eine Woche lang Nutzer im Segment erfasst werden. Aus diesem Grund haben wir Nutzer ausgewählt, die die App zuletzt vor zwei bis drei Wochen verwendet haben.

## Schritt 2: Eine Kampagne erstellen

Klicken Sie anschließend auf **Kampagne erstellen** und wählen Sie die Art der Kampagne, die wir an dieses Segment senden werden. In diesem Beispiel erstellen wir eine neue [Push-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Wir nennen die Kampagne „Nachricht an passive Nutzer:innen – 2 Wochen“ und erstellen dann den Content unserer Nachricht. In diesem Beispiel richten wir uns nur an iOS-Nutzer:innen, aber Sie können Braze für Android- und iOS-Push-Benachrichtigungen verwenden. 

Je näher der Zeitpunkt liegt, an dem ein Nutzer das letzte Mal in der App war, desto wichtiger ist es, dass sie aktuell und relevant ist. Wenn Sie einem Nutzer eine Nachricht schicken, nachdem er die App zwei Wochen lang nicht genutzt hat, ist es wichtig, dass Sie relevante Inhalte präsentieren und die Vorteile der App hervorheben.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

Als Nächstes erstellen wir einen wiederkehrenden Zeitplan für den Versand unserer wöchentlichen Nachricht donnerstags um 17:45 Uhr unter Verwendung der [Zustellung zur Ortszeit]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) in den **zeitbasierten Planungsoptionen**. Wir empfehlen Ihnen, Ihre Sitzungsgrafik zu betrachten, um Nutzer:innen kurz vor Zeiten hoher Nutzung anzusprechen. So stellen Sie sicher, dass Sie die Menschen dann ansprechen, wenn sie die App am ehesten nutzen. Sie können dies später ändern und Ihre ursprüngliche Hypothese testen.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Schritt 3: Kampagne starten

Jetzt sind Sie bereit, die Kampagne zu senden. Bestätigen Sie die Einstellungen auf der letzten Seite des Composers und klicken Sie auf **Kampagne starten**!


---
nav_title: "Versand von SMS-Nachrichten"
article_title: Überblick über den Versand von SMS-Nachrichten
page_order: 4
alias: /sms_message_sending/
description: "Dieser Referenzartikel behandelt die Grundlagen und die besten Praktiken des SMS-Versands."
page_type: reference
channel:
  - SMS
  
---

# Versand von SMS-Nachrichten

> Messaging kann kompliziert sein, muss es aber nicht. In den folgenden Abschnitten finden Sie die Grundlagen des Versands von SMS-Nachrichten bei Braze, einschließlich der Bedeutung von Abo-Gruppen, der Anforderungen an SMS-Segmente und Nachrichten-Teile sowie der verfügbaren erweiterten Anpassungsmöglichkeiten.

## Grundlagen des SMS-Versands

### Wählen Sie Ihre Abonnementgruppe

SMS-Nachrichten müssen von einer [Abonnementgruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) gesendet werden. Eine Abo-Gruppe ist eine Sammlung von Absender-Telefonnummern (wie Shortcodes, Langcodes und/oder alphanumerische Sender-IDs), die für eine bestimmte Art von Messaging verwendet werden. Sie müssen eine Abo-Gruppe festlegen, um sicherzustellen, dass nur abonnierte Nutzer:innen zum Targeting herangezogen werden. Einige Kund:innen haben möglicherweise mehrere Abo-Gruppen für unterschiedliche Anwendungsfälle, z. B. für SMS-Nachrichten zu Transaktionszwecken und für SMS-Nachrichten zu Werbezwecken.<br><br>

### Körper der Nachricht eingeben

Ein SMS-Text kann bis zu 1.600 Zeichen enthalten, einschließlich Emojis, Liquid und Connected Content. Eine einzige Kampagne kann zu vielen Nachrichtensegmenten führen. Braze SMS-Nachrichten können entweder aus [GSM-7-](https://en.wikipedia.org/wiki/GSM_03.38) oder [UCS-2-Kodierungsstandards](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) bestehen. Falls ein UCS-2-Zeichen (z. B. ein Emoji) verwendet wird, wird der Nachrichtentext automatisch für diesen Kodierungsstandard formatiert.<br><br> 

### Verstehen Sie Nachrichtensegmente und Zeichenbeschränkungen

SMS-Segmente sind die Art und Weise, wie die SMS-Branche Nachrichten zählt. Ein Nachrichtensegment ist eine Gruppierung von bis zu einer bestimmten Anzahl von Zeichen (160 bei GSM-7-Kodierung; 67 bei UCS-2-Kodierung), die in einer einzigen SMS versendet werden. Wenn Sie eine SMS mit 161 Zeichen in GSM-7-Kodierung versenden, werden Sie feststellen, dass zwei (2) Nachrichtensegmente gesendet wurden. Das Versenden mehrerer Nachrichtensegmente kann zu zusätzlichen Kosten führen.<br><br>

### Schlüsselwortanpassung (optional)

Die Vorschriften verlangen, dass auf alle Opt-in-, Opt-out- und Hilfe/Info-SMS-Schlüsselwortantworten geantwortet wird. Mit Braze können Sie Ihre eigenen Schlüsselwörter definieren, um Opt-in-, Opt-out- und Hilfe-Antworten zu triggern, Ihre eigenen Antworten verwalten, die an Nutzer:innen gesendet werden, und Schlüsselwortsätze für verschiedene Sprachen definieren. Weitere Informationen finden Sie in unserer Sammlung zum Thema [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/).

{% alert tip %}
Möchten Sie erfahren, wie Sie eine SMS-Kampagne erstellen? Sehen Sie sich unsere Schritt-für-Schritt-Anleitung zur [Erstellung einer SMS-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/) an.
{% endalert %}

## Bewährte Praktiken für den Versand {#sending-best-practices}

### SMS-Versand in mehrere Länder

Einige Marken möchten vielleicht an eine Gruppe von Nutzern senden, die Telefonnummern aus verschiedenen Ländern haben. Um eine SMS-Nachricht an eine Telefonnummer in einem bestimmten Land zu senden, verwenden Sie am besten eine lange Vorwahl oder eine kurze Vorwahl, die aus demselben Land stammt. Kurznummern können nämlich nur SMS an Telefonnummern aus demselben Land senden, in dem die Kurznummer erstellt wurde. 

Um diese Einschränkung zu überwinden, können Sie bei der [Einrichtung von]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) Abo-Gruppen Gruppen einrichten, die Lang- und Shortcodes aus mehreren verschiedenen Ländern enthalten. Wenn Sie diese Option aktiviert haben, werden beim Start einer Kampagne automatisch Telefonnummern mit der gleichen Landesvorwahl wie die Telefonnummer des Zielbenutzers verwendet. Sie müssen keine separaten Kampagnen für Nutzer mit Telefonnummern mit unterschiedlichen Ländervorwahlen erstellen, sondern können eine einzige Kampagne starten oder eine einzige Canvas-Komponente verwenden, um relevante Nutzer anzusprechen.

![SMS-Payloads werden unter Verwendung desselben Codes wie die Telefonnummer des Nutzers:innen der Zielgruppe versendet]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

#### Bewährte Praktiken

1. **Holen Sie die Erlaubnis ein**. Eine der wichtigsten Regeln für den geschäftlichen Einsatz von SMS ist, dass Sie zunächst die Erlaubnis Ihrer Kunden einholen müssen, um sie zu kontaktieren. Wenn Sie dies nicht tun, kann dies Ihrer Marke schaden und zu hohen Anwaltskosten führen.<br><br>
2. **Wählen Sie die richtige Nummer für Ihren Anwendungsfall**. Es gibt drei Haupttypen von Telefonnummern, mit denen Sie SMS-Nachrichten senden und empfangen können: lange Codes, kurze Codes und alphanumerische Absender-IDs, deren Möglichkeiten und Verfügbarkeit in den verschiedenen Regionen unterschiedlich sind. Überlegen Sie im Voraus, ob Ihr Unternehmen mit einem Vanity Code besser bedient ist. <br><br>
3. **Achten Sie auf das Timing**. Denken Sie daran, dass Kund:innen eher auf Materialien reagieren, die direkt an sie gerichtet sind. Ein wenig Personalisierung kann viel bewirken, z. B. durch die Verwendung des Vornamens des Empfängers oder durch das Hinzufügen von Konversationstexten, die die Interessen Ihrer Kunden widerspiegeln.<br><br>
4. **Führen Sie Gespräche in beide Richtungen**. SMS ist ein so effektiver Kanal für das Engagement mit Kund:innen, dass es wichtig ist, die Reaktionen auf Ihre Nachrichten zu antizipieren - und effektiv zu verarbeiten. 85% der Verbraucher möchten nicht nur Informationen erhalten, sondern auch auf Unternehmen antworten oder sich mit ihnen unterhalten können.<br><br>
5. **Messen Sie, was funktioniert**. Erreichen Sie Ihre Kunden zum richtigen Zeitpunkt, mit der besten Frequenz und mit den effektivsten Aufrufen zum Handeln? Die Verwendung der richtigen Tracking-Tools kann direkte und messbare Metriken bieten, die ihren ROI belegen. 

### Senden von großen Mengen

Planen Sie, große Mengen zu versenden? Wir haben einige bewährte Verfahren für Sie, um einen reibungslosen Ablauf zu gewährleisten.

- Passen Sie die Rate-Limits für die Zustellung Ihrer Kampagnen/Canvases nach Bedarf an die Größe der Zielgruppen an. Damit stellen Sie sicher, dass Sie das benötigte Sendevolumen erreichen und dass Braze die Nachrichten mit der von Twilio erwarteten und verkraftbaren Geschwindigkeit sendet.
- Achten Sie darauf, dass Sie die 160 Zeichen nicht überschreiten, und beachten Sie, dass Sonderzeichen doppelt gezählt werden (z. B. Schrägstriche `\`, Carets `^` und Tilden `~`). 


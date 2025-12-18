---
nav_title: "MMS"
article_title: Über MMS
page_order: 15
description: "In diesem Artikel erfahren Sie, was MMS-Nachrichten sind und welche Anwendungsfälle es für sie gibt."
page_type: reference
alias: /about_mms/
channel:
  - MMS
search_rank: 2  
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"} Über MMS Nachrichten

> MMS, auch bekannt als Multimedia Message Service, wird verwendet, um Nachrichten mit Multimedia-Inhalten (JPEG, GIF, PNG) an Mobiltelefone zu senden.<br><br>Wie SMS ist auch MMS ein Messaging-Kanal mit hoher Dringlichkeit, der es Ihnen erlaubt, so zu kommunizieren, wie Sie es auf keinem anderen Kanal können. MMS erweitert jedoch die Möglichkeiten von SMS, indem es Ihnen die Möglichkeit gibt, einer ansonsten reinen Text-SMS Medien hinzuzufügen.

## Potenzielle Anwendungsfälle

| Anwendungsfall | Erklärung |
| --- | --- |
| Aktionen | Starten Sie öffentlichkeitswirksame SMS Kampagnen, aber nutzen Sie auch den Medienaspekt von MMS, um Ihre Angebote attraktiver zu machen. | 
| Re-Engagement-Kampagnen | Binden Sie Kunden, die sich für den Erhalt von SMS entschieden haben, wieder ein, wenn alle anderen Kanäle sie nicht zurückbringen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Lernen Sie MMS kennen

### MMS-Verfügbarkeit

Die meisten US-amerikanischen und kanadischen Mobilfunkanbieter unterstützen den Empfang und die Anzeige von Multimedia-Inhalten auf den Telefonen ihrer Kunden. Für internationale Anbieter konvertiert Braze automatisch MMS-Nachrichten, die von einer unterstützten Telefonnummer in den USA oder Kanada gesendet werden, und zwar nur an Ziele, die MMS nicht unterstützen. Bei diesen Nachrichten ersetzt Braze die angehängten Medien durch eine kurze URL, die dem Nachrichtentext hinzugefügt wird und einen Link zu der Datei enthält.

### Abo-Gruppen

Eine [Abo-Gruppe]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) ist ein Verzeichnis mit Absenderrufnummern (Short-/Langcode und alphanumerische Absenderkennungen) für eine bestimmte Art von Messaging. Ihre Abo-Gruppe benötigt eine MMS-fähige Telefonnummer. Sprechen Sie mit Ihrem Braze-Kundenbetreuer über die Aktivierung dieser Funktion.

### Grenzwerte für MMS-Nachrichten und Durchsatz

Die Anbieter legen eine maximale Dateigröße fest, die letztlich über den Erfolg von MMS-Sendungen entscheidet. Diese Grenzen können je nach Land und Netzbetreiber variieren. Um auf der sicheren Seite zu sein, empfiehlt Braze, 600 KB für Ihre Multimedia-Inhalte nicht zu überschreiten und gleichzeitig einen Nachrichtentext einzufügen. Wir empfehlen auch zu testen, ob Ihre Medien den Nutzern:innen zugestellt werden können.

Der MMS-Durchsatz beträgt ein Segment pro Sekunde per Langcode.

#### Anbieterabhängige Größenbeschränkungen

| Dateigröße | Verarbeitungshinweise |
| --- | --- |
| 300 KB | Alle Anbieter sollten MMS-Nachrichten dieser Größe zuverlässig verarbeiten. |
| 600 KB | Die maximale MMS-Dateigröße bei den meisten Anbietern. |
| 1 MB |  Die meisten US-amerikanischen und kanadischen Mobilfunkanbieter können MMS-Nachrichten dieser Größe verarbeiten, wobei dies je nach Anbieter variieren kann. Bei einigen Anbietern sind möglicherweise größere Dateigrößen zulässig. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Eingehende MMS

Geht eine Nutzernachricht mit einem Medieninhalt ein, gibt Braze dessen URL mit dem Liquid-Tag sowohl in Currents als auch in Liquid bekannt. {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Akzeptierte Dateitypen

Braze akzeptiert JPEG-, GIF-, PNG- und VCF-Dateien und erlaubt es Ihnen, einzelne Multimedia-Assets an MMS-Nachrichten anzuhängen.



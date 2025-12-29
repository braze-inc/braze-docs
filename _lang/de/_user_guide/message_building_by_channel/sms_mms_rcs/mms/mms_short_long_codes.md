---
nav_title: "MMS-Kurz- und Langcodes"
article_title: MMS Kurz- und Lang-Codes
page_order: 1
description: "Dieser Referenzartikel behandelt die Unterschiede zwischen SMS- und MMS-Kurzcodes und Langcodes."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# MMS-Kurz- und Langcodes

> MMS und SMS sind beide an den SMS-Kanal von Braze gebunden. Für den Zugang zu MMS auf Ihrem Konto ist der Kauf von SMS für diejenigen erforderlich, die noch keinen Zugang erworben haben. Bestehende SMS-Kund:innen können auf MMS zugreifen, nachdem sie es erworben haben. 

MMS wird derzeit für US-Kurznummern (5- bis 6-stellige Nummern), US- und kanadische Langnummern (10-stellige Nummern) sowie US- und kanadische Kundennummern unterstützt. Der Versand von MMS an Nummern außerhalb der USA/Kanada ist möglich, aber MMS-Nachrichten werden in eine SMS-Nachricht mit einem Link zum Medienobjekt umgewandelt. Weitere Informationen finden Sie unter [Kurze und lange Codes]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## MMS-Kurzcodes

Einige Benutzer werden möglicherweise keine MMS-Kurznummern einrichten oder verwenden, aber sie werden bei Bedarf zu einem späteren Zeitpunkt verfügbar sein.

Alle Nutzer:innen, die ihre Kurzwahlnummern vor der Einführung von MMS durch Braze erhalten haben, können MMS sofort aktivieren. Wenden Sie sich an Ihren Customer Success Manager, wenn diese Situation auf Sie zutrifft und Sie MMS aktivieren möchten.

{% alert important %}
Wenn Sie MMS für Kurzwahlnummern aktivieren, für die MMS zuvor nicht aktiviert war, müssen die Kurzwahlnummern unter Umständen in einem Genehmigungsverfahren neu genehmigt werden, das Wochen dauern kann. Es ist wichtig, dieses Timing zu berücksichtigen, wenn Sie sich für die Aktivierung von MMS entscheiden.
{% endalert %}

### Bewährte Praktiken für MMS-Kurzmitteilungen

- Wir bei Braze empfehlen dringend, Transaktions- und Werbenachrichten getrennt zu halten, jeweils mit unterschiedlichen Kurzcodes. Da MMS an den SMS-Kanal gebunden ist und der SMS-Kanal stark reguliert ist, können Kunden für den Missbrauch des Kanals eine Geldstrafe zahlen müssen und ihre Kurznummer gesperrt bekommen (was nicht rückgängig zu machen ist). Indem Sie Transaktions- und Werbenachrichten an unterschiedliche Kurzcodes binden, schützen Sie Ihre Transaktionsnachrichten.
- Wenn Kund:innen bereits eine Kurzwahlnummer für Werbenachrichten haben und diese MMS-fähig ist, benötigen sie keine separate Kurzwahlnummer für MMS.

## MMS lange Codes

Kunden können MMS mit langen Codes versenden. Dazu müssen Sie sicherstellen, dass Ihre langen Codes MMS-fähig sind. Dies kann zunächst bei der Einrichtung oder später in Ihrem Konto geschehen. 

Beachten Sie, dass unsere MMS-Nachrichten nicht mit einer alphanumerischen Absender-ID gesendet werden können. Wenn Sie mehr über alphanumerische IDs erfahren möchten, lesen Sie bitte [Alphanumerische Sender-IDs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).

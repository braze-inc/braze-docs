---
nav_title: Akquisition von Telefonnummern
article_title: Akquisition von Telefonnummern
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Rufnummer von Twilio und Infobip erwerben können."
page_type: reference
channel:
  - WhatsApp
---

# Akquisition von Telefonnummern

> Um den WhatsApp-Nachrichtenkanal nutzen zu können, benötigen Sie eine Telefonnummer, die den Anforderungen von WhatsApp für die [Cloud-API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) oder die [On-Premises-API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) entspricht.

Sie müssen Ihre Telefonnummer selbst beschaffen, da Braze die Nummer nicht für Sie bereitstellt. Sie können entweder ein physisches Telefon mit einer SIM-Karte über Ihren geschäftlichen Telefonanbieter erwerben oder einen unserer Partner nutzen: Twilio oder Infoblip. **Sie müssen über ein eigenes Twilio- oder Infobip-Konto verfügen, da dies nicht über Braze möglich ist.**

## WhatsApp API-Anforderungen

Ihre Telefonnummer muss diese WhatsApp API-Anforderungen erfüllen:

- Im Besitz Ihres Unternehmens 
- Sie haben eine Landes- und Ortsvorwahl (z. B. eine Festnetz- und eine Handynummer)
- Sie können Sprachanrufe oder SMS empfangen
- Zugänglich während der Kontoeinrichtung (um Verifizierungscodes zu erhalten)
- Kein Kurzcode
- Bisher nicht mit der WhatsApp Business-Plattform verwendet
- Nicht mit einem persönlichen WhatsApp-Konto verbunden

## Erwerben einer Twilio (Twilio)-Telefonnummer

### Schritt 1: Kaufen Sie eine Telefonnummer über die Twilio Konsole oder API

1. Gehen Sie in der Twilio-Konsole zu **Entwickeln** > **Telefonnummern** > **Verwalten** > **Eine Nummer kaufen**. Wenn Sie diese Option nicht sehen, wählen Sie **Produkte erkunden**, blättern Sie zu **Supernetzwerke** und wählen Sie dann **Rufnummer** > **Nummer kaufen**. <br><br>![Twilio-Konsole mit geöffnetem Tab "Entwickeln" und der Option "Eine Nummer kaufen".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Geben Sie die gewünschte Vorwahl oder den Ort ein (falls vorhanden). Suchen Sie eine Nummer und wählen Sie dann **Kaufen**. <br><br> ![Ein Button, um die aufgelistete Rufnummer zu kaufen.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Nachdem Sie Ihre Telefonnummer erworben haben, gehen Sie zu **Aktive Nummern** und wählen Sie die soeben erworbene Telefonnummer aus. <br><br>!["Aktive Nummern" zeigt die gekaufte Rufnummer an.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Schritt 2: Konfigurieren Sie Ihre Rufnummer

Folgen Sie den Anweisungen von Twilio, um [Ihre Twilio-Telefonnummer so einzurichten, dass Sie den Verifizierungscode per E-Mail über Twilio Voice Only erhalten](https://www.twilio.com/docs/whatsapp/self-sign-up#verify-your-whatsapp-sender). **Befolgen Sie die Anweisungen in keinem anderen Schritt, denn dadurch wird Ihre Telefonnummer mit Twilio und nicht mit Braze verbunden.**

{% alert warning %}
**Befolgen Sie nur die Anweisungen von Twilio (Twilio), um einen Verifizierungscode zu erhalten.**

Wenn Sie die nächsten Schritte in der Anleitung von Twilio befolgen, verbinden Sie Ihre Telefonnummer mit Twilio (Twilio). Das bedeutet, dass Sie diese Nummer nicht mit Braze verbinden können, es sei denn, Sie führen eine Migration durch oder erwerben eine andere Nummer.
{% endalert %}

### Schritt 3: Schließen Sie den eingebetteten Anmeldevorgang ab

1. Nachdem Twilio konfiguriert ist, gehen Sie zu Ihrem Braze Dashboard > **Technologiepartner** > **WhatsApp** und wählen Sie **Integration beginnen** oder **WhatsApp Business Account hinzufügen**, je nachdem, was angezeigt wird, um den [eingebetteten Anmelde-Workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) auszulösen.<br><br>Im Schritt **Telefonnummer für WhatsApp hinzufügen** wählen Sie **Telefonanruf** für die Art und Weise, wie Sie Ihre Telefonnummer verifizieren möchten. <br><br>![Abschnitt mit den Optionen zum Überprüfen Ihrer Rufnummer per SMS oder Anruf.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Warten Sie ein paar Minuten, bis der Verifizierungscode an Ihren E-Mail-Posteingang gesendet wird, geben Sie den Verifizierungscode ein und schließen Sie die Einrichtung ab.

## Erwerben einer Infobip-Telefonnummer 

1. Gehen Sie in der Infobip-Konsole zu **Kanäle und Nummern** und wählen Sie **Nummern**.<br><br>![Infoblip Abschnitt "Kanäle und Nummern" mit "Nummern" darunter.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Wählen Sie **Nummer kaufen** > das Land, in dem Sie Nachrichten senden möchten > **SMS**.<br><br>![Button zum Kaufen einer Nummer.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Je nach dem von Ihnen gewählten Land müssen Sie möglicherweise einen zusätzlichen Registrierungsprozess durchführen (z. B. die Auswahl einer 10 DLC oder gebührenfreien Option für US-Telefonnummern). Achten Sie darauf, die verfügbare Option zu wählen.<br><br>![Eine Seite, auf der Sie die Art der Nummer auswählen können: entweder 10 DLC oder gebührenfrei.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Wählen Sie das verfügbare Angebot aus, fahren Sie mit den restlichen Schritten fort und warten Sie, bis Ihre Anfrage bearbeitet wird. Sie können den Status überprüfen, indem Sie auf **Zahlen** > **Mein Antrag** gehen. <br><br>![Ein Angebot mit Informationen zu Gebühren und Versicherungsschutz.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Je nach dem von Ihnen gewählten Land warten Sie darauf, dass sich das Infobip-Team wegen der Registrierungsdetails meldet (z. B. für 10DLC in den USA).<br><br>

6. Wenn Ihre Telefonnummer in Infobip bereit ist, gehen Sie zu Ihrem Braze Dashboard > **Technologiepartner** > **WhatsApp** und wählen Sie **Integration beginnen** oder **WhatsApp Business Account hinzufügen**, je nachdem, was angezeigt wird, um den [eingebetteten Anmelde-Workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) auszulösen.<br><br> Im Schritt **Telefonnummer für WhatsApp hinzufügen** wählen Sie **Textnachricht** für die Art und Weise, wie Sie Ihre Telefonnummer verifizieren möchten.<br><br>![Abschnitt mit den Optionen zum Überprüfen Ihrer Rufnummer per SMS oder Anruf.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Suchen Sie in den [Analyseprotokollen](https://www.infobip.com/docs/analyze/analyze-logs) des Kundenportals von Infobip nach dem Verifizierungscode. Es kann einige Minuten dauern, bis er erscheint, geben Sie den Verifizierungscode ein und schließen Sie die Einrichtung ab.





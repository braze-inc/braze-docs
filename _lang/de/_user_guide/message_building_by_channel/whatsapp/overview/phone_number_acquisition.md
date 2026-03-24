---
nav_title: Akquisition von Telefonnummern
article_title: Akquisition von Telefonnummern
page_order: 4
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Telefonnummer von Twilio und Infobip erwerben können."
page_type: reference
channel:
  - WhatsApp
---

# Akquisition von Telefonnummern

> Um den WhatsApp-Messaging-Kanal nutzen zu können, benötigen Sie eine Telefonnummer, die den Anforderungen von WhatsApp für die [Cloud-API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) oder die [On-Premises-API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) entspricht.

Sie müssen Ihre Telefonnummer selbst beschaffen, da Braze die Nummer nicht für Sie bereitstellt. Sie können entweder ein physisches Telefon mit einer SIM-Karte über Ihren geschäftlichen Telefonanbieter erwerben oder einen unserer Partner nutzen: Twilio oder Infobip. **Sie müssen über ein eigenes Twilio- oder Infobip-Konto verfügen, da dies nicht über Braze möglich ist.**

## WhatsApp-API-Anforderungen

Ihre Telefonnummer muss die folgenden WhatsApp-API-Anforderungen erfüllen:

- Im Besitz Ihres Unternehmens 
- Mit Landes- und Ortsvorwahl (z. B. Festnetz- oder Mobilfunknummern)
- Fähig, Sprachanrufe oder SMS zu empfangen
- Während der Kontoeinrichtung erreichbar (um Verifizierungscodes zu empfangen)
- Kein Shortcode
- Bisher nicht mit der WhatsApp Business-Plattform verwendet
- Nicht mit einem persönlichen WhatsApp-Konto verbunden

## Erwerben einer Twilio-Telefonnummer

### 1. Schritt: Kaufen Sie eine Telefonnummer über die Twilio-Konsole oder API

1. Gehen Sie in der Twilio-Konsole zu **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Wenn Sie diese Option nicht sehen, wählen Sie **Explore Products**, scrollen Sie zu **Super Networks** und wählen Sie dann **Phone Number** > **Buy a number**. <br><br>![Twilio-Konsole mit geöffnetem Tab „Develop" und der Option „Buy a number".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Geben Sie die gewünschte Vorwahl oder den Ort ein (falls vorhanden). Suchen Sie eine Nummer und wählen Sie dann **Buy**. <br><br> ![Ein Button, um die aufgelistete Telefonnummer zu kaufen.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Nachdem Sie Ihre Telefonnummer erworben haben, gehen Sie zu **Active Numbers** und wählen Sie die soeben erworbene Telefonnummer aus. <br><br>![„Active Numbers" zeigt die gekaufte Telefonnummer an.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### 2. Schritt: Konfigurieren Sie Ihre Telefonnummer

Folgen Sie den Anweisungen von Twilio, um Ihre Twilio-Telefonnummer so einzurichten, dass Sie den Verifizierungscode per E-Mail erhalten – verwenden Sie dabei **ausschließlich** [Twilio Voice](https://www.twilio.com/docs/whatsapp/self-sign-up#add-your-whatsapp-phone-number). **Befolgen Sie keine Anweisungen in anderen Schritten.**

{% alert warning %}
Befolgen Sie nur die Anweisungen von Twilio, um einen Verifizierungscode zu erhalten.
Wenn Sie die nächsten Schritte befolgen, verbinden Sie Ihre Telefonnummer mit Twilio. Das bedeutet, dass Sie diese Nummer nicht mit Braze verbinden können, es sei denn, Sie führen eine Migration durch oder erwerben eine andere Nummer.
{% endalert %}

1. Gehen Sie in der Twilio-Konsole zur Seite [Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) und wählen Sie die erworbene Telefonnummer aus.
2. Gehen Sie zum Abschnitt **Voice Configuration** und wählen Sie im Dropdown **Configure with** die Option **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. Wählen Sie in der Zeile **A call comes in** die Option **Webhook** und setzen Sie die URL auf `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, wobei Sie `YOUR_EMAIL_ADDRESS` durch Ihre E-Mail-Adresse ersetzen.
4. Gehen Sie in der Twilio-Konsole zu **2. Link WhatsApp Business Account with your number** > **2. Copy the phone number you register** und wählen Sie **Copy** neben der Telefonnummer.
5. Wählen Sie im Fenster **Self Sign-up** auf der Seite **Add your WhatsApp phone number** die Option **Add a new phone number** und fügen Sie die Telefonnummer ein.
6. Wählen Sie **Phone call** als Verifizierungsmethode und dann **Next**.
7. Sie erhalten den Verifizierungscode innerhalb von 10 Minuten per E-Mail.

### 3. Schritt: Schließen Sie den eingebetteten Registrierungs-Workflow ab

1. Nachdem Twilio konfiguriert ist, gehen Sie zu Ihrem Braze-Dashboard > **Technology Partners** > **WhatsApp** und wählen Sie **Begin integration** oder **Add WhatsApp Business Account** – je nachdem, was angezeigt wird –, um den [eingebetteten Registrierungs-Workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) auszulösen.<br><br>Im Schritt **Add a phone number for WhatsApp** wählen Sie **Phone call** als Methode zur Verifizierung Ihrer Telefonnummer. <br><br>![Abschnitt mit den Optionen zur Verifizierung Ihrer Telefonnummer per Textnachricht oder Telefonanruf.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Warten Sie einige Minuten, bis der Verifizierungscode an Ihren E-Mail-Posteingang gesendet wird, geben Sie den Verifizierungscode ein und schließen Sie die Einrichtung ab.

## Erwerben einer Infobip-Telefonnummer 

1. Gehen Sie in der Infobip-Konsole zu **Channels and Numbers** und wählen Sie **Numbers**.<br><br>![Infobip-Abschnitt „Channels and Numbers" mit der Auflistung „Numbers" darunter.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Wählen Sie **Buy Number** > das Land, in das Sie Nachrichten senden möchten > **SMS**.<br><br>![Button, um eine Nummer zu kaufen.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Je nach dem von Ihnen gewählten Land müssen Sie möglicherweise einen zusätzlichen Registrierungsprozess durchführen (z. B. die Auswahl einer 10DLC- oder gebührenfreien Option für US-Telefonnummern). Achten Sie darauf, die verfügbare Option auszuwählen.<br><br>![Eine Seite, auf der Sie die Art der Nummer auswählen können: entweder 10DLC oder gebührenfrei.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Wählen Sie das verfügbare Angebot aus, fahren Sie mit den restlichen Schritten fort und warten Sie, bis Ihre Anfrage bearbeitet wird. Sie können den Status überprüfen, indem Sie zu **Numbers** > **My Request** gehen. <br><br>![Ein Angebot mit Informationen zu Gebühren und Abdeckung.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Je nach ausgewähltem Land warten Sie darauf, dass sich das Infobip-Team mit Ihnen in Verbindung setzt, um die Registrierungsdetails zu klären (z. B. für 10DLC in den USA).<br><br>

6. Wenn Ihre Telefonnummer in Infobip bereit ist, gehen Sie zu Ihrem Braze-Dashboard > **Technology Partners** > **WhatsApp** und wählen Sie **Begin integration** oder **Add WhatsApp Business Account** – je nachdem, was angezeigt wird –, um den [eingebetteten Registrierungs-Workflow]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/) auszulösen.<br><br> Im Schritt **Add a phone number for WhatsApp** wählen Sie **Text message** als Methode zur Verifizierung Ihrer Telefonnummer.<br><br>![Abschnitt mit den Optionen zur Verifizierung Ihrer Telefonnummer per Textnachricht oder Telefonanruf.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Suchen Sie in den [Analyseprotokollen](https://www.infobip.com/docs/analyze/analyze-logs) des Infobip-Kundenportals nach dem Verifizierungscode. Es kann einige Minuten dauern, bis er erscheint. Geben Sie den Verifizierungscode ein und schließen Sie die Einrichtung ab.
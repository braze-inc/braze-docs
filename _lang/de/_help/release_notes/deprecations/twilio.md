---
nav_title: Twilio Partnerschaft
alias: /partners/twilio/

description: "Dieser Artikel beschreibt die Partnerschaft zwischen Braze und Twilio."
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Beachten Sie, dass die Unterstützung für die Twilio Webhook-Integration am 31\. Januar 2020 eingestellt wird. Wenn Sie mit Braze weiterhin auf SMS-Dienste zugreifen möchten, lesen Sie unsere [SMS-Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).
{% endalert %}

In diesem Beispiel konfigurieren wir den Braze Webhook-Kanal, um SMS und MMS über die [Twilio-API für den Nachrichtenversand][20] an Ihre Benutzer zu senden. Zu Ihrer Erleichterung ist eine Twilio Webhook-Vorlage im Dashboard enthalten.

## HTTP-URL

Die Webhook-URL wird von Twilio in Ihrem Dashboard bereitgestellt. Diese URL ist für Ihr Twilio-Konto eindeutig, da sie Ihre Twilio-Konto-ID enthält (`TWILIO_ACCOUNT_SID`).

In unserem Twilio-Beispiel lautet die Webhook-URL `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Sie finden diese URL im Abschnitt *Erste Schritte* der Twilio-Konsole.

![Twilio_Konsole][28]

## Anfragetext

Die Twilio-API erwartet, dass der Request Body URL-kodiert ist. Daher müssen wir zunächst den Request Type im Braze Webhook Composer auf `Raw Text` ändern. Die erforderlichen Parameter für den Text der Anfrage sind *To*, *From* und *Body*.

Der folgende Screenshot ist ein Beispiel dafür, wie Ihre Anfrage aussehen könnte, wenn Sie eine SMS an die Telefonnummer eines jeden Benutzers mit dem Text "Hallo von Braze!

- Sie benötigen gültige Telefonnummern für jedes Benutzerprofil in Ihrer Zielgruppe.
- Um das Anfrageformat von Twilio zu erfüllen, verwenden Sie den Filter `url_param_escape` Liquid für den Inhalt Ihrer Nachricht. Dieser Filter kodiert eine Zeichenkette so, dass alle Zeichen in einer HTML-Anfrage erlaubt sind; zum Beispiel ist das Pluszeichen (`+`) in der Telefonnummer `+12125551212` in URL-kodierten Daten verboten und wird in `%2B12125551212` umgewandelt.

![Webhook Körper][29]

## Kopfzeilen der Anfrage und Methode

Twilio benötigt zwei Anfrage-Header, den Anfrage-Content-Type und einen [HTTP Basic Authentication][32] Header. Fügen Sie sie zu Ihrem Webhook hinzu, indem Sie auf das Zahnradsymbol neben dem Webhook-Komponisten klicken und dann zweimal auf *Neues Paar hinzufügen*.

Kopfzeile Name | Kopfzeile Wert
--- | ---
Inhalt-Typ | `application/x-www-form-urlencoded`
Autorisierung | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Stellen Sie sicher, dass Sie `TWILIO_ACCOUNT_SID` und `TWILIO_AUTH_TOKEN` durch Werte aus Ihrem Twilio-Dashboard ersetzen. Schließlich erwartet der API-Endpunkt von Twilio eine HTTP-POST-Anfrage. Wählen Sie also diese Option in der Dropdown-Liste für die *HTTP-Methode*.

![Webhook-Methode][30]

## Vorschau Ihrer Anfrage

Verwenden Sie den Webhook-Composer, um eine Vorschau der Anfrage für einen zufälligen Benutzer oder für einen Benutzer mit bestimmten Anmeldeinformationen zu erstellen, um sicherzustellen, dass die Anfrage richtig gerendert wird.

![Webhook Vorschau][31]

[20]: https://www.twilio.com/docs/api/rest/sending-messages
[28]: {% image_buster /assets/img_archive/Twilio_Console.png %}
[29]: {% image_buster /assets/img_archive/Webhook_Body.png %}
[30]: {% image_buster /assets/img_archive/Webhook_Method.png %}
[31]: {% image_buster /assets/img_archive/Webhook_Preview.png %}
[32]: https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side

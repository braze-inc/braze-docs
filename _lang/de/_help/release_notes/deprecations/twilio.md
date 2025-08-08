---
nav_title: Twilio (Twilio) Partnerschaft
alias: /partners/twilio/

description: "Dieser Artikel stellt die Partnerschaft zwischen Braze und Twilio vor."
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Beachten Sie, dass die Unterstützung für die Twilio Webhook Integration am 31\. Januar 2020 eingestellt wird. Wenn Sie mit Braze weiterhin auf SMS Dienste zugreifen möchten, lesen Sie unsere [SMS Dokumentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).
{% endalert %}

In diesem Beispiel konfigurieren wir den Braze-Webhook-Kanal, um SMS und MMS über die [Twilio-API zum Versenden von Nachrichten](https://www.twilio.com/docs/api/rest/sending-messages) an Ihre Nutzer:innen zu senden. Auf dem Dashboard finden Sie ein Template für Twilio Webhooks, das Ihnen die Arbeit erleichtert.

## HTTP-URL

Die Webhook-URL wird von Twilio in Ihrem Dashboard bereitgestellt. Diese URL ist eindeutig für Ihr Twilio-Konto, da sie Ihre Twilio-Konto-ID (`TWILIO_ACCOUNT_SID`) enthält.

In unserem Twilio-Beispiel lautet die Webhook-URL `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Sie finden diese URL im Abschnitt *Erste Schritte* der Twilio-Konsole.

![Twilio_Console]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Anfragetext

Die Twilio API erwartet, dass der Körper der Anfrage URL-kodiert ist, also müssen wir zunächst den Typ der Anfrage im Braze-Webhook-Composer auf `Raw Text` ändern. Die erforderlichen Parameter für den Text der Anfrage sind *To*, *From* und *Body*.

Der folgende Screenshot ist ein Beispiel dafür, wie Ihre Anfrage aussehen könnte, wenn Sie eine SMS an die Telefonnummer jedes Nutzers:innen mit dem Text "Hallo von Braze!" senden.

- Sie benötigen gültige Telefonnummern in jedem Nutzerprofil Ihrer Zielgruppe.
- Um das Anfrageformat von Twilio zu erfüllen, verwenden Sie den Liquid Filter `url_param_escape` für den Inhalt Ihrer Nachrichten. Dieser Filter kodiert einen String so, dass alle Zeichen in einer HTML-Anfrage zulässig sind; zum Beispiel ist das Pluszeichen (`+`) in der Telefonnummer `+12125551212` in URL-kodierten Daten verboten und wird in `%2B12125551212` umgewandelt.

![Webhook Körper]({% image_buster /assets/img_archive/Webhook_Body.png %})

## Anfrage-Header und Methode

Twilio benötigt zwei Anfrage-Header, den Content-Typ der Anfrage und einen [HTTP Basic Authentication-Header](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Fügen Sie sie zu Ihrem Webhook hinzu, indem Sie auf das Zahnradsymbol neben dem Webhook-Composer klicken und dann zweimal auf *Neues Paar hinzufügen* klicken.

Kopfzeile Name | Kopfzeile Wert
--- | ---
Content-Typ | `application/x-www-form-urlencoded`
Autorisierung | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Ersetzen Sie `TWILIO_ACCOUNT_SID` und `TWILIO_AUTH_TOKEN` durch Werte aus Ihrem Twilio Dashboard. Der API Endpunkt von Twilio erwartet eine HTTP POST Anfrage. Wählen Sie daher diese Option in der Dropdown-Liste für die *HTTP Methode*.

![Webhook Methode]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Vorschau auf Ihre Anfrage

Verwenden Sie den Webhook Composer, um eine Vorschau der Anfrage für einen zufälligen Nutzer oder für einen Nutzer:innen mit bestimmten Zugangsdaten zu erstellen, um sicherzustellen, dass die Anfrage richtig dargestellt wird.

![Webhook Vorschau]({% image_buster /assets/img_archive/Webhook_Preview.png %})


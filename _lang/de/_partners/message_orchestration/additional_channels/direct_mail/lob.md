---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Lob.com, die es Ihnen erlaubt, Direkt-Mailing wie Briefe, Postkarten und Schecks per Post zu versenden."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] ist ein Online-Dienst, der es Ihnen erlaubt, Direkt-Mailing an Ihre Nutzer:innen zu senden.

Die Integration von Braze und Lob nutzt Braze-Webhooks und die Lob API, um Briefe, Postkarten und Schecks per Post zu versenden.  

## Voraussetzungen

|Anforderung| Beschreibung|
| ---| ---|
|Lob Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lob-Konto. |
| Lob API-Schlüssel | Ihren Lob API-Schlüssel finden Sie im Abschnitt Einstellungen unter Ihrem Namen im Lob Dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Lob Endpunkt auswählen

Die HTTP-URL, die im Webhook angefragt werden muss, ist für jede Aktion, die Sie mit Lob durchführen können, unterschiedlich. Im folgenden Beispiel verwenden wir den Postkarten API Endpunkt `https://api.lob.com/v1/postcards`. Besuchen Sie die [vollständige Endpunktliste][39], um den für Ihren Anwendungsfall geeigneten Endpunkt auszuwählen. 

| API-Endpunkt | Verfügbare Endpunkte |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/adressen<br>/v1/adressen/{id}<br>/v1/überprüfen<br>/v1/postkarten<br>/v1/postkarten/{id}<br>/v1/Brief<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_konten<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/gebiete<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routen<br>/v1/Länder<br>/v1/zustände|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 2: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Um eine Lob-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, navigieren Sie in der Braze-Plattform zu **Templates** > **Webhook-Vorlagen**. 

Wenn Sie eine einmalige Lob-Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook Template die folgenden Felder aus:
- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Lob benötigt einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf dem Tab **Einstellungen** müssen Sie `<LOB_API_KEY>` durch Ihren Lob API-Schlüssel ersetzen. Dieser Schlüssel muss ein ":" direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein. 

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Typ**: application/json

![Der Code des Anfragekörpers und die Webhook-URL werden im Tab "Braze webhook builder compose" angezeigt.][35]

#### Anfragetext

Im Folgenden sehen Sie einen Beispiel-Anfragetext für den Endpunkt Lob postcards. Dieser Body der Anfrage wird zwar im Basis-Template von Lob in Braze bereitgestellt, aber wenn Sie andere Endpunkte verwenden möchten, müssen Sie Ihre Liquid-Felder entsprechend anpassen.

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### Schritt 3: Vorschau auf Ihre Anfrage

An diesem Punkt sollte Ihre Kampagne bereit sein, um getestet und versendet zu werden. Überprüfen Sie das Dashboard von Lob und die Nachrichtenprotokolle der Entwickler:in der Braze-Entwicklerkonsole, wenn Sie auf Fehler stoßen. Der folgende Fehler wurde zum Beispiel durch einen falsch formatierten Authentifizierungs-Header verursacht. 

![Ein Nachrichten-Fehlerprotokoll, das die Zeit, den Namen der App, den Kanal und die Fehlermeldung anzeigt. Die Fehlermeldung enthält die Benachrichtigung und den Fehlercode.][36]

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth

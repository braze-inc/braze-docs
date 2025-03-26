---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lob.com, die es Ihnen ermöglicht, Direktwerbung wie Briefe, Postkarten und Schecks auf dem Postweg zu versenden."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] ist ein Online-Dienst, mit dem Sie Direktmailings an Ihre Nutzer senden können.

Die Integration von Braze und Lob nutzt die Webhooks von Braze und die API von Lob, um Briefe, Postkarten und Schecks auf dem Postweg zu versenden.  

## Voraussetzungen

|Anforderung| Beschreibung|
| ---| ---|
|Lob-Konto | Ein Lob-Konto ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Lob API-Schlüssel | Ihren Lob-API-Schlüssel finden Sie im Abschnitt Einstellungen unter Ihrem Namen im Lob-Dashboard. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Endpunkt Lob auswählen

Die im Webhook anzufordernde HTTP-URL ist für jede Aktion, die Sie mit Lob durchführen können, unterschiedlich. Im folgenden Beispiel verwenden wir den Postkarten-API-Endpunkt `https://api.lob.com/v1/postcards`. Besuchen Sie die [vollständige Endpunktliste][39], um den für Ihren Anwendungsfall geeigneten Endpunkt auszuwählen. 

| API-Endpunkt | Verfügbare Endpunkte |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/adressen<br>/v1/adressen/{id}<br>/v1/überprüfen<br>/v1/postkarten<br>/v1/postkarten/{id}<br>/v1/Brief<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_konten<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/gebiete<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routen<br>/v1/Länder<br>/v1/zustände|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 2: Erstellen Sie Ihre Braze Webhook-Vorlage

Um eine Lob-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvases verwenden können, navigieren Sie auf der Braze-Plattform zu **Vorlagen** > **Webhook-Vorlagen**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige Lob-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

Lob erfordert einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf der Registerkarte **Einstellungen** müssen Sie `<LOB_API_KEY>` durch Ihren Lob-API-Schlüssel ersetzen. Dieser Schlüssel muss ein ":" direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein. 

- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
  - **Autorisierung**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Inhalt-Typ**: application/json

![Der Bodycode der Anfrage und die Webhook-URL werden auf der Registerkarte Komposition des Braze Webhook-Builders angezeigt.][35]

#### Anfragetext

Im Folgenden sehen Sie einen Beispiel-Anfragetext für den Endpunkt Lob postcards. Dieser Anfragekörper ist zwar in der Basis-Lob-Vorlage in Braze enthalten, aber wenn Sie andere Endpunkte verwenden möchten, müssen Sie Ihre Liquid-Felder entsprechend anpassen.

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

### Schritt 3: Vorschau Ihrer Anfrage

An diesem Punkt sollte Ihre Kampagne bereit sein, um getestet und versendet zu werden. Überprüfen Sie das Lob-Dashboard und die Fehlermeldungsprotokolle der Braze-Entwicklerkonsole, wenn Sie auf Fehler stoßen. Der folgende Fehler wurde zum Beispiel durch einen falsch formatierten Authentifizierungs-Header verursacht. 

![Ein Nachrichten-Fehlerprotokoll, das die Zeit, den Anwendungsnamen, den Kanal und die Fehlermeldung anzeigt. Die Fehlermeldung enthält die Meldungsmeldung und den Statuscode.][36]

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth

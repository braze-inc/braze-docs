---
nav_title: optilyz
article_title: optilyz
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Optilyz, die es Ihnen ermöglicht, kundenorientierte, nachhaltige und gewinnbringende Direkt-Mailing Kampagnen durchzuführen."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) ist eine Plattform zur Automatisierung von Direkt-Mailings, mit der Sie kundenorientierte, nachhaltige und gewinnbringende Kampagnen durchführen können. 

_Diese Integration wird von optilyz gepflegt._

## Über die Integration

Nutzen Sie die Integration von Optilyz und Braze-Webhooks, um Ihren Kund:inen Direkt-Mailings wie Briefe, Postkarten und Selfmailer zu senden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Optilyz-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Optilyz-Konto. |
| optilyz API-Schlüssel<br><br>`<OPTILYZ_API_KEY>`| Ihr Customer-Success-Manager:in stellt Ihnen Ihren optilyz API-Schlüssel zur Verfügung.<br><br>Dieser API-Schlüssel ermöglicht es Ihnen, Ihre Braze- und Optilyz-Konten zu verbinden. |
| optilyz Automatisierung ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | Die ID für die Automatisierung finden Sie in einem Feld in der Kopfzeile der Seite.<br><br>Wenn Sie bei Optilyz angemeldet sind, können Sie zu der Automatisierung navigieren, an die Sie Daten senden möchten.<br>Die Automatisierung muss zuerst aktiviert werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anwendungsfälle

Direkt-Mailing wie einen digitalen Kanal zu betreiben bedeutet, sich von Massenmailings zu lösen und den Kanal als Teil Ihrer (digitalen) Customer Journey zu nutzen. Die Vorteile eines modernen Ansatzes für Direkt-Mailing sind:
- Gesteigerte Konversionsraten durch erhöhte Relevanz, zusätzliche Anwendungsfälle, einfachere A/B-Tests und kanalübergreifende Effekte
- Geringerer Aufwand durch Automatisierung und eine End-to-End Lösung
- Geringere Kosten durch Rahmenverträge und Kostentransparenz

## Integration

Für die Integration mit Optilyz verwenden Sie die [Optilyz API](https://www.optilyz.com/doc/api/), um Empfänger:innen-Daten an den Braze-Webhook zu senden.

### Schritt 1: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Um eine Optilyz Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, navigieren Sie in der Braze-Plattform zu **Templates** > **Webhook-Vorlagen**. 

Wenn Sie eine einmalige Optilyz-Webhook-Kampagne erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

Füllen Sie in Ihrem neuen Webhook Template die folgenden Felder aus:
- **Webhook URL**: Die Webhook-URL ist für jeden Kunden eindeutig und wird Ihnen von Ihrem Optilyz Customer-Success-Manager:in zur Verfügung gestellt.
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

optilyz benötigt außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber im Tab **Einstellungen** müssen Sie `<OPTILYZ_API_KEY>` durch Ihren Optilyz API-Schlüssel ersetzen. Dieser Schlüssel muss ein ":" direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein. 

- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Typ**: application/json

![Die Anfrage-Header und die HTTP-Methode, die im Braze-Webhook-Builder angezeigt werden.]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Anfragetext

In der folgenden Anfrage können Sie beliebige Liquid-Tags zur Personalisierung verwenden und ein angepasstes Template für die Anfrage gemäß der [API-Dokumentation](https://www.optilyz.com/doc/api/) von Optilyz erstellen.

Das Feld `variation` ist optional und kann festlegen, welcher Entwurf innerhalb der Automatisierung verwendet werden soll. Wird eine Variante ausgelassen, weist Optilyz eine der definierten Varianten nach dem Zufallsprinzip zu.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Ein Bild des Codes des Anfragekörpers und der Webhook-URL, die auf dem Braze Webhook Builder Tab angezeigt werden.]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### Schritt 2: Vorschau auf Ihre Anfrage

Als Nächstes erhalten Sie eine Vorschau Ihrer Anfrage im Panel **Vorschau** oder Sie wechseln zum Tab **Test**, wo Sie einen zufälligen Nutzer, einen bestehenden Nutzer:innen auswählen oder Ihren eigenen Nutzer anpassen können, um Ihren Webhook zu testen. Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen!

![Verschiedene Testfelder, die im Tab Test des Braze Webhook Builders verfügbar sind.]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}



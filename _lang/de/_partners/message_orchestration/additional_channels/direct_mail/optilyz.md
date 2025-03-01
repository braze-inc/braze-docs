---
nav_title: optilyz
article_title: optilyz
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und optilyz, die es Ihnen ermöglicht, kundenorientiertere, nachhaltigere und profitablere Direktmailing-Kampagnen durchzuführen."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz][1] ist eine Plattform zur Automatisierung von Direktmailings, mit der Sie kundenorientierte, nachhaltige und profitable Direktmailing-Kampagnen durchführen können. 

Verwenden Sie die Webhook-Integration von optilyz und Braze, um Ihren Kunden Direktwerbung wie Briefe, Postkarten und Selfmailer zu senden.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|optilyz-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein optilyz-Konto. |
| optilyz API-Schlüssel<br><br>`<OPTILYZ_API_KEY>`| Ihr optilyz Customer Success Manager wird Ihnen Ihren optilyz API-Schlüssel mitteilen.<br><br>Mit diesem API-Schlüssel können Sie Ihre Konten bei Braze und optilyz verbinden. |
| optilyz automation ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | Die Automatisierungs-ID finden Sie in einem Feld in der Kopfzeile der Seite.<br><br>Wenn Sie bei optilyz angemeldet sind, können Sie zu der Automatisierung navigieren, an die Sie Daten senden möchten.<br>Die Automatisierung muss zuerst aktiviert werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Anwendungsfälle

Direktwerbung wie einen digitalen Kanal zu betreiben, bedeutet, sich von Massenmailings zu verabschieden und den Kanal als Teil Ihrer (digitalen) Customer Journey zu nutzen. Die Vorteile eines modernen Ansatzes für Direktwerbung sind:
- Höhere Konversionsraten durch erhöhte Relevanz, zusätzliche Anwendungsfälle, einfachere A/B-Tests und kanalübergreifende Effekte
- Geringerer Aufwand durch Automatisierung und eine End-to-End-Lösung
- Geringere Kosten durch Rahmenverträge und Kostentransparenz

## Integration

Zur Integration mit optilyz verwenden Sie die [optilyz API][2], um Empfängerdaten an den Braze Webhook zu senden.

### Schritt 1: Erstellen Sie Ihre Braze Webhook-Vorlage

Um eine optilyz Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvases verwenden können, navigieren Sie zu **Vorlagen** > **Webhook-Vorlagen** in der Braze-Plattform. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige optilyz Webhook-Kampagne erstellen oder eine bestehende Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

Füllen Sie in Ihrer neuen Webhook-Vorlage die folgenden Felder aus:
- **Webhook URL**: Die Webhook-URL ist für jeden Kunden einzigartig und wird Ihnen von Ihrem optilyz Customer Success Manager mitgeteilt.
- **Anfrage Körper**: Rohtext

#### Kopfzeilen der Anfrage und Methode

optilyz benötigt außerdem einen HTTP-Header für die Autorisierung und eine HTTP-Methode. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf der Registerkarte **Einstellungen** müssen Sie `<OPTILYZ_API_KEY>` durch Ihren optilyz API-Schlüssel ersetzen. Dieser Schlüssel muss ein ":" direkt nach dem Schlüssel enthalten und in Base 64 kodiert sein. 

- **HTTP-Methode**: POST
- **Kopfzeilen anfordern**:
  - **Autorisierung**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Inhalt-Typ**: application/json

![Die Anfrage-Header und HTTP-Methode, die im Braze Webhook-Builder angezeigt werden.][6]{: style="max-width:50%"}

#### Anfragetext

Im folgenden Anfragekörper können Sie beliebige Liquid-Personalisierungs-Tags verwenden und eine benutzerdefinierte Anfragevorlage gemäß der [API-Dokumentation][2] von optilyz erstellen.

Das Feld `variation` ist optional und kann festlegen, welcher Entwurf innerhalb der Automatisierung verwendet werden soll. Wird eine Variante ausgelassen, weist optilyz eine der definierten Varianten nach dem Zufallsprinzip zu.

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

![Ein Bild des Anfrage-Body-Codes und der Webhook-URL, die in der Registerkarte Komposition des Braze Webhook-Builders angezeigt werden.][5]

### Schritt 2: Vorschau Ihrer Anfrage

Als Nächstes sehen Sie sich Ihre Anfrage im Bereich **Vorschau** an oder gehen Sie auf die Registerkarte **Test**, wo Sie einen zufälligen Benutzer, einen bestehenden Benutzer oder einen eigenen Benutzer auswählen können, um Ihren Webhook zu testen. Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen!

![Verschiedene Testfelder, die auf der Registerkarte Test des Braze Webhook Builders verfügbar sind.][7]

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
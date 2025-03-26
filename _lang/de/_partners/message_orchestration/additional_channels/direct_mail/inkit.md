---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Inkit, die es Ihnen ermöglicht, Zeit und Mühe zu sparen, indem Sie Ihre Direktmailing-Kampagnen automatisieren und Offline-Kunden wieder online bringen."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit][1] und Braze ermöglichen es Unternehmen, Dokumente sicher zu erstellen und zu verteilen - sowohl digital als auch per Direktmailing.

Die Integration von Braze und Inkit ermöglicht es Ihnen, Dokumente zu erstellen und sie mit Braze-Webhooks direkt an Braze-Benutzer zu versenden.

## Voraussetzungen

|Anforderung| Beschreibung|
| ---| ---|
|Inkit-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Inkit-Konto](https://www.inkit.com/). |
| Inkit API-Schlüssel<br><br>`<INKIT_API_TOKEN>` | Diesen Schlüssel finden Sie auf Ihrem [Inkit Dashboard](https://app.inkit.io/#/account/integrations) unter der Registerkarte **Entwicklung** und ermöglicht es Ihnen, Ihre Braze- und Inkit-Konten zu verbinden.|
| Inkit Vorlage ID<br><br>`<INKIT_TEMPLATE_ID>` | Nachdem Sie eine Vorlage erstellt haben, können Sie die ID der Vorlage aus der Registerkarte **Vorlagen** kopieren und in Ihrer Vorlage in Braze verwenden.<br><br>Sie könnten zum Beispiel in der Inkit-Umgebung eine Vorlage namens `invoice_template` mit der Vorlagen-ID `tmpl_3bDScFl9cwr3OAVR1RSdEC` erstellen.
| HTTP-Kopfzeile | Der HTTP-Header ist Teil der API-Anfrage, die Sie von Braze an Inkit senden. Darin geben Sie Ihren Inkit-API-Schlüssel an, um Anrufe bei der Inkit-API zu authentifizieren und zu autorisieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Eine Inkit-Vorlage erstellen

Erstellen Sie auf der Inkit-Plattform eine Vorlage, die Sie in Ihrer Braze-Kampagne in HTML, Word, PowerPoint, Excel oder PDF verwenden können. Lesen Sie die [Inkit-Dokumentation](https://docs.inkit.com/docs/create-a-template), um mehr zu erfahren.

### Schritt 2: Erstellen Sie Ihre Braze Webhook-Vorlage

Um eine Inkit-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvases verwenden können, navigieren Sie auf der Braze-Plattform zu **Vorlagen** > **Webhook-Vorlagen**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, gehen Sie zu **Engagement** > **Vorlagen & Medien** > **Webhook-Vorlagen**.
{% endalert %}

Wenn Sie eine einmalige Inkit-Webhook-Kampagne erstellen oder eine vorhandene Vorlage verwenden möchten, wählen Sie **Webhook** in Braze, wenn Sie eine neue Kampagne erstellen.

![Eine Auswahl der verfügbaren vorgefertigten Webhook-Vorlagen auf der Registerkarte Webhook-Vorlagen im Bereich Vorlagen & Medien.][7]

Sobald Sie die Inkit Webhook-Vorlage ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: Leer
- **Anfrage Körper**: Rohtext

Im Feld Webhook URL müssen Sie eine Inkit Webhook URL [erstellen](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) und eingeben.

![Der Bodycode der Anfrage und die Webhook-URL werden auf der Registerkarte Komposition des Braze Webhook-Builders angezeigt.][5]

#### Kopfzeilen der Anfrage und Methode

Inkit erfordert eine `HTTP Header` für die Autorisierung, einschließlich Ihres Inkit API-Schlüssels, der in Base 64 verschlüsselt ist. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf der Registerkarte **Einstellungen** müssen Sie `<INKIT_API_TOKEN>` durch Ihren Inkit-API-Schlüssel ersetzen.

{% raw %}
- **HTTP-Methode**: POST
- **Kopfzeile der Anfrage**:
  - **Autorisierung**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Inhalt-Typ**: application/json
{% endraw %}

#### Anfragetext

Vergewissern Sie sich, dass Ihre Flüssigkeit den richtigen benutzerdefinierten Attributen entspricht, die mit den folgenden erforderlichen und optionalen Feldern verbunden sind. Sie können auch benutzerdefinierte Datenfelder zu jeder Anfrage hinzufügen.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Schritt 3: Vorschau Ihrer Anfrage

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um ein anwendbares Braze-Tag handelt. `street` `unit` , `state` und `zip` müssen als [benutzerdefinierte Attribute][3] eingerichtet werden, um diesen Webhook zu senden.

Zeigen Sie Ihre Anfrage in der **Vorschau** an oder wechseln Sie zur Registerkarte **Test**, wo Sie einen zufälligen Benutzer, einen vorhandenen Benutzer oder einen eigenen Benutzer auswählen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihre Vorlage zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Vorlagen finden Sie in der Liste **Gespeicherte Webhook-Vorlagen**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}

[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/nachrichten_erstellung_durch_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}
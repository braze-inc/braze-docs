---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Inkit, die es Ihnen ermöglicht, Zeit und Mühe zu sparen, indem Sie Ihre Direkt-Mailing Kampagnen automatisieren und Offline-Kunden wieder online bringen."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) und Braze ermöglichen es Unternehmen, Dokumente sicher zu erstellen und zu verteilen - sowohl digital als auch per Direkt-Mailing.

_Diese Integration wird von Inkit gepflegt._

## Über die Integration

Die Integration von Braze und Inkit erlaubt es Ihnen, mit Braze-to-Braze-Webhooks Dokumente zu erstellen und diese direkt an Nutzer:innen zu versenden.

## Voraussetzungen

|Anforderung| Beschreibung|
| ---| ---|
|Inkit-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Inkit-Konto](https://www.inkit.com/). |
| Inkit API-Schlüssel<br><br>`<INKIT_API_TOKEN>` | Dieser Schlüssel befindet sich auf Ihrem [Inkit Dashboard](https://app.inkit.io/#/account/integrations) unter dem Tab **Entwicklung** und ermöglicht es Ihnen, Ihre Braze- und Inkit-Konten zu verbinden.|
| Inkit Template ID<br><br>`<INKIT_TEMPLATE_ID>` | Nachdem Sie eine Vorlage erstellt haben, können Sie die ID der Vorlage aus dem Tab **Vorlagen** kopieren, um sie in Ihrer Vorlage in Braze zu verwenden.<br><br>Sie könnten zum Beispiel in der Inkit-Umgebung ein Template namens `invoice_template` mit der Template ID: `tmpl_3bDScFl9cwr3OAVR1RSdEC` erstellen.
| HTTP-Kopfzeile | Der HTTP-Header ist Teil der API-Anfrage, die Sie von Braze an Inkit senden. Darin enthalten ist Ihr Inkit API-Schlüssel zur Authentifizierung und Autorisierung von Aufrufen der Inkit API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Eine Inkit-Vorlage erstellen

Erstellen Sie auf der Inkit-Plattform ein Template, das Sie in Ihrer Braze Kampagne in HTML, Word, PowerPoint, Excel oder PDF verwenden können. Lesen Sie die [Dokumentation von Inkit](https://docs.inkit.com/docs/create-a-template), um mehr zu erfahren.

### Schritt 2: Erstellen Sie Ihr Braze-to-Braze-Webhook Template

Um eine Inkit-Webhook-Vorlage zu erstellen, die Sie in zukünftigen Kampagnen oder Canvase verwenden können, navigieren Sie auf der Braze-Plattform zu **Templates** > **Webhook-Vorlagen**. 

Wenn Sie eine einmalige Inkit-Webhook-Kampagne erstellen oder ein bestehendes Template verwenden möchten, wählen Sie bei der Erstellung einer neuen Kampagne **Webhook** in Braze aus.

![Eine Auswahl der verfügbaren vorgefertigten Webhook-Templates finden Sie auf dem Tab Webhook Templates im Bereich Templates und Medien.]({% image_buster /assets/img/inkit-webhook-template.png %})

Sobald Sie das Inkit Webhook Template ausgewählt haben, sollten Sie folgendes sehen:
- **Webhook URL**: Leer
- **Anfrage Körper**: Rohtext

Im Feld Webhook URL müssen Sie eine Inkit Webhook URL [erstellen](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) und eingeben.

![Der Code des Anfragekörpers und die Webhook-URL werden im Tab "Braze webhook builder compose" angezeigt.]({% image_buster /assets/img/inkit-integration.png %})

#### Kopfzeilen der Anfrage und Methode

Inkit benötigt eine `HTTP Header` für die Autorisierung, einschließlich Ihres Inkit API-Schlüssels, der in Base 64 verschlüsselt ist. Das Folgende ist bereits als Schlüssel-Wert-Paar in der Vorlage enthalten, aber auf dem Tab **Einstellungen** müssen Sie `<INKIT_API_TOKEN>` durch Ihren Inkit API-Schlüssel ersetzen.

{% raw %}
- **HTTP-Methode**: POST
- **Anfrage-Header**:
  - **Autorisierung**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Typ**: application/json
{% endraw %}

#### Anfragetext

Vergewissern Sie sich, dass Ihr Liquid die richtigen angepassten Attribute enthält, die mit den folgenden obligatorischen und optionalen Feldern verbunden sind. Sie können auch angepasste Datenfelder zu jeder Anfrage hinzufügen.

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

### Schritt 3: Vorschau auf Ihre Anfrage

Ihr Rohtext wird automatisch hervorgehoben, wenn es sich um einen passenden Braze Tag handelt. `street`, `unit`, `state` und `zip` müssen als [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) eingerichtet werden, um diesen Webhook zu senden.

Eine Vorschau Ihrer Anfrage finden Sie im Panel **Vorschau** oder auf dem Tab **Test**, wo Sie einen zufälligen Nutzer, einen bestehenden Nutzer:innen auswählen oder Ihren eigenen anpassen können, um Ihren Webhook zu testen.

{% alert important %}
Denken Sie daran, Ihr Template zu speichern, bevor Sie die Seite verlassen! <br>Aktualisierte Webhook-Templates finden Sie in der Liste **Gespeicherte Webhook-Templates**, wenn Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) erstellen.
{% endalert %}



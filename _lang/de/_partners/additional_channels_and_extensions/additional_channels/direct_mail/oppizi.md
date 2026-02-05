---
nav_title: Oppizi
article_title: Oppizi 
alias: /partners/oppizi/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) ist weltweit führend im Offline Marketing und bietet Unternehmen eine Lösung aus einer Hand, um messbare, zielgerichtete Direkt-Mailing und Flyer Kampagnen durchzuführen.

_Diese Integration wird von Oppizi gepflegt._

## Voraussetzungen

| Anforderung                    | Beschreibung                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Oppizi Konto                 | Um diese Integration zu nutzen, benötigen Sie ein aktives Oppizi-Konto.                 |
| Oppizi API-Schlüssel                 | Zu finden in Ihrem Oppizi-Konto unter **Integrationen** > Braze.                |
| Oppizi Direkt-Mailing Workflow ID | Erstellen Sie einen Workflow in Oppizi auf der Seite **Direkt-Mailing Workflow**, um eine ID zu erhalten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Oppizi Integration können Sie:

* **Versenden Sie automatisierte Direkt-Mailing-Postkarten** mit Braze-Triggern, die mit den Webhook- und Direkt-Mailing-Workflows von Oppizi verbunden sind.
* **Konfigurieren Sie Schwellenwerte, Wellen und Limits** in den Direkt-Mailing-Workflows von Oppizi, um den Versand Ihrer Kampagnen zu steuern.
* **Entwerfen Sie professionelle Postkarten** mit dem integrierten Design-Tool von Oppizi - es sind keine Designkenntnisse erforderlich.
* **Verfolgen Sie die Performance von Kampagnen** in Realtime mit dem Dashboard von Oppizi.

## Integration

### Schritt 1: Generieren Sie Ihren Oppizi API-Schlüssel 

Um Ihr Webhook Template in Braze zu verwenden, müssen Sie zunächst Ihren Oppizi API-Schlüssel generieren.

1. Melden Sie sich bei Oppizi an.
2. Gehen Sie zu **Integrationen** > **Braze**.
3. Generieren Sie Ihren API-Schlüssel.

Von dieser Seite aus können Sie Ihre Schlüssel nach Bedarf verwalten, widerrufen und erstellen.

### Schritt 2: Erstellen Sie eine Braze-to-Braze-Webhook-Vorlage

Als nächstes erstellen Sie ein Webhook Template für Oppizi in Braze, das Sie in zukünftigen Kampagnen oder Canvase verwenden können.

1. Gehen Sie in Braze zu **Templates** > Webhook-Vorlagen.

Füllen Sie in Ihrem Webhook Template die folgenden Felder aus:

- **Webhook URL:** ```https://webhooks.oppizi.com/events```
- **Körper der Anfrage:** **Rohtext**

Für die Anfrage-Methode und die Header benötigt Oppizi eine HTTP-Methode sowie die folgenden HTTP-Header, die in das Template aufgenommen werden müssen. Füllen Sie die folgenden Felder aus:

- **HTTP-Methode:** POST
- **Anfrage-Header:**
  - **Autorisierung:** `Bearer <oppiziAPIKey>`
  - **Content-Typ:** `application/json`

![Ein Beispiel für den Oppizi-Webhook-Header in Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

In den **Body der Anfrage** müssen Sie das Feld **oppiziWorkflowID** aufnehmen. Diese ID wird bei der Erstellung eines Workflows in Oppiz generiert und wird benötigt, um anzugeben, zu welchem Direkt-Mailing-Workflow Ihre Empfänger:in hinzugefügt werden sollen. Jeder Direkt-Mailing-Workflow in Oppizi hat eine eindeutige ID. Wenn Sie also eine Oppizi-Webhook-Vorlage in Braze erstellen, stellen Sie sicher, dass Sie die Workflow-ID immer auf die richtige ID aktualisieren.

{% alert note %}
Überprüfen Sie, ob in Ihrem Braze-Konto die erforderlichen angepassten Attribute für die Postadressen Ihrer Empfänger:innen eingerichtet sind, da diese für den Versand von Direkt-Mailing erforderlich sind.
{% endalert %}

![Ein Beispiel für ein Oppizi-Webhook Template in Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

Im Folgenden finden Sie ein Beispiel für einen Anfragetext:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Schritt 3: Erstellen Sie einen Direkt-Mailing-Workflow in Oppizi

1. Gehen Sie in Oppizi zu **Direkt-Mailing Workflow** > **Workflow erstellen**
2. Konfigurieren Sie Details zum Workflow, einschließlich Schwellenwerte, Wellen, Postkartenformat und Druckvorlagen.
3. Im Abschnitt Webhook-Details finden Sie einen gebrauchsfertigen Anfragetext, einschließlich Ihrer Workflow ID, den Sie direkt in Braze einfügen können.

### Schritt 4: Vorschau und Test Ihrer Anfrage in Braze

Nachdem Sie den Body Ihrer Anfrage mit der Workflow ID von Oppizi hinzugefügt haben, führen Sie einen Test durch, um zu überprüfen, ob Ihre Einrichtung wie erwartet funktioniert.

Um den Test durchzuführen, aktualisieren Sie `requestType` von `live` auf `test` im Textkörper der Anfrage. Beachten Sie, dass dieser Schritt wichtig ist, um zu verhindern, dass Testempfänger:in zu Ihrer Direkt-Mailing Zielgruppe hinzugefügt werden.

Nachdem Sie die Tests abgeschlossen haben, aktualisieren Sie `requestType` wieder auf `live` und speichern Ihr Canvas. Jetzt sind Sie bereit, Ihre automatisierten Direkt-Mailing Kampagnen einzuführen.

---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Zapier, einem Internet-Automatisierungstool, das es Ihnen erlaubt, Daten zwischen Web-Apps auszutauschen und diese Informationen zur Automatisierung von Aktionen zu nutzen."
page_type: partner
search_tag: Partner

---
# Zapier-Integration

> [Zapier](https://zapier.com/) ist ein Internet-Tool für die Automatisierung, das es Ihnen erlaubt, Daten zwischen Web-Apps auszutauschen und diese Informationen dann zur Automatisierung von Aktionen zu verwenden. 

Die Partnerschaft zwischen Braze und Zapier nutzt die Braze API und die [Braze-Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) für die Verbindung mit Anwendungen von Drittanbietern - wie Google Workplace, Slack, Salesforce, WordPress usw. - um verschiedene Aktionen zu automatisieren.

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Zapier-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zapier-Konto. |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#api-definitions) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Im folgenden Zapier-Beispiel senden wir Informationen von WordPress an Braze über einen POST Webhook. Diese Informationen können dann zur Erstellung eines Braze-Canvas verwendet werden.

### Schritt 1: Erstellen Sie einen Zapier Trigger

In der Terminologie von Zapier ist ein "Zap" ein automatisierter Workflow, der Ihre Apps und Dienste miteinander verbindet. Der erste Teil eines Zaps besteht darin, einen Trigger zu bestimmen. Nachdem Ihr Zap aktiviert wurde, führt Zapier automatisch die entsprechenden Aktionen aus, sobald Ihr Trigger erkannt wird.

Anhand unseres WordPress-Beispiels richten wir in der Zapier-Plattform unseren Zap so ein, dass er triggert, wenn ein neuer WordPress-Beitrag hinzugefügt wird, und wählen als **Beitragsstatus** und **Beitragstyp** **Veröffentlicht** und **Beiträge** aus. 

![Wählen Sie in der Zapier-Plattform innerhalb eines Zap einen Auslöser aus, der ein "neuer Kommentar", ein "beliebiger Webhook" oder ein "neuer Beitrag" ist. In diesem Beispiel ist "neuer Beitrag" ausgewählt. ] [5]

![In der Zapier-Plattform konfigurieren Sie den Trigger innerhalb eines Zap, indem Sie den gewünschten Post-Status und Post-Typ auswählen. In diesem Beispiel ist "Veröffentlicht" und "Beiträge" ausgewählt.] [6]

### Schritt 2: Einen Webhook für eine Aktion hinzufügen

Definieren Sie als nächstes die Zapp-Aktion. Wenn Ihr Zapper aktiviert ist und Ihr Trigger erkannt wird, wird die Aktion automatisch ausgeführt.

Um unser Beispiel fortzusetzen, möchten wir eine POST-Anfrage als JSON an einen Braze Endpunkt senden. Wählen Sie dazu unter **Apps** die Option **Webhooks** aus.

![]({% image_buster /assets/img_archive/zapier3.png %})

### Schritt 3: Braze POST einrichten

Wenn Sie Ihren Webhook einrichten, verwenden Sie die folgenden Einstellungen und geben Sie Ihren Braze-REST-Endpunkt in der Webhook-URL an. Wenn Sie fertig sind, wählen Sie **Veröffentlichen**.

- **Methode**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Pass-Though Daten**: Falsch
- **Unflat**: Kein:e
- **Anfrage-Header**:
  - **Content-Typ**: application/json
  - **Autorisierung**: Überbringer YOUR-API-KEY
- **Daten**: 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Schritt 4: Erstellen Sie eine Braze Kampagne

Sobald Sie Ihr ZAP erfolgreich eingerichtet haben, können Sie Ihre Braze-Kampagnen oder Canvase mit WordPress-Daten anpassen, indem Sie die Daten in Ihren Nachrichten mit Liquid formatieren.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}

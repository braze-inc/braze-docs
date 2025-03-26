---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zapier, einem Webtool zur Automatisierung, mit dem Sie Daten zwischen Webanwendungen austauschen und diese Informationen zur Automatisierung von Aktionen nutzen können."
page_type: partner
search_tag: Partner

---
# Zapier-Integration

> [Zapier][1] ist ein Webtool für die Automatisierung, mit dem Sie Daten zwischen Webanwendungen austauschen und diese Informationen dann zur Automatisierung von Aktionen verwenden können. 

Die Partnerschaft zwischen Braze und Zapier nutzt die Braze-API und die [Braze-Webhooks][3], um sich mit Anwendungen von Drittanbietern zu verbinden, z. B. Google Workplace, Slack, Salesforce, WordPress usw., um verschiedene Aktionen zu automatisieren.

## Voraussetzungen

| Anforderungen | Beschreibung |
|---|---|
| Zapier-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Zapier-Konto. |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][0] ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Im folgenden Zapier-Beispiel werden wir Informationen von WordPress an Braze senden, indem wir einen POST-Webhook verwenden. Diese Informationen können dann zur Erstellung eines Braze Canvas verwendet werden.

### Schritt 1: Erstellen Sie einen Zapier-Auslöser

In der Terminologie von Zapier ist ein "Zap" ein automatisierter Workflow, der Ihre Anwendungen und Dienste miteinander verbindet. Der erste Teil eines Zaps besteht darin, einen Auslöser zu bestimmen. Nachdem Ihr Zap aktiviert ist, führt Zapier automatisch die entsprechenden Aktionen aus, sobald Ihr Auslöser erkannt wird.

Anhand unseres WordPress-Beispiels richten wir in der Zapier-Plattform unseren Zap so ein, dass er ausgelöst wird, wenn ein neuer WordPress-Beitrag hinzugefügt wird, und wählen **Veröffentlicht** und **Beiträge** als **Beitragsstatus** und **Beitragstyp** aus. 

![Wählen Sie in der Zapier-Plattform in einem Zap den Auslöser für einen "neuen Kommentar", einen "beliebigen Webhook" oder einen "neuen Beitrag". Für dieses Beispiel wird "neuer Beitrag" ausgewählt. ] [5]

![In der Zapier-Plattform konfigurieren Sie den Auslöser in einem Zap, indem Sie den gewünschten Post-Status und Post-Typ auswählen. In diesem Beispiel ist "Veröffentlicht" und "Beiträge" ausgewählt.] [6]

### Schritt 2: Einen Aktions-Webhook hinzufügen

Definieren Sie als nächstes die Zapp-Aktion. Wenn Ihr Zapper aktiviert ist und Ihr Auslöser erkannt wird, wird die Aktion automatisch ausgeführt.

Um unser Beispiel fortzusetzen, möchten wir eine POST-Anfrage als JSON an einen Braze-Endpunkt senden. Dazu wählen Sie unter **Apps** die Option **Webhooks**.

![][7]

### Schritt 3: Einrichten von Braze POST

Wenn Sie Ihren Webhook einrichten, verwenden Sie die folgenden Einstellungen und geben Sie Ihren Braze REST-Endpunkt in der Webhook-URL an. Wenn Sie fertig sind, wählen Sie **Veröffentlichen**.

- **Methode**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Though**: Falsch
- **Unflat**: Kein:e
- **Kopfzeile der Anfrage**:
  - **Inhalt-Typ**: application/json
  - **Autorisierung**: Träger YOUR-API-KEY
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

![][4]{: style="max-width:70%;"}

### Schritt 4: Erstellen Sie eine Braze-Kampagne

Sobald Sie Ihr Zap erfolgreich eingerichtet haben, können Sie Ihre Braze-Kampagnen oder Canvases mit WordPress-Daten anpassen, indem Sie die Informationen in Ihren Nachrichten mit Liquid formatieren.

[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[4]:{% image_buster /assets/img/zapier.png %}
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[12]:{% image_buster /assets/img_archive/zapier6.png %}
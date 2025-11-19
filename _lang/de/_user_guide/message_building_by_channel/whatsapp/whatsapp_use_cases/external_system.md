---
nav_title: WhatsApp und externes System
article_title: Integration von Braze und WhatsApp mit einem externen System
page_order: 2
description: "Dieser referenzierte Artikel enthält eine Schritt-für-Schritt-Anleitung für die Integration der Braze- und WhatsApp-Integration mit einer externen KI oder einem Kommunikationssystem."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integration von Braze und WhatsApp mit einem externen KI- oder Kommunikationssystem

> Nutzen Sie die leistungsstarken KI-Chatbots und Live-Agentenübergaben auf dem WhatsApp-Kanal, um Ihre Kund:in zu rationalisieren. Durch die Automatisierung von Routineanfragen und den nahtlosen Übergang zu menschlichen Agenten, wenn dies erforderlich ist, können Sie die Antwortzeiten erheblich verbessern und das Kundenerlebnis insgesamt steigern.

## Funktionsweise

Die Integration zwischen Braze und der externen KI oder dem Kommunikationssystem funktioniert wie eine Zweibahnstraße, bei der Braze der Kommunikationskanal und das externe System die "Intelligenz" ist, die Nachrichten verarbeitet und Antworten formuliert.

Der Integrations-Workflow kann in zwei Hauptabläufe unterteilt werden:
**Eingehender Fluss:** Die Nachricht eines Nutzers:innen kommt in Braze an und wird dann zur Verarbeitung an Ihr externes System weitergeleitet.
**Ausgehender Fluss:** Nach der Verarbeitung der Nachricht sendet Ihr externes System eine Antwort an Braze, das dann die Nachricht an den Endnutzer:in zustellt.

Um diese Kommunikation effizient zu automatisieren, nutzt diese Integration zwei wichtige Features von Braze: [Webhook-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) und [API-getriggerte Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

![Architektur der Integration zwischen dem Braze WhatsApp-Kanal und einem externen System.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Architektur der Integration zwischen dem Braze WhatsApp-Kanal und einem externen System.*</sup>

## Voraussetzungen

| Voraussetzung | Beschreibung |
| - | - |
| Externes System | Ein KI- oder Kommunikationssystem eines Drittanbieters, das in der Lage ist, Chatbots, automatisierte Systeme für den Client-Dienst über APIs oder beides zu erstellen und zu verwalten. |
| Integration von Braze und WhatsApp | Eine von Braze verwaltete WhatsApp-Nummer |
| REST-API-Schlüssel von Braze | Ein REST-API-Schlüssel mit `campaigns.trigger.send` Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Konfigurieren der Integration

### Schritt 1: Erstellen Sie eine Webhook-Kampagne für eingehende Nachrichten

Erstellen Sie zunächst eine Webhook-Kampagne, um eine Möglichkeit zu schaffen, von Braze empfangene WhatsApp-Nachrichten an Ihr externes System zu senden.

1. Erstellen Sie in Braze eine Webhook-Kampagne.
2. Wählen Sie im Webhook Composer **Webhook erstellen** aus.
3. Geben Sie in das Feld **Webhook URL** den API Endpunkt (URL) für das externe System ein, das die Nachricht erhalten soll.
4. Wählen Sie **Rohtext** für den Körper der Anfrage aus und geben Sie eine Nutzlast mit Personalisierung ein, die die `external_id` und die Telefonnummer des Nutzers:innen, den Inhalt der Nachricht und andere relevante Informationen enthält, z.B:

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5\. Wählen Sie im Schritt **Zustellung planen** Ihres Kampagnen-Editors für die Art der Zustellung die Option **Aktionsbasiert** und für den Auslöser der Kampagne die Option **Eingehende WhatsApp Nachricht senden**.

![Aktionsbasierte Zustellung mit einem Trigger für das Senden einer eingehenden WhatsApp Nachricht.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Stellen Sie Ihre Kampagne fertig, speichern Sie sie und starten Sie sie. Jetzt sendet Braze jedes Mal, wenn eine Nachricht eingeht, einen Webhook an Ihr externes System.

### Schritt 2: Erstellen Sie eine API-getriggerte Kampagne für ausgehende Nachrichten {#step-2}

Als nächstes erstellen Sie eine API-getriggerte Kampagne, mit der Ihr externes System Nachrichten über WhatsApp an Nutzer:innen senden kann.

1. Erstellen Sie in Braze eine WhatsApp Kampagne. 
2. Wählen Sie im Nachrichten-Editor entweder die **WhatsApp-Vorlage Nachricht** oder die **Antwort Nachricht** aus und wählen Sie dann das Layout der Vorlage oder der Antwort Nachricht aus. Sie können ein beliebiges Layout für Antwortnachrichten auswählen, da die eingehende Nachricht das 24-Stunden-WhatsApp-Fenster geöffnet hat.

![Nachrichten-Editor mit Optionen zum Auswählen des Nachrichtentyps und des Nachrichtenlayouts.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Fügen Sie die Eigenschaft API-Trigger in den Nachrichtentext ein, z.B. {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Dies erlaubt es Ihrem KI-System, die zu versendende Nachricht zu füllen.

![Nachrichten-Editor mit Nachrichtenkörper, der triggernde Eigenschaften enthält.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. Wählen Sie im Schritt **Zeitplan Zustellung** Ihres Kampagnen-Composers als Zustellungsart **Aktionsbasiert** aus.
5\. Speichern Sie die Kampagne, und notieren Sie sich die eindeutige `campaign_id`, die Braze für diese Kampagne erstellt. Sie benötigen die ID für den nächsten Schritt.

### Schritt 3: Verbinden Sie das externe System mit der API-getriggerten Kampagne

Schließlich konfigurieren Sie Ihr externes System so, dass es Braze aufruft und die Antwort sendet.

1. Stellen Sie im Code Ihres externen Systems nach der Verarbeitung der empfangenen Nachricht und der Generierung der Antwort eine POST-Anfrage an den Endpunkt Braze `/messages/send`.
2. Fügen Sie in den Körper der Anfrage `/messages/send` die `campaign_id` aus [Schritt 2](#step-2), die `external_id` des Nutzers:innen und den Inhalt der Antwort des externen Systems ein.
3. Verwenden Sie die Eigenschaft des API-Triggers aus [Schritt 2](#step-2), um die Antwort des externen Systems einzufügen, und vergessen Sie nicht, Ihren API-Schlüssel in den Anfrage-Header zur Authentifizierung aufzunehmen, wie in diesem cURL-Beispiel:

{% raw %}
```json
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"         
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

Jetzt haben Sie eine solide Grundlage für den Aufbau eines KI-Chatbot-Workflows!

### Anpassen Ihres Arbeitsablaufs

Sie können Ihre Integrationslogik erweitern:
- Verwenden Sie verschiedene Schlüsselwörter, um unterschiedliche Webhook-Kampagnen zu triggern.
- Erstellen Sie komplexere Konversationsabläufe mit mehrstufigen, über APIs getriggerten Kampagnen.
- Erfassen Sie Chat-Informationen in Braze als angepasste Attribute, um das Nutzerprofil zu erweitern und zukünftige Kampagnen zu segmentieren.

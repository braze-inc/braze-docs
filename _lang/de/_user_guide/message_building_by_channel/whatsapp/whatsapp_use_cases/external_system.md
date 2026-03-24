---
nav_title: WhatsApp und externe Systeme
article_title: Führen Sie die Integration von Braze und WhatsApp in ein externes System durch.
page_order: 2
description: "Dieser Referenzartikel enthält eine Schritt-für-Schritt-Anleitung zur Integration von Braze und WhatsApp in ein externes KI- oder Kommunikationssystem."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Integrieren Sie Braze und WhatsApp in ein externes KI- oder Kommunikationssystem.

> Nutzen Sie die Leistungsfähigkeit von KI-Chatbots und Live-Agent-Übergaben auf dem WhatsApp-Kanal, um Ihre Kundensupport-Abläufe zu optimieren. Durch die Automatisierung von Routineanfragen und den nahtlosen Übergang zu menschlichen Agenten bei Bedarf können Sie die Reaktionszeiten erheblich verbessern und das Gesamtkundenerlebnis optimieren.

## Funktionsweise

Die Integration zwischen Braze und dem externen KI- oder Kommunikationssystem funktioniert in beide Richtungen, wobei Braze als Kommunikationskanal fungiert und das externe System die „Intelligenz“ darstellt, die Nachrichten verarbeitet und Antworten formuliert.

Der Workflow der Integration lässt sich in zwei Hauptabläufe unterteilen:
**Eingehender Fluss:** Die Nachricht einer Nutzer:in wird an Braze übermittelt und anschließend zur Bearbeitung an Ihr externes System weitergeleitet.
**Ausgehender Fluss:** Nach der Verarbeitung der Nachricht sendet Ihr externes System eine Antwort an Braze, das die Nachricht anschließend an den Endnutzer:in übermittelt.

Um diese Kommunikation effizient zu automatisieren, nutzt diese Integration zwei wichtige Features von Braze: [Webhook-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) und [API-gesteuerte Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

![Architektur der Integration zwischen dem Braze WhatsApp-Kanal und einem externen System.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Architektur der Integration zwischen dem Braze WhatsApp-Kanal und einem externen System.*</sup>

## Voraussetzungen

| Voraussetzung | Beschreibung |
| - | - |
| Externes System | Ein KI- oder Kommunikationssystem eines Drittanbieters, das in der Lage ist, Chatbots, automatisierte Kundendienstsysteme unter Verwendung von APIs oder beides zu erstellen und zu verwalten. |
| Integration von Braze und WhatsApp | Eine von Braze verwaltete WhatsApp-Nummer |
| Braze REST-API-Schlüssel | Ein REST-API-Schlüssel mit entsprechenden`campaigns.trigger.send` Berechtigungen. Dies kann im Braze-Dashboard unter **„Einstellungen“** > **„API-Schlüssel“** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Konfigurieren der Integration

### Schritt 1: Erstellen Sie eine Webhook-Kampagne für eingehende Nachrichten.

Erstellen Sie zunächst eine Webhook-Kampagne, um eine Möglichkeit zu schaffen, die von Braze empfangenen WhatsApp-Nachrichten an Ihr externes System zu senden.

1. Erstellen Sie in Braze eine Webhook-Kampagne.
2. Wählen Sie im Webhook-Composer **die Option „Webhook erstellen“** aus.
3. Bitte geben Sie im Feld **„Webhook-URL“** den API-Endpunkt (URL) für das externe System ein, das die Nachricht empfangen soll.
4. Wählen Sie **„Raw text“** für den Text der Anfrage und geben Sie eine personalisierte Nutzlast ein, die die E-Mail-Adresse und Telefonnummer`external_id` des Nutzers, den Inhalt der Nachricht und andere relevante Informationen enthält, wie zum Beispiel:

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
5\. Wählen Sie im Schritt **„Lieferung planen“** Ihres Kampagnen-Composers **„Aktionsbasierte** **Zust**ellung“ als Liefertyp und **„WhatsApp-Eingehende Nachricht senden“** als Kampagnenauslöser aus.

![Aktionsbasierte Zustellung mit dem Auslöser, eine eingehende WhatsApp-Nachricht zu senden.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Bitte schließen Sie die Erstellung Ihrer Kampagne ab, speichern Sie sie und starten Sie sie anschließend. Nach dem Start der Kampagne sendet Braze bei jedem Empfang einer Nachricht einen Webhook an Ihr externes System.

### Schritt 2: Erstellen Sie eine API-gesteuerte Kampagne für ausgehende Nachrichten. {#step-2}

Erstellen Sie anschließend eine API-gesteuerte Kampagne, um eine Möglichkeit für Ihr externes System zu schaffen, Nachrichten über WhatsApp an die Nutzer:innen zurückzusenden.

1. Erstellen Sie in Braze eine WhatsApp-Kampagne. 
2. Wählen Sie im Nachrichten-Editor entweder **„WhatsApp-Template-Nachricht“** oder **„Antwortnachricht“** aus und wählen Sie anschließend das Layout für das Template oder die Antwortnachricht aus. Sie können ein beliebiges Layout für die Antwortnachricht auswählen, da die eingehende Nachricht das 24-Stunden-WhatsApp-Fenster geöffnet hat.

![Nachrichten-Editor mit Optionen, um den Nachrichtentyp und das Nachrichtenlayout auszuwählen.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Fügen Sie die API-Trigger-Eigenschaft zum Nachrichtentext hinzu, beispielsweise {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Dadurch kann Ihr KI-System die zu versendende Nachricht automatisch ausfüllen.

![Nachrichten-Editor mit Nachrichtentext, der Trigger-Eigenschaften enthält.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. Wählen Sie im Schritt **„Zeitplan für die Zustellung“** Ihres Kampagnen-Composers als Liefertyp **„Aktionsbasierte** Zustellung“ aus.
5\. Bitte speichern Sie die Kampagne und notieren Sie sich die eindeutige`campaign_id`ID, die Braze für diese Kampagne generiert. Für den nächsten Schritt benötigen Sie die ID.

### Schritt 3: Verbinden Sie das externe System mit der API-gesteuerten Kampagne.

Zuletzt konfigurieren Sie Ihr externes System so, dass es Braze aufruft und die Antwort sendet.

1. Bitte führen Sie im Code Ihres externen Systems nach der Verarbeitung der empfangenen Nachricht und der Generierung der Antwort eine POST-Anfrage an den `/messages/send`Braze-Endpunkt durch.
2. Bitte fügen Sie in die`/messages/send`Anfrage die Angaben`campaign_id`aus [Schritt 2](#step-2), die Angaben des Nutzers`external_id`:in und den Inhalt der Antwort des externen Systems ein.
3. Verwenden Sie die API-Trigger-Eigenschaft aus [Schritt 2](#step-2), um die Antwort des externen Systems einzufügen, und vergessen Sie nicht, Ihren API-Schlüssel zur Authentifizierung in den Anfrage-Header aufzunehmen, wie in diesem cURL-Beispiel:

{% raw %}
```bash
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

Nun verfügen Sie über eine solide Grundlage für die Erstellung eines KI-Chatbot-Workflows.

### Passen Sie Ihren Arbeitsablauf an

Sie können Ihre Logik für die Integration erweitern auf:
- Verwenden Sie unterschiedliche Schlüsselwörter, um verschiedene Webhook-Kampagnen zu triggern.
- Erstellen Sie komplexere Konversationsabläufe mit mehrstufigen, API-gesteuerten Kampagnen.
- Speichern Sie Chat-Informationen in Braze als angepasste Attribute, um das Nutzerprofil zu ergänzen und zukünftige Kampagnen zu segmentieren.

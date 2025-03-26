---
nav_title: WSC Sport
article_title: WSC Sport
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und WSC Sports, einer Sportvideoplattform, die es Ihnen ermöglicht, umfangreiche und robuste Sportmedien in Ihre Braze-Push-Benachrichtigungen einzubinden."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sport

> Die [WSC Sports-Plattform][1] erstellt personalisierte Sportvideos für jede digitale Plattform und jeden Sportfan - automatisch und in Echtzeit. 

Die Integration von Braze und WSC Sports ermöglicht es Ihnen, umfangreiche und robuste Sportmedien in Ihre Braze-Push-Benachrichtigungen aufzunehmen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| WSC-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein WSC-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen **Nachrichten**, **Segmente**, **Kampagnen** und **Canvas**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die WSC Sports-Anwendung wickelt den gesamten Prozess ab, von der Auswahl des Videos bis zur Ankunft der Push-Benachrichtigung auf dem Gerät des Endbenutzers. 

### Schritt 1: Wählen Sie die Sendeeinstellungen

![][2]{: style="float:right;max-width:25%;margin-bottom:15px;"}

Bevor Sie mit der Integration beginnen, stellen Sie sicher, dass Sie die gewünschten Kampagnen und Benutzersegmente in Braze erstellt haben. Wenn Sie fertig sind, wählen Sie auf der WSC Sports-Plattform das gewünschte Video aus und wählen Sie in den Sendeeinstellungen das Braze-Benutzersegment und die Kampagnen-ID, die Sie verwenden möchten. Wählen Sie schließlich den Zeitpunkt aus, zu dem Sie Ihre Push-Nachricht versenden möchten. 

#### API-Aufruf

Nach dem Versand wird WSC Sports die Push-Benachrichtigung über die folgenden Braze-Endpunkte an die ausgewählten Benutzersegmente senden, je nach den ausgewählten Optionen:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/nachrichten/senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

Der resultierende Text der Nachricht lautet wie folgt: 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Schritt 2: Test senden

An diesem Punkt sollte Ihre Kampagne bereit sein, um getestet und versendet zu werden. Prüfen Sie die Braze-Fehlermeldungsprotokolle, wenn Sie auf Fehler stoßen. 

[1]: https://wsc-sports.com/
[2]: {% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"

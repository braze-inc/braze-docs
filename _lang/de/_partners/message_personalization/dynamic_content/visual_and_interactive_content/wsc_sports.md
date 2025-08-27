---
nav_title: WSC Sports
article_title: WSC Sports
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und WSC Sports, einer Plattform für Sportvideos, die es Ihnen erlaubt, Rich-Push-Benachrichtigungen in Ihre Braze Push-Benachrichtigungen einzubinden."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> Die [WSC Sports-Plattform](https://wsc-sports.com/) generiert personalisierte Sportvideos für jede digitale Plattform und jeden Sportfan - automatisch und in Realtime. 

_Diese Integration wird von WSC Sports gepflegt._

## Über die Integration

Die Integration von Braze und WSC Sports erlaubt es Ihnen, Rich-Push-Benachrichtigungen mit robusten Sportmedien zu versehen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| WSC-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein WSC-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit **Nachrichten**, **Segmenten**, **Kampagnen** und **Canvas-Berechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Die WSC Sports-Anwendung übernimmt den End-to-End-Prozess, vom Auswählen des Videos bis zum Eintreffen der Push-Benachrichtigung auf dem Gerät des Endnutzers:innen. 

### Schritt 1: Sendeeinstellungen auswählen

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Bevor Sie mit der Integration beginnen, vergewissern Sie sich, dass Sie die gewünschten Kampagnen und Nutzer:innen-Segmente in Braze erstellt haben. Wenn Sie fertig sind, wählen Sie in der WSC Sports-Plattform das gewünschte Video aus und wählen Sie in den Sendeeinstellungen das Segment der Nutzer:innen von Braze und die ID der Kampagne, die Sie verwenden möchten. Wählen Sie schließlich den Zeitpunkt, zu dem Sie Ihre Push Nachricht versenden möchten. 

#### API-Aufruf

Sobald die Push-Benachrichtigung versendet wurde, stellt WSC Sports sie den ausgewählten Segmenten der Nutzer:innen über die folgenden Endpunkte von Braze zu, basierend auf den ausgewählten Optionen:
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/nachrichten/senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

Der Text der Nachricht sieht wie folgt aus: 
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

An diesem Punkt sollte Ihre Kampagne bereit sein, um getestet und versendet zu werden. Prüfen Sie die Protokolle der Braze Fehlermeldungen, wenn Sie auf Fehler stoßen. 



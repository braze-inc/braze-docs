---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und GrowthLoop, einer Plattform, die es Ihnen ermöglicht, Kundendaten direkt aus Data Warehouses zu segmentieren und an Braze zu senden."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) unterstützt Marketingteams bei der Aktivierung von Kundendaten aus dem Cloud Data Warehouse für Braze und andere Kanäle. Automatisieren, skalieren und messen Sie Marketingprogramme von Ihrem Cloud Data Warehouse aus und halten Sie die Daten an einem einzigen, zentralen Ort.

Die Integration von Braze und GrowthLoop ermöglicht es Ihnen, Kundendaten direkt aus dem Data Warehouse zu segmentieren und an Braze zu senden. Dadurch wird sichergestellt, dass die Benutzer die umfangreichen Funktionen von Braze in Verbindung mit ihrer einzigen Wahrheitsquelle optimieren können. Rationalisieren Sie die Marketingbemühungen für die Kundensegmentierung und -aktivierung, indem Sie den Zeitaufwand für die Segmentierung, den Start, das Testen und die Messung der Ergebnisse gezielter Kampagnen, die an Braze gesendet werden, reduzieren.

## Voraussetzungen 

| Anforderung | Beschreibung |
| ----------- | ----------- |
| GrowthLoop Wachstums- oder Unternehmenskonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein GrowthLoop-Konto. |
| Braze Rest API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][2] ab.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Anwendungsfälle

Senden Sie Kundenlisten aus Ihrem Data Warehouse an Braze und richten Sie E-Mail- und Push-Benachrichtigungskampagnen mit einem Klick aus, und halten Sie sie stets synchron.

- E-Mails basierend auf der Aktivierung von Anmeldungen - senden Sie E-Mails, um Nutzern zu helfen, die in Ihrem Anmeldefluss abfallen, und wandeln Sie sie in aktive Nutzer um.
- E-Mails auf der Grundlage eines beliebigen Benutzerverhaltens - Senden Sie E-Mails auf der Grundlage des Benutzerverhaltens, z. B. "In den Warenkorb".
- E-Mails an abgewanderte Kunden - Binden Sie abgewanderte Kunden per E-Mail mit einem Angebot wieder ein.

## Integration

### Konfigurieren Sie die Braze-Verbindung in GrowthLoop

Wenn Sie sich bei der Segmentierungsplattform in GrowthLoop anmelden, navigieren Sie zur Registerkarte **Ziele** in der linken Seitenleiste und klicken Sie auf **Neues Ziel** in der oberen rechten Ecke.

Scrollen Sie, bis Sie Braze gefunden haben, und klicken Sie auf **Braze hinzufügen**.

Es erscheint ein Popup-Fenster zur Konfiguration der Verbindung zum Ziel.

- **Name des Ziels**: So wird das Ziel in der App in Zukunft genannt und bezeichnet
- **Synchronisationsfrequenz**: Wählen Sie Täglich oder Stündlich; dies steuert, wie oft GrowthLoop Audiences nach Braze exportiert.
- **API-Schlüssel**: API-Schlüssel, der in den Anforderungen erstellt wurde, mit den erforderlichen Berechtigungen
- **API-URL**: URL wie in den Anforderungen definiert

Klicken Sie auf **Erstellen**, und Sie können Ihre erste Zielgruppe nach Braze exportieren! Um eine Audience in GrowthLoop zu erstellen, besuchen Sie [Audience erstellen](https://www.growthloop.com/help-center-articles/create-an-audience).

### Postexport

Sobald Ihre Zielgruppe exportiert wurde, erstellt GrowthLoop alle 15 Minuten eine aktualisierte Version Ihrer Kundenlisten und sendet sie an Braze.

Gleichzeitig entfernt GrowthLoop Nutzer aus Ihrer Zielgruppe, die nicht mehr qualifiziert sind, und fügt Ihrer Zielgruppe neu qualifizierte Nutzer hinzu. 

Braze gleicht Benutzer ab und erstellt eine Flagge, die anzeigt, dass sie Teil eines GrowthLoop-Publikums sind.

Wenn Sie in Braze eine Kampagne erstellen, können Sie Kunden in dieser GrowthLoop-Zielgruppe auswählen. 

## Fehlersuche

Kontaktieren Sie das GrowthLoop-Team unter solutions@growthloop.com, wenn Sie weitere Informationen oder Unterstützung benötigen.

[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints

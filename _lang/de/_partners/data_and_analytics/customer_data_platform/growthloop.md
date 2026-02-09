---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und GrowthLoop, einer Plattform, die es Ihnen erlaubt, Kundendaten direkt aus Data Warehouses zu segmentieren und an Braze zu senden."
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) unterstützt Marketing Teams bei der Aktivierung von Kundendaten aus dem Data Warehouse in der Cloud für Braze und andere Kanäle. Automatisieren, skalieren und messen Sie Marketing-Programme aus Ihrem Data Warehouse in der Cloud und halten Sie die Daten an einem einzigen, zentralen Standort.

_Diese Integration wird von GrowthLoop gepflegt._

## Über die Integration

Die Integration von Braze und GrowthLoop ermöglicht es Ihnen, Kundendaten direkt aus dem Data Warehouse zu segmentieren und an Braze zu senden. Dadurch wird sichergestellt, dass die Nutzer den tiefen Datensatz von Braze in Verbindung mit ihrer einzigen Wahrheitsquelle optimieren können. Rationalisieren Sie das Marketing für die Segmentierung und Aktivierung von Kunden und verkürzen Sie die Zeit, die für die Segmentierung, das Einführen, das Testen und die Messung der Ergebnisse von gezielten Kampagnen an Braze benötigt wird.

## Voraussetzungen 

| Anforderung | Beschreibung |
| ----------- | ----------- |
| GrowthLoop Wachstums- oder Unternehmenskonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein GrowthLoop-Konto. |
| Braze Rest API-Schlüssel | Ein REST-API-Schlüssel von Braze mit allen Berechtigungen.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Anwendungsfälle

Senden Sie Kundendaten aus Ihrem Data Warehouse an Braze, passen Sie E-Mail- und Push-Benachrichtigungs-Kampagnen mit einem Klick an und halten Sie sie stets auf dem gleichen Stand.

- E-Mails basierend auf der Aktivierung von Registrierungen - senden Sie E-Mails, um Nutzern zu helfen, die in Ihrem Registrierungsfluss abfallen, und wandeln Sie sie in aktive Nutzer:innen um.
- E-Mails basierend auf beliebigem Nutzer:innen-Verhalten - Senden Sie E-Mails basierend auf dem Nutzer:innen-Verhalten, wie z.B. "In den Warenkorb".
- E-Mails an abgewanderte Kund:innen - Binden Sie abgewanderte Kund:innen per E-Mail mit einem Angebot wieder ein.

## Integration

### Konfigurieren Sie die Braze-Verbindung in GrowthLoop

Wenn Sie sich bei der Segmentierungsplattform in GrowthLoop anmelden, navigieren Sie zum Tab **Ziele** in der linken Seitenleiste und klicken Sie auf **Neues Ziel** in der oberen rechten Ecke.

Scrollen Sie, bis Sie Braze gefunden haben, und klicken Sie auf **Braze hinzufügen**.

Es wird ein Popup-Fenster angezeigt, in dem Sie die Verbindung zum Ziel konfigurieren können.

- **Name des Ziels**: So wird das Ziel in der App künftig genannt und referenziert
- **Synchronisationsfrequenz**: Wählen Sie Täglich oder Stündlich aus; dies steuert, wie oft GrowthLoop Zielgruppen nach Braze exportiert.
- **API-Schlüssel**: API-Schlüssel, der in den Anforderungen erstellt wurde und über die erforderlichen Berechtigungen verfügt
- **API URL**: URL wie in den Anforderungen definiert

Klicken Sie auf **Erstellen**, und Sie können Ihre erste Zielgruppe nach Braze exportieren! Um eine Zielgruppe in GrowthLoop zu erstellen, besuchen Sie [Zielgruppe erstellen](https://www.growthloop.com/help-center-articles/create-an-audience).

### Postexport

Sobald Ihre Zielgruppe exportiert wurde, erstellt GrowthLoop alle 15 Minuten eine aktualisierte Version Ihrer Kund:in und sendet diese an Braze.

Gleichzeitig entfernt GrowthLoop Nutzer:innen aus Ihrer Zielgruppe, die nicht mehr qualifiziert sind, und fügt neue qualifizierte Nutzer:innen zu Ihrer Zielgruppe hinzu. 

Braze gleicht Nutzer:innen ab und erstellt eine Flagge, die anzeigt, dass sie Teil einer GrowthLoop-Zielgruppe sind.

Wenn Sie eine Kampagne in Braze erstellen, können Sie Kunden in dieser GrowthLoop-Zielgruppe auswählen. 

## Fehlersuche

Wenden Sie sich an das GrowthLoop Team unter solutions@growthloop.com, wenn Sie weitere Informationen oder Unterstützung benötigen.



---
nav_title: Nexla
article_title: Nexla
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Nexla, einer einheitlichen Plattform für Datenoperationen, die es Nutzern:in von Braze-Currents erlaubt, Data-Lake-Daten zu extrahieren, zu transformieren und in einem angepassten Format an andere Standorte zu laden."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) ist ein führendes Unternehmen im Bereich einheitlicher Datenoperationen und ein Gartner Cool Vendor 2021. Die Nexla-Plattform macht es für jeden einfach, skalierbare Datenflüsse zu erstellen und bietet reibungslose, geregelte Datenoperationen, bessere Zusammenarbeit und Agilität für Geschäfts- und Datenteams. Teams, die mit Daten arbeiten, erhalten eine einheitliche Erfahrung ohne oder mit wenig Code, um Daten für jeden Anwendungsfall zu integrieren, zu transformieren, bereitzustellen und zu überwachen. 

Die Braze- und Nexla-Integration erlaubt es Kunden, die [Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) verwenden, Nexla zu nutzen, um Data-Lake-Daten zu extrahieren, zu transformieren und in einem angepassten Format an andere Standorte zu laden, so dass Daten in Ihrem gesamten Ökosystem leicht zugänglich sind.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Nexla Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Nexla-Konto](https://www.nexla.com/get-demo). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Nexla's Daten-als-Produkt, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), machen es einfach, mit Daten jedes Formats zu arbeiten, ohne sich um Metadaten zu kümmern. Wenn Sie Ihre Datenströme zu oder von Braze mit Nexla einrichten, ist dies mit den No-Code-Tools einfach und in wenigen Minuten möglich. Nachdem der Datenfluss auf ein Ziel eingestellt ist, überwacht Nexla Ihren Datenfluss und skaliert auf jede beliebige Menge an Daten.

## Integration

### Schritt 1: Erstellen Sie ein Nexla-Konto

Wenn Sie noch kein Nexla-Konto haben, gehen Sie auf die [Website](https://www.nexla.com) von Nexla, um eine kostenlose Demo und einen Test zu beantragen. Als nächstes melden Sie sich bei [www.dataops.nexla.io](https://www.dataops.nexla.io) und melden Sie sich mit Ihren neuen Zugangsdaten an.

### Schritt 2: Fügen Sie Ihre Quelle hinzu

#### Wenn Braze Ihre Datenquelle ist
1. Navigieren Sie in der Nexla-Plattform in der linken Symbolleiste zu **Flows > Create a New Flow**.
2. Klicken Sie auf **Neue Quelle erstellen**, wählen Sie den Braze Konnektor aus und klicken Sie auf **Weiter**. 
3. Wählen Sie **Neue Zugangsdaten hinzufügen**, benennen Sie die Zugangsdaten, fügen Sie Ihren Braze API-Schlüssel und den REST-Endpunkt hinzu und **speichern Sie**.
4. Wählen Sie abschließend Ihre Daten aus und klicken Sie auf **Speichern**. 

Nexla durchsucht nun die Quelle nach allen Daten, die es findet, und generiert ein [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) zur Transformation oder zum Senden an das Ziel.

#### Wenn Braze Ihr Ziel ist

Besuchen Sie die Dokumentation von Nexla zur [Anbindung von Quellen an Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Schritt 3: Transformieren (optional)

Wenn Sie angepasste [Transformationen](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) an Ihren Daten vornehmen oder die vorgefertigten Konnektoren von Nexla verwenden möchten, klicken Sie auf den Button **Transformieren** auf dem Datensatz, um den Transformations-Builder aufzurufen. Eine Anleitung zur Verwendung des Transform Builders finden Sie in der [Dokumentation von Nexla.](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)

### Schritt 4: Senden an Ziel

Um Daten an ein Ziel zu senden, klicken Sie auf den Pfeil **An Ziel senden** im Datensatz und wählen einen der Konnektoren für das Ziel von Nexla oder Braze, wenn Sie eine andere Quelle hatten. Geben Sie Ihre Zugangsdaten ein, konfigurieren Sie die Zieloptionen, und klicken Sie auf **Speichern**. Die Daten werden sofort in dem von Ihnen angegebenen Format an das Ziel Ihrer Wahl weitergeleitet.

## Verwendung dieser Integration

Sobald der Fluss eingerichtet ist, ist nichts weiter erforderlich. Nexla verarbeitet alle Änderungen an den Quelldaten, skaliert auf neue Daten und benachrichtigt Sie bei Schemaänderungen oder Fehlern zur Triage. Wenn Sie Änderungen an den Transformationen, der Quelle oder dem Ziel vornehmen möchten, können Sie in diese Optionen klicken und die Änderung vornehmen. Nexla aktualisiert den Fluss dann sofort.


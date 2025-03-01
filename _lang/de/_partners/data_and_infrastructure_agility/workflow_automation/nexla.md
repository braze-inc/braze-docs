---
nav_title: Nexla
article_title: Nexla
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Nexla, einer einheitlichen Plattform für Datenoperationen, die es den Benutzern von Braze Currents ermöglicht, Data-Lake-Daten zu extrahieren, umzuwandeln und in einem benutzerdefinierten Format an andere Orte zu laden."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com) ist ein führendes Unternehmen im Bereich Unified Data Operations und 2021 ein Gartner Cool Vendor. Die Nexla-Plattform macht es für jeden einfach, skalierbare Datenflüsse zu erstellen und bietet reibungslose, geregelte Datenoperationen, bessere Zusammenarbeit und Flexibilität für Geschäfts- und Datenteams. Teams, die mit Daten arbeiten, erhalten eine einheitliche Erfahrung ohne oder mit wenig Code, um Daten für jeden Anwendungsfall zu integrieren, umzuwandeln, bereitzustellen und zu überwachen. 

Die Braze- und Nexla-Integration ermöglicht es Kunden, die [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/) verwenden, Nexla zu nutzen, um Data-Lake-Daten zu extrahieren, umzuwandeln und in einem benutzerdefinierten Format an andere Standorte zu laden, so dass Daten in Ihrem gesamten Ökosystem leicht zugänglich sind.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Nexla-Konto | Ein [Nexla-Konto][2] ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Nexla's Daten-als-Produkt, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), machen es einfach, mit Daten jedes Formats zu arbeiten, ohne sich um Metadaten zu kümmern. Wenn Sie Ihre Datenflüsse zu oder von Braze mit Nexla einrichten, ist dies dank der No-Code-Tools einfach und in wenigen Minuten möglich. Nachdem der Datenfluss auf ein Ziel eingestellt ist, überwacht Nexla Ihren Fluss und skaliert auf jede Datenmenge.

## Integration

### Schritt 1: Ein Nexla-Konto erstellen

Wenn Sie noch kein Nexla-Konto haben, gehen Sie auf die [Nexla-Website](https://www.nexla.com) und fordern Sie eine kostenlose Demo- und Testversion an. Als nächstes melden Sie sich bei [www.dataops.nexla.io](https://www.dataops.nexla.io) und melden Sie sich mit Ihren neuen Anmeldedaten an.

### Schritt 2: Fügen Sie Ihre Quelle hinzu

#### Wenn Braze Ihre Datenquelle ist
1. Navigieren Sie in der Nexla-Plattform in der linken Symbolleiste zu **Flows > Create a New Flow**.
2. Klicken Sie auf **Neue Quelle erstellen**, wählen Sie den Braze-Anschluss und klicken Sie auf **Weiter**. 
3. Wählen Sie **Neue Berechtigung hinzufügen**, geben Sie der Berechtigung einen Namen, fügen Sie Ihren Braze API-Schlüssel und den REST-Endpunkt hinzu und **speichern Sie**.
4. Wählen Sie abschließend Ihre Daten aus und klicken Sie auf **Speichern**. 

Nexla durchsucht nun die Quelle nach allen Daten, die es findet, und generiert ein [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) zur Umwandlung oder zum Senden an das Ziel.

#### Wenn Braze Ihr Ziel ist

Besuchen Sie die Nexla-Dokumentation zur [Verbindung von Quellen mit Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Schritt 3: Transformieren (optional)

Wenn Sie benutzerdefinierte [Transformationen](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) an Ihren Daten vornehmen oder die vorgefertigten Konnektoren von Nexla verwenden möchten, klicken Sie auf die Schaltfläche **Transformieren** im Datensatz, um den Transform Builder zu öffnen. Eine Anleitung zur Verwendung des Transform Builder finden Sie in der [Dokumentation von Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Schritt 4: An das Ziel senden

Um Daten an ein Ziel zu senden, klicken Sie im Datensatz auf den Pfeil **An Ziel senden** und wählen Sie einen der Zielkonnektoren von Nexla oder Braze, wenn Sie eine andere Quelle hatten. Geben Sie Ihre Anmeldedaten ein, konfigurieren Sie die Zieloptionen und klicken Sie auf **Speichern**. Die Daten fließen sofort in dem von Ihnen angegebenen Format an das Ziel Ihrer Wahl.

## Mit dieser Integration

Sobald der Fluss eingerichtet ist, ist nichts weiter erforderlich. Nexla verarbeitet alle Änderungen in den Quelldaten, skaliert auf alle neuen Daten und benachrichtigt Sie über alle Schemaänderungen oder Fehler, um diese zu klären. Wenn Sie Änderungen an den Transformationen, der Quelle oder dem Ziel vornehmen möchten, können Sie auf diese Optionen klicken und die Änderung vornehmen. Nexla aktualisiert den Fluss dann sofort.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo
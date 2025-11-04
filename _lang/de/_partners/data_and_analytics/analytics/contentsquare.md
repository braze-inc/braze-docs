---
nav_title: Contentsquare
article_title: Contentsquare
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Contentsquare, einer Analytics-Plattform für digitale Erlebnisse, die es Ihnen erlaubt, die Relevanz und die Konversionsrate Ihrer Kampagnen zu verbessern, indem Sie Nachrichten auf der Grundlage der digitalen Erlebnisse Ihrer Kund:innen ausrichten."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) ist eine Analytics-Plattform für digitale Erlebnisse, die ein noch nie dagewesenes Verständnis für das Kundenerlebnis ermöglicht.

_Diese Integration wird von Contentsquare gepflegt._

## Über die Integration

Die Integration von Braze und Contentsquare ermöglicht es Ihnen, Live-Signale (Betrug, Frustrationssignale usw.) als angepasste Events in Braze zu senden. Nutzen Sie die Insights von Contentsquare, um die Relevanz Ihrer Kampagnen und die Konversionsraten zu verbessern, indem Sie Nachrichten auf der Grundlage der digitalen Erlebnisse und der Körpersprache Ihrer Kund:in gezielt einsetzen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Contentsquare Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Contentsquare-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Um einen neuen Schlüssel im Braze-Dashboard zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel**. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({% image_buster /assets/img/contentsquare_custom_events.png %}). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Einige häufige Anwendungsfälle für Braze und Contentsquare sind:
- Personalisieren Sie Nachrichten auf der Grundlage von Kundenerlebnissen, indem Sie Daten über Kundenerlebnisse in Braze veröffentlichen.
- Retarget Kunden auf der Grundlage ihres digitalen Verhaltens, ihres Zögerns, ihrer Frustration und ihrer Absicht.
- Identifizieren Sie schlechte Erfahrungen innerhalb von Contentsquare und gewinnen Sie Kunden mit gezielten Nachrichten und Angeboten zur Bindung zurück.
- Gewinnen Sie gefährdete Kund:innen zurück, indem Sie relevante und einfühlsame Nachrichten zur richtigen Zeit und am richtigen Ort versenden.

## Integration

Um Contentsquare in Braze zu integrieren, müssen Sie die Installation einer "Live Signals"-Integration aus dem Contentsquare-Integrationskatalog anfragen:

1. Klicken Sie in Contentsquare im Menü **Einstellungen** auf **Konsole**. Dadurch werden Sie zu dem Projekt weitergeleitet, an dem Sie gerade arbeiten. 
2. Gehen Sie auf der Seite **Projekte** auf den Tab **Integrationen** und klicken Sie auf den Button **\+ Integration hinzufügen**.
3. Suchen Sie im Katalog der Integrationen die Integration **Live Signals** und klicken Sie auf **Hinzufügen**. Das Contentsquare Team wird sich dann mit Ihnen in Verbindung setzen, um das Code Snippet so zu konfigurieren, dass es Live-Signale an Braze sendet.
4. Contentsquare wird nun Ihre Integration bearbeiten. Der Text des Indikators wird aktualisiert, nachdem die Integration abgeschlossen ist.

Weitere Informationen finden Sie unter [Anfrage für die Integration von Contentsquare](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Verwendung dieser Integration

Sobald die Integration abgeschlossen ist, stehen Ihnen angepasste Events von Contentsquare zur Verwendung in Ihren Kampagnen und Canvase zur Verfügung. Sie können unter **Dateneinstellungen** > **Angepasste Events** überprüfen, welche Events an Braze gesendet werden.

![Contentsquare Live Signals Daten in Braze Angepasste Events Tab]({% image_buster /assets/img/contentsquare_custom_events.png %})



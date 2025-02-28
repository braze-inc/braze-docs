---
nav_title: Contentsquare
article_title: Contentsquare
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Contentsquare, einer Plattform für die Analyse digitaler Erlebnisse, die es Ihnen ermöglicht, die Relevanz und die Konversionsraten Ihrer Kampagnen zu verbessern, indem Sie Botschaften auf der Grundlage der digitalen Erfahrungen Ihrer Kunden ausrichten."
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) ist eine Plattform zur Analyse digitaler Erlebnisse, die ein noch nie dagewesenes Verständnis des Kundenerlebnisses ermöglicht.

Die Integration von Braze und Contentsquare ermöglicht es Ihnen, Live-Signale (Betrug, Frustrationssignale usw.) als benutzerdefinierte Ereignisse in Braze zu senden. Nutzen Sie die Erkenntnisse von Contentsquare, um die Relevanz Ihrer Kampagnen und die Konversionsraten zu verbessern, indem Sie die Botschaften auf der Grundlage der digitalen Erfahrungen und der Körpersprache Ihrer Kunden ausrichten.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Contentsquare Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Contentsquare-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Um einen neuen Schlüssel im Braze Dashboard zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel**. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Einige häufige Anwendungsfälle von Braze und Contentsquare sind:
- Personalisieren Sie Nachrichten auf der Grundlage von Kundenwünschen, indem Sie Daten über Kundenerfahrungen in Braze nutzen.
- Sprechen Sie Kunden auf der Grundlage ihres digitalen Verhaltens, ihres Zögerns, ihrer Frustration und ihrer Absichten erneut an.
- Identifizieren Sie schlechte Erfahrungen innerhalb von Contentsquare und gewinnen Sie Kunden mit gezielten Nachrichten und Angeboten zur Kundenbindung zurück.
- Gewinnen Sie gefährdete Kunden zurück, indem Sie relevante und einfühlsame Nachrichten zur richtigen Zeit und am richtigen Ort versenden.

## Integration

Um Contentsquare in Braze zu integrieren, müssen Sie die Installation einer "Live Signals" Integration aus dem Contentsquare Integrationskatalog anfordern:

1. Klicken Sie in Contentsquare im Menü **Einstellungen** auf **Konsole**. Dadurch werden Sie zu dem Projekt weitergeleitet, an dem Sie gerade arbeiten. 
2. Gehen Sie auf der Seite **Projekte** auf die Registerkarte **Integrationen** und klicken Sie auf die Schaltfläche **\+ Integration hinzufügen**.
3. Suchen Sie im Katalog der Integrationen die **Live Signals-Integration** und klicken Sie auf **Hinzufügen**. Das Contentsquare-Team wird sich dann mit Ihnen in Verbindung setzen, um das Code-Snippet so zu konfigurieren, dass es Live-Signale an Braze sendet.
4. Contentsquare wird nun Ihre Integration bearbeiten. Der Text des Indikators wird aktualisiert, nachdem die Integration abgeschlossen ist.

Weitere Informationen finden Sie unter [Beantragung einer Contentsquare-Integration](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186).

## Mit dieser Integration

Sobald die Integration abgeschlossen ist, können Sie die benutzerdefinierten Ereignisse von Contentsquare in Ihren Kampagnen und Canvases verwenden. Sie können unter **Dateneinstellungen** > **Benutzerdefinierte Ereignisse** überprüfen, welche Ereignisse an Braze gesendet werden.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie diese Seite unter **Einstellungen verwalten** > **Benutzerdefinierte Ereignisse**.
{% endalert %}

![Inhaltquare Live Signals Daten in der Registerkarte Braze Custom Events][1]

[1]: {% image_buster /assets/img/contentsquare_custom_events.png %} 

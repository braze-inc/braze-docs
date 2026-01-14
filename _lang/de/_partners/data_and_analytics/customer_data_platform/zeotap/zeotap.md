---
nav_title: Zeotap
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Zeotap, einer Kundendaten-Plattform der nächsten Generation, die Identitätsauflösung, Insights und Anreicherung bietet."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) ist eine Customer Data Platform (CDP) der nächsten Generation, die Ihnen hilft, Ihre mobile Zielgruppe zu entdecken und zu verstehen, indem sie Identitätsauflösung, Insights und Datenanreicherung bietet.

Mit der Integration von Zeotap und Braze können Sie den Umfang und die Reichweite Ihrer Kampagnen erweitern, indem Sie die Segmente von Zeotap synchronisieren, um Nutzerdaten auf Nutzer:innen-Kontos abzubilden. Sie können dann auf diese Daten reagieren und Ihren Nutzer:innen personalisierte Targeting-Erlebnisse zustellen.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
|Zeotap-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein [Zeotap-Konto](https://zeotap.com/). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz] ab ({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie ein Zeotap-Ziel

1. Navigieren Sie auf der Zeotap Unity Plattform zur Anwendung **ZIELE**.
2. Wählen Sie unter **Alle Kanäle** **Braze** aus.
3. Geben Sie in der daraufhin angezeigten Eingabeaufforderung den Namen Ihres Ziels sowie Ihren Client-Namen und den REST-API-Schlüssel von Braze an, der mit Ihrem Braze-Konto verknüpft ist.
4. Wählen Sie abschließend Ihre Braze REST Endpunkt Instanz aus der Dropdown-Liste aus und speichern Sie das Ziel. <br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Schritt 2: Erstellen und verknüpfen Sie ein Segment von Zeotap mit Ihrem Ziel 
 
1. Navigieren Sie auf der Zeotap Unity Plattform zur Anwendung **CONNECT**.
2. Erstellen Sie ein Segment und wählen Sie das in Schritt 1 erstellte Braze-Ziel aus.
3. Wählen Sie einen unterstützten Bezeichner für die Ausgabe aus: MAIDs, mit SHA256 gehashte E-Mail-Adressen oder andere von Braze erkannte 1P-Kunden:in (wenn Sie einen angepassten Bezeichner für Ihr Braze-Konto verwenden möchten, setzen Sie sich mit Zeotap in Verbindung, damit dieser für Ihr Konto aktiviert werden kann). Für die Integration von Braze kann nur ein Bezeichner für die Ausgabe verwendet werden. Diese Bezeichner müssen mit der externen ID übereinstimmen, die bei der Erfassung von Braze SDK-Daten verwendet wird.
4. Speichern Sie das Segment.

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Die Bezeichner, die angezeigt werden, sind sowohl in dem Segment verfügbar als auch von Braze unterstützt.
{% endalert %}

### Schritt 3: Segmente der Braze erstellen

Nachdem Sie ein Segment in Zeotap erfolgreich erstellt, gepusht und verarbeitet haben, erscheinen die Nutzer:innen von Zeotap im Braze-Dashboard. Sie können Nutzer:innen im Braze-Dashboard nach ihrer ID suchen. 

![Ein Braze Nutzerprofil, in dem unter "Angepasste Attribute" die Segmente eins bis vier als "wahr" aufgeführt sind.]({% image_buster /assets/img/zeotap/zeotap4.png %})

Wenn ein Nutzer zum Segment Zeotap gehört, erscheint der Segmentname als angepasstes Attribut in seinem Nutzerprofil mit dem booleschen Wert `true`. Notieren Sie sich den Namen des angepassten Attributs, da Sie ihn bei der Erstellung eines Segmentes von Braze benötigen. 

Als nächstes müssen Sie dieses Segment in Braze erstellen und definieren:
1. Wählen Sie im Braze-Dashboard **Segmente** und dann **Segmente erstellen**.
2. Als nächstes benennen Sie Ihr Segment und wählen das in Zeotap erstellte Segment mit den angepassten Attributen aus.
3. Speichern Sie Ihre Änderungen. 

![Im Braze Segment Builder finden Sie die importierten Segmente, die als angepasste Attribute eingestellt sind.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Sie können dieses neu erstellte Segment nun zu zukünftigen Kampagnen und Canvase von Braze hinzufügen, um diese Nutzer:innen zu targetieren. 


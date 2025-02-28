---
nav_title: Zeotap
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Zeotap, einer Kundendatenplattform der nächsten Generation, die Identitätsauflösung, Einblicke und Anreicherung bietet."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) ist eine Kundendatenplattform der nächsten Generation, die Ihnen hilft, Ihr mobiles Publikum zu entdecken und zu verstehen, indem sie Identitätsauflösung, Einblicke und Datenanreicherung bietet.

Mit der Integration von Zeotap und Braze können Sie den Umfang und die Reichweite Ihrer Kampagnen erweitern, indem Sie Zeotap-Kundensegmente synchronisieren, um Benutzerdaten mit Braze-Benutzerkonten zu verknüpfen. Sie können dann auf diese Daten reagieren und Ihren Nutzern personalisierte, zielgerichtete Erlebnisse bieten.

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
|Zeotap-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Zeotap-Konto](https://zeotap.com/). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze URL für Ihre Instanz][1] ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie ein Zeotap-Ziel

1. Navigieren Sie auf der Zeotap Unity-Plattform zur Anwendung **DESTINATIONS**.
2. Wählen Sie unter **Alle Kanäle** die Option **Hartlöten**.
3. Geben Sie in der daraufhin angezeigten Eingabeaufforderung den Namen Ihres Ziels, Ihren Client-Namen und den mit Ihrem Braze-Konto verbundenen Braze REST API-Schlüssel an.
4. Wählen Sie schließlich Ihre Braze REST-Endpunktinstanz aus der Dropdown-Liste aus und speichern Sie das Ziel. <br><br>![][1]

### Schritt 2: Erstellen und verknüpfen Sie ein Zeotap-Segment mit Ihrem Ziel 
 
1. Navigieren Sie auf der Zeotap Unity-Plattform zur Anwendung **CONNECT**.
2. Erstellen Sie ein Segment und wählen Sie das in Schritt 1 erstellte Braze-Ziel.
3. Wählen Sie einen unterstützten Ausgabebezeichner: MAIDs, eine mit SHA256 gehashte E-Mail-Adresse oder eine beliebige von Braze erkannte 1P-Kundenkennung (wenn Sie eine benutzerdefinierte Kennung für Ihr Braze-Konto verwenden möchten, setzen Sie sich mit Zeotap in Verbindung, damit diese für Ihr Konto aktiviert werden kann). Für die Braze-Integration kann nur ein Ausgabebezeichner verwendet werden. Diese Identifikatoren müssen mit der externen ID übereinstimmen, die beim Sammeln von Braze SDK-Daten festgelegt wurde.
4. Speichern Sie das Segment.

![][2]

{% alert note %}
Die angezeigten Bezeichner sind sowohl in dem Segment verfügbar als auch von Braze unterstützt.
{% endalert %}

### Schritt 3: Lötabschnitt erstellen

Nach erfolgreicher Erstellung, Übertragung und Verarbeitung eines Segments in Zeotap werden die Zeotap-Benutzer im Braze-Dashboard angezeigt. Sie können im Braze-Dashboard Benutzer nach ihrer Benutzer-ID suchen. 

![Ein Braze-Benutzerprofil, in dem die Segmente eins bis vier unter "Benutzerdefinierte Attribute" als "wahr" aufgeführt sind.][4]

Wenn ein Benutzer Teil des Zeotap-Segments ist, erscheint der Segmentname als benutzerdefiniertes Attribut in seinem Benutzerprofil mit dem booleschen Wert `true`. Notieren Sie sich den Namen des benutzerdefinierten Attributs, da Sie ihn bei der Erstellung eines Braze-Segments benötigen. 

Als nächstes müssen Sie dieses Segment in Braze erstellen und definieren:
1. Wählen Sie auf dem Braze-Dashboard **Segmente** und dann **Segment erstellen**.
2. Als nächstes benennen Sie Ihr Segment und wählen das in Zeotap erstellte benutzerdefinierte Attributsegment aus.
3. Speichern Sie Ihre Änderungen. 

![Im Braze Segment Builder finden Sie die importierten Segmente, die als benutzerdefinierte Attribute festgelegt wurden.][3]

Sie können dieses neu erstellte Segment nun zu zukünftigen Braze-Kampagnen und Canvases hinzufügen, um diese Endbenutzer anzusprechen. 

[1]: {% image_buster /assets/img/zeotap/zeotap1.png %}
[2]: {% image_buster /assets/img/zeotap/zeotap2.png %}
[3]: {% image_buster /assets/img/zeotap/zeotap3.png %}
[4]: {% image_buster /assets/img/zeotap/zeotap4.png %}

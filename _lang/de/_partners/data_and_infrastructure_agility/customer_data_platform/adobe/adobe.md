---
nav_title: Adobe
article_title: Adobe
description: "Diese Seite beschreibt die Partnerschaft zwischen Braze und Adobe, einer Plattform für Kundendaten, die es Marken ermöglicht, ihre Adobe-Daten (benutzerdefinierte Attribute und Segmente) mit Braze in Echtzeit zu verbinden und abzubilden. Marken können dann auf diese Daten reagieren und diesen Nutzern personalisierte, gezielte Erlebnisse bieten."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Die Echtzeit-Kundendatenplattform von Adobe basiert auf der Adobe Experience Platform und führt bekannte und anonyme Daten aus verschiedenen Unternehmensquellen zusammen, um Kundenprofile zu erstellen. Diese Profile können dann verwendet werden, um personalisierte Erlebnisse über alle Kanäle und Geräte in Echtzeit zu bieten.

Die Integration von Braze und Adobe CDP verbindet die Adobe-Daten Ihrer Marke (benutzerdefinierte Attribute und Segmente) mit Braze und bildet sie in Echtzeit ab. Sie können dann auf diese Daten reagieren und Ihren Nutzern personalisierte, gezielte Erlebnisse bieten. Bei Adobe ist die Integration intuitiv. Nehmen Sie einfach eine beliebige [Adobe-Identität](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), ordnen Sie sie einer externen ID von Braze zu und senden Sie sie an die Braze-Plattform. Alle gesendeten Daten werden in Braze über ein neues Attribut `AdobeExperiencePlatformSegments` zugänglich sein.

{% alert important %}
Die Adobe Experience Platform-Integration unterstützt derzeit keine dynamische Publikumsmitgliedschaft. Das bedeutet, dass es nur Werte zu Benutzerprofilen hinzufügen, aber nicht entfernen kann.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Adobe-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Adobe-Konto](https://account.adobe.com/). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Hartlöt-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Das Senden zusätzlicher benutzerdefinierter Attribute erhöht die Nutzung der Datenpunkte. Wir empfehlen Ihnen, mit Ihrem Kundenerfolgsmanager zu sprechen, um diesen potenziellen Anstieg der Datenpunkte besser zu verstehen.
{% endalert %}

## Integration

### Schritt 1: Konfigurieren Sie das Ziel Braze

Wählen Sie auf der Seite **Adobe-Einstellungen** unter **Sammlungen** die Option **Ziele**. Suchen Sie dort die Kachel **Braze** und wählen Sie **Konfigurieren**. 

![][1]

{% alert note %}
Wenn bereits eine Verbindung mit Braze besteht, sehen Sie eine Schaltfläche **Aktivieren** auf der Zielkarte. Weitere Informationen über den Unterschied zwischen Aktivieren und Konfigurieren finden Sie im Abschnitt Katalog in der [Dokumentation zum](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) Adobe Zielarbeitsbereich.
{% endalert %}

### Schritt 2: Lötmarke bereitstellen

Im Schritt **Konto** geben Sie Ihren Braze API-Schlüssel ein und wählen **Mit Ziel verbinden**.

![][3]{: style="max-width:60%"}

### Schritt 3: Authentifizierung

Als nächstes geben Sie im Schritt **Authentifizierung** Ihre Braze-Verbindungsdaten ein:
- **Name**: Geben Sie den Namen ein, unter dem Sie dieses Ziel in Zukunft wiedererkennen möchten.
- **Zielort**: Geben Sie eine Beschreibung ein, mit der Sie dieses Ziel identifizieren können.
- **Endpunkt-Instanz**: Geben Sie Ihre Braze-Endpunkt-Instanz ein.
- **Marketing-Anwendungsfall**: Marketing-Anwendungsfälle geben die Absicht an, für die Daten an das Ziel exportiert werden sollen. Sie können aus den von Adobe definierten Marketing-Anwendungsfällen auswählen oder Ihren eigenen Anwendungsfall erstellen. Wenn Sie mehr über die Anwendungsfälle von Adobe Marketing erfahren möchten, besuchen Sie die Seite [Data Governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![][4]{: style="max-width:60%;"}

### Schritt 4: Ziel erstellen
Wählen Sie **Ziel erstellen**. Ihr Ziel wurde erstellt. Sie können **Speichern & Beenden** wählen, um die Segmente später zu aktivieren, oder **Weiter**, um den Workflow fortzusetzen und die zu aktivierenden Segmente auszuwählen. 

### Schritt 5: Aktivieren Sie Segmente
Aktivieren Sie die Daten, die Sie in der Adobe Echtzeit-CDP haben, indem Sie Segmente dem Braze-Ziel zuordnen.

In der folgenden Liste finden Sie die allgemeinen Schritte, die zur Aktivierung eines Segments erforderlich sind. Eine ausführliche Anleitung zu den Adobe-Segmenten und dem Workflow für die Segmentaktivierung finden Sie bei [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Wählen und aktivieren Sie das Ziel Braze.
2. Wählen Sie die entsprechenden Segmente aus.
4. Konfigurieren Sie die Zeitplanung und die Dateinamen für jedes Segment, das Sie exportieren.
5. Wählen Sie die Attribute aus, die Sie an Braze senden möchten.
6. Prüfen und verifizieren Sie die Aktivierung.

### Schritt 6: Feldkartierung

Um Ihre Audience-Daten korrekt von der Adobe Experience Platform an Braze zu senden, müssen Sie den Schritt der Feldzuordnung durchführen. Das Mapping stellt eine Verbindung zwischen den Feldern des Adobe Experience-Datenmodells und den entsprechenden Feldern der Braze-Plattform her.

1. Wählen Sie im Schritt Mapping die Option **Neues Mapping hinzufügen**.<br>![][5]{: style="max-width:50%;"}<br><br>
2. Wählen Sie im Bereich Quellfeld die Pfeilschaltfläche neben dem leeren Feld, um das Fenster Quellfeld auswählen zu öffnen.<br>![][6]<br><br>
3. Wählen Sie in dem Fenster die Adobe-Attribute aus, die Sie Ihren Braze-Attributen zuordnen möchten. <br>![][7]{: style="max-width:70%;"}<br><br>Als nächstes wählen Sie den Identitäts-Namensraum. Diese Option wird verwendet, um einen Plattform-Identitäts-Namensraum einem Braze-Namensraum zuzuordnen.<br>![][8]{: style="max-width:80%;"}<br> Wählen Sie Ihre Quellfelder aus und wählen Sie dann **Auswählen**.<br><br>
4. Wählen Sie im Bereich Zielfeld das Mapping-Symbol neben dem Feld.<br>![][9]{: style="max-width:90%;"} <br><br>
5. Im Fenster Zielfeld auswählen können Sie zwischen drei Kategorien von Zielfeldern wählen:<br><br>- **Wählen Sie den Identitäts-Namensraum**: Verwenden Sie diese Option, um Platform Identity Namespaces auf Braze Identity Namespaces abzubilden.<br>- **Wählen Sie benutzerdefinierte Attribute**: Mit dieser Option können Sie Adobe XDM-Attribute benutzerdefinierten Braze-Attributen zuordnen, die Sie in Ihrem Braze-Konto definiert haben. <br><br>![][10]{: style="max-width:60%;"}<br><br>**Sie können diese Option auch verwenden, um bestehende XDM-Attribute in Braze umzubenennen.** Wenn Sie z.B. ein `lastname` XDM-Attribut einem benutzerdefinierten `Last_Name` Attribut in Braze zuordnen, wird das `Last_Name` Attribut in Braze erstellt, falls es noch nicht existiert, und das `lastname` XDM-Attribut wird diesem zugeordnet. <br><br> Wählen Sie Ihre Zielfelder aus und wählen Sie dann **Auswählen**.<br><br>
6. Ihre Feldzuordnung sollte in der Liste erscheinen.<br>![][11]<br><br>
7. Um weitere Zuordnungen hinzuzufügen, wiederholen Sie die Schritte 1 bis 6, falls erforderlich. 

## Anwendungsfall

Angenommen, Ihr XDM-Profilschema und Ihre Braze-Instanz enthalten die folgenden Attribute und Identitäten:

|     | XDM-Profil-Schema | Braze-Instanz |
| --- | ------------------ | -------------- |
| Attribute | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identitäten | - `Email`<br>\- Google Ad ID (`GAID`)<br>\- Apple ID für Werbetreibende (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Die korrekte Zuordnung würde wie folgt aussehen:

![Ziel-Zuordnungen: IdentityMap:IDFA zugeordnet zu IdentityMap:external_id, IdentityMap:GAID zugeordnet zu IdentityMap:external_id, IdentityMap:Email zugeordnet zu IdentityMap:external_id, xdm:mobilePhone.number zugeordnet zu CustomAttribute:PhoneNumber, xdm:person.name.lastName zugeordnet zu CustomAtrribute:LastName, xdm:person.name.firstName zugeordnet zu CustomAttribute:FirstName][12]

## Exportierte Daten
Um zu überprüfen, ob die Daten erfolgreich nach Braze exportiert wurden, sehen Sie in Ihrem Braze-Konto nach. Adobe Experience Platform-Segmente werden unter dem Attribut `AdobeExperiencePlatformSegments` nach Braze exportiert.

## Datennutzung und Governance
Alle Ziele der Adobe Experience Platform halten sich beim Umgang mit Ihren Daten an die Datenverwendungsrichtlinien. Unter [Data Governance in der Echtzeit-CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) finden Sie ausführliche Informationen darüber, wie die Adobe Experience Platform Data Governance durchsetzt. 

[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %}
[3]: {% image_buster /assets/img/adobe/braze-destination-account.png %}
[4]: {% image_buster /assets/img/adobe/braze-destination-authentication.png %}
[5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %}
[6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source.png %}
[7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}
[8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}
[9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}
[10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}
[11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %}
[12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 
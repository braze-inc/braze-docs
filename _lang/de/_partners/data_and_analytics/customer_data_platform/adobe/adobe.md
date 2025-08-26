---
nav_title: Adobe
article_title: Adobe
description: "Diese Seite beschreibt die Partnerschaft zwischen Braze und Adobe, einer Customer Data Platform, die es Marken erlaubt, ihre Adobe Daten (angepasste Attribute und Segmente) mit Braze in Echtzeit zu verbinden und abzubilden. Marken können dann auf Basis dieser Daten handeln und diesen Nutzer:innen personalisierte, zielgerichtete Erlebnisse bieten."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Die Customer Data Platform (CDP) von Adobe basiert auf der Adobe Experience Platform und führt bekannte und anonyme Daten aus verschiedenen Unternehmensquellen zusammen, um Kundenprofile zu erstellen. Diese Profile können dann verwendet werden, um über alle Kanäle und Geräte hinweg personalisierte Erlebnisse in Realtime zu bieten.

Die Integration von Braze und Adobe CDP verbindet die Adobe-Daten Ihrer Marke (angepasste Attribute und Segmente) mit Braze und bildet sie in Echtzeit ab. Sie können dann auf diese Daten reagieren und Ihren Nutzer:innen personalisierte, zielgerichtete Erlebnisse zustellen. Bei Adobe ist die Integration intuitiv. Nehmen Sie einfach eine beliebige [Adobe-Identität](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), bilden Sie sie auf eine externe ID von Braze ab und senden Sie sie an die Braze-Plattform. Alle gesendeten Daten werden in Braze über ein neues Attribut `AdobeExperiencePlatformSegments` zugänglich sein.

{% alert important %}
Die Integration der Adobe Experience Platform unterstützt derzeit keine dynamische Mitgliedschaft in der Zielgruppe. Das bedeutet, dass es nur Werte zu Nutzerprofilen hinzufügen, nicht aber entfernen kann.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Adobe-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Adobe-Konto](https://account.adobe.com/). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Das Senden zusätzlicher angepasster Attribute erhöht Ihre Datenpunkt-Nutzung. Wir empfehlen Ihnen, mit Ihrem Customer-Success-Manager zu sprechen, um diesen potenziellen Anstieg der Datenpunkte besser zu verstehen.
{% endalert %}

## Integration

### Schritt 1: Braze-Ziel konfigurieren

Wählen Sie auf der Seite **Adobe-Einstellungen** unter **Sammlungen** die **Ziele** aus. Suchen Sie von dort aus die Kachel **Braze** und wählen Sie **Konfigurieren**. 

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Wenn bereits eine Verbindung mit Braze besteht, sehen Sie auf der Zielkarte einen Button **Aktivieren**. Weitere Informationen zum Unterschied zwischen Aktivieren und Konfigurieren finden Sie im Abschnitt Katalog in der [Dokumentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) zum Adobe Workspace für Ziele.
{% endalert %}

### Schritt 2: Braze-Token bereitstellen

Geben Sie im Schritt **Konto** Ihren Braze API-Schlüssel an und wählen Sie **Mit Ziel verbinden** aus.

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Schritt 3: Authentifizierung

Als nächstes geben Sie im Schritt **Authentifizierung** Ihre Braze-Verbindungsdaten ein:
- **Name**: Geben Sie den Namen ein, unter dem Sie dieses Ziel in Zukunft wiedererkennen möchten.
- **Das Ziel**: Geben Sie eine Beschreibung ein, mit deren Hilfe Sie dieses Ziel identifizieren können.
- **Endpunkt Instanz**: Geben Sie Ihre Braze Endpunkt Instanz ein.
- **Anwendungsfälle im Marketing**: Anwendungsfälle des Marketings geben die Absicht an, für die Daten an das Ziel exportiert werden sollen. Sie können aus den von Adobe definierten Anwendungsfällen für das Marketing auswählen oder Ihren eigenen Anwendungsfall für das Marketing erstellen. Wenn Sie mehr über Anwendungsfälle im Marketing von Adobe erfahren möchten, besuchen Sie [Data Governance in Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Schritt 4: Ziel erstellen
Wählen Sie **Ziel erstellen**. Ihr Ziel wurde erstellt. Sie können **Speichern & Beenden** wählen, um die Segmente später zu aktivieren, oder **Weiter**, um den Arbeitsablauf fortzusetzen und die zu aktivierenden Segmente auszuwählen. 

### Schritt 5: Segmente aktivieren
Aktivieren Sie die Daten, die Sie in der Adobe Realtime CDP haben, indem Sie Segmente auf das Ziel Braze abbilden.

In der folgenden Liste finden Sie die allgemeinen Schritte, die zur Aktivierung eines Segments erforderlich sind. Eine ausführliche Anleitung zu den Segmenten von Adobe und dem Workflow zur Segmentierung finden Sie unter [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Wählen Sie das Ziel Braze aus und aktivieren Sie es.
2. Wählen Sie die zutreffenden Segmente aus.
4. Konfigurieren Sie die Zeitpläne und Dateinamen für jedes Segment, das Sie exportieren.
5. Wählen Sie die Attribute aus, die Sie an Braze senden möchten.
6. Überprüfen Sie die Aktivierung und überprüfen Sie sie.

### Schritt 6: Abbildung der Felder

Um Ihre Daten zur Zielgruppe von der Adobe Experience Platform korrekt an Braze zu senden, müssen Sie den Schritt der Abbildung der Felder abschließen. Die Abbildung stellt eine Verbindung zwischen den Feldern des Adobe Experience-Datenmodells und den entsprechenden Feldern der Braze-Plattform her.

1. Wählen Sie im Schritt Abbildung hinzufügen die Option **Neue Abbildung hinzufügen**.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. Wählen Sie im Bereich Quellfeld den Pfeil-Button neben dem leeren Feld, um das Fenster Quellfeld auswählen zu öffnen.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. Wählen Sie in dem Fenster die Adobe Attribute aus, die Sie Ihren Braze Attributen zuordnen möchten. <br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>Wählen Sie dann den Identitäts-Namensraum aus. Mit dieser Option können Sie einen Namespace für die Plattformidentität auf einen Braze-Namespace abbilden.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Wählen Sie Ihre Quellfelder aus und wählen Sie dann **Auswählen**.<br><br>
4. Wählen Sie im Abschnitt Targeting-Feld das Symbol für die Abbildung neben dem Feld aus.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. Im Fenster Zielfeld auswählen können Sie zwischen drei Kategorien von Zielfeldern wählen:<br><br>- **Identitäts-Namensraum auswählen**: Verwenden Sie diese Option, um Identitäts-Namensräume von Platform auf Identitäts-Namensräume von Braze abzubilden.<br>- **Wählen Sie angepasste Attribute aus**: Verwenden Sie diese Option, um Adobe XDM-Attribute an angepasste Braze-Attribute anzupassen, die Sie in Ihrem Braze-Konto definiert haben. <br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**Sie können diese Option auch verwenden, um bestehende XDM-Attribute in Braze umzubenennen.** Wenn Sie beispielsweise ein `lastname` XDM-Attribut an ein angepasstes `Last_Name` Attribut in Braze anpassen, wird das `Last_Name` Attribut in Braze erstellt, falls es noch nicht vorhanden ist, und das `lastname` XDM-Attribut wird diesem zugeordnet. <br><br> Wählen Sie Ihre Targeting-Felder und wählen Sie dann **Auswählen**.<br><br>
6. Ihre Abbildung des Feldes sollte in der Liste erscheinen.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Wenn Sie weitere Abbildungen hinzufügen möchten, wiederholen Sie die Schritte 1 bis 6, falls erforderlich. 

## Anwendungsfall

Nehmen wir an, Ihr XDM-Profilschema und Ihre Braze-Instanz enthalten die folgenden Attribute und Identitäten:

|     | Schema des XDM-Profils | Braze-Instanz |
| --- | ------------------ | -------------- |
| Attribute | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identitäten | - `Email`<br>\- Google Ads ID (`GAID`)<br>\- Apple ID für Werbetreibende (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Die korrekte Abbildung würde wie folgt aussehen:

![Ziel-Abbildungen: IdentityMap:IDFA abgebildet auf IdentityMap:external_id, IdentityMap:GAID abgebildet auf IdentityMap:external_id, IdentityMap:E-Mail abgebildet auf IdentityMap:external_id, xdm:mobilePhone.number abgebildet auf CustomAttribute:PhoneNumber, xdm:person.name.lastName abgebildet auf CustomAtrribute:LastName, xdm:person.name.firstName abgebildet auf CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Exportierte Daten
Um zu überprüfen, ob die Daten erfolgreich nach Braze exportiert wurden, sehen Sie in Ihrem Braze-Konto nach. Adobe Experience Platform Segmente werden unter dem Attribut `AdobeExperiencePlatformSegments` nach Braze exportiert.

## Nutzung und Verwaltung von Daten
Alle Ziele von Adobe Experience Platform halten sich beim Umgang mit Ihren Daten an die Richtlinien zur Datennutzung. Unter [Data Governance in Realtime CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) finden Sie detaillierte Informationen darüber, wie die Adobe Experience Platform Data Governance durchsetzt. 


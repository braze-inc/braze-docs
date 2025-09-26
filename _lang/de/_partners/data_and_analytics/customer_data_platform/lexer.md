---
nav_title: Lexer
article_title: Lexer
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Lexer, einer Customer Data Platform, die Marketern Kundendaten an die Hand gibt, um verkaufsfördernde Erlebnisse zu schaffen."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer](https://lexer.io/), eine speziell entwickelte Customer Data Platform für den Einzelhandel, hilft Marken, ihren Umsatz durch verbesserte Kundenerlebnisse zu steigern, indem sie eine robuste Datenanreicherung mit den intuitivsten Tools und fachkundiger Beratung kombiniert.

_Diese Integration wird von Lexer gepflegt._

## Über die Integration

Die Integration von Braze und Lexer erlaubt es Ihnen, Daten zwischen den beiden Plattformen zu synchronisieren. Nutzen Sie Ihre Daten in Lexer, um wertvolle Segmente in Braze zu erstellen, oder importieren Sie Ihre bestehenden Segmente in Lexer, um Insights zu erhalten. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Partner-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lexer-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen `user` Berechtigungen (außer `user.delete`) und `segment.list` Berechtigungen. Der Berechtigungssatz kann sich ändern, wenn Lexer die Unterstützung für weitere Braze-Objekte hinzufügt. Sie sollten also entweder jetzt mehr Berechtigungen erteilen oder ein Update dieser Berechtigungen in der Zukunft planen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre [URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Amazon AWS S3 Bucket und Zugangsdaten | Bevor Sie mit der Integration beginnen, müssen Sie über Zugangsdaten für ein AWS S3-Bucket verfügen, das mit Ihrem Lexer-Hub verbunden ist (dies kann ein Bucket sein, das Sie erstellen, oder eines, das Lexer für Sie erstellt und verwaltet). Besuchen Sie [Lexer](https://learn.lexer.io/docs/amazon-s3) für eine Anleitung zu dieser Anforderung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Navigieren Sie in Lexer zu **Verwalten > Integration**, wählen Sie die Kachel **Braze** aus, und klicken Sie auf **Braze integrieren**. Geben Sie die folgenden Informationen an:
- **Braze REST Endpunkt**
- **Braze REST API-Schlüssel**
- **AWS Zugangsdaten**
  - **AWS S3 Bucket-Name**
  - **AWS S3 [Bucket-Region](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html)**
  - **AWS S3 Bucket Pfad**: Dieser Pfad sollte mit dem Pfad übereinstimmen, den Sie bei der [Verbindung Ihres S3-Buckets mit Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/) angegeben haben. Dieses Feld sollte leer sein, wenn Sie Braze keine Angaben gemacht haben.
  - **AWS S3 geheimer Zugangsschlüssel**: Besuchen Sie Amazon für Informationen zur [Erstellung eines Zugangsschlüssels](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/).
- **Braze Export Segmente ID**: Die ID des Segments, das Sie in Braze erstellt haben und das alle Nutzer:innen enthält, die Sie in Lexer exportieren möchten. Wenn es Nutzer:innen gibt, die Sie nicht in Lexer exportieren möchten, können Sie sie aus dem Segment ausschließen, das Sie in Braze erstellt haben. Um den Bezeichner Ihres Segments zu finden, klicken Sie in Braze auf das gewünschte Segment und suchen Sie den **Segment API-Bezeichner**.

![]({% image_buster /assets/img/lexer/braze_integrate_screen.png %})

### Auswahl einer AWS S3-Option (Lexer-verwaltet oder selbstverwaltet)
Die Verwendung eines von Lexer verwalteten Buckets ist die bevorzugte Methode, um Braze mit Ihrem Lexer-Hub zu verbinden und reduziert den Einrichtungsaufwand. Lexer liefert Ihnen die einmaligen Details, die Sie zur Konfiguration von Braze benötigen.

Wenn Sie bereits ein S3-Bucket mit Braze verbunden haben und es für andere Zwecke verwenden, müssen Sie stattdessen Lexer Zugriff auf dieses selbstverwaltete Bucket gewähren, indem Sie die vorangehenden Schritte ausführen.

Diese Integration funktioniert, indem Sie Lexer Ihr bestehendes API-Token und Ihre Geheimnisse zur Verfügung stellen, so dass Lexer diese Exporte in Ihrem Namen durchführen kann. Außerdem importiert es Ihre Braze-Daten mit diesen Zugangsdaten und Ihrer S3-Konfiguration in Lexer, um Ihre Daten auf beiden Plattformen automatisch zu synchronisieren.

## Segmente an Braze senden

### Schritt 1: Aktivierung erstellen

Lexer Activate aktualisiert automatisch Ihre Braze-Profile und fügt Attribute hinzu oder entfernt sie, wenn Kunden in Ihr Segment eintreten oder es verlassen.

1. In Lexer, in **Lexer Aktivierungen**, klicken Sie auf **NEUE ZIELGRUPPE AKTIVIEREN**.
2. Wählen Sie die entsprechende Braze-Aktivierung für diese Kampagne aus.
3. Fügen Sie Ihr Segment hinzu.
4. Aktualisieren Sie den Namen Ihrer Zielgruppe; dieser wird in Braze zu Ihrem Attributwert.
5. Dies ist das angepasste Attribut, das wir in Braze aktualisieren werden. Wenden Sie sich zum Update an den [Lexer-Support](support@lexer.io).
6. Markieren Sie die entsprechende Listenaktion - in den meisten Fällen werden Sie Ihre Liste pflegen wollen.
7. Überprüfen Sie die Bedingungen, und klicken Sie auf **AUDIENCE SENDEN**.

![]({% image_buster /assets/img/lexer/lexer.png %})

### Schritt 2: Aktivierung überprüfen

Sobald Ihre Aktivierung in Aktivieren als gesendet bestätigt wurde, werden Sie sehen, dass die Datensätze in Braze aktualisiert werden. Ihre Profile werden in Braze erst dann vollständig aktualisiert, wenn Sie eine Bestätigungs-E-Mail von Lexer erhalten haben.

### Schritt 3: Erstellen Sie Ihr Braze Segment

In Braze sehen Sie, dass der Name Ihrer Zielgruppe in Lexer jetzt ein Wert in Ihrem angepassten Attribut `lexer_audience` ist. Braze hat ein Limit von 100 Werten pro Attribut.

Um Ihr Segment zu erstellen, navigieren Sie zu **Segment > + Segment erstellen** und wählen Sie **Angepasstes Attribut** als Filter. Wählen Sie als nächstes `lexer_audience` als Attribut und den Namen der gewünschten Zielgruppe von Lexer aus. Wenn Sie fertig sind, **speichern Sie** Ihre Zielgruppe.

Sie können dieses neu erstellte Segment nun zu zukünftigen Kampagnen und Canvase von Braze hinzufügen, um diese Nutzer:innen zu targetieren.



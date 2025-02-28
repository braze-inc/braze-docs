---
nav_title: Lexer
article_title: Lexer
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Lexer, einer Plattform für Kundendaten, die Marketingfachleuten Kundendaten an die Hand gibt, um verkaufsfördernde Erlebnisse zu schaffen."
alias: /partners/lexer/
page_type: partner
search_tag: Partner
---

# Lexer

> [Lexer][6], eine Plattform für Kundendaten, die speziell für den Einzelhandel entwickelt wurde, hilft Marken, ihren Umsatz durch verbesserte Kundenerlebnisse zu steigern, indem sie robuste Datenanreicherung mit den intuitivsten Tools und fachkundiger Beratung kombiniert.

Die Integration von Braze und Lexer ermöglicht es Ihnen, Daten zwischen den beiden Plattformen zu synchronisieren. Verwenden Sie Ihre Lexer-Daten, um wertvolle Braze-Segmente zu erstellen, oder importieren Sie Ihre bestehenden Segmente in Lexer, um neue Erkenntnisse zu gewinnen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Partner-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Lexer-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen `user` Berechtigungen (außer `user.delete`) und `segment.list` Berechtigungen. Der Berechtigungssatz kann sich ändern, wenn Lexer die Unterstützung für weitere Braze-Objekte hinzufügt. Daher sollten Sie entweder jetzt mehr Berechtigungen erteilen oder planen, diese Berechtigungen in Zukunft zu aktualisieren.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre [REST-Endpunkt-URL]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Amazon AWS S3 Bucket und Anmeldeinformationen | Bevor Sie mit der Integration beginnen, müssen Sie über die Zugangsdaten für einen AWS S3-Bucket verfügen, der mit Ihrem Lexer-Hub verbunden ist (dies kann ein Bucket sein, das Sie erstellen oder das Lexer für Sie erstellt und verwaltet). Besuchen Sie [Lexer](https://learn.lexer.io/docs/amazon-s3) für eine Anleitung zu dieser Anforderung. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Navigieren Sie in Lexer zu **Verwalten > Integration**, wählen Sie die Kachel **Braze** und klicken Sie auf **Braze integrieren**. Geben Sie die folgenden Informationen an:
- **Braze REST Endpunkt**
- **Braze REST API Schlüssel**
- **AWS-Anmeldeinformationen**
  - **AWS S3 Bucket Name**
  - **AWS S3 [Bucket-Region][4]**
  - **AWS S3 Bucket-Pfad**: Dieser Pfad sollte mit dem Pfad übereinstimmen, den Sie bei der [Verbindung Ihres S3-Buckets mit Braze][5] angegeben haben. Dieses Feld sollte leer sein, wenn Sie Braze nichts mitgeteilt haben.
  - **AWS S3 geheimer Zugangsschlüssel**: Besuchen Sie Amazon für Informationen zur [Erstellung eines Zugangsschlüssels][3].
- **Braze Export Segment ID**: Die ID für das Segment, das Sie in Braze erstellt haben und das alle Benutzer enthält, die Sie in Lexer exportieren möchten. Wenn es Benutzer gibt, die Sie nicht in Lexer exportieren möchten, können Sie sie aus dem Segment ausschließen, das Sie in Braze erstellt haben. Um Ihren Segment-Identifikator zu finden, klicken Sie in Braze auf das gewünschte Segment und suchen Sie den **Segment-API-Identifikator**.

![][1]

### Auswahl einer AWS S3-Option (Lexer-verwaltet oder selbst-verwaltet)
Die Verwendung eines von Lexer verwalteten Buckets ist die bevorzugte Methode, um Braze mit Ihrem Lexer-Hub zu verbinden und reduziert den Einrichtungsaufwand. Lexer liefert Ihnen die einmaligen Details, die Sie zur Konfiguration von Braze benötigen.

Wenn Sie bereits einen S3-Bucket mit Braze verbunden haben und diesen für andere Zwecke verwenden, müssen Sie Lexer stattdessen Zugriff auf diesen selbstverwalteten Bucket gewähren, indem Sie die vorangehenden Schritte ausführen.

Diese Integration funktioniert, indem Sie Lexer Ihr bestehendes API-Token und Ihre Geheimnisse zur Verfügung stellen, damit Lexer diese Exporte in Ihrem Namen durchführen kann. Es importiert auch Ihre Braze-Daten in Lexer unter Verwendung dieser Anmeldeinformationen und Ihrer S3-Konfiguration, um Ihre Daten auf beiden Plattformen automatisch zu synchronisieren.

## Segmente an Braze senden

### Schritt 1: Aktivierung erstellen

Lexer Activate aktualisiert Ihre Braze-Profile automatisch und fügt Attribute hinzu oder entfernt sie, wenn Kunden Ihr Segment betreten oder verlassen.

1. In Lexer klicken Sie unter **Lexer-Aktivierungen** auf **NEUE AUDIENZ AKTIVIEREN**.
2. Wählen Sie die passende Braze-Aktivierung für diese Kampagne.
3. Fügen Sie Ihr Segment hinzu.
4. Aktualisieren Sie den Namen Ihrer Zielgruppe; dieser wird in Braze zu Ihrem Attributwert.
5. Dies ist das benutzerdefinierte Attribut, das wir in Braze aktualisieren werden. Wenden Sie sich zum Aktualisieren an den [Lexer-Support](support@lexer.io).
6. Markieren Sie die entsprechende Listenaktion - in den meisten Fällen werden Sie Ihre Liste pflegen wollen.
7. Prüfen Sie die Bedingungen und klicken Sie auf **AUDIENCE SENDEN**.

![][7]

### Schritt 2: Überprüfung der Aktivierung

Sobald Ihre Aktivierung in Aktivieren als gesendet bestätigt wurde, werden Sie sehen, dass die Datensätze in Braze aktualisiert werden. Ihre Profile werden in Braze erst dann vollständig aktualisiert, wenn Sie eine Bestätigungs-E-Mail von Lexer erhalten haben.

### Schritt 3: Erstellen Sie Ihr Braze-Segment

In Braze sehen Sie, dass der Name Ihrer Zielgruppe in Lexer jetzt ein Wert in Ihrem benutzerdefinierten Attribut `lexer_audience` ist. Braze hat ein Limit von 100 Werten pro Attribut.

Um Ihr Segment zu erstellen, navigieren Sie zu **Segment > + Segment erstellen** und wählen Sie **Benutzerdefiniertes Attribut** als Filter. Als nächstes wählen Sie `lexer_audience` als Attribut und den gewünschten Namen der Lexer-Zielgruppe. Wenn Sie fertig sind, **speichern Sie** Ihr Publikum.

Sie können dieses neu erstellte Segment nun zu zukünftigen Braze-Kampagnen und Canvases hinzufügen, um diese Endbenutzer anzusprechen.

[1]: {% image_buster /assets/img/lexer/braze_integrate_screen.png %}
[2]: {{site.baseurl}}/api/basics/#company-secret-explanation
[3]: https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/
[4]: https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html
[5]: {{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/
[6]: https://lexer.io/
[7]: {% image_buster /assets/img/lexer/lexer.png %}

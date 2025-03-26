---
nav_title: Google Cloud-Speicher
article_title: Google Cloud-Speicher
alias: /partners/google_cloud_storage_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Google Cloud Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud-Speicher

> [Google Cloud Storage](https://cloud.google.com/storage/) ist ein massiv skalierbarer Objektspeicher für unstrukturierte Daten, der von Google als Teil der Cloud Computing-Produktsuite angeboten wird.

Die Integration von Braze und Google Cloud Storage ermöglicht es Ihnen, Currents-Daten an Google Cloud Storage zu übertragen. Sie können später einen ETL-Prozess (Extrahieren, Transformieren, Laden) verwenden, um Ihre Daten an andere Stellen zu übertragen, z. B. Google BigQuery.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Google Cloud Storage-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Google Cloud Storage-Konto. |
| Currents | Um Daten zurück in Google Cloud Storage zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Für die Integration mit Google Cloud Storage müssen Sie die entsprechenden Anmeldeinformationen einrichten, die es Braze ermöglichen, Informationen über die Speicherbereiche zu erhalten, in die geschrieben wird (`storage.buckets.get`) und Objekte in diesem Bereich zu erstellen (`storage.objects.create`). 

Verwenden Sie dazu die folgenden Anweisungen, die Sie durch die Erstellung einer Rolle und eines Dienstkontos führen, das einen privaten Schlüssel für Ihre Currents-Integration erzeugt.

### Schritt 1: Rolle erstellen

Erstellen Sie eine neue Rolle in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Rollen** > **\+ Rolle erstellen** navigieren.

![][2]

Als nächstes geben Sie der Rolle einen Namen, wählen **+Berechtigungen hinzufügen** und fügen Folgendes hinzu: `storage.buckets.get`, `storage.objects.create`, und `storage.objects.get`. Wählen Sie dann **Erstellen**.

Fügen Sie optional `storage.objects.delete` Berechtigungen hinzu, damit Braze unvollständige Dateien bereinigen kann. In seltenen Fällen kann es vorkommen, dass Google Cloud die Verbindung vorzeitig beendet, was dazu führt, dass Braze unvollständige Dateien in Google Cloud Storage schreibt. Unter normalen Umständen wird Braze es erneut versuchen und eine neue Datei mit den korrekten Daten erstellen, wobei die alte Datei im Google Cloud Storage verbleibt.

![][3]

### Schritt 2: Erstellen Sie ein Dienstkonto

Erstellen Sie ein neues Servicekonto in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Servicekonten** navigieren und **Servicekonto erstellen** wählen.

![][4]

Als nächstes geben Sie dem Dienstkonto einen Namen und gewähren ihm Zugriff auf Ihre neu erstellte benutzerdefinierte Rolle.

![In der Google Cloud Platform geben Sie auf der Seite Dienste erstellen den Namen Ihrer Rolle in das Feld "Wählen Sie eine Rolle" ein.][5]

#### Einen Schlüssel erstellen

Verwenden Sie unten auf der Seite die Schaltfläche **Schlüssel erstellen**, um einen privaten **JSON-Schlüssel** zur Verwendung in Braze zu erstellen. Nachdem der Schlüssel erstellt wurde, wird er auf Ihren Computer heruntergeladen.

![][6]

### Schritt 3: Ströme in Braze einrichten

Navigieren Sie in Braze zu **Currents** > **\+ Create Current** > **Google Cloud Storage Data Export** und geben Sie Ihren Integrationsnamen und Ihre Kontakt-E-Mail an.

Als nächstes laden Sie Ihren privaten JSON-Schlüssel unter **GCS JSON Credentials** hoch und geben den Namen Ihres CGS-Buckets und das GCS-Präfix (optional) an. 

{% alert important %}
Es ist wichtig, dass Sie Ihre Anmeldedaten auf dem neuesten Stand halten. Wenn die Anmeldedaten Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

![Die Seite Google Cloud Storage Currents in Braze. Auf dieser Seite gibt es Felder für den Integrationsnamen, die Kontakt-E-Mail, die GCS JSON-Zugangsdaten, den GCS Bucket-Namen und das Präfix.][7]

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Ereignisse zum Nachrichtenverhalten oder zum Kundenverhalten Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### Schritt 4: Google Cloud Storage (GCS) Exporte einrichten

Um Google Cloud Storage (GCS) Exporte einzurichten, gehen Sie zu **Technologiepartner** > **Google Cloud Storage**, geben Sie Ihre GCS-Zugangsdaten ein und wählen Sie **Dies als Standardziel für den Datenexport festlegen**.

{% alert tip %}
Ihre **GCS JSON Credentials** werden generiert, indem Sie die Schritte in der [Google Cloud-Dokumentation](https://cloud.google.com/iam/docs/keys-create-delete) befolgen. Stellen Sie sicher, dass Sie den gesamten JSON-Wert eingeben, der generiert wird.
{% endalert %}

![Die Seite Google Cloud Storage im Braze Dashboard.][8]{: style="max-width:70%;"}

Ihr entsprechendes Google Cloud IAM-Servicekonto muss über die folgenden Berechtigungen verfügen (Sie können dies bestätigen, indem Sie auf der Seite **Google Cloud Storage** in Braze die Schaltfläche **Zugangsdaten testen** auswählen):
- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.get`
- `storage.objects.list`

Die Organisation und der Inhalt der exportierten Dateien sind bei der Integration von AWS S3, Microsoft Azure und Google Cloud Storage identisch.

## Verhalten beim Exportieren

Benutzer, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, haben folgende Probleme:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Benutzers gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert. 

[2]: {% image_buster /assets/img/gcs1.png %}
[3]: {% image_buster /assets/img/gcs2.png %}
[4]: {% image_buster /assets/img/gcs3.png %}
[5]: {% image_buster /assets/img/gcs4.png %}
[6]: {% image_buster /assets/img/gcs5.png %}
[7]: {% image_buster /assets/img/gcs6.png %}
[8]: {% image_buster /assets/img/gcs7.png %}

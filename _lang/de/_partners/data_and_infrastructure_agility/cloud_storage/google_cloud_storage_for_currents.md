---
nav_title: Google-Cloudspeicher
article_title: Google-Cloudspeicher
alias: /partners/google_cloud_storage_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Google Cloud Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google-Cloudspeicher

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

![]({% image_buster /assets/img/gcs1.png %})



- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
 <br><br>In seltenen Fällen kann es vorkommen, dass Google Cloud die Verbindung vorzeitig beendet, was dazu führt, dass Braze unvollständige Dateien in Google Cloud Storage schreibt. 
{% endalert %}



![]({% image_buster /assets/img/gcs2.png %})

### Schritt 2: 

#### Schritt 2.1: 

Erstellen Sie ein neues Servicekonto in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Servicekonten** navigieren und **Servicekonto erstellen** wählen.

![]({% image_buster /assets/img/gcs3.png %})

Als nächstes geben Sie dem Dienstkonto einen Namen und gewähren ihm Zugriff auf Ihre neu erstellte benutzerdefinierte Rolle.



#### Schritt 2.2: Einen Schlüssel erstellen

Verwenden Sie unten auf der Seite die Schaltfläche **Schlüssel erstellen**, um einen privaten **JSON-Schlüssel** zur Verwendung in Braze zu erstellen. Nachdem der Schlüssel erstellt wurde, wird er auf Ihren Computer heruntergeladen.

![]({% image_buster /assets/img/gcs5.png %})

### Schritt 3: Ströme in Braze einrichten

Navigieren Sie in Braze zu **Currents** > **\+ Create Current** > **Google Cloud Storage Data Export** und geben Sie Ihren Integrationsnamen und Ihre Kontakt-E-Mail an.

Als nächstes laden Sie Ihren privaten JSON-Schlüssel unter **GCS JSON Credentials** hoch und geben den Namen Ihres CGS-Buckets und das GCS-Präfix (optional) an. 

{% alert important %}
Es ist wichtig, dass Sie Ihre Anmeldedaten auf dem neuesten Stand halten. Wenn die Anmeldedaten Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

![Die Seite Google Cloud Storage Currents in Braze. 

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Ereignisse zum Nachrichtenverhalten oder zum Kundenverhalten Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### Schritt 4: 

Um Google Cloud Storage (GCS) Exporte einzurichten, gehen Sie zu **Technologiepartner** > **Google Cloud Storage**, geben Sie Ihre GCS-Zugangsdaten ein und wählen Sie **Dies als Standardziel für den Datenexport festlegen**.



{% alert important %}

{% endalert %}



### Schritt 5: 



- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`





## Verhalten beim Exportieren

Benutzer, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, haben folgende Probleme:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Benutzers gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert.

## Fehlersuche

### 



```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```



- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`



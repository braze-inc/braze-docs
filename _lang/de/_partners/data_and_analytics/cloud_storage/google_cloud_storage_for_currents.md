---
nav_title: Google-Cloudspeicher
article_title: Google-Cloudspeicher
alias: /partners/google_cloud_storage_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Google Cloud Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google-Cloudspeicher

> [Google Cloud Storage](https://cloud.google.com/storage/) ist ein massiv skalierbarer Objektspeicher für unstrukturierte Daten, der von Google als Teil der Cloud Computing Produkt Suite angeboten wird.

{% alert important %}
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren Customer-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Google Cloud Storage erlaubt es Ihnen, Daten von Currents zu Google Cloud Storage zu streamen. Sie können später einen ETL-Prozess (Extract, Transform, Load) verwenden, um Ihre Daten an andere Standorte zu übertragen, z. B. Google BigQuery.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Google Cloud Storage Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Google Cloud Storage-Konto. |
| Currents | Um Daten zurück in Google Cloud Storage zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Für die Integration mit Google Cloud Storage müssen Sie die entsprechenden Zugangsdaten einrichten, die es Braze erlauben, Informationen über die Speicher-Buckets zu erhalten, in die geschrieben wird (`storage.buckets.get`) und Objekte innerhalb dieses Buckets zu erstellen (`storage.objects.create`). 

Verwenden Sie dazu die folgenden Anweisungen, die Sie durch die Erstellung einer Rolle und eines Dienstkontos führen, die einen Private Key für Ihre Currents-Integration erzeugen.

### Schritt 1: Rolle erstellen

Erstellen Sie eine neue Rolle in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Rollen** > **\+ Rolle erstellen** navigieren.

![]({% image_buster /assets/img/gcs1.png %})

Geben Sie der Rolle einen Namen, wählen Sie dann **+Berechtigungen hinzufügen** und wählen Sie Folgendes aus:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
Die Berechtigung `storage.objects.delete` ist optional. Sie erlaubt es Braze, unvollständige Dateien zu bereinigen.<br><br>In seltenen Fällen kann es vorkommen, dass Google Cloud die Verbindung vorzeitig beendet, was dazu führt, dass Braze unvollständige Dateien in Google Cloud Storage schreibt. In den meisten Fällen wird Braze einen neuen Versuch unternehmen und eine neue Datei mit den richtigen Daten erstellen, wobei die alte Datei im Google Cloud Storage verbleibt.
{% endalert %}

Wenn Sie fertig sind, wählen Sie **Erstellen**.

![]({% image_buster /assets/img/gcs2.png %})

### Schritt 2: Ein neues Dienst-Konto erstellen

#### Schritt 2.1: Erstellen Sie das Konto für den Dienst

Erstellen Sie ein neues Dienstkonto in Ihrer Google Cloud Platform-Konsole, indem Sie zu **IAM & admin** > **Dienstkonten** navigieren und **Dienstkonto erstellen** auswählen.

![]({% image_buster /assets/img/gcs3.png %})

Als nächstes geben Sie dem Dienstkonto einen Namen und gewähren ihm Zugriff auf Ihre neu erstellte angepasste Rolle.

![In der Google Cloud Platform geben Sie auf der Seite zum Erstellen von Diensten den Namen Ihrer Rolle in das Feld "Rolle auswählen" ein.]({% image_buster /assets/img/gcs4.png %})

#### Schritt 2.2: Einen Schlüssel erstellen

Verwenden Sie unten auf der Seite den Button **Schlüssel erstellen**, um einen **JSON** Private Key zur Verwendung in Braze zu erstellen. Nachdem der Schlüssel erstellt wurde, wird er auf Ihren Computer heruntergeladen.

![]({% image_buster /assets/img/gcs5.png %})

### Schritt 3: Currents in Braze einrichten

Navigieren Sie in Braze zu **Currents** > **\+ Create Current** > **Google Cloud Storage Data Export** und geben Sie den Namen Ihrer Integration und Ihre E-Mail an.

Als nächstes laden Sie Ihren Private Key im JSON-Format unter **GCS JSON Credentials** hoch und geben den Bucket-Namen und das GCS-Präfix (optional) an. 

{% alert important %}
Es ist wichtig, dass Sie Ihre Zugangsdaten immer auf dem neuesten Stand halten. Wenn die Zugangsdaten für Ihren Konnektor ablaufen, sendet der Konnektor keine Ereignisse mehr. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

![Die Google Cloud Storage Currents Seite in Braze. Auf dieser Seite gibt es Felder für den Namen der Integration, die Zugangsdaten per E-Mail, die GCS JSON-Zugangsdaten, den Bucket-Namen und das Präfix.]({% image_buster /assets/img/gcs6.png %})

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Nachrichten-Engagement-Events oder Kundenverhalten-Events Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### Schritt 4: Google Cloud Storage-Exporte einrichten

Um den Export von Google Cloud Storage (GCS) einzurichten, gehen Sie zu **Technologiepartner** > **Google Cloud Storage**, geben Sie Ihre Zugangsdaten für GCS ein und wählen Sie **Dies als Standardziel für den Datenexport** aus.

Denken Sie daran, dass die Organisation und der Inhalt der exportierten Dateien bei der Integration von AWS S3, Microsoft Azure und Google Cloud Storage identisch sind.

{% alert important %}
Achten Sie darauf, dass Sie den vollständigen JSON-Wert eingeben, der [von Google Cloud generiert](https://cloud.google.com/iam/docs/keys-create-delete) wird.
{% endalert %}

![Die Google Cloud Storage Seite im Braze-Dashboard.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Schritt 5: Testen Sie Ihre Zugangsdaten für das Dienstkonto (optional)

Ihr Google Cloud IAM Dienst-Konto muss über die folgenden Berechtigungen verfügen:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Um diese Berechtigungen im Braze-Dashboard zu überprüfen, gehen Sie auf die Seite **Google Cloud Storage** und wählen Sie **Zugangsdaten testen**.

![Der Abschnitt mit den Zugangsdaten für Google Cloud Storage im Braze-Dashboard.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Verhalten beim Exportieren

Nutzer:innen, die eine Lösung zur Speicherung von Daten in der Cloud integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, werden folgende Probleme haben:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Nutzers:innen gesendet (keine Speicherberechtigung erforderlich) und auf dem Datenspeicher gesichert.

## Fehlersuche

### Google Cloud Storage-Zugangsdaten sind ungültig

Wenn Sie beim Versuch, Ihre Zugangsdaten einzugeben, die folgende Fehlermeldung erhalten:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Stellen Sie sicher, dass Ihr Google Cloud IAM Dienst-Konto über die folgenden Berechtigungen verfügt:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Nach der Überprüfung können Sie [Ihre Zugangsdaten im Braze-Dashboard testen](#step-5-test-your-service-account-credentials-optional).

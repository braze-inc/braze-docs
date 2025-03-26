---
nav_title: Microsoft Azure Blob-Speicher
article_title: Microsoft Azure Blob-Speicher
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze Currents und Microsoft Azure Blog Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob-Speicher

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) ist ein massiv skalierbarer Objektspeicher für unstrukturierte Daten, der von Microsoft als Teil der Azure-Produktsuite angeboten wird.

Die Integration von Braze und Microsoft Azure Blob Storage ermöglicht es Ihnen, Daten zurück nach Azure zu exportieren und Currents-Daten zu streamen. Später können Sie einen ETL-Prozess (Extract, Transform, Load) verwenden, um Ihre Daten an andere Orte zu übertragen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Microsoft Azure und Azure-Speicherkonto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie ein Microsoft Azure- und Azure-Storage-Konto. |
| Currents | Um Daten nach Currents zu exportieren, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Für die Integration mit Microsoft Azure Blob Storage benötigen Sie ein Speicherkonto und einen Verbindungsstring, damit Braze entweder Daten zurück nach Azure exportieren oder Currents-Daten streamen kann.

### Schritt 1: Erstellen Sie ein Speicherkonto

Navigieren Sie in Microsoft Azure in der Seitenleiste zu **Speicherkonten** und klicken Sie auf **\+ Hinzufügen**, um ein neues Speicherkonto zu erstellen. Als nächstes geben Sie den Namen eines Speicherkontos an. Andere Standardeinstellungen müssen nicht aktualisiert werden. Wählen Sie abschließend **Überprüfen + Erstellen**. 

Auch wenn Sie bereits ein Speicherkonto haben, empfehlen wir Ihnen, ein neues Konto speziell für Ihre Braze-Daten anzulegen.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Schritt 2: Abrufen der Verbindungszeichenfolge

Sobald das Speicherkonto eingerichtet ist, navigieren Sie vom Speicherkonto aus zum Menü **Zugriffsschlüssel** und notieren Sie sich die Verbindungszeichenfolge.

Microsoft stellt zwei Zugriffsschlüssel zur Verfügung, um Verbindungen mit einem Schlüssel aufrechtzuerhalten, während der andere regeneriert wird. Sie benötigen nur die Verbindungszeichenfolge von einem der beiden.

{% alert note %}
Braze verwendet die Verbindungszeichenfolge aus diesem Menü, nicht den Schlüssel.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Schritt 3: Erstellen Sie einen Blob Service Container

Navigieren Sie zum Menü **Blobs** unter dem Abschnitt **Blob Service** Ihres Speicherkontos. Erstellen Sie einen Blob Service Container in dem Speicherkonto, das Sie zuvor angelegt haben. 

Geben Sie einen Namen für Ihren Blob Service Container an. Andere Standardeinstellungen müssen nicht aktualisiert werden.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Schritt 4: Ströme einrichten

Navigieren Sie in Braze zu **Currents > + Create Current > Azure Blob Data Export** und geben Sie Ihren Integrationsnamen und Ihre Kontakt-E-Mail an.

Als Nächstes geben Sie Ihre Verbindungszeichenfolge, den Containernamen und das BlobStorage-Präfix (optional) an.

![Die Seite Microsoft Azure Blob Storage Currents in Braze. Auf dieser Seite gibt es Felder für den Integrationsnamen, die Kontakt-E-Mail, den Verbindungsstring, den Containernamen und das Präfix.]({% image_buster /assets/img/maz.png %})

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Ereignisse zum Nachrichtenverhalten oder zum Kundenverhalten Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### Schritt 5: Azure-Datenexport einrichten

Im Folgenden werden die Anmeldeinformationen konfiguriert, die für Folgendes verwendet werden:
1. Segmentexporte über die API
2. CSV-Exporte (Export von Kampagnen-, Segment- und Canvas-Benutzerdaten über das Dashboard)
3. Berichte zum Engagement

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** > **Microsoft Azure** und geben Sie Ihre Verbindungszeichenfolge, den Namen des Azure-Speichercontainers und das Azure-Speicherpräfix an.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Vergewissern Sie sich als nächstes, dass das Kontrollkästchen **Dies ist das Standardziel für den Datenexport** markiert ist. Dadurch wird sichergestellt, dass Ihre exportierten Daten an Azure gesendet werden. Wenn Sie fertig sind, speichern Sie Ihre Integration.

![Die Microsoft Azure-Datenexportseite in Braze. Auf dieser Seite gibt es Felder für Verbindungsstring, Containername und Präfix.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es ist wichtig, dass Sie Ihre Verbindungszeichenfolge auf dem neuesten Stand halten. Wenn die Anmeldeinformationen Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Verhalten beim Exportieren

Benutzer, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, haben folgende Probleme:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Benutzers gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert. 

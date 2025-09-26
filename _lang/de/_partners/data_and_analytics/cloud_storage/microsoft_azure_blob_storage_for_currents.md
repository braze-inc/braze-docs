---
nav_title: Microsoft Azure Blob-Speicher
article_title: Microsoft Azure Blob-Speicher
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze-Currents und Microsoft Azure Blog Storage, einem massiv skalierbaren Objektspeicher für unstrukturierte Daten."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob-Speicher

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) ist ein massiv skalierbarer Objektspeicher für unstrukturierte Daten, der von Microsoft als Teil der Azure Produkt Suite angeboten wird.

{% alert important %}
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren Customer-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Microsoft Azure Blob Storage erlaubt es Ihnen, Daten zurück nach Azure zu exportieren und Daten von Currents zu streamen. Später können Sie einen ETL-Prozess (Extract, Transform, Load) verwenden, um Ihre Daten an andere Standorte zu übertragen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Microsoft Azure und Azure Speicherkonto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie ein Microsoft Azure- und Azure-Storage-Konto. |
| Currents | Um Daten nach Currents zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Für die Integration mit Microsoft Azure Blob Storage benötigen Sie ein Speicherkonto und einen Verbindungs-String, damit Braze entweder Daten zurück nach Azure exportieren oder Currents-Daten streamen kann.

### Schritt 1: Erstellen Sie ein Speicherkonto

Navigieren Sie in Microsoft Azure in der Seitenleiste zu **Speicherkonten** und klicken Sie auf **\+ Hinzufügen**, um ein neues Speicherkonto zu erstellen. Als nächstes geben Sie den Namen eines Speicherkontos an. Andere Standardeinstellungen müssen nicht aktualisiert werden. Wählen Sie abschließend **Überprüfen + Erstellen**. 

Auch wenn Sie bereits ein Speicherkonto haben, empfehlen wir Ihnen, ein neues Konto speziell für Ihre Braze-Daten anzulegen.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Schritt 2: Abrufen des Strings für die Verbindung

Sobald das Speicherkonto eingerichtet ist, navigieren Sie vom Speicherkonto aus zum Menü **Zugriffsschlüssel** und notieren sich den Verbindungsstring.

Microsoft stellt zwei Zugriffsschlüssel zur Verfügung, um Verbindungen mit einem Schlüssel aufrechtzuerhalten, während der andere regeneriert wird. Sie benötigen nur den String für eine der Verbindungen.

{% alert note %}
Braze verwendet den Connection String aus diesem Menü, nicht den Schlüssel.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Schritt 3: Erstellen Sie einen Blob-Dienst-Container

Navigieren Sie zum Menü **Blobs** unter dem Abschnitt **Blob Service** Ihres Speicherkontos. Erstellen Sie einen Blob Service Container in dem Speicherkonto, das Sie zuvor angelegt haben. 

Geben Sie einen Namen für Ihren Blob Service Container an. Andere Standardeinstellungen müssen nicht aktualisiert werden.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Schritt 4: Currents einrichten

Navigieren Sie in Braze zu **Currents > + Create Current > Azure Blob Data Export** und geben Sie den Namen Ihrer Integration und eine E-Mail an.

Als Nächstes geben Sie den String für die Verbindung, den Containernamen und das BlobStorage-Präfix (optional) an.

![Die Microsoft Azure Blob-Speicher Currents Seite in Braze. Auf dieser Seite gibt es Felder für den Namen der Integration, die E-Mail des Kontakts, den Verbindungsstring, den Containernamen und das Präfix.]({% image_buster /assets/img/maz.png %})

Scrollen Sie schließlich zum Ende der Seite und wählen Sie aus, welche Nachrichten-Engagement-Events oder Kundenverhalten-Events Sie exportieren möchten. Wenn Sie fertig sind, starten Sie Ihren Current.

### Schritt 5: Azure Datenexport einrichten

Im Folgenden werden die Zugangsdaten konfiguriert, die für Folgendes verwendet werden:
1. Segmentexporte über die API
2. CSV-Exporte (Export von Kampagnen-, Segment- und Canvas-Nutzerdaten über das Dashboard)
3. Engagement-Berichte

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** > **Microsoft Azure** und geben Sie Ihren Verbindungsstring, den Namen des Azure-Speichercontainers und das Azure-Speicherpräfix an.

Vergewissern Sie sich als nächstes, dass das Kästchen **Dieses Ziel als Standard-Ziel für den Datenexport festlegen** markiert ist. Dadurch wird sichergestellt, dass Ihre exportierten Daten an Azure gesendet werden. Wenn Sie fertig sind, speichern Sie Ihre Integration.

![Die Microsoft Azure Datenexportseite in Braze. Auf dieser Seite gibt es Felder für den Connection String, den Containernamen und das Präfix.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
Es ist wichtig, den String für die Verbindung auf dem neuesten Stand zu halten. Wenn die Zugangsdaten für Ihren Konnektor ablaufen, sendet der Konnektor keine Ereignisse mehr. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

## Verhalten beim Exportieren

Nutzer:innen, die eine Lösung zur Speicherung von Daten in der Cloud integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, werden folgende Probleme haben:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Nutzers:innen gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert. 

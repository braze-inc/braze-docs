---
nav_title: BlueConic
article_title: BlueConic
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und BlueConic, einer führenden reinen Kundendatenplattform, die es Ihnen ermöglicht, Daten über persistente, individuelle Profile zu vereinheitlichen und sie dann über einen Amazon Web Services S3-Server zwischen den beiden Systemen für Importziele zu synchronisieren."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic][1], die führende reine Kundendatenplattform, befreit die Daten von Unternehmen aus unterschiedlichen Systemen und macht sie zugänglich, wo und wann immer sie benötigt werden, um Kundenbeziehungen zu verändern und das Unternehmenswachstum zu fördern. 

Die Integration von Braze und BlueConic ermöglicht es Anwendern, Daten in persistenten, individuellen Profilen zu vereinheitlichen und sie dann über einen Amazon Web Services S3-Server zwischen den beiden Systemen für Importziele zu synchronisieren. Zu den möglichen Zielen gehören wachstumsorientierte Initiativen, Orchestrierung des Kundenlebenszyklus, Modellierung und Analyse, digitale Produkte und Erlebnisse, zielgruppenbasierte Monetarisierung und mehr. Diese Integration unterstützt sowohl den geplanten Batch-Import als auch den Export. 

{% alert important %}
Wenn Sie die Integration verwenden, sendet BlueConic bei jeder Synchronisierung Deltas (sich ändernde Daten). Dazu gehören alle Profile, die sich seit dem letzten Senden geändert haben, sowie alle Attribute dieses Profils. Überwachen Sie die Nutzung der Datenpunkte entsprechend.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| BlueConic Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [BlueConic-Konto][1]. Um auf die Plugins zugreifen zu können, benötigen Sie in Ihrem BlueConic-Konto einen Zugang zum [Anzeigen und Bearbeiten von Verbindungen][4]. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists` und `segments.details`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][2] ab. |
| S3-Authentifizierung | Sie benötigen Zugang zu einem Amazon Web Services (S3) Server, um die Daten zu exportieren und zu importieren. |
| Zugriffsschlüssel-ID<br>Geheimer Zugangsschlüssel | Mit der Zugriffsschlüssel-ID und dem geheimen Zugriffsschlüssel können Sie Ihren S3-Server für den Import und Export authentifizieren. |
| AWS-Eimer | Sie müssen innerhalb des Plugins eine Verbindung zu S3 herstellen. Nach der Authentifizierung werden die verfügbaren Buckets in einem Dropdown-Menü angezeigt. Hier werden die zu importierenden oder zu exportierenden Dateien gespeichert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen einer Lötverbindung

Wählen Sie in BlueConic in der Navigationsleiste **Verbindungen** und dann **Verbindung hinzufügen**. Suchen Sie in der daraufhin angezeigten Eingabeaufforderung nach **Braze** und wählen Sie **Braze-Verbindung**. 

Erweitern oder reduzieren Sie die verfügbaren Metadatenfelder in der Verbindung, indem Sie auf das graue Chevron-Symbol klicken. In diesen Feldern können Sie diese Verbindung favorisieren, Ihrer Verbindung einen Namen geben, Beschriftungen hinzufügen, eine Beschreibung einfügen und auswählen, ob Sie E-Mail-Benachrichtigungen erhalten möchten, wenn die Verbindung [läuft oder nicht läuft][5]. 

Speichern Sie Ihre Einstellungen.

### Schritt 2: Konfigurieren einer Braze-Verbindung

Um die Verbindung zwischen BlueConic und Braze zu konfigurieren, müssen Sie Ihre Braze-Kontodaten und Ihre Amazon Web Services (S3) Kontoinformationen hinzufügen, um die Verbindung zu authentifizieren. 

1. Wählen Sie in BlueConic die Option **Einrichten und Ausführen** im Bereich **Einrichtung** im linken Fensterbereich.<br><br>
2. Geben Sie auf der sich öffnenden Braze-Authentifizierungsseite Ihren Braze-REST-API-Endpunkt und Ihren Braze-API-Schlüssel ein.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Im Abschnitt S3-Einrichtung und Authentifizierung geben Sie diese Anmeldedaten ein: Amazon Web Services (S3) Zugangsschlüssel-ID, geheimer Zugangsschlüssel und S3-Bucket. Es müssen [dieselben Anmeldeinformationen]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/amazon_s3/) sein, die Sie bei der Einrichtung der Integration von Braze und Amazon S3 konfiguriert haben. Speichern Sie Ihre Einstellungen. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Schritt 3: Erstellen von Import- oder Exportzielen (Importmapping)

Sobald die Authentifizierung abgeschlossen ist, müssen Sie mindestens ein Import- oder Exportziel erstellen, die Verbindung einschalten und die Verbindung planen oder ausführen.

{% tabs %}
{% tab Importieren %}

1. Wählen Sie im linken Bereich **Daten in BlueConic importieren**, um die Konfigurationsseite für Braze-Daten zu öffnen.<br><br>
2. Wählen Sie den Speicherort der Daten in Braze. Hier können Sie BlueConic mitteilen, wo die zu importierenden Daten zu finden sind, indem Sie Ihr Braze-Publikum auswählen.<br>![Das BlueConic Braze-Publikum wird als "BlueConic Test User" eingestellt.]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Als nächstes ordnen Sie Bezeichner zwischen Braze und BlueConic zu. <br>![Das Braze-Feld "Externe ID" wird auf das BlueConic-Feld "Externe ID" abgebildet.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Um die Kundendaten zwischen den beiden Systemen zu verknüpfen, geben Sie einen oder mehrere Kundenidentifikatoren ein.<br>Verwenden Sie das Kontrollkästchen **Erstellung zulassen...**, um BlueConic zu erlauben, neue Profile für Daten zu erstellen, die nicht zu einem bestehenden BlueConic-Profil passen.<br><br>
4. Als nächstes stimmen Sie die BlueConic-Datenfelder, die Sie exportieren möchten, mit den Braze-Feldern ab. Verwenden Sie die Dropdown-Felder, um entweder die BlueConic-Profilkennung oder eine Profileigenschaft auf der linken Seite auszuwählen und wählen Sie die entsprechende Braze-Profilkennung. Verwenden Sie als nächstes das Dropdown-Menü, um festzulegen, wie importierte Inhalte zu den vorhandenen Werten hinzugefügt werden sollen: addiert, summiert, nur gesetzt, wenn die Profileigenschaft leer ist, oder auf löschen gesetzt (wenn das Feld Braze leer ist).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Verwenden Sie die Schaltfläche **Zuordnung hinzufügen**, um bei Bedarf weitere Zuordnungszeilen zu erstellen. Mit der Option **Restliche Felder hinzufügen** können Sie mehrere Mapping-Zeilen hinzufügen. BlueConic erkennt die übrigen Braze-Felder und gleicht sie mit den BlueConic-Profileigenschaften ab. Sie können die Zusammenführungsstrategie für Importe festlegen (set, add, sum, set if empty oder clear) und den Namen der BlueConic-Profileigenschaften ein eigenes Präfix geben.<br><br>
5. Wählen Sie schließlich **Verbindung ausführen**, um die Verbindung zu starten. Besuchen Sie [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections), um mehr über das Planen und Ausführen von Verbindungen zu erfahren.
{% endtab %}
{% tab Exportieren %}

1. Wählen Sie im linken Bereich **Daten nach Braze exportieren**, um Ihren Datenexport von BlueConic nach Braze zu konfigurieren.<br><br>
2. Wählen Sie ein BlueConic Segment für den Export. Es werden nur Profile in diesem Segment exportiert, deren Identifikatoren in Braze übereinstimmen.<br>![Ein BlueConic Segment mit 20k Profilen.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Als nächstes verknüpfen Sie Bezeichner zwischen BlueConic-Profilen und Braze-Feldern. Sie können optional festlegen, dass BlueConic neue Datensätze erstellen soll, wenn keine Übereinstimmung gefunden wird.<br>![Das Braze-Feld "Externe ID" wird auf das BlueConic-Feld "Externe ID" abgebildet.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Als nächstes stimmen Sie die BlueConic-Datenfelder, die Sie exportieren möchten, mit den Braze-Feldern ab. Verwenden Sie das Dropdown-Menü des BlueConic-Symbols, um die Art der [Informationen](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) zu wählen, die Sie exportieren möchten. Zu den verfügbaren Informationen gehören Profileigenschaften, BlueConic Profilkennungen, zugehörige Segmente, alle angesehenen Interaktionen, Berechtigungsstufen und ein statischer Textwert.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Klicken Sie abschließend auf **Verbindung ausführen**, um die Verbindung zu starten. Besuchen Sie [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections), um mehr über das Planen und Ausführen von Verbindungen zu erfahren.
{% endtab %}
{% endtabs %}

## Schritt 4: Verbindung einschalten

Verwenden Sie den Kippschalter neben dem Titel der Braze-Verbindung, um die Verbindung ein- und auszuschalten. Eine Verbindung muss eingeschaltet sein, um während der geplanten Zeiten zu laufen. 

[1]: https://www.blueconic.com/
[2]: https://portal.aws.amazon.com/billing/signup#/start
[3]: https://console.aws.amazon.com/iam/home?#security_credential
[4]: https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles
[5]: https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ
---
nav_title: BlueConic
article_title: BlueConic
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und BlueConic, einer führenden reinen Kundendaten-Plattform, die es Ihnen erlaubt, Daten in persistenten, individuellen Profilen zu vereinheitlichen und sie dann über einen Amazon S3 Server der Serviceleistungen für Importziele zwischen den beiden Systemen zu synchronisieren."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/), die führende Pure-Play Customer Data Platform, befreit die First-Party-Daten von Unternehmen aus unterschiedlichen Systemen und macht sie zugänglich, wo und wann immer sie benötigt werden, um Kundenbeziehungen zu transformieren und das Geschäftswachstum zu fördern. 

_Diese Integration wird von Blueconic gepflegt._

## Über die Integration

Die Integration von Braze und BlueConic erlaubt es Nutzern:innen, Daten in persistenten, individuellen Profilen zu vereinheitlichen und dann über einen Amazon S3 Server der Serviceleistungen; Dienste zwischen den beiden Systemen für Importziele zu synchronisieren. Zu den möglichen Zielen gehören wachstumsorientierte Initiativen, Orchestrierung des Kundenlebenszyklus, Modellierung und Analytics, digitale Produkte und Erlebnisse, zielgruppenorientierte Monetarisierung und vieles mehr. Diese Integration unterstützt sowohl den geplanten Batch-Import als auch den Export. 

{% alert important %}
Wenn Sie die Integration verwenden, sendet BlueConic bei jeder Synchronisierung Deltas (sich ändernde Daten). Dazu gehören alle Profile, die sich seit dem letzten Senden geändert haben, sowie alle Attribute dieses Profils. Überwachen Sie die Datenpunkt-Nutzung entsprechend.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| BlueConic Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [BlueConic-Konto](https://www.blueconic.com/). Um auf die Plugins zugreifen zu können, benötigen Sie in Ihrem BlueConic-Konto einen Zugang zum [Anzeigen und Bearbeiten von Verbindungen](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists`, und `segments.details`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz](https://portal.aws.amazon.com/billing/signup#/start) ab. |
| S3-Authentifizierung | Zum Exportieren und Importieren der Daten benötigen Sie Zugang zu einem Server von Amazon Serviceleistungen (S3). |
| ID des Zugriffsschlüssels<br>Geheimer Zugangsschlüssel | Die ID des Zugriffsschlüssels und der geheime Zugriffsschlüssel ermöglichen Ihnen die Authentifizierung Ihres S3 Servers für den Import und Export. |
| AWS Bucket | Sie müssen innerhalb des Plugins eine Verbindung zu S3 herstellen. Nach der Authentifizierung werden die verfügbaren Buckets in einem Dropdown-Menü angezeigt. Hier werden die zu importierenden oder zu exportierenden Dateien gespeichert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen einer Braze-Verbindung

Wählen Sie in BlueConic in der Navigationsleiste **Verbindungen** aus und dann **Verbindung hinzufügen**. Suchen Sie in der daraufhin angezeigten Eingabeaufforderung nach **Braze** und wählen Sie **Braze-Verbindung** aus. 

Erweitern oder reduzieren Sie die verfügbaren Metadatenfelder in der Verbindung, indem Sie auf das graue Chevron-Symbol klicken. In diesen Feldern können Sie diese Verbindung favorisieren, ihr einen Namen geben, Beschriftungen hinzufügen, eine Beschreibung einfügen und festlegen, dass Sie per E-Mail benachrichtigt werden, wenn die Verbindung [läuft oder nicht läuft](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ). 

Speichern Sie Ihre Einstellungen.

### Schritt 2: Konfigurieren einer Braze-Verbindung

Um die Verbindung zwischen BlueConic und Braze zu konfigurieren, müssen Sie die Zugangsdaten Ihres Braze-Kontos und die Daten Ihres Amazon Web Serviceleistungen; Dienste (S3)-Kontos hinzufügen, um die Verbindung zu authentifizieren. 

1. Wählen Sie in BlueConic im linken Panel im Bereich **Einrichtung** die Option **Einrichten und ausführen**.<br><br>
2. Geben Sie auf der sich öffnenden Braze-Authentifizierungsseite Ihren REST API-Endpunkt und Ihren Braze-API-Schlüssel ein.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. Im Abschnitt S3-Einrichtung und Authentifizierung geben Sie diese Zugangsdaten ein: Amazon S3 (Internet Serviceleistungen; Dienste) ID des Zugangsschlüssels, geheimer Zugangsschlüssel und S3-Bucket. Es müssen [dieselben Zugangsdaten]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) sein, die Sie bei der Einrichtung Ihrer Braze- und Amazon S3-Integration konfiguriert haben. Speichern Sie Ihre Einstellungen. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### Schritt 3: Erstellen von Import- oder Exportzielen (Import-Abbildung)

Sobald die Authentifizierung abgeschlossen ist, müssen Sie mindestens ein Import- oder Exportziel erstellen, die Verbindung einschalten und die Verbindung planen oder ausführen.

{% tabs %}
{% tab Importieren %}

1. Wählen Sie im linken Panel **Daten in BlueConic importieren**, um die Konfigurationsseite für Braze-Daten zu öffnen.<br><br>
2. Wählen Sie den Standort der Daten in Braze aus. Hier können Sie BlueConic mitteilen, wo die zu importierenden Daten zu finden sind, indem Sie Ihre Zielgruppe in Braze auswählen.<br>![Die Zielgruppe von BlueConic Braze wird als "BlueConic Nutzer:innen" festgelegt.]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. Als nächstes bilden Sie Bezeichner zwischen Braze und BlueConic ab. <br>![Das Braze-Feld "Externe ID", das auf das BlueConic-Feld "Externe ID" abgebildet werden soll.]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> Um die Kundendaten zwischen den beiden Systemen zu verknüpfen, geben Sie einen oder mehrere Bezeichner für die Kunden ein.<br>Verwenden Sie das Kontrollkästchen **Erstellung zulassen...**, um BlueConic zu erlauben, neue Profile für Daten zu erstellen, die nicht zu einem bestehenden BlueConic Profil passen.<br><br>
4. Als nächstes stimmen Sie die BlueConic Datenfelder, die Sie exportieren, mit den Braze Feldern ab. Verwenden Sie die Dropdown-Felder, um entweder den BlueConic Profil-Bezeichner oder eine Eigenschaft des Profils auf der linken Seite auszuwählen und wählen Sie den entsprechenden Braze Profil-Bezeichner aus. Verwenden Sie als nächstes das Dropdown-Menü, um festzulegen, wie importierte Inhalte zu den vorhandenen Werten hinzugefügt werden sollen: addiert, summiert, nur gesetzt, wenn die Eigenschaft des Profils leer ist, oder auf löschen gesetzt (wenn das Feld Braze leer ist).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>Verwenden Sie den Button **Abbildung hinzufügen**, um bei Bedarf weitere Abbildungen zu erstellen. Mit der Option **Restliche Felder hinzufügen** können Sie mehrere Zeilen mit Abbildungen hinzufügen. BlueConic erkennt die übrigen Felder von Braze und gleicht sie mit den Eigenschaften des BlueConic Profils ab. Sie können die Strategie für die Zusammenführung von Importen festlegen (setzen, hinzufügen, summieren, setzen, wenn leer oder löschen) und ein angepasstes Präfix für die Namen der Eigenschaften von BlueConic Profilen angeben.<br><br>
5. Wählen Sie schließlich **Verbindung ausführen**, um die Verbindung zu starten. Besuchen Sie [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections), um mehr über den Zeitplan und die Ausführung von Verbindungen zu erfahren.
{% endtab %}
{% tab Exportieren %}

1. Wählen Sie im linken Panel **Daten nach Braze exportieren** aus, um Ihren Datenexport von BlueConic nach Braze zu konfigurieren.<br><br>
2. Wählen Sie ein BlueConic Segment für den Export. Es werden nur Profile in diesem Segment mit übereinstimmenden Bezeichnern in Braze exportiert.<br>![Ein BlueConic Segment von 20k Profilen.]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. Als nächstes verknüpfen Sie Bezeichner zwischen BlueConic Profilen und Braze Feldern. Sie können optional festlegen, dass BlueConic neue Datensätze anlegen soll, wenn keine Übereinstimmung gefunden wird.<br>![Das Braze-Feld "Externe ID", das auf das BlueConic-Feld "Externe ID" abgebildet werden soll.]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. Als nächstes stimmen Sie die BlueConic Datenfelder, die Sie exportieren, mit den Braze Feldern ab. Verwenden Sie das Dropdown-Menü des BlueConic-Symbols, um die Art der [Informationen](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) zu wählen, die Sie exportieren möchten. Zu den verfügbaren Informationen gehören Profileigenschaften, BlueConic Profil Bezeichner, zugehörige Segmente, alle angesehenen Interaktionen, Berechtigungsstufen und ein statischer Textwert.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. Klicken Sie abschließend auf **Verbindung ausführen**, um die Verbindung zu starten. Besuchen Sie [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections), um mehr über den Zeitplan und die Ausführung von Verbindungen zu erfahren.
{% endtab %}
{% endtabs %}

## Schritt 4: Verbindung umschalten

Verwenden Sie den Kippschalter neben dem Titel der Braze-Verbindung, um die Verbindung ein- und auszuschalten. Eine Verbindung muss eingeschaltet sein, um zu den geplanten Zeiten zu laufen. 



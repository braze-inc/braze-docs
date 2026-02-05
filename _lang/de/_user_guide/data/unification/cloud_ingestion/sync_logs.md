---
nav_title: Synchronisationsprotokolle und Beobachtbarkeit
article_title: Synchronisationsprotokolle und Beobachtbarkeit
page_order: 10
page_type: reference
description: "Diese Seite bietet eine Übersicht über die in CDI verfügbaren Features zur Beobachtbarkeit."
---

# Synchronisationsprotokolle und Beobachtbarkeit

> Mit dem Dashboard Cloud Data Ingestion (CDI) **Sync Log** können Sie alle von CDI verarbeiteten Daten überwachen, überprüfen, ob die Daten erfolgreich synchronisiert wurden, und eventuelle Probleme mit "falschen" oder fehlenden Daten diagnostizieren.

Um auf die Synchronisierungsprotokolle zuzugreifen, gehen Sie zu **Dateneinstellungen** > **Datenaufnahme in der Cloud** und wählen Sie den Tab **Sync Log**.

## Das Dashboard Sync Log verstehen

Die Hauptseite **Synchronisierungsprotokoll** bietet eine Übersicht über alle Ihre Synchronisierungsläufe, einschließlich einer Übersicht der letzten Synchronisierungen nach ihrem aktuellen oder endgültigen Status.

* **Laufen:** Synchronisierungsaufträge, die derzeit ausgeführt werden.  
* **Erfolg:** Synchronisierungsaufträge, die abgeschlossen und alle Zeilen erfolgreich verarbeitet wurden.  
* **Teilweiser Erfolg:** Synchronisierungsaufträge, die abgeschlossen wurden, bei denen jedoch in einer oder mehreren Zeilen ein Fehler aufgetreten ist.  
* **Fehler:** Synchronisierungsaufträge, die nicht abgeschlossen werden konnten.  
* **Das Limit wurde überschritten:** Synchronisierungsaufträge, deren Verarbeitung wegen Überschreitung eines Datenlimits abgebrochen wurde.

![Ein Beispiel für Synchronisierungsprotokolle mit insgesamt 6.576 Erfolgen.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Die Synchronisierungsprotokolle enthalten außerdem die folgenden Details für jede Synchronisierung:

* **Sync-Name:** Der Name der Sync-Konfiguration.  
* **ID ausführen:** Ein eindeutiger Bezeichner für eine bestimmte Ausführung der Synchronisierung. Wählen Sie diese ID aus, um weitere Details anzuzeigen. Dies kann auch in den [CDI API Endpunkten]({{site.baseurl}}/api/endpoints/cdi) verwendet werden, oder um einen Synchronisationslauf mit Braze Support zu referenzieren.   
* **Status:** Der Status des Laufs (Erfolg, Teilerfolg, Fehler, läuft).  
* **Neue Zeilen aus der Quelle gelesen:** Die Anzahl der neuen Zeilen, die für diesen Lauf aus Ihrem Data Warehouse gezogen wurden.  
* **Ergebnisse:** Eine Aufschlüsselung, wie viele Zeilen innerhalb des Laufs erfolgreich waren oder fehlgeschlagen sind.  
* **Letzte "UPDATED_AT":** Der Zeitstempel des letzten Datensatzes, der in diesem Sync-Lauf verarbeitet wurde.  
* **Startzeit des Laufs:** Wann der Synchronisierungsauftrag begann.  
* **Dauer der Ausführung:** Die Gesamtzeit, die der Synchronisierungsauftrag gedauert hat.

![Details für ein Synchronisationsprotokoll.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Bindung von Daten

Sync-Protokolldaten, einschließlich aller Nutzdaten auf Zeilenebene und Fehlerdetails, werden bis zu **30 Tage** lang aufbewahrt. Protokolle, die älter als 30 Tage sind, werden automatisch gelöscht.

Die Metadaten des Synchronisierungslaufs, wie z.B. die Anzahl der verarbeiteten Zeilen, werden für mindestens 12 Monate aufbewahrt.

### Filtern von Synchronisierungsprotokollen

Sie können die Tabelle der Synchronisierungsprotokolle filtern, um bestimmte Läufe zu finden. Die verfügbaren Filter umfassen:

* **Datum des Arbeitsbeginns:** Wählen Sie einen vordefinierten Bereich (wie "Letzte 30 Tage") oder einen angepassten Datumsbereich.  
* **Status:** Filtern Sie nach einem oder mehreren Sync-Status (z.B. nur **Fehler-** und **Teilerfolgsstatus** anzeigen).  
* **Sync-Name:** Suchen Sie nach einer bestimmten Synchronisierung anhand ihres Namens.

Um eine bestimmte Synchronisierung zu untersuchen, wählen Sie die entsprechende **Run ID** aus der Tabelle Sync Logs aus. Auf der Seite **Ausführungsdetails** finden Sie ein detailliertes, zeilenweises Protokoll der Synchronisierung.

### Übersicht über den Lauf

Dieser Abschnitt fasst den ausgewählten Lauf zusammen, einschließlich der Startzeit, der Endzeit, der Dauer und der Gesamtanzahl der aus der Quelle gelesenen Zeilen. Außerdem wird angezeigt, wie viele Zeilen erfolgreich waren und wie viele zu einem Fehler führten.

### In dieser Ausführung verarbeitete Zeilen

Diese Tabelle bietet einen Einblick in die während der Synchronisierung verarbeiteten Daten auf Zeilenebene und ermöglicht es Ihnen, einzelne Datensätze zu überprüfen.

* **Suche:** Sie können in den Ergebnissen des Laufs nach einem bestimmten Nutzer:innen suchen, indem Sie die Leiste **Suche nach ID verwenden**.  
* **Verfügbare Details:**   
  * **UPDATED_AT:** Der Zeitstempel aus der Spalte `UPDATED_AT` für diese bestimmte Zeile.  
  * **ID:** Die Bezeichner (wie `external_id`, `email` oder `alias_name`), die verwendet werden, um den Datensatz mit einem Nutzerprofil von Braze abzugleichen.  
  * **Status:** Der individuelle Bearbeitungsstatus für diese Zeile**(Erfolg** oder **Fehler**).  
  * **Quell-Nutzlast:** Ein Link zum Anzeigen der Daten-Nutzdaten.  
  * **Fehlergrund:** Wenn der Status **Fehler** lautet, enthält diese Spalte eine Nachricht, die erklärt, warum die Zeile nicht synchronisiert werden konnte.

#### Anzeigen von Nutzdaten

Um die genauen Daten zu sehen, die für eine bestimmte Zeile an Braze gesendet wurden, wählen Sie **Nutzdaten anzeigen** in der Spalte **Quellnutzdaten**. Hier wird die rohe JSON-Nutzlast angezeigt, die für diesen Nutzer:innen verarbeitet wurde.

![Payload-Beispiel für eine bestimmte Zeile in einem Sync-Protokoll.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Synchronisierungsprotokolle exportieren

Wählen Sie **Zeilen exportieren**, um die Protokolle auf Zeilenebene für einen Synchronisierungslauf zu exportieren. Wählen Sie dann zum Exportieren nach:

* **Zeilen mit Fehlern:** Lädt eine Datei herunter, die nur die Zeilen enthält, die einen **Fehlerstatus** hatten.
* **Alle Zeilen:** Lädt eine Datei herunter, die alle in diesem Lauf verarbeiteten Zeilen enthält.

{% alert important %}
Das Exportieren von Synchronisierungsprotokollen für alle Zeilen befindet sich derzeit in einer frühen Phase. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

Protokolle können nicht direkt aus dem Dashboard exportiert werden. Nachdem der Export erstellt wurde, erhalten Sie eine E-Mail mit einem Link zum Herunterladen der Protokoll-Exportdatei. 

## Benachrichtigungen

Sie können E-Mail-Benachrichtigungen konfigurieren, um über den Status Ihrer CDI-Synchronisierungen informiert zu bleiben. Diese Einstellungen werden konfiguriert, wenn Sie eine Synchronisierung erstellen, und können jederzeit aktualisiert werden.

### Fehlerbenachrichtigungen

Mindestens eine E-Mail Adresse ist erforderlich, um Benachrichtigungen über Synchronisierungsfehler zu erhalten. Diese Warnungen werden gesendet, wenn ein ganzer Synchronisierungsauftrag nicht ausgeführt oder abgeschlossen werden kann oder wenn die Synchronisierung auf einen Fehler stößt, der ein Eingreifen des Nutzers:in erfordert, z.B. abgelaufene Zugangsdaten oder eine fehlende Quelltabelle.

Zusätzliche Benachrichtigungen umfassen:

- **Zeilenfehler:** Erhalten Sie Warnungen, wenn ein bestimmter Prozentsatz von Zeilen innerhalb einer Synchronisierung nicht aktualisiert wird.
- **Schwellenwert für das Scheitern (%):** Geben Sie den Prozentsatz der Zeilenausfälle an, die einen Alarm auslösen sollen. Wenn Sie diesen Wert beispielsweise auf **1** setzen, erhalten Sie eine Benachrichtigung, wenn 1 % oder mehr der Zeilen in einem Synchronisierungslauf zu einem Fehler führen.
- **Synchronisierung erfolgreich:** Erhalten Sie eine Benachrichtigung über den erfolgreichen Abschluss einer Synchronisierung.
- **Warnung, auch wenn sich keine Zeilen ändern:** Sie erhalten auch dann eine Benachrichtigung, wenn ein erfolgreicher Synchronisierungslauf keine neuen oder aktualisierten Zeilen verarbeitet.
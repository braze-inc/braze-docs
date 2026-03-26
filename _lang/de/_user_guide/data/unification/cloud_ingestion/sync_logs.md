---
nav_title: Synchronisieren Sie Protokolle und Beobachtbarkeit.
article_title: Synchronisieren Sie Protokolle und Beobachtbarkeit.
page_order: 10
page_type: reference
description: "Diese Seite bietet eine Übersicht über die in CDI verfügbaren Observability-Features."
---

# Synchronisieren Sie Protokolle und Beobachtbarkeit.

> Über das Dashboard „Cloud Data Ingestion (CDI) **Sync Log“** können Sie alle von CDI verarbeiteten Daten überwachen, überprüfen, ob die Daten erfolgreich synchronisiert wurden, und Probleme mit „falschen“ oder fehlenden Daten diagnostizieren.

Um auf die Synchronisierungsprotokolle zuzugreifen, navigieren Sie bitte zu **„Dateneinstellungen“** > **„Cloud-Datenaufnahme“** und wählen Sie die Registerkarte **„Synchronisierungsprotokoll“** aus.

## Das Dashboard „Synchronisierungsprotokoll“ verstehen

Die Hauptseite **„Synchronisierungsprotokoll“** bietet einen umfassenden Überblick über alle Ihre Synchronisierungsläufe, einschließlich einer Übersicht über die letzten Synchronisierungen nach ihrem aktuellen oder endgültigen Status.

* **Laufen:** Synchronisieren Sie derzeit ausgeführte Aufträge.  
* **Erfolg:** Synchronisierungsaufträge wurden abgeschlossen, und alle Zeilen wurden erfolgreich verarbeitet.  
* **Teilweise erfolgreich:** Synchronisierungsaufträge, die abgeschlossen wurden, jedoch bei einer oder mehreren Zeilen ein Fehler aufgetreten ist.  
* **Fehler:** Synchronisierungsaufträge, die nicht abgeschlossen werden konnten.  
* **Grenze überschritten:** Synchronisieren Sie Aufträge, deren Verarbeitung aufgrund einer überschrittenen Begrenzung der Daten unterbrochen wurde.

![Ein Beispiel für Synchronisierungsprotokolle mit insgesamt 6.576 erfolgreichen Vorgängen.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Synchronisierungsprotokolle enthalten außerdem die folgenden Details zu jeder Synchronisierung:

* **Synchronisierungsname:** Der Name der Synchronisierungskonfiguration.  
* **Lauf-ID:** Ein eindeutiger Bezeichner für eine bestimmte Ausführung der Synchronisierung. Bitte wählen Sie diese ID aus, um weitere Details anzuzeigen. Dies kann auch in den [CDI-API-Endpunkten]({{site.baseurl}}/api/endpoints/cdi) verwendet werden oder um einen Synchronisierungslauf mit Braze Support zu referenzieren.   
* **Status:** Der Status des Laufs (erfolgreich, teilweise erfolgreich, Fehler, läuft).  
* **Neue Zeilen aus der Quelle gelesen:** Die Anzahl der neuen Zeilen, die für diesen Durchlauf aus Ihrem Data Warehouse abgerufen wurden.  
* **Ergebnisse:** Eine Aufschlüsselung der Anzahl der erfolgreichen und fehlgeschlagenen Zeilen innerhalb des Durchlaufs.  
* **Letzter"UPDATED_AT": ** Der Zeitstempel des letzten Datensatzes, der in diesem Synchronisierungslauf verarbeitet wurde.  
* **Startzeit des Laufs:** Wann der Synchronisierungsauftrag begonnen hat.  
* **Laufzeit:** Die Gesamtzeit, die der Synchronisierungsauftrag benötigt hat, um abgeschlossen zu werden.

![Details zum Synchronisierungsprotokoll.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Bindung der Daten

Synchronisierungsprotokolldaten, einschließlich aller Daten auf Zeilenebene und Fehlerdetails, werden bis zu **30 Tage** lang aufbewahrt. Protokolle, die älter als 30 Tage sind, werden automatisch gelöscht.

Synchronisierungslauf-Metadaten, wie beispielsweise die Anzahl der verarbeiteten Zeilen, werden mindestens 12 Monate lang aufbewahrt.

### Synchronisierungsprotokolle filtern

Sie können einen Filter für die Synchronisierungsprotokolltabelle anwenden, um bestimmte Durchläufe zu finden. Die verfügbaren Filter umfassen:

* **Arbeitsbeginn:** Bitte wählen Sie einen vordefinierten Zeitraum (z. B. „Letzte 30 Tage“) oder einen angepassten Zeitraum aus.  
* **Status:** Filtern Sie nach einem oder mehreren Synchronisierungsstatus (z. B. nur **Fehler-** und **Teil**-Erfolgsstatus anzeigen).  
* **Synchronisierungsname:** Suchen Sie nach einer bestimmten Synchronisierung anhand ihres Namens.

Um eine bestimmte Synchronisierung zu untersuchen, wählen Sie bitte die entsprechende **Run-ID** aus der Tabelle „Synchronisierungsprotokolle“ aus. Auf der Seite **„Ausführungsdetails**“ finden Sie ein detailliertes Protokoll der Synchronisierung, das Zeile für Zeile aufgeführt ist.

### Übersicht über den Lauf

Dieser Abschnitt fasst den ausgewählten Lauf zusammen, einschließlich Startzeit, Endzeit, Dauer und Gesamtzahl der aus der Quelle gelesenen Zeilen. Es wird auch angegeben, wie viele Zeilen erfolgreich verarbeitet wurden und wie viele zu einem Fehler geführt haben.

### In dieser Ausführung verarbeitete Zeilen

Diese Tabelle bietet Transparenz auf Zeilenebene hinsichtlich der während der Synchronisierung verarbeiteten Daten, sodass Sie einzelne Datensätze überprüfen können.

* **Suche:** Sie können mithilfe der Suchleiste **„Suche nach Benutzer-ID“** innerhalb der Ergebnisse des Durchlaufs nach einem bestimmten Nutzer:in suchen.  
* **Verfügbare Informationen:**   
  * **UPDATED_AT:** Der Zeitstempel aus der`UPDATED_AT`Spalte für diese bestimmte Zeile.  
  * **ID:** Die Bezeichner (wie `external_id`, `email`, oder `alias_name`), die verwendet werden, um den Datensatz mit einem Braze-Nutzerprofil abzugleichen.  
  * **Status:** Der individuelle Verarbeitungsstatus für diese Zeile (**Erfolgreich** oder **Fehler**).  
  * **Quell-Nutzlast:** Ein Link zum Anzeigen der Daten-Nutzlast.  
  * **Grund für den Fehler:** Wenn der Status **„Fehler“** lautet, enthält diese Spalte eine Nachricht, die erklärt, warum die Zeile nicht synchronisiert werden konnte.

#### Anzeigen von Nutzlasten

Um die genauen Daten anzuzeigen, die für eine bestimmte Zeile an Braze gesendet wurden, wählen Sie in der Spalte **„Quell**-Payload“ **die Option „Payload anzeigen“** aus. Hiermit wird die rohe JSON-Nutzlast angezeigt, die für diesen Nutzer:in verarbeitet wurde.

![Beispiel für die Nutzlast einer bestimmten Zeile in einem Synchronisierungsprotokoll.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Synchronisierungsprotokolle exportieren

Wählen Sie **„Zeilen auswählen“,** um die Protokolle auf Zeilenebene für einen Synchronisierungslauf zu exportieren. Wählen Sie anschließend die Exportmethode:

* **Zeilen mit Fehlern:** Lädt eine Datei herunter, die ausschließlich die Zeilen mit dem Status **„Fehler“** enthält.
* **Alle Zeilen:** Lädt eine Datei herunter, die alle in diesem Durchlauf verarbeiteten Zeilen enthält.

{% multi_lang_include early_access_beta_alert.md feature='Exporting sync logs for all rows' %}

Protokolle können nicht direkt aus dem Dashboard exportiert werden. Nach der Erstellung des Exports erhalten Sie eine E-Mail mit einem Link zum Herunterladen der Protokollexportdatei. 

## Benachrichtigungen

Sie können E-Mail-Benachrichtigungen konfigurieren, um über den Status Ihrer CDI-Synchronisierungen auf dem Laufenden zu bleiben. Diese Einstellungen werden beim Erstellen einer Synchronisierung konfiguriert und können jederzeit ein Update erhalten.

### Fehlermeldungen

Es ist mindestens eine E-Mail-Adresse erforderlich, um Benachrichtigungen über Fehler auf Synchronisierungsebene zu erhalten. Diese Benachrichtigungen werden versendet, wenn ein gesamter Synchronisierungsauftrag nicht ausgeführt oder abgeschlossen werden kann oder wenn bei der Synchronisierung ein Fehler auftritt, der eine Änderung durch die Nutzer:innen erfordert, beispielsweise abgelaufene Zugangsdaten oder eine fehlende Quelltabelle.

Weitere Benachrichtigungen umfassen:

- **Zeilenfehler:** Erhalten Sie Benachrichtigungen, wenn ein bestimmter Prozentsatz der Zeilen bei einer Synchronisierung nicht ein Update erhalten kann.
- **Ausfallschwelle (%):** Geben Sie den Prozentsatz der Zeilenfehler an, der eine Warnmeldung triggern soll. Wenn Sie diesen Wert beispielsweise auf **1** setzen, wird eine Benachrichtigung gesendet, wenn 1 % oder mehr der Zeilen in einem Synchronisierungslauf zu einem Fehler führen.
- **Synchronisierung erfolgreich:** Bitte beachten Sie, dass Sie eine Benachrichtigung erhalten, sobald die Synchronisierung erfolgreich abgeschlossen wurde.
- **Bitte beachten Sie, dass auch bei unveränderten Zeilen eine Benachrichtigung erfolgt.** Erhalten Sie eine Benachrichtigung, auch wenn bei einer erfolgreichen Synchronisierung keine neuen oder Updates verarbeitet werden.
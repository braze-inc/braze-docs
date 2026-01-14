---
nav_title: Aktions-Pfade
article_title: Aktionspfade 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Dieser Referenzartikel beschreibt die Verwendung von Action Paths, einer Komponente, mit der Sie Benutzer auf der Grundlage ihrer Aktionen sortieren können."
tool: Canvas
---

# Aktionspfade 

> Mit den Aktionspfaden in Canvas können Sie Ihre Benutzer auf der Grundlage ihrer Aktionen sortieren. 

![Ein Aktions-Pfad-Schritt in einer Canvas-Nutzer:innen-Reise.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Mit Aktionspfaden können Sie:

* Passen Sie Nutzerpfade auf der Grundlage einer bestimmten Aktion an, einschließlich Customer-Engagement-Events und angepasste Events
* Binden Sie Nutzer:innen für eine bestimmte Zeitspanne, um ihren nächsten Pfad auf der Grundlage ihrer Aktionen während dieses Zeitraums zu priorisieren

## Einen Aktions-Pfad erstellen

Um einen Aktionspfad zu erstellen, fügen Sie eine Komponente zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag & Drop aus der Seitenleiste oder wählen Sie die Schaltfläche <i class="fas fa-plus-circle"></i> plus am unteren Rand eines Schritts und wählen Sie **Aktionspfade**. 

### Aktionseinstellungen

Legen Sie in den **Aktionseinstellungen** das **Bewertungsfenster** fest, um zu bestimmen, wie lange Benutzer in dem Schritt gehalten werden. Standardmäßig werden Nutzer:innen innerhalb eines Tages bewertet, aber Sie können dieses Fenster je nach Ihrem Canvas in Sekunden, Minuten, Stunden, Tagen und Wochen anpassen. Das maximale Bewertungsfenster für einen Aktionspfad beträgt 31 Tage.

In den **Aktionseinstellungen** können Sie auch die Rangfolge für Ihre Komponenten aktivieren, indem Sie den Schalter **Benutzer in Rangfolge vorziehen** einschalten.

![Die Aktionseinstellungen mit einem Bewertungsfenster von 1 Tag.]({% image_buster /assets/img/actionpath_settings.png %})

In der Standardeinstellung ist **Ranking** ausgeschaltet. Wenn ein:e Nutzer:in den Aktionspfad aufruft und das mit einer Aktionsgruppe verbundene Trigger-Event ausführt, wird er sofort durch die entsprechende Aktionsgruppe geführt. Wenn ein Benutzer kein Trigger-Ereignis auslöst, rückt er am Ende des Bewertungszeitraums in die Standardgruppe **Alle anderen** vor.

Wenn **Nutzer:innen nach Rangfolge vorbringen** aktiviert ist, bedeutet dies, dass die **Rangfolge** eingeschaltet ist. Alle Nutzer:innen werden also bis zum Ende des Testzeitraums gebunden. Am Ende des Bewertungszeitraums durchlaufen die Nutzer:innen in der Aktionsgruppe mit der höchsten Priorität, für die sie am Ende des Bewertungszeitraums in Frage kommen. Nutzer:innen, die während des Bewertungsfensters keine der Aktionen durchführen, durchlaufen die Standardgruppe **Alle anderen**.

#### In-App-Nachrichten

Beachten Sie, dass der oder die Nutzer:in zwei Sitzungsstarts durchführen muss, um die In-App-Nachricht zu erhalten, wenn der Aktionsgruppen-Trigger eine Sitzung startet und der nächste Schritt eine In-App-Nachricht ist. Die erste Sitzung ordnet den oder die Nutzer:in der App-Gruppe innerhalb des Aktionspfads zu, und die zweite Sitzung triggert die In-App-Nachricht.

#### Beispiel für den Ranglistenstatus

Nehmen wir an, Sie haben einen Aktionspfad mit einem Bewertungszeitraum von einem Tag und zwei Aktionsgruppen: Gruppe 1 und Gruppe 2. Gruppe 1 hat das Trigger-Event „Sitzung starten“ und Gruppe 2 hat „Kauf tätigen“. Wenn **Ranking** aktiviert ist, werden alle Benutzer im Aktionspfad einen Tag lang "festgehalten". Wenn ein:e Nutzer:in eine Sitzung begonnen und einen Kauf getätigt hat, steigt er oder sie am Ende des Tages in den Pfad mit dem höchsten Rang auf. In diesem Fall würde der Benutzer in Gruppe 1 aufsteigen. 

Wenn im vorangegangenen Beispiel das **Ranking** ausgeschaltet ist und ein Benutzer eines der Trigger-Ereignisse ("Sitzung starten" oder "Kauf tätigen") ausführt, wird dieser Benutzer in der entsprechenden Aktionsgruppe basierend auf der Trigger-Aktion befördert.

Beachten Sie, dass sich die Entry-Eigenschaften von Canvas von den Event-Eigenschaften unterscheiden. Canvas-Eingabeeigenschaften sind Eigenschaften aus dem Ereignis, das den Canvas ausgelöst hat. Diese Eigenschaften können nur im ersten vollständigen Schritt eines Canvas verwendet werden, wenn Sie den ursprünglichen Canvas-Workflow verwenden. Bei der Verwendung von Canvas werden persistente Eingangs-Eigenschaften aktiviert und ermöglichen die Wiederverwendung der Eingangs-Eigenschaften im gesamten Canvas. Event-Eigenschaften hingegen haben ihren Ursprung in einem Event oder einer Aktion, die im Workflow des Nutzers oder der Nutzerin stattfindet.

### Aktionsgruppen

Fügen Sie einen oder mehrere Trigger hinzu, um Ihre Aktionsgruppen zu definieren. Hier können Sie eine Reihe von Triggern auswählen, z. B. wenn Nutzer:innen:

- Einen Kauf tätigen
- Eine Sitzung beginnen
- Ein [angepasstes Event]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) durchführen
- Ein Konversions-Event durchführen
- E-Mail-Adresse hinzufügen
- Ändern Sie den Wert eines angepassten Attributs (einschließlich Arrays, aber nicht verschachtelte angepasste Attribute). Dazu gehört das erstmalige Hinzufügen eines neuen Attributs mit einem Wert zu einem Nutzerprofil (wenn das Attribut vorher nicht vorhanden war).
- Ihren Abonnementstatus oder den Status Ihrer Abonnementgruppe aktualisieren
- Interaktion mit einer Kampagne oder Inhaltskarte
- Einen Standort eingeben
- Ein Geofence triggern
- Eine eingehende SMS oder WhatsApp-Nachricht senden

![Eine Aktionsgruppe namens "Gruppe 1" für Nutzer:innen, die einen Kauf tätigen.]({% image_buster /assets/img/actionpath_group.png %})

In jeder Aktionsgruppeneinstellung haben Sie außerdem die Möglichkeit, das Kontrollkästchen **Ich möchte, dass diese Gruppe den Canvas verlässt** auszuwählen. Das bedeutet, dass die Nutzer:innen dieser Gruppe den Canvas am Ende des Bewertungszeitraums verlassen.

### Canvase mit erneuter Qualifizierung

Wenn Nutzer:innen einen Aktions-Pfad mehrfach eingeben und gleichzeitig mehrere Einträge im Aktions-Pfad haben, variiert das erwartete Verhalten in Abhängigkeit vom **Ranking-Status**.

| Ranglistenstatus | Aktion Pfad Verhalten |
|---|--------------|
| **Aus** | Wenn eine relevante Aktion ausgeführt wird, dedupliziert Braze-Entrys und rückt den frühesten Entry sofort in der entsprechenden Aktionsgruppe nach vorne. <br><br/> Wenn eine relevante Aktion nicht durchgeführt wird, werden alle Entrys am Ende des entsprechenden Bewertungsfensters nach vorne gerückt. Es findet keine Deduplizierung statt. |
| **Ein** | Alle Entrys werden am Ende des jeweiligen Bewertungsfensters nach vorne gerückt. Es findet keine Deduplizierung statt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Beachten Sie, dass die Ranglisten [nach dem Start]({{site.baseurl}}/post-launch_edits/) nicht [mehr geändert werden können]({{site.baseurl}}/post-launch_edits/).



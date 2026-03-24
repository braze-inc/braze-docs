---
nav_title: Bearbeiten Sie Canvases nach dem Start
article_title: Bearbeiten Sie Canvases nach dem Start
page_order: 0
description: "Dieser Referenzartikel befasst sich mit den verschiedenen Aspekten eines Canvas, die nach dem ersten Start geändert werden können."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Bearbeiten Sie Canvases nach dem Start

> In diesem Referenzartikel erfahren Sie, was in einem Canvas nach dem ersten Start geändert werden kann.

Sie können Ihre Canvase nach dem Start bearbeiten, indem Sie:

* Einfügen neuer Canvas-Schritte in die User Journey
* Hinzufügen neuer Varianten und Verbindungen
* Anpassen der Variantenverteilung
* Anhalten oder Fortsetzen aller Canvas-Schritte

{% alert note %}
Die Verteilung der Kontrollvariante kann erst nach dem Start verringert werden.
{% endalert %}

Sie können in Ihrer User Journey alle folgenden Einträge löschen:

- [Canvas-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Leinwand-Varianten 
- Verbindungen zwischen Canvas-Schritten

Wenn Sie Ihre Canvas-Benutzerreise bearbeiten oder weitere Schritte hinzufügen möchten, gelten die folgenden Details:

- Benutzer, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt. 
- Wenn Ihre Einstellungen für den Canvas-Eingang es Nutzern:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte bestanden haben, zum erneuten Eintritt berechtigt.
- Benutzer, die sich derzeit in einem gestarteten Canvas befinden, aber noch nicht die Punkte der User Journey erreicht haben, an denen neue Schritte hinzugefügt werden, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten. 

Wenn Sie einen [Delay-]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) oder [Action Paths-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) löschen, können Sie die Benutzer, die derzeit in diesem Schritt warten, optional in einen anderen Canvas-Schritt umleiten. Bei Verzögerungen verbleiben die Nutzer:innen bis zum Ende der Verzögerungszeit in diesem Schritt. Bei Aktions-Pfaden verbleiben die Nutzer:innen bis zum Ende des Bewertungszeitraums in diesem Schritt.

Beachten Sie, dass Braze beim ersten Start eines Canvas die Benutzer in die Warteschlange des Nachrichtenschritts einreiht, in dem sie sich gerade befinden, und nicht in alle nachfolgenden Nachrichten im Canvas. Wenn Sie nach dem Start Änderungen an der Canvas vornehmen, können einige Nutzer:innen bereits in der Warteschlange stehen und die Änderungen möglicherweise nicht übernehmen. Wenn Sie die Canvas anhalten, duplizieren, dann ändern und diese neue Version starten, bewertet die Canvas alle Nutzer:innen erneut, nicht nur diejenigen, die noch nicht in die Warteschlange gestellt wurden.

Siehe den Abschnitt [Bewährte Verfahren](#best-practices) für spezifische Anwendungsfälle bei der Bearbeitung. Generell ist es ratsam, die Bearbeitung von Live-Canvase zu vermeiden, da es zu unerwartetem Verhalten kommen kann.

{% details Expand for original Canvas editor details %}

Beachten Sie die folgenden zulässigen Bearbeitungen des Canvas nach dem Start, je nachdem, mit welchem Workflow Ihr Canvas erstellt wurde. Wenn Ihr Canvas den ursprünglichen Canvas-Workflow verwendet, müssen Sie ihn zunächst in Canvas Flow klonen, um nach dem Start Änderungen vornehmen zu können.

Sie können bestehende Verbindungen weder bearbeiten noch löschen, und Sie können keinen Schritt zwischen bestehende verbundene Schritte einfügen. Wenn Sie Ihre Canvas-Benutzerreise bearbeiten oder weitere Schritte hinzufügen möchten, gelten die folgenden Details:

- Benutzer, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt. 
- Wenn Ihre Einstellungen für den Canvas-Eingang es Nutzern:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte bestanden haben, zum erneuten Eintritt berechtigt.
- Nutzer:innen, die sich derzeit in einem gestarteten Canvas befinden, aber noch nicht die neu hinzugefügten Schritte in der User Journey erreicht haben, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten.
- Wenn ein Verzögerungsschritt der letzte Schritt im Canvas ist, werden Benutzer, die diesen Schritt erreichen, automatisch aus dem Canvas befördert und erhalten keine neu erstellten Schritte mehr.

{% alert important %}
Wenn Sie die Einstellungen für **„Verzögerung“** oder **„Fenster“** für einen Canvas-Schritt aktualisieren, gelten für Nutzer:innen, die sich zum Zeitpunkt des Updates in diesem Schritt befinden, weiterhin die Verzögerungszeiten, die ihnen bei ihrem ursprünglichen Eintritt zugewiesen wurden. Nur neue Nutzer:innen, die sich bei Canvas anmelden, und diejenigen, die noch nicht in der Warteschlange für diesen Schritt stehen, erhalten die Nachricht zum aktualisierten Zeitpunkt.
{% endalert %}

Das Beenden eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang einer Nachricht warten, aus dem System ausgeloggt werden. Wenn Sie Canvas wieder aktivieren und die Nutzer:innen noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen; in diesem Fall erhalten sie sie nicht).

{% enddetails %}

## Canvas-Details

Nach dem Start eines Canvas können Sie die folgenden Einstellungen und Details bearbeiten:

* Name und Beschreibung der Leinwand
* Teams und Tags
* Entry-Typ, Zeitplan und Kontrollen
* Abo-Status
* Rate-Limiting
* Frequency-Capping
* Ruhezeiten
* Zielgruppen

Nachdem ein Canvas gestartet wurde:

- Konvertierungsereignisse können nicht bearbeitet werden. 
- Die folgenden Schritte können nicht hinzugefügt oder entfernt werden, und die Reihenfolge kann nicht geändert werden, um die Rangfolge anzupassen: [Zielgruppenpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) und [Experimentpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Workaround 1:** Erstellen Sie einen neuen Zielgruppen-Pfad, Aktions-Pfad oder Experiment-Pfad und konfigurieren Sie die Pfade zu diesem neuen Schritt neu.
  - **Workaround 2:** Duplizieren Sie das Canvas, um Ihre Bearbeitungen vorzunehmen.

### Einzelne Schritte

Für einzelne Canvas-Schritte können Sie nach dem Start die folgenden Details bearbeiten:

* Name
* Nachrichteninhalt
* Trigger
* Zielgruppe
* Ausnahme-Events
* Verzögerungen (nur für Verzögerungsschritte)

Der Zeitplantyp und die Kontrollprozentsätze des Schritts können jedoch nach dem Start nicht mehr bearbeitet werden. Für die Schritte „Aktions-Pfade“ und „Zielgruppen-Pfade“ können die Ranglisten und Bewertungsfenster nach dem Start nicht mehr bearbeitet werden.

### Prozentuale Anteile der Leinwandvariante

Nach dem Start eines Canvas können Sie nur die Prozentzahlen der Kontrollvariante verringern. Wenn ein Variantenprozentsatz in Canvas geändert wird, werden Sie feststellen, dass Ihre Benutzer möglicherweise auf andere Varianten umverteilt werden.

Diesen Nutzern wird zunächst zufällig eine bestimmte Variante zugewiesen, bevor sie zum ersten Mal eine Kampagne erhalten. Von diesem Zeitpunkt an wird den Nutzer:innen bei jedem weiteren Aufruf der Kampagne (oder bei jedem erneuten Aufruf einer Canvas-Variante) dieselbe Variante angezeigt, sofern die Variantenanteile nicht geändert werden.

Wenn sich die Prozentsätze der Varianten ändern, werden die Nutzer:innen möglicherweise auf andere Varianten umverteilt. Nutzer:innen bleiben in diesen Varianten, bis die Prozentsätze wieder geändert werden. Beachten Sie, dass Nutzer:innen bei Canvase, die Verzweigungen mit `NOT`-Filtern mit zufälligen Bucket-Nummern verwenden, möglicherweise nicht jedes Mal dieselbe Verzweigung erhalten, wenn sie das Canvas erneut betreten.

#### Kontrollgruppen

Kontrollgruppen bleiben konsistent, wenn der Prozentsatz der Varianten unverändert bleibt. Wenn der Prozentsatz einer Kontrollgruppe verringert oder erhöht wird, können Benutzer, die zuvor Nachrichten erhalten haben, bei einem späteren Versand nicht mehr in die Kontrollgruppe aufgenommen werden, und kein Benutzer in der Kontrollgruppe würde jemals eine Nachricht erhalten.

### Lokale Sendezeit

Canvases, deren Veröffentlichung zu einer lokalen Sendezeit im Zeitplan vorgesehen ist, können bis zu 24 Stunden vor der geplanten Sendezeit bearbeitet werden. Dieses Fenster wird die „sichere Zone“ genannt. 

{% alert tip %}
Wenn Sie größere Änderungen vornehmen wollen, die zu einer völlig neuen Canvas-Kopie führen, denken Sie daran, die Nutzer:innen auszuschließen, die das erste Canvas erhalten haben, und den Zeitplan für das Canvas neu anzupassen, um das Senden von Zeitzonen zu ermöglichen.
{% endalert %}

Wenn ein Zeitplan für Eingänge so eingestellt ist, dass Nutzer:innen sofort nach dem Start eingegeben werden, startet Canvas zum nächstgelegenen Zeitpunkt in Schritten von 5 Minuten. Wenn Sie beispielsweise ein Canvas mit einem Update aktualisieren, um Nutzer:innen um 8:31 Uhr PST sofort einzutragen, wird die Startzeit auf 8:30 Uhr PST und die Zeitzone des Unternehmens festgelegt.

### Löschen von Varianten

Wenn Varianten aus einem Canvas gelöscht werden, geschieht Folgendes:

- Schritte innerhalb der Variante (einschließlich derjenigen, die von anderen Varianten gemeinsam genutzt werden) werden gelöscht. 
- Die Stufen-Analytics und die Top-Level-Analytics für Canvas, wie beispielsweise _Gesamtzahl der Eingänge_, _Gesamtzahl der Austritte_ und _Konversionsrate_, werden gelöscht.
- Benutzer in gelöschten Varianten werden aus den Schritten ausgeschlossen, und alle folgenden Nachrichten werden nicht gesendet.

### Eigenschaften der Leinwandeinträge

Die Eigenschaften von Canvas-Einträgen werden beim Senden nicht in Steps eingebettet. Dies bedeutet, dass bei einer Änderung der Eingangs-Eigenschaften des Canvases nach dem Start des Canvases diese Änderungen nur für neue Nutzer:innen gelten, die den Canvas betreten. Wenn Ihr Canvas dem Betreten des Canvas durch Nutzer:innen erlaubt, werden alle Nutzer:innen, die erneut eintreten, anhand der aktualisierten Eingangs-Eigenschaften des Canvas ermittelt.

## Bewährte Praktiken

Sehen Sie sich diese bewährten Verfahren an, die Sie beachten sollten, wenn Sie Ihr Canvas bearbeiten oder ergänzen, nachdem es gestartet wurde.

{% alert important %}
Im Allgemeinen sollten Sie Änderungen vermeiden, während Canvas aktiv ist und Nutzer:innen in die Warteschlange stellt.
{% endalert %}

### Getrennte Schritte

Sie können Ihr Canvas mit getrennten Schritten starten und diese Canvases auch nach dem Start speichern. Bevor Sie einen Schritt von Ihrem Workflow abkoppeln, empfehlen wir Ihnen, die Analytics-Ansicht der Schritte für Nutzer:innen in Bearbeitung zu überprüfen.

Nehmen wir an, ein:e Nutzer:in befindet sich in einem nicht angeschlossenen Schritt Ihres Canvas-Workflows. Diese Nutzer:in bringt sich zum nächsten Schritt voran, sofern es einen gibt. Die Einstellungen des Schritts legen fest, wie der Nutzer:in voranbringen soll. 

Indem Sie nicht verbundene Schritte erstellen oder bearbeiten, können Sie Änderungen an diesen unabhängigen Schritten vornehmen, ohne sie direkt mit dem Rest Ihres Canvas verbinden zu müssen. Dies unterstützt Sie dabei, Ihre Schritte zu überprüfen, bevor Sie Canvas erneut starten. 

### Experiment Pfad Schritt

Wenn Ihr Canvas ein aktives oder laufendes Experiment „Winning Path“ oder „Personalized Path“ enthält und Sie den aktiven Canvas aktualisieren (unabhängig davon, ob Sie den Schritt „Experiment-Pfad“ selbst aktualisieren), wird das laufende Experiment beendet, und der Experiment-Pfad-Schritt ermittelt keinen Gewinnerpfad und keine personalisierten Pfade. Um das Experiment neu zu starten, können Sie den bestehenden Experiment-Pfad trennen und einen neuen starten, oder Sie duplizieren das Canvas und starten ein neues Canvas. Andernfalls durchlaufen die Nutzer:innen den Experiment-Pfad, als ob keine Optimierungsmethode ausgewählt worden wäre.

### Zeitverzögerungen

Das Bearbeiten von Canvases mit Zeitverzögerungen kann etwas kompliziert sein. Beachten Sie daher bitte die folgenden Details, wenn Sie Änderungen an Ihren Canvases vornehmen:

- Wenn Sie die Verzögerung in einem Verzögerungsschritt aktualisieren, erhalten nur neue Nutzer:innen, die den Canvas betreten, und Nutzer:innen, die nicht für diesen Schritt in die Warteschlange gestellt wurden, die Nachricht zum aktualisierten Zeitpunkt.
- Wenn Sie einen Schritt mit einer Zeitverzögerung (z. B. „Verzögerung“ oder „Aktions-Pfade“) löschen und beschließen, diese Nutzer:innen in einen anderen Canvas-Schritt umzuleiten, werden die Nutzer:innen erst nach Ablauf der Zeitverzögerung des Schritts umgeleitet. Nehmen wir beispielsweise an, Sie löschen einen Verzögerungsschritt mit einer Verzögerung von einem Tag und leiten diese Nutzer:innen zu einem Schritt mit Nachrichten weiter. In diesem Fall werden die Nutzer:innen erst nach Ablauf der eintägigen Verzögerung weitergeleitet.
- Wenn Ihr Canvas über einen oder mehrere Experiment-Pfad-Schritte verfügt, könnte das Löschen von Schritten die Ergebnisse dieses Schrittes ungültig machen.

### Leinwände stoppen

Das Anhalten eines Canvas beendet nicht die Sitzung der Nutzer:innen, die in einem Schritt warten. Wenn Sie die Leinwand wieder aktivieren und die Nutzer:innen weiterhin warten, schließen sie den Schritt ab und fahren mit dem nächsten Schritt fort. Sollte jedoch die Zeit, in der der Nutzer:in zum nächsten Schritt hätte übergehen sollen, bereits verstrichen sein, verlässt er stattdessen die Canvas. 

Nehmen wir beispielsweise an, Sie haben einen Canvas erstellt, der mit dem Canvas Flow-Workflow erstellt wurde und um 14 Uhr mit einer Variante mit zwei Schritten gestartet werden soll: einem Verzögerungsschritt mit einer einstündigen Verzögerung, der in einen Schritt mit einer Nachricht übergeht. 

Ein:e Nutzer:in öffnet dieses Canvas um 14:01 Uhr und öffnet gleichzeitig den Schritt „Delay“. Dies bedeutet, dass der Nutzer:in um 15:01 Uhr zum nächsten Schritt der User Journey (dem Schritt „Nachricht“) im Zeitplan übergehen soll. Wenn Sie Canvas um 14:30 Uhr beenden und um 15:30 Uhr wieder aktivieren, wird die Nutzer:in aus Canvas ausgeloggt, da es bereits nach 15:01 Uhr ist. Wenn Sie die Canvas jedoch um 14:40 Uhr wieder aktivieren, geht die Nutzer:in wie erwartet um 15:01 Uhr zum Schritt „Nachricht“ über.

## Was Sie wissen sollten

Die folgenden häufig auftretenden Probleme können durch das Bearbeiten oder Hinzufügen weiterer Komponenten zu einer anderen Komponente in einem Canvas nach dem Start getriggert werden. 

{% alert important %}
Die folgenden Probleme können vermieden werden. Sollten Sie nach dem Start eines Canvas Änderungen vornehmen müssen, empfehlen wir Ihnen, zunächst sicherzustellen, dass alle Nutzer:innen, die das Canvas bereits betreten haben, ihre Benutzerreise abgeschlossen haben. Darüber hinaus empfehlen wir, Schritte, die bereits von mindestens einer Nutzer:in bearbeitet wurden, nicht zu löschen.
{% endalert %}

- Fehlende Berichtsdaten (wenn Nachrichten-Varianten gelöscht und erneut hinzugefügt werden)
- Die Nutzer:innen folgen nicht dem erwarteten Pfad.
- Nachrichten werden zu unerwarteten Zeitpunkten versendet.
- Die Änderungen überschreiben die Currents-Daten nicht, daher können Abweichungen zwischen den Canvas-Schritten auftreten (z. B. solche,`canvas_step_ids`die aufgrund einer Löschung nicht in Canvas vorhanden sind).
- Nutzer:innen können dieselbe Nachricht zweimal erhalten.
- Nutzer:innen erhalten aufgrund der bestehenden Rate-Limits keine Nachrichten.
  - Wenn Sie das Rate-Limit für ein aktives Canvas aktualisieren, gilt das neue Rate-Limit für alle zukünftigen Nachrichtenversendungen, einschließlich der Nutzer:innen, die sich bereits im Canvas befinden. Aufgrund interner Zwischenspeicherung (bis zu 30 Sekunden) kann es jedoch zu einer kurzen Verzögerung kommen, bevor die neuen Rate-Limits vollständig angewendet werden. Bitte beachten Sie, dass Braze die Nutzer:innen für den Schritt „Nachricht“ in die Warteschlange stellt, in dem sie sich gerade befinden, sodass das beim tatsächlichen Versand der Nachricht für jeden Schritt geltende Rate-Limit angewendet wird.
- Wenn ein Canvas [automatisch beendet]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#available-statuses) wird, werden auch die Entwürfe des Canvas nach dem Start gelöscht.

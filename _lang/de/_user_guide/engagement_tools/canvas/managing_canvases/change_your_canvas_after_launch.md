---
nav_title: Bearbeiten von Leinwänden nach dem Start
article_title: Bearbeiten von Leinwänden nach dem Start
page_order: 0
description: "Dieser Referenzartikel befasst sich mit den verschiedenen Aspekten eines Canvas, die nach dem ersten Start geändert werden können."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Bearbeiten von Leinwänden nach dem Start

> In diesem Referenzartikel erfahren Sie, was in einem Canvas nach dem ersten Start geändert werden kann.

Sie können Ihre Canvase nach dem Start bearbeiten, indem Sie:

* Einfügen neuer Canvas-Schritte in die User Journey
* Hinzufügen neuer Varianten und Verbindungen
* Anpassen der Variantenverteilung
* Anhalten oder Fortsetzen aller Canvas-Schritte

{% alert note %}
Die Verteilung der Kontrollvariante kann erst nach dem Start verringert werden.
{% endalert %}

Beachten Sie die folgenden zulässigen Bearbeitungen des Canvas nach dem Start, je nachdem, mit welchem Workflow Ihr Canvas erstellt wurde. Wenn Ihr Canvas den Original-Canvas-Workflow verwendet, müssen Sie zuerst zu Canvas Flow klonen, um nachträgliche Bearbeitungen vornehmen zu können.

Sie können in Ihrer User Journey alle folgenden Einträge löschen:

- [Canvas-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Leinwand-Varianten 
- Verbindungen zwischen Canvas-Schritten

Wenn Sie Ihre Canvas-Nutzer:innen bearbeiten oder weitere Schritte hinzufügen möchten, gelten die folgenden Angaben:

- Benutzer, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt. 
- Wenn Ihre Einstellungen für den Canvas-Eingang es Nutzern:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte bestanden haben, zum erneuten Eintritt berechtigt.
- Benutzer, die sich derzeit in einem gestarteten Canvas befinden, aber noch nicht die Punkte der User Journey erreicht haben, an denen neue Schritte hinzugefügt werden, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten. 

Wenn Sie einen [Delay-]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) oder [Action Paths-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) löschen, können Sie die Benutzer, die derzeit in diesem Schritt warten, optional in einen anderen Canvas-Schritt umleiten. Bei Verzögerungen bleiben die Nutzer:innen bis zum Ende der Verzögerungszeit im Schritt. Bei Aktionspfaden bleiben die Benutzer bis zum Ende des Bewertungsfensters in dem Schritt.

Beachten Sie, dass Braze beim ersten Start eines Canvas die Benutzer in die Warteschlange des Nachrichtenschritts einreiht, in dem sie sich gerade befinden, und nicht in alle nachfolgenden Nachrichten im Canvas. Wenn Sie den Canvas nach dem Start bearbeiten, sind einige Benutzer bereits in der Warteschlange und können die Änderungen nicht übernehmen. Wenn Sie den Canvas anhalten, ihn duplizieren, dann ändern und diese neue Version starten, wird der Canvas alle Nutzer:innen erneut bewerten, nicht nur die Nutzer:innen, die noch nicht in die Warteschlange aufgenommen wurden.

Siehe den Abschnitt [Bewährte Verfahren](#best-practices) für spezifische Anwendungsfälle bei der Bearbeitung. Generell ist es ratsam, die Bearbeitung von Live-Canvase zu vermeiden, da es zu unerwartetem Verhalten kommen kann.

{% details Expand for original Canvas editor details %}

Sie können bestehende Verbindungen weder bearbeiten noch löschen, und Sie können keinen Schritt zwischen bestehende verbundene Schritte einfügen. Wenn Sie Ihre Canvas-Nutzer:innen bearbeiten oder weitere Schritte hinzufügen möchten, gelten die folgenden Angaben:

- Benutzer, die den Canvas noch nicht betreten haben, sind für alle neu erstellten Schritte berechtigt. 
- Wenn Ihre Einstellungen für den Canvas-Eingang es Nutzern:innen erlauben, Schritte erneut zu betreten, sind Nutzer:innen, die bereits neu erstellte Schritte bestanden haben, zum erneuten Eintritt berechtigt.
- Nutzer:innen, die sich derzeit in einem gestarteten Canvas befinden, aber noch nicht die neu hinzugefügten Schritte in der User Journey erreicht haben, sind berechtigt, diese neu hinzugefügten Schritte zu erhalten.
- Wenn ein Verzögerungsschritt der letzte Schritt im Canvas ist, werden Benutzer, die diesen Schritt erreichen, automatisch aus dem Canvas befördert und erhalten keine neu erstellten Schritte mehr.

{% alert important %}
Wenn Sie die Einstellungen für **Verzögerung** oder **Fenster** für einen Canvas-Schritt aktualisieren, bleiben die Nutzer:innen, die sich zum Zeitpunkt der Aktualisierung in diesem Schritt befinden, bei der Verzögerungszeit, die ihnen beim ursprünglichen Eintritt in den Schritt zugewiesen wurde. Nur neue Nutzer:innen, die den Canvas betreten, und solche, die noch nicht in die Warteschlange für diesen Schritt aufgenommen wurden, erhalten die Nachricht zum aktualisierten Zeitpunkt.
{% endalert %}

Nutzer:innen, die auf den Empfang einer Nachricht warten, werden durch das Beenden eines Canvas nicht verlassen. Wenn Sie die Leinwand wieder aktivieren und die Benutzer immer noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem sie die Nachricht hätten erhalten sollen, ist bereits verstrichen, dann erhalten sie sie nicht).

{% enddetails %}

## Canvas-Details

Sie können die folgenden Canvas-Einstellungen und Informationen bearbeiten, nachdem ein Canvas gestartet wurde:

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
* Verspätungen (nur für Verzögerungsschritte)

Der Zeitplantyp und die Kontrollprozentsätze des Schritts können jedoch nach dem Start nicht mehr bearbeitet werden. Bei den Schritten Aktionspfade und Publikumspfade sind die Ranglisten und Bewertungsfenster nach dem Start nicht mehr bearbeitbar.

### Prozentuale Anteile der Leinwandvariante

Nach dem Start eines Canvas können Sie nur die Prozentzahlen der Kontrollvariante verringern. Wenn ein Variantenprozentsatz in Canvas geändert wird, werden Sie feststellen, dass Ihre Benutzer möglicherweise auf andere Varianten umverteilt werden.

Diesen Nutzern wird zunächst zufällig eine bestimmte Variante zugewiesen, bevor sie zum ersten Mal eine Kampagne erhalten. Von da an erhalten Sie bei jedem weiteren Empfang der Kampagne (oder wenn der Benutzer eine Canvas-Variante erneut aufruft) dieselbe Variante, es sei denn, die Variantenprozentsätze werden geändert.

Wenn sich die Prozentsätze der Varianten ändern, werden die Nutzer:innen möglicherweise auf andere Varianten umverteilt. Die Benutzer bleiben in diesen Varianten, bis die Prozentsätze erneut geändert werden. Beachten Sie, dass Nutzer:innen bei Canvase, die Verzweigungen mit `NOT`-Filtern mit zufälligen Bucket-Nummern verwenden, möglicherweise nicht jedes Mal dieselbe Verzweigung erhalten, wenn sie das Canvas erneut betreten.

#### Kontrollgruppen

Kontrollgruppen bleiben konsistent, wenn der Prozentsatz der Varianten unverändert bleibt. Wenn der Prozentsatz einer Kontrollgruppe verringert oder erhöht wird, können Benutzer, die zuvor Nachrichten erhalten haben, bei einem späteren Versand nicht mehr in die Kontrollgruppe aufgenommen werden, und kein Benutzer in der Kontrollgruppe würde jemals eine Nachricht erhalten.

### Lokale Sendezeit

Canvase, die für den Start zu einer Ortszeit geplant sind, können bis zu 24 Stunden vor der geplanten Sendezeit bearbeitet werden. Dieses Fenster wird die „sichere Zone“ genannt. 

{% alert tip %}
Wenn Sie größere Änderungen vornehmen wollen, die zu einer völlig neuen Canvas-Kopie führen, denken Sie daran, die Nutzer:innen auszuschließen, die das erste Canvas erhalten haben, und den Zeitplan für das Canvas neu anzupassen, um das Senden von Zeitzonen zu ermöglichen.
{% endalert %}

### Löschen von Varianten

Wenn Varianten aus einem Canvas gelöscht werden, geschieht Folgendes:

- Die Schritte innerhalb der Variante (einschließlich derer, die von anderen Varianten gemeinsam genutzt werden) werden gelöscht. 
- Die Schrittanalysen und die Top-Level-Analysen für den Canvas, wie z.B. _Gesamteingänge_, _Gesamtausgänge_ und _Konversionsrate_, werden gelöscht.
- Benutzer in gelöschten Varianten werden aus den Schritten ausgeschlossen, und alle folgenden Nachrichten werden nicht gesendet.

### Eigenschaften der Leinwandeinträge

Die Eigenschaften von Canvas-Einträgen werden beim Senden nicht in Steps eingebettet. Das bedeutet, wenn die Eigenschaften eines Canvas-Eintrags bearbeitet werden, nachdem ein Canvas gestartet wurde, gelten diese Änderungen nur für neue Benutzer, die das Canvas betreten. Wenn Ihr Canvas es zulässt, dass Benutzer den Canvas erneut betreten, werden alle Benutzer, die den Canvas erneut betreten, durch die aktualisierten Eigenschaften des Canvas-Eintrags bestimmt.

## Bewährte Praktiken

Sehen Sie sich diese bewährten Verfahren an, die Sie beachten sollten, wenn Sie Ihr Canvas bearbeiten oder ergänzen, nachdem es gestartet wurde.

{% alert important %}
Vermeiden Sie es im Allgemeinen, Änderungen vorzunehmen, während der Canvas aktiv ist und Nutzer:innen in der Warteschlange stehen.
{% endalert %}

### Getrennte Schritte

Sie können Ihr Canvas mit getrennten Schritten starten und diese Canvases auch nach dem Start speichern. Bevor Sie einen Schritt von Ihrem Workflow abkoppeln, empfehlen wir Ihnen, die Analytics-Ansicht der Schritte für Nutzer:innen in Bearbeitung zu überprüfen.

Nehmen wir an, ein:e Nutzer:in befindet sich in einem nicht angeschlossenen Schritt Ihres Canvas-Workflows. Dieser Benutzer wird zum nächsten Schritt weitergehen, falls es einen gibt. Die Einstellungen des Schritts geben vor, wie der Benutzer vorgehen soll. 

Indem Sie nicht verbundene Schritte erstellen oder bearbeiten, können Sie Änderungen an diesen unabhängigen Schritten vornehmen, ohne sie direkt mit dem Rest Ihres Canvas verbinden zu müssen. Auf diese Weise können Sie Ihre Schritte testen, bevor Sie Ihren Canvas erneut starten. 

### Experiment Pfad Schritt

Wenn Ihr Canvas ein aktives oder laufendes Winning Path- oder Personalized Path-Experiment enthält und Sie das aktive Canvas aktualisieren, wird das laufende Experiment beendet, unabhängig davon, ob Sie den Experiment-Pfad-Schritt selbst aktualisieren, und der Experiment-Schritt wird keinen Winning Path oder personalisierte Pfade ermitteln. Um das Experiment neu zu starten, können Sie den bestehenden Experiment-Pfad trennen und einen neuen starten, oder Sie duplizieren das Canvas und starten ein neues Canvas. Andernfalls durchlaufen die Nutzer:innen den Experiment-Pfad, als ob keine Optimierungsmethode ausgewählt worden wäre.

### Zeitverzögerungen

Die Bearbeitung von Leinwänden mit Zeitverzögerungen kann ein wenig knifflig sein! Beachten Sie also die folgenden Details, wenn Sie Ihre Canvases bearbeiten.

Wenn Sie die Verzögerung in einem Verzögerungsschritt aktualisieren, erhalten nur neue Benutzer, die den Canvas betreten, und Benutzer, die nicht für diesen Schritt in die Warteschlange gestellt wurden, die Nachricht mit der aktualisierten Verzögerung.

Wenn Sie einen Schritt mit einer Zeitverzögerung (z. B. Verzögerung oder Aktionspfade) löschen und beschließen, diese Benutzer in einen anderen Canvas-Schritt umzuleiten, werden die Benutzer erst umgeleitet, wenn die Zeitverzögerung des Schritts abgelaufen ist. Nehmen wir an, Sie löschen einen Verzögerungsschritt mit einer eintägigen Verzögerung und leiten diese Nutzer:innen auf einen Schritt für Nachrichten um. In diesem Fall werden die Nutzer:innen erst dann weitergeleitet, wenn die eintägige Frist abgelaufen ist.

Wenn Ihr Canvas über einen oder mehrere Experiment-Pfad-Schritte verfügt, könnte das Löschen von Schritten die Ergebnisse dieses Schrittes ungültig machen.

### Leinwände stoppen

Das Beenden eines Canvas führt nicht dazu, dass Nutzer:innen, die in einem Schritt warten, beendet werden. Wenn Sie die Leinwand wieder aktivieren und die Benutzer immer noch warten, werden sie den Schritt abschließen und zum nächsten Schritt übergehen. Wenn jedoch die Zeit, in der der Nutzer:innen zum nächsten Schritt hätte übergehen sollen, abgelaufen ist, verlässt er stattdessen den Canvas. 

Nehmen wir an, Sie haben ein Canvas, das mit dem Canvas-Flow-Workflow erstellt wurde und um 14 Uhr starten soll, mit einer Variante mit zwei Schritten: einem Verzögerungsschritt mit einer einstündigen Verzögerung, der in einen Nachrichten-Schritt übergeht. 

Ein:e Nutzer:in öffnet dieses Canvas um 14:01 Uhr und öffnet gleichzeitig den Schritt „Delay“. Das bedeutet, dass der Nutzer:innen für den nächsten Schritt der User Journey (den Schritt Nachricht) um 15:01 Uhr eingeplant wird. Wenn Sie den Canvas um 14:30 Uhr anhalten und um 15:30 Uhr wieder aktivieren, wird der Nutzer:innen den Canvas verlassen, da es nach 15:01 Uhr ist. Wenn Sie jedoch das Canvas um 14:40 Uhr wieder aktivieren, wird der oder die Nutzer:in wie erwartet um 15:01 Uhr zum Schritt „Nachricht“ übergehen.

## Was Sie wissen sollten

Die folgenden häufigen Probleme können durch das Bearbeiten oder Hinzufügen weiterer Komponenten zu einer anderen Komponente in einem Canvas nach dem Start ausgelöst werden. 

{% alert important %}
Die folgenden Probleme sind vermeidbar. Wenn Sie Änderungen an einem Canvas vornehmen müssen, nachdem dieser gestartet wurde, empfehlen wir Ihnen, sich zunächst zu vergewissern, dass alle Nutzer:innen, die den Canvas bereits betreten haben, ihre Nutzer:innenreise abgeschlossen haben. Außerdem empfehlen wir Ihnen, keine Schritte zu löschen, die bereits mindestens einen Nutzer:innen bearbeitet haben.
{% endalert %}

- Fehlende Berichtsdaten (wenn Varianten von Nachrichten gelöscht und wieder hinzugefügt werden)
- Nutzer:innen folgen nicht dem erwarteten Pfad
- Nachrichten werden zu unerwarteten Zeiten gesendet
- Die Bearbeitungen überschreiben die Currents-Daten nicht, so dass Sie möglicherweise Diskrepanzen zwischen den Canvas-Schritten feststellen (z. B. `canvas_step_ids`, die aufgrund einer Löschung nicht im Canvas vorhanden sind).
- Nutzer:innen können die gleiche Nachricht zweimal erhalten
- Nutzer:innen können aufgrund des bestehenden Rate-Limits keine Nachrichten mehr empfangen
  - Wenn Nutzer:innen in ein Canvas entsandt werden, wird das Rate-Limits, das für das Canvas gilt, wenn ein Nutzer:in entsandt wird, auf den Nutzer:innen angewendet. Nachdem das Canvas versendet wurde, kann das Rate-Limit für diesen Nutzer nicht mehr bearbeitet werden. Eine Erhöhung oder Verringerung des Rate-Limits nach dem Start hat also keine Auswirkungen auf Nutzer:innen, die bereits versendet wurden.
---
nav_title: Experimentpfade
article_title: Experimentpfade 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Dieser Artikel befasst sich mit Experiment Paths, einer Komponente, mit der Sie mehrere Canvas-Pfade gegeneinander und eine Kontrollgruppe an jedem beliebigen Punkt der User Journey testen können."
tool: Canvas
---

# Experimentpfade

> Mit Experimentpfaden können Sie mehrere Canvas-Pfade gegeneinander und gegen eine Kontrollgruppe an einem beliebigen Punkt in der Nutzer-Journey testen. Mit dieser Komponente können Sie die Performance des Pfads verfolgen, um fundierte Entscheidungen über Ihre Canvas-Journey zu treffen.

Wenn Sie einen Experimentpfad-Schritt in Ihre User Journey einfügen, werden die Nutzer:innen nach dem Zufallsprinzip verschiedenen Pfaden (oder einer optionalen Kontrollgruppe) zugewiesen, die Sie erstellen. Teile des Publikums werden je nach den von Ihnen gewählten Prozentsätzen verschiedenen Pfaden zugewiesen, so dass Sie verschiedene Botschaften oder Pfade gegeneinander testen und feststellen können, welcher am effektivsten ist. 

![Ein Experiment-Pfad-Schritt, der sich in Pfad 1, Pfad 2 und Kontrolle aufteilt.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Anwendungsfälle

Experimentpfade eignen sich am besten für das Testen von Zustellung, Kadenz, Kopie der Nachrichten und Kombinationen von Kanälen.

- **Lieferung:** Vergleichen Sie die Ergebnisse zwischen Nachrichten, die mit unterschiedlichen [Zeitverzögerungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) gesendet wurden, basierend auf Benutzeraktionen[(Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)) und unter Verwendung von [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas).<br><br>
- **Kadenz:** Testen Sie mehrere Nachrichtenflüsse über einen bestimmten Zeitraum. Sie könnten zum Beispiel zwei verschiedene Onboarding-Kadenzen testen:
    - Kadenz 1: Senden Sie 2 Nachrichten in den ersten 2 Wochen des Nutzers oder der Nutzerin
    - Kadenz 2: Senden Sie 3 Nachrichten in den ersten 2 Wochen des Nutzers oder der Nutzerin
    
    Beim Targeting von passiven Nutzer:innen können Sie testen, wie effektiv es ist, innerhalb einer Woche zwei Nachrichten zur Rückgewinnung zu versenden, anstatt nur eine.
- **Nachrichtenkopie:** Ähnlich wie bei einem [Standard-A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) können Sie verschiedene Nachrichtentexte testen, um zu sehen, welche Formulierung zu einer höheren Konversionsrate führt.<br><br>
- **Kanal-Kombinationen:** Testen Sie die Wirksamkeit verschiedener Kombinationen von Nachrichtenkanälen. Sie können zum Beispiel die Wirkung einer reinen E-Mail mit der einer E-Mail in Kombination mit einer Push-Mitteilung vergleichen.

## Voraussetzung

Um Experimentierpfade zu verwenden, muss Ihr Canvas Umwandlungsereignisse enthalten. Sie können zwar keine Konversions-Events hinzufügen, nachdem ein Canvas gestartet wurde, aber Sie können das gestartete Canvas klonen und Konversions-Events hinzufügen, um Experimentpfade hinzuzufügen.

## Erstellen eines Experiment-Pfads

Um eine Experimentpfade-Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente aus der Seitenleiste oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand eines Schritts und wählen Sie **Experimentierpfade**. 

In der Standardkonfiguration dieser Komponente gibt es zwei Standardpfade, **Pfad 1** und **Pfad 2**, wobei 50 % der Zielgruppe über jeden Pfad gesendet werden. Klicken Sie auf die Komponente, um das Fenster **Experimentiereinstellungen** zu öffnen. Dort sehen Sie die Konfigurationsoptionen für die Komponente.

### Schritt 1: Anzahl der Pfade und die Verteilung der Zielgruppe wählen

Sie können bis zu vier Pfade hinzufügen, indem Sie auf **Pfad hinzufügen** klicken, und eine optionale Kontrollgruppe, indem Sie **Kontrollgruppe hinzufügen** markieren. Mit Hilfe der Prozentfelder für jeden Pfad können Sie den Prozentsatz der Zielgruppe angeben, der auf jeden Pfad und die Kontrollgruppe entfallen soll. Die angegebenen Prozentsätze müssen in der Summe 100% ergeben, damit Sie fortfahren können. Wenn Sie schnell alle verfügbaren Pfade (und die Kontrolle) auf denselben Prozentsatz setzen möchten, klicken Sie auf **Pfade gleichmäßig verteilen**.

Sie können auch wählen, ob die Benutzer in der Kontrollgruppe den Canvas weiter durchlaufen oder nach dem Conversion-Tracking-Fenster für das **Verhalten der Kontrollgruppe** verlassen sollen. Optional können Sie eine Beschreibung hinzufügen, um anderen zu erklären, was mit diesem Experimentpfad getestet werden soll, oder um zusätzliche Informationen zu notieren, die hilfreich sein könnten.

![Experiment-Einstellungen, wo Sie Pfade hinzufügen und den Prozentsatz der Nutzer:innen in jedem Pfad verteilen können.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Wenn die erneute Qualifizierung für den Canvas wieder aktiviert ist, werden Nutzer:innen, die den Canvas aufrufen und einen zufällig gewählten Pfad durchlaufen, denselben Pfad erneut durchlaufen, wenn sie wieder teilnahmeberechtigt werden und den Canvas erneut aufrufen. Dadurch bleibt die Gültigkeit des Experiments und der damit verbundenen Analysen erhalten. Wenn Sie möchten, dass der Schritt immer eine zufällige Pfadzuweisung vornimmt, wählen Sie **Zufällige Pfade in Experimentpfade**. Diese Option ist nicht verfügbar, wenn Sie entweder den Gewinnerpfad oder personalisierte Pfade verwenden.
{% endalert %}

### Schritt 2: Aktivieren Sie den Siegerpfad oder die personalisierten Pfade (optional). {#step-2}

Sie können Ihr Experiment optimieren, indem Sie den [Gewinnerpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) oder die [personalisierten Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths) aktivieren. Beide Optionen funktionieren, indem Sie Ihre Pfade zunächst mit einem Teil Ihrer Zielgruppe testen. Nach dem Ende des Experiments werden die verbleibenden und nachfolgenden Benutzer entweder auf den insgesamt besten Pfad (Winning Path) oder den besten Pfad für jeden Benutzer (Personalized Paths) geschickt.

### Schritt 3: Pfade erstellen

Und schließlich müssen Sie Ihre nachgelagerten Pfade erstellen. Wählen Sie **Fertig** und kehren Sie zum Canvas-Builder zurück. Klicken Sie auf den <i class="fas fa-plus-circle"></i> Plus-Button unter jedem Pfad, um mit der Erstellung von Journeys zu beginnen und die üblichen Canvas-Tools nach Belieben zu verwenden.

![Hinzufügen von Schritten zu jedem Pfad, der sich von einer Experiment-Pfad-Komponente abspaltet.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Denken Sie daran, dass Pfade und ihre nachgelagerten Schritte nicht mehr aus einem Canvas entfernt werden können, nachdem sie erstellt wurden. Nach dem Start können Sie jedoch die Verteilung der Zielgruppe auf die Pfade nach Belieben ändern. Wenn Sie beispielsweise einen Tag nach dem Start eines Canvas zu dem Schluss kommen, dass ein Pfad aufgrund der Analysen besser ist als die anderen, können Sie diesen Pfad auf 100 % und die anderen auf 0 % festlegen. Je nach Bedarf können Sie die Nutzer:innen auch weiterhin auf mehrere Pfade schicken.

{% alert important %}
Um eine Kontamination des Experiments zu verhindern, wird, wenn Ihr Canvas ein aktives oder laufendes Winning Path- oder Personalized Path-Experiment enthält und Sie das aktive Canvas aktualisieren, unabhängig davon, ob Sie den Experiment-Pfad-Schritt selbst aktualisieren, das laufende Experiment beendet und der Experiment-Pfad-Schritt wird keinen Winning Path oder personalisierte Pfade ermitteln. Um das Experiment neu zu starten, können Sie den bestehenden Experiment-Pfad trennen und einen neuen starten, oder Sie duplizieren das Canvas und starten ein neues Canvas. Andernfalls durchlaufen die Nutzer:innen den Experiment-Pfad, als ob keine Optimierungsmethode ausgewählt worden wäre. Sie können auch keine personalisierten Pfade oder Gewinnerpfade für eine bereits aktive Leinwand mit einem Experimentierpfadschritt aktivieren.<br><br>Weitere Informationen finden Sie unter [Bearbeiten von Leinwänden nach dem Start]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Leistung nachverfolgen

Wählen Sie auf der Seite **Canvas Analytics** den Experiment-Pfad aus, um eine [detaillierte Tabelle]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) zu öffnen, die mit dem Tab **Varianten analysieren** identisch ist, um detaillierte Performance- und Konversionsstatistiken über verschiedene Pfade hinweg zu vergleichen. Sie können die Tabelle auch als CSV-Datei exportieren und die prozentualen Änderungen für Metriken von Interesse im Verhältnis zu dem von Ihnen ausgewählten Pfad oder der Kontrolle vergleichen.

Jeder Schritt in jedem Pfad zeigt Statistiken in der [Canvas-Analytics-Ansicht]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) an, genau wie jeder andere Canvas-Schritt. Beachten Sie jedoch, dass die Analysen der einzelnen Schritte die Struktur des Experiments **nicht** berücksichtigen. Die Analysen im Schritt Experiment sollten zum Vergleich der verschiedenen Pfade verwendet werden.

### Performance des Gewinnerpfad und der personalisierten Pfade

Nutzen Sie die Vorteile von Winning Paths, um die Leistung über einen bestimmten Zeitraum zu verfolgen und die nachfolgenden Benutzer automatisch auf den Pfad mit der besten Leistung zu schicken. Weitere Informationen zur Analyse, wenn **Winning Path** oder **Personalized Paths** für Ihr Experiment aktiviert sind, finden Sie unter:

- [Gewinnerpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Personalisierte Pfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Zusätzliche Einstellungen

Die Experimentpfade zeichnen Nutzer:innen auf, die jeden Schritt aufrufen und während des zugewiesenen Pfads wechseln. Damit werden alle Konversions-Events verfolgt, die in der Canvas-Einrichtung angegeben sind. Geben Sie auf der Registerkarte **Zusätzliche Einstellungen** ein, wie viele Tage (zwischen 1 und 30) dieses Experiment die Konversionen verfolgen soll. Das Zeitfenster, das Sie hier angeben, bestimmt, wie lange Konversions-Events (die Sie in der Canvas-Einrichtung ausgewählt haben) für das Experiment verfolgt werden. Die in der Canvas-Einrichtung angegebenen Konvertierungsfenster pro Ereignis gelten nicht für die Nachverfolgung dieses Schritts und werden durch dieses Konvertierungsfenster ersetzt.


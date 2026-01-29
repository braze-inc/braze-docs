---
nav_title: Gewinnerpfad
article_title: Gewinnerpfad in Experimentpfaden 
page_type: reference
description: "Dieser Referenzartikel behandelt Winning Path, ein Feature, mit dem Sie Ihre A/B-Tests automatisieren können, wenn es für einen Experimentpfad-Schritt aktiviert ist."
tool: Canvas
---

# Gewinnerpfad in Experimentpfaden

> Winning Path ist ähnlich wie [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) in Kampagnen und ermöglicht Ihnen die Automatisierung Ihrer A/B-Tests.

Wenn der Winning Path in einem Experiment-Pfad-Schritt aktiviert ist, werden alle nachfolgenden Nutzer:innen nach einer bestimmten Zeitspanne auf den Pfad mit der höchsten Konversionsrate geleitet.

## Winning Path verwenden

### Schritt 1: Add an Experiment Path step

Fügen Sie einen [Experimentierpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) zu Ihrem Canvas hinzu und aktivieren Sie dann die Option **Gewinnpfad**.

![Einstellungen im Experimentierpfad mit dem Titel "Nachfolgende Benutzer auf den Gewinnerpfad verteilen". Der Abschnitt enthält einen Umschalter für den Winning-Pfad und Optionen zur Konfiguration des Konversions-Events und des Experiment-Fensters.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Schritt 2: Konfigurieren Sie die Einstellungen für den Gewinnweg

Geben Sie das Umwandlungsereignis an, das den Gewinner bestimmen soll. Wenn keine Konversions-Events verfügbar sind, kehren Sie zum ersten Schritt der Canvas-Einrichtung zurück und [weisen Konversions-Events zu]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Wenn Sie Öffnungen oder Klicks als Konversions-Event wählen, stellen Sie sicher, dass der erste Schritt im Pfad ein [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) ist. Braze zählt nur das Engagement ab dem ersten Schritt der Nachricht im jeweiligen Pfad. Wenn der Pfad mit einem anderen Schritt beginnt (wie z.B. einem Verzögerungs- oder Zielgruppen-Pfad-Schritt) und die Nachricht später kommt, wird diese Nachricht bei der Bewertung der Performance nicht berücksichtigt.

Legen Sie als nächstes das **Experimentierfenster** fest. Das **Experiment-Fenster** gibt an, wie lange das Experiment läuft, bevor der Gewinner-Pfad bestimmt wird und alle Nutzer:innen, die ihm folgen, diesen Pfad hinuntergeschickt werden. Das Fenster beginnt, wenn der erste Nutzer:innen den Schritt betritt.

![Gewinner-Pfad-Einstellungen mit dem ausgewählten Konversions-Event "Klicks" für ein 12-Stunden-Experimentierfenster.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Schritt 3: Fallback bestimmen {#statistical-significance}

Wenn die Ergebnisse des Tests nicht ausreichen, um einen statistisch signifikanten Gewinner zu ermitteln, werden standardmäßig alle zukünftigen Nutzer:innen auf den Pfad mit der besten Performance geschickt. Alternativ können Sie auch auswählen, **allen zukünftigen Nutzer:innen die Mischung der Pfade weiter zu senden**. Mit dieser Option werden zukünftige Nutzer:innen entsprechend der in der Experiment-Pfad-Verteilung angegebenen Prozentsätze auf die verschiedenen Pfade geschickt.

!["Allen zukünftigen Nutzern weiterhin den Pfadmix senden" ausgewählt, was mit den Nutzer:innen geschieht, wenn das Testergebnis statistisch nicht signifikant ist.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Eine Verzögerungsgruppe erscheint nur dann in Ihrer Pfadverteilung, wenn Ihr Canvas für eine einmalige Eingabe eingerichtet ist und Ihr Experiment-Schritt drei Pfade oder weniger hat. Wiederkehrende und getriggerte Canvase haben keine Verzögerungsgruppe, wenn Winning Path aktiviert ist.
{% endalert %}

### Schritt 4: Fügen Sie Ihre Pfade hinzu und starten Sie den Canvas

Eine einzelne Experimentpfad-Komponente kann bis zu vier Pfade enthalten. Wenn Ihr Canvas jedoch für [einen einmaligen Entry](#one-time-entry) eingerichtet ist, muss ein Pfad für die Verzögerungsgruppe reserviert werden, die Braze automatisch hinzufügt, wenn Winning Path aktiviert ist. Das bedeutet, dass Sie bei Canvase mit einmaligem Entry bis zu drei Pfade zu Ihrem Experiment hinzufügen können.

Richten Sie Ihr Canvas nach Bedarf ein und starten Sie es dann. Wenn der erste Nutzer:innen das Experiment betreten hat, können Sie im Canvas die Analytics sehen und [die Performance Ihres Experiments tracken.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

Nachdem ein Winning Path abgeschlossen ist, gehen alle nachfolgenden Nutzer:innen, die den Canvas betreten, den Winning Path durch, einschließlich der Nutzer:innen, die wieder eingestiegen sind und zuvor in der Kontrollgruppe des Experiment-Pfad-Schritts waren.

## Analytics {#analytics}

Wenn Winning Path aktiviert ist, wird Ihre Analytics-Ansicht in zwei Tabs unterteilt: **Erstes Experiment** und **Gewinnweg**.

- **Erstes Experiment:** Zeigt die Metriken für jeden Pfad während des Experimentierfensters an. Sie erhalten eine Zusammenfassung der Performance aller Pfade für die angegebenen Konversions-Events und können sehen, welcher Pfad als Sieger ausgewählt wurde.
- **Der Weg zum Sieg:** Zeigt nur die Metriken für den Siegerpfad ab dem Zeitpunkt an, an dem das Erste Experiment beendet wurde.

## Was Sie wissen sollten

### Einmaliger Entry {#one-time-entry}

Bei der Verwendung von Gewinnwegen in einem Canvas, bei dem Nutzer:innen nur eine einmalige Eingabe vornehmen dürfen, wird automatisch eine Verzögerungsgruppe eingefügt. Während der Dauer des Experiments wird ein bestimmter Prozentsatz der Nutzer:innen in der Verzögerungsgruppe gehalten, während die übrigen Nutzer:innen Ihre Experiment-Pfade betreten.

![Experimentierschritt mit einer Verzögerungsgruppe für den Siegerpfad]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Wenn der Test abgeschlossen und ein Siegerpfad ermittelt ist, werden die Nutzer:innen, die der Verzögerungsgruppe zugewiesen sind, auf den gewählten Pfad geleitet und fahren mit dem Canvas fort.

![Experiment-Pfad-Schritt mit einer Verzögerungsgruppe, die auf dem Siegerpfad gesendet wird]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Lieferung in Ortszeit

Wir raten davon ab, in Canvases with Winning Paths eine lokale Zeitangabe zu verwenden. Das liegt daran, dass die Experimentierfenster beginnen, wenn der erste Nutzer:innen durchläuft. Benutzer, die sich in sehr frühen Zeitzonen befinden, können den Schritt betreten und den Start des Experimentierfensters viel früher auslösen, als Sie erwarten. Das kann dazu führen, dass das Experiment beendet wird, bevor der Großteil Ihrer Benutzer in typischeren Zeitzonen genug Zeit hatte, das Canvas zu betreten oder zu konvertieren oder beides. 

Wenn Sie eine lokale Zustellung wünschen, sollten Sie ein Zeitfenster von 24-48 oder mehr Stunden einplanen. Auf diese Weise betreten Nutzer:innen in frühen Zeitzonen den Canvas und triggern den Start des Experiments, aber es bleibt noch genügend Zeit im Experimentierfenster. Nutzer:innen in späteren Zeitzonen haben noch genügend Zeit, um den Canvas und den Experiment-Schritt mit Gewinn-Pfaden zu betreten und möglicherweise umzuwandeln, bevor das Experiment-Fenster abläuft.

### Varianten basierend auf Klicks

Wenn Sie eine Winning Path Variante auf der Basis von Klicks einrichten, zählt jede Interaktion als Klick, es sei denn, sie wird von Braze als Abmeldeklick identifiziert.

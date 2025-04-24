---
nav_title: Personalisierte Pfade 
article_title: Personalisierte Pfade in Experimentpfaden 
page_type: reference
description: "Mit Personalized Paths können Sie jeden Punkt einer Canvas-Reise für einzelne Benutzer auf der Grundlage der Konversionswahrscheinlichkeit personalisieren."
tool: Canvas
---

# Personalisierte Pfade in Experimentpfaden

> Personalisierte Pfade sind ähnlich wie [personalisierte Varianten]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) in Kampagnen und ermöglichen es Ihnen, jeden Punkt einer Canvas-Reise für einzelne Benutzer auf der Grundlage der Konversionswahrscheinlichkeit zu personalisieren.

## So funktioniert Personalized Paths

Wenn personalisierte Pfade in einem Experimentpfad-Schritt aktiviert sind, ist das Verhalten leicht unterschiedlich, je nachdem, ob Ihr Canvas auf einmaliges oder wiederholtes Senden eingestellt ist:

- **Einmaliges Senden von Canvas:** Eine Gruppe von Benutzern wird in einer Verzögerungsgruppe zurückgehalten. Die verbleibenden Benutzer nehmen an einem ersten Test teil, um ein ähnliches Modell für eine von Ihnen festgelegte Dauer zu trainieren - mindestens 24 Stunden für beste Ergebnisse. Nach dem Test wird ein Modell erstellt, um herauszufinden, welches Nutzerverhalten mit einer höheren Wahrscheinlichkeit für eine Konvertierung auf einem bestimmten Pfad verbunden ist. Schließlich wird jede:r Nutzer:in in der Verzögerungsgruppe auf den Weg geschickt, der am wahrscheinlichsten zu einer Konversion führt, und zwar auf der Grundlage des Verhaltens, das er an den Tag legt, und dessen, was das Look-alike-Modell während des ersten Tests gelernt hat.
- **Wiederkehrende, durch Aktionen getriggerte und durch APIs getriggerte Canvase:** Ein erstes Experiment wird mit allen Nutzer:innen durchgeführt, die den Experimentpfad innerhalb eines bestimmten Zeitfensters betreten. Um die Integrität des Experiments aufrechtzuerhalten, werden Nutzer:in, die mehrere Nachrichten erhalten, bevor das Zeitfenster endet, jedes Mal der gleichen Variante zugeordnet. Nach dem Experiment-Fenster wird jede:r Nutzer:in auf den Weg geschickt, der für sie:ihn am ehesten zu einer Konversion führt.

## Personalisierte Pfade verwenden

### Schritt 1: Einen Experimentierpfad hinzufügen

Fügen Sie einen [Experimentierpfad]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) zu Ihrem Canvas hinzu und aktivieren Sie dann **Personalisierte Pfade**.

![][1]{: style="max-width:75%;" }

### Schritt 2: Konfigurieren Sie die Einstellungen für personalisierte Pfade

Geben Sie das Umwandlungsereignis an, das den Gewinner bestimmen soll. Wenn keine Konversions-Events verfügbar sind, kehren Sie zum ersten Schritt der Canvas-Einrichtung zurück und [weisen Konversions-Events zu]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Wenn Sie ein Conversion-Ereignis mit Öffnungen oder Klicks wählen, um den Gewinner zu ermitteln, dann trägt nur der erste Nachrichtenschritt im Pfad, der Öffnungen oder Klicks erzeugt, zur Ermittlung des Gewinners bei. Nachfolgende Schritte auf dem Pfad werden nicht berücksichtigt.

Legen Sie dann das **Experimentierfenster** fest. Das **Experimentierfenster** bestimmt, wie lange die Benutzer über alle Pfade geschickt werden, bevor der beste Pfad für jeden Benutzer in der Verzögerungsgruppe ausgewählt wird. Das Fenster beginnt, wenn der erste Nutzer:innen den Schritt betritt.

![][2]{: style="max-width:75%;" }

### Schritt 3: Fallback festlegen

Wenn die Ergebnisse des Tests nicht ausreichen, um einen statistisch signifikanten Gewinner zu ermitteln, werden alle zukünftigen Benutzer standardmäßig auf den einzigen Pfad mit der besten Leistung geschickt.

Alternativ können Sie auch auswählen, **allen zukünftigen Nutzer:innen die Mischung der Pfade weiter zu senden**.

![][3]

Mit dieser Option werden künftige Benutzer entsprechend den in der Pfadverteilung des Experiments angegebenen Prozentsätzen auf die verschiedenen Pfade geschickt.

![][4]

### Schritt 4: Fügen Sie Ihre Pfade hinzu und starten Sie den Canvas

{% tabs local %}
{% tab Einzelversand Canvas %}

Eine einzelne Experimentpfad-Komponente kann bis zu vier Pfade enthalten. Allerdings können Sie bei einmalig gesendeten Leinwänden bis zu drei Pfade hinzufügen, wenn die Option Personalisierte Pfade aktiviert ist. Der vierte Pfad sollte für die Verzögerungsgruppe reserviert sein, die Braze automatisch zu Ihrem Experiment hinzufügt.

Richten Sie Ihr Canvas nach Bedarf ein und starten Sie es dann. Wenn der erste Nutzer:innen das Experiment betreten hat, können Sie im Canvas die Analytics sehen und [die Performance Ihres Experiments tracken.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Wenn das Experimentfenster verstrichen und das Experiment abgeschlossen ist, schickt Braze die Nutzer:innen der Verzögerungsgruppe auf die Pfade mit der höchsten personalisierten Wahrscheinlichkeit für eine Konversion, basierend auf der Empfehlung des Look-alike-Modells.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Wiederkehrendes oder aktionsgesteuertes oder API-gesteuertes Canvas %}

Sie können bis zu vier Pfade in einem einzigen Experimentierpfad testen. Fügen Sie Ihre Pfade hinzu und richten Sie Ihr Canvas nach Bedarf ein.  

Wenn der erste Nutzer:innen das Experiment betreten hat, können Sie im Canvas die Analytics sehen und [die Performance Ihres Experiments tracken.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

Wenn das Experiment-Fenster verstrichen und das Experiment abgeschlossen ist, werden alle nachfolgenden Nutzer:innen des Canvas auf den Weg geschickt, der für sie am ehesten zu einer Konversion führt.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Analytics {#analytics}

Wenn Personalisierte Pfade aktiviert wurde, ist Ihre Analytics-Ansicht in zwei Tabs unterteilt: **Erstes Experiment** und **personalisierte Pfade**.

{% tabs local %}
{% tab Erstes Experiment %}

Die Registerkarte **Erstes Experiment** zeigt die Metriken für jeden Pfad während des Experimentierfensters. Sie können eine Zusammenfassung der Leistung aller Pfade für die angegebenen Konvertierungsereignisse sehen.

![Ergebnisse eines ersten Experimentes zur Ermittlung des besten Performance-Pfades für je:den Nutzer:in. Eine Tabelle zeigt die Leistung der einzelnen Pfade auf der Grundlage verschiedener Metriken für den Zielkanal.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Standardmäßig sucht der Test nach Assoziationen zwischen den benutzerdefinierten Ereignissen des Benutzers und seinen Pfadeinstellungen. Diese Analyse stellt fest, ob angepasste Events die Wahrscheinlichkeit erhöhen oder verringern, auf einen bestimmten Pfad zu reagieren. Diese Beziehungen werden dann verwendet, um zu bestimmen, welchen Nutzer:innen welcher Pfad zugewiesen wird, nachdem das Experiment-Fenster vorüber ist.

Die Beziehungen zwischen benutzerdefinierten Ereignissen und Nachrichteneinstellungen werden in der Tabelle auf der Registerkarte **Erstes Experiment** angezeigt.

![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Wenn der Test keine sinnvolle Beziehung zwischen angepassten Events und Pfadpräferenzen finden kann, greift der Test auf eine sitzungsbasierte Analysemethode zurück.

{% details Fallback-Analyse-Methode %}

**Sitzungsbasierte Analyse-Methode**<br>
Wenn die Fallback-Methode zur Bestimmung der personalisierten Pfade verwendet wird, zeigt die Registerkarte **Erstes Experiment** eine Aufschlüsselung der bevorzugten Varianten der Benutzer auf der Grundlage einer Kombination bestimmter Merkmale.

Diese Merkmale sind:

- **Aktualität:** Wann sie zuletzt eine Sitzung hatten
- **Frequenz:** Wie oft sie Sitzungen abhalten
- **Amtszeit:** Wie lange sie bereits Nutzer:in sind

![Die Tabelle mit den Nutzereigenschaften, die zeigt, welche Nutzer:innen aufgrund der drei Buckets für Häufigkeit, Häufigkeit und Dauer der Nutzung prognostiziert werden, Pfad 1 und Pfad 2 zu bevorzugen.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Denken Sie an die Aktualität, d.h. wie lange die letzte Interaktion mit Ihnen zurückliegt, an die Häufigkeit, d.h. wie oft sie sich engagieren, und an die Dauer, d.h. wie lange sie sich insgesamt mit Ihnen engagieren. Wir gruppieren die Benutzer anhand dieser drei Dinge (wie in der Tabelle mit **den Benutzereigenschaften** erläutert) in "Bereiche" und sehen dann, welcher Bereich welchen Pfad am meisten mag. Es ist, als würden Sie die Benutzer in Hunderte von verschiedenen Listen sortieren, je nachdem, wann sie zuletzt bei Ihnen eingekauft haben, wie oft sie einkaufen und wie lange sie schon Kunden sind.

Wenn es darum geht, eine Nachricht für einen Benutzer auszuwählen, prüft Braze die Kategorien, in die er fällt. Jeder Bucket beeinflusst die Pfadauswahl der Nutzer:innen auf unterschiedliche Weise. Wir quantifizieren diesen Einfluss mit einer statistischen Methode namens [logistische Regression](https://en.wikipedia.org/wiki/Logistic_regression), mit der sich zukünftiges Verhalten auf der Grundlage vergangener Aktionen vorhersagen lässt. Diese Methode berücksichtigt die Benutzerinteraktionen während des ersten Versands der Nachricht. Diese Tabelle fasst die Ergebnisse nur zusammen, indem sie anzeigt, welchen Pfad die Nutzer in jedem Bereich am liebsten nutzen.

Letztendlich kombiniert Braze all diese Daten, um für je:den Nutzer:in einen maßgeschneiderten Nachrichtenpfad auszuwählen, um sicherzustellen, dass die Nachricht für ihn so ansprechend und relevant wie möglich ist.

{% alert note %}
Die Zeitintervalle für jeden Bucket werden auf der Grundlage von Canvas-spezifischen Nutzerdaten bestimmt, die von Canvase zu Canvase variieren können.
{% endalert %}

**Wie personalisierte Pfade ausgewählt werden**<br>
Bei dieser Methode ist die empfohlene Nachricht eines einzelnen Nutzers oder einer einzelnen Nutzerin die Summe der Effekte seiner spezifischen Häufigkeit, Häufigkeit und Dauer. Häufigkeit, Häufigkeit und Dauer der Nutzung werden in Buckets unterteilt, wie in der Tabelle **Nutzer:innen zu** sehen ist. Die Zeitspanne der einzelnen Buckets wird durch die Daten der Nutzer:innen in jedem einzelnen Canvas bestimmt und ändert sich von Canvas zu Canvas.

Jeder Bucket kann einen unterschiedlichen Beitrag oder "Push" zu jedem Pfad leisten. Die Stärke des Push für jeden Bucket wird anhand der Antworten der Nutzer:innen im ersten Experiment mit Hilfe einer [logistischen Regression](https://en.wikipedia.org/wiki/Logistic_regression) bestimmt. Diese Tabelle fasst die Ergebnisse nur zusammen, indem sie anzeigt, welchen Pfad die Nutzer in jedem Bereich am liebsten nutzen. Der tatsächliche personalisierte Pfad eines einzelnen Benutzers hängt von der Summe der Auswirkungen der drei Bereiche ab, in denen er sich befindet - einer für jedes Merkmal.

{% enddetails %}

{% endtab %}
{% tab Personalisierte Pfade %}

Die Registerkarte **Personalisierte Pfade** zeigt die Ergebnisse des letzten Experiments, bei dem die Benutzer der Gruppe Verzögerung den für sie besten Pfad gewählt haben.

Die drei Karten auf dieser Seite zeigen Ihren voraussichtlichen Auftrieb, die Gesamtergebnisse und die voraussichtlichen Ergebnisse, wenn Sie stattdessen nur den Winning Path gesendet hätten. Selbst wenn es keinen Aufschwung gibt, was manchmal vorkommen kann, ist das Ergebnis dasselbe wie bei einem herkömmlichen A/B-Test, bei dem nur der Winning Path versendet wird.

- **Projizierter Auftrieb:** Die Verbesserung des von Ihnen gewählten Konversionsereignisses durch die Verwendung von personalisierten Pfaden, anstatt jeden Benutzer auf den allgemein besten Pfad zu schicken.
- **Gesamtergebnisse:** Die Ergebnisse des zweiten Sendevorgangs basierend auf Ihrem Konversions-Event.
- **Prognostizierte Ergebnisse:** Die voraussichtlichen Ergebnisse des zweiten Versands auf der Grundlage der von Ihnen gewählten Optimierungsmetrik, wenn Sie stattdessen nur die Gewinnvariante versendet hätten.

![Registerkarte Personalisierte Pfade für ein Canvas. Die Karten zeigen den prognostizierten Lift, die Gesamtkonversionen (mit personalisierten Pfaden) und die prognostizierten einmaligen Öffnungen (mit Gewinnpfad).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Personalisierte Pfade mit lokaler Zeitangabe verwenden

Wir raten davon ab, die Zustellung zur Ortszeit in Canvase mit personalisierten Pfaden zu verwenden. Das liegt daran, dass die Experimentierfenster beginnen, wenn der erste Nutzer:innen durchläuft. Benutzer, die sich in sehr frühen Zeitzonen befinden, können den Schritt betreten und den Start des Experimentierfensters viel früher auslösen, als Sie erwarten. Das kann dazu führen, dass das Experiment beendet wird, bevor der Großteil Ihrer Benutzer in typischeren Zeitzonen genug Zeit hatte, den Canvas zu betreten und zu konvertieren.

Wenn Sie eine lokale Zustellung wünschen, sollten Sie ein Zeitfenster von 24-48 oder mehr Stunden einplanen. Auf diese Weise betreten Nutzer:innen in frühen Zeitzonen den Canvas und triggern den Start des Experiments, aber es bleibt noch genügend Zeit im Experimentierfenster. Nutzer:innen in späteren Zeitzonen haben noch genügend Zeit, den Canvas und den Experiment-Schritt mit personalisierten Pfaden zu betreten und möglicherweise umzuwandeln, bevor das Experiment-Fenster abläuft.

[1]: {% image_buster /assets/img/experiment_step/experiment_personalized_path.png %}
[2]: {% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %}
[3]: {% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %}
[4]: {% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %}
[5]: {% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}
[6]: {% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}

---
nav_title: Zufällige Bucket-Nummern
article_title: Zufällige Bucket-Nummern
page_order: 2
page_type: reference
description: "Dieser Artikel behandelt das Konzept der Zufallszahlen und wie Sie damit Varianten und Kontrollgruppen erstellen können."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Zufällige Bucket-Nummern

> Eine zufällige Bucket-Nummer ist ein Benutzerattribut, das verwendet werden kann, um gleichmäßig verteilte Segmente von Zufallsbenutzern zu erstellen. 

## Übersicht

Wenn ein Nutzerprofil in Braze erstellt wird, wird dieser Nutzerin oder diesem Nutzer automatisch eine zufällige Bucket-Nummer zwischen 0 und 9999 (einschließlich) zugewiesen. Sie können diese Segmente verwenden, um die Effektivität mehrerer Kampagnen oder Canvases bei Gruppen von Nutzern im Laufe der Zeit zu testen.

### Verwendung der globalen Kontrollgruppe

Zufällige Bucket-Nummern werden in Ihrer globalen Kontrollgruppe verwendet - einer Gruppe von Benutzern, die keine Kampagnen oder Canvases erhalten. Braze wählt nach dem Zufallsprinzip mehrere Bereiche mit zufälligen Bucket-Nummern aus und schließt Benutzer aus diesen ausgewählten Buckets ein. Zufällige Bucket-Nummern werden ohne Gewichtung oder Berücksichtigung der zuletzt vergebenen Nummern zugewiesen. 

{% alert note %}
Wenn ein Nutzer:innen gelöscht und neu angelegt wird, erhält er eine andere zufällige Bucket-Nummer, da er als neuer Nutzer betrachtet wird.
{% endalert %}

Wenn Sie eine globale Kontrollgruppe eingerichtet haben und zufällige Bucket-Nummern für andere Anwendungsfälle verwenden möchten, lesen Sie die Hinweise, auf die [Sie achten]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) sollten.

### Wann Sie zufällige Eimerzahlen verwenden sollten

Wenn Sie die Effektivität mehrerer Kampagnen oder Canvases über einen längeren Zeitraum hinweg testen möchten, können Sie zufällige Bucket-Nummern zur Segmentierung Ihrer Nutzer verwenden.

### Wann Sie etwas anderes verwenden sollten

Wenn Sie Benutzer für Tests innerhalb einer einzelnen Kampagne oder eines einzelnen Canvas segmentieren möchten, verwenden Sie [A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) für Kampagnen. Für Canvases können Sie verschiedene [Varianten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) für Tests auf Reiseebene erstellen oder [Experimentierpfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) für Tests auf Schrittebene verwenden.

## Segmente mit zufälligen Eimernummern erstellen

Fügen Sie beim [Erstellen eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) den Filter "Random Bucket #" hinzu. Geben Sie dann eine Zahl oder einen Zahlenbereich an, den Sie in Ihr Segment aufnehmen möchten.

![Ein Filter für Segmente, der für zufällige Bucket-Nummern nicht mehr als "3000" ist.]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Sie können diese Art von Segmenten verwenden, wenn Sie einen Test mit drei verschiedenen Varianten durchführen und auch eine Kontrollgruppe einbeziehen möchten. Betrachten Sie den folgenden Beispielplan für die Erstellung von Segmenten gleicher Größe für drei Varianten und eine Kontrollgruppe:

- Bucket-Nummern 0 bis 2499 entsprechen dem Kontrollsegment
- Bucket-Nummern 2500 bis 4999 gehören zu dem Segment, das Variante 1 erhält
- Bucket-Nummern 5000 bis 7499 gehören zu dem Segment, das Variante 2 erhält
- Bucket-Nummern 7500 bis 9999 gehören zu dem Segment, das die Variante 3 erhalten wird

Je nachdem, wie viele Segmente Sie wünschen und wie sich die Nutzer innerhalb der einzelnen Segmente verteilen, kann Ihr Plan anders aussehen.

Schalten Sie für jedes Ihrer Segmente mit zufälligen Bucket-Nummern, einschließlich der Kontrollgruppe, das [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) ein. Wenn Sie den Erfolg von Varianten im Vergleich zur Kontrollgruppe auswerten möchten, können Sie auf die Seite mit den [benutzerdefinierten Ereignissen]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) gehen und sehen, wie oft jedes Segment bestimmte benutzerdefinierte Ereignisse abgeschlossen hat.

### Zufälliger Wiedereintritt der Zielgruppe über zufällige Bucket-Nummern

Der zufällige Wiedereintritt einer Zielgruppe kann für [A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) oder das Targeting bestimmter Nutzer:innen in Ihren Kampagnen nützlich sein. Um eine zufällige Wiederaufnahme der Zielgruppe mit zufälligen Bucket-Nummern durchzuführen, gehen Sie wie folgt vor:

1. [Erstellen Sie Ihr Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. Definieren Sie die zufälligen Buckets. Verwenden Sie in Ihrer Kampagne oder Ihrem Canvas den Filter für zufällige Buckets, um Ihre Zielgruppe in verschiedene Gruppen aufzuteilen. Sie können zum Beispiel genau zwei zufällige Buckets angeben, in die Sie Ihre Zielgruppe aufteilen (50 % der Nutzer:innen pro Bucket).
3. Geben Sie im Abschnitt **Zielgruppen** Ihrer Kampagne oder Ihres Canvas die Einstellungen für den Zufallsbereich an. Auf diese Weise kann Braze die Benutzer anhand der festgelegten Prozentsätze automatisch den entsprechenden Bereichen zuordnen.
4. Richten Sie eine Logik ein, die es Nutzer:innen erlaubt, das Segment erneut zu betreten. So können Sie beispielsweise Nutzern erlauben, das Segment erneut zu betreten, wenn sie 15 Tage lang nicht mit einer App gearbeitet haben.
5. Starten Sie Ihre Kampagne und überwachen Sie die Leistung der einzelnen Buckets. Sie können Metriken wie Engagement-Raten und Konversionsraten analysieren, um festzustellen, wie effektiv die erneute Interaktion mit einer Zielgruppe für Ihren Anwendungsfall ist.



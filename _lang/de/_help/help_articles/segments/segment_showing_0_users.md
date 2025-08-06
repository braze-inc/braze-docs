---
nav_title: "Fehlende Nutzer:innen im Segment"
article_title: "Fehlende Nutzer:innen im Segment"
page_order: 1

page_type: solution
description: "Dieser Hilfeartikel führt Sie durch die Schritte zur Fehlerbehebung, wenn in Ihrem Segment keine Nutzer:innen angezeigt werden, Sie aber mit mehr rechnen."
tool: Segments
---

# Fehlende Nutzer:innen im Segment

Es gibt zwei mögliche Lösungen, wenn Sie `0` Nutzer:innen sehen, aber Sie haben mehr erwartet:
* [Genaue Statistiken berechnen](#calculate-exact-statistics)
* [Überprüfen Sie die Datenübertragung](#verify-data-transfer)

## Genaue Statistiken berechnen

Die Segmente-Statistiken könnten eine Schätzung darstellen. Die Schätzung wird auf der Grundlage einer Zufallsstichprobe mit einem Konfidenzintervall von 95% berechnet, dass das Ergebnis innerhalb von `+/- 1%` liegt. Je kleiner Ihre Nutzerbasis ist, desto wahrscheinlicher ist es, dass die Größe Ihres Segments nur eine grobe Schätzung ist. Klicken Sie im Panel **Segmentdetails** auf **Exakte Statistik berechnen**. Dadurch wird die genaue Anzahl der Nutzer:innen in Ihrem Segment berechnet.

![Panel "Segmente", das die Option "Exakte Statistik berechnen" anzeigt]({% image_buster /assets/img_archive/trouble8.png %})

## Überprüfen Sie die Datenübertragung

Es ist möglich, dass die Daten, nach denen Sie filtern, nicht an Braze gesendet werden. Um zu überprüfen, welche angepassten Events an Braze gesendet werden, sehen Sie in Ihrem [Bericht über angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics) nach.

Wählen Sie das angepasste Event zusammen mit den spezifischen Daten und der App aus, um zu sehen, welche Daten tatsächlich an Braze übertragen werden. Wenn Sie feststellen, dass `0` Daten an Braze gesendet werden, müssen Sie als Nächstes prüfen, wie Sie die Ereignisse an Braze senden.

![Grafik, die die Anzahl der angepassten Events als Null anzeigt]({% image_buster /assets/img_archive/trouble9.png %})

{% alert important %}
Die Daten, die Sie im Braze-Dashboard sehen, haben möglicherweise nicht die gleiche Syntax wie die Daten, die Sie an Braze senden. Achten Sie darauf, dass diese beiden genau übereinstimmen.
{% endalert %}

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 5\. Januar 2021_


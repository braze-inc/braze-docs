---
nav_title: Fehlende Benutzer im Segment
article_title: Fehlende Benutzer im Segment
page_order: 1

page_type: solution
description: "Dieser Hilfeartikel führt Sie durch die Schritte zur Fehlerbehebung, wenn in Ihrem Segment keine Nutzer angezeigt werden, Sie aber mit mehr rechnen."
tool: Segments
---

# Fehlende Benutzer im Segment

Es gibt zwei mögliche Lösungen, wenn Sie `0` Benutzer sehen, aber mehr erwartet haben:
* [Exakte Statistik berechnen](#calculate-exact-statistics)
* [Überprüfen Sie die Datenübertragung](#verify-data-transfer)

## Exakte Statistik berechnen

Die Segmentstatistik könnte eine Schätzung sein. Die Schätzung wird auf der Grundlage einer Zufallsstichprobe mit einem Konfidenzintervall von 95% berechnet, dass das Ergebnis innerhalb von `+/- 1%` liegt. Je kleiner Ihre Nutzerbasis ist, desto wahrscheinlicher ist es, dass die Größe Ihres Segments nur eine grobe Schätzung ist. Klicken Sie auf **Exakte Statistik berechnen** im Bereich **Segmentdetails**. Damit wird die genaue Anzahl der Nutzer in Ihrem Segment berechnet.

![Segmentdetails, das die Option Exakte Statistik berechnen anzeigt][28]

## Überprüfen Sie die Datenübertragung

Es ist möglich, dass die Daten, nach denen Sie filtern, nicht an Braze gesendet werden. Um zu überprüfen, welche benutzerdefinierten Ereignisse an Braze gesendet werden, sehen Sie sich Ihren [Bericht über benutzerdefinierte Ereignisse an][1].

Wählen Sie das benutzerdefinierte Ereignis zusammen mit den spezifischen Daten und der App aus, um zu sehen, welche Daten tatsächlich an Braze übertragen werden. Wenn Sie feststellen, dass die Daten von `0` an Braze gesendet werden, müssen Sie im nächsten Schritt prüfen, wie Sie die Ereignisse an Braze senden.

![Diagramm, das die Anzahl der benutzerdefinierten Ereignisse als Null anzeigt][29]

{% alert important %}
Die Daten, die Sie im Braze-Dashboard sehen, haben möglicherweise nicht die gleiche Syntax wie die, die Sie an Braze senden. Achten Sie darauf, dass diese beiden genau übereinstimmen.
{% endalert %}

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 5\. Januar 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics
[28]: {% image_buster /assets/img_archive/trouble8.png %}
[29]: {% image_buster /assets/img_archive/trouble9.png %}

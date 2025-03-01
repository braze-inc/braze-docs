---
nav_title: Nicht ausgelöste Kampagne oder Canvas
article_title: Nicht ausgelöste Kampagne oder Canvas
page_order: 5

page_type: solution
description: "Dieser Hilfeartikel führt Sie durch die Schritte zur Lösung von Problemen mit Kampagnen oder Canvases, die nicht wie erwartet ausgelöst werden."
tool: 
- Campaigns
- Canvas
---

# Nicht getriggerte Kampagne oder Canvas

Es gibt eine Reihe von Gründen, warum Sie nicht das erwartete Auslöseverhalten erhalten haben. Die Lösung für den häufigsten Fehler besteht darin, sicherzustellen, dass die Kampagne, die Sie auslösen, nicht dasselbe Auslöseereignis im Segment verwendet.

## Auslöser für Kampagnen

Die Segmentzugehörigkeit wird vor Auslöseaktionen ausgewertet. Das bedeutet, dass der Nutzer, der nicht in das erste Segment fällt, die Kampagne nicht erhält, selbst wenn er den Auslöser betätigt.

Wenn Ihre Kampagne durch ein benutzerdefiniertes Ereignis ausgelöst wird, müssen Sie sicherstellen, dass dieses Ereignis nicht durch ein Segment vorgefiltert wird, das Sie in der Kampagne verwenden möchten. 

Wenn das Segment beispielsweise das Ereignis `SessionStart` "Hat die App mehr als einmal verwendet" enthält und das Ereignis, von dem die Kampagne ausgelöst wird, `SessionStart` ist, erhält der Benutzer die Nachricht, aber nicht unbedingt für die erste Sitzung. Das liegt daran, dass die Kampagne im ersten Schritt, wenn sie prüft, ob ein Benutzer eine Kampagne erhalten soll, das Zielgruppensegment überprüft. 

Kurz gesagt: Vermeiden Sie es, eine aktionsbasierte Kampagne oder ein Canvas mit demselben Auslöser wie den Zielgruppenfilter zu konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines benutzerdefinierten Ereignisses). Es kann eine [Wettlaufbedingung][2] auftreten, bei der der Benutzer nicht in der Zielgruppe ist, wenn er das Auslöseereignis ausführt. Das bedeutet, dass er die Kampagne nicht erhält oder den Canvas nicht betritt.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlersuche in der Kampagne benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da wir nur die Diagnoseprotokolle der letzten 30 Tage haben.
{% endalert %}

_Zuletzt aktualisiert am 25\. Juni 2024_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/#session-start-event/
[2]: {{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/
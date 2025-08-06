---
nav_title: Unausgelöste Kampagne oder Canvas
article_title: Unausgelöste Kampagne oder Canvas
page_order: 5

page_type: solution
description: "Dieser Hilfeartikel führt Sie durch die Schritte zur Lösung von Problemen mit Kampagnen oder Canvase, die nicht wie erwartet ausgelöst werden."
tool: 
- Campaigns
- Canvas
---

# Nicht ausgelöste Kampagne oder Canvas

Es gibt eine Reihe von Gründen, warum Sie nicht das erwartete Verhalten des Triggers erhalten haben. Die Lösung für den häufigsten Fehler besteht darin, sicherzustellen, dass die Kampagne, die Sie triggern, nicht das gleiche Trigger-Ereignis im Segment verwendet.

## Auslöser für Kampagnen

Die Segmentzugehörigkeit wird vor triggernden Aktionen ausgewertet. Das bedeutet, dass Nutzer:innen, die nicht in das erste Segment fallen, die Kampagne nicht erhalten, selbst wenn sie den Trigger ausführen.

Wenn Ihre Kampagne durch ein angepasstes Event getriggert wird, sollten Sie sicherstellen, dass dieses Event nicht durch ein Segment, das Sie in der Kampagne verwenden möchten, vorgefiltert ist. 

Wenn das Segment beispielsweise das Ereignis `SessionStart` "Hat die App mehr als einmal genutzt" enthält und das Ereignis, von dem die Kampagne getriggert wird, `SessionStart` ist, erhält der Nutzer:in zwar die Nachricht, aber nicht unbedingt für die erste Sitzung. Das liegt daran, dass die Kampagne im ersten Schritt bei der Prüfung, ob ein Nutzer:innen eine Kampagne erhalten soll, das Segment Targeting überprüft. 

Kurz gesagt, vermeiden Sie es, eine aktionsbasierte Kampagne oder ein Canvas mit demselben Trigger wie den Zielgruppen-Filter zu konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines angepassten Events). Es kann eine [Race-Condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#race-conditions/) auftreten, bei der sich der Nutzer:in nicht in der Zielgruppe befindet, wenn er das Trigger-Ereignis ausführt, was bedeutet, dass er die Kampagne nicht erhält oder den Canvas nicht betritt.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlersuche in der Kampagne benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da wir nur die Diagnoseprotokolle der letzten 30 Tage haben.
{% endalert %}

_Zuletzt aktualisiert am 25\. Juni 2024_


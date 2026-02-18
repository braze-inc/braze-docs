---
nav_title: Fehlersuche
article_title: Fehlerbehebung Canvase
page_order: 11
page_type: reference
description: "Diese Seite enthält Schritte zur Fehlerbehebung für Canvase."
tool: Canvas
---

# Fehlerbehebung Canvase

> Diese Seite hilft Ihnen bei der Fehlerbehebung von Problemen mit Ihren Canvase.

## Warum hat ein Nutzer:innen einen getriggerten Canvas-Schritt nicht erhalten?

Bestätigen Sie zunächst, dass das angepasste Event an Braze weitergegeben wird. Gehen Sie zu **Analytics** > **Bericht über angepasste Events**, und wählen Sie dann das entsprechende angepasste Event und den Datumsbereich aus. Wenn das Ereignis nicht angezeigt wird, vergewissern Sie sich, dass es korrekt eingerichtet ist und dass der Nutzer:innen die richtige Aktion durchgeführt hat.

Wenn das angepasste Event angezeigt wird, gehen Sie zur weiteren Fehlerbehebung wie folgt vor:

- Überprüfen Sie das heruntergeladene Profil des Nutzers:innen, um sich zu vergewissern, dass er das Ereignis ausgelöst hat und wann er es ausgelöst hat. Wenn das Ereignis getriggert wurde, vergleichen Sie den Zeitstempel, zu dem das Ereignis getriggert wurde, mit dem Zeitpunkt, zu dem der Canvas live ging. Das Ereignis kann ausgelöst worden sein, bevor der Canvas online ging.
- Überprüfen Sie die Changelogs für das Canvas und alle Segmente, die beim Targeting verwendet werden, um festzustellen, ob sich der Nutzer:in dem Segment befand, als sein angepasstes Event getriggert wurde. Wenn sie nicht in dem Segment wären, hätten sie den Canvas-Schritt nicht erhalten.
- Überprüfen Sie, ob der Nutzer:innen durch Segmentierung in eine Kontrollgruppe aufgenommen wurde und daher den Canvas-Schritt nicht erhalten hat.
- Wenn es eine geplante Verzögerung gibt, prüfen Sie, ob das angepasste Event des Nutzers:innen vor der Verzögerung ausgelöst wurde. Wenn das Ereignis vor der Verzögerung getriggert worden wäre, hätten sie den Canvas-Schritt nicht erhalten.

{% alert note %}
In-App-Nachrichten können nur durch Ereignisse ausgelöst werden, die über das SDK gesendet werden, nicht über die REST API.
{% endalert %}

## Warum wird mein Canvas nicht wie erwartet gesendet?

Canvase sind robust und komplex, und wir wissen, dass Sie viel Zeit und Sorgfalt aufwenden, um sie zu gestalten. Wenn Sie also feststellen, dass Ihr Canvas nicht so gesendet wird, wie Sie es wünschen, empfehlen wir Ihnen, Ihren Zeitplan, die Zielgruppen für den Eingang und die Einstellungen für den Eingang zu überprüfen und die Schritte zur [Erstellung eines Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) noch einmal zu lesen.

### Zeitplan

- Ist der Zeitplan für den Canvas [korrekt eingerichtet]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#entry-schedule-types)?
- Haben Sie das richtige Datum und die richtige Uhrzeit ausgewählt?
- Bei [aktionsbasierter Zustellung]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=action-based%20delivery#entry-schedule-types): Haben die Nutzer:innen die angegebenen Aktionen ausgeführt, seit Sie das Canvas gestartet haben?

### Eingang-Einstellungen

Die [Eingangseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=basics#selecting-entry-controls) sind wichtig, um zu verstehen, wie Ihre Canvase gesendet werden. Prüfen Sie, ob Sie die Anzahl der Personen, die das Canvas betreten können, begrenzt haben.

Nutzer:innen können ein Canvas auch verlassen, wenn sie keine Nachrichten mehr erhalten möchten. Wenn das Canvas beispielsweise nur Push-Benachrichtigungen enthält und ein Nutzer:in nach dem ersten Schritt die Push-Benachrichtigung abbestellt, würde dieser Nutzer:innen aus dem Canvas aussteigen. Erwägen Sie die Verwendung [verschiedener Canvas-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), um alternative Nutzer:innen hinzuzufügen.

### Segmentierung Ihrer Zielgruppe

Beachten Sie die folgenden Fragen zu Ihrer Zielgruppe:

- Haben Sie das richtige Segment ausgewählt?
- Wie wird das Segment eingerichtet?
- Haben Sie bestätigt, dass das Segment irgendwelche Nutzer:innen enthält?
- Haben Sie zusätzliche Filter hinzugefügt, um die Anzahl der Nutzer:innen im Canvas zu begrenzen?
- Sind die Nutzer:innen qualifiziert, die erste Stufe Ihrer Varianten zu erhalten? Wenn der erste Schritt Ihres Canvas beispielsweise eine Push-Benachrichtigung ist, die Zielgruppen für den Eingang aber alle Push-fähig sind, werden keine Nutzer:innen Nachrichten erhalten.

## Warum hat sich meine Zielgruppe nicht gleichmäßig zwischen der Kontrollgruppe und der Variante aufgeteilt?

Bei der Erstellung Ihres Canvas haben Sie vielleicht erwartet, dass sich Ihre Zielgruppe gleichmäßig auf Ihre Kontrollgruppe und Ihre Variante aufteilt, wie in dem folgenden [Anwendungsfall](#use-case). Lassen Sie uns besprechen, warum das so ist und wie Sie das Problem lösen können!

Welcher Gruppe ein Nutzer:in beitritt, hängt von seinen Einstellungen ab. Dies kann entweder die Kontrollgruppe oder die Variante sein. Ein Nutzer:innen betritt ein Canvas, wenn er alle von Ihnen im [Eingangsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) definierten Kriterien erfüllt. Bei der Einrichtung Ihres Canvas legen Sie fest, welcher Prozentsatz der Nutzer:innen jede Variante und die Kontrollgruppe betreten wird.

Wenn Ihre Kontrollgruppe im Vergleich zu Ihrer Variante groß ist (was nicht Ihre Absicht ist), empfehlen wir Folgendes:
1. Setzen Sie den Zielgruppen-Filter für den Eingang auf **Foreground Push Enablement**.
2. Setzen Sie den Zielgruppen-Filter für Ihren Eingang auf **Push-Abonnement-Status**, **E-Mail-Abonnement-Status** oder beides auf **Opt-in** oder **Abonnent**.

Bestätigen Sie bei der Erstellung eines Canvas mit einer Kontrollgruppe, dass alle Nutzer:innen des Eingangs in der Lage sind, Nachrichten innerhalb des Canvas zu empfangen (z.B. wenn das Canvas Push- und E-Mail-Nachrichten enthält).

### Anwendungsfall

Stellen wir uns das folgende Szenario vor:
- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt bei dieser Variante ist eine Push-Benachrichtigung.
- 90% der Nutzer:innen wurden für die Variante ausgewählt, 10% für die Kontrollgruppe.

![Canvas-Beispiel mit 90% Variante und 10% Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario werden 90% der Nutzer:innen, die den Canvas betreten, die Variante eingeben. 

Wenn wir uns die aktiven Nutzer:innen ansehen, können wir feststellen, dass trotz der 29,8k Nutzer:innen nur 64% von ihnen Push aktiviert haben:

![Segmente mit dem Filter "Push Enabled" auf "true" und geschätzten Nutzer:innen von 29,8k.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass nicht alle Nutzer:innen eine Push-Benachrichtigung erhalten können, auch wenn wir 90% der Nutzer:innen für die Variante angegeben haben. Diese Nutzer:innen, die keine Push-Benachrichtigung erhalten können, werden die Variante trotzdem eingeben.
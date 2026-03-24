---
nav_title: Fehlersuche
article_title: Fehlerbehebung bei Canvases
page_order: 11
page_type: reference
description: "Diese Seite enthält Schritte zur Fehlerbehebung für Canvase."
tool: Canvas
---

# Fehlerbehebung bei Canvases

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

## Warum wird meine Canvas-Nachricht nicht wie erwartet versendet?

Canvase sind robust und komplex, und wir wissen, dass Sie viel Zeit und Sorgfalt aufwenden, um sie zu gestalten. Sollten Sie feststellen, dass Ihr Canvas nicht wie gewünscht versendet wird, empfehlen wir Ihnen, Ihren Canvas-Zeitplan, die Zielgruppe und die Einstellungen zu überprüfen und die Schritte zum [Erstellen eines Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) zu überprüfen.

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
- Haben Sie überprüft, ob das Segment Nutzer:innen enthält?
- Haben Sie zusätzliche Filter hinzugefügt, um die Anzahl der Nutzer:innen im Canvas zu begrenzen?
- Sind die Nutzer:innen qualifiziert, die erste Stufe Ihrer Varianten zu erhalten? Wenn der erste Schritt Ihres Canvas beispielsweise eine Push-Benachrichtigung ist, die Zielgruppen für den Eingang aber alle Push-fähig sind, werden keine Nutzer:innen Nachrichten erhalten.

## Warum haben am Tag der Zeitumstellung keine Nutzer:innen an meinem täglich im Zeitplan stehenden Canvas-Kurs teilgenommen?

An Tagen, an denen die Sommerzeit beginnt oder endet, können täglich im Zeitplan aufgeführte Canvases bis zu einer Stunde früher oder später als üblich ausgeführt werden. Wenn Ihre Teilnahmekriterien auf benutzerdefinierten Attributen oder Ereignissen mit Zeitstempeln basieren, die innerhalb einer Stunde vor der geplanten Teilnahmezeit liegen, sind Nutzer:innen möglicherweise am Tag der Zeitumstellung noch nicht teilnahmeberechtigt, da das Attribut oder Ereignis noch nicht protokolliert wurde.

Nehmen wir beispielsweise an, dass Nutzer:innen in der Regel um 3:00 p.mUhr in der Zeitzone Ihres Canvas ein Update für die angepassten Attribute erhalten und Ihr Canvas täglich um 3:30 p.mUhr in derselben Zeitzone ausgeführt wird. An einem Tag, an dem die Sommerzeit beginnt, kann Canvas Nutzer:innen bis zu einer Stunde früher als üblich in Bezug auf dieses Attribut-Update bewerten – bevor das Attribut protokolliert wurde. Wenn die Wiederteilnahme deaktiviert ist, können Nutzer:innen, die an vorherigen Tagen teilgenommen haben, nicht erneut teilnehmen, was zu null Eingängen für diesen Tag führt.

Um dies zu vermeiden, stellen Sie bitte sicher, dass Ihre angepassten Attribut- oder Ereignisaktualisierungen mehr als eine Stunde vor der geplanten Eingabezeit von Canvas erfolgen.

## Warum hat sich meine Zielgruppe nicht gleichmäßig auf die Kontrollgruppe und die Variantengruppe verteilt?

Bei der Erstellung Ihres Canvas haben Sie möglicherweise erwartet, dass sich Ihre Zielgruppe gleichmäßig auf Ihre Kontrollgruppe und Ihre Variantengruppe aufteilt, wie im folgenden [Anwendungsfall](#use-case) dargestellt. Lassen Sie uns erörtern, warum dies der Fall ist und wie man das Problem beheben kann.

Welcher Gruppe ein Nutzer:in beitritt, hängt von seinen Einstellungen ab. Dies kann entweder die Kontrollgruppe oder die Variante sein. Eine Nutzer:in gelangt in einen Canvas, wenn sie alle Ihre im [Eingang]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=entry%20schedule#step-12-determine-your-canvas-entry-schedule) definierten Kriterien erfüllt. Bei der Einrichtung Ihres Canvas legen Sie fest, welcher Prozentsatz der Nutzer:innen in jede Variante und in die Kontrollgruppe aufgenommen wird.

Wenn Ihre Kontrollgruppe im Vergleich zu Ihrer Variante groß ist (was nicht Ihre Absicht ist), empfehlen wir Folgendes:
1. Bitte stellen Sie Ihren Eingangs-Zielgruppen-Filter auf **„Foreground Push aktiviert“** ein.
2. Stellen Sie Ihren Zielgruppen-Filter für **den Push-Abonnementstatus**, **den E-Mail-Abonnementstatus** oder beides auf **„Opt-in“** oder **„Subscribed“** ein.

Bitte stellen Sie bei der Erstellung eines Canvas mit einer Kontrollgruppe sicher, dass alle Nutzer:innen in den Zielgruppen Nachrichten innerhalb des Canvas empfangen können (z. B. wenn der Canvas Push- und E-Mail-Nachrichten enthält).

### Anwendungsfall

Stellen wir uns das folgende Szenario vor:
- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt bei dieser Variante ist eine Push-Benachrichtigung.
- 90% der Nutzer:innen wurden für die Variante ausgewählt, 10% für die Kontrollgruppe.

![Canvas-Beispiel mit einer 90-prozentigen Variante und einer 10-prozentigen Kontrollgruppe.]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario werden 90% der Nutzer:innen, die den Canvas betreten, die Variante eingeben. 

Betrachtet man die aktiven Nutzer:innen, so stellt man fest, dass von den insgesamt 29,8 Tausend Nutzer:innen nur 64 % Push-Benachrichtigungen aktiviert haben:

![Segment mit dem Filter „Push aktiviert“ auf „true“ gesetzt und geschätzten 29,8 Tausend Nutzer:innen.]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass nicht alle Nutzer:innen eine Push-Benachrichtigung erhalten können, auch wenn wir 90% der Nutzer:innen für die Variante angegeben haben. Diese Nutzer:innen, die keine Push-Benachrichtigung erhalten können, werden die Variante trotzdem eingeben.
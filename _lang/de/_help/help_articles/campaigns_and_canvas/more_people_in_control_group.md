---
nav_title: Umgang mit einer großen Kontrollgruppe
article_title: Umgang mit einer großen Kontrollgruppe
page_order: 2

page_type: solution
description: "Dieser Hilfeartikel beschreibt, warum Ihre Kontrollgruppe möglicherweise größer ist als erwartet, und führt Sie durch die Schritte, mit denen Sie dies beheben können."
tool: Canvas
---

# Umgang mit einer großen Kontrollgruppe

Bei der Erstellung Ihres Canvas haben Sie vielleicht erwartet, dass sich Ihre Zielgruppe gleichmäßig auf Ihre Kontrollgruppe und Ihre Variante aufteilt, wie in dem folgenden [Beispiel](#example). Wir können Ihnen erklären, warum das so ist und wie Sie das Problem beheben können!

Welcher Gruppe ein Nutzer:in beitritt, hängt von seinen Einstellungen ab. Dies kann entweder die Kontrollgruppe oder die Variante sein. Ein Nutzer tritt in ein Canvas ein, wenn er alle Kriterien erfüllt, die Sie im [Eingangsschritt]({{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas). Bei der Einrichtung Ihres Canvas legen Sie fest, wie viel Prozent der Nutzer:innen in jede Variante und die Kontrollgruppe eintreten werden.

Wenn Ihre Kontrollgruppe im Vergleich zu Ihrer Variante groß ist (was nicht Ihre Absicht ist), empfehlen wir Folgendes:
1. Setzen Sie den Zielgruppen-Filter für Ihren Eingang auf "Is Push Enablement".
2. Setzen Sie den Zielgruppen-Filter für Ihren Eingang auf "ist Opt-in oder abonniert".

Wenn Sie ein Canvas mit einer Kontrollgruppe erstellen, stellen Sie sicher, dass alle Nutzer:innen der Zielgruppe des Eingangs in der Lage sind, Nachrichten innerhalb des Canvas zu empfangen (z.B. enthält das Canvas Push- und E-Mail-Nachrichten).

## Anwendungsfall

Stellen wir uns das folgende Szenario vor:
- Ein Canvas hat eine einzelne Variante und eine Kontrollgruppe.
- Der erste Schritt bei dieser Variante ist eine Push-Benachrichtigung.
- 90% der Nutzer:innen wurden für die Variante ausgewählt, 10% für die Kontrollgruppe.

![Canvas Beispiel]({% image_buster /assets/img_archive/trouble15.png %})

In diesem Szenario werden 90% der Nutzer:innen, die den Canvas betreten, die Variante eingeben. 

Wenn wir uns die aktiven Nutzer:innen ansehen, können wir feststellen, dass trotz der 39,8k Nutzer:innen nur 73% von ihnen Push aktiviert haben:

![Eingang Zielgruppe]({% image_buster /assets/img_archive/trouble16.png %})

Das bedeutet, dass nicht alle Nutzer:innen eine Push-Benachrichtigung erhalten können, auch wenn wir 90% der Nutzer:innen für die Variante angegeben haben. Diese Nutzer:innen, die keine Push-Benachrichtigung erhalten können, werden die Variante trotzdem eingeben.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 3\. Dezember 2020_


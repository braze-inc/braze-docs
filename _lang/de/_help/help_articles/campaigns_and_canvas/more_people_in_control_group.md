---
nav_title: Umgang mit einer großen Kontrollgruppe
article_title: Umgang mit einer großen Kontrollgruppe
page_order: 2

page_type: solution
description: "Dieser Hilfe-Artikel beschreibt, warum Ihre Kontrollgruppe möglicherweise größer ist als erwartet, und führt Sie durch die Schritte, mit denen Sie dies beheben können."
tool: Canvas
---

# Umgang mit einer großen Kontrollgruppe

Bei der Erstellung Ihres Canvas haben Sie vielleicht erwartet, dass sich Ihr Publikum gleichmäßig auf Ihre Kontrollgruppe und Ihre Variantengruppe aufteilt, wie im folgenden [Beispiel](#example). Wir können Ihnen erklären, warum das so ist und wie Sie das Problem beheben können!

Die Gruppe, der ein Benutzer beitritt, hängt von seinen Einstellungen ab. Dies kann entweder die Kontrollgruppe oder die Variantengruppe sein. Ein Benutzer betritt ein Canvas, wenn er alle von Ihnen im [Eingabeschritt][1] definierten Kriterien erfüllt. Bei der Einrichtung Ihres Canvas legen Sie fest, welcher Prozentsatz der Benutzer jede Variante und die Kontrollgruppe eingeben wird.

Wenn Ihre Kontrollgruppe im Vergleich zu Ihrer Variantengruppe groß ist (und das ist nicht Ihre Absicht), empfehlen wir Folgendes:
1. Setzen Sie den Filter für Ihren Eintrag auf "Ist Push aktiviert".
2. Setzen Sie den Filter für Ihre Zielgruppe auf "ist angemeldet oder abonniert".

Wenn Sie ein Canvas mit einer Kontrollgruppe erstellen, stellen Sie sicher, dass alle Benutzer in der Entry Audience in der Lage sind, Nachrichten innerhalb des Canvas zu empfangen (z. B. enthält das Canvas Push- und E-Mail-Nachrichten).

## Anwendungsfall

Stellen wir uns das folgende Szenario vor:
- Ein Canvas hat eine einzige Variante und eine Kontrollgruppe.
- Der erste Schritt der Variante ist eine Push-Benachrichtigung.
- 90% der Nutzer wurden für die Variante ausgewählt und 10% für die Kontrollgruppe.

![Leinwand Beispiel][41]

In diesem Szenario werden 90% der Benutzer, die den Canvas betreten, die Variante eingeben. 

Wenn wir uns die aktiven Nutzer ansehen, können wir feststellen, dass trotz der 39,8k Nutzer nur 73% von ihnen Push aktivieren:

![Eintritt Publikum][42]

Das bedeutet, dass, obwohl wir 90 % der Benutzer für die Eingabe der Variante angegeben haben, nicht alle dieser Benutzer tatsächlich eine Push-Benachrichtigung erhalten können. Diese Benutzer, die keine Push-Benachrichtigung erhalten können, werden die Variante trotzdem eingeben.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 3\. Dezember 2020_

[1]: {{site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2-use-the-entry-wizard-to-set-up-your-canvas
[41]: {% image_buster /assets/img_archive/trouble15.png %}
[42]: {% image_buster /assets/img_archive/trouble16.png %}

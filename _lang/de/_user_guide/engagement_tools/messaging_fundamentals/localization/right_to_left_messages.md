---
nav_title: Nachrichten von rechts nach links
article_title: Erstellen von Nachrichten von rechts nach links
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "Auf dieser Seite finden Sie bewährte Verfahren für die Erstellung von Nachrichten in Braze, die von rechts nach links gelesen werden."
---

# Erstellen von Nachrichten von rechts nach links

> Wie Nachrichten von rechts nach links letztendlich aussehen, hängt weitgehend davon ab, wie Dienstanbieter (wie Apple, Android und Google) sie darstellen. Auf dieser Seite finden Sie bewährte Verfahren für die Gestaltung von Nachrichten von rechts nach links, damit Ihre Nachrichten so genau wie möglich angezeigt werden.

## Aussehen der Nachrichten

Wenn Sie eine Nachricht von rechts nach links erstellen, sollten Sie Folgendes beachten:

- **Erscheinung im Braze-Dashboard:** Wenn eine Nachricht auf dem Gerät eines Nutzers:innen erscheint, wird ihr Aussehen weitgehend durch das Betriebssystem und die Spracheinstellungen des Geräts bestimmt. Das bedeutet, dass das, was Sie auf dem Dashboard sehen, nicht immer zu 100 % korrekt ist.
- **Erscheinung auf dem Gerät:** Apple und Android haben einen großen Einfluss darauf, wie Nachrichten dargestellt werden, während die Anbieter von E-Mail Serviceleistungen (ESP) einen gewissen Einfluss haben. Die Anpassung von HTML-E-Mails in Braze ist zwar flexibler, aber dieselbe Nachricht kann je nach den Einstellungen des Nutzers:innen auf verschiedenen Geräten unterschiedlich dargestellt werden.

Überprüfen Sie außerdem die Zeichensetzung und Emojis, um festzustellen, ob Ihre Nachricht standardmäßig oder von rechts nach links wiedergegeben wird.

| Standard Western Rendering | Rechts-nach-links-Rendering |
|------------------|------------------------|
| Zeigt das Ausrufezeichen und das Emoji am **Ende** des Satzes an. | Zeigt das Ausrufezeichen und das Emoji am **Anfang** des Satzes an. |
| ![Ein Beispiel für eine Standardnachricht von rechts nach links.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![Ein Beispiel für eine Nachricht von links nach rechts.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Erstellen einer Nachricht von rechts nach links

So erstellen Sie Ihre Nachricht von rechts nach links in Braze:

1. Verfassen Sie Ihre Standardnachricht im Braze-Editor.
2. Kopieren Sie den Nachrichtentext aus Braze und verwenden Sie dann ein Lokalisierungstool, um ihn in eine Nachricht von rechts nach links umzuwandeln.
3. Fügen Sie Ihre konvertierte Nachricht wieder in Braze ein.
4. Überprüfen Sie die Textformatierung und -ausrichtung. Wenn Sie eine E-Mail per Drag-and-Drop oder im HTML-Format erstellen, können Sie dies mit dem Composer tun. Andernfalls müssen Sie ein separates Textverarbeitungsprogramm verwenden.<br><br>![E-Mail Drag-and-Drop-Editor Menü mit Button zum Umschalten der Textausrichtung zwischen rechts-nach-links und links-nach-rechts.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Überlegungen
 
### Lange Push-Benachrichtigungen

Die Methode des Kopierens und Einfügens von Push-Nachrichten kann bei längeren Push-Benachrichtigungen eine Herausforderung darstellen, da längere Inhalte auf einem mobilen Gerät möglicherweise in mehreren Zeilen dargestellt werden. Wenn Sie Ihren Nachrichtentext von außerhalb von Braze kopieren (z.B. ein Word-Dokument) und direkt in Braze einfügen, können sich die Satzausrichtung und die Wortplatzierung ändern. Um dieses Szenario zu vermeiden, kopieren Sie in Raten und fügen Sie einen Zeilenumbruch ein. Kopieren Sie zum Beispiel die ersten fünf Wörter und fügen Sie einen Zeilenumbruch ein, kopieren Sie die nächsten fünf Wörter, fügen Sie einen Zeilenumbruch ein und so weiter.

Die Vorschau- und Testfunktionen sind für Nachrichten von links nach rechts ausgelegt. Daher werden Nachrichten von rechts nach links im Bereich **Vorschau & Test** nicht korrekt dargestellt, aber auf Nutzer:innen, wenn deren Einstellungen dafür konfiguriert sind. Wir empfehlen Ihnen, Nachrichten an sich selbst in einer Live-Umgebung zu senden, um zu überprüfen, ob sie je nach den Einstellungen Ihres Geräts korrekt wiedergegeben werden.

### Bidirektionaler Text

Viele Nutzer:innen, die in Rechts-nach-Links-Sprachen schreiben, verwenden eigentlich bidirektionalen Text: eine Kombination aus Links-nach-Rechts- und Rechts-nach-Links-Sprachen. Ein Marketer kann zum Beispiel eine Nachricht auf Hebräisch mit einem englischen Firmennamen senden. Braze kann die Formatierung von bidirektionalem Text nicht verarbeiten. Zwei Möglichkeiten zur Vermeidung von Formatierungsproblemen sind entweder die vollständige Vermeidung von bidirektionalem Text oder die Trennung von links-nach-rechts-Text und rechts-nach-links-Text durch Zeilenumbrüche. 

{% alert tip %}
Die korrekte Formatierung von bidirektionalem Text ist besonders wichtig, wenn Sie Nachrichten mit Promo-Codes verfassen. Promo-Codes werden oft von links nach rechts formatiert, da dieselben Codes in verschiedenen Märkten verwendet werden können. Es gibt zwei Möglichkeiten, Promo-Codes unterzubringen: entweder Sie verwenden ein Bild für den Promo-Code oder Sie fügen den Promo-Code am Ende der Nachricht nach einem Zeilenumbruch ein.
{% endalert %}

### Sonderzeichen, Zahlen und Emojis

Sonderzeichen (wie Satzzeichen, mathematische Symbole und Währungen), Zahlen, Aufzählungszeichen und Emojis können beim Erstellen von Nachrichten in Braze von rechts nach links "herumspringen". Um dies zu umgehen, schreiben Sie Ihre Kopie mit der richtigen Formatierung in einem externen Textverarbeitungsprogramm und fügen Sie die Kopie dann in Braze ein. Es kann auch hilfreich sein, Emojis nicht am Anfang Ihres Textes zu platzieren und sie (sowie Sonderzeichen und Zahlen) stattdessen durch Zeilenumbrüche vom Text zu trennen, um Ausrichtungsprobleme zu vermeiden.

### Arabische Nachrichten

Wenn Sie arabische Nachrichten verfassen, verwenden Sie eine deutlich höhere Schriftgröße, um die gleiche Lesbarkeit wie in anderen Sprachen zu erreichen. Wir empfehlen, für Sprachen, die das lateinische oder römische Alphabet verwenden, eine Schriftgröße zu wählen, die etwa 20% größer ist als Ihre übliche Größe. Das liegt daran, dass arabische Schriften klein gehalten werden, um den vertikalen Platz für die diakritischen Zeichen (Akzentzeichen) zu nutzen.

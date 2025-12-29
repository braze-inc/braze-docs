---
nav_title: Verbesserung der niedrigen Latenzzeit
article_title: Verbesserung der niedrigen Latenz für Content-Cards als Banner
page_order: 10
description: "Dieser Artikel befasst sich mit Strategien, die sicherstellen, dass die Anforderungen an niedrige Latenzzeiten mit Content-Cards erfüllt werden."
channel:
  - content cards
---

# Verbesserung der Latenzzeit für Content-Cards als Banner

> Wenn Sie bei Ihrer Content-Cards-Implementierung für kritische Anwendungsfälle, wie z.B. Homepage-Banner, mit Latenz zu kämpfen haben, finden Sie auf dieser Seite Strategien und Tipps zur Lösung und Beschleunigung des Renderings.

{% alert tip %}
Möchten Sie auf Ihrer App oder Website auffällige, angepasste Banner anzeigen? Versuchen Sie es mit [Bannern]({{site.baseurl}}/user_guide/message_building_by_channel/banners/), die für Anwendungsfälle mit niedriger Latenz entwickelt wurden.
{% endalert %}

## Verwenden Sie einen geplanten Eingang anstelle eines aktionsbasierten Eingangs

Aktionsbasierte Karten sowohl in Kampagnen als auch in Canvase erfordern eine Hintergrundverarbeitung. Braze muss erst von der triggernden Aktion (z.B. einem Kauf oder dem Beginn einer Sitzung) erfahren, bevor eine Karte für eine Nutzer:in erstellt werden kann. Daher wird es eine Verzögerung geben, bevor diese Karten verfügbar sind.

Aktionsbasierte Karten bringen zusätzliche Komplexität in Ihre Anwendung, da Sie möglicherweise ständig Abfragen und Aktualisierungen durchführen müssen, um zu warten, bis die Karte verfügbar ist. Konfigurieren Sie Ihre Karte stattdessen so, dass sie unter `Scheduled Entry` zu finden ist. Dadurch wird die Karte für die Zielgruppe immer verfügbar sein.

Wenn Sie Ihre Karten im Zeitplan vorab bringen, liegen sie bereit und warten darauf, dass der Nutzer:innen Ihre App öffnet und Karten anfragt.

## Verwenden Sie die Sendelogik "Auf den ersten Eindruck".

Zusammen mit den zeitlich geplanten Sendungen vermeidet die Option `At First Impression` Latenzzeiten, da eine Karte schneller erstellt und in Braze gespeichert wird. Die `At Campaign Launch` erstellt alle Karten für alle segmentierten Nutzer:innen im Voraus, was einige Zeit in Anspruch nehmen kann. Die Option `At First Impression` generiert eine Karte für einen Nutzer:innen, wenn sie zum ersten Mal angefragt wird, z.B. wenn ein Nutzer:innen Ihre App zum ersten Mal öffnet.

Das bedeutet, dass die Karten zusammen mit dem geplanten Eingang sofort verfügbar sind, sobald Sie sie benötigen, entweder zu Beginn der Sitzung oder für ein zeitbasiertes Berechtigungsfenster.

## Denken Sie daran, dass der Eingang in Canvas eine Voraussetzung für den Erhalt von Karten ist.

Denken Sie bei der Verwendung von Canvas daran, dass ein Nutzer:innen zunächst auf der Grundlage der von Ihnen konfigurierten Eingangskriterien in das Canvas eintreten muss und *dann* den Nachrichten-Schritt Ihrer Content-Card durchlaufen muss. Erst dann wird die Karte für Ihre App oder Website verfügbar sein. Denken Sie daran, dass die Karte erst erstellt wird, wenn der Nutzer:innen den Schritt durchläuft, und dass es zu einer Verzögerung kommen kann, wenn die Karte verfügbar ist.

## Aktualisieren Sie die Karten nicht übermäßig

Content-Cards werden vom SDK bei jedem neuen Sitzungsstart automatisch aktualisiert. Sie können während einer aktiven Sitzung auch jederzeit manuell eine Aktualisierung der Content-Cards anfragen.

Wenn Sie die Methode `requestContentCardsRefresh` aufrufen und zu häufig aktualisieren, kann dies zu Rate-Limiting führen. Wenn Ihre App vorübergehend eine Rate-Limitierung erfährt, können Sie die Karten bei Bedarf oder zu einem kritischen Zeitpunkt des Engagements des Nutzers:innen in Ihrer App nicht mehr aktualisieren.

Um dies zu verhindern, rufen Sie diese Aktualisierungsmethode nur zu wichtigen Zeitpunkten im Lebenszyklus des Nutzers auf, z.B. nachdem ein Nutzer:in einen Kauf getätigt hat oder nachdem ein Nutzer:in sein Abo upgegradet hat.

## Vermeiden Sie Connected-Content

Connected-Content reichert Content-Cards mit First-Party- oder Drittanbieter-API-Daten an. Wenn sie jedoch in einer Content-Card Nachricht enthalten ist, blockiert sie die Verfügbarkeit der Karte, bis die Anfrage des Connected-Content-Netzwerks abgeschlossen werden kann. In einigen Fällen führt dies dazu, dass SDKs es ein paar Sekunden später erneut versuchen, um die Rendering-Logik Ihrer App nicht zu verzögern, die möglicherweise darauf wartet, dass das SDK seine Aktualisierungsaufgabe abschließt.

Wenn Sie Connected-Content verwenden müssen, bringen Sie diese Karten im Voraus in den Zeitplan ein und verwenden Sie die Option `At Campaign Launch`, damit die Karten bereits vor der nächsten Sitzung eines Nutzers:innen erstellt werden. Beachten Sie, dass diese Karten nicht sofort verfügbar sein werden, da Braze alle Karten für alle berechtigten Nutzer:innen schreibt.

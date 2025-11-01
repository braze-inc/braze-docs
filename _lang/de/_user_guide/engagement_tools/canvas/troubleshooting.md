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
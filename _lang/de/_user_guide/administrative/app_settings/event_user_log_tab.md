---
nav_title: Event-Benutzerprotokoll
article_title: Event-Nutzerprotokoll
page_order: 7
page_type: reference
description: "Dieser Referenzartikel behandelt das Event-Nutzerprotokoll, das Ihnen bei der Fehlersuche und Fehlerbehebung in Ihrer Braze Integration helfen kann."

---

# Event-Nutzerprotokoll

> Das Event-Nutzerprotokoll kann Ihnen dabei helfen, Probleme in Ihrer Braze Integration aufzuschlüsseln, zu debuggen oder anderweitig zu beheben. Auf dieser Registerkarte finden Sie ein Fehlerprotokoll, in dem die Art des Fehlers, die zugehörige Anwendung, der Zeitpunkt des Auftretens und oft auch die Rohdaten des Fehlers angezeigt werden.

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze Learning-Kurs [Qualitätssicherung und Debugging-Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), in dem Sie lernen, wie Sie das Ereignisbenutzerprotokoll für Ihre eigene Fehlersuche und -behebung verwenden können.
{% endalert %}

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Event-Nutzerprotokoll.**

Um Ihre Protokolle leicht zu finden, können Sie nach folgenden Kriterien filtern:

* SDK oder API
* App-Namen
* Zeitrahmen
* Nutzer:in

Jedes Protokoll ist in mehrere Abschnitte unterteilt, die Folgendes enthalten können:

* Geräteattribute
* Nutzerattribute
* Events
* Kampagnen-Events
* Antwortdaten

Wählen Sie das Symbol **Daten erweitern** aus, um die JSON-Rohdaten für dieses bestimmte Protokoll anzuzeigen.

![Das Symbol "Daten erweitern" neben einem bestimmten Protokoll.]({% image_buster /assets/img_archive/expand_data.png %})

Event-Nutzerprotokolle bleiben 30 Tage lang im Dashboard, nachdem sie protokolliert wurden.

![Rohprotokolle für Ereignisse]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Fehlersuche

### Fehlende SDK-Protokolle für Testbenutzer

Wenn Sie eine:n Nutzer:in zu einer internen Gruppe hinzugefügt haben, diese:r aber keine SDK-Protokolle im Event-Nutzerprotokoll anzeigt, kann dies an einer fehlenden Konfigurationsoption liegen. Um SDK-Protokolle zu erfassen, stellen Sie sicher, dass die Option **Benutzerereignisse für Gruppenmitglieder aufzeichnen** in den **Internen Gruppeneinstellungen** für diese [interne Gruppe]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) aktiviert ist.

### Verzögerung bei der Aktualisierung von Protokollen

Dies ist möglicherweise eine normale Langsamkeit unserer API.

Wenn Sie SDK-Methoden aufrufen, speichert das SDK diese Events in der Regel lokal und gibt sie alle 10 Sekunden an den Server weiter. Es kann zwischen einer Sekunde und einigen Minuten dauern, bis unsere Warteschlange für die Auftragsverarbeitung Events aufnimmt, je nachdem, wie hoch die Gesamtlast zu diesem Zeitpunkt ist.  

Wenn Sie möchten, dass Events so schnell wie möglich eintreffen, versuchen Sie, die Funktion `requestImmediateDataFlush()` aufzurufen.

### Sitzungsende und Sitzungsbeginn haben ähnliche Zeitstempel (iOS)

Das Event-Nutzerprotokoll zeigt den Zeitstempel an, zu dem Braze über das Ende der Sitzung informiert wurde. Das sind Millisekunden, bevor die nächste Sitzung beginnt. Braze kann nicht wissen, dass die Sitzung beendet ist, bevor die App wieder geöffnet wird, da iOS die Ausführung von Threads aggressiv stoppt, wenn die App im Hintergrund läuft. Daher können keine Daten an Braze übertragen werden, bevor die App wieder geöffnet wird.

Während die Endzeit der Sitzung als Sekunden vor dem Beginn der Sitzung angegeben wird, wird die Sitzungsdauer beim Flushen des Events separat gespült und entspricht der korrekten Zeit, zu der die App geöffnet war. Daher hat dieses Verhalten keine Auswirkungen auf den Filter `Median Session Duration`.

In Bezug auf Nutzersitzungen können Sie Braze verwenden, um Daten wie diese zu überwachen:

- Wie viele Sitzungen ein Benutzer gehabt hat
- Wann ein Benutzer zuletzt eine Sitzung gestartet hat
- Wenn der Benutzer nach Erhalt einer Kampagne eine Sitzung startet
- Wie hoch die durchschnittliche Sitzungsdauer der Nutzerin oder des Nutzers ist

Diese Verhaltensweisen werden nicht dadurch beeinflusst, dass das Sitzungsende-Event bei der nächsten Sitzung gespült wird.


---
nav_title: Event-Benutzerprotokoll
article_title: Event-Benutzerprotokoll
page_order: 7
page_type: reference
description: "Dieser Referenzartikel behandelt das Event-Benutzerprotokoll, das Ihnen bei der Fehlersuche und Fehlerbehebung in Ihrer Braze Integration helfen kann."

---

# Event-Benutzerprotokoll

> Das Event-Benutzerprotokoll kann Ihnen dabei helfen, Probleme in Ihrer Braze Integration aufzuschlüsseln, zu debuggen oder anderweitig zu beheben. Auf diesem Tab finden Sie ein Fehlerprotokoll, in dem die Art des Fehlers, die zugehörige App, der Zeitpunkt des Auftretens und oft auch eine Möglichkeit zur Anzeige der zugehörigen Rohdaten aufgeführt werden.

{% alert tip %}
Zusätzlich zu diesem Artikel empfehlen wir Ihnen auch unseren Braze-Lernkurs [Qualitätssicherung und Debugging-Tools](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), in dem Sie lernen, wie Sie das Event-Benutzerprotokoll für Ihre eigene Fehlerbehebung und Ihr Debugging verwenden können.
{% endalert %}

Um auf das Protokoll zuzugreifen, gehen Sie zu **Einstellungen** > **Event-Benutzerprotokoll**.

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

![Das Symbol „Daten erweitern" neben einem bestimmten Protokoll.]({% image_buster /assets/img_archive/expand_data.png %})

Event-Benutzerprotokolle bleiben 30 Tage lang im Dashboard, nachdem sie protokolliert wurden.

![Rohprotokolle für Events]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Fehlerbehebung

### Fehlende SDK-Protokolle für Testnutzer:innen

Wenn Sie eine:n Nutzer:in zu einer internen Gruppe hinzugefügt haben, aber keine SDK-Protokolle im Event-Benutzerprotokoll angezeigt werden, kann dies an einer fehlenden Konfigurationsoption liegen. Um SDK-Protokolle zu erfassen, stellen Sie sicher, dass die Option **Nutzer:innen-Events für Gruppenmitglieder aufzeichnen** in den **Internen Gruppeneinstellungen** für diese [interne Gruppe]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) aktiviert ist.

### Verzögerung bei der Aktualisierung von Protokollen

Dies ist möglicherweise eine normale Verzögerung seitens unserer API.

Wenn Sie SDK-Methoden aufrufen, speichert das SDK diese Events in der Regel lokal zwischen und überträgt sie alle 10 Sekunden an den Server. Es kann zwischen einer Sekunde und einigen Minuten dauern, bis unsere Warteschlange für die Auftragsverarbeitung Events aufnimmt, je nachdem, wie hoch die Gesamtlast zu diesem Zeitpunkt ist.  

Wenn Sie möchten, dass Events so schnell wie möglich eintreffen, versuchen Sie, die Funktion `requestImmediateDataFlush()` aufzurufen.

### Fehler bei der Anzeige von In-App-Nachrichten

Wenn eine In-App-Nachricht nicht angezeigt wird, können Sie den Grund im Event-Benutzerprotokoll finden, indem Sie die JSON-Rohdaten für die entsprechende SDK-Anfrage erweitern und in der Antwort nach dem Feld `error_code` suchen. Der `error_code` gibt den spezifischen Grund für die fehlgeschlagene Impression an (z. B. ein ungültiger Farbwert oder ein Rendering-Problem). Teilen Sie diesen Fehlercode dem [Braze Support]({{site.baseurl}}/braze_support/) mit, falls eine weitere Untersuchung erforderlich ist.

### Sitzungsende und Sitzungsbeginn haben ähnliche Zeitstempel (iOS)

Das Event-Benutzerprotokoll zeigt den Zeitstempel an, zu dem Braze über das Ende der Sitzung informiert wurde. Dieser liegt Millisekunden vor dem Beginn der nächsten Sitzung. Braze kann nicht wissen, dass die Sitzung beendet ist, bevor die App wieder geöffnet wird, da iOS die Ausführung von Threads aggressiv stoppt, wenn die App im Hintergrund läuft – daher können keine Daten an Braze übertragen werden, bevor die App wieder geöffnet wird.

Während die Endzeit der Sitzung als Sekunden vor dem Sitzungsbeginn angegeben wird, wird die Sitzungsdauer beim Übertragen des Events separat gesendet und ist korrekt – sie spiegelt die Zeit wider, in der die App geöffnet war. Daher hat dieses Verhalten keine Auswirkungen auf den Filter `Median Session Duration`.

In Bezug auf Nutzer:innen-Sitzungen können Sie Braze verwenden, um Daten wie diese zu überwachen:

- Wie viele Sitzungen ein:e Nutzer:in gehabt hat
- Wann ein:e Nutzer:in zuletzt eine Sitzung gestartet hat
- Ob der:die Nutzer:in nach Erhalt einer Kampagne eine Sitzung startet
- Wie hoch die durchschnittliche Sitzungsdauer des:der Nutzer:in ist

Diese Verhaltensweisen werden nicht dadurch beeinflusst, dass das Sitzungsende-Event bei der nächsten Sitzung übertragen wird.
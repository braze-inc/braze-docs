---
nav_title: "Vorschau der Nutzer:in"
article_title: Vorschau der Benutzerpfade
page_order: 0.3
alias: /preview_user_paths/
description: "Auf dieser Seite erfahren Sie, wie Sie in Canvas eine Vorschau der Nutzerpfade anzeigen können."
Tool:
  - Canvas
---

# Vorschau der Benutzerpfade in Canvas

> Erleben Sie Canvas so wie Ihre Benutzer. Dazu gehört eine Vorschau auf das Timing und die Nachrichten, die Ihre Nutzer:innen erhalten. Diese Testläufe dienen der Qualitätssicherung, um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden, bevor Sie Ihre Canvas versenden.

## Erstellen eines Testlaufs

Befolgen Sie diese Schritte, um eine Vorschau der User Journey zu erhalten:

1. Gehen Sie zu Ihrem Canvas Builder. Speichern Sie alle nicht gespeicherten Änderungen und beheben Sie alle Fehler.
2. Wählen Sie **Testleinwand** in der Fußzeile.
3. Wählen Sie einen Testbenutzer.
4. (Optional) Wählen Sie einen Empfänger:in für den Test aus.
5. Wählen Sie **Test ausführen**.

Sie können eine Vorschau ausführen, wenn Sie keine Berechtigung zum Bearbeiten eines Canvas haben, aber diese Vorschau wird mit ungespeicherten Änderungen ausgeführt, falls es welche gibt.

### Unterstützte Schritte

Die folgenden Schritte werden unterstützt:
- Nachricht 
- Zielgruppenpfad
- Decision-Split
- Delay
- Aktions-Pfad
- Experiment Pfad
- Nutzer:in Update (nur im UI-Editor, d.h. die Schritte mit dem JSON-Editor werden übersprungen)

Wenn sich der Test mit einem Schritttyp überschneidet, der oben nicht aufgeführt ist, wird der nicht unterstützte Schritt übersprungen, und der Testnutzer:in fährt mit dem nächsten unterstützten Schritt fort.

### Leinwand Schritt Details

Um weitere Details zu den Zulassungskriterien zu sehen, wählen Sie **Mehr anzeigen**. Schritte mit Segmentierung zeigen die erfüllten oder nicht erfüllten Kriterien. Nachrichten zeigen dies auch für Zustellungsvalidierungen und Kanal-Zulässigkeit an. Nachrichtenschritte zeigen, welche Kanäle gesendet bzw. nicht gesendet wurden.

### Liquid

Braze verarbeitet Liquid-Logik während eines Testlaufs, auch wenn Sie keine eigentliche Nachricht senden. Das bedeutet, dass die [Abbruchlogik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) und andere Liquid-Logiken gespiegelt werden und sich auf die Canvas-Benutzerführung auswirken können.

Wenn Ihre Vorschau den letzten Schritt der User Journey sendet, anstatt abzubrechen, verwendet die Vorschau möglicherweise die aktuelle Zeit als Testzeit für Liquid und nicht den tatsächlichen Zeitpunkt, an dem sich der Benutzer gemäß Canvas-Entryzeit in diesem Schritt befinden würde.

## Vorschauen zur zeitlichen Planung

Bei geplanten Canvase betritt der Testnutzer:in zur nächsten geplanten Eintrittszeit. Bei aktionsbasierten Canvase mit Startterminen gibt der Testnutzer:in zum Startdatum und zur Startzeit ein. 

Während die Standard-Startzeiten weiterhin gelten, ist die Eintrittszeit in allen Instanzen konfigurierbar, d.h. Sie können ein Datum in der Vergangenheit oder in der Zukunft simulieren. Sie können jedoch keine Tests vor dem Startdatum oder nach dem Enddatum des Canvas durchführen.

Die Schritte "Nachricht" und "Verzögerung" geben den Zeitpunkt an, zu dem der Benutzer die Nachricht weiterleiten oder empfangen würde, ohne dass die Verzögerungen neu konfiguriert werden müssen. Beachten Sie, dass die Schritte zwar anzeigen, ob Intelligentes Timing verwendet wird, diese Vorschau des Benutzerpfads jedoch keine Schätzung für einen Testnutzer:in berechnet.

Bei Canvase mit einem Aktionsauslöser wie "Änderung des Werts eines angepassten Attributs" versucht Braze, die Änderung zu simulieren, indem das Attribut des Nutzers im Auslöser **nur für den Testlauf des Canvas** vorübergehend leer gesetzt wird (dies wirkt sich nicht auf das Nutzerprofil aus). Damit soll getestet werden, ob sich das Attribut gegenüber seinem aktuellen Wert ändert.

## Ein- und Ausstieg von Benutzern

Testnutzer:in nehmen an der Vorschau teil, auch wenn sie im wirklichen Leben nicht teilnahmeberechtigt sind. Wenn sie nicht in Frage kommen, können Sie sehen, warum sie die Kriterien nicht erfüllt haben. Wenn ein Testnutzer:in die Vorschau eintritt, gehen wir davon aus, dass der Testnutzer:in die Targeting-Kriterien passt und die Kriterien zum Auslösen der Aktion erfüllt. Bei einem Canvas, das angepasste Events in den Eingangskriterien verwendet, wird beispielsweise davon ausgegangen, dass der Testnutzer:in den Eingangskriterien das angepasste Event wie erwartet ausgeführt hat. Wenn jedoch dasselbe angepasste Event an anderer Stelle im Canvas verwendet wird (z.B. bei den Ausstiegskriterien), sollten Sie bedenken, wie sich dies auf den Pfad Ihrer Nutzer:innen auswirken könnte.

Ereignisse, API-Auslöser, angepasste Attribute und Canvas-Eingangs-Eigenschaften, von denen angenommen wird, dass sie einen Testbenutzer in das Canvas eintreten lassen, werden im tatsächlichen Benutzerprofil nicht aktualisiert und bleiben auch nicht über den Testlauf hinaus bestehen. Wenn zum Beispiel beim Test ein angepasstes Attribut als Canvas-Trigger verwendet wird, werden die Triggerkriterien so auf die Nutzervorschau angewendet, **als wäre** die Änderung des angepassten Attributs getriggert worden.

### Betrachtung

Wenn Sie einen Aktions-Pfad mit Aktionen testen, die Exit-Kriterien (einschließlich Event-Eigenschaften) entsprechen, wird das Exit-Kriterium ausgelöst und der Testlauf endet. Wenn Sie einen Nachrichtenschritt testen, der den Ausstiegskriterien entspricht, wird das Ausstiegskriterium getriggert und der Testlauf endet. 

Aktuell können Sie keine bestimmten Ereignisse oder Eigenschaften innerhalb von Aktionspfaden auswählen, um Ausstiegskriterien auszulösen (nur den kompletten Pfad). Erfüllt ein Benutzer potenziell mehrere Ausstiegskriterien, wird das erste, das verarbeitet wird und das er erfüllt, als Ergebnis angezeigt.

## Experimentierpfade und Canvas-Varianten

- Bei Canvases mit übergeordneten Varianten wählen Sie zu Beginn des Tests eine Variante aus.
- Wählen Sie für Experimentierpfade die Variante aus, die der Benutzer durchläuft, wenn der Testbenutzer auf den Schritt stößt.
- Bei Experimentierpfaden, die den personalisierten Pfad oder die Gewinnvariante verwenden, gibt es zwar eine Verzögerungszeit, in der der Testbenutzer in einem Meldungsschritt wartet, aber diese Verzögerung wird nicht berücksichtigt, da Braze davon ausgeht, dass der Benutzer die ausgewählte Variante sofort durchlaufen hat.

## Test sendet

Sie haben die Möglichkeit, Testnachrichten an eine interne Testgruppe oder einzelne Benutzer zu senden, während der Testlauf gefüllt wird. Das bedeutet, dass nur Nachrichten gesendet werden, auf die der Nutzer:in auf dem Testpfad trifft. Die Empfänger erhalten die Nachrichten standardmäßig mit ihren Attributen, aber Sie können diese mit den Attributen des Testnutzers:in überschreiben.

Um alle Nachrichten in einem Canvas auf einmal zu senden, unabhängig vom Pfad und ohne Vorschau des Pfades, können Sie auf der Registerkarte **Testversand** die Option **Alle Nachrichten senden** auswählen.

## Reaktionsfähigkeit

Canvas-Schritte reagieren bei der Vorschau von Benutzerpfaden auf das Timing. Updates, die über den Schritt Benutzer-Update vorgenommen werden, werden in den nachfolgenden Schritten des Ablaufs berücksichtigt, aber nicht auf das eigentliche Nutzerprofil angewendet. Die Auswirkungen der Eingabe einer Variante durch einen Benutzer spiegeln sich in zukünftigen Schritten in einer Vorschau wider.

In ähnlicher Weise erkennen Filter Aktionen, die durch die Interaktion des Testnutzers:in mit anderen Schritten im Canvas entstanden sind. Dieser Vorschau-Modus erkennt zum Beispiel, dass ein Nutzer:in auf eine Nachricht gestoßen ist, die zuvor im Canvas "gesendet" wurde, und er erkennt, dass der Testnutzer:in "Aktion" getreten ist, um einen Aktions-Pfad voranzubringen.

Weitere Einzelheiten zum reaktionsschnellen Verhalten finden Sie unter [Ausstiegskriterien]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria).

## Connected-Content

Connected-Content wird ausgeführt, wenn er im Canvas enthalten ist. Das heißt: Wenn Sie ein Canvas testen, das Connected-Content-Aufrufe oder Content-Blöcke mit Connected-Content enthält, kann das Canvas die Connected-Content-Aufrufe senden. Dadurch werden die Daten, die in anderen Kampagnen oder Canvasen referenziert werden, verändert.

Denken Sie bei der Vorschau von Benutzerpfaden daran, solchen Connected-Content zu entfernen, der Nutzerprofile oder Daten verändert, die in anderen Canvasen oder Kampagnen referenziert werden.

## Webhooks

Webhooks werden ausgeführt, wenn Testnachrichten gesendet werden, aber nicht während des Testlaufs. Ähnlich wie bei Connected-Content sollten Sie Webhooks entfernen, die Nutzerprofile oder Daten verändern, die in anderen Canvasen oder Kampagnen referenziert werden.

## Anwendungsfall

In diesem Szenario wird das Canvas so eingerichtet, dass es Nutzer anspricht, die noch keine Sitzung in einer App hatten. Diese Journey enthält einen Nachrichtenschritt mit einer Begrüßungsmail, eine Verzögerung um einen Tag und den Schritt "Zielgruppenpfade", der sich wiederum in zwei Pfade gliedert: Benutzer mit mindestens einer Sitzung und alle anderen. Je nachdem, in welchen Zielgruppen-Pfad ein Nutzer:innen fällt, wird der nachfolgende Schritt Nachricht gesendet.

![Ein Beispiel für ein Canvas mit einem Nachrichten-Schritt, einem Verzögerungs-Schritt, einem Zielgruppen-Pfad-Schritt und zwei Nachrichten-Schritten.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Da der Testbenutzer die Zulassungskriterien für den Canvas erfüllt, kann er diesen betreten und die User Journey durchlaufen. Da unser Testnutzer:in jedoch die App seit einem Kalendertag nicht mehr geöffnet hat, setzt er den Weg über "Alle anderen" fort und erhält eine Push-Benachrichtigung, in der steht: "Letzte Chance! Erledigen Sie Ihre erste Aufgabe und erhalten Sie einen exklusiven Bonus."

![Der Abschnitt "Testergebnisse" zeigt an, dass der Testnutzer:in die Eingabekriterien erfüllt hat, und bietet eine Zusammenfassung seiner Reise, einschließlich der Schritte, die er gesendet wurde.]({% image_buster /assets/img/preview_user_path_results_example.png %})

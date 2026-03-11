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

> Erleben Sie Canvas so wie Ihre Benutzer. Dies umfasst die Vorschau des Zeitpunkts und der Nachrichten, die Ihre Nutzer:innen erhalten. Diese Testläufe dienen der Qualitätssicherung, um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden, bevor Sie Ihre Canvas versenden.

## Erstellen eines Testlaufs

Befolgen Sie diese Schritte, um eine Vorschau der User Journey zu erhalten:

1. Gehen Sie zu Ihrem Canvas Builder. Speichern Sie alle nicht gespeicherten Änderungen und beheben Sie alle Fehler.
2. Wählen Sie **Testleinwand** in der Fußzeile.
3. Wählen Sie einen Testbenutzer.
4. (Optional) Wählen Sie einen Empfänger:in für den Test aus.
5. Wählen Sie **Test ausführen**.

Sie können eine Vorschau anzeigen, wenn Sie keine Berechtigung zum Bearbeiten eines Canvas haben. Diese Vorschau wird jedoch mit ungespeicherten Änderungen angezeigt, sofern solche vorhanden sind.

### Unterstützte Schritte

Die folgenden Schritte werden unterstützt:
- Nachricht 
- Zielgruppenpfad
- Decision-Split
- Delay
- Aktions-Pfad
- Experiment Pfad
- Nutzer-Update (nur im UI-Editor, d. h. Schritte mit dem JSON-Editor werden übersprungen)

Wenn sich der Test mit einem Schritt überschneidet, der oben nicht aufgeführt ist, wird der nicht unterstützte Schritt übersprungen, und der Testnutzer:in fährt mit dem nächsten unterstützten Schritt fort.

### Leinwand Schritt Details

Um weitere Details zu den Zulassungskriterien auszuwählen, wählen Sie **bitte „Mehr anzeigen**“. Die Schritte mit Segmentierung zeigen die erfüllten oder nicht erfüllten Kriterien an. Nachrichten zeigen dies auch für Validierungen der Zustellung und Kanalberechtigung an. Die Nachrichtenschritte zeigen an, welche Kanäle gesendet wurden und welche nicht.

### Liquid

Braze verarbeitet Liquid Logic während eines Testlaufs, auch wenn Sie keine tatsächliche Testnachricht senden. Das bedeutet, dass die [Abbruchlogik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) und andere Liquid-Logiken gespiegelt werden und sich auf die Canvas-Benutzerführung auswirken können.

Wenn Ihre Vorschau den letzten Schritt der User Journey sendet, anstatt abzubrechen, verwendet die Vorschau möglicherweise die aktuelle Zeit als Testzeit für Liquid und nicht den tatsächlichen Zeitpunkt, an dem sich der Benutzer gemäß Canvas-Entryzeit in diesem Schritt befinden würde.

## Vorschauen zur zeitlichen Planung

Bei geplanten Canvases betritt der Testnutzer:in das System zur nächsten geplanten Eintrittszeit im Zeitplan. Bei aktionsbasierten Canvases mit Startdaten gibt der Testnutzer:in das Startdatum und die Startzeit ein. 

Die Standard-Startzeiten gelten weiterhin, jedoch kann die Eintrittszeit in allen Instanzen konfiguriert werden, was bedeutet, dass Sie ein Datum in der Vergangenheit oder Zukunft simulieren können. Es ist jedoch nicht möglich, vor dem Startdatum oder nach dem Enddatum für Canvas zu testen.

Die Schritte "Nachricht" und "Verzögerung" geben den Zeitpunkt an, zu dem der Benutzer die Nachricht weiterleiten oder empfangen würde, ohne dass die Verzögerungen neu konfiguriert werden müssen. Bitte beachten Sie, dass die Schritte zwar angeben, ob intelligentes Timing verwendet wird, diese Vorschau des Benutzerpfads jedoch keine Schätzung für einen Testnutzer:in berechnet.

Bei Canvases mit einem Aktionsauslöser wie „Änderung des benutzerdefinierten Attributwerts“ versucht Braze, die Änderung zu simulieren, indem das Attribut des Nutzers im Auslöser vorübergehend **nur für den Testlauf des Canvas** auf leer gesetzt wird (dies hat keine Auswirkungen auf das Nutzerprofil). Dies dient dazu, zu überprüfen, ob sich das Attribut von seinem aktuellen Wert ändert.

## Ein- und Ausstieg von Benutzern

Testnutzer:innen erhalten Zugang zur Vorschau, auch wenn sie in der Realität nicht berechtigt sind. Wenn sie nicht in Frage kommen, können Sie sehen, warum sie die Kriterien nicht erfüllt haben. Wenn ein Testnutzer:in die Vorschau eintritt, gehen wir davon aus, dass der Testnutzer:in die Targeting-Kriterien passt und die Kriterien zum Auslösen der Aktion erfüllt. Bei einem Canvas, das angepasste Events in den Eingangskriterien verwendet, wird beispielsweise davon ausgegangen, dass der Testnutzer:in den Eingangskriterien das angepasste Event wie erwartet ausgeführt hat. Wenn jedoch dasselbe angepasste Event an anderer Stelle im Canvas verwendet wird (z.B. bei den Ausstiegskriterien), sollten Sie bedenken, wie sich dies auf den Pfad Ihrer Nutzer:innen auswirken könnte.

Ereignisse, API-Trigger, benutzerdefinierte Attribute und Canvas-Eingangs-Eigenschaften, die es einem Testbenutzer ermöglichen sollen, das Canvas aufzurufen, werden im tatsächlichen Benutzerprofil nicht aktualisiert und bleiben nach dem Testlauf nicht erhalten. Wenn zum Beispiel beim Test ein angepasstes Attribut als Canvas-Trigger verwendet wird, werden die Triggerkriterien so auf die Nutzervorschau angewendet, **als wäre** die Änderung des angepassten Attributs getriggert worden.

### Betrachtung

Wenn Sie einen Aktions-Pfad mit Aktionen testen, die den Abbruchkriterien entsprechen (einschließlich Event-Eigenschaften), werden die Abbruchkriterien getriggert und der Testlauf wird beendet. Wenn Sie einen Nachrichtenschritt testen, der den Abbruchkriterien entspricht, werden die Abbruchkriterien ausgelöst und der Testlauf wird beendet. 

Aktuell können Sie keine bestimmten Ereignisse oder Eigenschaften innerhalb von Aktionspfaden auswählen, um Ausstiegskriterien auszulösen (nur den kompletten Pfad). Erfüllt ein Benutzer potenziell mehrere Ausstiegskriterien, wird das erste, das verarbeitet wird und das er erfüllt, als Ergebnis angezeigt.

## Experimentierpfade und Canvas-Varianten

- Bei Canvases mit übergeordneten Varianten wählen Sie zu Beginn des Tests eine Variante aus.
- Wählen Sie für Experimentierpfade die Variante aus, die der Benutzer durchläuft, wenn der Testbenutzer auf den Schritt stößt.
- Bei Experimentierpfaden, die den personalisierten Pfad oder die Gewinnvariante verwenden, gibt es zwar eine Verzögerungszeit, in der der Testbenutzer in einem Meldungsschritt wartet, aber diese Verzögerung wird nicht berücksichtigt, da Braze davon ausgeht, dass der Benutzer die ausgewählte Variante sofort durchlaufen hat.

## Test sendet

Sie haben die Möglichkeit, Testnachrichten an eine interne Testgruppe oder einzelne Benutzer zu senden, während der Testlauf gefüllt wird. Dies bedeutet, dass nur Nachrichten gesendet werden, auf die der Nutzer entlang des Testpfads stößt. Die Empfänger:innen erhalten standardmäßig Nachrichten mit ihren Attributen, jedoch können Sie diese mit den Attributen des Testnutzer:in überschreiben.

Um alle Nachrichten in einem Canvas auf einmal zu senden, unabhängig vom Pfad und ohne Vorschau des Pfades, können Sie auf der Registerkarte **Testversand** die Option **Alle Nachrichten senden** auswählen.

## Reaktionsfähigkeit

Canvas-Schritte reagieren bei der Vorschau von Benutzerpfaden auf das Timing. Updates, die über den Schritt Benutzer-Update vorgenommen werden, werden in den nachfolgenden Schritten des Ablaufs berücksichtigt, aber nicht auf das eigentliche Nutzerprofil angewendet. Die Auswirkungen der Eingabe einer Variante durch einen Benutzer spiegeln sich in zukünftigen Schritten in einer Vorschau wider.

Ebenso erkennen Filter Aktionen, die als Ergebnis der Interaktion des Testnutzer:ins mit anderen Canvas-Schritten aufgetreten sind. Dieser Vorschaumodus erkennt beispielsweise, dass ein Nutzer auf einen Schritt mit Nachrichten gestoßen ist, der zuvor im Canvas „gesendet“ wurde, und er erkennt, dass der Testnutzer:in „Maßnahmen ergriffen“ hat, um einen Aktions-Pfad voranzubringen.

Weitere Einzelheiten zum reaktionsschnellen Verhalten finden Sie unter [Ausstiegskriterien]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria).

## Connected-Content

Connected-Content wird ausgeführt, wenn er in Canvas enthalten ist. Das heißt: Wenn Sie ein Canvas testen, das Connected-Content-Aufrufe oder Content-Blöcke mit Connected-Content enthält, kann das Canvas die Connected-Content-Aufrufe senden. Dadurch werden die Daten, die in anderen Kampagnen oder Canvasen referenziert werden, verändert.

Denken Sie bei der Vorschau von Benutzerpfaden daran, solchen Connected-Content zu entfernen, der Nutzerprofile oder Daten verändert, die in anderen Canvasen oder Kampagnen referenziert werden.

## Webhooks

Webhooks werden ausgeführt, wenn Testnachrichten gesendet werden, jedoch nicht während des Testlaufs. Ähnlich wie bei Connected-Content sollten Sie Webhooks entfernen, die Nutzerprofile oder Daten verändern, die in anderen Canvasen oder Kampagnen referenziert werden.

## Anwendungsfall

In diesem Szenario wird das Canvas so eingerichtet, dass es Nutzer anspricht, die noch keine Sitzung in einer App hatten. Diese Journey enthält einen Nachrichtenschritt mit einer Begrüßungsmail, eine Verzögerung um einen Tag und den Schritt "Zielgruppenpfade", der sich wiederum in zwei Pfade gliedert: Benutzer mit mindestens einer Sitzung und alle anderen. Je nachdem, in welchen Zielgruppen-Pfad eine Nutzer:in fällt, wird der nachfolgende Nachrichtenschritt gesendet.

![Ein Beispiel für ein Canvas mit einem Nachrichten-Schritt, einem Verzögerungs-Schritt, einem Zielgruppen-Pfad-Schritt und zwei Nachrichten-Schritten.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Da der Testbenutzer die Zulassungskriterien für den Canvas erfüllt, kann er diesen betreten und die User Journey durchlaufen. Da unser Testnutzer:in die App jedoch im letzten Kalendertag nicht geöffnet hat, wird er weiterhin über den Pfad „Alle anderen“ weitergeleitet und erhält eine Push-Benachrichtigung mit folgendem Text: "Letzte Chance! Erledigen Sie Ihre erste Aufgabe und erhalten Sie einen exklusiven Bonus."

![Der Abschnitt „Testergebnisse“ zeigt, dass die Testnutzer:innen die Teilnahmekriterien erfüllt haben, und enthält eine Zusammenfassung ihres Weges, einschließlich der Schritte, die sie durchlaufen haben.]({% image_buster /assets/img/preview_user_path_results_example.png %})

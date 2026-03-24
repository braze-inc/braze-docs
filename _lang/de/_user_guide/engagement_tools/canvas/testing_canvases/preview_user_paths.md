---
nav_title: Vorschau der Nutzerpfade
article_title: Vorschau der Nutzerpfade
page_order: 0.3
alias: /preview_user_paths/
description: "Auf dieser Seite erfahren Sie, wie Sie in Canvas eine Vorschau der Nutzerpfade anzeigen können."
Tool:
  - Canvas
---

# Vorschau der Nutzerpfade in Canvas

> Erleben Sie die Canvas-Journey, die Sie für Ihre Nutzer:innen erstellt haben. Dies umfasst die Vorschau des Timings und der Nachrichten, die Ihre Nutzer:innen erhalten. Diese Testläufe dienen der Qualitätssicherung, um sicherzustellen, dass Ihre Nachrichten an die richtige Zielgruppe gesendet werden – noch bevor Sie Ihr Canvas versenden.

## Erstellen eines Testlaufs

Befolgen Sie diese Schritte, um eine Vorschau der User Journey zu erhalten:

1. Gehen Sie zu Ihrem Canvas Builder. Speichern Sie alle nicht gespeicherten Änderungen und beheben Sie alle Fehler.
2. Wählen Sie **Test Canvas** in der Fußzeile.
3. Wählen Sie eine:n Testnutzer:in aus.
4. (Optional) Wählen Sie eine:n Empfänger:in für den Test aus.
5. Wählen Sie **Test ausführen**.

Sie können eine Vorschau anzeigen, auch wenn Sie keine Berechtigung zum Bearbeiten eines Canvas haben. Diese Vorschau wird jedoch mit nicht gespeicherten Änderungen ausgeführt, sofern solche vorhanden sind.

### Unterstützte Schritte

Die folgenden Schritte werden unterstützt:
- Nachricht 
- Zielgruppenpfad
- Decision-Split
- Delay
- Aktions-Pfad
- Experiment-Pfad
- Nutzer-Update (nur im UI-Editor, d. h. Schritte mit dem JSON-Editor werden übersprungen)

Wenn der Test auf einen Schritttyp trifft, der oben nicht aufgeführt ist, wird der nicht unterstützte Schritt übersprungen, und die/der Testnutzer:in fährt mit dem nächsten unterstützten Schritt fort.

### Canvas-Schritt-Details

Um weitere Details zu den Eingangskriterien anzuzeigen, wählen Sie **Mehr anzeigen**. Schritte mit Segmentierung zeigen die erfüllten oder nicht erfüllten Kriterien an. Nachrichten zeigen dies auch für Zustellungsvalidierungen und Kanalberechtigung an. Nachrichtenschritte zeigen an, welche Kanäle gesendet wurden und welche nicht.

### Liquid

Braze verarbeitet Liquid-Logik während eines Testlaufs, auch wenn Sie keine tatsächliche Testnachricht senden. Das bedeutet, dass die [Abbruchlogik für Nachrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) und andere Liquid-Logik berücksichtigt werden und sich auf die Canvas-User-Journey auswirken können.

Wenn Ihre Vorschau den letzten Schritt der User Journey sendet, anstatt abzubrechen, verwendet die Vorschau möglicherweise die aktuelle Zeit als Testzeit für die Liquid-Auswertung und nicht den tatsächlichen Zeitpunkt, zu dem sich die/der Nutzer:in basierend auf der Canvas-Eintrittszeit in diesem Schritt befinden würde.

## Vorschauen für das Timing

Bei geplanten Canvasen tritt die/der Testnutzer:in zur nächsten geplanten Eintrittszeit ein. Bei aktionsbasierten Canvasen mit Startdaten tritt die/der Testnutzer:in zum Startdatum und zur Startzeit ein. 

Die Standard-Startzeiten gelten weiterhin, jedoch ist die Eintrittszeit in allen Fällen konfigurierbar, sodass Sie ein Datum in der Vergangenheit oder Zukunft simulieren können. Es ist jedoch nicht möglich, vor dem Startdatum oder nach dem Enddatum des Canvas zu testen.

Nachrichten- und Delay-Schritte zeigen den Zeitpunkt an, zu dem eine:r Nutzer:in weitergeleitet wird oder die Nachricht erhält, ohne dass die Verzögerungen neu konfiguriert werden müssen. Bitte beachten Sie, dass die Schritte zwar angeben, ob intelligentes Timing verwendet wird, diese Vorschau des Nutzerpfads jedoch keine Schätzung für eine:n Testnutzer:in berechnet.

Bei Canvasen mit einem Aktions-Trigger wie „Änderung des angepassten Attributwerts" versucht Braze, die Änderung zu simulieren, indem das Attribut der/des Nutzer:in im Trigger vorübergehend auf leer gesetzt wird – **nur für den Testlauf des Canvas** (dies hat keine Auswirkungen auf das Nutzerprofil). Dies dient dazu, zu überprüfen, ob sich das Attribut von seinem aktuellen Wert ändert.

## Ein- und Ausstieg von Nutzer:innen

Testnutzer:innen erhalten Zugang zur Vorschau, auch wenn sie in der Realität nicht berechtigt sind. Wenn sie nicht berechtigt sind, können Sie sehen, warum sie die Kriterien nicht erfüllt haben. Wenn eine:r Testnutzer:in die Vorschau betritt, gehen wir davon aus, dass die/der Testnutzer:in die Zielgruppenkriterien erfüllt und die Aktions-Trigger-Kriterien ausgeführt hat. Bei einem Canvas, das angepasste Events in den Eingangskriterien verwendet, wird beispielsweise davon ausgegangen, dass die/der Testnutzer:in das angepasste Event wie erwartet in den Eingangskriterien ausgeführt hat. Wenn jedoch dasselbe angepasste Event an anderer Stelle im Canvas verwendet wird (z. B. in den Ausstiegskriterien), sollten Sie bedenken, wie sich dies auf den Nutzerpfad auswirken könnte.

Events, API-Trigger, angepasste Attribute und Canvas-Eingangs-Eigenschaften, die es einer/einem Testnutzer:in ermöglichen sollen, das Canvas zu betreten, werden im tatsächlichen Nutzerprofil nicht aktualisiert und bleiben nach dem Testlauf nicht erhalten. Wenn zum Beispiel beim Testen ein angepasstes Attribut als Canvas-Trigger verwendet wird, werden die Trigger-Kriterien auf die Vorschau der/des Nutzer:in angewendet, **als ob** die Änderung des angepassten Attributs getriggert worden wäre.

### Hinweis

Wenn Sie einen Aktions-Pfad mit Aktionen testen, die den Ausstiegskriterien entsprechen (einschließlich Event-Eigenschaften), werden die Ausstiegskriterien getriggert und der Testlauf wird beendet. Wenn Sie einen Nachrichtenschritt testen, der den Ausstiegskriterien entspricht, werden die Ausstiegskriterien getriggert und der Testlauf wird beendet. 

Aktuell können Sie kein bestimmtes Event oder keine bestimmte Eigenschaft innerhalb eines Aktions-Pfads auswählen, um Ausstiegskriterien auszulösen (nur den Pfad als Ganzes). Wenn eine:r Nutzer:in potenziell mehrere Ausstiegskriterien erfüllen könnte, wird das erste, das verarbeitet wird und das sie/er erfüllt, als Ergebnis angezeigt.

## Experiment-Pfade und Canvas-Varianten

- Bei Canvasen mit übergeordneten Varianten wählen Sie zu Beginn des Tests eine Variante aus.
- Bei Experiment-Pfaden wählen Sie die Variante aus, die die/der Nutzer:in durchläuft, wenn die/der Testnutzer:in auf den Schritt trifft.
- Bei Experiment-Pfaden, die den personalisierten Pfad oder die Gewinnvariante verwenden, gibt es zwar eine Verzögerungszeit, in der die/der Testnutzer:in in einem Nachrichtenschritt wartet, aber diese Verzögerung wird nicht berücksichtigt, da Braze davon ausgeht, dass die/der Nutzer:in die ausgewählte Variante sofort durchlaufen hat.

## Testversand

Sie haben die Möglichkeit, Testnachrichten an eine interne Testgruppe oder eine:n einzelne:n Nutzer:in zu senden, während der Testlauf ausgeführt wird. Das bedeutet, dass nur Nachrichten gesendet werden, auf die die/der Nutzer:in entlang des Testpfads trifft. Die Empfänger:innen erhalten standardmäßig Nachrichten mit ihren eigenen Attributen, Sie können diese jedoch mit den Attributen der/des Testnutzer:in überschreiben.

Um alle Testnachrichten in einem Canvas auf einmal zu senden – unabhängig vom Pfad und ohne Vorschau des Pfads – können Sie auf dem Tab **Testversand** die Option **Alle Testnachrichten senden** auswählen.

## Reaktionsfähigkeit

Canvas-Schritte reagieren bei der Vorschau von Nutzerpfaden auf das Timing. Updates, die über den Nutzer-Update-Schritt vorgenommen werden, werden in den nachfolgenden Schritten des Ablaufs berücksichtigt, aber nicht auf das tatsächliche Nutzerprofil angewendet. Die Auswirkungen des Eintritts einer/eines Nutzer:in in eine Variante werden in zukünftigen Schritten der Vorschau widergespiegelt.

Ebenso erkennen Filter Aktionen, die als Ergebnis der Interaktion der/des Testnutzer:in mit anderen Canvas-Schritten aufgetreten sind. Dieser Vorschaumodus erkennt beispielsweise, dass eine:r Nutzer:in auf einen Nachrichtenschritt gestoßen ist, der zuvor im Canvas „gesendet" wurde, und er erkennt, dass die/der Testnutzer:in „eine Aktion ausgeführt" hat, um einen Aktions-Pfad voranzubringen.

Weitere Einzelheiten zum reaktionsfähigen Verhalten finden Sie unter [Ausstiegskriterien]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria).

## Connected-Content

Connected-Content wird ausgeführt, wenn er im Canvas enthalten ist. Das heißt: Wenn Sie ein Canvas testen, das Connected-Content-Aufrufe oder Content-Blöcke mit Connected-Content enthält, kann das Canvas die Connected-Content-Aufrufe senden, wodurch die Daten verändert werden könnten, die in anderen Kampagnen oder Canvasen referenziert werden.

Denken Sie bei der Vorschau von Nutzerpfaden daran, Connected-Content zu entfernen, der Nutzerprofile oder Daten verändert, die in anderen Canvasen oder Kampagnen referenziert werden.

## Webhooks

Webhooks werden ausgeführt, wenn Testnachrichten gesendet werden, jedoch nicht während des Testlaufs. Ähnlich wie bei Connected-Content sollten Sie Webhooks entfernen, die Nutzerprofile oder Daten verändern, die in anderen Canvasen oder Kampagnen referenziert werden.

## Kontextvariablen und Seed-Gruppen

Bei einem Nachrichtenschritt mit E-Mail als Messaging-Kanal senden Seed-Gruppen Seed-Kopien von E-Mails, wenn eine:r Nutzer:in diesen Schritt im Canvas erreicht. Diese Seed-Kopien werden nicht als Teil der eigenen Canvas-Journeys der Seed-Gruppen-Empfänger:innen gesendet, daher führt Braze keine [Kontext-Schritte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) aus und wertet keine Kontextvariablen für diese Empfänger:innen aus. Wenn Ihr E-Mail-Inhalt Kontextvariablen referenziert, erhalten die Seed-Gruppen-Empfänger:innen eine Seed-Kopie ohne diese Daten. Um Nachrichten zu testen, die auf Kontextvariablen-Daten angewiesen sind, verwenden Sie die **Test Canvas**-Vorschau mit Testversand anstelle von Seed-Gruppen.

## Anwendungsfall

In diesem Szenario wird das Canvas so eingerichtet, dass es Nutzer:innen anspricht, die keine Sitzung in einer App hatten. Diese Journey enthält einen Nachrichtenschritt mit einer Willkommens-E-Mail, einen Delay-Schritt von einem Tag und einen Zielgruppenpfade-Schritt, der sich in zwei Pfade aufteilt: Nutzer:innen mit mindestens einer Sitzung und alle anderen. Je nachdem, in welchen Zielgruppenpfad eine:r Nutzer:in fällt, wird der nachfolgende Nachrichtenschritt gesendet.

![Ein Beispiel für ein Canvas mit einem Nachrichtenschritt, einem Delay-Schritt, einem Zielgruppenpfade-Schritt und zwei Nachrichtenschritten.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Da unsere:r Testnutzer:in die Canvas-Eingangskriterien erfüllt, kann sie/er das Canvas betreten und die User Journey durchlaufen. Da unsere:r Testnutzer:in die App jedoch am letzten Kalendertag nicht geöffnet hat, wird sie/er über den Pfad „Alle anderen" weitergeleitet und erhält eine Push-Benachrichtigung mit folgendem Text: „Letzte Chance! Erledigen Sie Ihre erste Aufgabe und erhalten Sie einen exklusiven Bonus."

![Der Abschnitt „Testergebnisse" zeigt, dass die/der Testnutzer:in die Eingangskriterien erfüllt hat, und enthält eine Zusammenfassung der Journey, einschließlich der Schritte, die gesendet wurden.]({% image_buster /assets/img/preview_user_path_results_example.png %})
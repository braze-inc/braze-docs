Um die Genauigkeit Ihres Modells zu messen, zeigt Ihnen die Metrik für _die Vorhersagequalität_, wie effektiv dieses bestimmte Modell für maschinelles Lernen zu sein scheint, wenn es mit historischen Daten getestet wird. Braze zieht die Daten entsprechend den Gruppen, die Sie auf der Seite zur Modellerstellung angegeben haben. Das Modell wird anhand eines Datensatzes (dem „Trainingsdatensatz“) trainiert und anschließend anhand eines neuen, separaten Datensatzes (dem „Testdatensatz“) getestet.

Die Vorhersage wird alle zwei Wochen erneut trainiert und zusammen mit der Metrik für _die Vorhersagequalität_ aktualisiert, damit Ihre Vorhersagen immer auf dem neuesten Stand des Nutzerverhaltens sind. Außerdem werden jedes Mal die Vorhersagen der letzten zwei Wochen mit den tatsächlichen Nutzerergebnissen verglichen. Die _Vorhersagequalität_ wird dann anhand dieser realen Ergebnisse (und nicht anhand von Schätzungen) berechnet. Dabei handelt es sich um einen automatischen Backtest (d.h. das Testen eines Vorhersagemodells anhand historischer Daten), um sicherzustellen, dass die Vorhersage in realen Szenarien korrekt ist. Das letzte Mal, dass diese Umschulung und das Backtesting stattgefunden haben, wird auf der Seite **Prognosen** und auf der Analyseseite einer einzelnen Prognose angezeigt. Auch bei einer Vorhersage wird dieser Backtest einmal nach der Erstellung durchgeführt. Auf diese Weise können Sie sich der Genauigkeit Ihrer individuellen Vorhersage sicher sein, selbst mit der kostenlosen Version der Funktion.

{% details Beispiel für die Qualität der Prognosen %}

Wenn beispielsweise 20 % Ihrer Nutzer:innen im Durchschnitt abwandern und Sie eine zufällige Teilmenge von 20 % Ihrer Nutzer:innen auswählen und diese nach dem Zufallsprinzip als abgewandert bezeichnen (unabhängig davon, ob sie es wirklich sind oder nicht), werden Sie voraussichtlich nur 20 % der tatsächlichen Abgewanderten korrekt identifizieren. Das ist reine Spekulation. Wenn das Modell nur so gut funktionieren würde, wäre der Auftrieb in diesem Fall 1.

Wenn das Modell es Ihnen hingegen erlauben würde, 20% der Nutzer anzusprechen und dabei alle "echten" Churners zu erfassen und niemanden sonst, wäre der Lift 100% / 20% = 5. Wenn Sie dieses Verhältnis für jeden Anteil der wahrscheinlichsten Abwanderer, die Sie ansprechen könnten, aufzeichnen, erhalten Sie die [Liftkurve](https://en.wikipedia.org/wiki/Lift_(data_mining)). 

Eine andere Möglichkeit, die Qualität der Steigerung (und auch die _Qualität der Vorhersage_) zu betrachten, ist die Frage, wie weit die Kurve der Prognose bei der Identifizierung von Abgewanderten im Testsatz zwischen zufälligem Raten (0 %) und Perfektion (100 %) liegt. Die Originalarbeit über die Qualität von Steigerungen finden Sie unter [Messung der Qualität der Steigerung im Datenbank-Marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}

### Wie es gemessen wird

Unser Maß für die _Qualität der Vorhersage_ ist die [Aufzugsqualität](https://dl.acm.org/doi/10.1145/380995.381018). Im Allgemeinen referenziert "Lift" den erhöhten Anteil oder Prozentsatz eines erfolgreichen Ergebnisses, wie z.B. einer Konversion. In diesem Fall ist das erfolgreiche Ergebnis die korrekte Identifizierung eines Nutzers oder einer Nutzerin, der oder die abgewandert wäre. Die Qualität der Steigerung ist die durchschnittliche Steigerung, die die Prognose für alle möglichen Zielgruppengrößen für das Messaging des Testsatzes liefert. Dieser Ansatz misst, um wie viel besser als das zufällige Raten das Modell ist. Bei diesem Maß bedeutet 0 %, dass das Modell nicht besser ist als eine zufällige Schätzung, wer abwandern wird, und 100 % bedeutet, dass man genau weiß, wer abwandern wird.

### Empfohlene Bereiche

Hier finden Sie unsere Empfehlungen für verschiedene Bereiche der _Vorhersagequalität_:

| Vorhersagequalität Bereich (%) | Empfehlung |
| ---------------------- | -------------- |
| 60 - 100 | Ausgezeichnet. Größtmögliche Genauigkeit. Es ist unwahrscheinlich, dass eine Änderung der Zielgruppendefinitionen einen zusätzlichen Nutzen bringt. |
| 40 - 60 | Gut. Dieses Modell generiert genaue Prognosen, aber mit anderen Zielgruppeneinstellungen können eventuell noch bessere Ergebnisse erzielt werden. |
| 20 - 40| Ausreichend. Die Genauigkeit und der Nutzen dieses Modells sind recht hoch. Dennoch empfiehlt es sich, andere Zielgruppendefinitionen auszuprobieren, um zu sehen, ob sich die Performance verbessert. |
| 0 - 20 | Schlecht. Ändern Sie die Zielgruppendefinitionen und versuchen Sie es erneut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

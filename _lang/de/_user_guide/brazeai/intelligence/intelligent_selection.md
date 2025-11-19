---
nav_title: Intelligente Auswahl
article_title: Intelligente Auswahl
page_order: 1.0
description: "Dieser Artikel behandelt die Intelligente Auswahl, eine Funktion, die die Leistung einer wiederkehrenden Kampagne oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer, die jede Nachrichtenvariante erhalten, automatisch anpasst."
search_rank: 10
toc_headers: h2
---

# Intelligente Auswahl {#intelligent-selection}

> Intelligente Auswahl ist eine Funktion, die die Leistung einer wiederkehrenden Kampagne oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer, die jede Nachrichtenvariante erhalten, automatisch anpasst. 

## Über Intelligente Auswahl

Eine Variante, die anscheinend besser abschneidet als andere, wird an mehr Nutzer gesendet, während Varianten, die weniger gut abschneiden, an weniger Nutzer gesendet werden. Jede Anpassung erfolgt mithilfe eines [statistischen Algorithmus](https://en.wikipedia.org/wiki/Multi-armed_bandit), der sicherstellt, dass Braze echte Performance-Unterschiede ausgleicht und nicht nur zufällig ist.

![A/B-Tests Abschnitt einer Kampagne mit aktivierter intelligenter Auswahl.]({% image_buster /assets/img/intelligent_selection1.png %})

Intelligente Auswahl wird:
- Schauen Sie sich immer wieder die Performance-Daten an und verlagern Sie den Kampagnen-Traffic allmählich auf die Winning-Varianten.
- Stellen Sie sicher, dass mehr Nutzer Ihre leistungsstärkste Variante erhalten, ohne die statistische Sicherheit zu beeinträchtigen.
- Schließen Sie Varianten mit schlechter Performance aus und identifizieren Sie Varianten mit hoher Performance schneller als bei einem [herkömmlichen A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- Testen Sie häufiger und mit größerer Zuversicht, dass Ihre Nutzer Ihre beste Nachricht sehen. 

Die intelligente Auswahl funktioniert am besten bei Kampagnen, die mehr als einmal gesendet werden. Es benötigt frühe Performance-Daten, um mit der Optimierung zu beginnen, so dass Kampagnen, die nur einmal gesendet werden, nicht davon profitieren. Für diese Kampagnen empfehlen wir Ihnen, stattdessen einen traditionellen [A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) durchzuführen.

## Voraussetzungen

{% tabs %}
{% tab Campaign %}
Bevor Sie die intelligente Auswahl zu Ihrer Kampagne hinzufügen, sollten Sie sicherstellen, dass Sie alles richtig eingerichtet haben:

- Ihre Kampagne sendet nach einem wiederkehrenden Zeitplan. Kampagnen mit einmaliger Versendung werden nicht unterstützt.
- Sie haben mindestens zwei Varianten von Nachrichten hinzugefügt.
- Sie haben ein Konversions-Event definiert, um die Performance von Varianten zu messen.
- Das Zeitfenster für die erneute Anspruchsberechtigung ist auf 24 Stunden oder länger festgelegt. Kürzere Fenster werden nicht unterstützt, da sie die Integrität der Steuerungsvariante beeinträchtigen würden. Wenn Sie mehr erfahren möchten, lesen Sie [diese FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Um die Intelligente Auswahl in einem Canvas zu verwenden, bestätigen Sie Folgendes:
- Ihr Canvas enthält mindestens zwei Varianten von Nachrichten in einem Messaging-Schritt.
- Sie haben mindestens ein Konversions-Event hinzugefügt.
{% endtab %}
{% endtabs %}

## Hinzufügen einer intelligenten Auswahl

Sie können Ihren Kampagnen und Canvase eine intelligente Auswahl hinzufügen.

{% tabs %}
{% tab Campaign %}
Die Intelligente Auswahl kann zu jeder Multi-Send-Kampagne im Schritt **Zielgruppen** des Braze-Kampagnen-Composers hinzugefügt werden. Kampagnen, die nur einmal senden, können dieses Feature nicht nutzen.

{% alert note %}
Die intelligente Auswahl kann nicht in Kampagnen mit einer Wiederzulassungsfrist von weniger als 24 Stunden verwendet werden, da sie die Integrität der Kontrollvariante beeinträchtigen würde. Wenn Sie mehr erfahren möchten, lesen Sie die [Intelligence FAQ]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Fügen Sie mindestens ein Konversions-Event und zwei Varianten zu Ihrem Canvas hinzu. Wählen Sie dann im Schritt Erstellen eine der prozentualen Varianten aus. 

![Ein Canvas mit zwei Varianten, die jeweils auf eine 50%ige Variantenverteilung eingestellt sind und die Aktivierung der intelligenten Auswahl zulassen.]({% image_buster /assets/img/intelligent_selection.png %})

Damit können Sie die Variantenverteilung bearbeiten und die Intelligente Auswahl einschalten. 

![Option "Intelligente Auswahl" für ein Canvas aktiviert]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

Die intelligente Auswahl ist nicht verfügbar, wenn Sie Ihrem Canvas noch keine Conversion-Ereignisse hinzugefügt haben oder wenn Ihre Kampagne aus einer Solo-Variante besteht.
{% endtab %}
{% endtabs %}

## Laufzeit

Bei Kampagnen und Canvase läuft die intelligente Auswahl so lange, bis sie genügend Erkenntnisse über die "wahren" Konversionsraten der Varianten gesammelt hat. "Genug" wird durch eine spezielle Metrik namens "Reue" bestimmt Sie können sich das so vorstellen, dass sich die Intelligente Auswahl von selbst ausschaltet, wenn genügend Daten vorhanden sind, um zu wissen, welche Variante die beste ist. 

In den meisten Fällen wird Intelligent Selection eine der Varianten als Gewinnvariante auswählen. Diese Variante erhält 100% der Hörerschaft für zukünftige Sendungen.

{% alert note %}
Es ist möglich, dass die intelligente Auswahl aufhört zu optimieren, ohne einen einzigen klaren Gewinner auszuwählen. Die intelligente Auswahl stellt die Optimierung ein, wenn sie mit 95%iger Sicherheit davon ausgehen kann, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1% der derzeitigen Rate verbessern wird.
{% endalert %}

## Intelligente Auswahl der Variantenverteilung

Die intelligente Auswahl stützt sich bei der Verteilung der Varianten auf den aktuellen Stand der Konversionen in den Kampagnen. Sie bestimmt nur die endgültigen Verteilungen nach der Trainingsperiode. 

Das bedeutet, dass in der Anfangsphase der Kampagne sowohl die 99%ige als auch die 1%ige Intelligente Auswahl annähernd gleich viele Sendungen erhalten können, aber die endgültigen Prozentsätze für die Zuteilung der Varianten können auf 99%-1% festgelegt werden.

Wenn Sie nicht möchten, dass die intelligente Auswahl in der Anfangsphase der Kampagne 50/50 sendet, empfehlen wir Ihnen, einen traditionellen A/B-Test mit festen Varianten durchzuführen.

## Häufig gestellte Fragen {#faq}

### Warum ist die Wiederzulassung in weniger als 24 Stunden in Kombination mit Intelligent Selection nicht möglich?

Wir lassen nicht zu, dass Kampagnen mit intelligenter Auswahl in einem zu kurzen Zeitfenster wieder wählbar sind, da dies die Integrität der Kontrollvariante beeinträchtigen würde. Indem wir eine Lücke von 24 Stunden schaffen, stellen wir sicher, dass der Algorithmus mit einem statistisch gültigen Datensatz arbeiten kann.

Normalerweise führen Kampagnen mit Wiederwahlmöglichkeit dazu, dass Nutzer:innen dieselbe Variante erneut eingeben müssen, die sie zuvor erhalten haben. Bei der Intelligenten Auswahl kann Braze nicht garantieren, dass ein Benutzer dieselbe Kampagnenvariante erhält, da sich die Variantenverteilung aufgrund des Aspekts der optimalen Zuweisung für diese Funktion verschoben hätte. Wäre es zulässig, dass die Nutzerin oder der Nutzer erneut eintritt, bevor die intelligente Auswahl die Performance der Variante überprüft, könnten die Daten aufgrund der Nutzer:innen, die erneut eintreten, verzerrt sein.

Zum Beispiel, wenn eine Kampagne diese Varianten verwendet:

- Variante A: 20%
- Variante B: 20%
- Kontrolle: 60%

Dann könnte die Variantenverteilung für die zweite Runde wie folgt aussehen:

- Variante A: 15%
- Variante B: 25%
- Kontrolle: 60%

### Warum zeigen meine Intelligent Selection-Varianten in der Anfangsphase meiner Kampagne gleiche Sendungen an?

Die intelligente Auswahl weist Varianten für den Versand auf der Grundlage des aktuellen Status der Konversion der Kampagne zu. Es bestimmt die endgültigen Variantenzuweisungen erst nach einer Trainingsperiode, in der die Sendungen gleichmäßig auf die Varianten verteilt werden. Wenn Sie nicht möchten, dass die Intelligente Auswahl in den frühen Phasen Ihrer Kampagne gleichmäßig sendet, verwenden Sie feste Varianten für einen traditionellen A/B-Test.

### Wird die Intelligente Auswahl aufhören zu optimieren, ohne einen klaren Gewinner zu ermitteln?

Die intelligente Auswahl stellt die Optimierung ein, wenn sie mit 95%iger Sicherheit davon ausgehen kann, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1 % der aktuellen Rate verbessern wird.

### Warum kann ich die intelligente Auswahl in meinem Canvas oder meiner Kampagne nicht aktivieren (ausgegraut)?

Die intelligente Auswahl ist nicht verfügbar, wenn:

- Sie haben keine Konversionsereignisse zu Ihrer Kampagne oder Ihrem Canvas hinzugefügt
- Sie erstellen eine Kampagne, die nur einmal versendet wird
- Sie haben die Wiederholbarkeit mit einem Zeitfenster von weniger als 24 Stunden aktiviert
- Ihr Canvas besteht aus einer einzigen Variante, der keine weiteren Varianten oder Kontrollgruppen hinzugefügt wurden.
- Ihr Canvas besteht aus einer einzigen Kontrollgruppe, der keine Varianten hinzugefügt wurden

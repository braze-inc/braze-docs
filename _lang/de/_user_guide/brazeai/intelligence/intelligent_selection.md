---
nav_title: Intelligente Auswahl
article_title: Intelligente Auswahl
page_order: 1
description: "Dieser Artikel behandelt die Intelligente Auswahl, eine Funktion, die die Leistung einer wiederkehrenden Kampagne oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer, die jede Nachrichtenvariante erhalten, automatisch anpasst."
search_rank: 10
---

# Intelligente Auswahl {#intelligent-selection}

> Intelligente Auswahl ist eine Funktion, die die Leistung einer wiederkehrenden Kampagne oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer, die jede Nachrichtenvariante erhalten, automatisch anpasst. 

Eine Variante, die anscheinend besser abschneidet als andere, wird an mehr Nutzer gesendet, während Varianten, die weniger gut abschneiden, an weniger Nutzer gesendet werden. Jede Anpassung wird mit einem [statistischen Algorithmus][227] vorgenommen, der sicherstellt, dass wir echte Performance-Unterschiede berücksichtigen und nicht nur zufällige.

![Abschnitt A/B-Tests einer Kampagne mit aktivierter Intelligenter Auswahl.][3]

Intelligente Auswahl wird:
- Schauen Sie sich immer wieder die Performance-Daten an und verlagern Sie den Kampagnen-Traffic allmählich auf die Winning-Varianten.
- Stellen Sie sicher, dass mehr Nutzer Ihre leistungsstärkste Variante erhalten, ohne die statistische Sicherheit zu beeinträchtigen.
- Schließen Sie Varianten mit schlechter Performance aus und identifizieren Sie Varianten mit hoher Performance schneller als bei einem [herkömmlichen A/B-Test][1].
- Testen Sie häufiger und mit größerer Zuversicht, dass Ihre Nutzer Ihre beste Nachricht sehen. 

Die intelligente Auswahl ist ideal für Kampagnen, die für den mehrfachen Versand geplant sind. Die ersten Ergebnisse werden benötigt, um Ihre Kampagne anzupassen. Eine Kampagne, die nur einmal versendet wird, ist daher nicht sinnvoll. Für diese Kampagnen wäre ein [A/B-Test][1] effektiver.

## Wie füge ich die Intelligente Auswahl zu meinen Kampagnen hinzu?

### Kampagne Intelligente Auswahl
Die Intelligente Auswahl kann zu jeder Multi-Send-Kampagne im Schritt **Zielgruppen** des Braze-Kampagnen-Composers hinzugefügt werden. Kampagnen, die nur einmal senden, können dieses Feature nicht nutzen.

### Canvas Intelligente Auswahl
Wenn Sie Varianten zu Ihrem Canvas hinzufügen, klicken Sie auf einen der Variantenprozentsätze. Damit können Sie die Variantenverteilung bearbeiten und die Intelligente Auswahl einschalten.

![Ein Canvas mit zwei Varianten, die jeweils auf 50% Variantenverteilung eingestellt sind und die Aktivierung der Intelligenten Auswahl ermöglichen.][2]

Die intelligente Auswahl ist nicht verfügbar, wenn Sie Ihrem Canvas noch keine Conversion-Ereignisse hinzugefügt haben oder wenn Ihre Kampagne aus einer Solo-Variante besteht.

{% alert note %}
Die Verwendung der intelligenten Auswahl mit Kampagnen, bei denen die Wiederzulassung in weniger als 24 Stunden aktiviert wurde, ist nicht zulässig, da dies die Integrität der Kontrollvariante beeinträchtigen würde. Lesen Sie die [FAQ zum Thema Intelligenz]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection), um mehr zu erfahren.
{% endalert %}

## Wie lange wird er laufen?

Bei Kampagnen und Canvase läuft die intelligente Auswahl so lange, bis sie genügend Erkenntnisse über die "wahren" Konversionsraten der Varianten gesammelt hat. "Genug" wird durch eine spezielle Metrik namens "Reue" bestimmt Sie können sich das so vorstellen, dass sich die Intelligente Auswahl von selbst ausschaltet, wenn genügend Daten vorhanden sind, um zu wissen, welche Variante die beste ist. 

In den meisten Fällen wird Intelligent Selection eine der Varianten als Gewinnvariante auswählen. Diese Variante erhält 100% der Hörerschaft für zukünftige Sendungen.

{% alert note %}
Es ist möglich, dass die intelligente Auswahl aufhört zu optimieren, ohne einen einzigen klaren Gewinner auszuwählen. Die intelligente Auswahl stellt die Optimierung ein, wenn sie mit 95%iger Sicherheit davon ausgehen kann, dass die Fortsetzung des Experiments die Konversionsrate nicht um mehr als 1% der derzeitigen Rate verbessern wird.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[2]: {% image_buster /assets/img/intelligent_selection.png %}
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit


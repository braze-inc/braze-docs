---
nav_title: Fehlersuche
article_title: Prädiktive Churn-Fehlerbehebung
description: "Dieser Referenzartikel behandelt einige Schritte zur Fehlerbehebung und Überlegungen, die Sie bei der Verwendung von Predictive Churn beachten sollten."
page_order: 3

---

# Fehlersuche

> Predictive Churn (und jedes Modell des maschinellen Lernens) ist nur so gut wie die Daten, die dem Modell zur Verfügung stehen. Außerdem ist sie in hohem Maße davon abhängig, dass bestimmte Datenmengen zur Verfügung stehen. 

## Mögliche Fehler

### Nicht genügend Daten zum Trainieren 

Diese Nachricht erscheint, wenn Ihre Abwanderungsdefinition zu eng gefasst ist und zu wenige abgewanderte Nutzer:innen liefert. 

Um dies zu beheben, müssen Sie entweder die Anzahl der Tage und/oder die Aktionen, die die Abwanderung definieren, ändern, um mehr Nutzer:innen zu erfassen. Vergewissern Sie sich, dass Sie die Filter von `AND/OR` richtig verwenden, um keine zu restriktiven Definitionen zu erstellen. 

{% alert important %}
Auch wenn Predictive Churn auf Unternehmensebene aktiviert ist, haben einige Workspaces möglicherweise nicht genügend Nutzer:innen, um Prognosen zu erstellen. Normalerweise benötigen Sie 300.000 monatlich aktive Nutzer:innen in einem einzigen Workspace.
{% endalert %}

### Probleme mit Prognosen zur Größe der Zielgruppe

Wenn Sie Ihre Zielgruppe für die Vorhersage erstellen, um die Art der Nutzung, für die Sie Ihr Modell trainieren möchten, fein abzustimmen, werden Sie möglicherweise auf diese Meldung stoßen, die Sie darüber informiert, dass Ihre Zielgruppe für die Vorhersage zu wenige Nutzer hat: 

"Nicht genug Abgewanderte in der Vergangenheit, um eine zuverlässige Prognose zu erstellen"

![Prognose Daten Anforderungen zeigen 31 Abgewanderte in der Vergangenheit (erfüllt die Anforderung) und 0 Nicht-Abgewanderte in der Vergangenheit (unter dem Minimum). Eine Nachricht mit einer Warnung weist darauf hin, dass nicht genügend Abgewanderte die Prognose erstellen.]({% image_buster /assets/img/churn/audience_size_error.png %})

Wenn Ihre Definition der Zielgruppe für die Vorhersage zu eng gefasst ist, können Sie möglicherweise nicht mit einem ausreichend großen Pool an historischen und aktiven Nutzern arbeiten. Um dies zu beheben, müssen Sie entweder die Anzahl der Tage und die Art der Attribute ändern, die in dieser Definition verwendet werden, oder die Aktionen ändern, die die Abwanderung definieren, oder beides. 

Wenn Ihr Vorhersagepublikum auch nach der Änderung Ihrer Definitionen weiterhin ein Problem darstellt, haben Sie möglicherweise zu wenige Benutzer, um diese optionale Funktion zu unterstützen. Wir würden vorschlagen, dass Sie stattdessen versuchen, eine Vorhersage ohne die zusätzlichen Ebenen und Filter zu erstellen. 

### Prognose Zielgruppe ist zu groß

Die Definition einer Prognose-Zielgruppe darf 100 Millionen Nutzer:innen nicht überschreiten. Wenn Sie die Nachricht erhalten, dass Ihre Zielgruppe zu groß ist, empfehlen wir Ihnen, weitere Ebenen zu Ihrer Zielgruppe hinzuzufügen oder das Zeitfenster zu ändern, auf dem sie basiert.

### Vorhersage hat schlechte Qualität

![]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
Wenn Ihr Modell eine [Vorhersagequalität]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) von 40% oder mehr hat, sind Sie auf einem guten Weg! Wenn Ihre Vorhersagequalität jedoch auf 39% oder weniger sinkt, müssen Sie Ihre Definitionen für die Abwanderung und die Vorhersagezielgruppe möglicherweise so ändern, dass sie spezifischer sind oder andere Zeitfenster haben. 

Wenn Sie bei der Erstellung Ihrer Prognosedefinitionen nicht in der Lage sind, sowohl die Anforderungen an die Größe der Zielgruppe zu erfüllen als auch eine Prognosequalität von mehr als 40% zu erreichen, bedeutet dies wahrscheinlich, dass die an Braze gesendeten Daten für diesen Anwendungsfall nicht ideal sind, dass es nicht genügend Benutzer gibt, anhand derer ein Modell erstellt werden kann, oder dass Ihr Produktlebenszyklus länger ist, als unser aktuelles 60-Tage-Rückblickfenster unterstützt. 

## Überlegungen zu Daten

Die folgenden Fragen sollten Sie sich stellen, wenn Sie Predictive Churn einrichten. Modelle für maschinelles Lernen sind nur so gut wie die Daten, mit denen sie trainiert werden. Eine gute Datenhygiene und das Verständnis dessen, was in das Modell einfließt, machen also einen großen Unterschied.

- Welche wertvollen Aktionen führen zu Bindung und Treue?
- Haben Sie angepasste Events eingerichtet, die diesen spezifischen Aktionen zugeordnet sind? Predictive Churn arbeitet mit benutzerdefinierten Ereignissen im Gegensatz zu benutzerdefinierten Attributen.
- Denken Sie in Zeitfenstern, innerhalb derer Sie das Abwandern definieren? Sie können Abwanderung als etwas definieren, das in bis zu 60 Tagen passiert.
- Haben Sie an Jahreszeiten gedacht, die zu untypischem Nutzerverhalten führen, wie z.B. die Feiertage? Rasche Veränderungen im Verbraucherverhalten werden Ihre Prognosen beeinflussen. 


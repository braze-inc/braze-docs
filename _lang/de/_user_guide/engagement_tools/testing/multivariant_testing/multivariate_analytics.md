---
nav_title: Analytics
article_title: Multivariate und A/B-Test-Analysen
page_order: 10
page_type: reference
description: "Dieser Artikel erklärt, wie Sie die Ergebnisse einer multivariaten oder A/B-Kampagne anzeigen und interpretieren können."
---

# Multivariate und A/B-Test-Analysen

> Dieser Artikel erklärt, wie Sie die Ergebnisse eines multivariaten oder A/B-Tests anzeigen können. Wenn Sie Ihren Test noch nicht eingerichtet haben, finden Sie unter [Erstellen von multivariaten und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) weitere Informationen.

Nachdem Ihre Kampagne gestartet ist, können Sie die Leistung jeder Variante überprüfen, indem Sie Ihre Kampagne im Bereich **Kampagnen** des Dashboards auswählen. 

## Analyse nach Optimierungsoption

Ihre Analyseansicht variiert, je nachdem, ob Sie bei der Ersteinrichtung eine [Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) ausgewählt haben.

### Keine Optimierung

Wenn Sie beim Einrichten Ihrer Kampagne die Option **Keine Optimierung** gewählt haben, bleibt Ihre Analyseansicht unverändert. Auf der Seite **Kampagnenanalyse** Ihrer Kampagne sehen Sie die Leistung Ihrer Varianten im Vergleich zu Ihrer Kontrollgruppe, falls Sie eine enthalten haben.

![Abschnitt Performance der Campaign Analytics für eine E-Mail-Kampagne mit mehreren Varianten. In der Tabelle sind verschiedene Metriken zur Performance für jede Variante aufgeführt, z.B. Empfänger:in, Bounces, Klicks und Konversionen.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Weitere Einzelheiten finden Sie in dem Artikel [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) für Ihren Messaging-Kanal.

### Gewinnervariante

Wenn Sie bei der Einrichtung Ihrer Kampagne die **Gewinnvariante** für Ihre Optimierung ausgewählt haben, haben Sie Zugriff auf eine zusätzliche Registerkarte Ihrer Kampagnenanalyse namens **A/B-Test-Ergebnis**. Nachdem die Gewinner-Variante an die verbleibenden Nutzer:innen in Ihrem Test gesendet wurde, zeigt dieser Tab die Ergebnisse dieses Versands an.

Das **A/B-Test-Ergebnis** ist in zwei Registerkarten unterteilt: **Erster Test** und **Gewinnvariante**.

{% tabs local %}
{% tab Initial Test %}

Die Registerkarte **Erster Test** zeigt die Metriken für jede Variante des ersten A/B-Tests, der an einen Teil Ihres Zielsegments gesendet wurde. Sie können eine Zusammenfassung sehen, wie alle Varianten abgeschnitten haben und ob es einen Gewinner im Test gab oder nicht.

Wenn eine Variante alle anderen mit mehr als 95%iger [Sicherheit]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence) übertrifft, markiert Braze diese Variante mit dem Etikett "Gewinner".

Wenn keine Variante alle anderen mit 95%iger Sicherheit schlägt und Sie sich trotzdem dafür entscheiden, die leistungsstärkste Variante zu versenden, wird die leistungsstärkste Variante trotzdem versandt und mit der Bezeichnung "Gewinner" versehen.

![Ergebnisse eines ersten Tests zur Ermittlung der Winning Variant, bei dem keine Variante mit ausreichender Sicherheit besser als die anderen abgeschnitten hat, um die 95-Prozent-Konfidenzschwelle für statistische Signifikanz zu erreichen.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Wie die Gewinnvariante ausgewählt wird

Braze testet alle Varianten gegeneinander mit [Pearson's Chi-Quadrat-Tests](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Damit wird gemessen, ob eine Variante bei einem Signifikanzniveau von p < 0,05, das wir als 95%ige Signifikanz bezeichnen, statistisch gesehen alle anderen übertrifft oder nicht. Ist dies der Fall, wird die gewinnende Variante mit dem Label "Gewinner" gekennzeichnet.

Dies ist ein anderer Test als der Konfidenzwert, der nur die Leistung einer Variante im Vergleich zur Kontrolle mit einem numerischen Wert zwischen 0 und 100% beschreibt.

Eine Variante kann besser abschneiden als die Kontrollgruppe, aber der Chi-Quadrat-Test prüft, ob eine Variante besser ist als alle anderen. [Nachfolgende Tests](#recommended-follow-ups) können weitere Details liefern.

{% endtab %}
{% tab Winning Variant %}

Die Registerkarte **Gewinnende Variante** zeigt die Ergebnisse des zweiten Versands, bei dem jedem verbleibenden Benutzer die Variante mit der besten Leistung aus dem ersten Test zugesandt wurde. **Zielgruppe %** entspricht dem Prozentsatz des Zielsegments, das Sie für die Gruppe der Gewinnvariante reserviert haben.

![Ergebnisse der Gewinner-Variante an die Gruppe der Gewinner-Varianten gesendet.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Wenn Sie die Leistung der Gewinner-Variante während der gesamten Kampagne, einschließlich der A/B-Test-Sendungen, sehen möchten, besuchen Sie die Seite **Kampagnenanalyse**.

### Personalisierte Variante {#personalized-variant}

Wenn Sie bei der Einrichtung Ihrer Kampagne die Option **Personalisierte Variante** für Ihre Optimierung gewählt haben, ist das **A/B-Test-Ergebnis** in zwei Registerkarten unterteilt: **Erster Test** und **personalisierte Variante**.

{% tabs local %}
{% tab Initial Test %}

Die Registerkarte **Erster Test** zeigt die Metriken für jede Variante des ersten A/B-Tests, der an einen Teil Ihres Zielsegments gesendet wurde.

![Ergebnisse eines ersten Tests zur Ermittlung der performantesten Variante für jeden Nutzer:in. Eine Tabelle zeigt die Performance der einzelnen Varianten auf der Grundlage verschiedener Metriken für den Targeting-Kanal.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Standardmäßig sucht der Test nach Assoziationen zwischen den benutzerdefinierten Ereignissen des Benutzers und seinen Einstellungen für die Nachrichtenvariante. Diese Analyse stellt fest, ob benutzerdefinierte Ereignisse die Wahrscheinlichkeit, auf eine bestimmte Nachrichtenvariante zu reagieren, erhöhen oder verringern. Diese Beziehungen werden dann verwendet, um zu bestimmen, welche Nutzer:innen welche Variante der Nachricht in der endgültigen Sendung erhalten.

Die Beziehungen zwischen benutzerdefinierten Ereignissen und Nachrichteneinstellungen werden in der Tabelle auf der Registerkarte **Erstes Senden** angezeigt.

![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Wenn der Test keine sinnvolle Beziehung zwischen angepassten Events und Variantenpräferenzen finden kann, greift er auf eine sitzungsbasierte Analysemethode zurück.

{% details Fallback analysis method %}

**Sitzungsbasierte Analyse-Methode**<br>
Wenn die Fallback-Methode für die Bestimmung der personalisierten Varianten verwendet wird, zeigt die Registerkarte **Erster Test** eine Aufschlüsselung der bevorzugten Varianten der Benutzer auf der Grundlage einer Kombination bestimmter Merkmale. 

Diese Merkmale sind:

- **Aktualität:** Wann sie zuletzt eine Sitzung hatten
- **Frequenz:** Wie oft sie Sitzungen abhalten
- **Amtszeit:** Wie lange sie bereits Nutzer:in sind

Der Test könnte beispielsweise ergeben, dass die meisten Benutzer Variante A bevorzugen, aber Benutzer, die vor 3-12 Tagen eine Sitzung hatten, zwischen 1-12 Tagen zwischen den Sitzungen liegen und in den letzten 67-577 Tagen erstellt wurden, bevorzugen eher Variante B. Daher erhielten die Benutzer in dieser Teilpopulation beim zweiten Senden Variante B, während der Rest Variante A erhielt.

![Die Tabelle mit den Nutzereigenschaften, die zeigt, welche Nutzer:innen auf der Grundlage der drei Buckets für Häufigkeit, Häufigkeit und Dauer der Nutzung prognostiziert werden, Variante A und Variante B zu bevorzugen.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Wie personalisierte Varianten ausgewählt werden**<br>
Bei dieser Methode ist die empfohlene Nachricht eines einzelnen Nutzers oder einer einzelnen Nutzerin die Summe der Effekte seiner spezifischen Häufigkeit, Häufigkeit und Dauer. Häufigkeit, Häufigkeit und Dauer der Nutzung werden in Buckets unterteilt, wie in der Tabelle **Nutzer:innen zu** sehen ist. Der Zeitbereich der einzelnen Buckets wird durch die Daten der Nutzer in jeder einzelnen Kampagne bestimmt und ändert sich von Kampagne zu Kampagne. 

Jeder Bucket kann einen unterschiedlichen Beitrag oder "Push" zu jeder Variante der Nachricht leisten. Die Stärke des Push für jeden Bucket wird anhand der Antworten der Nutzer:innen beim ersten Senden mit Hilfe einer [logistischen Regression](https://en.wikipedia.org/wiki/Logistic_regression) bestimmt. Diese Tabelle fasst die Ergebnisse nur zusammen, indem sie anzeigt, mit welcher Variante sich die Nutzer in jedem Bereich tendenziell beschäftigen. Die tatsächliche personalisierte Variante eines einzelnen Benutzers hängt von der Summe der Auswirkungen der drei Bereiche ab, in denen er sich befindet - einer für jedes Merkmal.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

Die Registerkarte **Personalisierte Variante** zeigt die Ergebnisse des zweiten Versands, bei dem jedem verbleibenden Nutzer die Variante zugesandt wurde, mit der er sich am ehesten beschäftigen würde.

Die drei Karten auf dieser Seite zeigen Ihren voraussichtlichen Gewinn, das Gesamtergebnis und die voraussichtlichen Ergebnisse, wenn Sie nur die Gewinnvariante verschickt hätten. Selbst wenn es keinen Aufschwung gibt, was manchmal vorkommen kann, ist das Ergebnis dasselbe wie bei einem herkömmlichen A/B-Test, bei dem nur die Gewinnervariante versendet wird. 

- **Projizierter Auftrieb:** Die Verbesserung der von Ihnen gewählten Optimierungskennzahl für diese Sendung aufgrund der Verwendung von personalisierten Varianten anstelle eines standardmäßigen A/B-Tests (wenn die verbleibenden Nutzer nur die Gewinnervariante erhalten haben).
- **Gesamtergebnisse:** Die Ergebnisse des zweiten Versands auf der Grundlage der von Ihnen gewählten Optimierungsmetrik*(Unique Opens*, *Unique Clicks* oder *Primary Conversion Event*).
- **Prognostizierte Ergebnisse:** Die voraussichtlichen Ergebnisse des zweiten Versands auf der Grundlage der von Ihnen gewählten Optimierungsmetrik, wenn Sie stattdessen nur die Gewinnvariante versendet hätten. 

![Tab der personalisierten Variante für eine Kampagne, die für eindeutige Öffnungen optimiert ist. Die Karten zeigen den hochgerechneten Aufzug, die eindeutigen Öffnungen insgesamt (mit personalisierter Variante) und die hochgerechneten eindeutigen Öffnungen (mit Gewinnvariante).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

Die Tabelle auf dieser Seite zeigt die Metriken für jede Variante aus dem personalisierten Variantenversand. **Zielgruppe %** entspricht dem Prozentsatz des Zielsegments, das Sie für die Gruppe der personalisierten Varianten reserviert haben.

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Vertrauen verstehen {#understanding-confidence}

Konfidenz ist das statistische Maß dafür, wie sicher wir sind, dass ein Unterschied in den Daten, z. B. bei den Konversionsraten, real ist und nicht nur auf Zufall beruht.

{% alert note %}
Haben Sie kein Vertrauen in Ihre Ergebnisse? Vertrauen wird nur angezeigt, wenn Sie eine Kontrollgruppe haben.
{% endalert %}

Ein wichtiger Teil Ihrer Ergebnisse ist das Vertrauen in Ihre Ergebnisse. Was wäre zum Beispiel, wenn die Kontrollgruppe eine Konversionsrate von 20 % hätte und Variante A eine Konversionsrate von 25 %? Dies scheint darauf hinzudeuten, dass das Senden von Variante A effektiver ist als das Senden keiner Nachricht. Eine Konfidenz von 95 % bedeutet, dass der Unterschied zwischen den beiden Konversionsraten wahrscheinlich auf einen tatsächlichen Unterschied in den Antworten der Nutzer zurückzuführen ist und dass es nur eine Wahrscheinlichkeit von 5 % gibt, dass der Unterschied zufällig entstanden ist.

Braze vergleicht die Konversionsrate jeder Variante mit der Konversionsrate der Kontrollvariante mit einem statistischen Verfahren namens [Z-Test](https://en.wikipedia.org/wiki/Z-test). Ein Ergebnis von 95 % oder mehr Konfidenz, wie im vorangegangenen Beispiel, zeigt an, dass der Unterschied statistisch signifikant ist. Das trifft überall dort zu, wo Sie im Braze-Dashboard eine Metrik sehen, die den Unterschied zwischen zwei Nachrichten oder Nutzer:innen beschreibt.

Im Allgemeinen ist eine Konfidenz von mindestens 95 % erforderlich, um zu zeigen, dass Ihre Ergebnisse die tatsächlichen Präferenzen der Nutzer:innen widerspiegeln und nicht auf Zufall beruhen. Bei strengen wissenschaftlichen Tests ist die 95 %ige Konfidenz (oder anders ausgedrückt der "p"-Wert, der kleiner als 0,05 ist) der übliche Maßstab, um die statistische Signifikanz zu bestimmen. Wenn Sie immer wieder eine Konfidenz von 95 % nicht erreichen, versuchen Sie, die Stichprobengröße zu erhöhen oder die Anzahl der Varianten zu verringern. 

Das Vertrauen sagt nichts darüber aus, ob eine Variante besser ist als die anderen. Sie ist lediglich ein Maß dafür, wie sicher wir sind, dass sich die beiden (oder mehr) Konversionsraten tatsächlich voneinander unterscheiden. Dies ist lediglich eine Funktion des Stichprobenumfangs und der Unterschiede zwischen den scheinbaren Konversionsraten. Ob die Gesamtraten hoch oder niedrig sind, hat keinen Einfluss auf die Stärke des Vertrauensmaßes. Es ist möglich, dass eine Variante eine ganz andere Konversionsrate hat als eine andere und dennoch keine 95 % oder mehr Konfidenz aufweist. Es ist auch möglich, dass zwei Varianten ähnliche Konversionsraten bzw. Uplift-Raten haben und dennoch unterschiedlich vertrauenswürdig sind.

### Statistisch unbedeutende Ergebnisse

Ein Test, der keine 95%ige Sicherheit bietet, kann dennoch wichtige Insights liefern. Hier sind ein paar Dinge, die Sie aus einem Test mit statistisch unbedeutenden Ergebnissen lernen können:

- Es ist möglich, dass alle Ihre Varianten in etwa die gleiche Wirkung hatten. Wenn Sie das wissen, sparen Sie die Zeit, die Sie sonst für diese Änderungen aufgewendet hätten. Manchmal stellen Sie fest, dass herkömmliche Marketing-Taktiken, wie z. B. die Wiederholung Ihres Aufrufs zum Handeln, bei Ihrer Zielgruppe nicht unbedingt funktionieren.
- Auch wenn Ihre Ergebnisse vielleicht zufällig waren, können sie die Hypothese für Ihren nächsten Test bestimmen. Wenn mehrere Varianten in etwa die gleichen Ergebnisse zu erzielen scheinen, lassen Sie einige von ihnen zusammen mit neuen Varianten erneut laufen, um zu sehen, ob Sie eine effektivere Alternative finden können. Wenn eine Variante besser abschneidet, aber nicht um einen signifikanten Betrag, können Sie einen weiteren Test durchführen, bei dem der Unterschied dieser Variante stärker ausgeprägt ist.
- Testen Sie weiter! Ein Test mit unbedeutenden Ergebnissen sollte zu bestimmten Fragen führen. Gab es wirklich keinen Unterschied zwischen Ihren Varianten? Hätten Sie Ihren Test anders strukturieren sollen? Sie können diese Fragen beantworten, indem Sie Folgetests durchführen.
- Tests sind zwar nützlich, um herauszufinden, welche Art von Botschaft die meisten Reaktionen bei Ihrem Publikum hervorruft, aber es ist auch wichtig zu verstehen, welche Änderungen in der Botschaft nur eine vernachlässigbare Wirkung haben. Auf diese Weise können Sie entweder den Test für eine andere, effektivere Alternative fortsetzen oder die Zeit einsparen, die Sie vielleicht für die Entscheidung zwischen zwei alternativen Nachrichten gebraucht hätten.

Unabhängig davon, ob Ihr Test einen klaren Gewinner hat oder nicht, kann es hilfreich sein, einen [Folgetest](#recommended-follow-ups) durchzuführen, um Ihre Ergebnisse zu bestätigen oder Ihre Erkenntnisse auf ein etwas anderes Szenario anzuwenden.

## Diskrepanzen zwischen Kontrollgruppe und Variante

Bei In-App-Nachricht-Kampagnen kann die Art und Weise, wie Nutzer:innen getrackt und Impressionen protokolliert werden, zu Diskrepanzen bei der erwarteten Aufteilung zwischen Kontrollgruppe und Variante führen. Dies liegt daran, dass die tatsächlich protokollierten Impressionen diese Aufteilung möglicherweise nicht widerspiegeln, und Braze hat letztlich keine Kontrolle über das individuelle Verhalten der Nutzer:innen, die den Trigger ausführen.

Nehmen wir zum Beispiel an, eine Kampagne hat beim Start eine Zielgruppe von 200 Nutzern, wobei 100 Nutzer:innen in der Kontrollgruppe und 100 Nutzer:innen in der Variante sind.

Die 100 Nutzer:innen in der Variante erhalten die In-App-Nachricht, und 50 von ihnen führen die Aktion triggern aus und sehen die In-App-Nachricht. Die 100 Nutzer in der Kontrollgruppe werden nur getrackt, wenn sie die Aktion triggern, die die Kampagne auslöst, und 75 von ihnen führen die Aktion triggern aus und protokollieren eine Impression, sehen aber die In-App-Nachricht nicht.

Trotz der anfänglichen 50/50-Aufteilung sind die protokollierten eindeutigen Impressionen nicht ausgeglichen. Die Variante hat 50 Impressionen, während die Kontrollgruppe 75 Impressionen hat.

### Verzögerungen bei In-App-Nachricht 

Bei getriggerten In-App-Nachricht-Kampagnen, die verzögerte Anzeigen beinhalten, werden die Impressionen der Kontrollgruppe zu dem Zeitpunkt erfasst, an dem der Endnutzer die In-App-Nachricht ursprünglich erhalten hätte. Wenn eine Kampagne zum Beispiel so eingestellt ist, dass die Anzeige um eine Stunde verzögert wird, werden die Impressionen der Kontrollgruppe erst nach Ablauf der einstündigen Verzögerung protokolliert. Dies hilft beim genauen Tracking der Impressionen in Bezug auf den beabsichtigten Zeitpunkt der Zustellung der Nachricht.

## Empfohlene Folgemaßnahmen {#recommended-follow-ups}

Ein multivariater und A/B-Test kann (und sollte!) Sie zu Ideen für künftige Tests inspirieren und Sie zu Änderungen in Ihrer Kommunikationsstrategie anleiten. Mögliche Folgemaßnahmen sind unter anderem die folgenden:

#### Ändern Sie Ihre Messaging Strategie anhand der Testergebnisse

Ihre multivariaten Ergebnisse können Sie dazu veranlassen, die Art und Weise zu ändern, wie Sie Ihre Nachrichten formulieren oder formatieren.

#### Verändern Sie die Art und Weise, wie Sie Ihre Benutzer verstehen

Jeder Test gibt Aufschluss über das Verhalten Ihrer Nutzer, über die Reaktion der Nutzer auf verschiedene Nachrichtenkanäle und über die Unterschiede (und Gemeinsamkeiten) zwischen Ihren Segmenten.

#### Verbessern Sie die Struktur zukünftiger Tests

War Ihre Stichprobengröße zu klein? Waren die Unterschiede zwischen Ihren Varianten zu subtil? Jeder Test bietet eine Opportunity zu lernen, wie man zukünftige Tests verbessern kann. Wenn Ihr Vertrauen gering ist, ist Ihre Stichprobengröße zu klein und sollte für zukünftige Tests vergrößert werden. Wenn Sie keinen eindeutigen Unterschied in der Performance Ihrer Varianten feststellen, ist es möglich, dass die Unterschiede zu subtil waren, um einen erkennbaren Effekt auf die Nutzer:innen zu haben.

#### Führen Sie einen Folgetest mit einer größeren Stichprobengröße durch

Größere Proben erhöhen die Wahrscheinlichkeit, kleine Unterschiede zwischen Varianten zu erkennen.

#### Führen Sie einen Folgetest über einen anderen Messaging-Kanal durch

Wenn Sie feststellen, dass eine bestimmte Strategie in einem Kanal sehr effektiv ist, sollten Sie diese Strategie auch in anderen Kanälen testen. Wenn eine bestimmte Art von Botschaft in einem Kanal wirksam ist, in einem anderen jedoch nicht, können Sie daraus schließen, dass bestimmte Kanäle für bestimmte Arten von Botschaften besser geeignet sind. Vielleicht gibt es aber auch einen Unterschied zwischen Nutzern, die eher Push-Benachrichtigungen aktivieren, und solchen, die eher auf In-App-Nachrichten achten. Letztendlich hilft Ihnen diese Art von Test, herauszufinden, wie Ihre Zielgruppe mit Ihren verschiedenen Kanälen interagiert.

#### Führen Sie einen Folgetest mit einem anderen Segment von Nutzer:innen durch

Erstellen Sie dazu einen weiteren Test mit demselben Messaging-Kanal und denselben Varianten, aber wählen Sie ein anderes Segment von Nutzer:innen. Wenn zum Beispiel eine Art von Messaging bei engagierten Nutzer:innen extrem effektiv war, könnte es sinnvoll sein, die Wirkung auf passive Nutzer:innen zu untersuchen. Es ist möglich, dass die passiven Nutzer:innen ähnlich reagieren oder eine der anderen Varianten bevorzugen. Dieser Test wird Ihnen helfen, mehr über Ihre verschiedenen Segmente zu erfahren und darüber, wie diese auf verschiedene Arten von Nachrichten reagieren. Warum sollten Sie Annahmen über Ihre Segmente treffen, wenn Sie Ihre Strategie auf Daten stützen können?

#### Führen Sie einen Folgetest auf der Grundlage von Insights aus einem früheren Test durch

Nutzen Sie die Insights, die Sie aus vergangenen Tests gewonnen haben, um Ihre zukünftigen Tests zu steuern. Deutet ein früherer Test darauf hin, dass eine bestimmte Nachrichtentechnik effektiver ist? Sind Sie unsicher, welcher Aspekt einer Variante sie besser macht? Die Durchführung von Folgetests auf der Grundlage dieser Fragen wird Ihnen helfen, aufschlussreiche Insights über Ihre Nutzer:innen zu gewinnen.

#### Vergleichen Sie die langfristigen Auswirkungen der verschiedenen Varianten

Wenn Sie A/B-Tests mit Re-Engagement-Botschaften durchführen, vergessen Sie nicht, die langfristigen Auswirkungen der verschiedenen Varianten mithilfe von [Retention Reports]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) zu vergleichen. Mithilfe von Retention Reports können Sie analysieren, wie sich jede Variante Tage, Wochen oder einen Monat nach Erhalt der Nachricht auf ein beliebiges Nutzerverhalten Ihrer Wahl ausgewirkt hat, und feststellen, ob es einen Uplift gibt.

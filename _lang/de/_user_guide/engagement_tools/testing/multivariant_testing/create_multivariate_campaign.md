---
nav_title: Tests erstellen
article_title: Erstellen Sie multivariate und A/B-Tests
page_order: 1
page_type: reference
description: "Dieser Artikel erklärt, wie Sie mit Braze multivariate und A/B-Tests erstellen können."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Erstellen Sie multivariate und A/B-Tests {#creating-tests}

> Sie können für jede Kampagne, die auf einen einzelnen Kanal und ein einzelnes Gerät abzielt, einen [multivariaten oder A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) erstellen. Wenn Sie zum Beispiel multivariate oder A/B-Tests für eine Push-Kampagne verwenden möchten, können Sie nur iOS-Geräte oder nur Android-Geräte als Zielgruppe verwenden – nicht beide Gerätetypen in derselben Kampagne.

![Das Dropdown-Menü, wenn Sie den Button „Kampagne erstellen" auswählen, um zwischen mehreren Kanälen oder einem Kanal zu wählen.]({% image_buster /assets/img/ab_create_1.png %}){: style="max-width:25%;float:right;margin-left:15px;" }

## 1. Schritt: Kampagne erstellen

1. Gehen Sie zu **Messaging** > **Kampagnen**.
2. Wählen Sie **Kampagne erstellen** und einen Kanal für die Kampagne aus dem Bereich, der multivariate und A/B-Tests zulässt. Eine ausführliche Dokumentation zu jedem Messaging-Kanal finden Sie unter [Erstellen einer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

## 2. Schritt: Varianten zusammenstellen

Sie können bis zu acht Varianten Ihrer Nachricht erstellen, die sich durch Titel, Inhalt, Bilder und mehr unterscheiden. Die Anzahl der Unterschiede zwischen den Nachrichten bestimmt, ob es sich um einen multivariaten oder einen A/B-Test handelt. Bei einem A/B-Test wird die Auswirkung der Änderung einer Variable untersucht, während bei einem multivariaten Test zwei oder mehr Variablen untersucht werden.

Einige Ideen, wie Sie mit der Differenzierung Ihrer Varianten beginnen können, finden Sie unter [Tipps für verschiedene Kanäle](#tips-different-channels).

![Auswählen von „Variante hinzufügen" für eine Kampagne.]({% image_buster /assets/img/ab_create_2.png %})

## 3. Schritt: Zeitplan für Ihre Kampagne

Die Planung Ihrer multivariaten Kampagne funktioniert genauso wie die Planung jeder anderen Braze-Kampagne. Alle gängigen [Zustellungsarten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/) sind verfügbar.

Nachdem ein multivariater Test begonnen hat, können Sie keine Änderungen mehr an der Kampagne vornehmen. Wenn Sie die Parameter ändern, z. B. die Betreffzeile oder den HTML-Text, betrachtet Braze das Experiment als kompromittiert und deaktiviert es sofort.

{% alert important %}
Um eine [Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) zu nutzen (verfügbar für ausgewählte Kanäle), planen Sie Ihre Kampagne so, dass sie einmal zugestellt wird. Optimierungen sind nicht verfügbar für Kampagnen, die wiederholt werden oder bei denen die Wiederberechtigung aktiviert ist.
{% endalert %}

## 4. Schritt: Wählen Sie ein Segment und verteilen Sie Ihre Nutzer:innen auf verschiedene Varianten

Wählen Sie Segmente für das Targeting aus und verteilen Sie die Mitglieder dann auf Ihre ausgewählten Varianten und die optionale [Kontrollgruppe](#including-a-control-group). Bewährte Methoden für die Auswahl eines Segments zum Testen finden Sie unter [Ein Segment auswählen](#choosing-a-segment).

Für Push-, E-Mail- und Webhook-Kampagnen, die für einen einmaligen Versand geplant sind, können Sie auch eine [Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) verwenden. Eine Optimierung reserviert einen Teil Ihrer Zielgruppe aus dem A/B-Test und hält ihn für einen zweiten optimierten Versand auf der Grundlage der Ergebnisse des ersten Tests zurück.

### Kontrollgruppe {#including-a-control-group}

Sie können einen Prozentsatz Ihrer Zielgruppe für eine randomisierte Kontrollgruppe reservieren. Nutzer:innen in der Kontrollgruppe erhalten den Test nicht, aber Braze überwacht ihre Konversionsrate während der gesamten Dauer der Kampagne.

Wenn Sie Ihre Ergebnisse betrachten, können Sie die Konversionsraten Ihrer Varianten mit einer von Ihrer Kontrollgruppe bereitgestellten Basis-Konversionsrate vergleichen. So können Sie sowohl die Auswirkungen Ihrer Varianten als auch die Konversionsrate vergleichen, die sich ergeben würde, wenn Sie überhaupt keine Nachricht senden würden.

![A/B-Test-Panel, das die prozentuale Aufschlüsselung der Kontrollgruppe, Variante 1, Variante 2 und Variante 3 mit jeweils 25 % anzeigt.]({% image_buster /assets/img/ab_create_4.png %})

{% alert important %}
Die Verwendung einer Kontrollgruppe bei der Ermittlung eines Gewinners durch _Öffnungen_ oder _Klicks_ wird nicht empfohlen. Da die Kontrollgruppe die Nachricht nicht erhält, können diese Nutzer:innen keine Öffnungen oder Klicks durchführen. Daher ist die Konversionsrate dieser Gruppe per Definition 0 % und stellt keinen sinnvollen Vergleich zu den Varianten dar.
{% endalert %}

#### Kontrollgruppen mit A/B-Tests

Wenn Sie Rate-Limiting bei einem A/B-Test verwenden, wird das Rate-Limit nicht in gleicher Weise auf die Kontrollgruppe angewandt wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen darstellt. Verwenden Sie geeignete Konversionsfenster, um diese Verzerrung zu vermeiden.

#### Kontrollgruppen mit intelligenter Auswahl

Die Größe der Kontrollgruppe für eine Kampagne mit [intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) richtet sich nach der Anzahl der Varianten. Wenn jede Variante an mehr als 20 % der Nutzer:innen gesendet wird, beträgt die Kontrollgruppe 20 %, und die Varianten werden gleichmäßig auf die verbleibenden 80 % verteilt. Wenn Sie jedoch so viele Varianten haben, dass jede Variante an weniger als 20 % der Nutzer:innen gesendet wird, muss die Kontrollgruppe kleiner werden. Wenn die intelligente Auswahl mit der Analyse der Performance Ihres Tests beginnt, vergrößert oder verkleinert sich die Kontrollgruppe entsprechend den Ergebnissen.

## 5. Schritt: Konversions-Event festlegen (optional)

Wenn Sie ein Konversions-Event für eine Kampagne festlegen, können Sie sehen, wie viele Empfänger:innen dieser Kampagne eine bestimmte Aktion durchgeführt haben, nachdem sie die Kampagne erhalten haben.

Dies wirkt sich nur auf den Test aus, wenn Sie in den vorangegangenen Schritten **Primäre Konversionsrate** gewählt haben. Weitere Informationen finden Sie unter [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/).

## 6. Schritt: Überprüfen und starten

Überprüfen Sie auf der Bestätigungsseite die Details Ihrer multivariaten Kampagne und starten Sie den Test! Als Nächstes erfahren Sie, wie Sie [Ihre Testergebnisse verstehen]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/) können.

## Wissenswertes

Wenn Ihr Experiment bereits mit dem Senden begonnen hat und Sie die Nachricht bearbeiten, wird das Experiment für ungültig erklärt, und alle Experimentergebnisse werden entfernt.

- Um das erwartete Verhalten des Experiments nicht zu beeinträchtigen, empfehlen wir, Nachrichten nicht innerhalb einer Stunde nach dem Start der Experimentkampagne zu bearbeiten.
- Wenn Ihr Experiment abgeschlossen ist und Sie die Nachricht nach dem Versand bearbeiten, bleiben die Experimentergebnisse in Ihrem Dashboard Analytics verfügbar. Wenn Sie die Kampagne jedoch neu starten, werden die Experimentergebnisse entfernt.

### Tipps für verschiedene Kanäle {#tips-different-channels}

Je nachdem, welchen Kanal Sie auswählen, können Sie verschiedene Komponenten Ihrer Nachricht testen. Sie können zum Beispiel versuchen, Varianten mit einer Idee darüber zu erstellen, was Sie testen möchten und was Sie zu beweisen hoffen. Welche Hebel können Sie betätigen, und was sind die gewünschten Auswirkungen? Es gibt zwar Millionen von Möglichkeiten, die Sie mit einem multivariaten und A/B-Test untersuchen können, aber wir haben ein paar Vorschläge für den Anfang:

| Kanal | Aspekte der Nachricht, die Sie ändern können | Ergebnisse, auf die Sie achten sollten |
| ---------------------| --------------- | ------------- |
| Push | Text <br> Verwendung von Bildern und Emojis <br> Deeplinks  <br> Darstellung von Zahlen (z. B. „Verdreifachung" gegenüber „Steigerung um 200 %")  <br> Darstellung der Zeit (z. B. „endet um Mitternacht" gegenüber „endet in 6 Stunden") | Öffnungen  <br> Konversionsrate |
| E-Mail | Betreff <br> Anzeigename <br> Anrede <br> Textkörper <br> Verwendung von Bildern und Emojis <br> Darstellung von Zahlen (z. B. „Verdreifachung" gegenüber „Steigerung um 200 %") <br> Darstellung der Zeit (z. B. „endet um Mitternacht" gegenüber „endet in 6 Stunden") | Öffnungen  <br> Konversionsrate |
| In-App-Nachricht | Für „Push" aufgelistete Aspekte <br> [Bildspezifikationen für In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#in-app-messages) | Klick <br> Konversionsrate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Vergessen Sie bei der Durchführung von A/B-Tests nicht, [Funnel-Berichte]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) zu erstellen, die Ihnen Aufschluss darüber geben, wie sich die einzelnen Varianten auf Ihren Konversionstrichter ausgewirkt haben – insbesondere dann, wenn „Konversion" in Ihrem Unternehmen mehrere Schritte oder Aktionen umfasst.
{% endalert %}

Darüber hinaus kann die ideale Länge Ihres Tests je nach Kanal variieren. Denken Sie daran, wie viel Zeit die meisten Nutzer:innen durchschnittlich für das Engagement auf den einzelnen Kanälen benötigen.

Wenn Sie zum Beispiel Push testen, erzielen Sie möglicherweise schneller aussagekräftige Ergebnisse als beim Testen von E-Mails, da Nutzer:innen Push-Nachrichten sofort sehen, es aber Tage dauern kann, bis sie eine E-Mail sehen oder öffnen. Wenn Sie In-App-Nachrichten testen, denken Sie daran, dass die Nutzer:innen die App öffnen müssen, um die Kampagne zu sehen. Sie sollten also länger warten, um Ergebnisse sowohl von Ihren aktivsten App-Nutzer:innen als auch von Ihren typischeren Nutzer:innen zu sammeln.

Wenn Sie sich nicht sicher sind, wie lange Ihr Test laufen soll, kann das Feature [intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) nützlich sein, um effizient eine Gewinnervariante zu finden.

### Ein Segment auswählen {#choosing-a-segment}

Da verschiedene Segmente Ihrer Nutzer:innen unterschiedlich auf Nachrichten reagieren können, sagt der Erfolg einer bestimmten Nachricht sowohl etwas über die Nachricht selbst als auch über ihr Zielsegment aus. Versuchen Sie daher, einen Test zu entwerfen, der Ihr Zielsegment berücksichtigt.

Während aktive Nutzer:innen beispielsweise auf „Dieses Angebot läuft morgen ab!" und „Dieses Angebot läuft in 24 Stunden ab!" gleich häufig reagieren, sind Nutzer:innen, die die App seit einer Woche nicht mehr geöffnet haben, möglicherweise empfänglicher für die letztere Formulierung, da sie ein stärkeres Gefühl der Dringlichkeit vermittelt.

Außerdem sollten Sie bei der Auswahl des Segments, in dem Sie Ihren Test durchführen möchten, darauf achten, ob die Größe dieses Segments für Ihren Test ausreicht. Im Allgemeinen benötigen multivariate und A/B-Tests mit mehr Varianten eine größere Testgruppe, um statistisch signifikante Ergebnisse zu erzielen. Das liegt daran, dass mehr Varianten dazu führen, dass weniger Nutzer:innen jede einzelne Variante sehen.

{% alert tip %}
Als Richtwert gilt, dass Sie wahrscheinlich etwa 15.000 Nutzer:innen pro Variante (einschließlich der Kontrollgruppe) benötigen, um eine 95%ige Sicherheit Ihrer Testergebnisse zu erreichen. Die genaue Anzahl der Nutzer:innen kann jedoch je nach Ihrem speziellen Fall höher oder niedriger sein. Für eine genauere Anleitung zu Stichprobengrößen pro Variante sollten Sie einen [Stichprobengrößenrechner](https://www.calculator.net/sample-size-calculator.html) heranziehen.
{% endalert %}

### Verzerrung und Randomisierung

Eine häufige Frage bei der Zuweisung von Kontroll- und Testgruppen ist, ob sie zu Verzerrungen bei Ihren Tests führen können. Andere fragen sich manchmal, woher wir wissen, ob diese Zuweisungen wirklich zufällig sind.

Nutzer:innen werden Nachrichtenvarianten, Canvas-Varianten oder ihren jeweiligen Kontrollgruppen zugewiesen, indem ihre (zufällig generierte) Nutzer-ID mit der (zufällig generierten) Kampagnen- oder Canvas-ID verkettet wird, der Modulus dieses Wertes mit 100 genommen wird und die Nutzer:innen dann in Abschnitte eingeteilt werden, die den prozentualen Zuweisungen für die im Dashboard gewählten Varianten und optionalen Kontrollgruppen entsprechen. Es gibt also keine praktische Möglichkeit, dass das Verhalten der Nutzer:innen vor der Erstellung einer bestimmten Kampagne oder eines Canvas systematisch zwischen den Varianten und der Kontrollgruppe variieren könnte. Es ist auch nicht sinnvoll, zufälliger (oder genauer gesagt pseudozufälliger) als diese Implementierung zu sein.

#### Zu vermeidende Fehler

Es gibt einige häufige Fehler, die den Anschein von Unterschieden je nach Messaging-Kanal erwecken können, wenn die Zielgruppen nicht korrekt gefiltert werden.

Wenn Sie zum Beispiel eine Push-Nachricht an eine breite Zielgruppe mit einer Kontrollgruppe senden, sendet die Testgruppe Nachrichten nur an Nutzer:innen mit einem Push-Token. Die Kontrollgruppe umfasst jedoch sowohl Nutzer:innen, die einen Push-Token haben, als auch Nutzer:innen, die keinen haben. In diesem Fall muss Ihre ursprüngliche Zielgruppe für die Kampagne oder das Canvas nach einem Push-Token filtern (`Foreground Push Enabled` ist `true`). Dasselbe gilt für die Berechtigung zum Empfang von Nachrichten auf anderen Kanälen: Opt-in, Push-Token oder Abonnement.

Beachten Sie, dass wenn eine Kontrollvariante nicht aus Canvas-Schritten besteht, für Nutzer:innen in dieser Kontrollvariante keine Ausstiegskriterien-Events protokolliert werden.

{% alert note %}
Wenn Sie manuell zufällige Bucket-Nummern für Kontrollgruppen verwenden, lesen Sie [worauf Sie achten sollten]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for) in Ihren Kontrollgruppen.
{% endalert %}
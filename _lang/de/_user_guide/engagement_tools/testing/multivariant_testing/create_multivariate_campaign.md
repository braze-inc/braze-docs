---
nav_title: Tests erstellen
article_title: Multivariate und A/B-Tests erstellen
page_order: 1
page_type: reference
description: "Dieser Artikel erklärt, wie Sie mit Braze multivariate und A/B-Tests erstellen können."

local_redirect: #optimizations
  optimizations: '/docs/user_guide/engagement_tools/testing/multivariant_testing/optimizations/'
---

# Multivariate und A/B-Tests erstellen {#creating-tests}

> Sie können für jede Kampagne, die auf einen einzelnen Kanal zielt, einen [multivariaten oder A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) erstellen.



## Schritt 1: Kampagne erstellen

1. 
2.  

## Schritt 2: Varianten zusammenstellen

 Die Anzahl der Unterschiede zwischen den Nachrichten bestimmt, ob es sich um einen multivariaten oder einen A/B-Test handelt. Bei einem A/B-Test wird die Auswirkung der Änderung einer Variable untersucht, während bei einem multivariaten Test zwei oder mehr Variablen untersucht werden.

Einige Ideen, wie Sie mit der Differenzierung Ihrer Varianten beginnen können, finden Sie unter [Tipps für verschiedene Kanäle](#tips-different-channels).



## Schritt 3: Zeitplan für Ihre Kampagne

Die Planung Ihrer multivariaten Kampagne funktioniert genauso wie die Planung jeder anderen Braze-Kampagne. Alle gängigen [Lieferarten][4] sind verfügbar.

Sobald ein multivariater Test beginnt, können Sie keine Änderungen mehr an der Kampagne vornehmen. Wenn Sie die Parameter ändern, z. B. die Betreffzeile oder den HTML-Text, betrachtet Braze das Experiment als gefährdet und deaktiviert es sofort.

{% alert important %}
 Optimierungen sind nicht verfügbar für Kampagnen, die wiederholt werden oder bei denen die Wiederholbarkeit aktiviert ist.
{% endalert %}

## Schritt 4: Wählen Sie ein Segment und verteilen Sie Ihre Nutzer:innen auf verschiedene Varianten

Wählen Sie die Zielsegmente aus und verteilen Sie dann die Mitglieder auf Ihre ausgewählten Varianten und die optionale [Kontrollgruppe](#including-a-control-group). Bewährte Methoden für die Auswahl eines Segments zum Testen finden Sie unter [Auswahl eines Segments](#choosing-a-segment).

Für Push-, E-Mail- und Webhook-Kampagnen, die für einen einmaligen Versand geplant sind, können Sie auch eine [Optimierung]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) verwenden. Dadurch wird ein Teil Ihrer Zielgruppe aus dem A/B-Test reserviert und für einen zweiten optimierten Versand auf der Grundlage der Ergebnisse des ersten Tests gehalten.

### Kontrollgruppe {#including-a-control-group}

Sie können einen Prozentsatz Ihrer Zielgruppe für eine randomisierte Kontrollgruppe reservieren. Nutzer:innen der Kontrollgruppe erhalten den Test nicht, aber Braze überwacht ihre Konversionsrate während der gesamten Dauer der Kampagne.

Wenn Sie Ihre Ergebnisse betrachten, können Sie die Konversionsraten Ihrer Varianten mit einer von Ihrer Kontrollgruppe bereitgestellten Basis-Konversionsrate vergleichen. So können Sie sowohl die Auswirkungen Ihrer Varianten als auch die Auswirkungen Ihrer Varianten mit der Konversionsrate vergleichen, die sich ergeben würde, wenn Sie überhaupt keine Nachricht senden würden.

![A/B-Testfenster, das die prozentuale Aufschlüsselung der Kontrollgruppe, Variante 1, Variante 2 und Variante 3 mit 25 % für jede Gruppe anzeigt.][5]

{% alert important %}
 Da die Kontrollgruppe die Nachricht nicht erhält, können diese Benutzer keine Öffnungen oder Klicks vornehmen. Daher ist die Konversionsrate dieser Gruppe per Definition 0 % und stellt keinen sinnvollen Vergleich zu den Varianten dar.


#### Kontrollgruppen mit A/B-Tests

Wenn Sie die Ratenbegrenzung bei einem A/B-Test verwenden, wird die Ratenbegrenzung nicht in gleicher Weise auf die Kontrollgruppe angewandt wie auf die Testgruppe, was eine potenzielle Quelle für zeitliche Verzerrungen ist. Verwenden Sie geeignete Umrechnungsfenster, um diese Verzerrung zu vermeiden.

#### Kontrollgruppen mit Intelligenter Auswahl

Die Größe der Kontrollgruppe für eine Kampagne mit [Intelligenter Auswahl][1] richtet sich nach der Anzahl der Varianten.  Wenn Sie jedoch so viele Varianten haben, dass jede Variante an weniger als 20% der Nutzer gesendet wird, muss die Kontrollgruppe kleiner werden. Wenn Intelligent Selection mit der Analyse der Leistung Ihres Tests beginnt, vergrößert oder verkleinert sich die Kontrollgruppe entsprechend den Ergebnissen.

## Schritt 5: Konversions-Event planen (optional)

Wenn Sie ein Conversion-Ereignis für eine Kampagne festlegen, können Sie sehen, wie viele Empfänger dieser Kampagne eine bestimmte Aktion durchgeführt haben, nachdem sie die Kampagne erhalten haben.

Dies wirkt sich nur auf den Test aus, wenn Sie in den vorangegangenen Schritten **Primäre Konversionsrate** gewählt haben.  

## Schritt 6: Überprüfung und Einführung

Überprüfen Sie auf der Bestätigungsseite die Details Ihrer multivariaten Kampagne und starten Sie den Test! Als nächstes lernen Sie, wie Sie [Ihre Testergebnisse verstehen]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/) können.

## Was Sie wissen sollten



- 
-  

### Tipps für verschiedene Kanäle {#tips-different-channels}

   Es gibt zwar Millionen von Möglichkeiten, die Sie mit einem multivariaten und A/B-Test untersuchen können, aber wir haben ein paar Vorschläge für den Anfang:

| Kanal |  |  |
| ---------------------| --------------- | ------------- |
| Push | Kopieren <br> Verwendung von Bildern und Emoji <br> Deeplinks  <br> Darstellung von Zahlen (z.B. "Verdreifachung" gegenüber "Steigerung um 200%")  <br> Darstellung der Zeit (z.B. "endet um Mitternacht" gegenüber "endet in 6 Stunden") | Öffnungen  <br> Konversionsrate |
| E-Mail | Betreff <br> Anzeigename <br> Anrede <br> Textkörper <br> Verwendung von Bildern und Emoji <br> Darstellung von Zahlen (z.B. "Verdreifachung" gegenüber "Steigerung um 200%") <br> Darstellung der Zeit (z.B. "endet um Mitternacht" gegenüber "endet in 6 Stunden") | Öffnungen  <br> Konversionsrate |
| In-App-Nachricht | Aspekte für "Push" aufgelistet <br> [Nachrichtenformat][7] | Klick <br> Konversionsrate |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Vergessen Sie bei der Durchführung von A/B-Tests nicht, [Trichterberichte]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) zu erstellen, die Ihnen Aufschluss darüber geben, wie sich die einzelnen Varianten auf Ihren Konversionstrichter ausgewirkt haben, insbesondere dann, wenn "Konversion" in Ihrem Unternehmen mehrere Schritte oder Aktionen umfasst.
{% endalert %}

Darüber hinaus kann die ideale Länge Ihres Tests je nach Kanal variieren. Denken Sie daran, wie viel Zeit die meisten Nutzer:innen durchschnittlich für das Engagement auf den einzelnen Kanälen benötigen.

 

Wenn Sie sich nicht sicher sind, wie lange Ihr Test laufen soll, kann die Funktion [Intelligente Auswahl][6] nützlich sein, um effizient eine Gewinnvariante zu finden.

### Ein Segment auswählen {#choosing-a-segment}

Da verschiedene Segmente Ihrer Nutzer unterschiedlich auf Nachrichten reagieren können, sagt der Erfolg einer bestimmten Nachricht sowohl etwas über die Nachricht selbst als auch über ihr Zielsegment aus. Versuchen Sie daher, einen Test zu entwerfen, der Ihr Zielsegment berücksichtigt.

Während aktive Nutzer beispielsweise auf "Dieses Angebot läuft morgen ab!" und "Dieses Angebot läuft in 24 Stunden ab!" gleich häufig reagieren, reagieren Nutzer, die die App seit einer Woche nicht mehr geöffnet haben, möglicherweise eher auf die letztere Formulierung, da sie ein stärkeres Gefühl der Dringlichkeit vermittelt.

Außerdem sollten Sie bei der Auswahl des Segments, in dem Sie Ihren Test durchführen möchten, darauf achten, ob die Größe dieses Segments für Ihren Test ausreicht. Im Allgemeinen benötigen multivariate und A/B-Tests mit mehr Varianten eine größere Testgruppe, um statistisch signifikante Ergebnisse zu erzielen. Das liegt daran, dass mehr Varianten dazu führen, dass weniger Nutzer jede einzelne Variante sehen.

{% alert tip %}
Als Richtwert gilt, dass Sie wahrscheinlich etwa 15.000 Nutzer:innen pro Variante (einschließlich der Kontrolle) benötigen, um eine 95%ige Sicherheit Ihrer Testergebnisse zu erreichen.  Für eine genauere Anleitung zu Varianten des Stichprobenumfangs sollten Sie einen [Stichprobenumfangsrechner](https://www.calculator.net/sample-size-calculator.html) heranziehen.
{% endalert %}

### Verzerrung und Zufallsauswahl

 Andere fragen sich manchmal, woher wir wissen, ob diese Zuweisungen wirklich zufällig sind.

Benutzer werden Nachrichtenvarianten, Canvas-Varianten oder ihren jeweiligen Kontrollgruppen zugewiesen, indem ihre (zufällig generierte) Benutzer-ID mit der (zufällig generierten) Kampagnen- oder Canvas-ID verkettet wird, der Modulus dieses Wertes mit 100 genommen wird und die Benutzer dann in Slices eingeteilt werden, die den prozentualen Zuweisungen für die im Dashboard gewählten Varianten und optionalen Kontrollen entsprechen.  Es ist auch nicht sinnvoll, zufälliger (oder genauer gesagt pseudozufällig) als diese Implementierung zu sein.

#### Zu vermeidende Fehler

Es gibt einige häufige Fehler, die den Anschein von Unterschieden je nach Messaging-Kanal erwecken, wenn die Zielgruppen nicht korrekt gefiltert werden.

Wenn Sie zum Beispiel eine Push-Nachricht an eine breite Zielgruppe mit einer Kontrollgruppe senden, wird die Testgruppe nur Nachrichten an Nutzer:innen mit einem Push-Token senden.  In diesem Fall muss Ihre ursprüngliche Zielgruppe für die Kampagne oder das Canvas nach einem Push-Token filtern (`Push Enabled` ist `true`). Das Gleiche gilt für die Berechtigung zum Empfang von Nachrichten auf anderen Kanälen: Opt-in, Push-Token, Abonnement usw.

{% alert note %}

{% endalert %}

[1]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[2]: {% image_buster /assets/img/ab_create_1.png %}
[3]: {% image_buster /assets/img/ab_create_2.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[5]: {% image_buster /assets/img/ab_create_4.png %}
[6]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/

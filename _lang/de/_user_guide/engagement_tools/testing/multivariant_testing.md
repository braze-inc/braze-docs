---
nav_title: Multivariate &amp; A/B-Tests
article_title: Multivariate und A/B-Tests
page_order: 2
page_type: reference
description: "Dieser Referenzartikel erklärt Multivariate und A/B-Tests und ihre Vorteile."
search_rank: 2
---

# Multivariate und A/B-Tests

> Diese Seite erklärt, was eine Multivariate- und A/B-Tests sind und welche Vorteile sie bieten. Wie Sie einen Multivariate-Test oder einen A/B-Test erstellen können, erfahren Sie unter [Erstellen von Multivariate- und A/B-Tests mit Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Die Multivariate- und A/B-Tests können mit [Intelligenter Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) verwendet werden.

## Was sind multivariate und A/B-Tests?

### A/B-Test

Ein A/B-Test ist ein Experiment, bei dem die Reaktionen der Nutzer auf mehrere Versionen derselben Marketingkampagne verglichen werden. Diese Versionen haben ähnliche Marketingziele, unterscheiden sich aber in Wortlaut und Stil.

Ziel ist es, die Version der Kampagne zu ermitteln, die Ihre Marketingziele am besten erreicht. In diesem Abschnitt gehen wir darauf ein, wie Sie die Wirksamkeit der unterschiedlichen Inhalte testen können.

{% alert note %}
Wenn Sie Unterschiede in der Zeitplanung oder im Timing der Nachrichten auswerten möchten (z.B. das Versenden einer Nachricht über einen abgebrochenen Einkaufswagen nach einer Stunde Inaktivität im Vergleich zu einem Tag Inaktivität), lesen Sie unseren Abschnitt über die [Einrichtung eines Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Angenommen, Sie haben zwei Optionen für eine Push-Benachrichtigung:

- "Dieses Angebot läuft morgen aus!"
- "Dieses Angebot läuft in 24 Stunden ab!"

Mit einem A/B-Test können Sie feststellen, welche Formulierung zu einer höheren Konversionsrate führt. Wenn Sie das nächste Mal eine Push-Benachrichtigung über ein Angebot versenden, werden Sie wissen, welche Art der Formulierung effektiver ist. Dieser Test untersucht jedoch nur die Wirkung einer Variablen – die Kopie in der Push-Benachrichtigung.

### Multivariate-Test

Ein Multivariate-Test ähnelt einem A/B-Test, nur dass er die Auswirkungen von zwei oder mehr Variablen testet. Kehren wir zu unserem Beispiel mit den Push-Benachrichtigungen zurück. Eine weitere Variable, die wir vielleicht testen möchten, ist die Frage, ob am Ende der Nachricht ein Emoji eingefügt werden soll. Wir würden nun zwei Variablen (oder Variablen - nicht zu verwechseln mit Varianten) testen, daher der Begriff "multivariat". Dazu müssten wir insgesamt vier Versionen der Nachricht testen - zwei Optionen für die Kopie multipliziert mit zwei Optionen für das Emoji (vorhanden oder nicht) ergibt vier Varianten der Nachricht.

In der Braze-Dokumentation wird der Begriff „Multivariate-Test“ synonym mit „A/B-Test“ verwendet, da das Verfahren für deren Einrichtung dasselbe ist.

## Vorteile von multivariaten und A/B-Tests {#the-benefits-of}

Multivariate-und A/B-Tests bieten Ihnen eine einfache und klare Möglichkeit, mehr über Ihre Zielgruppe zu erfahren. Sie müssen nicht mehr raten, worauf die Nutzer reagieren werden - jede Kampagne ist eine Gelegenheit, verschiedene Varianten einer Nachricht auszuprobieren und die Reaktion der Zielgruppe zu messen.

Zu den spezifischen Szenarien, in denen Multivariate- und A/B-Tests nützlich sein können, gehören:

- **Wenn Sie eine Nachrichtenart zum ersten Mal ausprobieren:** Sind Sie besorgt, dass die In-App-Nachrichten beim ersten Mal nicht richtig funktionieren? Multivariate Tests ermöglichen es Ihnen, zu experimentieren und herauszufinden, was bei Ihren Nutzern ankommt.
- **Bei der Erstellung von Onboarding-Kampagnen und anderen Kampagnen, die ständig gesendet werden:** Da die meisten Ihrer Nutzer mit dieser Kampagne in Berührung kommen werden, sollten Sie dafür sorgen, dass sie so effektiv wie möglich ist.
- **Wenn Sie mehrere Ideen für Nachrichten haben, die Sie senden möchten:** Wenn Sie sich nicht sicher sind, welche Sie wählen sollen, führen Sie einen Test durch und treffen Sie dann eine datengestützte Entscheidung.
- **Wenn Sie untersuchen, ob Ihre Nutzer:innen auf „altbewährte“ Marketingtechniken reagieren:** Marketer halten sich oft an konventionelle Taktiken, um mit den Nutzern und Nutzerinnen in Kontakt zu treten, aber die Nutzerbasis eines jeden Produkts ist anders. Manchmal bringt die Wiederholung Ihrer Handlungsaufforderung und die Verwendung von Social Proof nicht die gewünschten Ergebnisse. Multivariate- und A/B-Tests ermöglichen es Ihnen, über den Tellerrand zu schauen und unkonventionelle Taktiken zu entdecken, die für Ihr spezielle Zielgruppe funktionieren.

### Verteilung der Variationen

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Tipps für multivariate und A/B-Tests

Multivariate und A/B-Tests können Ihnen wichtige Erkenntnisse über Ihre Nutzer liefern. Um Testergebnisse zu erhalten, die das Verhalten Ihrer Nutzer:innen wirklich widerspiegeln, befolgen Sie diese Richtlinien.

#### Führen Sie den Test mit einer großen Anzahl von Benutzern durch

Große Stichproben stellen sicher, dass Ihre Ergebnisse die Präferenzen Ihres durchschnittlichen Nutzers widerspiegeln und weniger durch Ausreißer beeinflusst werden. Größere Stichprobengrößen ermöglichen es Ihnen auch, Gewinnvarianten mit geringeren Gewinnspannen zu identifizieren.

#### Sortieren Sie Benutzer nach dem Zufallsprinzip in verschiedene Testgruppen

Mit multivariaten Tests können Sie bis zu acht zufällig ausgewählte Testgruppen erstellen. Die Randomisierung dient dazu, Verzerrungen in der Testgruppe zu beseitigen und die Wahrscheinlichkeit zu erhöhen, dass die Testgruppen in ihrer Zusammensetzung ähnlich sind. Dadurch wird sichergestellt, dass unterschiedliche Antwortquoten auf Unterschiede in Ihren Nachrichten und nicht auf Ihre Beispiele zurückzuführen sind.

#### Wissen Sie, welche Elemente Sie testen möchten

Multivariate- und A/B-Tests ermöglichen es Ihnen, die Unterschiede zwischen verschiedenen Versionen einer Nachricht zu testen. In manchen Fällen kann ein einfacher Test am effektivsten sein, da Sie durch die Isolierung der Änderungen feststellen können, welche Elemente den größten Einfluss auf die Reaktion hatten. In anderen Fällen können Sie durch die Darstellung von mehr Unterschieden zwischen den Varianten Ausreißer untersuchen und verschiedene Gruppen von Elementen vergleichen. Keine der beiden Methoden ist unbedingt falsch, vorausgesetzt, Sie wissen von Anfang an, was Sie testen möchten.

#### Entscheiden Sie, wie lange Ihr Test laufen soll, und beenden Sie ihn nicht vorzeitig.

Entscheiden Sie vor Beginn des Tests, wie lange er dauern soll, und halten Sie sich daran. Vermarkter sind oft versucht, Tests abzubrechen, sobald sie Ergebnisse sehen, die ihnen gefallen, und damit ihre Ergebnisse zu verfälschen. Widerstehen Sie der Versuchung zu gucken und beenden Sie Ihren Test niemals vorzeitig!

#### Fügen Sie Ihren Test zu Kampagnen hinzu, bevor sie gestartet werden, nicht danach

Wenn Sie Ihren Test zu einer Kampagne hinzufügen, nachdem diese bereits gestartet wurde, wird der Test nicht ordnungsgemäß ausgeführt und Sie erhalten möglicherweise falsche oder irreführende Statistiken. Wenn Sie z.B. einer gestarteten Kampagne einen Test hinzufügen, der einen erneuten Eintritt zulässt, durchlaufen Nutzer:innen bei einem erneuten Eintritt in die Kampagne immer denselben Weg, um Datenungenauigkeiten beim Test zu vermeiden. Wenn Sie außerdem eine der Varianten ändern, während der Test läuft, wird diese Änderung Ihren Test ungültig machen und ihn neu starten.

Für genaue Testergebnisse:
1. Klonen Sie die gestartete Kampagne.
2. Stoppen Sie die ursprüngliche Kampagne.
3. Fügen Sie dann den Test zu der geklonten Kampagne hinzu. 

#### Wenn möglich, schließen Sie eine Kontrollgruppe ein

Wenn Sie eine [Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) einbeziehen, können Sie feststellen, ob Ihre Nachrichten eine größere Auswirkung auf die Konversion der Nutzer haben als wenn Sie gar keine Nachricht senden.



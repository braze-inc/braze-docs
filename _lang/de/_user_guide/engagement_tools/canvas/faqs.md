---
nav_title: FAQ
article_title: Canvas FAQ
page_order: 8
alias: "/canvas_v2_101/"
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Canvas."
tool: Canvas

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Canvas.

### Wie viele Schritte kann ich in ein Canvas aufnehmen?

Sie können bis zu 200 Schritte in einem Canvas hinzufügen.

### Was passiert, wenn die Zielgruppe und die Sendezeit bei einem Canvas, der eine Variante, aber mehrere Verzweigungen hat, identisch sind?

Wir stellen für jeden Schritt einen Auftrag in die Warteschlange – sie laufen etwa zur gleichen Zeit und einer von ihnen „gewinnt". In der Praxis kann dies etwas gleichmäßig verteilt sein, aber es ist wahrscheinlich, dass zumindest eine leichte Tendenz zu dem Schritt besteht, der zuerst erstellt wurde. 

Außerdem können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen Filter für [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) hinzu.

### Kann ich einen Canvas mit nicht verbundenen Schritten starten?

Ja. Sie können Canvase auch nach dem Start mit nicht verbundenen Schritten speichern. 

### Wohin gelangen Nutzer:innen, wenn sie einen nicht verbundenen Schritt erreicht haben?

Wenn sich ein:e Nutzer:in in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, wird er oder sie zum nächsten Schritt vorangebracht, sofern es einen gibt. Die Einstellung des Schritts gibt vor, wie der oder die Nutzer:in vorankommen soll. Dies soll es ermöglichen, Änderungen an Schritten vorzunehmen, ohne sie direkt mit dem Rest des Canvas verbinden zu müssen. Dies gibt Ihnen auch etwas Spielraum zum Testen, bevor Sie sofort live gehen, und ermöglicht es effektiv, einen Entwurf zu speichern.

Wir empfehlen, die Analytics-Ansicht für Nutzer:innen zu überprüfen, die in einem Canvas-Schritt ausstehend sind, bevor Sie die Verbindung zu einem Schritt unterbrechen.

### Was passiert, wenn Sie einen Canvas anhalten?

Wenn Sie einen Canvas anhalten, gilt Folgendes:

- Nutzer:innen werden daran gehindert, den Canvas zu betreten.
- Es werden ungeachtet der aktuellen Position im Ablauf keine weiteren Nachrichten verschickt.
- **Ausnahme:** Canvase mit E-Mails werden nicht sofort gestoppt. Nachdem die Sendeanfragen an SendGrid gesendet wurden, können wir nicht mehr verhindern, dass sie den Nutzer:innen zugestellt werden.

### Soll ich einen Canvas oder separate Canvase pro Nutzerlebenszyklus erstellen?

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie möglicherweise unterschiedliche Ansätze beim Aufbau Ihrer User Journey. Die Flexibilität von Canvas erlaubt es Ihnen, User Journeys für jede Phase des Nutzerlebenszyklus abzubilden. In unseren [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) finden Sie mehrere Beispiele für optimierte Ansätze zur Erstellung effektiver User Journeys.

### Wann werden In-App-Nachrichten in Canvas gesendet?

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet, wenn der oder die Nutzer:in den Canvas-Schritt betritt, bevor der Canvas gestoppt wird, erhält er oder sie die In-App-Nachricht beim nächsten Sitzungsstart, solange die In-App-Nachricht noch nicht abgelaufen ist.

Es ist möglich, dass ein:e Nutzer:in eine Sitzung startet, bevor der Canvas gestoppt wird, die In-App-Nachricht aber nicht sofort angezeigt wird. Dies kann vorkommen, wenn die In-App-Nachricht durch ein angepasstes Event getriggert wird oder verzögert ist. Das bedeutet, dass es für ein:e Nutzer:in möglich ist, eine Impression einer In-App-Nachricht zu protokollieren und die In-App-Nachricht zu „empfangen", nachdem der Canvas gestoppt wurde. Allerdings hätte der oder die Nutzer:in die Sitzung starten müssen, bevor der Canvas gestoppt wurde, aber **nachdem** er oder sie den Canvas-Schritt erhalten hat.

{% alert note %}
Das Anhalten eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User Journey verlassen. Wenn Sie den Canvas wieder aktivieren und Nutzer:innen noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem die Nachricht hätte gesendet werden sollen, ist bereits verstrichen – dann erhalten sie sie nicht).
{% endalert %}

### Wann wird ein Ausnahme-Event getriggert?

Ausnahme-Events triggern nur, während der oder die Nutzer:in auf den Empfang der Canvas-Komponente wartet, mit der sie verknüpft sind. Wenn ein:e Nutzer:in eine Aktion im Voraus durchführt, wird das Ausnahme-Event nicht getriggert. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Event im Voraus durchgeführt haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Wie wirkt sich die Bearbeitung eines Canvas auf Nutzer:innen aus, die sich bereits im Canvas befinden?

Wenn Sie einige der Schritte eines mehrstufigen Canvas bearbeiten, erhalten Nutzer:innen, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie noch nicht für den Schritt ausgewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können, finden Sie unter [Ändern Ihres Canvas nach dem Start]({{site.baseurl}}/post-launch_edits/).

### Wie werden Nutzerkonversionen in einem Canvas verfolgt?

Ein:e Nutzer:in kann nur einmal pro Canvas-Eingang konvertieren. Konversionen werden der letzten Nachricht zugeordnet, die der oder die Nutzer:in für diesen Eingang erhalten hat. Der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konversionen wider, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben oder nicht. Bei jedem weiteren Schritt werden nur Konversionen angezeigt, die stattgefunden haben, während dieser der letzte Schritt war, den der oder die Nutzer:in erhalten hat.

{% alert note %}
Wenn ein:e Nutzer:in ein Canvas erneut betritt, werden Konversions-Events nur für den letzten Eingang getrackt. Konversions-Events werden für frühere Eingänge nicht protokolliert, auch wenn das Konversions-Event rückwirkend erfasst wird.
{% endalert %}

{% details Für Beispiele aufklappen %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsbeginn" („Öffnet die App"):

- Nutzer:in A öffnet die App nach dem Eingang, aber bevor er oder sie die erste Nachricht erhält.
- Nutzer:in B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Konversionen an, während die einzelnen Schritte eine Konversion von eins beim ersten Schritt und null bei allen folgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten zum Zeitpunkt des Konversions-Events aktiv sind, gelten die gleichen Regeln.
{% endalert %}

**Beispiel 2**

Es gibt einen einstufigen Canvas mit aktivierten Ruhezeiten:

1. Nutzer:in betritt den Canvas.
2. Der erste Schritt hat keinen Delay, liegt aber innerhalb der eingestellten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event durch.

**Ergebnis:** Der oder die Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht im Schritt, da er oder sie den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Arten von Konversionsraten?

- Die Gesamtzahl der Canvas-Konversionen gibt an, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Konversionen sie jeweils abgeschlossen haben. 
- Die Varianten-Konversionsrate oder der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konversionen wider, die von Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben, als Gesamtsumme. 
- Die Schritt-Konversionsrate gibt an, wie viele Personen diesen Nachrichtenschritt erhalten und eines der beschriebenen Konversions-Events abgeschlossen haben.

### Was ist der Unterschied zwischen einer Komponente und einem Schritt?

Eine [Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) ist ein einzelner Teil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Komponenten können Aktionen wie die Aufteilung Ihrer User Journey, das Hinzufügen eines Delays und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Schritt in Canvas bezieht sich auf die personalisierte User Journey in Ihren Canvas-Verzweigungen. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre User Journey bilden.

### Wie kann ich die Analytics für jede meiner Canvas-Komponenten anzeigen?

Um die Analytics einer Canvas-Komponente anzuzeigen, gehen Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Hier können Sie die Analytics für jede Komponente einsehen. Weitere Details finden Sie unter [Canvas-Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/).

### Ist Canvas-Analytics oder der Segmenter genauer, wenn es um die Anzahl der eindeutigen Nutzer:innen geht?

Der Segmenter ist eine genauere Statistik für eindeutige Nutzerdaten als Canvas- oder Kampagnenstatistiken. Das liegt daran, dass Canvas- und Kampagnenstatistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert – das bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl anders ist als die des Segmenters. So können Nutzer:innen zum Beispiel mehr als einmal für ein Canvas oder eine Kampagne konvertieren.

### Warum stimmt die Anzahl der Nutzer:innen, die ein Canvas betreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer:innen, die ein Canvas betreten, kann von der erwarteten Anzahl abweichen, da Zielgruppen und Trigger unterschiedlich ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen Trigger für [die Änderung eines Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Dies führt dazu, dass Nutzer:innen aus dem Canvas herausfallen, wenn sie nicht zu Ihrer ausgewählten Zielgruppe gehören, bevor irgendwelche Trigger-Aktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Reise?

Anonyme Nutzer:innen können zwar Canvase betreten und verlassen, aber ihre Aktionen werden erst dann mit einem bestimmten Nutzerprofil verknüpft, wenn sie identifiziert werden. Daher werden ihre Interaktionen in Ihren Analytics möglicherweise nicht vollständig erfasst. Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) verwenden, um einen Bericht über diese Metriken zu erstellen.

### Warum ist die Konversionsrate meines Canvas-Schritts nicht gleich der Gesamtkonversionsrate meiner Canvas-Variante?

Es ist üblich, dass die Gesamtkonversion einer Canvas-Variante größer ist als die Summe der einzelnen Schritte. Dies liegt daran, dass ein:e Nutzer:in ein Konversions-Event für eine Variante durchführen kann, sobald er oder sie die Variante betritt. Dieses Konversions-Event wird jedoch nicht auf einen Canvas-Schritt angerechnet. Jede:r Nutzer:in, der oder die den Canvas betritt und das Konversions-Event ausführt, bevor er oder sie den ersten Canvas-Schritt erhält, wird also in der Gesamtzahl der Varianten-Konversionen gezählt, nicht aber in der Gesamtzahl der Schritte. Dasselbe gilt für Nutzer:innen, die den Canvas betreten, aber den Canvas wieder verlassen, bevor sie einen Schritt erhalten.

### Wie werden Canvas-Zielgruppen ausgewertet? 

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Zeitpunkt des Sendens überprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach dem Empfang eines vorherigen Schritts (oder vor einem Delay) durch.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlerbehebung mit Canvas benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

### Was ist der Unterschied zwischen „Hat keine Canvas-Variante betreten" und „Ist nicht in der Canvas-Kontrollgruppe"?

Vollständige Filter-Definitionen finden Sie unter [Segmentierungs-Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Hat keine Canvas-Variante betreten

Der oder die Nutzer:in hat nie einen Variationspfad eines bestimmten Canvas betreten. Alle Nutzer:innen, die nicht in der Kontrollgruppe sind, werden berücksichtigt, unabhängig davon, ob sie den Canvas betreten haben. Dazu gehören Nutzer:innen, die eine andere Variante betreten haben, und Nutzer:innen, die keine Variante betreten haben. 

#### Ist nicht in der Canvas-Kontrollgruppe

Der oder die Nutzer:in hat den Canvas betreten, ist aber nicht in der Kontrollgruppe und hat daher eine Variante erhalten. Dazu gehören nur Nutzer:innen, die den Canvas betreten haben.

Beachten Sie, dass die Zuweisung von Varianten beim Canvas-Eingang erfolgt. Wenn ein:e Nutzer:in keinen Canvas betreten hat, wird ihm oder ihr keine Variante zugewiesen. Mit anderen Worten: Er oder sie gehört weder zur Kontrollgruppe noch zu einer Variante.

{% details Für FAQs zum ursprünglichen Canvas-Editor aufklappen %}

### Wie konvertiere ich ein bestehendes Canvas aus dem ursprünglichen Editor in den aktuellen Editor?

Sie können [Ihren Canvas klonen]({{site.baseurl}}/cloning_canvases/). Dadurch wird eine Kopie Ihres ursprünglichen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die wichtigsten Unterschiede zwischen dem aktuellen und dem ursprünglichen Canvas-Editor?

#### Symbolleiste der Canvas-Komponenten

Im ursprünglichen Canvas-Editor wurde standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen beliebigen Schritt in Ihrer User Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen den Vorteil einer erhöhten Sichtbarkeit und Anpassung für Ihre Bearbeitungserfahrung bietet. Sie können alle Ihre Canvas-Komponenten sofort in der Canvas-Schritt-Symbolleiste sehen.

#### Schrittverhalten

Zuvor enthielt jeder vollständige Schritt Informationen wie Delay- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppen-Filter, Nachrichtenkonfiguration und Optionen für den Nachrichtenfortschritt – alles in einer Komponente. Dabei handelt es sich im aktuellen Editor um separate Einstellungen, die Ihre Canvas-Erstellung besser anpassbar machen und einige Unterschiede in der Funktionalität mit sich bringen.

#### Fortschritt der Nachrichtenkomponente

[Nachrichtenkomponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) bringen alle Nutzer:innen voran, die den Schritt betreten. Es ist nicht erforderlich, das Verhalten beim Nachrichtenfortschritt festzulegen, was die Konfiguration des gesamten Schritts vereinfacht. Wenn Sie die Option **Weiterleiten, wenn Nachricht gesendet wurde** implementieren möchten, fügen Sie einen separaten Zielgruppenpfad hinzu, um Nutzer:innen zu filtern, die den vorherigen Schritt nicht erhalten haben.  

#### Delay-Verhalten „in"

[Delay-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) warten die gesamte Delay-Zeit ab, bevor sie mit dem nächsten Schritt fortfahren. 

Nehmen wir an, dass wir am 12. April eine Delay-Komponente haben, bei der die Verzögerung so eingestellt ist, dass Ihr:e Nutzer:in an einem Tag um 14 Uhr zum nächsten Schritt weitergeleitet wird. Ein:e Nutzer:in betritt die Komponente am 13. April um 14:01 Uhr. 
- Beim ursprünglichen Workflow würde der oder die Nutzer:in am 14. April um 14 Uhr zum nächsten Schritt übergehen, also weniger als einen Tag nach dem Eingang. 
- Im aktuellen Editor würde der oder die Nutzer:in am 15. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies die gleiche Uhrzeit ist, aber mehr als einen Tag vom Eingangszeitpunkt entfernt. 

#### Verhalten des intelligenten Timings

Da [intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) in der Nachrichtenkomponente gespeichert ist, werden Delays vor den Berechnungen des intelligenten Timings angewendet. Je nachdem, wann ein:e Nutzer:in die Komponente betritt, erhält er oder sie die Nachricht also möglicherweise später als in einem Canvas, das mit dem ursprünglichen Canvas-Workflow erstellt wurde.

Nehmen wir an, Ihr Delay ist auf 2 Tage eingestellt, intelligentes Timing ist aktiviert, und es hat festgestellt, dass die beste Zeit für den Versand Ihrer Nachricht 14 Uhr ist. Ein:e Nutzer:in betritt den Delay-Schritt um 14:01 Uhr.
- **Aktueller Workflow:** Es dauert 48 Stunden, bis das Delay verstrichen ist, sodass der oder die Nutzer:in die Nachricht am dritten Tag um 14 Uhr erhält.
- **Ursprünglicher Workflow:** Der oder die Nutzer:in erhält die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie, dass bei aktiviertem intelligentem Timing die Nachricht innerhalb von 24 Stunden nach dem Betreten der Nachrichtenkomponente durch den oder die Nutzer:in zum festgelegten intelligenten Zeitpunkt gesendet wird (auch wenn keine Delay-Komponente beteiligt ist).

#### Ausnahme-Events

##### Ruhezeiten

Ausnahme-Events werden über Aktionspfade angewendet, die von den Nachrichtenschritten getrennt sind. Die Ruhezeiten werden in der Nachrichtenkomponente durchgesetzt. Das bedeutet: Wenn ein:e Nutzer:in den Aktions-Pfad bereits durchlaufen hat (und nicht mit dem Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten stößt, wenn er oder sie die Nachrichtenkomponente erreicht, und das Canvas so konfiguriert ist, dass die Nachricht nach den Ruhezeiten erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht häufig vorkommt.

Für Segmente und Filter verfügt der Nachrichtenschritt über Zustellungsvalidierungen, die es ermöglichen, zusätzliche Segmente und Filter zu konfigurieren, die zum Zeitpunkt des Versands validiert werden. Dies verhindert den oben genannten Randfall der Ruhezeiten.

##### Zeitplaneinstellung „in" oder „zum nächsten"

Ausnahme-Events werden über Aktionspfade erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster" und nicht „in X-Zeit" oder „zum nächsten X-Zeitpunkt".

{% enddetails %}

### Was sollte ich angeben, wenn ich ein Support-Ticket für einen „Request Timed Out"-Fehler einreiche?

Wenn Sie beim Bearbeiten eines Canvas auf einen „Request Timed Out"-Fehler stoßen und den [Braze-Support]({{site.baseurl}}/braze_support/) kontaktieren müssen, geben Sie die folgenden Informationen an, um die Lösung zu beschleunigen:

- **Bildschirmaufnahme:** Eine Aufnahme der Schritte, die Sie vor dem Auftreten des Fehlers durchgeführt haben, einschließlich aller Seitenwechsel.
- **Zeitstempel und Zeitzone:** Der genaue Zeitpunkt, zu dem der Fehler aufgetreten ist, und Ihre Zeitzone.
- **Browser und Version:** Der Browser, den Sie verwenden (z. B. Chrome 120, Safari 17), und ob Sie versucht haben, den Fehler in einem anderen Browser zu reproduzieren.
- **Schritte zur Reproduktion:** Eine klare Beschreibung der Aktionen, die den Fehler auslösen, einschließlich aller beteiligten Canvas-Schritte oder Konfigurationen.
- **Netzwerkprotokolle (optional):** Öffnen Sie die Entwicklertools Ihres Browsers (Tab **Netzwerk**), reproduzieren Sie den Fehler und exportieren Sie das Netzwerkprotokoll als HTTP-Archiv-Datei (HAR). Dies hilft dem Support-Team zu identifizieren, welcher API-Aufruf das Timeout verursacht.
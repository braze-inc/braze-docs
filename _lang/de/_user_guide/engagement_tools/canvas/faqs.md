---
nav_title: FAQ
article_title: Leinwand FAQ
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

Wir stellen für jeden Schritt einen Auftrag in die Warteschlange - sie laufen etwa zur gleichen Zeit und einer von ihnen "gewinnt". In der Praxis kann dies etwas gleichmäßig sortiert sein, aber es ist wahrscheinlich, dass zumindest eine leichte Tendenz zu dem Schritt besteht, der zuerst erstellt wurde. 

Außerdem können wir keine Garantien dafür geben, wie diese Verteilung genau aussehen wird. Wenn Sie eine gleichmäßige Aufteilung wünschen, fügen Sie einen [Random Bucket Number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) Filter hinzu.

### Kann ich einen Canvas mit nicht verbundenen Schritten starten?

Ja Sie können Canvase auch nach dem Start mit nicht verbundenen Schritten speichern. 

### Wohin gehen die Nutzer:innen, wenn sie eine unterbrochene Stufe erreicht haben?

Wenn sich ein Nutzer:in einem nicht verbundenen Schritt Ihres Canvas-Workflows befindet, wird er zum nächsten Schritt vorgebracht, sofern es einen gibt. Die Einstellung des Schritts gibt vor, wie der Nutzer:in voranzukommen hat. Dies soll es Benutzern ermöglichen, Änderungen an Schritten vorzunehmen, ohne sie direkt mit dem Rest des Canvas zu verbinden. Dies gibt Ihnen auch etwas Spielraum zum Testen, bevor Sie sofort live gehen, denn es ist zulässig, einen Entwurf zu speichern.

Wir empfehlen, die Analytics-Ansicht für Nutzer:innen in einem Canvas-Schritt zu überprüfen, bevor Sie die Verbindung zu einem Schritt unterbrechen.

### Was passiert, wenn Sie einen Canvas anhalten?

Wenn Sie einen Canvas anhalten, gilt Folgendes:

- Die Benutzer werden daran gehindert, den Canvas aufzurufen.
- Es werden ungeachtet der aktuellen Position im Ablauf keine weiteren Nachrichten verschickt.
- **Eine Ausnahme:** Leinwände mit Emails werden nicht sofort gestoppt. Nachdem die Anfragen an SendGrid gesendet wurden, können wir nicht mehr verhindern, dass sie dem Nutzer:innen zugestellt werden.

### Soll ich einen Canvas oder separate Canvase für jeden Nutzerlebenszyklus erstellen?

Je nachdem, was Sie mit Ihrem Canvas erreichen möchten, benötigen Sie unterschiedliche Ansätze, um Ihre Nutzer:innen zu erreichen. Die Flexibilität von Canvas erlaubt es Ihnen, die User Journeys jeder Phase des Nutzerlebenszyklus abzubilden. In unseren [Braze-Canvas-Templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) finden Sie mehrere Beispiele für optimierte Ansätze zur Erstellung effektiver User Journeys.

### Wann werden In-App-Nachrichten in Canvas gesendet?

In-App-Nachrichten werden beim nächsten Sitzungsstart gesendet. Das bedeutet, dass der oder die Nutzer:in, wenn er oder sie den Canvas-Schritt vor dem Beenden der Canvas-Sitzung aufruft, die In-App-Nachricht beim nächsten Sitzungsstart erhält, solange die In-App-Nachricht noch nicht abgelaufen ist.

Zwar kann ein:e Nutzer:in eine Sitzung starten, bevor Canvas beendet wird, aber die In-App-Nachricht wird nicht sofort angezeigt. Dies kann vorkommen, wenn die In-App-Nachricht durch ein angepasstes Event getriggert wird oder sich verzögert. Das bedeutet, dass es für ein:e Nutzer:in möglich ist, eine Impression einer In-App-Nachricht zu protokollieren und die In-App-Nachricht zu „empfangen“, nachdem der Canvas gestoppt wurde. Allerdings hätte der oder die Nutzer:in die Sitzung starten müssen, bevor der Canvas gestoppt wurde, aber **nachdem** er oder sie den Canvas-Schritt erhalten hat.

{% alert note %}
Das Anhalten eines Canvas führt nicht dazu, dass Nutzer:innen, die auf den Empfang von Nachrichten warten, die User Journey verlassen. Wenn Sie die Leinwand wieder aktivieren und die Benutzer immer noch auf die Nachricht warten, erhalten sie diese (es sei denn, der Zeitpunkt, zu dem sie die Nachricht hätten erhalten sollen, ist bereits verstrichen, dann erhalten sie sie nicht).
{% endalert %}

### Wann wird ein Ausnahmeereignis ausgelöst?

Ausnahme-Events triggern nur, während der Nutzer:in auf die Canvas-Komponente wartet, mit der sie verknüpft ist. Wenn ein:e Nutzer:in eine Aktion durchführt, wird das Ausnahme-Event nicht ausgelöst. Wenn Sie Nutzer:innen ausschließen möchten, die ein bestimmtes Ereignis vorgebracht haben, verwenden Sie stattdessen [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

### Wie wirkt sich die Bearbeitung eines Canvas auf Benutzer aus, die sich bereits im Canvas befinden?

Wenn Sie einige der Schritte eines mehrstufigen Canvas bearbeiten, erhalten Benutzer, die bereits in der Zielgruppe waren, aber die Schritte noch nicht erhalten haben, die aktualisierte Version der Nachricht. Beachten Sie, dass dies nur geschieht, wenn sie noch nicht für den Schritt bewertet wurden.

Weitere Informationen darüber, was Sie nach dem Start bearbeiten können, finden Sie unter [Ändern Ihres Canvas nach dem Start]({{site.baseurl}}/post-launch_edits/).

### Wie werden Benutzerkonversionen in einem Canvas verfolgt?

Ein Benutzer kann nur einmal pro Canvas-Eintrag konvertieren. Umrechnungen werden der letzten Nachricht zugeordnet, die der Benutzer für diesen Eintrag erhalten hat. Der Zusammenfassungsblock am Anfang eines Canvas spiegelt alle Konvertierungen wider, die von Benutzern innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben oder nicht. Bei jedem weiteren Schritt werden nur Konversionen angezeigt, die während des letzten Schrittes, den der Nutzer:innen erhalten hat, stattgefunden haben.

{% details Expand for examples %}

**Beispiel 1**

Es gibt einen Canvas-Pfad mit 10 Push-Benachrichtigungen und das Konversions-Event ist „Sitzungsbeginn“ („Öffnet die App“):

- Nutzer:in A öffnet die App nach der Anmeldung, aber bevor er oder sie die erste Nachricht erhält.
- Benutzer B öffnet die App nach jeder Push-Benachrichtigung.

**Ergebnis:** Die Zusammenfassung zeigt zwei Konversionen an, während die einzelnen Schritte eine Konversion von eins beim ersten Schritt und null bei allen folgenden Schritten anzeigen.

{% alert note %}
Wenn Ruhezeiten zum Zeitpunkt des Konversions-Events aktiv sind, gelten die gleichen Regeln.
{% endalert %}

**Beispiel 2**

Es gibt einen einstufigen Canvas mit aktivierten Ruhezeiten:

1. Nutzer:in ruft den Canvas auf.
2. Der erste Schritt hat keinen Delay, liegt aber innerhalb der eingestellten Ruhezeiten, sodass die Nachricht unterdrückt wird.
3. Nutzer:in führt das Konversions-Event durch.

**Ergebnis:** Der Nutzer:in wird in der gesamten Canvas-Variante als konvertiert gezählt, aber nicht der Schritt, da er oder sie den Schritt nicht erhalten hat.

{% enddetails %}

### Was ist der Unterschied zwischen den verschiedenen Arten von Konversionsraten?

- Die Gesamtzahl der Canvas-Konversionen gibt an, wie viele eindeutige Nutzer:innen ein Konversions-Event abgeschlossen haben, nicht wie viele Konversionen sie jeweils abgeschlossen haben. 
- Die Variante Konversionsrate oder der zusammenfassende Block am Anfang eines Canvas spiegelt alle Konversionen wider, die von den Nutzer:innen innerhalb dieses Pfads durchgeführt wurden, unabhängig davon, ob sie eine Nachricht erhalten haben oder nicht, und zwar in einer Gesamtsumme. 
- Die Konversionsrate gibt an, wie viele Personen diese Nachricht erhalten und eines der beschriebenen Konversions-Events abgeschlossen haben.

### Was ist der Unterschied zwischen einer Komponente und einem Schritt?

Eine [Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) ist ein einzelner Teil Ihres Canvas, mit dem Sie die Effektivität Ihres Canvas bestimmen können. Die Komponenten können Aktionen wie die Aufteilung Ihrer Nutzer:innen, das Hinzufügen eines Delays und sogar das Testen mehrerer Canvas-Pfade umfassen. Ein Canvas-Schritt referenziert auf die personalisierte Nutzer:in in Ihren Canvas-Verzweigungen. Im Wesentlichen besteht Ihr Canvas aus einzelnen Komponenten, die Schritte für Ihre Nutzer:innen darstellen.

### Wie kann ich die Analysen für jede meiner Canvas-Komponenten anzeigen?

Um die Analytik einer Canvas-Komponente anzuzeigen, gehen Sie zu Ihrem Canvas und scrollen Sie auf der Seite **Canvas-Details** nach unten. Hier können Sie die Analysen für jede Komponente einsehen. Sehen Sie sich die [Canvas-Analysen]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) für weitere Details an.

### Ist Canvas Analytics oder der Segmenter genauer, wenn es um die Anzahl der einzelnen Benutzer geht?

Der Segmenter ist eine genauere Statistik für eindeutige Benutzerdaten als Canvas- oder Kampagnenstatistiken. Das liegt daran, dass Canvas- und Kampagnen-Statistiken Zahlen sind, die Braze inkrementiert, wenn etwas passiert. Das bedeutet, dass es Variablen gibt, die dazu führen können, dass diese Zahl anders ist als die der Segmentierung. So können Nutzer:innen zum Beispiel mehr als einmal für ein Canvas oder eine Kampagne konvertieren.

### Warum stimmt die Anzahl der Benutzer, die ein Canvas betreten, nicht mit der erwarteten Anzahl überein?

Die Anzahl der Nutzer, die ein Canvas betreten, kann von der von Ihnen erwarteten Anzahl abweichen, da die Zielgruppen und Auslöser ausgewertet werden. In Braze wird eine Zielgruppe vor dem Trigger ausgewertet (es sei denn, Sie verwenden einen Trigger für [die Änderung eines Attributs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Dies führt dazu, dass Nutzer, die nicht zu Ihrer ausgewählten Zielgruppe gehören, aus dem Canvas herausfallen, bevor irgendwelche Auslöseaktionen ausgewertet werden.

### Was passiert mit anonymen Nutzer:innen während ihrer Canvas-Reise?

Anonyme Benutzer können zwar Canvases betreten und verlassen, aber ihre Aktionen werden erst dann mit einem bestimmten Benutzerprofil verknüpft, wenn sie identifiziert werden. Daher werden ihre Interaktionen in Ihren Analysen möglicherweise nicht vollständig erfasst. Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) verwenden, um einen Bericht über diese Metriken zu erstellen.

### Warum ist die Konversionsrate meiner Canvas-Schritte nicht gleich der Gesamtkonversionsrate meiner Canvas-Variante?

Es ist üblich, dass die Gesamtsumme der Umwandlung einer Canvas-Variante größer ist als die Summe der einzelnen Schritte. Dies liegt daran, dass ein Nutzer:innen ein Konversions-Event für eine Variante durchführen kann, sobald er die Variante eingibt. Dieses Konversions-Event wird jedoch nicht auf einen Canvas-Schritt angerechnet. Jeder Nutzer:innen, der den Canvas betritt und das Konversions-Event ausführt, bevor er den ersten Canvas-Schritt erhält, wird also für die Gesamtzahl der Varianten-Konversionen und nicht für die Gesamtzahl der Schritte gezählt. Dasselbe gilt für einen Nutzer:in, der den Canvas betritt, aber den Canvas wieder verlässt, bevor er einen Schritt erhält.

### Wie werden die Canvas-Zuschauer bewertet? 

Standardmäßig werden Filter und Segmente für vollständige Schritte im Canvas zum Zeitpunkt des Sendens überprüft. Der Decision-Split-Schritt führt eine Auswertung direkt nach dem Empfang eines vorherigen Schritts (oder vor einer Verzögerung) durch.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlersuche mit Canvas benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

### Was ist der Unterschied zwischen "Hat nicht an der Canvas-Variante teilgenommen" und "Ist nicht in der Canvas-Kontrollgruppe"?

Vollständige Filter-Definitionen finden Sie unter [Segmentierungs-Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Hat keine Canvas-Variante eingegeben

Der Nutzer:in hat nie einen Variationspfad eines bestimmten Canvas eingegeben. Alle Nutzer:innen, die nicht in der Kontrollgruppe sind, werden berücksichtigt, unabhängig davon, ob sie den Canvas betreten haben. Dazu gehören Nutzer:innen, die eine andere Variante eingegeben haben, und Nutzer:innen, die keine Variante eingegeben haben. 

#### Gehört nicht zur Canvas-Kontrollgruppe

Der Nutzer:in hat den Canvas betreten, ist aber nicht in der Kontrollgruppe und hat daher eine Variation erhalten. Dazu gehören nur Nutzer:innen, die den Canvas betreten haben.

Beachten Sie, dass die Zuweisung von Variationen beim Eingang in Canvas erfolgt. Wenn ein Nutzer:innen keinen Canvas eingegeben hat, wird ihm keine Variante zugewiesen. Mit anderen Worten: Sie gehören weder zur Kontrollgruppe noch zu einer Variante.

{% details Expand for original Canvas editor FAQs %}

### Wie konvertiere ich ein bestehendes Canvas aus dem ursprünglichen Editor in den aktuellen Editor?

Sie können [Ihren Canvas klonen]({{site.baseurl}}/cloning_canvases/). Dadurch wird eine Kopie Ihres ursprünglichen Canvas im aktuellsten Canvas-Workflow erstellt.

### Was sind die wichtigsten Unterschiede zwischen dem aktuellen und dem ursprünglichen Canvas-Editor?

#### Symbolleiste der Canvas-Komponente

Im ursprünglichen Canvas-Editor wurde standardmäßig ein vollständiger Schritt hinzugefügt, wenn Sie einen beliebigen Schritt in Ihrer User Journey erstellt haben. Diese vollständigen Schritte werden durch verschiedene Canvas-Komponenten ersetzt, was Ihnen den Vorteil einer erhöhten Sichtbarkeit und Anpassung an Ihre Bearbeitungserfahrung bietet. Sie können alle Ihre Canvas-Komponenten sofort in der Canvas-Schritt-Symbolleiste sehen.

#### Stufenverhalten

Zuvor enthielt jeder vollständige Schritt Informationen wie Delay- und Zeitplaneinstellungen, Ausnahme-Events, Zielgruppen-Filter, Nachrichtenkonfiguration und Optionen für den Fortschritt von Nachrichten – alles in einer Komponente. Dabei handelt es sich um separate Einstellungen im aktuellen Editor, mit denen Sie Ihre Canvas-Erstellung besser anpassen können und die einige Unterschiede in der Funktionalität mit sich bringen.

#### Weiterentwicklung der Nachrichtenkomponente

[Nachrichten-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) bringen alle Nutzer:innen voran, die den Schritt betreten. Es ist nicht erforderlich, das Verhalten beim Vorbringen von Nachrichten festzulegen, was die Konfiguration des gesamten Schritts vereinfacht. Wenn Sie die Option **Weiterleiten, wenn Nachricht gesendet wurde** implementieren möchten, fügen Sie einen separaten Audience Paths hinzu, um Benutzer zu filtern, die den vorherigen Schritt nicht erhalten haben.  

#### Verzögerung „in“ Verhalten

Die [Delay-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) warten die gesamte Delay-Zeit ab, bevor sie mit dem nächsten Schritt fortfahren. 

Nehmen wir an, dass wir am 12\. April eine Verzögerungskomponente haben, bei der die Verzögerung so eingestellt ist, dass Ihr Benutzer an einem Tag um 14 Uhr zum nächsten Schritt weitergeleitet wird. Ein:e Nutzer:in gibt die Komponente am 13\. April um 14:01 Uhr ein. 
- Bei dem ursprünglichen Workflow würde der Nutzer:innen am 14\. April um 14 Uhr zum nächsten Schritt übergehen, also weniger als einen Tag nach dem Eingang. 
- Im aktuellen Editor würde der Nutzer:innen am 15\. April um 14 Uhr zum nächsten Schritt übergehen. Beachten Sie, dass dies die gleiche Zeit ist, aber mehr als einen Tag von der Entry-Zeit entfernt. 

#### Intelligentes Timing-Verhalten

Da [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) in der Nachrichtenkomponente gespeichert ist, werden Delays vor den Berechnungen des Intelligenten Timings angewendet. Je nachdem, wann ein:e Nutzer:in die Komponente aufruft, erhält er oder sie die Nachricht also möglicherweise später als in einem Canvas, das mit dem ursprünglichen Canvas-Workflow erstellt wurde.

Nehmen wir an, Ihre Verzögerung ist auf 2 Tage eingestellt, Intelligent Timing ist aktiviert, und es hat festgestellt, dass die beste Zeit für den Versand Ihrer Nachricht 14 Uhr ist. Ein:e Nutzer:in betritt den Delay-Schritt um 14:01 Uhr.
- **Aktueller Arbeitsablauf:** Es dauert 48 Stunden, bis die Verzögerung verstrichen ist, so dass der Nutzer:innen die Nachricht am dritten Tag um 14 Uhr erhält.
- **Ursprünglicher Workflow:** Der Benutzer erhält die Nachricht am zweiten Tag um 14 Uhr.

Beachten Sie, dass bei Aktivierung von „Intelligentes Timing“ die Nachricht innerhalb von 24 Stunden nach dem Aufrufen der Nachrichtenkomponente durch den oder die Nutzer:in zum festgelegten intelligenten Zeitpunkt gesendet wird (auch wenn keine Delay-Komponente beteiligt ist).

#### Ausnahme-Events

##### Ruhezeiten

Ausnahme-Events werden über Aktions-Pfade angewendet, die von den Nachrichtenschritten getrennt sind. Die Ruhezeiten werden in der Nachrichtenkomponente durchgesetzt. Das bedeutet, wenn ein Nutzer:innen den Aktions-Pfad bereits durchlaufen hat (und nicht mit dem Ausnahme-Event ausgeschlossen wurde), dann auf Ruhezeiten stößt, wenn er die Komponente Nachricht erreicht, und sein Canvas so konfiguriert hat, dass die Nachricht nach den Ruhezeiten erneut gesendet wird, wird das Ausnahme-Event nicht mehr angewendet. Beachten Sie, dass dieser Anwendungsfall nicht üblich ist.

Für Segmente und Filter verfügt der Schritt Nachricht über Zustellungsvalidierungen, die es den Nutzer:innen ermöglichen, zusätzliche Segmente und Filter zu konfigurieren, die zum Zeitpunkt des Versands validiert werden. Dies verhindert den bereits erwähnten Randfall der Ruhezeiten.

##### Zeitplaneinstellung „in“ oder „nächste“

Ausnahme-Events werden über Aktions-Pfade erstellt. Aktionspfade unterstützen nur „nach einem X-Zeitfenster“ und nicht „in X-Zeit“ oder „zum nächsten X-Zeitpunkt“.

{% enddetails %}
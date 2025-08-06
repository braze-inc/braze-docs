---
nav_title: Logik der Segmentierung
article_title: Logik der Segmentierung 
page_order: 3

page_type: solution
description: "Dieser Hilfe-Artikel erläutert die Unterschiede zwischen UND- und ODER-Operatoren und zeigt Ihnen, wie Sie mit ihnen leistungsstarke Segmente erstellen können."
tool: Segments
---

# Logik der Segmentierung 

Die Operatoren `AND` und `OR` ermöglichen eine leistungsstarke Filterung bei der [Erstellung eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). Mit diesen Operatoren können Sie Ihre Nutzer:innen beim Erstellen Ihrer Kampagnen oder Canvase auf der Grundlage ihrer Aktionen oder Verhaltensweisen im Schritt **Zielgruppe** zusammenstellen.

## Verstehen der Operatoren AND und OR

Die Operatoren `AND` und `OR` funktionieren auf unterschiedliche Weise. Sie können jeden Operator verwenden, je nachdem, was Sie bei der Segmentierung Ihrer Zielgruppe erreichen möchten. 

### Wann Sie den Operator AND verwenden sollten

Im Allgemeinen verwenden Sie `AND`, wenn Sie an der Schnittmenge von zwei oder mehr Werten für ein bestimmtes Attribut interessiert sind.

Lassen Sie uns überlegen, wie Sie in einer Kampagne Nutzer:innen aus allen Ländern außer Kanada und den Vereinigten Staaten zusammenstellen können. In diesem Fall kann die Verwendung des Operators `AND` helfen, diese Nutzer:innen zu filtern. Die Erklärung `Country is not United States AND Country is not Canada` wird nur Nutzer:innen einschließen, die nicht aus den Vereinigten Staaten und nicht aus Kanada stammen. Mit dieser Logik werden also sowohl Nutzer:innen in Kanada als auch in den Vereinigten Staaten ausgeschlossen.

### Wann Sie den OR Operator verwenden sollten

Verwenden Sie `OR`, wenn Ihr Ziel darin besteht, Nutzer:innen anzusprechen, die mindestens eine Bedingung in einer Reihe von Bedingungen erfüllen. Wenn Sie drei Bedingungen haben, die durch `OR` miteinander verbunden sind, dann können eine, zwei oder alle Bedingungen wahr sein, damit die eigentliche Aussage wahr ist.

Stellen Sie sich zum Beispiel vor, dass Sie eine Nachricht an alle Nutzer:innen der Version 1.0 oder 1.1 Ihrer App senden möchten. Um die Nutzer:innen der Version 1.0 und der Version 1.1 zu targetieren, können Sie die Filter `Is 1.0` und `Is 1.1` mit dem Operator `OR` in Ihrem Segment verwenden. Damit werden alle Nutzer:innen mit den Versionen 1.0 oder 1.1 zusammengestellt.

In diesem nächsten Beispiel betrachten wir eine Aktion, die sowohl für Nutzer:innen in den Vereinigten Staaten als auch in Kanada gilt. Sie möchten sicherstellen, dass nur Nutzer:innen in Gebieten, in denen die Aktion gültig ist, die Aktion erhalten. In diesem Szenario verwenden Sie die folgende Anweisung für das Targeting Ihrer Kampagne: `Country is United States OR Country is Canada`. Mit dem Operator `OR` würde Ihre Kampagne nur an Nutzer:innen aus Kanada oder aus den Vereinigten Staaten gehen.

#### Wann Sie den OR Operator vermeiden sollten

Es kann Situationen des Nutzer:in Targeting geben, in denen die Verwendung des Operators `OR` vermieden werden sollte. Der `OR` Operator erstellt eine Aussage, die als wahr ausgewertet wird, wenn ein Nutzer:innen die Kriterien für einen oder mehrere der Filter in einer Aussage erfüllt. Wenn Sie zum Beispiel ein Segment von Nutzern:in erstellen möchten, die zu den "Feinschmeckern" gehören, aber weder zu den "Nicht-Feinschmeckern" noch zu den "Süßigkeiten-Liebhabern", dann würde hier der Operator `OR` funktionieren.

![]({% image_buster /assets/img_archive/or_operator_segment.png %})

Wenn Sie jedoch Nutzer:in segmentieren möchten, die zu dem Segment "Feinschmecker" gehören und nicht zu den Segmenten "Nicht-Feinschmecker" und "Süßigkeiten-Liebhaber", dann verwenden Sie den Operator `AND`. Auf diese Weise befinden sich Nutzer:innen, die die Kampagne oder das Canvas erhalten, in dem beabsichtigten Segment ("Foodies") und nicht gleichzeitig in den anderen Segmenten ("Nicht-Foodies" und "Süßigkeiten-Liebhaber"). 

Die folgenden negativen Targeting-Kriterien sollten nicht mit dem Operator `OR` verwendet werden, wenn zwei oder mehr Filter auf dasselbe Attribut verweisen:

- `is not`
- `does not equal`
- `does not match regex`

Wenn `is not`, `does not equal` oder `does not match regex` zusammen mit dem Operator `OR` zwei- oder mehrmals in einer Anweisung verwendet werden, werden Nutzer:innen mit allen Werten für das betreffende Attribut gezielt angesprochen.

### Beide Operatoren verwenden

In diesem nächsten Beispiel verwenden wir die beiden Operatoren `AND` und `OR`. Hier umfasst die Zielgruppe Nutzer:innen, die Nike-Sneaker oder Adidas-Sneaker gekauft haben und sich für den Erhalt von E-Mail-Benachrichtigungen entschieden haben.

![Erstellung eines Segments für Sneaker-Käufer, bei denen die bevorzugte Marke eines Nutzers:innen Nike oder Adidas ist und die sich für eine E-Mail an]({% image_buster /assets/img_archive/NikeSneakers.png %}) entschieden haben.

Eine weitere Möglichkeit, um sicherzustellen, dass Sie die richtige Logik aufbauen, ist die Erstellung Ihres Segments und die [Vorschau der Nutzer:innen]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/), die auf der Grundlage Ihrer Filter in dieses Segment fallen. Auf diese Weise können Sie sicherstellen, dass die Attribute, die App-Version oder jede andere Segmentierung mit dem übereinstimmt, was Sie sehen.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 3\. Juni 2022_


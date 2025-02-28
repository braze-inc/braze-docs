---
nav_title: Logik der Segmentierung
article_title: Logik der Segmentierung 
page_order: 3

page_type: solution
description: "Dieser Hilfeartikel erläutert die Unterschiede zwischen UND- und ODER-Operatoren und zeigt Ihnen, wie Sie mit ihnen leistungsstarke Segmente erstellen können."
tool: Segments
---

# Logik der Segmentierung 

Die Operatoren `AND` und `OR` ermöglichen eine leistungsstarke Filterung bei der [Erstellung eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). Mithilfe dieser Operatoren können Sie Ihre Nutzer im Schritt **Zielgruppe** bei der Erstellung Ihrer Kampagnen oder Canvases auf der Grundlage ihrer Aktionen oder Verhaltensweisen ansprechen.

## Verstehen der Operatoren AND und OR

Die Operatoren `AND` und `OR` funktionieren auf unterschiedliche Weise. Sie können jeden Operator verwenden, je nachdem, was Sie bei der Segmentierung Ihrer Zielgruppe erreichen möchten. 

### Wann Sie den Operator AND verwenden sollten

Im Allgemeinen verwenden Sie `AND`, wenn Sie an der Schnittmenge von zwei oder mehr Werten für ein bestimmtes Attribut interessiert sind.

Lassen Sie uns überlegen, wie Sie in einer Kampagne Nutzer aus allen Ländern außer Kanada und den Vereinigten Staaten ansprechen können. In diesem Fall kann die Verwendung des `AND` Operators helfen, diese Benutzer zu filtern. Die Erklärung `Country is not United States AND Country is not Canada` wird nur Nutzer umfassen, die nicht aus den Vereinigten Staaten und nicht aus Kanada stammen. Mit dieser Logik werden also sowohl Nutzer in Kanada als auch in den Vereinigten Staaten ausgeschlossen.

### Wann Sie den Operator OR verwenden sollten

Verwenden Sie `OR`, wenn Ihr Ziel darin besteht, Nutzer anzusprechen, die mindestens eine Bedingung aus einer Reihe von Bedingungen erfüllen. Wenn Sie drei Bedingungen haben, die durch `OR` miteinander verbunden sind, dann können eine, zwei oder alle Bedingungen wahr sein, damit die eigentliche Aussage wahr ist.

Stellen Sie sich zum Beispiel vor, dass Sie eine Nachricht an alle Benutzer der Version 1.0 oder 1.1 Ihrer App senden möchten. Um die Benutzer der Version 1.0 und der Version 1.1 zu finden, können Sie die Filter `Is 1.0` und `Is 1.1` mit dem Operator `OR` in Ihrem Segment verwenden. Damit werden alle Benutzer angesprochen, die die Versionen 1.0 oder 1.1 verwenden.

In diesem nächsten Beispiel betrachten wir eine Werbeaktion, die sowohl für Nutzer in den Vereinigten Staaten als auch in Kanada gilt. Sie möchten sicherstellen, dass nur Benutzer in Gebieten, in denen die Aktion gültig ist, die Aktion erhalten. In diesem Szenario verwenden Sie die folgende Anweisung, um Ihre Kampagne zu steuern: `Country is United States OR Country is Canada`. Mit dem Operator `OR` würde Ihre Kampagne nur an Nutzer gehen, deren Land Kanada oder die Vereinigten Staaten ist.

#### Wann Sie den Operator OR vermeiden sollten

Es kann Situationen geben, in denen die Verwendung des `OR` Operators vermieden werden sollte. Der Operator `OR` erstellt eine Aussage, die als wahr ausgewertet wird, wenn ein Benutzer die Kriterien für einen oder mehrere Filter in einer Aussage erfüllt. Wenn Sie z.B. ein Segment von Nutzern erstellen möchten, die zu den "Feinschmeckern" gehören, aber weder zu den "Nicht-Feinschmeckern" noch zu den "Süßigkeiten-Liebhabern", dann würde hier der Operator `OR` funktionieren.

![][1]

Wenn Ihr Ziel jedoch darin besteht, Nutzer zu segmentieren, die zum Segment "Feinschmecker" gehören und nicht zu den Segmenten "Nicht-Feinschmecker" und "Süßigkeiten-Liebhaber", dann verwenden Sie den Operator `AND`. Auf diese Weise befinden sich die Nutzer, die die Kampagne oder das Canvas erhalten, in dem beabsichtigten Segment ("Foodies") und nicht gleichzeitig in den anderen Segmenten ("Nicht-Foodies" und "Süßigkeiten-Liebhaber"). 

Die folgenden negativen Targeting-Kriterien sollten nicht mit dem Operator `OR` verwendet werden, wenn zwei oder mehr Filter auf dasselbe Attribut verweisen:

- `is not`
- `does not equal`
- `does not match regex`

Wenn `is not`, `does not equal` oder `does not match regex` zusammen mit dem Operator `OR` zwei oder mehr Mal in einer Anweisung verwendet werden, werden Benutzer mit allen Werten für das entsprechende Attribut angesprochen.

### Beide Operatoren verwenden

In diesem nächsten Beispiel verwenden wir die beiden Operatoren `AND` und `OR`. In diesem Fall umfasst die Zielgruppe Benutzer, die Nike- oder Adidas-Sneaker gekauft haben und sich für den Erhalt von E-Mail-Benachrichtigungen entschieden haben.

![Aufbau eines Segments für Sneaker-Käufer, deren Lieblingsmarke Nike oder Adidas ist und die sich für E-Mails entschieden haben][33]

Eine weitere Möglichkeit, um sicherzustellen, dass Sie die richtige Logik entwickeln, ist die Erstellung Ihres Segments und [eine Vorschau der Nutzer][35], die auf der Grundlage Ihrer Filter in dieses Segment fallen. Auf diese Weise können Sie sicherstellen, dass die Attribute, die App-Version oder jede andere Segmentierung mit dem übereinstimmt, was Sie sehen.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 3\. Juni 2022_

[1]: {% image_buster /assets/img_archive/or_operator_segment.png %}
[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/

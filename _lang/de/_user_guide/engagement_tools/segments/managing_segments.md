---
nav_title: Segmente verwalten
article_title: Segmente verwalten
page_order: 1
page_type: tutorial
tool: Segments
description: "Dieser Artikel behandelt die Aktionen, die Sie zur Verwaltung Ihrer Segmente durchführen können, z. B. das Filtern einer Liste von Segmenten, das Erstellen von Segmenten und das Bearbeiten von Segmenten."

---

# Segmente verwalten

> Im Abschnitt Segmente können Sie eine umfassende Liste Ihrer bestehenden Segmente einsehen, neue Segmente erstellen und bestehende Segmente bearbeiten. Sie können die Liste der Segmente verfeinern, indem Sie verschiedene Filter und Spalten auswählen, sodass nur die für Sie relevantesten Informationen angezeigt werden.

![Der Abschnitt Segmente zeigt eine Liste der aktiven Segmente an.]({% image_buster /assets/img/segment/segments_page.png %})

## Ihre Ansicht anpassen

Passen Sie Ihre Ansicht der Segmentliste an, indem Sie Filter verwenden und die anzuzeigenden Spalten ändern. Wenn Sie den Abschnitt **Segmente** verlassen und zurückkehren, kehrt die Liste zur Standardansicht zurück und alle zuvor ausgewählten Filter werden zurückgesetzt.

### Status-Filter

Sie können die Liste einschränken, um nur aktive oder archivierte Segmente anzuzeigen. Jedes nicht archivierte Segment gilt als aktiv.

### Filter

Sortieren Sie die Segmente in der Liste, indem Sie die folgenden Filter anpassen:
- **Zuletzt bearbeitet von:** Die Person, die die Segmente zuletzt bearbeitet hat
- **Zuletzt bearbeitet:** Zeitraum, in dem die Segmente zuletzt bearbeitet wurden
- **Geschätzte Größe:** Ungefährer Bereich, wie viele Nutzer:innen sich in den Segmenten befinden
- **Tags:** Mit den Segmenten verknüpfte Tags
- **Teams:** Mit den Segmenten verknüpfte Teams
- **Nur Segmente mit erweitertem Tracking:** Zeigt nur die Segmente an, für die [Analytics Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) aktiviert ist.

### Spalten

Dies sind die Informationsspalten, die Sie für die Anzeige in der Segmentliste auswählen können:
- **Filter:** Anzahl der Filter im Segment
- **Zuletzt bearbeitet:** Datum, an dem das Segment zuletzt bearbeitet wurde
- **Zuletzt bearbeitet von:** Die Person, die das Segment zuletzt bearbeitet hat
- **Tags:** Mit dem Segment verknüpfte Tags
- **Teams:** Mit dem Segment verknüpfte Teams
- **Geschätzte Größe:** Geschätzte Anzahl der Nutzer:innen im Segment
- **Canvase:** Anzahl der Canvase, die das Segment verwenden
- **Kampagnen:** Anzahl der Kampagnen, die das Segment verwenden

### Nur Markierte anzeigen

Wenn Sie **Nur Markierte anzeigen** auswählen, wird Ihre Ansicht auf die Segmente eingegrenzt, die Sie mit einem Stern markiert haben.

## Messaging-Nutzung eines Segments anzeigen {#messaging-use}

Gehen Sie zum Abschnitt **Messaging-Nutzung** eines Segments, um eine Übersicht darüber zu erhalten, wo das Segment verwendet wird – z. B. innerhalb anderer Segmente, Kampagnen und Canvase.

{% alert note %}
Um Schleifen von Segmenten zu verhindern, die sich gegenseitig referenzieren, können Segmente, die den Filter **Segmentzugehörigkeit** verwenden, nicht von anderen Segmenten referenziert werden. Weitere Einzelheiten finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Bestimmte Segmente verwalten

![Das Bearbeitungsmenü für ein Segment mit den Optionen „Bearbeiten", „Duplizieren", „Archivieren" und „Zu Markierten hinzufügen".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Um ein bestimmtes Segment zu verwalten, bewegen Sie den Mauszeiger darüber und wählen Sie das Menüsymbol am Ende der Zeile aus, um die folgenden Optionen anzuzeigen:
- **Bearbeiten:** Bearbeiten Sie die Filter in Ihrem Segment.
- **Duplizieren:** Erstellen Sie eine Kopie Ihres Segments.
- **Archivieren:** Archivieren Sie das Segment. Beachten Sie, dass dadurch auch alle Kampagnen oder Canvase archiviert werden, die dieses Segment verwenden.
- **Zu Markierten hinzufügen:** Markieren Sie das Segment mit einem Stern, sodass Sie schnell darauf zugreifen können, indem Sie im Abschnitt Segmente das Kontrollkästchen „Nur Markierte anzeigen" aktivieren.
 
Sie können auch Massenaktionen durchführen – insbesondere Massenarchivierung und Massen-Tagging –, indem Sie die Kontrollkästchen neben den Namen mehrerer Segmente aktivieren.

![Mehrere Segmente ausgewählt, wobei „CRM" im Dropdown-Feld „Taggen als" ausgewählt ist.]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Änderungen seit letztem Aufruf

Die Anzahl der Aktualisierungen an den Segmenten durch andere Mitglieder Ihres Teams wird über die Metrik *Änderungen seit letztem Aufruf* auf der Segment-Übersichtsseite erfasst. Wählen Sie **Änderungen seit letztem Aufruf** aus, um ein Changelog der Aktualisierungen an Name, Beschreibung und Zielgruppe des Segments anzuzeigen. Bei jeder Aktualisierung können Sie sehen, wer die Änderung durchgeführt hat und wann. Mit diesem Changelog können Sie Änderungen an Ihrem Segment nachvollziehen.

## Nach Segmenten suchen

Suchen Sie nach Segmentnamen, indem Sie Begriffe in das Suchfeld eingeben. 

Es wird nach allen Begriffen und Zeichenfolgen gesucht, die in dieses Feld eingegeben werden. Wenn Sie zum Beispiel nach „test segment 1" suchen, erhalten Sie Segmente mit „test", „segment" oder „1" an beliebiger Stelle in ihrem Namen. Um nach einer exakten Zeichenfolge zu suchen, setzen Sie Anführungszeichen um Ihren Suchbegriff. Die Suche nach ["test segment 1"] gibt alle Segmente zurück, die die genaue Phrase „test segment 1" in ihrem Namen enthalten.

![Die Suchergebnisse für die Eingabe von „all users" in das Suchfeld umfassen „All Users (Test)", „All Users", „All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segmente in Canvasen

Um nach allen Segmentreferenzen zu suchen, einschließlich solcher in anderen Segmenten, Kampagnen oder Canvasen, gehen Sie zum Abschnitt [Messaging-Nutzung](#messaging-use) eines Segments. Der Filter **Zielsegment** auf der **Canvas**-Seite durchsucht nur Canvas-Zielgruppensegmente.

![Filter „Zielsegment" auf der Canvas-Seite.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}
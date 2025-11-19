---
nav_title: Segmente verwalten
article_title: Segmente verwalten
page_order: 1
page_type: tutorial
tool: Segments
description: "Dieser Artikel behandelt die Aktionen, die Sie zur Verwaltung Ihrer Segmente durchführen können, z. B. das Filtern einer Liste von Segmenten, das Erstellen von Segmenten und das Bearbeiten von Segmenten."

---

# Segmente verwalten

> Im Bereich Segmente können Sie eine umfassende Liste Ihrer bestehenden Segmente einsehen, neue Segmente erstellen und bestehende Segmente bearbeiten. Sie können die Liste der Segmente verfeinern, indem Sie eine Vielzahl von Filtern und Spalten auswählen, so dass nur die für Sie wichtigsten Informationen angezeigt werden.

![Der Bereich Segmente zeigt eine Liste der aktiven Segmente an.]({% image_buster /assets/img/segment/segments_page.png %})

## Anpassen Ihrer Ansicht

Passen Sie Ihre Ansicht der Liste der Segmente an, indem Sie Filter verwenden und die Spalten ändern, die angezeigt werden sollen. Wenn Sie den Bereich **Segmente** verlassen und zurückkehren, kehrt die Liste zur Standardansicht zurück und löscht alle zuvor ausgewählten Filter.

### Status-Filter

Sie können die Liste einschränken, um nur aktive oder archivierte Segmente anzuzeigen. Jedes nicht archivierte Segment wird als aktiv betrachtet.

### Filter

Sortieren Sie die Segmente in der Liste, indem Sie die folgenden Filter anpassen:
- **Zuletzt bearbeitet von:** Der Benutzer, der die Segmente zuletzt bearbeitet hat
- **Zuletzt editiert:** Zeitbereich, in dem die Segmente zuletzt bearbeitet wurden
- **Geschätzte Größe:** Ungefährer Bereich, wie viele Nutzer:innen in den Segmenten sind
- **Tags:** Mit den Segmenten verbundene Tags
- **Teams:** Mit den Segmenten verbundene Teams
- **Nur Erweitertes-Tracking-Segmente:** Zeigen Sie nur die Segmente an, für die [Analytics Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) aktiviert ist.

### Spalten

Dies sind die Spalten mit Informationen, die Sie für die Anzeige in der Segmentliste auswählen können:
- **Filter:** Anzahl der Filter im Segment
- **Zuletzt bearbeitet:** Datum, an dem das Segment zuletzt bearbeitet wurde
- **Zuletzt bearbeitet von:** Der Benutzer, der das Segment zuletzt bearbeitet hat
- **Tags:** Mit dem Segment verbundene Tags
- **Teams:** Mit dem Segment verbundene Teams
- **Geschätzte Größe:** Geschätzte Anzahl der Nutzer in dem Segment
- **Canvase:** Anzahl von Leinwänden, die das Segment verwenden
- **Kampagnen:** Anzahl der Kampagnen, die das Segment verwenden

### Nur Markierte anzeigen

Wenn Sie **Nur markierte anzeigen** wählen, wird Ihre Ansicht auf die Segmente eingegrenzt, die Sie markiert haben.

## Anzeigen der Messaging-Nutzung eines Segments

Gehen Sie zum Abschnitt **Messaging-Verwendung** eines Segments, um eine Übersicht darüber zu erhalten, wo das Segment verwendet wird, z. B. innerhalb anderer Segmente, Kampagnen und Canvase.

{% alert note %}
Um zu verhindern, dass Schleifen von Segmenten sich gegenseitig referenzieren, können Segmente, die den Filter **Segmentzugehörigkeit** verwenden, nicht von anderen Segmenten referenziert werden. Weitere Einzelheiten finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Verwaltung bestimmter Segmente

![Das Bearbeitungsmenü für ein Segment mit den Optionen "Bearbeiten", "Duplizieren", "Archivieren" und "Zu Sternchen hinzufügen".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Um ein bestimmtes Segment zu verwalten, bewegen Sie den Mauszeiger über das Segment und wählen Sie das Menüsymbol am Ende der Zeile, um die folgenden Optionen anzuzeigen:
- **Bearbeiten:** Bearbeiten Sie die Filter in Ihrem Segment.
- **Duplikat:** Erstellen Sie eine Kopie Ihres Segments.
- **Archiv:** Archivieren Sie das Segment. Beachten Sie, dass dadurch auch alle Kampagnen oder Canvases, die dieses Segment verwenden, archiviert werden.
- **Zu markierten hinzufügen:** Markieren Sie das Segment mit einem Stern, so dass Sie schnell darauf zugreifen können, indem Sie das Kontrollkästchen Nur mit Sternchen markierte anzeigen im Bereich Segmente aktivieren.
 
Sie können auch Massenaktionen durchführen, insbesondere Massenarchivierung und Massen-Tagging, indem Sie die Kästchen neben den Namen mehrerer Segmente markieren.

![Mehrere Segmente ausgewählt mit "CRM" ausgewählt im Dropdown-Feld "Tag als".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Änderungen seit letztem Aufruf

Die Anzahl der Aktualisierungen der Segmente durch andere Mitglieder Ihres Teams wird durch die Metrik *Änderungen seit letzter Ansicht* auf der Segmentübersichtsseite verfolgt. Wählen Sie **Änderungen seit letzter Ansicht**, um ein Änderungsprotokoll der Aktualisierungen des Namens, der Beschreibung und der Zielgruppe des Segments anzuzeigen. Bei jeder Aktualisierung können Sie sehen, wer die Aktualisierung durchgeführt hat und wann. Mit diesem Changelog können Sie Änderungen an Ihrem Segment überprüfen.

## Suche nach Segmenten
Suchen Sie nach Namen von Segmenten, indem Sie Begriffe in das Suchfeld eingeben. 

Es wird nach allen Begriffen und Zeichenfolgen gesucht, die in dieses Feld eingegeben werden. Wenn Sie zum Beispiel nach "Testsegment 1" suchen, erhalten Sie Segmente mit "Test", "Segment" oder "1" an beliebiger Stelle in ihrem Namen. Um nach einer exakten Zeichenfolge zu suchen, setzen Sie Anführungszeichen um Ihren Suchbegriff. Die Suche nach ["Testsegment 1"] gibt alle Segmente zurück, die die genaue Phrase "Testsegment 1" in ihrem Namen enthalten.

![Die Suchergebnisse für die Eingabe von "alle Nutzer:innen" in das Suchfeld umfassen "Alle Nutzer:innen (Test)", "Alle Nutzer:innen", "Alle Nutzer:innen 15".]({% image_buster /assets/img/segment/segments_search.png %})


---
nav_title: Berichterstattung
article_title: LINE Berichterstattung
page_order: 4
description: "Dieser Referenzartikel behandelt die bei Braze verwendeten LINE-Metriken und wie Sie diese in Ihren LINE-Kampagnen anzeigen können."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# LINE Berichterstattung

> Nachdem Sie Ihre Kampagne oder Canvas gestartet haben, können Sie die wichtigsten Kennzahlen auf der Seite mit den Kampagnendetails oder der Canvas-Analyse einsehen. In diesem Artikel erfahren Sie, wo Sie diese Metriken finden können und was sie bedeuten.

{% alert tip %}
Suchen Sie nach Definitionen für die Begriffe und Kennzahlen in Ihrem Bericht? Weitere Informationen finden Sie im [Glossar zu den Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/).
{% endalert %}

## Kampagnen-Analysen

Auf der Registerkarte **Kampagnenanalyse** können Sie Ihre Berichte in einer Reihe von Panels einsehen. Es kann sein, dass Sie mehr oder weniger als die in den folgenden Abschnitten aufgelisteten sehen, aber jeder hat seinen Zweck.

{% alert note %}
Statistiken zu Aufrufen und Klicks für LINE werden nur berechnet, wenn mehr als 20 Nutzer:innen das Event an einem bestimmten Tag durchführen.
{% endalert %}

### Kampagnendetails

Der Bereich **Kampagnendetails** zeigt einen Überblick über die Leistung Ihrer LINE-Nachrichten.

In diesem Bereich sehen Sie die Gesamtmetriken, wie z.B. die Anzahl der gesendeten Nachrichten an die Anzahl der Empfänger, die primäre Konversionsrate und den Gesamtumsatz, der mit dieser Nachricht erzielt wurde. Auf dieser Seite können Sie auch die Einstellungen für Zustellung, Zielgruppe und Konversion überprüfen.

#### Kontrollgruppen

Um die Wirkung einer einzelnen LINE-Botschaft zu messen, können Sie einem A/B-Test eine [Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) hinzufügen. Der Bereich **Kampagnendetails** auf der obersten Ebene enthält keine Metriken aus der Variante Kontrollgruppe.

### LINE-Performance

Das **LINE-Performance-Panel** zeigt Ihnen, wie gut Ihre Nachricht in verschiedenen Bereichen abgeschnitten hat. Die Metriken in diesem Bereich variieren je nach dem von Ihnen gewählten Nachrichtenkanal und je nachdem, ob Sie einen multivariaten Test durchführen oder nicht. Sie können auf das Symbol <i class="fa fa-eye preview-icon"></i> **Vorschau** klicken, um Ihre Nachricht für jede Variante oder jeden Kanal zu sehen.

\![Das Panel "LINE Performance" zeigt Metriken für zwei Varianten an.]({% image_buster /assets/img/line/line_performance.png %})

Wenn Sie Ihre Ansicht vereinfachen möchten, wählen Sie **\+ Spalten hinzufügen/entfernen** und löschen Sie alle gewünschten Metriken. Standardmäßig werden alle Metriken angezeigt.

#### LINE Metriken

Hier sind einige wichtige LINE-Kennzahlen, die Sie in Ihren Analysen sehen können. Die Definitionen aller LINE-Metriken, die in Braze verwendet werden, finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/).

| Begriff | Definition |
| --- | --- |
| Sendungen | Die Gesamtzahl der Sendungen, die erfolgreich zwischen Braze und LINE übertragen wurden. Dies bedeutet nicht, dass die Nachricht vom Nutzer oder von der Nutzerin empfangen wurde. |
| Eindeutige Öffnungen | Die Gesamtzahl der gesendeten LINE-Nachrichten, die von Nutzern geöffnet wurden, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde. |
| Öffnungen gesamt | Die Gesamtzahl der Male, die die gesendeten LINE-Nachrichten von Nutzern geöffnet wurden, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht worden ist. |
| Eindeutige Klicks | Die Gesamtzahl der gesendeten LINE-Nachrichten, die von Nutzern angeklickt wurden, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde. |
| Klicks gesamt | Die Gesamtzahl der Klicks auf die gesendeten LINE-Nachrichten durch Nutzer, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde. |
{: .reset-td-br-1 .reset-td-br-2 }

### Historische Leistung

Im Bereich **Historische Leistung** können Sie die Metriken aus dem Bereich **Nachrichtenleistung** als Diagramm im Zeitverlauf betrachten. Verwenden Sie die Filter am oberen Rand des Fensters, um die im Diagramm angezeigten Statistiken und Kanäle zu ändern. Der Zeitbereich dieses Diagramms entspricht immer dem oben auf der Seite angegebenen Zeitbereich.

Um eine Aufschlüsselung nach Tagen zu erhalten, wählen Sie das Hamburger-Menü <i class="fas fa-bars"></i> und wählen Sie **CSV herunterladen**, um einen CSV-Export des Berichts zu erhalten.

### Details zum Konversions-Event
 
Das Panel **Details zum Konversions-Event** zeigt Ihnen die Performance Ihrer Konversions-Events für Ihre Kampagne. Weitere Informationen finden Sie unter [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

### Konversionskorrelation

Das Panel **Konversionskorrelation** gibt Ihnen Aufschluss darüber, welche Benutzerattribute und Verhaltensweisen die von Ihnen für Kampagnen festgelegten Ergebnisse fördern oder beeinträchtigen. Weitere Informationen finden Sie unter [Umrechnungskorrelation]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).



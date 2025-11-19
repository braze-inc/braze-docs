---
nav_title: Berichts-Builder (Legacy)
article_title: Berichts-Builder (alt)
alias: /report_builder_legacy/
page_order: 0
page_type: reference
description: "Auf dieser Seite erfahren Sie, wie Sie einen Bericht mit dem Berichts-Builder ausführen, einschließlich der Erstellung von Kampagnen- und Canvas-Vergleichsberichten sowie der Erstellung von Berichten und Charts."
tool: 
  - Reports

---

# Berichts-Builder (alt)

> Der Report-Builder erlaubt es Ihnen, die Ergebnisse mehrerer Kampagnen oder Canvase in einer einzigen Ansicht zu vergleichen, so dass Sie leicht feststellen können, welche Engagement-Strategien Ihre wichtigsten Metriken am meisten beeinflusst haben. Sowohl für Kampagnen als auch für Canvase können Sie Ihre Daten exportieren und Ihren Bericht speichern, um ihn in Zukunft einzusehen.<br><br>Eine beschreibende Liste der Metriken, die Sie in Ihren Berichten finden, finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/).

![Beispiel für einen Kampagnenvergleich]({% image_buster /assets/img/campaign_comparison/campaign_main.png %}){: style="max-width:80%;"}

Nutzen Sie diesen Bericht, um wichtige Fragen zum Engagement zu beantworten, zum Beispiel:

- Welches waren die Kampagnen oder Canvase mit der besten Performance für einen bestimmten Tag oder Kanal?
- Welche Varianten von multivariaten Kampagnen hatten den größten Uplift gegenüber der Kontrolle?  
- Welche saisonale Kampagne führte zu einer höheren Kaufrate? Der Sommerschlussverkauf, der Herbstschlussverkauf oder der Winterschlussverkauf?
- Welche Push-Benachrichtigungen innerhalb dieses Canvas hatten die höchsten Öffnungsraten?
- Welche Schritte in dieser Gruppe von Canvase hatten die meisten Konversionen?
- Hat Version 1 einer Willkommens-E-Mail oder Version 2 einer Willkommens-E-Mail zu höherem Engagement und höherer Konversion geführt? Haben die Änderungen funktioniert?
- Wie wirken sich unterschiedliche Zustellungsmethoden (z. B. 3 geplante Pushs, 3 aktionsbasierte Pushs und 3 API-getriggerte Pushs) auf Ihre Öffnungs-, Konversionsraten oder Kaufraten aus?
- Haben sich die laufenden Verbesserungen bei den Nachrichten von passiven Nutzer:innen im Laufe der Zeit positiv auf Ihre KPIs ausgewirkt?

{% alert tip %}
Versuchen Sie, in allen Kampagnen und Canvase, die Sie vergleichen möchten, dieselben Konversions-Events für Konversion A, B usw. zu verwenden, damit Sie diese Konversionen in Ihren Berichten des Berichts-Builders aneinanderreihen können.
{% endalert %}

## Ausführen eines Berichts

### Schritt 1: Neuen Bericht erstellen

Navigieren Sie auf dem Dashboard zu **Analytics** > **Berichts-Builder.**

Wählen Sie **Neuen Bericht erstellen** und wählen Sie entweder einen Kampagnen-Vergleichsbericht oder einen Canvas-Vergleichsbericht.

Wenn Sie einen Bericht über Kampagnen ausführen möchten, können Sie zwischen einem **manuellen** und einem **automatisierten** Bericht auswählen. Berichte können entweder Kampagnen oder Canvases enthalten, aber nicht beides. Alle Kampagnen und Canvase, die innerhalb der letzten 12 Monate zuletzt Nachrichten gesendet haben, kommen für einen Bericht in Frage.

![Dashboard der Kampagne]({% image_buster /assets/img/campaign_comparison/create_report.png %}){: style="max-width:80%;"}

Im Folgenden finden Sie die Unterschiede zwischen diesen beiden Optionen:

| **Aktion** | **Manuell** | **Automatisch** |
| ---- | ---------- | ------------- |
| **Bericht erstellen** | Sie können Ihre Kampagnenliste mit Hilfe von Filtern eingrenzen und dann bestimmte Kampagnen abhaken. | Sie erstellen Ihren Bericht, indem Sie die Filteroptionen verwenden, um die Kampagnenliste einzugrenzen. |
| **Bericht speichern und ansehen** | Sie können Ihren Bericht speichern. Wenn Sie sie das nächste Mal aufrufen, können Sie dieselbe Kampagne sehen, die Sie zuvor hinzugefügt haben, da diese Kampagnen immer noch unter Ihren "Zuletzt gesendet"-Filter fallen. | Sie können Ihren Bericht speichern. Wenn Sie ihn das nächste Mal aufrufen, wird der Bericht automatisch aktualisiert und enthält alle Kampagnen, die Ihren Filtern entsprechen. |
| **Bericht bearbeiten** | Sie können **Bericht bearbeiten** auswählen, um Kampagnen aus Ihrem Bericht hinzuzufügen oder zu löschen. | Sie können Ihren Bericht bearbeiten, indem Sie die Filterkriterien anpassen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Sowohl **manuelle** als auch **automatisierte** Berichte können bis zu 250 Kampagnen in einem Bericht enthalten.
{% endalert %}

Canvas-Berichte funktionieren ähnlich wie ein manueller Kampagnenbericht, da die Auswahl von Canvas und die Aktualisierung von Berichten ebenfalls manuell erfolgen muss. Sie können maximal fünf Canvase in einen Bericht aufnehmen.

### Schritt 2: Wählen Sie Ihre Metriken

Nachdem Sie Ihren Bericht erstellt haben, finden Sie in jeder Zeile eine leere Tabelle mit Kampagnen. Die Tabelle füllt sich, nachdem Sie **Spalten bearbeiten** ausgewählt und die Metriken ausgewählt haben, die Sie hinzufügen möchten.

![Kampagnen Optionen]({% image_buster /assets/img/campaign_comparison/campaign_comparison_columns.png %}){: style="max-width:80%;"}

Ihre Tabelle wird mit den von Ihnen gewählten Metriken aufgefüllt. Definitionen zu diesen Metriken finden Sie im [Glossar der Berichtsmetriken]({{site.baseurl}}/user_guide/data/report_metrics/). Einige Metriken sind nur für Kampagnen-Vergleichsberichte verfügbar.

Sie können auch die Berechnungen für den **Durchschnitt** einer beliebigen Rate oder numerischen Metrik und für die **Summe** einer beliebigen numerischen Metrik umschalten.

### Schritt 3: Wählen Sie eine Zeitspanne

Sie können einen bestimmten Zeitraum auswählen, für den Berichtsdaten angezeigt werden sollen. Wenn für eine bestimmte Kampagne, ein Canvas, eine Canvas-Variante oder eine Canvas-Komponente keine Daten für den von Ihnen ausgewählten Zeitraum vorliegen, sind die Ergebnisse für diese Zeile leer. 

![Numerische Metrik der Kampagne]({% image_buster /assets/img/campaign_comparison/metric.png %}){: style="max-width:60%;"}

### Schritt 4: Benennen und speichern Sie Ihren Bericht

Benennen Sie Ihren Bericht, bevor Sie ihn speichern. Wenn ein Bericht ohne Namen gespeichert wird, verwendet Braze den Standardnamen "Kampagnenvergleichsbericht".

![Notiz zur Kampagne]({% image_buster /assets/img/campaign_comparison/comparison_name.png %}){: style="max-width:60%;"}

Wenn Sie fertig sind, wählen Sie **Speichern**. Gespeicherte Berichte können zu einem späteren Zeitpunkt auf der Seite **Berichts-Builder** angezeigt werden.

## Kampagnenvergleichsbericht mit multivariaten Kampagnen

Bei allen multivariaten Kampagnen können Sie diese Metriken nach Varianten und Kontrollgruppen aufgeschlüsselt anzeigen, indem Sie auf den Pfeil neben dem Namen der Kampagne klicken. Die Zeilen mit Ihren Varianten enthalten die Performance-Ergebnisse für diese Variante, und die Zeile mit Ihrer Kontrolle enthält nur die Ergebnisse für Ihre Konversions-Events. 

![Notiz zur Kampagne]({% image_buster /assets/img/campaign_comparison/compare_note.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Die Metriken, die die Zeile für Ihre gesamte Kampagne auffüllen, spiegeln die Performance der Varianten wider, enthalten aber nicht die Performance der Kontrolle. Zum Beispiel ist das primäre Konversions-Event A für Ihre gesamte Kampagne die Summe des primären Konversions-Events A für Ihre Varianten, und dies beinhaltet nicht das primäre Konversions-Event A für Ihre Kontrolle.

{% alert important %}
Wenn Sie eine Variante aus einer multivariaten Kampagne löschen, stehen die Daten dieser Variante nicht mehr zur Verwendung in einem zukünftigen Bericht zur Verfügung.
{% endalert %}

## Aufschlüsselung des Canvas-Vergleichsberichts

Innerhalb eines Canvas-Berichts können Sie Ihre Canvase nach Varianten, Schritten oder Nachrichten aufschlüsseln.

### Variante

Wenn Sie die **Aufschlüsselung nach Variante** auswählen, können Sie die Statistiken für Ihre Canvase insgesamt sowie die Statistiken für die einzelnen Varianten einsehen, die durch Auswählen des Pfeils neben dem Namen des Canvas erweitert werden können.

![Varianten]({% image_buster /assets/img/campaign_comparison/campaign_comparison1.png %}){: style="max-width:90%;"}

### Schritte 

Wenn Sie die **Aufschlüsselung nach Schritten** auswählen, können Sie Metriken auf Schrittebene anzeigen, wobei jede Zeile des Berichts die Zeile eines Schritts enthält.

![Steps]({% image_buster /assets/img/campaign_comparison/campaign_comparison2.png %}){: style="max-width:90%;"}

### Nachricht

Ähnlich wie bei der Aufschlüsselung auf Schrittebene zeigt das **Auswählen** der **Aufschlüsselung nach Nachrichten** die Namen der Schritte in jeder Zeile an. Innerhalb der **Bearbeitungsspalten** haben Sie jedoch Zugriff auf Metriken auf Nachrichtenebene, wie z.B. kanalspezifische Statistiken wie E-Mail-Klicks und Push-Öffnungen.

![Bericht]({% image_buster /assets/img/campaign_comparison/campaign_comparison3.png %}){: style="max-width:90%;"}

Beachten Sie, dass Sie im Braze-Dashboard eine Vorschau der ersten 50 Zeilen Ihres Canvas-Berichts sehen können. Sie können auf den vollständigen Bericht zugreifen, wenn Sie eine CSV-Datei exportieren.

## Zugriff auf gespeicherte Berichte

Wenn Sie auf einen gespeicherten **manuellen Bericht** zugreifen, können Sie dieselben Kampagnen sehen, die Sie zuvor hinzugefügt haben, da diese Kampagnen immer noch unter Ihren "Zuletzt gesendet"-Filter fallen.

Wenn Sie auf einen gespeicherten **automatischen Bericht** zugreifen, wird der Bericht automatisch aktualisiert und enthält alle Kampagnen, die Ihren Filtern entsprechen. Wenn Ihr Bericht beispielsweise Kampagnen mit dem Tag "Promotion" gefiltert hat, können Sie jedes Mal, wenn Sie diesen Bericht aufrufen, alle Kampagnen mit dem Tag "Promotion" sehen, auch wenn diese Kampagnen nach der Erstellung dieses Berichts erstellt wurden.

## Berichte bearbeiten

In einem **manuellen Bericht** können Sie einen Bericht bearbeiten, indem Sie **Bearbeiten** auswählen. Von dort aus können Sie Kampagnen auswählen oder die Auswahl aufheben, um sie in Ihren Bericht aufzunehmen.

In einem **automatischen Bericht** schalten Sie einfach die Filter um, um die Ergebnisse in Ihrem Bericht einzugrenzen.

## Berichte exportieren

Sie können auch **Export** auswählen, um Ihren Bericht als CSV-Datei herunterzuladen.

Wenn Ihr Bericht Kampagnen mit mehreren Varianten enthält, enthält der Export zwei CSV-Dateien: 

- Eine Datei, die nur die Metriken der obersten Ebene für jede Kampagne enthält
- Eine Datei, die Metriken auf Variantenebene enthält

Die Datei mit den Metriken für die einzelnen Varianten enthält `variant_` am Anfang des Dateinamens. Wenn Sie zum ersten Mal einen automatisierten Bericht exportieren, erscheint ein Popup-Fenster, in dem Sie aufgefordert werden, das Herunterladen mehrerer Dateien zuzulassen - klicken Sie auf **Zulassen**.

![Kampagne Download]({% image_buster /assets/img/campaign_comparison/download.png %}){: style="max-width:60%;"}

### Canvas-Vergleichsberichte exportieren

Ihr CSV-Export spiegelt die Aufschlüsselungsansicht wider, die Sie beim Auswählen von **Export** gewählt haben. Wenn Sie z.B. die Aufschlüsselung auf Schrittsebene gewählt haben, enthält Ihr Export Daten zu Ihren Metriken für die einzelnen Schritte. Um Daten aus einer anderen Aufschlüsselung zu exportieren, müssen Sie zunächst zu dieser Aufschlüsselung navigieren und dort **Export** auswählen.

Wenn Sie einen Canvas-Bericht zur Aufschlüsselung von Varianten herunterladen, erhalten Sie zwei CSV-Dateien:

- Eine Datei, die nur Metriken der obersten Ebene für jeden Canvas enthält
- Eine Datei, die Metriken auf Variantenebene enthält

## Charts bauen 

Verwenden Sie Diagramme, um eine ausgewählte Kennzahl in Ihrem Bericht zu visualisieren. Diagramme sind für Berichte zu Kampagnen verfügbar, wenn die Spalten mindestens eine Kennzahl enthalten.

![Kampagnen Performance Chart mit ausgewählter Metrik Gesendete Nachrichten]({% image_buster /assets/img/campaign_comparison/report_builder_charts.png %})

Standardmäßig zeigt das Chart in jedem Bericht die Metrik in der ersten Spalte des Berichts an. Weitere Kennzahlen für die Grafik finden Sie im Dropdown-Menü. Jede Metrik in Ihrer Berichtstabelle kann in Ihrem Chart angezeigt werden.

Sie können maximal drei Metriken grafisch darstellen. Die Einheiten für alle Metriken müssen die gleichen sein. Wenn Sie beispielsweise in der ersten Dropdown-Liste einen Kurs auswählen, stehen in der zweiten Dropdown-Liste nur Kurse zur Auswahl.

Wenn Ihr Chart nur eine Metrik enthält, werden bis zu 30 Kampagnen in absteigender Reihenfolge angezeigt, basierend auf der von Ihnen ausgewählten Metrik. Wenn die Metrik Ihres Charts beispielsweise E-Mail-Klicks sind, dann zeigt Ihr Chart die 30 E-Mail Kampagnen mit den meisten Klicks an, geordnet von den meisten bis zu den wenigsten Klicks. Wenn Ihr Bericht mehr als 30 Kampagnen enthält, werden nur die 30 besten im Chart angezeigt. Wenn Sie mehr als eine Metrik auswählen, werden in Ihrem Diagramm nur die fünf besten Kampagnen auf der Grundlage der zuerst ausgewählten Metrik angezeigt.

Diagramme werden derzeit nicht gespeichert, wenn Sie einen Bericht speichern.




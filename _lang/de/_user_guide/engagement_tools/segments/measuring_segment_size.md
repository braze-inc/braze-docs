---
nav_title: Messung der Segmentgröße
article_title: Messung der Segmentgröße
page_order: 9
page_type: reference
tool: 
- Segments
description: "Auf dieser Seite erfahren Sie, wie Sie die Mitgliedschaft und Größe Ihres Segments überwachen können."
---

# Messung der Größe eines Segments

> Auf dieser Seite erfahren Sie, wie Sie die Mitgliedschaft und Größe Ihres Segments überwachen können.

## Berechnung der Segmentzugehörigkeit

Braze aktualisiert die Segmentzugehörigkeit des oder der Nutzer:in, wenn die Daten an unsere Server zurückgesendet und verarbeitet werden, in der Regel sofort. Die Segmentzugehörigkeit eines Nutzers oder einer Nutzerin ändert sich erst, wenn die Sitzung verarbeitet wurde. So wird beispielsweise ein:e Nutzer:in, der oder die beim ersten Start der Sitzung in ein Segment für passive Nutzer:innen fällt, sofort aus dem Segment für passive Nutzer:innen verschoben, wenn die Sitzung verarbeitet wird.

### Berechnung der insgesamt erreichbaren Benutzer

Jedes Segment zeigt die Gesamtzahl der Nutzer:innen an, die zu diesem Segment gehören. Wenn Sie nach **Nutzern aller Apps** filtern, werden auch einige der am häufigsten verwendeten Messaging-Kanäle (wie Web-Push oder E-Mail) und die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle angezeigt. 

Es ist möglich, dass die Anzahl der Gesamtnutzer:innen von der Anzahl der Nutzer:innen abweicht, die über jeden Kanal erreichbar sind. Außerdem sind nicht alle Kanäle in der Tabelle der erreichbaren Nutzer:innen aufgeführt. Zum Beispiel werden Content-Cards, Webhooks und WhatsApp in der Aufschlüsselung nicht angezeigt. Das bedeutet, dass die Gesamtzahl der erreichbaren Nutzer:innen größer sein könnte als die Summe der Nutzer:innen der einzelnen angezeigten Kanäle.

![Eine Tabelle mit der Gesamtzahl der erreichbaren Nutzer:innen, aufgeschlüsselt nach Nutzer:innen, die per E-Mail, iOS Push, Android Push, Web Push, Kindle Push und Android China Push erreichbar sind.][3]

Damit ein:e Nutzer:in als über einen bestimmten Kanal erreichbar aufgeführt wird, muss er oder sie über beides verfügen:
* Eine gültige E-Mail-Adresse oder ein Push-Token, das mit ihrem Profil verknüpft ist; und
* Sie haben sich für Ihre App angemeldet oder abonniert.

Ein einzelner Benutzer kann zu verschiedenen erreichbaren Benutzergruppen gehören. So kann eine Nutzer:in beispielsweise sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beide angemeldet sein, aber kein zugehöriges iOS-Push-Token besitzen. Die Lücke zwischen der Gesamtzahl der erreichbaren Nutzer:innen und der Summe der verschiedenen Kanäle ist die Anzahl der Nutzer:innen, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

## Statistik für Segmentgröße

Die geschätzten Statistiken werden angenähert, indem nur ein Teil Ihres Segments abgetastet wird. Sie sollten also damit rechnen, dass die geschätzten Größen größer oder kleiner sind als der tatsächliche Wert, wobei größere Workspaces potenziell größere Fehlerspannen aufweisen. Um eine genaue Zählung der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Exakte Statistik berechnen**. Die genaue Segmentzugehörigkeit wird immer berechnet, bevor ein Segment von einer Nachricht in einer Kampagne oder einem Canvas betroffen ist.

Braze liefert die folgenden Statistiken zur Segmentgröße. 

### Statistiken filtern

Für jede Filtergruppe können Sie die geschätzten erreichbaren Benutzer anzeigen. Wählen Sie **Zusätzliche Trichterstatistiken erweitern**, um eine Aufschlüsselung nach Kanälen zu sehen.

![Eine Filtergruppe mit einem Filter für ein Geschlecht, das nicht unbekannt ist.][2]{: style="max-width:80%;"}

### Segment-Statistiken

Für ein ganzes Segment können Sie unten auf der Seite die geschätzten erreichbaren Nutzer sowie die geschätzten Nutzerzahlen für jeden Kanal anzeigen. Sie können auch die genaue Anzahl der erreichbaren Nutzer anzeigen (sowohl für das Segment insgesamt als auch pro Kanal), indem Sie die Option **Exakte Statistik berechnen** wählen.

Beachten Sie Folgendes:
- Die Berechnung der genauen Statistiken kann einige Minuten in Anspruch nehmen. Diese Funktion berechnet die genauen Statistiken nur auf Segmentebene, nicht auf Filter- oder Filtergruppenebene.
- Bei großen Segmenten ist es normal, dass selbst bei der Berechnung exakter Statistiken leichte Abweichungen auftreten. Es wird erwartet, dass die Genauigkeit dieses Features 99,999 % oder mehr beträgt.

## Historische Größe der Segmente anzeigen

Für alle Segmente können Sie ein Chart mit der geschätzten Mitgliederzahl der Segmente für jeden Tag anzeigen. Dieses Chart zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentzugehörigkeit nach Datumsbereich zu filtern.

![Verwenden Sie das Dropdown-Menü „Bisherige Zugehörigkeit“, um die Segmentzugehörigkeit nach Datumsbereich zu filtern.][1]

Da das Ziel dieses Charts darin besteht, Ihnen ein Gefühl für die Gesamttrends der Segmentmitgliedschaft zu vermitteln, ist die tägliche Anzahl eine Schätzung, ähnlich wie die Segmentgröße eine Schätzung ist, bevor Sie **Exakte Statistik berechnen** auswählen. Und da dieses Diagramm Schätzungen anzeigt, ist es möglich, dass die Größe Ihres Segments in diesem Chart als "0" erscheint, obwohl die tatsächliche Größe (die nach dem Auswählen von **Genaue Statistiken berechnen** ermittelt werden kann) nicht "0" ist. Es ist besonders wahrscheinlich, dass das Chart eine Schätzung von "0" anzeigt, wenn Ihr Segment im Verhältnis zur Größe Ihrer Workspace-Population sehr klein ist.

Braze schätzt die Anzahl der Segmente, indem es eine Teilmenge Ihrer Nutzer:innen abfragt und diese Ergebnisse dann auf Ihre gesamte Zielgruppe hochrechnet. Das bedeutet, dass die Ergebnisse des Charts nur eine Schätzung der Segmentzugehörigkeit an diesem Tag darstellen und dass sie von Tag zu Tag schwanken können, da für diese Schätzung jeden Tag eine andere Stichprobe von Nutzer:innen abgefragt werden kann.

{% alert note %}
Alle Schätzungen können um ca. 1% der Gesamtbevölkerung Ihres Workspace höher oder niedriger sein als der angezeigte Wert. Bei größeren Workspaces mit mehr Nutzer:innen ist es wahrscheinlicher, dass die Schätzungen von den exakten Berechnungen um einen höheren numerischen Betrag abweichen, auch wenn die Differenz immer noch 1% der Nutzer:innen des Workspace beträgt. Das bedeutet, dass bei großen Workspaces größere Unterschiede zwischen den Schätzungen und den genauen Zählungen zu erwarten sind.
{% endalert %}

### Gründe für wesentliche Änderungen

Die Mitgliederzahl kann sich aus einer Reihe von Gründen, wie den in dieser Tabelle genannten, erheblich ändern.

| Grund | Beispiel |
| --- | --- |
| Normales Verhalten der Nutzer:in | Nutzer:innen abonnieren nach einer besonders erfolgreichen Kampagne. |
| Nutzer:innen werden per CSV importiert | Es wurde eine CSV-Datei mit Nutzer:innen importiert, die die Segmentierung deutlich erhöhte. |
| Segmentierungskriterien für die Zielgruppe werden geändert | Die Regeln für die Zielgruppe eines bestehenden Segments (z.B. Filter) wurden geändert, was zu erheblichen Änderungen in der Segmentierung führte. |
| Nutzer:innen werden gelöscht | Eine erhebliche Anzahl von Nutzer:innen wurde gelöscht. |
| Eine mit Braze synchronisierte Partnerintegration | Ein Dritter hat Daten an Braze gesendet, die die Segmentierung erheblich beeinflusst haben. |
| Inaktive:r Nutzer:in werden archiviert | Eine große Anzahl inaktiver Profile wurde archiviert. Eine große Anzahl von Nutzern:innen, die mit dem CSV-Nutzerimport importiert werden, protokollieren zum Beispiel nie Aktivitäten und werden gleichzeitig archiviert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

[1]: {% image_buster /assets/img_archive/historical_membership2.png %}
[2]: {% image_buster /assets/img_archive/segment_filter_stats.png %}
[3]: {% image_buster /assets/img_archive/segmenter_reachable_users.png %}
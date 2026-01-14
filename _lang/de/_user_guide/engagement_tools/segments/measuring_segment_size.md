---
nav_title: Messung der Größe eines Segments
article_title: Messung der Segmentgröße
page_order: 5
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

![Eine Tabelle mit der Gesamtzahl der erreichbaren Nutzer:innen, aufgeschlüsselt nach Nutzern:innen, die per E-Mail, iOS Push, Android Push, Web-Push und Kindle Push erreichbar sind.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Damit ein:e Nutzer:in als über einen bestimmten Kanal erreichbar aufgeführt wird, muss er oder sie über beides verfügen:
* Eine gültige E-Mail-Adresse oder ein Push-Token, das mit ihrem Profil verknüpft ist; und
* Sie haben sich für Ihre App angemeldet oder abonniert.

Ein einzelner Benutzer kann zu verschiedenen erreichbaren Benutzergruppen gehören. So kann eine Nutzer:in beispielsweise sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beide angemeldet sein, aber kein zugehöriges iOS-Push-Token besitzen. Die Lücke zwischen der Gesamtzahl der erreichbaren Nutzer:innen und der Summe der verschiedenen Kanäle ist die Anzahl der Nutzer:innen, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

## Statistik für Segmentgröße

Die geschätzten Statistiken werden angenähert, indem nur ein Teil Ihres Segments abgetastet wird. Sie sollten also damit rechnen, dass die geschätzten Größen größer oder kleiner sind als der tatsächliche Wert, wobei größere Workspaces potenziell größere Fehlerspannen aufweisen. Um eine genaue Zählung der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Exakte Statistik berechnen**. Die genaue Segmentzugehörigkeit wird immer berechnet, bevor ein Segment von einer Nachricht in einer Kampagne oder einem Canvas betroffen ist. 

Braze liefert die folgenden Statistiken zur Segmentgröße. 

### Statistiken filtern

Für jede Filtergruppe können Sie die geschätzten erreichbaren Benutzer anzeigen. Wählen Sie **Zusätzliche Trichterstatistiken erweitern**, um eine Aufschlüsselung nach Kanälen zu sehen.

![Eine Filtergruppe mit einem Filter für Nutzer:innen, die genau eine Sitzung gezählt haben.]({% image_buster /assets/img_archive/segment_filter_stats.png %}){: style="max-width:80%;"}

## Erreichbare Nutzer:innen Schätzung

Sie können die geschätzten erreichbaren Nutzer:innen eines Segments, einschließlich der geschätzten Anzahl der Nutzer:innen für jeden Kanal, im Panel **Erreichbare Nutzer**:innen einsehen. Diese **Schätzung** zeigt Ihnen eine ungefähre Spanne für die Größe Ihres Segments und eine Schätzung, welcher Prozentsatz Ihrer gesamten Nutzer:innen-Basis in dieses Segment fällt. Beachten Sie, dass die geschätzten Statistiken 15 Minuten lang zwischengespeichert werden, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor. In diesem Fall werden die geschätzten Statistiken automatisch aktualisiert. Sie können auch die genaue Anzahl der erreichbaren Nutzer:innen (sowohl für das Segment insgesamt als auch pro Kanal) anzeigen, indem Sie **Exakte Statistik berechnen** auswählen. 


![Das Panel "Erreichbare Nutzer:innen" zeigt an, dass es schätzungsweise 2.3M-2.4M Nutzer:innen gibt.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Überlegungen zur Schätzung von Zählungen

Braze misst die Anzahl der geschätzten Nutzer:innen, indem es eine Teilmenge Ihrer Nutzer:innen abfragt, und extrapoliert diese Ergebnisse dann auf Ihre gesamte Zielgruppe. Da sich die Untergruppe der Nutzer:innen, die Braze abfragt, bei jeder Berechnung dieser Schätzung ändern kann, kann sich die Schätzung auch in Fällen ändern, in denen Ihre Zielgruppe technisch gesehen gleich bleiben sollte. Wenn Sie beispielsweise Ihre Filter neu anordnen oder dasselbe Segment zu einem anderen Zeitpunkt erneut überprüfen, ist es möglich, dass sich die geschätzte Anzahl ändert (auch wenn **Exakte Statistik berechnen** dieselben Ergebnisse anzeigen würde, wenn sich Ihr Segment nicht geändert hätte).

Wenn Sie in Ihrem Workspace eine große Zahl von Nutzern:innen haben, kann es zu größeren Abweichungen zwischen den geschätzten Zählungen und den exakten Berechnungen kommen, vor allem, wenn Ihr Segment nur einen sehr kleinen Prozentsatz der gesamten Workspace-Population ausmacht. Das liegt daran, dass Braze die Schätzung misst, indem es eine Teilmenge Ihrer Nutzer:innen abfragt und die Ergebnisse auf Ihre gesamte Nutzerbasis extrapoliert. Bei einer größeren Nutzer:innen-Basis sind größere Unterschiede zwischen der geschätzten und der genauen Anzahl zu erwarten.

Sehr kleine Segmente haben einen geschätzten Bereich, der 0 einschließt, was bedeutet, dass der Prozentsatz der gesamten Nutzer:innen auf 0 gerundet werden kann. In diesen Fällen hilft Ihnen die Funktion **Exakte Statistik berechnen** dabei, eine genaue Zählung der Größe Ihres Segments zu erhalten, die in Wirklichkeit nicht 0 sein muss.

![Das seitliche Panel "Erreichbare Nutzer:innen".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Erreichbare Nutzer:innen nach Kanal

Um die Anzahl der Nutzer:innen zu sehen, die für jeden Messaging-Kanal erreichbar sind, wählen Sie **Aufschlüsselung anzeigen** im Panel **Erreichbare Nutzer**:innen. Hier werden einige der am häufigsten genutzten Messaging-Kanäle (wie Web-Push oder E-Mail) und die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle angezeigt. 

Die Metrik _Total_ steht für eindeutige Nutzer:innen. Wenn ein Nutzer:innen zum Beispiel sowohl Android Push als auch iOS Push hat, wird er für beide Zeilen gezählt, aber nur als 1 Nutzer:innen in der Zeile _Gesamt_ gezählt.

Es ist jedoch möglich, dass die Gesamtzahl der Nutzer:innen von der Summe der über die einzelnen Kanäle erreichbaren Nutzer:innen abweicht, da ein einzelner Nutzer zu verschiedenen erreichbaren Nutzergruppen gehören kann. So kann eine Nutzer:in beispielsweise sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beide angemeldet sein, aber kein zugehöriges iOS-Push-Token besitzen. 

Denken Sie daran, dass nicht alle Kanäle in der Tabelle **Erreichbare Nutzer:innen** aufgeführt sind (z.B. Content-Cards, Webhooks und WhatsApp). Wenn Sie beispielsweise Nutzer:innen haben, die nur über Whatsapp erreichbar sind, werden diese zwar in der _Gesamtzahl_, nicht aber in den kanal-spezifischen Zeilen angezeigt. Das bedeutet, dass sich die Gesamtzahl der erreichbaren Nutzer:innen von der Summe der Nutzer:innen für jeden angezeigten Kanal unterscheiden kann.

In den Fällen, in denen die _Summe_ höher ist als die Summe der Kanäle, stellt die Lücke die Anzahl der Nutzer:innen dar, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

Damit ein Nutzer:innen als über einen bestimmten Kanal erreichbar aufgelistet wird, muss der Nutzer:innen:
- Eine gültige E-Mail Adresse oder ein Push-Token, das mit ihrem Profil verknüpft ist, und
- Opt-in oder Abonnent:in für Ihre App.

## Exakte Statistik berechnen 

Um eine genaue Zählung der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Exakte Statistik berechnen** im Bereich **Erreichbare Nutzer:innen**.

Um die Statistiken für eine zuvor durchgeführte Berechnung zu aktualisieren, wählen Sie **Exakte Statistiken aktualisieren**. Das Datum, an dem diese Berechnung zuletzt durchgeführt wurde, wird automatisch aktualisiert.

Beachten Sie, dass die Genauigkeit einer Berechnung nur 99,999% oder mehr beträgt. Bei großen Segmenten werden Sie also möglicherweise leichte Abweichungen feststellen - selbst bei der Berechnung exakter Statistiken -, was normal ist. Außerdem werden die exakten Statistikergebnisse 24 Stunden lang zwischengespeichert, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor. In diesem Fall können Sie die exakten Statistiken neu berechnen.

![Das Panel "Erreichbare Nutzer:innen" mit einer Option zur Anzeige der Aufschlüsselung.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Die Statistiken auf der Ebene der einzelnen Filter werden immer geschätzt, auch wenn Sie exakte Statistiken berechnen. **Exakte Statistiken berechnen** berechnet nur die exakten Statistiken auf der Ebene des Segments, nicht auf der Ebene des Filters oder der Filtergruppe. Diese Berechnung kann einige Minuten in Anspruch nehmen. Insbesondere bei größeren Workspaces kann es vorkommen, dass Sie längere Zeit benötigen, um Berechnungen durchzuführen. Sie können Ihren Fortschritt auf dem Fortschrittsbalken im Panel **Erreichbare Nutzer:innen** verfolgen. Wenn eine Berechnung voraussichtlich länger als fünf Minuten dauert, wird Braze Ihnen die Ergebnisse per E-Mail schicken. 

Braze priorisiert jeweils eine Berechnung pro Workspace, so dass die gleichzeitige Ausführung mehrerer Berechnungen zu Verzögerungen führen kann. Sie können **Warteschlange anzeigen** auswählen, um zu sehen, welche Segmente vor den Ihren liegen, wie weit sie fortgeschritten sind und wer sie initiiert hat. So erhalten Sie eine Idee davon, wann Ihre Berechnung möglicherweise priorisiert wird.

![Eine Warteschlange für Berechnungen mit einer Berechnung.]({% image_buster /assets/img_archive/calculation_queue.png %})

Sie können eine exakte Statistikberechnung abbrechen, indem Sie **Abbrechen** auswählen. Dies kann von Vorteil sein, wenn sich mehrere Berechnungen in der Warteschlange befinden und Sie einer anderen Berechnung den Vorrang geben möchten. 

![Eine aktive Berechnung mit der Option zum Abbrechen]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:25%"}

## Historische Größe der Segmente anzeigen

Für alle Segmente können Sie ein Chart mit der geschätzten Mitgliederzahl der Segmente für jeden Tag anzeigen. Dieses Chart zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentzugehörigkeit nach Datumsbereich zu filtern.

![Verwenden Sie das Dropdown-Menü Historische Mitgliedschaft, um die Mitgliedschaft in Segmenten nach Datumsbereich zu filtern.]({% image_buster /assets/img_archive/historical_membership2.png %})

Da das Ziel dieses Charts darin besteht, Ihnen ein Gefühl für die Gesamttrends der Segmentmitgliedschaft zu vermitteln, ist die tägliche Anzahl eine Schätzung, ähnlich wie die Segmentgröße eine Schätzung ist, bevor Sie **Exakte Statistik berechnen** auswählen. Und da dieses Diagramm Schätzungen anzeigt, ist es möglich, dass die Größe Ihres Segments in diesem Chart als "0" erscheint, obwohl die tatsächliche Größe (die nach dem Auswählen von **Genaue Statistiken berechnen** ermittelt werden kann) nicht "0" ist. Es ist besonders wahrscheinlich, dass das Chart eine Schätzung von "0" anzeigt, wenn Ihr Segment im Verhältnis zur Größe Ihrer Workspace-Population sehr klein ist.

Nehmen wir zum Beispiel an, Ihr Workspace enthält 100 Millionen Nutzer:innen und Ihr Segment hat etwa 700 Nutzer:innen. Es ist möglich, dass an manchen Tagen keine Nutzer:innen in dem Segment sind und keine Nutzer:innen in dem zufälligen Bucket-Bereich landen, der für die Schätzung der historischen Mitgliedschaft verwendet wird, so dass die Anzahl der Mitglieder an einem Tag 0 beträgt.

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

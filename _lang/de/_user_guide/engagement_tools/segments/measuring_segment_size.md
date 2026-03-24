---
nav_title: Segmentgröße messen
article_title: Segmentgröße messen
page_order: 5
page_type: reference
tool: 
- Segments
description: "Auf dieser Seite erfahren Sie, wie Sie die Zugehörigkeit und Größe Ihres Segments überwachen können."
---

# Segmentgröße messen

> Auf dieser Seite erfahren Sie, wie Sie die Zugehörigkeit und Größe Ihres Segments überwachen können.

## Berechnung der Segmentzugehörigkeit

Braze aktualisiert die Segmentzugehörigkeit der Nutzer:innen, sobald die Daten an unsere Server zurückgesendet und verarbeitet werden – in der Regel sofort. Die Segmentzugehörigkeit ändert sich erst, wenn die jeweilige Sitzung verarbeitet wurde. So wird beispielsweise ein:e Nutzer:in, der oder die beim ersten Start der Sitzung in ein Segment für inaktive Nutzer:innen fällt, sofort aus dem Segment für inaktive Nutzer:innen verschoben, wenn die Sitzung verarbeitet wird.

### Berechnung der insgesamt erreichbaren Nutzer:innen

Jedes Segment zeigt die Gesamtzahl der Nutzer:innen an, die zu diesem Segment gehören. Wenn Sie nach **Nutzer:innen aller Apps** filtern, werden auch einige der am häufigsten verwendeten Messaging-Kanäle (wie Web-Push oder E-Mail) und die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle angezeigt. 

Es ist möglich, dass die Gesamtzahl der Nutzer:innen von der Anzahl der über jeden Kanal erreichbaren Nutzer:innen abweicht. Außerdem sind nicht alle Kanäle in der Tabelle der erreichbaren Nutzer:innen aufgeführt. Zum Beispiel werden Content-Cards, Webhooks und WhatsApp in der Aufschlüsselung nicht angezeigt. Das bedeutet, dass die Gesamtzahl der erreichbaren Nutzer:innen größer sein könnte als die Summe der Nutzer:innen der einzelnen angezeigten Kanäle.

![Eine Tabelle, die die Gesamtzahl der erreichbaren Nutzer:innen aufschlüsselt, unterteilt nach Nutzer:innen, die per E-Mail, iOS-Push, Android-Push, Web-Push und Kindle-Push erreichbar sind.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Damit ein:e Nutzer:in als über einen bestimmten Kanal erreichbar aufgeführt wird, muss er oder sie über beides verfügen:
* Eine gültige E-Mail-Adresse oder ein Push-Token, das mit dem Profil verknüpft ist, und
* Opt-in oder Abo für Ihre App.

Ein:e einzelne:r Nutzer:in kann zu verschiedenen erreichbaren Nutzergruppen gehören. So kann ein:e Nutzer:in beispielsweise sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beide angemeldet sein, aber kein zugehöriges iOS-Push-Token besitzen. Die Differenz zwischen der Gesamtzahl der erreichbaren Nutzer:innen und der Summe der verschiedenen Kanäle ist die Anzahl der Nutzer:innen, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

## Statistik für Segmentgröße

Die geschätzten Statistiken werden angenähert, indem nur ein Teil Ihres Segments abgetastet wird. Sie sollten also damit rechnen, dass die geschätzten Größen größer oder kleiner als der tatsächliche Wert ausfallen, wobei größere Workspaces potenziell größere Fehlerspannen aufweisen. Um eine genaue Zählung der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Exakte Statistik berechnen**. Die genaue Segmentzugehörigkeit wird immer berechnet, bevor ein Segment von einer Nachricht in einer Kampagne oder einem Canvas betroffen ist. 

Braze liefert die folgenden Statistiken zur Segmentgröße. 

### Filterstatistiken

Für jede Filtergruppe können Sie die geschätzten erreichbaren Nutzer:innen anzeigen. Wählen Sie **Zusätzliche Funnel-Statistiken erweitern**, um eine Aufschlüsselung nach Kanälen zu sehen.

![Eine Filtergruppe mit einem Filter für Nutzer:innen, die genau eine Sitzung hatten.]({% image_buster /assets/img_archive/segment_filter_stats.png %})

## Schätzung erreichbarer Nutzer:innen

Sie können die geschätzten erreichbaren Nutzer:innen eines gesamten Segments, einschließlich der geschätzten Anzahl der Nutzer:innen für jeden Kanal, im Panel **Erreichbare Nutzer:innen** einsehen. Diese **Schätzung** zeigt Ihnen eine ungefähre Spanne für die Größe Ihres Segments und eine Schätzung, welcher Prozentsatz Ihrer gesamten Nutzerbasis in dieses Segment fällt. Beachten Sie, dass die geschätzten Statistiken 15 Minuten lang zwischengespeichert werden, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor – in diesem Fall werden die geschätzten Statistiken automatisch aktualisiert. Sie können auch die genaue Anzahl der erreichbaren Nutzer:innen (sowohl für das Segment insgesamt als auch pro Kanal) anzeigen, indem Sie **Exakte Statistik berechnen** auswählen. 


![Das Panel „Erreichbare Nutzer:innen" gibt an, dass es schätzungsweise 2,3 bis 2,4 Millionen Nutzer:innen gibt.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Überlegungen zu geschätzten Zählungen

Braze misst die Anzahl der geschätzten Nutzer:innen, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und diese Ergebnisse dann auf Ihre gesamte Zielgruppe extrapoliert werden. Da sich die Teilmenge der Nutzer:innen, die Braze abfragt, bei jeder Berechnung dieser Schätzung ändern kann, kann sich die Schätzung auch in Fällen ändern, in denen Ihre Zielgruppenzugehörigkeit technisch gesehen gleich bleiben sollte. Wenn Sie beispielsweise Ihre Filter neu anordnen oder dasselbe Segment zu einem anderen Zeitpunkt erneut überprüfen, ist es möglich, dass sich die geschätzte Anzahl ändert (auch wenn **Exakte Statistik berechnen** dieselben Ergebnisse anzeigen würde, wenn sich Ihr Segment nicht geändert hätte).

Wenn Sie in Ihrem Workspace eine große Zahl von Nutzer:innen haben, kann es zu größeren Abweichungen zwischen den geschätzten Zählungen und den exakten Berechnungen kommen, vor allem wenn Ihr Segment nur einen sehr kleinen Prozentsatz der gesamten Workspace-Population ausmacht. Das liegt daran, dass Braze die Schätzung ermittelt, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und die Ergebnisse auf Ihre gesamte Nutzerbasis extrapoliert werden. Bei einer größeren Nutzerbasis sind größere Unterschiede zwischen der geschätzten und der genauen Anzahl zu erwarten.

Sehr kleine Segmente haben einen geschätzten Bereich, der 0 einschließt, was bedeutet, dass der Prozentsatz der gesamten Nutzer:innen auf 0 gerundet werden kann. In diesen Fällen hilft Ihnen die Funktion **Exakte Statistik berechnen** dabei, eine genaue Zählung der Größe Ihres Segments zu erhalten, die in Wirklichkeit nicht 0 sein muss.

![Das Panel „Erreichbare Nutzer:innen" zeigt die genaue Anzahl von „31" Nutzer:innen an.]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Erreichbare Nutzer:innen nach Kanal

Um die Anzahl der Nutzer:innen zu sehen, die für jeden Messaging-Kanal erreichbar sind, wählen Sie **Aufschlüsselung anzeigen** im Panel **Erreichbare Nutzer:innen**. Hier werden einige der am häufigsten genutzten Messaging-Kanäle (wie Web-Push oder E-Mail) und die Anzahl der erreichbaren Nutzer:innen für diese spezifischen Kanäle angezeigt. 

Die Metrik _Gesamt_ steht für eindeutige Nutzer:innen. Wenn ein:e Nutzer:in zum Beispiel sowohl Android-Push als auch iOS-Push hat, wird er oder sie für beide Zeilen gezählt, aber nur als 1 Nutzer:in in der Zeile _Gesamt_ berücksichtigt.

Es ist jedoch möglich, dass die Gesamtzahl der Nutzer:innen von der Summe der über die einzelnen Kanäle erreichbaren Nutzer:innen abweicht, da ein:e einzelne:r Nutzer:in zu verschiedenen erreichbaren Nutzergruppen gehören kann. So kann ein:e Nutzer:in beispielsweise sowohl eine gültige E-Mail-Adresse als auch ein gültiges Android-Push-Token haben und für beide angemeldet sein, aber kein zugehöriges iOS-Push-Token besitzen. 

Denken Sie daran, dass nicht alle Kanäle in der Tabelle **Erreichbare Nutzer:innen** aufgeführt sind (z. B. Content-Cards, Webhooks und WhatsApp). Wenn Sie beispielsweise Nutzer:innen haben, die nur über WhatsApp erreichbar sind, werden diese zwar in der _Gesamtzahl_, nicht aber in den kanalspezifischen Zeilen angezeigt. Das bedeutet, dass sich die Gesamtzahl der erreichbaren Nutzer:innen von der Summe der Nutzer:innen für jeden angezeigten Kanal unterscheiden kann.

In den Fällen, in denen die _Gesamtzahl_ höher ist als die Summe der Kanäle, stellt die Differenz die Anzahl der Nutzer:innen dar, die sich für das Segment qualifiziert haben, aber über diese Kommunikationskanäle nicht erreichbar sind.

Damit ein:e Nutzer:in als über einen bestimmten Kanal erreichbar aufgelistet wird, muss er oder sie über Folgendes verfügen:
- Eine gültige E-Mail-Adresse oder ein Push-Token, das mit dem Profil verknüpft ist, und
- Opt-in oder Abo für Ihre App.

#### Angewandte Filter für kanalspezifische erreichbare Nutzer:innen

Die folgenden Filter werden für jeden Kanal angewendet, um die erreichbaren Nutzer:innen zu ermitteln.

| Kanal | Filter |
| --- | --- |
| E-Mail | **E-Mail verfügbar** ist wahr. |
| Push | **Vordergrund-Push aktiviert** ist wahr. |
| SMS | **Abo-Gruppe** ist eine beliebige SMS-Abo-Gruppe. **Ungültige Telefonnummer** ist falsch. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exakte Statistik berechnen 

Um eine genaue Zählung der Nutzer:innen in Ihrem Segment zu erhalten, wählen Sie **Exakte Statistik berechnen** im Bereich **Erreichbare Nutzer:innen**.

Um die Statistiken für eine zuvor durchgeführte Berechnung zu aktualisieren, wählen Sie **Exakte Statistiken aktualisieren**. Das Datum, an dem diese Berechnung zuletzt durchgeführt wurde, wird automatisch aktualisiert.

Beachten Sie, dass die Genauigkeit einer Berechnung nur 99,999 % oder mehr beträgt. Bei großen Segmenten werden Sie also möglicherweise leichte Abweichungen feststellen&#8212;selbst bei der Berechnung exakter Statistiken&#8212;, was normal ist. Außerdem werden die exakten Statistikergebnisse 24 Stunden lang zwischengespeichert, es sei denn, Sie nehmen Änderungen an Ihrem Segment vor. In diesem Fall können Sie die exakten Statistiken neu berechnen.

{% alert note %}
Segmente, die durch [zufällige Bucket-Nummern]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) gleichmäßig aufgeteilt werden, sind nicht gleich groß. Wenn Sie beispielsweise ein Segment mit dem Filter **Zufällige Bucket-Nummer kleiner als 5000** und ein Segment mit dem Filter **Zufällige Bucket-Nummer mindestens 5000** erstellen, ist es möglich und zu erwarten, dass die Segmentgrößen um bis zu einige Prozentpunkte variieren. Dies ist darauf zurückzuführen, dass inaktive Nutzer:innen gelöscht werden und Nutzer:innen möglicherweise nicht erreichbar sind.
{% endalert %}

![Das Panel „Erreichbare Nutzer:innen" mit exakten Statistiken und einem erweiterten Aufschlüsselungsmenü.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

Die Statistiken auf der Ebene der einzelnen Filter werden immer geschätzt, auch wenn Sie exakte Statistiken berechnen. **Exakte Statistik berechnen** berechnet nur die exakten Statistiken auf der Ebene des Segments, nicht auf der Ebene des Filters oder der Filtergruppe. Diese Berechnung kann einige Minuten in Anspruch nehmen. Insbesondere bei größeren Workspaces können längere Zeiträume für die Berechnungen erforderlich sein. Sie können Ihren Fortschritt auf dem Fortschrittsbalken im Panel **Erreichbare Nutzer:innen** verfolgen. Wenn eine Berechnung voraussichtlich länger als fünf Minuten dauert, sendet Braze Ihnen die Ergebnisse per E-Mail. 

Braze priorisiert jeweils eine Berechnung pro Workspace, sodass die gleichzeitige Ausführung mehrerer Berechnungen zu Verzögerungen führen kann. Sie können **Warteschlange anzeigen** auswählen, um zu sehen, welche Segmente vor Ihren liegen, wie weit sie fortgeschritten sind und wer sie initiiert hat. So erhalten Sie eine Idee davon, wann Ihre Berechnung möglicherweise priorisiert wird.

![Eine Berechnungswarteschlange mit einer Berechnung.]({% image_buster /assets/img_archive/calculation_queue.png %})

Sie können eine exakte Statistikberechnung abbrechen, indem Sie **Abbrechen** auswählen. Dies kann von Vorteil sein, wenn sich mehrere Berechnungen in der Warteschlange befinden und Sie einer anderen Berechnung den Vorrang geben möchten. 

![Eine aktive Berechnung mit der Möglichkeit zum Abbrechen]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:35%"}

## Historische Segmentgröße anzeigen

Für alle Segmente können Sie ein Chart mit der historischen Zugehörigkeit anzeigen, das die geschätzte Segmentzugehörigkeit für jeden Tag darstellt. Dieses Chart zeigt, wie sich die Größe Ihres Segments im Laufe der Zeit verändert hat. Verwenden Sie das Dropdown-Menü, um die Segmentzugehörigkeit nach Datumsbereich zu filtern.

![Verwenden Sie das Dropdown-Menü „Bisherige Zugehörigkeit", um die Segmentzugehörigkeit nach Datumsbereich zu filtern.]({% image_buster /assets/img_archive/historical_membership2.png %})

Da das Ziel dieses Charts darin besteht, Ihnen ein Gefühl für die Gesamttrends der Segmentzugehörigkeit zu vermitteln, ist die tägliche Anzahl eine Schätzung – ähnlich wie die Segmentgröße eine Schätzung ist, bevor Sie **Exakte Statistik berechnen** auswählen. Und da dieses Chart Schätzungen anzeigt, ist es möglich, dass die Größe Ihres Segments hier als „0" erscheint, obwohl die tatsächliche Größe (die nach dem Auswählen von **Exakte Statistik berechnen** ermittelt werden kann) nicht „0" ist. Es ist besonders wahrscheinlich, dass das Chart eine Schätzung von „0" anzeigt, wenn Ihr Segment im Verhältnis zur Größe Ihrer Workspace-Population sehr klein ist.

Nehmen wir beispielsweise an, Ihr Workspace umfasst 100 Millionen Nutzer:innen und Ihr Segment hat etwa 700 Nutzer:innen. Es ist möglich, dass an manchen Tagen keine Nutzer:innen in diesem Segment sind und keine Nutzer:innen in den zufälligen Bucket-Bereich fallen, der für die historische Zugehörigkeitsschätzung verwendet wird, was zu einer Tageszählung von 0 führt.

Braze schätzt die Anzahl der Segmentmitglieder, indem eine Teilmenge Ihrer Nutzer:innen abgefragt und diese Ergebnisse dann auf Ihre gesamte Zielgruppe hochgerechnet werden. Das bedeutet, dass die Ergebnisse des Charts nur eine Schätzung der Segmentzugehörigkeit an diesem Tag darstellen und dass sie von Tag zu Tag schwanken können, da für diese Schätzung jeden Tag eine andere Stichprobe von Nutzer:innen abgefragt werden kann.

{% alert note %}
Alle Schätzungen können um ca. 1 % der Gesamtpopulation Ihres Workspace höher oder niedriger sein als der angezeigte Wert. Bei größeren Workspaces mit mehr Nutzer:innen ist es wahrscheinlicher, dass die Schätzungen von den exakten Berechnungen um einen höheren numerischen Betrag abweichen, auch wenn die Differenz immer noch 1 % der Nutzerpopulation des Workspace beträgt. Das bedeutet, dass bei großen Workspaces größere Unterschiede zwischen den Schätzungen und den genauen Zählungen zu erwarten sind.
{% endalert %}

### Gründe für wesentliche Änderungen

Die Zugehörigkeitszahl kann sich aus verschiedenen Gründen erheblich ändern, wie in dieser Tabelle aufgeführt.

| Grund | Beispiel |
| --- | --- |
| Normales Nutzerverhalten | Nutzer:innen abonnieren nach einer besonders erfolgreichen Kampagne. |
| Nutzer:innen werden per CSV importiert | Es wurde eine CSV-Datei mit Nutzer:innen importiert, die die Segmentzugehörigkeit deutlich erhöhte. |
| Zielgruppenkriterien des Segments werden geändert | Die Zielgruppenregeln eines bestehenden Segments (z. B. Filter) wurden geändert, was zu erheblichen Änderungen in der Segmentzugehörigkeit führte. |
| Nutzer:innen werden gelöscht | Eine erhebliche Anzahl von Nutzer:innen wurde gelöscht. |
| Eine Partnerintegration wurde mit Braze synchronisiert | Ein Drittanbieter hat Daten an Braze gesendet, die die Segmentzugehörigkeit erheblich beeinflusst haben. |
| Inaktive Nutzer:innen werden archiviert | Eine große Anzahl inaktiver Profile wurde archiviert. Zum Beispiel protokolliert eine große Anzahl von per CSV importierten Nutzer:innen nie Aktivitäten und wird gleichzeitig archiviert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
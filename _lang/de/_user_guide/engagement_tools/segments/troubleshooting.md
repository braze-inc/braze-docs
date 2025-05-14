---
nav_title: Fehlersuche
article_title: Segmente zur Fehlerbehebung
page_order: 10
page_type: reference
tool: 
  - Segments
description: "Dieser Referenzartikel behandelt die Schritte zur Fehlerbehebung und die Überlegungen, die Sie bei der Verwendung von Segmenten beachten müssen."
---

# Segmente zur Fehlerbehebung

## Benutzerverhalten

### Benutzer ist nicht mehr in einem Segment

Wenn ein Benutzer bei der Erstellung eines Segments nicht verfügbar ist, könnten sich seine Benutzerdaten, die seine Eignung für das Segment bestimmen, aufgrund seiner eigenen Aktivitäten oder anderer Kampagnen und Canvases, mit denen er zuvor interagiert hat, geändert haben. Wenn die erneute Qualifizierung aktiviert ist, werden in ihrem Nutzerprofil die neuesten Daten der erhaltenen Kampagne angezeigt.

### Informationen werden für Nutzer:innen anderer Apps angezeigt, wenn ich einen Filter für eine bestimmte App verwende

Benutzer können mehrere Apps haben. Wenn Sie also eine bestimmte App im Abschnitt **Verwendete Apps** auf der Segmentierungsseite auswählen, erhalten Sie Ergebnisse für Benutzer, die mindestens diese App haben. Der Filter liefert keine Ergebnisse für die Nutzer:innen, die ausschließlich diese App haben.

## Analytik und Berichterstattung

### *Gesendete Nachrichten* oder *eindeutige Empfänger* in Campaign Analytics stimmen nicht mit der Anzahl der Segmente überein 

Wenn die Anzahl der *gesendeten Nachrichten* oder der *eindeutigen Empfänger* in Ihrer Kampagnenanalyse nicht mit der Anzahl der Benutzer im Segmentfilter `Has received message from campaign X` übereinstimmt, kann dies zwei mögliche Gründe haben:

1. **Benutzer können seit dem Start der Kampagne archiviert, verwaist oder gelöscht worden sein.**<br><br>Nehmen wir zum Beispiel an, 1.000 Nutzer:innen erhalten eine Kampagne und Sie machen noch am selben Tag einen CSV-Export. Sie sehen 1.000 gemeldete Benutzer. Im Laufe des nächsten Monats werden 50 dieser 1.000 Nutzer:innen gelöscht (z .B. über den Endpunkt `users/delete`). Wenn Sie einen weiteren CSV-Export durchführen, sehen Sie 950 gemeldete Benutzer, während die Anzahl der *eindeutigen Empfänger* in **Campaign Analytics** immer noch 1.000 beträgt.<br><br>Mit anderen Worten: Die Metrik *Unique Recipients* ist eine inkrementelle Zählung, während der Segmenter und der CSV-Export eine Zählung der aktuell existierenden Benutzer liefert.<br><br>

2. **Die Kampagne ist wiederholbar, sodass Nutzer:innen mehrmals an der Kampagne teilnehmen können.**<br><br>Nehmen wir an, für eine E-Mail-Kampagne ist die Wiederholbarkeit auf null Minuten eingestellt (Benutzer können die Kampagne erneut betreten, solange sie die Anforderungen für das Zielgruppensegment erfüllen), und die Kampagne läuft bereits seit über einem Monat. Die Zahl der *gesendeten Nachrichten* in **Campaign Analytics** würde nicht mit der Zahl im Segment übereinstimmen, da dieses Feld Nachrichten enthalten würde, die an doppelte Benutzer gesendet wurden.<br><br>Das liegt daran, dass Braze einzigartige Benutzer als *einzigartige tägliche Empfänger* zählt, oder die Anzahl der Benutzer, die eine bestimmte Nachricht an einem Tag erhalten haben. Das bedeutet, dass erneut qualifizierte Nutzer:innen mehr als einmal als einmalige:r Empfänger:in gezählt werden, da das Fenster „eindeutig“ nur einen Tag lang geöffnet ist. Dies kann dazu führen, dass die Anzahl der *eindeutigen täglichen Empfänger* höher ist als die Anzahl der Benutzerprofile im CSV-Export. Die Benutzerprofile in der CSV-Datei sind wirklich einzigartig.
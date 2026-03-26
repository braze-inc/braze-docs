---
nav_title: Funnel-Berichte
article_title: Funnel-Berichte für Kampagnen und Canvase
page_order: 6
page_type: reference
description: "Auf dieser Seite erfahren Sie, welche Vorteile Funnel-Berichte bieten, wie Sie sie einrichten und wie Sie Ihren Bericht interpretieren können."
tool: Reports
---

# Funnel-Berichte

> Die Funnel-Berichterstattung bietet einen visuellen Bericht, mit dem Sie die Reise Ihrer Kund:innen nach Erhalt einer Kampagne oder eines Canvas analysieren können. ![Funnel-Bericht 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Wenn Ihre Kampagne oder Ihr Canvas eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie nachvollziehen, wie sich die verschiedenen Varianten auf den Konversionstrichter ausgewirkt haben, und auf Grundlage dieser Daten optimieren.

![Funnel-Bericht 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Funnel-Berichte einrichten

![Funnel-Bericht 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Sie können Funnel-Berichte für bestehende aktive Kampagnen und Canvase ausführen. Diese Berichte zeigen eine Reihe von Ereignissen, die Empfänger:innen im Laufe von 1–30 Tagen ab dem Datum durchlaufen, an dem sie das Canvas oder die Kampagne betreten. Nutzer:innen gelten als konvertiert für einen Schritt im Funnel, wenn sie das Ereignis in der angegebenen Reihenfolge ausführen.

Funnel-Berichte sind an den folgenden Stellen im Dashboard verfügbar:

- Die Seite **Campaign Analytics** für eine bestimmte Kampagne
- Die **Canvas-Detailseite** für ein bestimmtes Canvas über den Button **Varianten analysieren** 

{% alert important %}
Funnel-Berichte sind für [API-Kampagnen]({{site.baseurl}}/api/api_campaigns/) nicht verfügbar.
{% endalert %}

### 1. Schritt: Wählen Sie einen Datumsbereich

Sie können einen Zeitrahmen für Ihren Bericht auswählen (innerhalb der letzten sechs Monate) und die Daten verfeinern, um Nutzer:innen zu sehen, die beim Betreten der Kampagne oder des Canvas die Funnel-Ereignisse innerhalb eines bestimmten Zeitfensters (maximal 30 Tage) abgeschlossen haben. Im folgenden Beispiel würde Ihr Funnel nach Nutzer:innen suchen, die diese Kampagne oder dieses Canvas in den letzten sieben Tagen erhalten und den Funnel innerhalb von drei Tagen abgeschlossen haben.

{% alert note %}
Wenn Sie das Zeitfenster für den Abschluss des Funnels auf einen Tag festlegen, muss das Funnel-Ereignis innerhalb von 24 Stunden nach Erhalt der Nachricht stattfinden. Wenn Sie jedoch mehrere Tage auswählen, wird das Zeitfenster als Kalendertage in der Zeitzone des Unternehmens gezählt.
{% endalert %}

![Funnel-Bericht für ein Canvas, bei dem „Letzte 7 Tage" im Zeitrahmen-Dropdown ausgewählt ist.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### 2. Schritt: Ereignisse für Funnel-Schritte auswählen

Bei jedem Funnel-Bericht ist das erste Ereignis der Empfang Ihrer Nachricht durch die Nutzer:innen. Die nachfolgenden Ereignisse, die Sie auswählen, filtern die Anzahl der Nutzer:innen, die sowohl diese als auch die vorherigen Ereignisse durchgeführt haben. 

#### Verfügbare Funnel-Bericht-Ereignisse

| Kampagne | Sitzung gestartet, Kauf getätigt, angepasstes Event durchgeführt, Nachrichten-Engagement-Event |
| Canvas | Sitzung gestartet, Kauf getätigt, angepasstes Event durchgeführt, Canvas-Schritt erhalten, mit Schritt interagiert |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Das Berichtsereignis **Mit Schritt interagiert** kann nur mit Canvas-Schritten verwendet werden, die den E-Mail- oder Push-Messaging-Kanal nutzen.
{% endalert %}

![Funnel-Bericht für ein Canvas mit einer Dropdown-Liste der verfügbaren Berichtsereignisse.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Funnel-Berichte ermöglichen es Ihnen, den Erfolg Ihrer Nachrichten über die Konversions-Events oder Engagement-Events hinaus zu vergleichen, die Sie ursprünglich eingerichtet haben. Wenn es also ein Konversions-Event gibt, das Sie ursprünglich nicht hinzugefügt haben, können Sie die Konversionen für dieses Event dennoch mit einem Funnel tracken.

Wenn Sie zum Beispiel ein 14-tägiges Berichtszeitfenster auswählen, gefolgt von den Ereignissen `Added to cart` und `Made purchase`, sehen Sie sowohl die Anzahl der Nutzer:innen, die innerhalb von 14 Tagen nach Erhalt der Nachricht etwas in den Warenkorb gelegt haben, als auch die Anzahl der Nutzer:innen, die innerhalb von 14 Tagen nach Erhalt der Kampagne etwas in den Warenkorb gelegt und dann einen Kauf getätigt haben.

Ein anderes Beispiel: Sie möchten vielleicht den Prozentsatz der Nutzer:innen sehen, die nach dem Klick auf eine E-Mail konvertiert haben. Um dies zu berechnen, könnten Sie einen Bericht erstellen, bei dem das zweite Ereignis der Klick auf Ihre E-Mail und das dritte Ereignis die Durchführung Ihres Konversions-Events ist.

Nachdem Sie **Bericht erstellen** ausgewählt haben, kann die Erstellung des Funnel-Berichts einige Minuten dauern. Während dieser Zeit können Sie vom Bericht aus zu anderen Seiten im Dashboard navigieren. Sie erhalten eine Benachrichtigung im Dashboard, wenn Ihr Bericht fertig ist.

## Interpretation Ihres Funnel-Berichts

In Ihrem Funnel-Bericht können Sie die Kontrollgruppe direkt mit den von Ihnen eingerichteten Varianten vergleichen. Jedes aufeinanderfolgende Ereignis zeigt an, wie viel Prozent der vorherigen Nutzer:innen diese Aktion abgeschlossen und durch den Funnel konvertiert haben.

### Bestandteile des Funnel-Berichts

- **Horizontale Achse**: Zeigt den Prozentsatz der Empfänger:innen an, die diese Aktionen durchgeführt haben. 
- **Chart**: Zeigt die Anzahl der erhaltenen Nachrichten, die Anzahl der Nutzer:innen, die die vorherigen Aktionen durchgeführt haben, sowie die von Ihnen gewählte Aktion, die Konversionsrate und die prozentuale Veränderung gegenüber der Kontrollgruppe.
- **Option „Neu generieren"**: Ermöglicht Ihnen, Ihren Bericht neu zu generieren, und zeigt an, wann der aktuelle Bericht zuletzt erstellt wurde. 
- **Varianten**: Der durch farbige Spalten gekennzeichnete Funnel-Bericht lässt bis zu 8 Varianten und eine Kontrollgruppe zu. Standardmäßig werden im **Chart** nur drei Varianten angezeigt. Um mehr zu sehen, können Sie die restlichen Varianten manuell auswählen.

![Funnel-Bericht-Chart.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Für Kampagnen mit mehreren Varianten**: Braze zeigt eine Tabelle mit Metriken für jedes Ereignis und jede Variante sowie die prozentuale Veränderung gegenüber der Kontrollgruppe an. Die Konversionsrate ist die Anzahl der Nutzer:innen, die das Ereignis (und die nachfolgenden) durchgeführt haben, pro Empfänger:in der Nachricht.

**Für Kampagnen mit Wiederwählbarkeit**: Wenn Nutzer:innen die Kampagne innerhalb des Berichtszeitfensters mehr als einmal erhalten, bestimmt Braze anhand der Aktionen, die diese Nutzer:innen nach dem ersten Erhalt der Kampagne innerhalb des Zeitfensters durchgeführt haben, ob sie in den Funnel aufgenommen werden sollen.
- Beachten Sie, dass es eine Diskrepanz zwischen den Funnel- und den Standard-Konversionswerten geben kann, da Nutzer:innen bei Wiederwählbarkeit mehrmals konvertieren können, Funnel-Berichte jedoch maximal eine Konversion zählen, auch wenn Nutzer:innen das Event mehr als einmal durchführen. 

**Für multivariate Kampagnen mit Wiederwählbarkeit**: Wenn Nutzer:innen innerhalb des Berichtszeitfensters mehrere Varianten aus der Kampagne erhalten, bestimmt Braze anhand der Aktionen, die diese Nutzer:innen nach dem ersten Erhalt der Kampagnenvariante durchgeführt haben, ob sie in den Varianten-Funnel aufgenommen werden sollen. Das bedeutet, dass ein und dieselbe Nutzer:in auf mehrere verschiedene Varianten angerechnet werden kann, wenn sie während des Zeitfensters für den Funnel mehrere Varianten erhalten hat.

{% alert important %}
Verwaiste Nutzer:innen werden in Funnel-Berichten nicht getrackt. Wenn anonyme Nutzer:innen ein Canvas oder eine Kampagne betreten und später über die Methode `changeUser()` identifiziert werden, ändert sich ihre Braze-ID. Funnel-Berichte verfolgen nur Follow-up-Ereignisse, die mit der Nutzer-ID zum Zeitpunkt des Eingangs übereinstimmen, und berücksichtigen keine Ereignisse, die Nutzer:innen nach dem Wechsel ihrer ID durchführen. Das bedeutet, dass Konversions-Events, die Nutzer:innen nach ihrer Identifizierung durchführen, nicht in den Funnel-Bericht aufgenommen werden.
{% endalert %}

## Häufig gestellte Fragen

### Warum unterscheiden sich die Analytics im Canvas vom Funnel-Bericht?

Canvas-Analytics auf Schrittebene und Funnel-Berichte verwenden unterschiedliche Geltungsregeln für denselben Datumsbereich und stimmen daher nicht zwangsläufig überein. Die Unterschiede ergeben sich daraus, wie jeder Bericht definiert, „welche Ereignisse zählen".

**Canvas-Analytics (Varianten analysieren):** Der Datumsbereich filtert Ereignisse danach, **wann sie stattgefunden haben**. Wenn Sie den 1.–7. Januar auswählen, sehen Sie alle Eintritte und Konversions-Events, die in diesem Zeitfenster stattgefunden haben – unabhängig davon, wann die Nutzer:innen das Canvas betreten haben. Nutzer:innen, die am 1. Januar eingetreten sind, aber am 8. Januar konvertiert haben, würden einen Eintritt und null Konversionen anzeigen, da die Konversion außerhalb des ausgewählten Datumsbereichs lag. Das auf dem Canvas-Schritt konfigurierte Konversionsfenster kann zudem deutlich über 14 Tage hinausgehen, sodass Analytics auf Schrittebene Konversionen über einen längeren Zeitraum erfassen können.

**Funnel-Berichte:** Der Datumsbereich filtert Nutzer:innen danach, **wann sie das Canvas betreten haben**. Wenn Sie den 1.–7. Januar auswählen, umfasst der Bericht alle Nutzer:innen, die in diesem Zeitfenster eingetreten sind, und verfolgt dann ihre Aktionen bis zu 14 Tage nach dem Eintritt (oder das von Ihnen im Funnel konfigurierte Zeitfenster). Dieselben Nutzer:innen, die am 1. Januar eingetreten sind und am 8. Januar konvertiert haben, würden einen Eintritt und eine Konversion anzeigen, da die Konversion innerhalb des Zeitfensters nach dem Eintritt stattfand.

Darüber hinaus erfordern Funnel-Berichte, dass Ereignisse in der angegebenen Reihenfolge stattfinden, und zählen jede Nutzer:in maximal einmal, während Canvas-Analytics alle Konversionen und Interaktionen ohne Reihenfolgebeschränkung zählen.
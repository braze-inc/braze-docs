---
nav_title: Funnel-Berichte
article_title: Funnel-Berichte für Kampagnen und Canvase
page_order: 6
page_type: reference
description: "Auf dieser Seite erfahren Sie, welche Vorteile Funnel-Berichte bieten, wie Sie sie einrichten und wie Sie Ihren Bericht interpretieren können."
tool: Reports
---

# Funnel-Berichte

> Der Funnel-Bericht bietet einen visuellen Bericht, mit dem Sie die Reisen Ihrer Kund:in analysieren können, die sie nach dem Erhalt einer Kampagne oder eines Canvas unternehmen. \![Funnel-Bericht 2]({% image_buster /assets/img/funnel_report/funnel_report2.png %}){: style="float:right;max-width:15%;margin-bottom:15px; border: 0"}

Wenn Ihre Kampagne oder Ihr Canvas eine Kontrollgruppe oder mehrere Varianten verwendet, können Sie nachvollziehen, wie sich die verschiedenen Varianten auf den Konversionstrichter ausgewirkt haben, und auf der Grundlage dieser Daten optimieren.

\![Funnel-Bericht 1]({% image_buster /assets/img/funnel_report/funnel_report1.jpg %}){: style="max-width:80%;"}

## Funnel-Berichte einrichten

\![Funnel-Bericht 5]({% image_buster /assets/img/funnel_report/canvas_campaign.png %}){: style="float:right;max-width:40%;border:0;margin-left:15px;"}

Sie können Funnel-Berichte für bestehende aktive Kampagnen und Canvase ausführen. Diese Berichte zeigen eine Reihe von Ereignissen, die ein Empfänger:in im Laufe von 1-30 Tagen ab dem Datum, an dem er das Canvas oder die Kampagne betritt, durchläuft. Ein Nutzer:in gilt als konvertiert, wenn er einen Schritt im Funnel in der angegebenen Reihenfolge ausführt.

Funnel-Berichte sind an den folgenden Standorten im Dashboard verfügbar:

- Die Seite **Campaign Analytics** für eine bestimmte Kampagne
- Die **Canvas-Detailseite** für einen bestimmten Canvas, indem Sie den Button **Varianten analysieren** auswählen 

{% alert important %}
Funnel-Berichte sind für [API Kampagnen]({{site.baseurl}}/api/api_campaigns/) nicht verfügbar.
{% endalert %}

### Schritt 1: Wählen Sie einen Datumsbereich

Sie können einen Zeitrahmen für Ihren Bericht auswählen (innerhalb der letzten sechs Monate) und die Daten verfeinern, um Nutzer:innen zu sehen, die beim Betreten der Kampagne oder des Canvas die Funnel-Ereignisse innerhalb eines bestimmten Zeitfensters (maximal 30 Tage) abgeschlossen haben. Im folgenden Beispiel würde Ihr Funnel nach Nutzer:innen suchen, die diese Kampagne oder das Canvas in den letzten sieben Tagen erhalten und den Funnel innerhalb von drei Tagen abgeschlossen haben.

{% alert note %}
Wenn Sie das Zeitfenster für die Fertigstellung des Funnels auf einen Tag festlegen, muss das Funnel-Ereignis innerhalb von 24 Stunden nach Eingang der Nachricht stattfinden. Wenn Sie jedoch mehrere Tage auswählen, wird das Zeitfenster als Kalendertage in der Zeitzone des Unternehmens gezählt.
{% endalert %}

\![Funnel-Bericht für ein Canvas, bei dem "Letzte 7 Tage" im Zeitrahmen-Dropdown ausgewählt wurde.]({% image_buster /assets/img/funnel_report/funnel_report5.png %}){: style="max-width:90%;"}

### Schritt 2: Ereignisse für Funnel-Schritte auswählen

Bei jedem Funnel-Bericht ist das erste Ereignis, wenn der Nutzer:innen Ihre Nachricht erhält. Von dort aus wird die Anzahl der Nutzer:innen, die diese Ereignisse durchgeführt haben, sowie die der vorherigen Ereignisse in einen Funnel geleitet. 

#### Verfügbare Funnel-Bericht-Ereignisse

| Kampagne | Sitzung gestartet, Kauf getätigt, Angepasstes Event durchgeführt, Nachricht Engagement Event |
| Canvas | Sitzung gestartet, Kauf getätigt, angepasstes Event durchgeführt, Canvas-Schritt erhalten, mit Schritt interagiert |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
Das Ereignis " **Mit Schritt interagiert** " kann nur mit Canvas-Schritten verwendet werden, die den E-Mail- oder Push Messaging-Kanal verwenden.
{% endalert %}

\![Funnel-Bericht für ein Canvas mit einer Dropdown-Liste der verfügbaren Berichtsereignisse.]({% image_buster /assets/img/funnel_report/funnel_report3.png %}){: style="max-width:80%;"}

Funnel-Berichte ermöglichen es Ihnen, den Erfolg Ihrer Nachrichten über die Konversions-Events oder Engagement-Events hinaus zu vergleichen, die Sie ursprünglich eingerichtet haben. Wenn es also ein Konversions-Event gibt, das Sie ursprünglich nicht hinzugefügt haben, können Sie die Konversionen für dieses Event dennoch mit einem Funnel tracken.

Wenn Sie zum Beispiel ein 14-tägiges Berichtszeitfenster auswählen, gefolgt von den Ereignissen `Added to cart` und `Made purchase`, sehen Sie sowohl die Anzahl der Nutzer:innen, die innerhalb von 14 Tagen nach Erhalt der Nachricht in den Warenkorb gelegt haben, als auch die Anzahl der Nutzer:innen, die innerhalb von 14 Tagen nach Erhalt der Kampagne in den Warenkorb gelegt und dann einen Kauf getätigt haben.

Ein anderes Beispiel: Sie möchten vielleicht den Prozentsatz der Nutzer:innen sehen, die nach dem Klick auf eine E-Mail konvertiert haben. Um dies zu berechnen, könnten Sie einen Bericht erstellen, bei dem das zweite Ereignis der Klick auf Ihre E-Mail und das dritte Ereignis die Durchführung Ihres Konversions-Events ist.

Nachdem Sie **Bericht erstellen** ausgewählt haben, kann die Erstellung des Funnel-Berichts einige Minuten dauern. Während dieser Zeit können Sie vom Bericht aus zu anderen Seiten des Dashboards navigieren. Sie erhalten eine Benachrichtigung im Dashboard, wenn Ihr Bericht fertig ist.

## Interpretation Ihres Funnel-Berichts

In Ihrem Funnel-Bericht können Sie die Kontrollgruppe direkt mit den Varianten vergleichen, die Sie eingerichtet haben. Jedes aufeinanderfolgende Ereignis zeigt an, wie viel Prozent der vorherigen Nutzer:innen diese Aktion abgeschlossen und durch den Funnel konvertiert haben.

### Bestandteile des Funnel-Berichts

- **Horizontale Achse**: Zeigt den Prozentsatz der Empfänger:innen von Nachrichten an, die diese Aktionen durchgeführt haben. 
- **Chart**: Zeigt die Anzahl der eingegangenen Nachrichten, die Anzahl der Nutzer:innen, die die vorherigen Aktionen durchgeführt haben, sowie die von Ihnen gewählte Aktion, die Konversionsrate und die prozentuale Veränderung gegenüber der Kontrolle.
- **Option Regenerieren**: Ermöglicht Ihnen, Ihren Bericht neu zu generieren und zeigt an, wann der aktuelle Bericht zuletzt erstellt wurde. 
- **Varianten**: Der durch farbige Spalten gekennzeichnete Funnel-Bericht lässt bis zu 8 Varianten und eine Kontrollgruppe zu. Standardmäßig werden im **Chart** nur drei Varianten angezeigt. Um mehr zu sehen, können Sie die restlichen Varianten manuell auswählen.

\![Funnel-Bericht Chart.]({% image_buster /assets/img/funnel_report/funnel_report4.jpg %})

**Für Kampagnen mit mehreren Varianten**: Braze zeigt eine Tabelle mit Metriken für jedes Ereignis und jede Variante sowie die prozentuale Veränderung gegenüber der Kontrolle an. Die Konversionsrate ist die Anzahl der Nutzer:innen pro Empfänger:in der Nachricht, die das Ereignis (und die nachfolgenden) durchgeführt haben.

**Für Kampagnen mit Wiederwählbarkeit**: Wenn ein Nutzer die Kampagne mehr als einmal innerhalb des Berichtszeitfensters erhält, bestimmt Braze anhand der Aktionen, die dieser Nutzer:in nach dem ersten Erhalt der Kampagne innerhalb des Zeitfensters durchgeführt hat, ob der Nutzer in den Funnel aufgenommen werden soll.
- Beachten Sie, dass es eine Diskrepanz zwischen den Trichter- und den Standard-Konversionswerten geben kann, da Nutzer:innen mehrmals konvertieren können, aber Funnel-Berichte maximal einmal konvertieren, auch wenn ein Nutzer das Event mehr als einmal durchführt. 

**Für multivariate Kampagnen mit Wiederzulassung**: Wenn ein Nutzer innerhalb des Berichtszeitfensters mehrere Varianten aus der Kampagne erhält, bestimmt Braze anhand der Aktionen, die dieser Nutzer:in nach dem ersten Erhalt der Kampagnenvariante durchgeführt hat, ob diese in den Varianten-Trichter aufgenommen werden sollen. Das bedeutet, dass ein und derselbe Nutzer:innen auf mehrere verschiedene Varianten angerechnet werden kann, wenn er während des Zeitfensters für den Funnel mehrere Varianten erhalten hat.

{% alert important %}
Verwaiste Nutzer:innen werden in Funnel-Berichten nicht getrackt. Wenn ein anonymer Nutzer:in ein Canvas oder eine Kampagne eintritt und später über die Methode `changeUser()` identifiziert wird, ändert sich seine Braze ID. Funnel-Berichte verfolgen nur Follow-up-Ereignisse, die mit der ID des Nutzers zum Zeitpunkt des Eingangs übereinstimmen, und berücksichtigen nicht die Ereignisse, die der Nutzer:innen nach dem Wechsel seiner ID durchführt. Das bedeutet, dass Konversions-Events, die der Nutzer:innen nach seiner Identifizierung durchführt, nicht in den Funnel-Bericht aufgenommen werden.
{% endalert %}


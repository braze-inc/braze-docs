---
nav_title: Bindungsberichte
article_title: Bindungsberichte für Kampagnen und Canvase
page_order: 5
tool: Reports
page_type: reference
description: "Auf dieser Seite erfahren Sie, wie Sie die Bindung von Nutzer:innen messen können, die ein ausgewähltes Bindungsereignis in einer bestimmten Kampagne oder einem Canvas durchgeführt haben."
---

# Bindungsberichte

> Die Nutzerbindung ist eine der wichtigsten Metriken für jeden Marketer. Wenn engagierte Nutzer:innen immer wieder zurückkommen, ist das ein Zeichen dafür, dass das Geschäft gut läuft. Braze erlaubt es Ihnen, die Bindung der Nutzer:innen direkt auf der **Analytics-Seite** Ihrer Kampagne oder Ihres Canvas zu messen.

{% alert important %}
Berichte zur Bindung sind für API-getriggerte Kampagnen nicht verfügbar.
{% endalert %}

## Ausführen eines Berichts zur Bindung von Daten

### Schritt 1: Wählen Sie einen Datumsbereich aus

![Berichtsdatum]({% image_buster /assets/img/date_select_retention.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Beginnen Sie, indem Sie eine beliebige Kampagne oder ein Canvas in Ihrem Braze-Dashboard besuchen und einen Datumsbereich für Ihren Bericht auswählen. Die Auswahl eines geeigneten Datumsbereichs ist von entscheidender Bedeutung, da er sich auf die Bindungsberichte auswirkt. 

Dieser Bericht enthält alle Nutzer:innen, die die Kampagne oder das Canvas während dieses Zeitfensters zum ersten Mal betreten haben. Von diesen Nutzer:innen werden die Daten derjenigen, die ihre Bindung während des Datumsbereichs durchgeführt haben, im Bericht angezeigt.

Um einen Datumsbereich auszuwählen, navigieren Sie zur Kampagnen- oder Canvas **Analytics-Seite** und wählen Sie verschiedene Bereiche aus oder legen Sie einen angepassten Bereich für Ihren Bericht fest.

### Schritt 2: Bindungs-Event auswählen

{% tabs %}
{% tab Campaign %}

Gehen Sie dann zum Abschnitt **Kampagnen-Bindung**. Die Kampagnenbindung zeigt Ihnen die Rate, mit der jede:r Nutzer:in, der oder die diese spezielle Kampagne erhalten hat, innerhalb von 30 Tagen nach Erhalt der Kampagne ein Bindungs-Event (von Ihnen im Bindungsbericht angegeben) durchgeführt hat.

{% endtab %}
{% tab Canvas %}

Als nächstes wählen Sie **Varianten analysieren**. Von hier aus können Sie Ihre Varianten analysieren, sich Ihren Funnel-Bericht ansehen und Ihren Bindungsbericht einsehen. Die Canvas-Bindung zeigt Ihnen die Rate an, mit der jeder Benutzer, der dieses bestimmte Canvas erhalten hat, ein Bindungs-Event (von Ihnen im Bindungsbericht angegeben) innerhalb von 30 Tagen nach Erhalt des Canvas durchgeführt hat.

{% endtab %}
{% endtabs %}

![Wählen Sie ein Ereignis der Bindung aus]({% image_buster /assets/img/retention_1.png %}){: style="max-width:80%"}

### Schritt 3: Bericht erzeugen

Nachdem Sie ein Ereignis für die Bindung ausgewählt haben, wählen Sie **Bericht ausführen**, um die Abfrage zu starten.

![Bericht ausführen]({% image_buster /assets/img/retention_2.png %}){: style="max-width:80%"}

Die Ausführung dieser Abfrage kann einige Minuten dauern, je nachdem, wie viele Daten abgerufen werden müssen, um die Ergebnisse zu generieren. Wenn es zu lange dauert, erhalten Sie eine Benachrichtigung, die Sie auffordert, das Laden des Berichts zu wiederholen. Es kann sein, dass Sie bis zu fünf Minuten warten müssen, bevor der Bericht geladen wird.

Nachdem der Bericht erstellt wurde, kann er 24 Stunden lang nicht mit demselben Binde-Ereignis erneut ausgeführt werden. Sie sehen immer einen Zeitstempel, wann der Bericht zuletzt erstellt wurde, und eine Option zum erneuten Erstellen, wenn es mehr als einen Tag her ist. Sie können jedoch das Ereignis für die Bindung ändern und den Bericht erneut ausführen, um die Auswirkungen der Kampagne auf verschiedene KPIs zu untersuchen.

Der Bericht listet nur die Tage auf, an denen die Kampagne oder der Canvas Nachrichten versendet hat. Für einige Kampagnen und Canvase kann das bedeuten, dass der Bericht nur einen Tag anzeigt, wenn er nur einmal gesendet wurde. Wenn es sich um einen wiederkehrenden oder getriggerten Vorgang handelt, sehen Sie möglicherweise mehrere Tage in der Tabelle.

{% tabs %}
{% tab Campaign %}

![Vollständiger Bericht]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Vollständiger Bericht]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Erklärung zum Bericht

Der Bindungsbericht bietet sowohl eine rollende als auch eine bereichsbezogene Bindungsformel. Um Ihre Kampagne oder Ihren Canvas-Bericht mit einem dieser Bindungstypen anzuzeigen, wählen Sie entweder **Rolling Retention** oder **Range Retention** für Ihren **Bindungstyp** aus.

### Rollende Bindung

Die rollende Bindung misst, wie viele Nutzer:innen an oder nach einem der oben im Bericht aufgeführten Tage zurückkehren und das Bindungs-Event durchführen. Wenn also ein Nutzer:innen eine Sitzung zwischen dem dritten und dem siebten Tag begonnen hat, wird der Nutzer:innen in den Spalten "3 Tage", "1 Tag" und "0 Tage" als behalten gezählt. Jede:r Nutzer:in, der oder die nach der 30-Tage-Marke ab dem Versand der Kampagne oder des Canvas als erhalten gilt, wird in der Spalte „30 Tage“ in dieser Zeile gezählt.

Ein:e Nutzer:in, der oder die das Event innerhalb eines Zeitfensters von 30+ Tagen mehrfach abschließt, wird als Teil mehrerer Zeitfenster gezählt. Ein Nutzer:in, der eine Sitzung nach einem Tag beendet, wird beispielsweise in den Spalten für >0 und >1 hochgezählt. Wenn sie die Veranstaltung dann nach drei Tagen abschließen, werden sie in den vorherigen Spalten (>0 und >1) erneut hochgezählt, was dazu führen kann, dass die Bindungsrate 100% übersteigt.

#### So lesen Sie Berichte zur rollierenden Bindung

Das Chart des Berichts über die Bindung für die Spalte Tag drei würde wie folgt aussehen: Y% oder Y Anzahl der Nutzer:innen (basierend auf den gewählten Einheiten) haben das Ereignis drei oder mehr Tage nach Erhalt der Kampagne an Tag Z durchgeführt.

![Rolling Report]({% image_buster /assets/img/campaign_retention3.png %})

Ein weiteres Beispiel ist die Tabelle in der vorangehenden Abbildung. Am 25\. März haben insgesamt 38 Nutzer:innen die Bindung durchgeführt. Die Bindung am Tag Null lag bei 68,42%, was bedeutet, dass 68,42% der Nutzer:innen das Bindeereignis null oder mehr Tage (am Tag Null oder später) nach Erhalt der Kampagne durchgeführt haben. Die Bindung am siebten Tag lag bei 57,89%, d.h. 57,89% der Nutzer:innen haben das Ereignis sieben oder mehr Tage (am siebten Tag oder später) nach Erhalt der Kampagne durchgeführt.

Diese Information kann nützlich sein, wenn Sie wissen möchten, wie viel Prozent der Nutzer:innen Ihr Produkt 30+ Tage nach der ersten Nutzung verwendet haben bzw. nicht verwendet haben. Ein Prozent- oder Zahlenwert in der Spalte Tag 30 zeigt Ihnen den Prozentsatz der Nutzer:innen, die am Tag 30 oder später zurückgekehrt sind.

### Bindung der Reichweite

Die Bindung an den Bereich misst, wie viele Nutzer:innen innerhalb der oben im Bericht aufgeführten Tage wiederkommen. Wenn also ein Nutzer:innen eine Sitzung zwischen dem dritten und siebten Tag und dann noch einmal am 13\. Tag begonnen hat, würde er sowohl im Bereich "Tag 3-7" als auch im Bereich "Tag 7-14" als behalten gezählt werden.

#### So lesen Sie die Berichte zur Bindung von Reichweiten

Bereichsberichte gehören zu den am intuitivsten zu lesenden Berichten. Sie geben eindeutig an, welcher Prozentsatz aller Nutzer:innen in einer Kohorte das Bindungs-Event innerhalb eines bestimmten Zeitraums durchgeführt hat. In der folgenden Abbildung, die sich auf die Kohorte „Alle Nutzer:innen“ bezieht, haben beispielsweise 35,71 % der Kohorte im Datumsbereich „Tag 0 (0–24 Std.)“ den Bericht über die Speicherung durchgeführt. Wenn ein:e Nutzer:in mehrere Bindungs-Events innerhalb mehrerer Datumsbereiche durchführt, werden sie für jeden Bereich als gebunden gezählt.

![Bericht zur Bindung]({% image_buster /assets/img/range_retention.png %})

### Komponenten des Bindungsberichts

- **Nutzerspalte**: Der angezeigte Wert ist die Anzahl eindeutiger Nutzer:innen, die die Startaktion innerhalb des ausgewählten Zeitrahmens durchgeführt haben. Die Anzahl der Nutzer:innen des aktuellen Tages wird nicht berücksichtigt, da sie gerade berechnet wird. 
- **Kohorten Z-Reihen**: Zeigt die Tage an, an denen die Kampagne oder der Canvas Nachrichten versendet hat.
- **Tag X-Spalten**: Tage zwischen 0 und 30 Tagen in verschiedenen Abstufungen.
- **Zeile „Alle Nutzer:innen“**: Auch bekannt als die Berichtzusammenfassungszeile, fasst die Bindungsdaten für den gesamten Zeitraum zusammen. Beachten Sie, dass, wenn ein Nutzer:innen die Kampagne oder das Canvas in mehreren Kohorten erhalten hat, seine Ergebnisse hier doppelt gezählt werden. 
- **Prozentsätze/Zahlen**: Zeigt den Prozentsatz oder die Anzahl der Nutzer:innen, die das Ereignis X oder mehr Tage nach Erhalt der Kampagne oder des Canvas am Tag Z durchgeführt haben. Diese Prozentsätze sind die gewichteten Durchschnittsprozentsätze. Unvollständige Werte werden mit einem Sternchen gekennzeichnet.
- **Datumsbereich**: Der Datumsbereich umfasst alle Nutzer:innen, die die Kampagne oder das Canvas innerhalb dieses Zeitfensters erhalten haben. Von diesen Nutzern:innen werden die Daten derjenigen, die ihre Bindung innerhalb des Datumsbereichs durchgeführt haben, im Bericht angezeigt.
- **Einheiten**: Sie können die Einheiten zwischen dem Prozentsatz der Nutzer:innen und der Anzahl der Nutzer:innen in der oberen rechten Ecke des Charts anpassen. Bestimmte Einheiten können sich als aussagekräftiger erweisen, wenn es darum geht, die Wirkung einer Kampagne oder eines Canvas zu beurteilen.
- **Farbzuordnung**: In Ihrem Bericht über die Bindung werden höhere Prozentsätze oder die Anzahl der Nutzer:innen in dunkleren Blautönen dargestellt. Geringere Prozentsätze oder Anzahl der Nutzer:innen sind in helleren Blautönen gehalten. Dies geschieht, um den Nutzer:innen die Visualisierung dieser Daten zu erleichtern.
- **Diagramm zum Bindungsbericht**: Diese Grafik fasst die Ergebnisse für alle Kohorten für den ausgewählten Datumsbereich zusammen.

### Performance nach Variante

Wenn Sie Ihren Bindungsbericht nach Variante anzeigen, können Sie die rollende Bindung für jede Variante oder Nachrichtenvariation für den ausgewählten Zeitraum sowie die Kontrollgruppe vergleichen. Sie können diesen Bericht anzeigen, indem Sie **Leistung anzeigen für** auf **Nach Variante** umschalten.

Einige Anwendungsfälle für die Darstellung der Performance nach Varianten:

- Gibt es Varianten oder Experimente, bei denen die Ergebnisse wie vergebliche Mühe erscheinen oder keine statistische Aussagekraft haben? Schauen Sie noch einmal hin und sehen Sie, ob die eine oder andere einen längerfristigen Einfluss hatte.
- Sehen Sie sich an, wie die Bindung aussieht, wenn Sie keine Nachricht gesendet haben, indem Sie die Bindungsdaten der Kontrollgruppe untersuchen.

{% tabs %}
{% tab Campaign %}

![Ansicht nach Variante]({% image_buster /assets/img/variant_view.png %})

{% endtab %}
{% tab Canvas %}

![Ansicht nach Variante]({% image_buster /assets/img/variant_view_canvas.png %})

{% endtab %}
{% endtabs %}

#### Bindungsbericht nach Variantenkomponenten

- **Datumsbereich**: Auf der Seite **Details der** Kampagne oder des Canvas eingestellt, umfasst der Datumsbereich alle Nutzer:innen, die die Kampagne oder das Canvas während dieses Zeitfensters erhalten haben. Von diesen Nutzern:innen werden die Daten derjenigen, die ihre Bindung während des Datumsbereichs durchgeführt haben, im Bericht angezeigt. Jeden Tag werden die Bindungsrate, die prozentuale Veränderung gegenüber der Kontrollgruppe und das Vertrauen gemessen.
- **Bindungsrate**: Zeigt die Bindungsrate nach Variante an. Die Bindungsrate entspricht der Anzahl der Nutzer:innen, die das Bindungsereignis durchgeführt haben, geteilt durch die Gesamtzahl der Nutzer:innen, die die Kampagne oder das Canvas erhalten haben.
- **Prozentuale Veränderung gegenüber der Kontrolle**: Gibt die prozentuale Veränderung pro Variante gegenüber der Kontrollgruppe an.
- **Zuversicht**: {% multi_lang_include analytics/metrics.md metric='Confidence' %} Braze vergleicht die Konversionsrate jeder Variante mit der Konversionsrate der Kontrollvariante mit einem statistischen Verfahren, dem so genannten Z-Test, um einen [Konfidenzprozentsatz]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence) zu berechnen.
- **Einheiten**: Sie können die Einheiten zwischen dem Prozentsatz der Nutzer:innen und der Anzahl der Nutzer:innen in der oberen rechten Ecke des Charts anpassen. Bestimmte Einheiten können sich als aussagekräftiger erweisen, wenn es darum geht, die Wirkung einer Kampagne oder eines Canvas zu beurteilen.
- **Variante Graph**: Dieses Diagramm fasst die Ergebnisse nach Varianten für den ausgewählten Datumsbereich zusammen.

## Worauf Sie in Ihren Berichten über die Bindung achten sollten

Bindungsberichte sind einfach zu erstellen, aber schwierig zu interpretieren und umzusetzen. Um Marketern zu helfen, haben wir eine Reihe von Themen und Fragen zusammengestellt, die Sie bei der Betrachtung Ihrer Bindungsberichte berücksichtigen sollten.

- Berücksichtigen Sie Wochentagstrends für wiederkehrende Kampagnen (z.B.: Erzielen Kohorten am Montag eine bessere Performance als Kohorten am Samstag?)
- Wo beginnt die Wirkung zu schwinden? Dies könnte ein Signal dafür sein, dass eine neue Kampagne oder ein Canvas, die/das auf Nutzer:innen zu diesem Zeitpunkt abzielt, als weitere Maßnahme zur Bindung benötigt wird. 
- Spüren Sie eine Ermüdung in Bezug auf Nachrichten?
- Hatte eine bestimmte Optimierung, die Sie vor X Tagen an einer Kampagne oder einem Canvas vorgenommen haben, eine positive Wirkung?




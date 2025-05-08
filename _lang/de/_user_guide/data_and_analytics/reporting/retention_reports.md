---
nav_title: Bindung Berichte
article_title: Bindungsberichte für Kampagnen und Canvase
page_order: 5
tool: Reports
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie die Benutzerbindung für Benutzer messen können, die in einer bestimmten Kampagne oder einem Canvas ein ausgewähltes Ereignis zur Benutzerbindung durchgeführt haben."
---

# Bindungsberichte

> Die Nutzerbindung ist eine der wichtigsten Metriken für jeden Marketer. Wenn engagierte Nutzer:innen immer wieder zurückkommen, ist das ein Zeichen dafür, dass das Geschäft gut läuft. Braze erlaubt es Ihnen, die Bindung der Nutzer:innen direkt auf der **Analytics-Seite** Ihrer Kampagne oder Ihres Canvas zu messen.

{% alert important %}
Berichte zur Bindung sind für API-getriggerte Kampagnen nicht verfügbar.
{% endalert %}

## Bindungsbericht ausführen

### Schritt 1: Wählen Sie einen Datumsbereich aus

![Datum des Berichts][8]{: style="float:right;max-width:30%;margin-left:15px;"}

Beginnen Sie, indem Sie eine beliebige Kampagne oder ein Canvas in Ihrem Braze-Dashboard besuchen und einen Datumsbereich für Ihren Bericht auswählen. Die Auswahl eines geeigneten Datumsbereichs ist von entscheidender Bedeutung, da er sich auf die Bindungsberichte auswirkt. 

Dieser Bericht enthält alle Benutzer, die die Kampagne oder das Canvas innerhalb dieses Zeitfensters erstmals betreten haben. Von diesen Benutzern werden die Daten derjenigen, die ihr Beibehaltungsereignis innerhalb des Datumsbereichs durchgeführt haben, in dem Bericht angezeigt.

Um einen Datumsbereich auszuwählen, müssen Sie in die obere rechte Ecke der Kampagne oder der Canvas **Analytics-Seite** navigieren. Hier können Sie verschiedene Bereiche auswählen oder einen eigenen Bereich für Ihren Bericht festlegen.

### Schritt 2: Bindungs-Event auswählen

{% tabs %}
{% tab Kampagne %}

Scrollen Sie dann nach unten zum Abschnitt **Kampagnenaufbewahrung**. Die Kampagnenbindung zeigt Ihnen die Rate, mit der jede:r Nutzer:in, der oder die diese spezielle Kampagne erhalten hat, innerhalb von 30 Tagen nach Erhalt der Kampagne ein Bindungs-Event (von Ihnen im Bindungsbericht angegeben) durchgeführt hat.

{% endtab %}
{% tab Canvas %}

Klicken Sie anschließend auf **Varianten analysieren** am unteren Rand der Seite. Von hier aus können Sie Ihre Varianten analysieren, sich Ihren Funnel-Bericht ansehen und Ihren Bindungsbericht einsehen. Die Canvas-Bindung zeigt Ihnen die Rate an, mit der jeder Benutzer, der dieses bestimmte Canvas erhalten hat, ein Bindungs-Event (von Ihnen im Bindungsbericht angegeben) innerhalb von 30 Tagen nach Erhalt des Canvas durchgeführt hat.

{% endtab %}
{% endtabs %}

![Bindungs-Event auswählen][1]{: style="max-width:80%"}

### Schritt 3: Bericht erzeugen

Sobald Sie ein Event zur Speicherung ausgewählt haben, klicken Sie auf **Bericht ausführen**, um die Abfrage zu starten.

![Bericht ausführen][2]{: style="max-width:80%"}

Die Ausführung dieser Abfrage kann einige Minuten dauern, je nachdem, wie viele Daten abgerufen werden müssen, um die Ergebnisse zu generieren. Wenn es zu lange dauert, erhalten Sie eine Benachrichtigung, die Sie auffordert, das Laden des Berichts zu wiederholen. Es kann sein, dass Sie bis zu fünf Minuten warten müssen, bevor der Bericht geladen wird.

Sobald der Bericht erstellt wurde, kann er 24 Stunden lang nicht mehr mit demselben Bindungs-Event ausgeführt werden. Sie sehen immer einen Zeitstempel, wann der Bericht zuletzt erstellt wurde, und eine Option zum erneuten Erstellen, wenn mehr als ein Tag vergangen ist. Sie können jedoch das Ereignis für die Bindung ändern und den Bericht erneut ausführen, um die Auswirkungen der Kampagne auf verschiedene KPIs zu untersuchen.

Der Bericht listet nur die Tage auf, an denen die Kampagne oder der Canvas Nachrichten versendet hat. Für einige Kampagnen und Canvase kann das bedeuten, dass der Bericht nur einen Tag anzeigt, wenn er nur einmal gesendet wurde. Wenn es sich um einen wiederkehrenden oder getriggerten Vorgang handelt, sehen Sie möglicherweise mehrere Tage in der Tabelle.

{% tabs %}
{% tab Kampagne %}

![Vollständiger Bericht]({% image_buster /assets/img/campaign_retention3.png %})

{% endtab %}
{% tab Canvas %}

![Vollständiger Bericht]({% image_buster /assets/img/canvas_retention_report.png %}){: style="max-width:70%"}

{% endtab %}
{% endtabs %}

## Erklärung zum Bericht

Der Bindungsbericht bietet sowohl eine rollende als auch eine bereichsbezogene Bindungsformel. Um Ihre Kampagne oder Ihren Canvas-Bericht mit einem dieser Bindungstypen anzuzeigen, wählen Sie entweder **Rolling Retention** oder **Range Retention** für Ihren **Bindungstyp** aus.

### Rollende Bindung

Die rollende Bindung misst, wie viele Nutzer:innen an oder nach einem der oben im Bericht aufgeführten Tage zurückkehren und das Bindungs-Event durchführen. Wenn also ein:e Nutzer:in eine Sitzung zwischen Tag 3 und 7 begonnen hat, wird der oder die Nutzer:in in den Spalten „3 Tage“, „1 Tag“ und „0 Tage“ als gebunden gezählt. Jede:r Nutzer:in, der oder die nach der 30-Tage-Marke ab dem Versand der Kampagne oder des Canvas als erhalten gilt, wird in der Spalte „30 Tage“ in dieser Zeile gezählt.

Ein:e Nutzer:in, der oder die das Event innerhalb eines Zeitfensters von 30+ Tagen mehrfach abschließt, wird als Teil mehrerer Zeitfenster gezählt. So wird beispielsweise ein:e Nutzer:in, der oder die eine Sitzung nach 1 Tag beendet, in den Spalten für >0 und >1 erhöht. Wenn sie das Event dann nach 3 Tagen abschließen, werden sie in den vorherigen Spalten (>0 und >1) erneut erhöht, was dazu führen kann, dass die Bindungsrate 100 % übersteigt.

#### So lesen Sie Berichte über die rollierende Speicherung

Die Tabelle des Bindungsberichts für eine Spalte des dritten Tages würde wie folgt lauten: Y % oder Y Anzahl der Nutzer:innen (basierend auf den ausgewählten Einheiten) haben das Event drei oder mehr Tage nach Erhalt der Kampagne am Tag Z durchgeführt.

![Rollender Bericht]({% image_buster /assets/img/campaign_retention3.png %})

Ein weiteres Beispiel: Am 25\. März haben insgesamt 38 Nutzer die Vorratsdatenspeicherung durchgeführt, wie Sie der Tabelle in der vorhergehenden Abbildung entnehmen können. Die Beibehaltung an Tag 0 lag bei 68,42 %, d. h. 68,42 % der Nutzer haben das Beibehaltungsereignis 0 oder mehr Tage (an Tag 0 oder später) nach Erhalt der Kampagne durchgeführt. Die 7-Tage-Bindung lag bei 57,89 %, was bedeutet, dass 57,89 % der Nutzer:innen das Event 7 oder mehr Tage (am 7\. Tag oder später) nach Erhalt der Kampagne durchführten.

Diese Informationen können nützlich sein, wenn Sie wissen möchten, wie viel Prozent der Nutzer Ihr Produkt 30+ Tage nach der ersten Nutzung verwendet haben bzw. nicht verwendet haben. Ein Prozent- oder Zahlenwert in der Spalte Tag 30 zeigt Ihnen den Prozentsatz der Nutzer:innen, die am Tag 30 oder später zurückgekehrt sind.

### Bindung der Reichweite

Die Reichweitenbindung misst, wie viele Benutzer innerhalb der oben im Bericht aufgeführten Tage wiederkommen. Wenn also ein:e Nutzer:in eine Sitzung zwischen Tag 3 und 7 und dann noch einmal an Tag 13 begonnen hat, würde er sowohl im Bereich „Tag 3–7“ als auch im Bereich „Tag 7–14“ als gebunden gezählt werden.

#### So lesen Sie die Berichte zur Reichweitenerhaltung

Bereichsberichte gehören zu den am intuitivsten zu lesenden Berichten. Sie geben eindeutig an, welcher Prozentsatz aller Nutzer:innen in einer Kohorte das Bindungs-Event innerhalb eines bestimmten Zeitraums durchgeführt hat. In der folgenden Abbildung, die sich auf die Kohorte „Alle Nutzer:innen“ bezieht, haben beispielsweise 35,71 % der Kohorte im Datumsbereich „Tag 0 (0–24 Std.)“ den Bericht über die Speicherung durchgeführt. Wenn ein:e Nutzer:in mehrere Bindungs-Events innerhalb mehrerer Datumsbereiche durchführt, werden sie für jeden Bereich als gebunden gezählt.

![Bindungsbericht][5]

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
{% tab Kampagne %}

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
- **Konfidenz**: {% multi_lang_include metrics.md metric='Konfidenz' %} Braze vergleicht die Konversionsrate jeder Variante mit der Konversionsrate der Kontrollvariante mit einem statistischen Verfahren namens Z-Test, um einen [Konfidenzprozentsatz]({{site.baseurl}}/user_guide/intelligence/multivariate_testing/#understanding-confidence) zu berechnen.
- **Einheiten**: Sie können die Einheiten zwischen dem Prozentsatz der Nutzer:innen und der Anzahl der Nutzer:innen in der oberen rechten Ecke des Charts anpassen. Bestimmte Einheiten können sich als aussagekräftiger erweisen, wenn es darum geht, die Wirkung einer Kampagne oder eines Canvas zu beurteilen.
- **Variante Graph**: Dieses Diagramm fasst die Ergebnisse nach Varianten für den ausgewählten Datumsbereich zusammen.

## Worauf Sie in Ihren Berichten über die Bindung achten sollten

Bindungsberichte sind einfach zu erstellen, aber schwierig zu interpretieren und umzusetzen. Um Marketern zu helfen, haben wir eine Reihe von Themen und Fragen zusammengestellt, die Sie bei der Betrachtung Ihrer Bindungsberichte berücksichtigen sollten.

- Berücksichtigen Sie Wochentagstrends für wiederkehrende Kampagnen (z.B.: Erzielen Kohorten am Montag eine bessere Performance als Kohorten am Samstag?)
- Wo beginnt die Wirkung zu schwinden? Dies könnte ein Signal dafür sein, dass eine neue Kampagne oder ein Canvas, die/das auf Nutzer:innen zu diesem Zeitpunkt abzielt, als weitere Maßnahme zur Bindung benötigt wird. 
- Spüren Sie eine Ermüdung in Bezug auf Nachrichten?
- Hatte eine bestimmte Optimierung, die Sie vor X Tagen an einer Kampagne oder einem Canvas vorgenommen haben, eine positive Wirkung?

[1]: {% image_buster /assets/img/retention_1.png %}
[2]: {% image_buster /assets/img/retention_2.png %}
[5]: {% image_buster /assets/img/range_retention.png %}
[8]: {% image_buster /assets/img/date_select_retention.png %}



---
nav_title: Berichte ansehen
article_title: Anzeigen der Berichte des Decisioning Studios
page_order: 3
description: "Erfahren Sie, wie Sie BrazeAI Decisioning Studio™-Berichte in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Kampagnen beeinflussen."
---

# Anzeigen der Berichte des Decisioning Studios

> Erfahren Sie, wie Sie BrazeAI Decisioning Studio™-Berichte in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Kampagnen beeinflussen. Von Metriken zur Performance über den Zustand der Daten bis hin zu Systemänderungen - diese Berichte helfen Ihnen, Ergebnisse zu verstehen, Fehlerbehebungen durchzuführen und fundierte Entscheidungen zu treffen.

## Voraussetzungen

Bevor Sie die Berichte des Decisioning Studios in der Braze anzeigen können, müssen Sie diese aufrufen:

- Sie haben einen aktiven Vertrag für Braze und BrazeAI Decisioning Studio™. 
- Wenden Sie sich an Ihren CSM, damit er das BrazeAI Decisioning Studio™ in Ihrem Namen für Sie aktiviert.
- Verfügen Sie über einen Live-Agenten von BrazeAI Decisioning Studio™.

## Berichte ansehen {#view}

Um Metriken für die Agenten eines Decisioning Studios in Braze anzuzeigen, gehen Sie zu **KI Decisioning** > **BrazeAI Decisioning Studio™** und wählen Sie einen Agenten aus.

Der Startbildschirm von BrazeAI Decisioning Studio™ für die Berichterstattung zeigt ein Dashboard mit mehreren Berichtskarten. Jede Karte zeigt einen Berichtstyp an, z. B. Performance, Insights, Diagnostics und Timeline, mit kurzen Beschreibungen und Symbolen für jeden Bericht.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Hier können Sie Berichte wie Performance, Insights, Diagnosen und Zeitleisten einsehen. Weitere Einzelheiten finden Sie unter [Verfügbare Berichte](#reports).

## Ändern von Berichtsdaten

Nachdem Sie [einen Bericht geöffnet haben](#view), können Sie den Datumsbereich ändern, indem Sie ein neues Start- und Enddatum aus dem Kalender-Dropdown auswählen.

Der SELEKTOR für den Datumsbereich von BrazeAI Decisioning Studio™ ist mit einem Kalender-Dropdown geöffnet. Der Kalender zeigt auswählbare Start- und Enddaten zur Anpassung der Berichtsansicht an.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Sie können auch ein Standard-Startdatum festlegen oder Daten auswählen, die immer ausgeschlossen werden sollen. Die ausgeschlossenen Daten werden aus allen Berichten für diesen Agenten herausgefiltert.

Um Daten festzulegen oder auszuschließen, wählen Sie <i class="fa-solid fa-gear"></i> **Einstellungen** und ändern Sie dann Ihr Standarddatum oder schließen Sie Daten nach Bedarf aus.

Das Panel "Einstellungen" in BrazeAI Decisioning Studio™ ist geöffnet und zeigt Optionen zum Festlegen eines Standard-Startdatums und zum Ausschluss bestimmter Daten aus Berichten. Das Panel enthält zwei Abschnitte mit den Bezeichnungen Standard-Startdatum und Ausschlussdaten. Unter Ausschließen von Daten sind mehrere Daten aufgeführt, neben denen jeweils ein Kontrollkästchen steht.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Verfügbare Berichte {#reports}

### Leistung

Der Performance-Bericht bietet Metriken auf hoher Ebene, die Behandlungsgruppen (von Braze) mit einer oder mehreren Kontrollgruppen (z.B. Umsatz) vergleichen. Es unterstützt zwei verschiedene Ansichten: **Trending** und **Driver Tree**.

Standardmäßig verwendet der Bericht die **Trending-Ansicht**, die vergleicht, wie BrazeAI™ im Vergleich zu Ihren Kontrollgruppen im Laufe der Zeit performt, und die Entwicklung des Uplifts trackt.

\![Trendansicht des Leistungsberichts mit einem Liniendiagramm, das die Performance von BrazeAI™ und der Kontrollgruppe im Zeitverlauf vergleicht. Das Chart zeigt zwei Linien mit den Bezeichnungen BrazeAI™ und Control, wobei die y-Achse mit Uplift und die x-Achse mit Datum beschriftet ist. Eine Legende kennzeichnet jede Gruppe durch eine Farbe.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

Alternativ können Sie den **Treiberbaum** auswählen, um zu sehen, wie die wichtigsten Werttreiber mit den Targeting-Metriken verknüpft sind, damit Sie die Beziehung zwischen ihnen besser verstehen.

\![Baumansicht der Performance-Berichtstreiber mit einem hierarchischen Diagramm, das die wichtigsten Werttreiber auf Targeting-Metriken abbildet. Das Diagramm zeigt mehrere miteinander verbundene Knoten an, die jeweils mit dem Namen eines Treibers oder einer Metrik beschriftet sind und veranschaulichen, wie verschiedene Faktoren zur Gesamtperformance beitragen.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

Um die Performance zwischen zwei Gruppen zu vergleichen, wählen Sie in den Dropdown-Listen die gewünschten Vergleichskriterien aus. In der folgenden Tabelle finden Sie weitere Einzelheiten:

| Feld | Beschreibung |
|-------|-------------|
| Vergleichsgruppen | Die Gruppen, die Sie in Ihrem Bericht vergleichen möchten. |
| Aggregation | Die Art und Weise, wie der Bericht Daten gruppiert, z. B. Summen, Durchschnittswerte oder Prozentsätze. |
| Segmente | Die [Segmente der Zielgruppe]({{site.baseurl}}/user_guide/engagement_tools/segments/), die Sie in Braze erstellt haben. |
| Zeitleiste Ereignisse | Die spezifischen Ereignisse, die im Laufe der Zeit angezeigt werden, wie z.B. der Versand von Nachrichten, Öffnungen oder Konversionen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Insights

Insights zeigen Ihnen, wie die verschiedenen Empfehlungsoptionen in Ihrer Aktionsbank generiert werden, wie z.B. SL oder Blockauswahl. Es gibt zwei verschiedene Insights-Berichte: **Agentenpräferenzen** und **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
Der Bericht über die **Agentenpräferenzen** hilft Ihnen, saisonale Trends zu erkennen und die Relevanz der Auswahl in der Aktionsbank zu bewerten, um fundierte Entscheidungen für Updates zu treffen.

\![Bericht zu den Agentenpräferenzen mit einem Balkendiagramm, das vergleicht, wie oft verschiedene Empfehlungsoptionen in einem bestimmten Zeitraum ausgewählt wurden. Das Chart zeigt mehrere farbige Balken an, von denen jeder eine Empfehlungsoption aus der Aktionsbank vertritt. Die y-Achse ist mit dem Prozentsatz der gewählten Optionen beschriftet und die x-Achse enthält die Namen der Optionen.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

In der folgenden Tabelle finden Sie weitere Einzelheiten zu diesem Bericht:

| Feld | Beschreibung |
|-------|-------------|
| Dimension | Das Attribut, das zur Organisation der Ergebnisse verwendet wird, z. B. Kanal, Kampagne oder Plattform. |
| Vergleichsgruppe | Die Gruppen, die Sie in Ihrem Bericht vergleichen möchten. Sie können mehrere Vergleichsgruppen auswählen, bis zu NUM. |
| Parameter | Die Metrik, die auf dieses Attribut angewendet wird, z.B. Öffnungen, Klicks oder Konversionsrate. |
| Segment | Das [Segment der Zielgruppe]({{site.baseurl}}/user_guide/engagement_tools/segments/), das Sie in Braze erstellt haben. |
| Option             | Die spezifische Empfehlungsoption, die aus der Aktionsbank ausgewählt wurde. |
| Beschreibung        | Eine kurze Erklärung, wofür die Option steht.            |
| \#mal gewählt  | Die Gesamtzahl, wie oft die Option ausgewählt wurde.         |
| % der gewählten Zeit   | Der Prozentsatz der gesamten Auswahlen, bei denen diese Option gewählt wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
Der **SHAPs-Bericht** verwendet das SHAPley Additive ExPlanations (SHAP)-Modell, um Ihnen dabei zu helfen, zu quantifizieren, wie jedes Feature oder jede Variable zu Ihrem Empfehlungsmodell beiträgt. Jeder Punkt auf dem Chart steht für einen SHAP und die Verteilung der Punkte gibt einen allgemeinen Eindruck von der Richtungswirkung eines Features.

\![SHAPs Report Chart, das ein horizontales Balkendiagramm mit mehreren farbigen Balken anzeigt, die verschiedene Features oder Variablen darstellen. Jeder Balken zeigt die Auswirkung eines Features auf das Empfehlungsmodell, wobei die x-Achse mit dem SHAP-Wert beschriftet ist und die y-Achse die Namen der Features wie Häufigkeit, Frequenz und Kanal auflistet. Das Chart visualisiert, wie jedes Feature positiv oder negativ zu den Prognosen des Modells beiträgt.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnostik

Der Diagnosebericht enthält zwei verschiedene Berichtstypen: **Ausgehend** und **eingehend**.

{% tabs local %}
{% tab outbound %}
Der Bericht zur ausgehenden Diagnostik zeigt das tägliche Volumen der generierten und aktivierten Empfehlungen für Ihre Zielgruppen. Nutzen Sie das Tracking, um Probleme bei der Zustellung zu erkennen, Aktivierungsspitzen oder -rückgänge zu verfolgen und zu überprüfen, ob die Nachrichten die richtigen Gruppen wie erwartet erreichen.

\![Ausgehender Diagnosebericht mit einem Line Chart, der das tägliche Tracking des Volumens der generierten und aktivierten Empfehlungen für verschiedene Zielgruppen anzeigt. Das Chart zeigt zwei Linien mit den Bezeichnungen Generiert und Aktiviert, wobei die y-Achse die Anzahl der Empfehlungen und die x-Achse das Datum angibt. Eine Legende kennzeichnet jede Zeile durch eine Farbe. Die Schnittstelle enthält Dropdown-Filter für den Datumsbereich und die Auswahl der Zielgruppe oberhalb des Charts.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

Der eingehende Diagnosebericht überwacht den Zustand Ihrer Daten-Feeds in BrazeAI™. Es verfolgt Details wie die Anzahl der Dateien, die Größe und das Zeilenvolumen für jedes Asset. So können Sie sicherstellen, dass die Daten wie erwartet einfließen und Fehlerbehebungen durchführen, bevor sie sich auf Ihre Modelle oder Kampagnen auswirken.

Über das Dropdown-Menü können Sie verschiedene Metriken für den Chart auswählen, z.B. die durchschnittliche Dateigröße oder die Anzahl der Dateien.

\![Eingehender Diagnosebericht mit einem Liniendiagramm zum Tracking der täglichen Dateizahl und der durchschnittlichen Dateigröße der an BrazeAI™ zugestellten Daten. Das Chart zeigt zwei Linien mit den Bezeichnungen File count und Average file size MBs, wobei die y-Achse die Werte und die x-Achse das Datum anzeigt. Oberhalb des Charts befinden sich Dropdown-Filter für die Auswahl des Datumsbereichs und der Daten-Assets.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

In der folgenden Tabelle finden Sie weitere Einzelheiten zu den einzelnen Metriken im eingehenden Bericht:

| Feld | Beschreibung |
|-------|-------------|
| Daten-Asset | Der Name des zugestellten Datensatzes oder der Datei. |
| Datum | Das Datum, an dem die Daten empfangen wurden. |
| Letzter Zustellungszeitpunkt | Der Zeitpunkt, zu dem die Daten zuletzt zugestellt wurden. |
| Anzahl der Dateien | Die Gesamtzahl der empfangenen Dateien. |
| Maximale Dateigröße (MBs) | Die Größe der größten empfangenen Datei, in Megabyte. |
| Durchschnittliche Dateigröße (MBs) | Die durchschnittliche Größe aller empfangenen Dateien, in Megabyte. |
| Anzahl der Dateizeilen | Die Gesamtzahl der in den zugestellten Dateien enthaltenen Zeilen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Zeitleiste

Der Zeitleistenbericht bietet eine visuelle Aufzeichnung der wichtigsten Ereignisse zusammen mit Ihren Performance-Metriken. Zu diesen Ereignissen gehören Modellläufe, Konfigurationsänderungen, Updates der Leitplanken und mehr. Anmerkungen erscheinen direkt in den Uplift-Charts und in einem speziellen Tab für die Zeitleiste, so dass Sie Veränderungen in den Ergebnissen sofort erkennen können, ohne historische Veränderungen tracken zu müssen.

\![Timeline-Bericht, der ein Chart mit Performance-Metriken im Zeitverlauf anzeigt. Wichtige Ereignisse wie Modellläufe, Konfigurationsänderungen und Leitplanken-Updates sind in der Zeitleiste durch Symbole gekennzeichnet. Unterhalb des Charts werden in einer Tabelle Ereignisse mit Spalten für Datum, Typ, Beschriftung, Details und Sichtbarkeit in Charts aufgelistet.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

Um die Performance zwischen zwei Gruppen zu vergleichen, wählen Sie in den Dropdown-Listen die gewünschten Vergleichskriterien aus. In der folgenden Tabelle finden Sie weitere Einzelheiten:

| Feld | Beschreibung |
|-------|-------------|
| Datum | Das Datum, an dem das Ereignis eingetreten ist. |
| Typ | Die Kategorie des Ereignisses, z. B. System-Update, Modelllauf oder Konfigurationsänderung. |
| Beschriftung | Der Name oder Bezeichner des Ereignisses. |
| Details | Zusätzliche Informationen, die das Ereignis beschreiben. |
| Sichtbar in Charts | Gibt an, ob das Ereignis in verwandten Charts angezeigt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

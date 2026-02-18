---
nav_title: Berichte und Insights
article_title: Berichte und Insights
description: "Erfahren Sie, wie Sie Berichte aus dem BrazeAI Decisioning Studio™ in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Kampagnen beeinflussen."
page_order: 3
---

# Berichte und Insights

> Erfahren Sie, wie Sie Berichte aus dem BrazeAI Decisioning Studio™ in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Kampagnen beeinflussen. Von Metriken, Performance und Datenintegrität bis hin zu Systemänderungen – diese Berichte helfen Ihnen, Ergebnisse zu verstehen, Fehler zu beheben und zuversichtlich gut informierte Entscheidungen zu treffen.

## Voraussetzungen

Bevor Sie die Berichte von Decisioning Studio in der Braze anzeigen können, müssen Sie:

- Es besteht ein aktiver Vertrag für Braze und BrazeAI Decisioning Studio™. 
- Ihr CSM hat BrazeAI Decisioning Studio™ in Ihrem Namen für Sie aktiviert.
- Sie verfügen über einen Live-Agenten von BrazeAI Decisioning Studio™.

## Berichte anzeigen {#view}

Um Metriken für einen Decisioning Studio-Agenten in Braze anzuzeigen, gehen Sie zu **KI Decisioning** > **BrazeAI Decisioning Studio™** und wählen Sie einen Agenten aus.

![Der Startbildschirm des BrazeAI Decisioning Studio™ für Berichte zeigt ein Dashboard mit mehreren Berichtskarten. Jede Karte zeigt einen Berichtstyp (z. B. Performance, Insights, Diagnosen und Zeitleiste) mit kurzen Beschreibungen und Symbolen für jeden Bericht an.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Hier können Sie z. B. Berichte über Performance, Insights, Diagnosen oder Zeitleisten einsehen. Weitere Einzelheiten finden Sie unter [Verfügbare Berichte](#reports).

## Berichtsdaten ändern

Nachdem dem [Öffnen eines Berichts](#view) können Sie den Datumsbereich ändern, indem Sie ein neues Start- und Enddatum aus dem Kalender-Dropdown-Menü auswählen.

![Der BrazeAI Decisioning Studio™ SELEKTOR für den Datumsbereich ist mit einem Kalender-Dropdown geöffnet. Der Kalender zeigt auswählbare Start- und Enddaten zur Anpassung der Berichtsansicht.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Sie können auch ein Standard-Startdatum festlegen oder bestimmte Termine auswählen, die immer ausgeschlossen werden sollen. Die ausgeschlossenen Daten werden aus allen Berichten für diesen Agenten herausgefiltert.

Um Tage festzulegen oder auszuschließen, wählen Sie <i class="fa-solid fa-gear"></i> **Einstellungen** aus. Dort können Sie das Standarddatum ändern oder Daten ausschließen.

![In BrazeAI Decisioning Studio™ geöffnetes Panel mit Optionen zum Festlegen eines Standard-Startdatums und zum Ausschluss bestimmter Daten aus Berichten. Das Panel enthält die zwei Abschnitte „Standard-Startdatum“ und „Daten ausschließen“. Unter „Daten ausschließen“ sind mehrere Termine mit je einem Kontrollkästchen aufgeführt.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Verfügbare Berichte {#reports}

### Performance

Der Performance-Bericht bietet Metriken für Agenten auf hoher Ebene, die Behandlungsgruppen (von Braze) mit einer oder mehreren Kontrollgruppen (z.B. Umsatz) vergleichen. Er unterstützt zwei verschiedene Ansichten: **Trending** und **Treiberbaum**.

Standardmäßig verwendet der Bericht die **Trending**-Ansicht, die vergleicht, wie BrazeAI™ gegenüber Ihren Kontrollgruppen im Zeitverlauf performt, und die Uplift-Entwicklung trackt.

![Die Trendansicht des Leistungsberichts zeigt ein Liniendiagramm, in dem die Performance von BrazeAI™ und der Kontrollgruppe im Zeitverlauf verglichen wird. Der Chart zeigt zwei Linien mit den Bezeichnungen „BrazeAI™“ und „Kontrollgruppe“, wobei die y-Achse mit „Uplift“ und die x-Achse mit Daten beschriftet ist. Außerdem gibt es eine Farblegende für die Gruppen.]({% image_buster /assets/img/decisioning_studio/reporting_agent_performance_trending.png %})

Alternativ können Sie den **Treiberbaum** auswählen. So sehen Sie auf einen Blick, wie die wichtigsten Werttreiber mit den Targeting-Metriken verknüpft sind, und können die Beziehung zwischen ihnen besser verstehen.

![Die Baumansicht der Performance-Berichtstreiber zeigt ein hierarchisches Diagramm, das die wichtigsten Werttreiber auf Targeting-Metriken abbildet. Das Diagramm zeigt mehrere miteinander verbundene Knoten an, die jeweils mit dem Namen eines Treibers oder einer Metrik beschriftet sind. Daran können Sie sehen, wie verschiedene Faktoren zur Gesamtperformance beitragen.]({% image_buster /assets/img/decisioning_studio/reporting_performance_drivertree.png %})

Um die Performance zweier Gruppen zu vergleichen, wählen Sie in den Dropdown-Listen die gewünschten Vergleichskriterien aus. In der folgenden Tabelle finden Sie weitere Einzelheiten:

| Feld | Beschreibung |
|-------|-------------|
| Vergleichsgruppen | Die Gruppen, die Sie in Ihrem Bericht vergleichen möchten. |
| Aggregation | Die Art und Weise, wie der Bericht Daten gruppiert, z. B. Summen, Durchschnittswerte oder Prozentsätze. |
| Segmente | Die [Zielgruppensegmente]({{site.baseurl}}/user_guide/engagement_tools/segments/), die Sie in Braze erstellt haben. |
| Zeitleisten-Events | Die konkreten Events, die im Laufe der Zeit angezeigt werden, wie z. B. der Versand von Nachrichten, Öffnungen oder Konversionen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Insights

Insights zeigen Ihnen, wie die verschiedenen Empfehlungsoptionen in Ihrer Aktionsbank erstellt werden, z.B. die Blockauswahl. Es gibt zwei verschiedene Insights-Berichte: **Agentenpräferenzen** und **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
Der Bericht über die **Agentenpräferenzen** hilft Ihnen, saisonale Trends zu erkennen und die Relevanz der Auswahl in der Aktionsbank zu bewerten, um fundierte Entscheidungen für Updates zu treffen.

![Der Bericht zu den Agentenpräferenzen zeigt ein Balkendiagramm, in dem verglichen wird, wie oft verschiedene Empfehlungsoptionen über einen bestimmten Zeitraum ausgewählt wurden. Der Chart zeigt mehrere farbige Balken an, von denen jeder eine Empfehlungsoption aus der Aktionsbank vertritt. Die y-Achse ist mit dem Prozentsatz der gewählten Optionen beschriftet, die x-Achse mit den Optionen.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

In der folgenden Tabelle finden Sie weitere Einzelheiten zu diesem Bericht:

| Feld | Beschreibung |
|-------|-------------|
| Dimension | Das Attribut, das zur Organisation der Ergebnisse verwendet wird, z. B. Kanal, Kampagne oder Plattform. |
| Vergleichsgruppe | Die Gruppen, die Sie in Ihrem Bericht vergleichen möchten. Sie können mehrere Vergleichsgruppen auswählen. |
| Parameter | Die Metrik, die auf dieses Attribut angewendet wird, z. B. Öffnungen, Klicks oder Konversionsrate. |
| Segment | Das [Zielgruppensegment]({{site.baseurl}}/user_guide/engagement_tools/segments/), das Sie in Braze erstellt haben. |
| Option             | Die konkrete Empfehlungsoption, die aus der Aktionsbank ausgewählt wurde. |
| Beschreibung        | Eine kurze Erklärung, was die Option bedeutet.            |
| Häufigkeit  | Wie oft die Option insgesamt ausgewählt wurde.         |
| Erfolgsquote   | Der Prozentanteil der gesamten Auswahlen, bei denen diese Option gewählt wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab shaps %}
Der **SHAPs-Bericht** verwendet das Shapley Additive ExPlanations (SHAP)-Modell, um Ihnen dabei zu helfen, zu quantifizieren, wie jedes Feature oder jede Variable zu Ihrem Empfehlungsagenten beiträgt. Jeder Punkt im Chart steht für einen SHAP und die Verteilung der Punkte gibt einen allgemeinen Eindruck davon, wie die Features wirken.

![SHAPs Report Chart, das ein horizontales Balkendiagramm mit mehreren farbigen Balken anzeigt, die verschiedene Features oder Variablen darstellen. Jeder Balken zeigt die Auswirkung eines Features auf den Empfehlungsagenten, wobei die x-Achse mit dem SHAP-Wert beschriftet ist und die y-Achse die Namen der Features wie Häufigkeit, Frequenz und Kanal auflistet. Das Chart visualisiert, wie jedes Feature positiv oder negativ zu den Prognosen des Agenten beiträgt.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}

### Diagnostik

Der Diagnosebericht enthält zwei verschiedene Berichtstypen: **ausgehend** und **eingehend**.

{% tabs local %}
{% tab outbound %}
Der Diagnosebericht für ausgehende Nachrichten zeigt das tägliche Volumen der generierten und aktivierten Empfehlungen für Ihre Zielgruppen. Nutzen Sie das Tracking, um Probleme bei der Zustellung zu erkennen, Aktivierungsspitzen oder -rückgänge zu verfolgen und zu überprüfen, ob die Nachrichten die erwarteten Gruppen erreichen.

![Ausgehender Diagnosebericht mit einem Line Chart, der das tägliche Tracking des Volumens der generierten und aktivierten Empfehlungen für verschiedene Zielgruppen anzeigt. Der Chart zeigt zwei Linien mit den Bezeichnungen „Generiert“ und „Aktiviert“. Die y-Achse zeigt die Anzahl der Empfehlungen, die x-Achse das Datum. Außerdem gibt es eine Farblegende für die Linien. In der Benutzeroberfläche befinden sich über den Charts Dropdown-Filter für den Datumsbereich und die Auswahl der Zielgruppe.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

Der Diagnosebericht über eingehende Nachrichten überwacht die Integrität Ihrer Daten-Feeds in BrazeAI™. Es verfolgt Details wie die Anzahl der Dateien, die Größe und das Zeilenvolumen für jedes Asset. So können Sie sicherstellen, dass die Daten wie erwartet einfließen und Fehlerbehebungen durchführen, bevor sie sich auf Ihre Agenten oder Kampagnen auswirken.

Über das Dropdown-Menü können Sie verschiedene Metriken für den Chart auswählen, z. B. die durchschnittliche Dateigröße oder die Anzahl der Dateien.

![Eingehender Diagnosebericht mit einem Liniendiagramm zum Tracking der täglichen Dateizahl und der durchschnittlichen Dateigröße der an BrazeAI™ zugestellten Daten. Der Chart enthält zwei Linien mit den Bezeichnungen „Dateianzahl“ und „Durchschnittliche Dateigröße in MB“. Die y-Achse zeigt die Werte, die x-Achse das Datum an. Oberhalb des Charts befinden sich Dropdown-Filter für die Auswahl des Datumsbereichs und der Daten-Assets.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

In der folgenden Tabelle finden Sie weitere Details zu den einzelnen Metriken im Bericht zu eingehenden Nachrichten:

| Feld | Beschreibung |
|-------|-------------|
| Daten-Asset | Der Name des zugestellten Datensatzes oder der Datei. |
| Datum | Das Datum, an dem die Daten empfangen wurden. |
| Letzte Zustellungszeit | Der Zeitpunkt, zu dem die Daten zuletzt zugestellt wurden. |
| Anzahl der Dateien | Die Gesamtzahl der empfangenen Dateien. |
| Maximale Dateigröße (MB) | Die Größe der größten empfangenen Datei in Megabyte. |
| Durchschnittliche Dateigröße (MB) | Die durchschnittliche Größe aller empfangenen Dateien in Megabyte. |
| Anzahl der Dateizeilen | Die Gesamtzahl der in den zugestellten Dateien enthaltenen Zeilen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

### Zeitleiste

Der Zeitleisten-Bericht bietet eine visuelle Aufzeichnung der wichtigsten Events zusammen mit Ihren Performance-Metriken. Zu diesen Ereignissen gehören Agentenläufe, Konfigurationsänderungen, Updates der Leitplanken und mehr. Anmerkungen werden direkt in den Uplift-Charts und in einem speziellen Tab für die Zeitleiste angezeigt. So können Sie Veränderungen in den Ergebnissen sofort erkennen, ohne Veränderungen tracken zu müssen.

![Zeitleistenbericht mit einem Chart mit Performance-Metriken im Zeitverlauf. Wichtige Ereignisse, wie z.B. Agentenläufe, Konfigurationsänderungen und Updates der Leitplanken, werden in der Zeitleiste durch Symbole gekennzeichnet. Unter dem Chart werden in einer Tabelle Events mit Spalten für Datum, Typ, Beschriftung, Details und Sichtbarkeit in Diagrammen aufgelistet.]({% image_buster /assets/img/decisioning_studio/reporting_timeline.png %})

Um die Performance zweier Gruppen zu vergleichen, wählen Sie in den Dropdown-Listen die gewünschten Vergleichskriterien aus. In der folgenden Tabelle finden Sie weitere Einzelheiten:

| Feld | Beschreibung |
|-------|-------------|
| Datum | Das Datum, an dem das Event eingetreten ist. |
| Typ | Die Kategorie des Ereignisses, z. B. System-Update, Agentenlauf oder Konfigurationsänderung. |
| Label | Der Name oder Bezeichner des Events. |
| Details | Zusätzliche Informationen, die das Event beschreiben. |
| Sichtbar in Charts | Gibt an, ob das Event in den entsprechenden Diagrammen angezeigt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

---
nav_title: Berichte und Insights
article_title: Berichte und Insights
description: "Erfahren Sie, wie Sie Berichte aus dem BrazeAI Decisioning Studio™ in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Kampagnen beeinflussen."
page_order: 3
---

# Berichte und Insights

> Erfahren Sie, wie Sie Berichte aus dem BrazeAI Decisioning Studio™ in Braze anzeigen können, damit Sie verstehen, wie KI-gestützte Entscheidungen Ihre Kampagnen beeinflussen. Von Performance-Metriken über Datenintegrität bis hin zu Systemänderungen – diese Berichte helfen Ihnen, Ergebnisse zu verstehen, Probleme zu beheben und fundierte Entscheidungen mit Zuversicht zu treffen.

## Voraussetzungen

Bevor Sie Decisioning Studio-Berichte in Braze anzeigen können, müssen folgende Bedingungen erfüllt sein:

- Ein aktiver Vertrag für Braze und BrazeAI Decisioning Studio™ liegt vor.
- Kontaktieren Sie Ihren CSM, damit BrazeAI Decisioning Studio™ in Ihrem Namen für Sie aktiviert wird.
- Ein aktiver BrazeAI Decisioning Studio™-Agent ist vorhanden.

## Berichte anzeigen {#view}

Um die Metriken für einen Decisioning Studio-Agenten in Braze anzuzeigen, navigieren Sie zu **AI Decisioning** > **BrazeAI Decisioning Studio™** und wählen Sie anschließend einen Agenten aus.

![Der Startbildschirm von BrazeAI Decisioning Studio™ zeigt ein Dashboard mit mehreren Berichtskarten an. Jede Karte zeigt einen Berichtstyp wie Performance, Insights, Diagnosen und Zeitleiste mit kurzen Beschreibungen und Symbolen für jeden Bericht an.]( {% image_buster /assets/img/decisioning_studio/reporting_home.png %} )

Hier können Sie Berichte wie Performance, Insights, Diagnosen und Zeitleisten einsehen. Weitere Einzelheiten finden Sie unter [Verfügbare Berichte](#available-reports).

## Berichtsdaten ändern

Nach dem [Öffnen eines Berichts](#view) können Sie den Datumsbereich ändern, indem Sie ein neues Start- und Enddatum aus dem Kalender-Dropdown-Menü auswählen.

![BrazeAI Decisioning Studio™ Datumsbereichs-Selektor mit einem Kalender-Dropdown-Menü. Der Kalender zeigt auswählbare Start- und Enddaten zur Anpassung der Berichtsansicht.]({% image_buster /assets/img/decisioning_studio/reporting_change_date_range.png %}){: style="max-width:50%;"}

Sie können auch ein Standard-Startdatum festlegen oder bestimmte Daten auswählen, die immer ausgeschlossen werden sollen. Ausgeschlossene Daten werden aus allen Berichten für diesen Agenten herausgefiltert.

Um Daten festzulegen oder auszuschließen, wählen Sie <i class="fa-solid fa-gear"></i> **Einstellungen** aus und ändern Sie dann Ihr Standarddatum oder schließen Sie Daten nach Bedarf aus.

![Das Einstellungen-Panel in BrazeAI Decisioning Studio™ ist geöffnet und zeigt Optionen zum Festlegen eines Standard-Startdatums und zum Ausschließen bestimmter Daten aus Berichten an. Das Panel enthält die zwei Abschnitte „Standard-Startdatum" und „Daten ausschließen". Unter „Daten ausschließen" sind mehrere Daten mit je einem Kontrollkästchen aufgeführt.]({% image_buster /assets/img/decisioning_studio/reporting_set_exclude_dates.png %})

## Verfügbare Berichte {#available-reports}

- [Performance]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/performance/): Übergeordnete Agenten-Metriken, die Behandlungsgruppen mit Kontrollgruppen vergleichen, mit den Ansichten **Trending** und **Treiberbaum**.
- [Insights]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/insights/): Wie Empfehlungsoptionen in Ihrer Aktionsbank generiert werden, einschließlich Agentenpräferenzen und SHAPs-Berichten.
- [Diagnosen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/diagnostics/): Datenintegrität für ausgehende und eingehende Daten, einschließlich Empfehlungsvolumen und Daten-Feed-Überwachung.
- [Zeitleiste]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/reporting/timeline/): Eine visuelle Aufzeichnung wichtiger Events (Agent-Ausführungen, Konfigurationsänderungen, Updates der Sicherheitsvorkehrungen) zusammen mit Performance-Metriken.
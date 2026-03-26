---
nav_title: Diagnose
article_title: Diagnosebericht
page_order: 3
description: "Erfahren Sie, wie Sie den Diagnosebericht verwenden, um die Integrität ausgehender und eingehender Daten in BrazeAI Decisioning Studio zu überwachen."
---

# Diagnosebericht

> Der Diagnosebericht enthält zwei verschiedene Berichtstypen: **Ausgehend** und **Eingehend**.

{% tabs local %}
{% tab outbound %}
Der Diagnosebericht für ausgehende Daten zeigt das tägliche Volumen der generierten und aktivierten Empfehlungen über Ihre Zielgruppen hinweg. Nutzen Sie ihn, um Zustellungsprobleme zu erkennen, Spitzen oder Einbrüche bei Aktivierungen zu verfolgen und zu bestätigen, dass Nachrichten die richtigen Gruppen wie erwartet erreichen.

![Diagnosebericht für ausgehende Daten mit einem Linien-Chart, das das tägliche Volumen der generierten und aktivierten Empfehlungen für verschiedene Zielgruppen verfolgt. Das Chart zeigt zwei Linien mit den Bezeichnungen „Generiert" und „Aktiviert", wobei die y-Achse die Zahl der Empfehlungen und die x-Achse die Datumsangaben darstellt. Eine Legende identifiziert jede Linie anhand der Farbe. Die Schnittstelle enthält Dropdown-Filter für Datumsbereich und Zielgruppenauswahl oberhalb des Charts.]({% image_buster /assets/img/decisioning_studio/reporting_diagnostics_outbound.png %})

{% endtab %}

{% tab inbound %}

Der Diagnosebericht für eingehende Daten überwacht die Integrität Ihrer Daten-Feeds in BrazeAI<sup>TM</sup>. Er verfolgt Details wie Dateianzahl, Dateigrößen und Zeilenvolumen für jedes Asset und hilft Ihnen zu bestätigen, dass Daten wie erwartet einfließen, sowie Probleme zu beheben, bevor sie Ihre Agenten oder Kampagnen beeinträchtigen.

Sie können das Dropdown verwenden, um verschiedene Chart-Metriken auszuwählen, wie z. B. die durchschnittliche Dateigröße oder die Dateianzahl.

![Diagnosebericht für eingehende Daten mit einem Linien-Chart, das die tägliche Dateianzahl und durchschnittliche Dateigröße für an BrazeAI<sup>TM</sup> zugestellte Daten-Assets verfolgt. Das Chart zeigt zwei Linien mit den Bezeichnungen „Dateianzahl" und „Durchschnittliche Dateigröße MBs", wobei die y-Achse die Werte und die x-Achse die Datumsangaben darstellt. Oberhalb des Charts befinden sich Dropdown-Filter für Datumsbereich und Daten-Asset-Auswahl.]( {% image_buster /assets/img/decisioning_studio/reporting_diagnostics_inbound.png %} )

In der folgenden Tabelle finden Sie weitere Details zu jeder Metrik im Bericht für eingehende Daten:

| Feld | Beschreibung |
|-------|-------------|
| Daten-Asset | Der Name des zugestellten Datensatzes oder der zugestellten Datei. |
| Datum | Das Datum, an dem die Daten empfangen wurden. |
| Letzte Zustellungszeit | Der letzte Zeitpunkt, zu dem die Daten zugestellt wurden. |
| Dateianzahl | Die Gesamtzahl der empfangenen Dateien. |
| Max. Dateigröße (MBs) | Die Größe der größten empfangenen Datei in Megabyte. |
| Durchschnittliche Dateigröße (MBs) | Die durchschnittliche Größe aller empfangenen Dateien in Megabyte. |
| Dateizeilenanzahl | Die Gesamtzahl der Zeilen in den zugestellten Dateien. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}
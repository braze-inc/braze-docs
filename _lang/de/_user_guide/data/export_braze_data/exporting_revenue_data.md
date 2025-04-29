---
nav_title: Daten zu Exporteinnahmen und Gesamteinnahmen
article_title: Daten zu Exporteinnahmen und Gesamteinnahmen
page_order: 4
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Umsatzdaten und Statistiken exportieren können."
tool: 
  - Reports

---

# Daten zu Exporteinnahmen und Gesamteinnahmen

> Auf dieser Seite finden Sie die Seite [Umsatzbericht]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report/) des Dashboards, auf der Sie Daten zum Umsatz in bestimmten Zeiträumen, zum Umsatz eines bestimmten Produkts und zum Gesamtumsatz Ihrer App einsehen können.

Sie finden den **Umsatzbericht** unter **Analytics**.

{% alert tip %}
Suchen Sie nach weiteren Möglichkeiten, Daten über Ihre Einnahmen zu erhalten? Versuchen Sie, Kaufverhalten (sowie den Kauf eines Produkts) als [Konversions-Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) zu Kampagnen oder Canvase hinzuzufügen.
{% endalert %}

Um Ihre Umsatzdaten zu exportieren, wählen Sie <i class="fas fa-bars" title="Chart Kontextmenü"></i> im Diagramm **Performance im Zeitverlauf** und wählen Sie Ihre Exportoption.

## Grafik Performance im Zeitverlauf

Die folgenden Daten können im Diagramm **Performance im Zeitverlauf** angezeigt werden:

- KPI-Formeln
- Käufe
    - (Optional) Käufe nach Produkt
- Umsatz
    - (Optional) Umsatzerlös nach Segmenten
    - (fakultativ) Umsatzerlöse nach Produkten
- Umsatz pro Stunde
    - (Fakultativ) Umsatz pro Stunde nach Segmenten
- Umsatz pro Nutzer:in

![Grafik Einnahmen][9]

## Umsatz gesamt

Sie können die Umsatzstatistiken von Fall zu Fall auf den Seiten [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) oder [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) einsehen. 

{% multi_lang_include metrics.md metric='Total Revenue' %}

{% alert tip %}
Umsatzberichte können nicht über APIs exportiert werden. Hilfe zum CSV-Export finden Sie unter [Fehlerbehebung beim Export]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

{% comment %}

## Direkte Einnahmen

Sie können die folgenden zusätzlichen Metriken zum Umsatz einsehen, indem Sie mit dem [Berichts-Builder][1] einen Kampagnenvergleichsbericht erstellen:

- [Direkter Umsatz gesamt][2]
- [Direkte Käufe gesamt][3]
- [Eindeutige Direktkäufe][4]
- [Umsatz pro Empfänger:in][5]

Diese Metriken basieren auf der Attribution des letzten Klicks, was bedeutet, dass der Umsatz einer Kampagne zugerechnet wird, wenn diese Kampagne:

1. Ist die letzte Kampagne, die der Nutzer:innen vor dem Kauf angeklickt hat.
    <br>**UND**<br>
2. Wurde vom Nutzer:innen weniger als 3 Tage vor dem Kauf angeklickt

{% endcomment %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-revenue
[3]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#total-direct-purchases
[4]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#unique-direct-purchases
[5]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#revenue-per-recipient



[9]: {% image_buster /assets/img_archive/Export_revenue_graph.png %}

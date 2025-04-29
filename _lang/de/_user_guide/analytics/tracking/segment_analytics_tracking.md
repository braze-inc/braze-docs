---
nav_title: Segment Analytics Tracking
article_title: Segment Analytics Tracking
page_order: 8
page_type: reference
description: "Dieser Artikel referenziert das Segment Analytics Tracking und zeigt Ihnen, wie Sie Umsätze und Käufe im Zeitverlauf, Sitzungen im Zeitverlauf und angepasste Events im Zeitverlauf betrachten können."
tool: 
  - Segments
  - Reports
---

# Segment Analytics Tracking

> Wenn das Analytics Tracking für ein Segment aktiviert ist, können Sie Sitzungen, angepasste Events und Umsätze im Zeitverlauf für dieses Segment anzeigen.

Wenn Sie das Analytics Tracking für ein Segment nicht einschalten, können Sie dennoch auf [Realtime-Statistiken][11] für dieses Segment zugreifen und die Nutzer:innen mit Kampagnen ansprechen. Der einzige Unterschied besteht darin, ob Sie auf die auf dieser Seite erwähnten Analyse-Tools zugreifen können.

## Einschalten von Segment Analytics

Schalten Sie auf der Seite **Segment Details** eines Segments **Analytics Tracking** ein.

![Analytics Tracking für ein Segment umschalten][16]

In einer App kann das Tracking für bis zu 25 Segmente aktiviert werden. Braze empfiehlt das Tracking von Segmenten, die für Sie wichtig sind, um die Auswirkungen Ihrer Kampagnen auf Sitzungen, Umsätze und Käufe zu analysieren.

## Anzeigen der Einnahmen und Käufe im Laufe der Zeit

Gehen Sie zu **Analytics** > **Umsatzbericht**, um Daten zu [Umsatz und Käufen im Zeitverlauf für dieses Segment][14] anzuzeigen.

![Daten zu den Einnahmen nach Segmenten][17]

Um die Daten der Segmente für jeden angepassten Zeitraum visuell zu vergleichen, fügen Sie dem Diagramm Segmente hinzu oder entfernen sie. Wählen Sie in der Dropdown-Liste **Aufschlüsselung** die Option **Nach Segmenten** und wählen Sie dann Ihre Segmente in **Aufschlüsselung Werte** aus.

Wählen Sie einen beliebigen Segmentnamen oberhalb des Diagramms aus, um die Sichtbarkeit der Metriken für dieses Segment ein- oder auszuschalten.

![Umsätze für mehrere Segmente][21]

## Sitzungen im Laufe der Zeit

Auf ähnliche Weise finden Sie auf der **Startseite** Daten über [Sitzungen im Zeitverlauf für dieses bestimmte Segment][13].

![Sitzungsdaten nach Segmenten][18]

## Angepasste Events im Zeitverlauf anzeigen

Sehen Sie sich Daten über [Angepasste Events im Zeitverlauf für Segmente][20] an, indem Sie zu **Analytics** > Bericht über angepasste Events gehen.

## Verwendung von Query Builder Templates

Wenn das Analytics Tracking aktiviert ist, können Sie mit den Templates des Query Builders die Performance-Metriken für Kampagnen, Canvas, Varianten und Schritte nach Segmenten aufschlüsseln. Wenn Sie mehr erfahren möchten, lesen Sie [Segmente Daten]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment).

[11]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#segment-statistics
[13]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data
[14]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[16]: {% image_buster /assets/img_archive/A_Tracking_2.png %}
[17]: {% image_buster /assets/img_archive/Revenue.png %}
[18]: {% image_buster /assets/img_archive/events_over_time2.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[21]: {% image_buster /assets/img_archive/segment_revenue_multiple.png %}

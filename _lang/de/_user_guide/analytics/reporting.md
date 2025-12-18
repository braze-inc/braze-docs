---
nav_title: Ihre Berichte
article_title: Ihre Berichte
page_order: 7
layout: dev_guide
guide_top_header: "Ihre Berichte"
guide_top_text: "Ihre Daten bedeuten Ihnen sehr viel, deshalb haben wir innerhalb von Braze (ohne <a href='/docs/user_guide/data/distribution/braze_currents/'>Currents</a>) mehrere Berichtsoptionen eingerichtet. Wenn Sie nicht sicher sind, wo Sie anfangen sollen, lesen Sie die <a href='/docs/user_guide/analytics/reporting/#reports-overview'>Übersicht über die Berichte</a> und Analytics, die Sie zur Beantwortung gängiger Fragen zur Marketing Strategie verwenden können."

page_type: landing
description: "Auf dieser Landing Page finden Sie Artikel über die in Braze (ohne Currents) verfügbaren Berichtsoptionen, darunter Segmente, Engagement-Berichte, den Berichts-Builder und mehr."
tool: Reports
search_rank: 2
guide_featured_title: "Abschnittsartikel"
guide_featured_list:
  - name: Glossar zu den Berichtsmetriken
    link: /docs/user_guide/analytics/reporting/report_metrics/
    image: /assets/img/braze_icons/book-closed.svg
  - name: Segmentdaten
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Engagement-Berichte
    link: /docs/user_guide/analytics/reporting/engagement_reports/
    image: /assets/img/braze_icons/line-chart-up-01.svg
  - name: Berichts-Builder
    link: /docs/user_guide/analytics/reporting/report_builder/
    image: /assets/img/braze_icons/tool-01.svg
  - name: Dashboard-Builder
    link: /docs/user_guide/analytics/reporting/dashboard_builder/
    image: /assets/img/braze_icons/tool-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Berichte konfigurieren
    link: /docs/user_guide/analytics/reporting/configuring_reporting/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Kampagnen-Analytics
    link: /docs/user_guide/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Canvas Analytics
    link: /docs/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/
    image: /assets/img/braze_icons/line-chart-down-01.svg
  - name: Angepasste Events
    link: /docs/user_guide/data/custom_data/custom_events/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Funnel-Bericht
    link: /docs/user_guide/analytics/reporting/funnel_reports/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Global Control Bericht
    link: /docs/user_guide/engagement_tools/testing/global_control_group/
    image: /assets/img/braze_icons/globe-04.svg
  - name: Bindungsbericht
    link: /docs/user_guide/analytics/reporting/retention_reports/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Daten zur Einnahme
    link: /docs/user_guide/data/export_braze_data/exporting_revenue_data/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Umsatzbericht
    link: /docs/user_guide/analytics/reporting/revenue_report/
    image: /assets/img/braze_icons/piggy-bank-02.svg
  - name: Segment-Insights
    link: /docs/user_guide/engagement_tools/segments/segment_insights/#segment-insights
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Bericht zur globalen Kontrollgruppe
    link: /docs/user_guide/analytics/reporting/global_control_group_reporting/
    image: /assets/img/braze_icons/globe-slated-02.svg
---

# Übersicht der Berichte

## Welche Variante hat gewonnen?

{% tabs local %}
{% tab Campaign Analytics %}
**Kampagnen-Analytics**

Mit [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) erhalten Sie Realtime-Updates zu den Ergebnissen der einzelnen Kampagnen und Varianten innerhalb dieser Kampagnen sowie zu den Details auf Nachrichtenebene. Sie können den Datumsbereich anpassen, um die Performance Ihrer Kampagne im Laufe der Zeit zu verstehen, und eine Vorschau Ihrer Nachrichten anzeigen, um sich an Ihre Tests zu erinnern.

{% endtab %}

{% tab Canvas Analytics %}
**Canvas-Analytik**

Verwenden Sie [Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), um Top-Statistiken über Ihr Canvas zu erhalten und zu sehen, wie Ihre Messaging Strategie performt. Öffnen Sie ein beliebiges Live-Canvas, um wichtige Statistiken zur Performance anzuzeigen:

- Anzahl der innerhalb des Canvas gesendeten Nachrichten
- Anzahl der Canvas-Aufnahmen
- Konversionsanzahl
- Durch das Canvas generierte Einnahmen
- Geschätzte Zielgruppe insgesamt

<br>

**Performance nach Variante**

[Analysieren Sie Varianten]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) in einem Live-Canvas, um automatisch berechnete Konversionsraten für jedes Konversions-Event anzuzeigen. Sie können auch Uplift- und Konfidenzberechnungen für jede Variante und jedes Konversions-Event in einem einfach zu vergleichenden Tabellenformat anzeigen.

Weitere Fragen, die Sie mit diesem Bericht beantworten können:

- Gab es ein statistisch signifikantes Vertrauen?
- Wie war die Performance von Variante 1 im Vergleich zu Variante 2?

{% endtab %}

{% tab Report Builder %}
**Berichts-Builder**

Verwenden Sie den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), um die Ergebnisse mehrerer Kampagnen oder Canvase in einer einzigen Ansicht zu vergleichen und schnell festzustellen, welche Engagement-Strategien sich am stärksten auf Ihre wichtigsten Metriken ausgewirkt haben.

Sehen Sie sich diese Seite an:

- Erstellen Sie einen Bericht über Kampagnen und Canvase der letzten Woche oder des letzten Monats, berechnen Sie wichtige Metriken und teilen Sie diese mit Ihren Teamkollegen.
- Vergleichen Sie die Performance verschiedener Varianten sowohl für multivariate Tests als auch für Canvase.
- Ermitteln Sie, welcher Messaging-Kanal die meiste Konversion oder das meiste Engagement für eine bestimmte Kampagne oder einen Canvas erzielt hat.
- Verfolgen Sie allgemeine Performance-Trends einer Gruppe von Kampagnen oder Canvase (z.B. alle Nachrichten, die mit einem Tag "Newsletter" verbunden sind).

Weitere Fragen, die Sie mit diesem Feature beantworten können:

- Wie war die Performance der ersten Version meiner Willkommens-E-Mail im Vergleich zur zweiten Version?
- Wie hoch waren meine durchschnittlichen Öffnungsraten bei Push in diesem Monat im Vergleich zum letzten Monat für einen bestimmten Tag?
- Welcher Newsletter des Monats hatte die meisten Konversionen?

{% endtab %}
{% endtabs %}

## Welche Variante wirkte sich am stärksten auf die Bindung aus?

{% tabs local %}
{% tab Retention Reports %}
**Bindungsberichte**

Verwenden Sie Retention Reports für [Kampagnen]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) oder [Canvase]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/), um die Bindung von Nutzer:innen zu messen, die ein ausgewähltes Ereignis in einer bestimmten Kampagne durchgeführt haben.

Sehen Sie sich diesen Bericht an:

- Ermitteln Sie, wie effektiv eine Nachricht für das erneute Engagement von Nutzern:innen war, indem Sie das Vorkommen verschiedener Ereignisse bis zu einem Monat nach Erhalt einer Kampagne analysieren.
- Vergleichen Sie das Vorkommen verschiedener Ereignisse in verschiedenen Varianten eines [A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

Weitere Fragen, die Sie mit diesem Bericht beantworten können:

- Welche Variante wirkte sich am stärksten auf die Bindung aus?
- Wie lange nutzen meine Kund:innen, die diese Kampagne erhalten haben, meine App danach noch?
- Wie hat sich diese Kampagne auf die Bindung nach einem Tag ausgewirkt? Nach 30 Tagen?

{% alert note %} Berichte über die Bindung sind für SMS- und API-getriggerte Kampagnen nicht verfügbar. {% endalert %}

{% endtab %}
{% tab Funnel Report %}

Verwenden Sie Funnel-Berichte für [Kampagnen]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) oder [Canvase]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/), um die Wege zu analysieren, die Ihre Kund:in nach Erhalt einer Kampagne zurücklegen. Sie können auswählen, welche nativen oder angepassten Events in jede Funnel-Analyse einbezogen werden sollen, und dann untersuchen, wie jede Variante im Vergleich zu ihrem ausgewählten Konversionstrichter performt.

Das können Sie mit diesem Bericht tun:

- Verstehen Sie, an welcher Stelle des Konversionstrichters Nutzer:innen abgebrochen sind, und identifizieren Sie Opportunitäten für erneute Interaktionen mit Nachrichten.
- Zeigen Sie Konversionen zu Events an, die bei der Einrichtung der Kampagne ursprünglich nicht als Konversions-Event vorgesehen waren.
- Analysieren Sie den Funnel anhand einer Reihe von Aktionen (z. B. "Wie viel Prozent der Kund:in haben eine E-Mail erhalten, eine Sitzung begonnen, einen Artikel in den Warenkorb gelegt und dann gekauft?").

Weitere Fragen, die Sie mit diesem Bericht beantworten können:

- Wo auf dem Konversionspfad erfolgt die Kundenabwanderung?
- Wie kann ich meine Marketing Strategien verbessern?

{% endtab %}
{% endtabs%}

## Wie engagiert sind meine Nutzer:innen?

{% tabs local %}
{% tab Report Builder %}

Verwenden Sie den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), um die Ergebnisse mehrerer Kampagnen oder Canvase in einer einzigen Ansicht zu vergleichen und schnell festzustellen, welche Engagement-Strategien sich am stärksten auf Ihre wichtigsten Metriken ausgewirkt haben.

Sehen Sie sich diese Seite an:

- Erstellen Sie einen Bericht über Kampagnen und Canvase der letzten Woche oder des letzten Monats, berechnen Sie wichtige Metriken und teilen Sie diese mit Ihren Teamkollegen.
- Ermitteln Sie, welcher Messaging-Kanal die meiste Konversion oder das meiste Engagement für eine bestimmte Kampagne oder einen Canvas erzielt hat.
- Verfolgen Sie allgemeine Performance-Trends einer Gruppe von Kampagnen oder Canvase (z.B. alle Nachrichten, die mit einem Tag "Newsletter" verbunden sind).

Weitere Fragen, die Sie mit diesem Feature beantworten können:

- Wie war die Performance der ersten Version meiner Willkommens-E-Mail im Vergleich zur zweiten Version?
- Wie hoch waren meine durchschnittlichen Öffnungsraten bei Push in diesem Monat im Vergleich zum letzten Monat für einen bestimmten Tag?
- Welcher Newsletter des Monats hatte die meisten Konversionen?

{% endtab %}
{% tab Overview Data %}
**Übersichtsdaten**

Auf der [Übersichtsseite]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) erhalten Sie eine Zusammenfassung der wichtigsten Metriken zur Performance Ihrer App und Insights zur Nutzer:innen-Basis Ihrer App.

Auf dieser Seite finden Sie diese Statistiken:

- Nutzerzahl seit Beginn
- Lifetime-Sitzungen
- Monatlich aktive Nutzer:innen (MAU)
- Daily Active Users (DAU)
- Neue Nutzer:innen
- Kundenbindung
- Tägliche Sitzungen
- Tägliche Sitzungen je MAU

Weitere Fragen, die Sie mit diesem Dashboard beantworten können:

- Kann ich eine Verbesserung der Klebrigkeit im Vergleich zum Vormonat feststellen?
- Sehe ich ein generelles Wachstum für meine iOS oder Android App?
- Wie sieht mein Gesamtvolumen an E-Mails diesen Monat aus?

{% endtab %}
{% tab Engagement Reports %}
**Engagement-Berichte**

Verwenden Sie [Engagement-Berichte]({{site.baseurl}}/user_guide/analytics/reporting/engagement_reports/), um einen wiederkehrenden E-Mail-Export von Engagement-Statistiken für ausgewählte Kampagnen und Canvase einzurichten. Dieser Bericht ist der am stärksten anpassbare und detaillierteste im Dashboard.

Abhängig von Ihrem Messaging-Kanal können Sie die folgenden Statistiken exportieren:

| Kanal| Statistiken verfügbar|
| ------| --------------|
| E-Mail | Sendungen, Öffnungen, Eindeutige Öffnungen, Klicks, Eindeutige Klicks, Click to Open, Abmeldungen, Bounces, Zustellungen, Spam-Meldungen |
| Push  | Sendungen, Öffnungen, Beeinflusste Öffnungen, Bounces, Body Clicks |
| Web-Push | Sendungen, Öffnungen, Bounces, Body Clicks |
| In-App-Nachricht | Impressionen, Klicks, Erste Schaltflächenklicks, Zweite Schaltflächenklicks |
| Webhook  |  Sendungen, Fehler |
| SMS | Zustellungen, Zustellungen an den Spediteur, Bestätigte Zustellungen, Misslungene Zustellungen, Ablehnungen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Fragen, die Sie mit diesem Bericht beantworten können:

- Wie sieht es mit der Performance all meiner Nachrichten zur Rückgewinnung aus?
- Kampagnenspezifische Gesamtzustellungsrate
- Wie haben sich alle meine Braze Kampagnen im Juni entwickelt? Für das Jahr 2021 bis heute?
- Welche Trends erkenne ich bei multivariaten Tests?

{% endtab %}
{% endtabs %}

## Wie unterscheidet sich das Verhalten der Nutzer:innen nach Segmenten?

{% tabs local %}
{% tab Segment Data %}
**Segmentdaten**

Wenn Sie [Analytics Tracking]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) für ein Segment aktiviert haben, öffnen Sie dieses Segment, um die [Daten des Segments]({{site.baseurl}}/viewing_and_understanding_segment_data/) anzuzeigen. Segmente Daten verfolgen Sitzungen, angepasste Events und Umsätze im Zeitverlauf für die entsprechenden Nutzer:innen.

Auf dieser Seite finden Sie diese Statistiken:

- Gesamtzahl von:
  - Nutzer:innen in Ihrem Segment und wie viel Prozent Ihrer gesamten Nutzerbasis sie ausmachen
  - Per E-Mail erreichbare Nutzerkonten, die E-Mails ausdrücklich zugestimmt haben
  - Per Push-Benachrichtigung erreichbare Nutzerkonten, die Push-Benachrichtigungen ausdrücklich zugestimmt haben
- Durchschnittlicher Lifetime-Value (LTV) für Nutzer:innen in diesem Segment
- Liste der Engagement-Tools, die auf dieses Segment abzielen
- Segment-Insights

{% endtab %}
{% tab Segment Insights %}
**Segment-Insights**

Mit [Segment-Insights]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) können Sie Segmente miteinander vergleichen, um zu verstehen, wie sich die folgenden Metriken auf Dinge wie die Länge des Lebenszyklus und die Sitzungshäufigkeit auswirken können:

- Demografische Daten
- Plattformen
- Einwilligungsstatus
- Kategorie-Einstellungen
- Quittung für die Kampagne

Weitere Fragen, die Sie mit diesem Bericht beantworten können:

- Wie viele Sitzungen wurden nach Erhalt des Onboarding-Canvas im Vergleich zur Kontrollgruppe absolviert?
- Wie groß ist der Unterschied in der Lebensdauer von Nutzern:innen, die sich für Push entschieden haben, im Vergleich zu Nutzern:innen, die sich für E-Mail entschieden haben, und zu Nutzern:innen, die sich für beides entschieden haben?

{% endtab %}
{% tab Custom Events %}
**Benutzerdefinierte Ereignisse**

Verwenden Sie die Seite [Angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-analytics), um zu überwachen, wie oft ein angepasstes Event aufgetreten ist und wann jeder Nutzer:innen es zum letzten Mal für die Segmentierung ausgeführt hat.

Sehen Sie sich diese Seite an:

- Häufigkeit angepasster Events überwachen
- Überwachen Sie angepasste Events nach Segmenten
- Analysieren Sie, wie Kampagnen die Aktivität angepasster Events beeinflussen
- [KPI-Formeln]({{site.baseurl}}/user_guide/data/creating_a_formula/) erstellen und überwachen
- Fehlerbehebung für angepasstes Event Tracking

{% endtab %}
{% endtabs %}

## Hat meine Kampagne eine Kapitalrendite erbracht?

{% tabs local %}
{% tab Revenue Data %}
**Umsatzdaten**

Auf der Seite [Einnahmen]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) können Sie die Einnahmen und Käufe in bestimmten Zeiträumen oder die Gesamteinnahmen oder Käufe Ihrer App tracken.

Auf dieser Seite finden Sie diese Statistiken:

- Ergebnisse der KPI-Formel
- Anzahl an Produktkäufen
- Umsatzerlöse für verschiedene Segmente
- Produktspezifischer Umsatz
- Stundenumsatz
- Stündliche Einnahmen für verschiedene Segmente
- Umsatz pro Nutzer:innen

{% endtab %}
{% tab Global Control Group Report %}
**Bericht zur globalen Kontrollgruppe**

Nachdem Sie eine [globale Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) eingerichtet haben, verwenden Sie den [globalen Kontrollbericht]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/), um die Auswirkungen Ihres gesamten Marketings von Braze zu bewerten. Mit diesem Bericht können Sie das Verhalten von Nutzern:innen, die Nachrichten erhalten, mit dem Verhalten von Nutzern:innen, die keine Nachrichten erhalten, vergleichen. So können Sie besser verstehen, wie Ihre Kampagnen und Canvase zu Ihren Geschäftszielen beitragen.

Sehen Sie sich diese Seite an:

- Messen Sie auf einfache Weise die Wirkung und den inkrementellen Uplift von Kampagnen und Canvase auf Sitzungen und angepasste Events.
- Schließen Sie Mitglieder der Kontrollgruppe automatisch nach dem Zufallsprinzip vom Nachrichtenempfang aus.
- Exportieren Sie die Mitglieder der Kontrollgruppe für weitere Analysen.

Weitere Fragen, die Sie mit dem Bericht beantworten können:

- Wie hat sich das Versenden von Messaging-Nachrichten insgesamt auf das Kundenverhalten ausgewirkt?
- Wie hoch ist der ROI von Braze als Plattform (für Erneuerungen oder Diskussionen mit Interessengruppen)?

{% endtab %}
{% endtabs %}

## Welche Kampagnen sollte ich als nächstes durchführen?

{% tabs local %}
{% tab Funnel Report %}

Verwenden Sie Funnel-Berichte für [Kampagnen]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) oder [Canvase]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/), um die Wege zu analysieren, die Ihre Kund:in nach Erhalt einer Kampagne zurücklegen. Sie können auswählen, welche nativen oder angepassten Events in jede Funnel-Analyse einbezogen werden sollen, und dann untersuchen, wie jede Variante im Vergleich zu ihrem ausgewählten Konversionstrichter performt.

Das können Sie mit diesem Bericht tun:

- Verstehen Sie, an welcher Stelle des Konversionstrichters Nutzer:innen abgebrochen sind, und identifizieren Sie Opportunitäten für erneute Interaktionen mit Nachrichten.
- Zeigen Sie Konversionen zu Events an, die bei der Einrichtung der Kampagne ursprünglich nicht als Konversions-Event vorgesehen waren.
- Analysieren Sie den Funnel anhand einer Reihe von Aktionen (z. B. "Wie viel Prozent der Kund:in haben eine E-Mail erhalten, eine Sitzung begonnen, einen Artikel in den Warenkorb gelegt und dann gekauft?").

Weitere Fragen, die Sie mit diesem Bericht beantworten können:

- Wo auf dem Konversionspfad erfolgt die Kundenabwanderung?
- Wie kann ich meine Marketing Strategien verbessern?

{% endtab %}
{% tab Predictive Churn %}
**Voraussichtliche Abwanderung**

[Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) ist das erste Modell in der [Braze Predictive Suite]({{site.baseurl}}/user_guide/brazeai/). Mit Abwanderungsprognosen können Sie die weitere Abwanderung proaktiv verringern.

Da jedes Unternehmen Abwanderung und Bindung anders definiert, können Sie Ihre Definitionen einfach in Predictive Churn eingeben, und Braze erledigt den Rest. Sie können auch Kampagnen oder Canvase erstellen, um auf die Prognosen zu reagieren oder Segmente für weitere Analysen zu bilden.

Weitere Fragen, die Sie mit diesem Feature beantworten können:

- Wie viele meiner idealen Nutzer:innen sind von Abwanderung bedroht?
- Welche Verhaltensweisen oder Attribute haben meine Nutzer:innen mit hohem Risiko gemeinsam?

{% endtab %}
{% tab Report Builder %}
**Berichts-Builder**

Verwenden Sie den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), um die Ergebnisse mehrerer Kampagnen oder Canvase in einer einzigen Ansicht zu vergleichen und schnell festzustellen, welche Engagement-Strategien sich am stärksten auf Ihre wichtigsten Metriken ausgewirkt haben.

Sehen Sie sich diese Seite an:

- Erstellen Sie einen Bericht über Kampagnen und Canvase der letzten Woche oder des letzten Monats, berechnen Sie wichtige Metriken und teilen Sie diese mit Ihren Teamkollegen.
- Vergleichen Sie die Performance verschiedener Varianten sowohl für multivariate Tests als auch für Canvase.
- Ermitteln Sie, welcher Messaging-Kanal die meiste Konversion oder das meiste Engagement für eine bestimmte Kampagne oder einen Canvas erzielt hat.
- Verfolgen Sie allgemeine Performance-Trends einer Gruppe von Kampagnen oder Canvase (z.B. alle Nachrichten, die mit einem Tag "Newsletter" verbunden sind).

Weitere Fragen, die Sie mit diesem Feature beantworten können:

- Wie war die Performance der ersten Version meiner Willkommens-E-Mail im Vergleich zur zweiten Version?
- Wie hoch waren meine durchschnittlichen Öffnungsraten bei Push in diesem Monat im Vergleich zum letzten Monat für einen bestimmten Tag?
- Welcher Newsletter des Monats hatte die meisten Konversionen?

{% endtab %}
{% endtabs %}

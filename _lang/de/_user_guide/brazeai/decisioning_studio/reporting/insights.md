---
nav_title: Insights
article_title: Insights-Bericht
page_order: 2
description: "Erfahren Sie, wie Sie den Insights-Bericht verwenden, um zu verstehen, wie Empfehlungsoptionen in Ihrer Aktionsbank in BrazeAI Decisioning Studio generiert werden."
---

# Insights-Bericht

> Insights zeigen Ihnen, wie die verschiedenen Empfehlungsoptionen in Ihrer Aktionsbank generiert werden, z. B. die Blockauswahl. Es gibt zwei verschiedene Insights-Berichte: **Agent-Präferenzen** und **SHAPs**.

{% tabs local %}
{% tab agent preferences %}
Der Bericht **Agent-Präferenzen** hilft Ihnen, saisonale Trends zu erkennen und die Relevanz der Auswahlmöglichkeiten in der Aktionsbank zu bewerten, um fundierte Entscheidungen für Updates zu treffen.

![Bericht zu Agent-Präferenzen mit einem Balkendiagramm, das vergleicht, wie oft verschiedene Empfehlungsoptionen über einen bestimmten Zeitraum ausgewählt wurden. Das Diagramm zeigt mehrere farbige Balken, die jeweils eine Empfehlungsoption aus der Aktionsbank darstellen, wobei die y-Achse den prozentualen Anteil der Auswahl und die x-Achse die Optionsnamen anzeigt.]({% image_buster /assets/img/decisioning_studio/reporting_insights_agent_preferences.png %})

In der folgenden Tabelle finden Sie weitere Details zu diesem Bericht:

| Feld | Beschreibung |
|-------|-------------|
| Dimension | Das Attribut, das zur Organisation der Ergebnisse verwendet wird, z. B. Kanal, Kampagne oder Plattform. |
| Vergleichsgruppe | Die Gruppen, die Sie in Ihrem Bericht vergleichen möchten. Sie können mehrere Vergleichsgruppen auswählen. |
| Parameter | Die Metrik, die auf dieses Attribut angewendet wird, z. B. Öffnungen, Klicks oder Konversionsrate. |
| Segment | Das [Zielgruppen-Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/), das Sie in Braze erstellt haben. |
| Option             | Die spezifische Empfehlungsoption, die aus der Aktionsbank ausgewählt wurde. |
| Beschreibung        | Eine kurze Erklärung dessen, was die Option darstellt.            |
| Anzahl der Auswahlen  | Die Gesamtanzahl, wie oft die Option ausgewählt wurde.         |
| % der Auswahlen   | Der prozentuale Anteil aller Auswahlen, bei denen diese Option gewählt wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab SHAPs %}
Der **SHAPs**-Bericht verwendet das Shapley Additive exPlanations (SHAP)-Modell, um Ihnen zu helfen, den Beitrag jedes Features oder jeder Variable zu Ihrem Empfehlungsagenten zu quantifizieren. Jeder Punkt im Chart repräsentiert einen SHAP-Wert, und die Verteilung der Punkte vermittelt einen allgemeinen Eindruck von der Richtungswirkung eines Features.

![SHAPs-Bericht-Chart mit einem horizontalen Balkendiagramm mit mehreren farbigen Balken, die verschiedene Features oder Variablen darstellen. Jeder Balken zeigt den Einfluss eines Features auf den Empfehlungsagenten, wobei die x-Achse den SHAP-Wert und die y-Achse Feature-Namen wie Recency, Frequency und Channel anzeigt. Das Chart visualisiert, wie jedes Feature positiv oder negativ zu den Prognosen des Agenten beiträgt.]({% image_buster /assets/img/decisioning_studio/reporting_insights_shaps.png %})

{% endtab %}
{% endtabs %}
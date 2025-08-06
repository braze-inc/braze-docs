---
nav_title: Eppo
article_title: Eppo
description: "Erfahren Sie, wie Sie Eppo in Braze integrieren können."
alias: /partners/eppo/
page_type: partner
search_tag: Partner
---

# Eppo

> [Eppo](https://www.geteppo.com/) ist eine Experimentierplattform der nächsten Generation, die es Teams ermöglicht, A/B-Tests durchzuführen, Features in großem Umfang zu verwalten und KI-gestützte Insights für datengestützte Entscheidungen zu nutzen.

*Diese Integration wird von Eppo verwaltet.*

Die Integration von Braze und Eppo erlaubt es Ihnen, A/B-Tests in Braze einzurichten und die Ergebnisse in Eppo zu analysieren, um Insights zu gewinnen und die Performance der Nachrichten mit langfristigen Metriken wie Umsatz oder Bindung zu verknüpfen.

## Voraussetzungen

| Anforderung                        | Beschreibung                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------|
| Eppo-Konto                       | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Eppo-Konto.                   |
| Currents oder Snowflake Daten gemeinsam nutzen | Currents oder Snowflake Data Sharing ist erforderlich, damit Eppo die Daten der Experimente analysieren kann. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Konfigurieren Sie Currents oder Snowflake Data Sharing in Braze

Eppo analysiert Experimente direkt in Ihrem Data Warehouse. Um die Integration zu ermöglichen, müssen die Daten zum Messaging Engagement von Braze in dem mit Eppo verbundenen Warehouse verfügbar sein. Mit Currents können Sie Kampagnendaten aus Braze exportieren oder mit [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) auf Braze-Daten in Ihrer Snowflake-Instanz zugreifen.

### Schritt 2: Richten Sie Ihr Experiment in einer Braze-Kampagne oder einem Canvas ein

Sie können in Ihren Kampagnen und Canvase native Features für A/B-Tests verwenden. Mehr dazu erfahren Sie unter [Multivariate und A/B-Tests](https://www.braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing#what-are-multivariate-and-ab-testing).

### Schritt 3: Eppo für die Messung von Braze-Experimenten einrichten

Um Experimente mit Braze-Daten in Eppo durchzuführen, erstellen Sie [Zuweisungstabellen](https://docs.geteppo.com/data-management/definitions/assignment-sql/) in Ihrem Warehouse auf der Grundlage der aus Braze exportierten Nachrichten-Ereignisdaten auf Nutzerebene. Für Canvas- und Kampagnen-Experimente werden getrennte Tabellen empfohlen, da sie auf unterschiedlichen Metadaten beruhen.

{% tabs local %}
{% tab Canvas-Experimente %}
Für Canvas-Experimente können Zuweisungen entweder erstellt werden:

- Auf der Einstiegsebene von Canvas (`users.canvas.Entry`)
- Oder in einem Canvas-Experiment-Schritt (`users.canvas.experimentstep.SplitEntry`)

In diesen Fällen werden Felder wie `canvas_name`, `experiment_step_id`, `canvas_variation_name` und `experiment_split_id` verwendet, um den Namen und die Variation des Experiments zu definieren.

{% endtab %}

{% tab Kampagnen-Experimente %}
Bei Kampagnen-Experimenten verwenden Sie Sendeereignisse (wie Push, E-Mail, SMS), um festzustellen, wann ein Nutzer:innen das Experiment betreten hat. `campaign_name` `message_variation_name` und `time` werden verwendet, um die Zuordnungstabelle aufzufüllen.

{% endtab %}
{% endtabs %}

Um nachrichten-spezifische Metriken (wie Klicks oder Öffnungen) zu verfolgen, fügen Sie eine **sekundäre Entität** ein, indem Sie eine `combined_id` erstellen, die die Nutzer:innen-ID mit dem Namen der Kampagne oder des Canvas verbindet. Diese `combined_id` wird auch in Ihren Faktentabellen verwendet, um die Metriken mit dem richtigen Experiment und der richtigen Variation abzugleichen.

Eppo verwendet diese Zuweisungen und Faktentabellen, um die Ergebnisse zu analysieren, und es wird empfohlen, ein **Protokoll** in Eppo einzurichten, um die Einrichtung zukünftiger Experimente zu standardisieren. Weitere Informationen finden Sie in der [Dokumentation von Eppo](https://docs.geteppo.com/guides/marketing/integrating-with-braze/).

## Support

Wenn Sie Fragen zur Einrichtung von Braze-Currents, Snowflake Data Sharing oder zur Konfiguration von multivariaten Kampagnen haben, wenden Sie sich bitte an Ihren Braze Customer-Success-Manager:in.

Wenn Sie Hilfe bei der Konfiguration von Eppo zur Messung von Braze-Experimenten benötigen, wenden Sie sich an das Eppo Support Team.

---
nav_title: Sisu Data
article_title: Sisu Data
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Sisu Data, einem führenden Anbieter von Cloud Decision Intelligence, die es Ihnen erlaubt, über alle Kampagnen hinweg oder auf Kampagnenebene zu verstehen, warum sich Metriken ändern und was die besten Ergebnisse liefert."
alias: /partners/sisu_data
page_type: partner
search_tag: Partner
---

# Sisu Data

> [Sisu Data](https://sisudata.com/) ist der führende Anbieter von Cloud Decision Intelligence, der maschinelles Lernen einsetzt, um die Performance von Metriken automatisch zu zerlegen und schnelle, umfassende und umsetzbare Insights zu liefern.

Die Integration von Sisu Data und Braze lässt Sie über alle Kampagnen hinweg oder auf Kampagnenebene verstehen, warum sich Metriken (z. B. Öffnungsrate, Click-through-Rate, Konversionsrate usw.) ändern und was die optimalen Ergebnisse antreibt. Nachdem diese Segmente identifiziert wurden, können Nutzer:innen von Braze die Ergebnisse in ihrem Data Warehouse materialisieren oder sie direkt von Sisu an Braze senden, um Nutzer:innen zu retarchen und zu erneuern.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sisu-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Sisu-Konto](https://sisudata.com/). |
| Cloud Lagerhaus | Diese Integration setzt voraus, dass Ihre Braze Daten in einem Cloud Warehouse (z.B. Snowflake, BigQuery) gespeichert sind. Um diesen Integrationsprozess zu rationalisieren, empfehlen wir die Nutzung der nativen Funktionen von Braze über [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Bereiten Sie einen Datensatz vor

Der Datensatz sollte den KPI angeben, den Sie mit Sisu analysieren möchten. Wenn Sie zum Beispiel besser verstehen möchten, warum die Konversionsraten im Wochenvergleich gesunken sind, sollte der Reichweitendatensatz eine wöchentliche Konversion darstellen. Die Spalten im Datensatz sollten mögliche Gründe für einen Rückgang der Konversionsrate darstellen.

### Schritt 2: Erstellen Sie eine Metrik  

Sobald der Datensatz vorbereitet ist, müssen Sie eine Metrik erstellen, die auf eine aggregierte Spalte referenziert. Da ein Datensatz mehrere Metriken liefern kann, kann der Nutzer:innen auch eine Reihe von Dimensionen kuratieren, die standardmäßig in allen Analysen enthalten sein sollen oder nicht. Beachten Sie, dass Nutzer:innen auch weiterhin auf der Analyseebene kuratieren können.

![]({% image_buster /assets/img/sisudata/metric_creation.png %})

### Schritt 3: Eine Analyse erstellen  

Es gibt verschiedene Analysen, die Nutzer:innen in Sisu erstellen können, je nach Anwendungsfall. Eine der gebräuchlichsten Analysen ist die Analyse des Zeitraums, um zu verstehen, welche Segmente sich am stärksten verändert haben. Nutzer:innen können entscheiden, ob sie tägliche, wöchentliche, monatliche oder angepasste Zeiträume analysieren möchten, indem sie die entsprechenden Zeiträume auswählen.

So kann der Nutzer:innen beispielsweise eine Analyse der Konversionsrate im Monatsvergleich für eine bestimmte Anzeigengruppe und einen bestimmten Engagement-Kanal erstellen und die wichtigsten positiven und negativen Faktoren verstehen.

{% tabs %}
{% tab Top positive Treiber %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Die wichtigsten negativen Faktoren %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

Von hier aus können Sie sich auf Kohorten konzentrieren, in denen sie sich engagieren möchten, oder Kampagnen ändern. Instanz hat Sisu automatisch festgestellt, dass Push-Benachrichtigungen, die dienstags verschickt werden, und E-Mails, die in großen Mengen verschickt werden, die Konversionsrate stark beeinträchtigen.

![]({% image_buster /assets/img/sisudata/segment.png %})

### Schritt 4: Schreiben Sie die Ergebnisse in das Data Warehouse zurück

Nutzer:innen können die Ergebnisse aus Sisu über [Sisu's API](https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults) extrahieren und die Segmente in einem Data Warehouse materialisieren. Snowflake-Kunden können diese Segmente in Braze über [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/) aktivieren.

Für andere Data Warehouses können Nutzer:innen eine bestehende Lösung zur Aktivierung nutzen oder sich an Sisu wenden, um zusätzliche Hilfe zu erhalten.

## Support

Wenn Sie Fragen zu dieser Integration haben, wenden Sie sich an Sisu unter partners@sisudata.com.


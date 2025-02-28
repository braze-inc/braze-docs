---
nav_title: Sisu Data
article_title: Sisu Data
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Sisu Data, einem führenden Anbieter von Cloud Decision Intelligence, die es Ihnen ermöglicht, kampagnenübergreifend oder auf Kampagnenebene zu verstehen, warum sich die Metriken ändern und was die besten Ergebnisse liefert."
alias: /partners/sisudata
page_type: partner
search_tag: Partner
---

# Sisu Data

> [Sisu Data][2] ist der führende Anbieter von Cloud-Entscheidungsintelligenz, der maschinelles Lernen einsetzt, um die Leistung von Metriken automatisch zu zerlegen und schnelle, umfassende und umsetzbare Erkenntnisse zu liefern.

Die Integration von Sisu Data und Braze ermöglicht es Ihnen, über alle Kampagnen hinweg oder auf Kampagnenebene zu verstehen, warum sich die Metriken (z.B. Öffnungsrate, Klickrate, Konversionsrate usw.) ändern und was die besten Ergebnisse liefert. Nachdem diese Segmente identifiziert wurden, können Braze-Benutzer die Ergebnisse in ihrem Data Warehouse materialisieren oder sie direkt von Sisu an Braze senden, um die Benutzer erneut anzusprechen und zu binden.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sisu-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Sisu-Konto][3]. |
| Cloud Lagerhaus | Diese Integration setzt voraus, dass Ihre Braze-Daten in einem Cloud-Warehouse (z. B. Snowflake, BigQuery) gespeichert sind. Um diesen Integrationsprozess zu vereinfachen, empfehlen wir die Nutzung der nativen Funktionen von Braze über [Currents][4]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Bereiten Sie einen Datensatz vor

Der Datensatz sollte den KPI angeben, den Sie mit Sisu analysieren möchten. Wenn Sie zum Beispiel besser verstehen möchten, warum die Konversionsraten im Wochenvergleich gesunken sind, sollte der Reichweitendatensatz eine wöchentliche Konversion darstellen. Die Spalten im Datensatz sollten potenzielle Gründe für einen möglichen Rückgang der Konversionsrate darstellen.

### Schritt 2: Eine Metrik erstellen  

Sobald der Datensatz vorbereitet ist, müssen Sie eine Metrik erstellen, die auf eine aggregierte Spalte verweist. Da ein Datensatz mehrere Metriken liefern kann, kann der Benutzer auch eine Reihe von Dimensionen festlegen, die standardmäßig in allen Analysen enthalten sein sollen oder nicht. Beachten Sie, dass die Benutzer weiterhin auf der Analyseebene kuratieren können.

![][6]

### Schritt 3: Eine Analyse erstellen  

Es gibt verschiedene Analysen, die Benutzer in Sisu erstellen können, je nach Anwendungsfall. Eine der gebräuchlichsten Analysen ist eine Analyse im Zeitvergleich, um zu verstehen, welche Segmente sich am stärksten verändert haben. Sie können entscheiden, ob Sie tägliche, wöchentliche, monatliche oder benutzerdefinierte Zeiträume analysieren möchten, indem Sie die entsprechenden Zeiträume auswählen.

So kann der Benutzer beispielsweise eine Analyse der Konversionsrate im Monatsvergleich für eine bestimmte Anzeigengruppe und einen bestimmten Engagement-Kanal erstellen und die wichtigsten positiven und negativen Faktoren verstehen.

{% tabs %}
{% tab Top positive Treiber %}

![]({% image_buster /assets/img/sisudata/kda_result_positive.png %})

{% endtab %}
{% tab Die wichtigsten negativen Faktoren %}

![]({% image_buster /assets/img/sisudata/kda_result_negative.png %})

{% endtab %}
{% endtabs %}

Von hier aus können Sie sich auf die Kohorten konzentrieren, an denen sie sich beteiligen möchten, oder Kampagnen ändern. So hat Sisu beispielsweise automatisch festgestellt, dass Push-Benachrichtigungen, die dienstags verschickt werden, und E-Mails, die in großen Mengen verschickt werden, die Konversionsrate stark beeinträchtigen.

![][9]

### Schritt 4: Schreiben Sie die Ergebnisse zurück in das Data Warehouse

Benutzer können die Ergebnisse von Sisu mit [Sisus API][10] ] extrahieren und die Segmente in einem Data Warehouse materialisieren. Snowflake-Kunden können diese Segmente in Braze über [Cloud Data Ingestion][5] aktivieren.

Für andere Data Warehouses können die Benutzer eine bestehende Aktivierungslösung nutzen oder sich an Sisu wenden, um zusätzliche Hilfe zu erhalten.

## Unterstützen Sie

Wenn Sie Fragen zu dieser Integration haben, wenden Sie sich an Sisu unter partners@sisudata.com.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://sisudata.com/
[3]: https://sisudata.com/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/
[6]: {% image_buster /assets/img/sisudata/metric_creation.png %}
[9]: {% image_buster /assets/img/sisudata/segment.png %}
[10]: https://docs.sisudata.com/docs/api/#tag/AnalysesService/operation/AnalysesService_AnalysisRunResults

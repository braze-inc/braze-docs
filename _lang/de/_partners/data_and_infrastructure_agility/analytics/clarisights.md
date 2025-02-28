---
nav_title: Clarisights
article_title: Clarisights
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Clarisights, einer Self-Service-Plattform für Performance-Marketing-Reporting, die es Ihnen ermöglicht, Daten aus Braze-Kampagnen und Canvases zu importieren, um eine einheitliche Reporting-Schnittstelle für Performance- und CRM/Retention-Marketing zu schaffen."
alias: /partners/Clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights][2] ist eine Self-Service-Plattform für Performance-Marketing-Berichte für datengesteuerte Unternehmen. Es integriert, verarbeitet und visualisiert automatisch alle Ihre Daten aus Marketing-, Analyse- und Attributionsquellen.

Die Integration von Braze und Clarisights ermöglicht es Ihnen, Daten aus Braze-Kampagnen und Canvases zu importieren, um eine einheitliche Berichtsschnittstelle für Performance- und CRM/Retention-Marketing zu erhalten.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Clarisights-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein Clarisights-Arbeitsbereich erforderlich. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Name des Lötarbeitsplatzes | Der Name des Arbeitsbereichs, der mit dem Braze-API-Schlüssel verknüpft ist. Dieser Name wird verwendet, um die Arbeitsbereich-Integration in Clarisights zu identifizieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Integration von Braze und Clarisights können Benutzer verschiedene Visualisierungen und Tabellen erstellen, um Erkenntnisse aus den von ihnen erstellten Kampagnen zu gewinnen. Beliebte Anwendungsfälle sind unter anderem:

{% tabs %}
{% tab Bessere Sichtbarkeit %}
Bessere Übersicht über die Gesamtleistung von Kampagnen und Canvases.

![Eine Grafik mit einem Beispiel für eine bessere Lebensfähigkeit in der Clarisights-Plattform. Diese Grafik enthält Statistiken für Kampagnen- und Canvas-Öffnungen, Klicks, Sendungen, Konversionen usw.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Detaillierte Berichterstattung %}
Detaillierte Berichte für Kampagnen und Canvases.

![Eine Grafik mit granularen Berichten, wie z.B. "Insgesamt gesendet nach Sendekanal" und "Konversionsrate".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Einheitliche Dashboards %}
Einheitliche Dashboards für CMOs und CXOs.

![Eine Grafik mit einem Beispiel für vereinheitlichte Dashboards.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integration

Um Braze-Daten mit Clarisights zu synchronisieren, müssen Sie einen Braze-Connector erstellen und Braze-Arbeitsbereiche verbinden.

1. Navigieren Sie in Clarisights zur Seite **Integrationen**, suchen Sie den **Braze-Anschluss** und wählen Sie **\+ Verbinden**.<br>![Eine Liste der verfügbaren Konnektoren aus dem Clarisights-Marktplatz für Integrationen.][6]<br><br>
2. Als nächstes verbinden Sie Ihr Clarisights-Konto über den Integrationsablauf mit Braze. Dazu müssen Sie Ihren Braze REST API-Schlüssel, den Namen des Braze-Arbeitsbereichs und den Braze REST-Endpunkt angeben.<br>![Braze Workspace Connector in der Clarisights-Plattform. Diese Seite enthält Felder für den Namen des Braze-Arbeitsbereichs, den Braze REST API-Schlüssel und den Braze REST-Endpunkt.][7]<br><br>Vor der erfolgreichen Integration sehen die Benutzer die verbundenen Arbeitsbereiche auf derselben Seite.<br>![Unter "Braze-Konten" finden Sie eine Liste der verbundenen Arbeitsbereiche.][9]<br><br>

## Mit dieser Integration

Um Braze als Datenquelle in Ihre Clarisights-Berichte aufzunehmen, navigieren Sie zu **Neuer Bericht erstellen**. Benennen Sie Ihren Bericht und wählen Sie in der daraufhin angezeigten Eingabeaufforderung **Braze** als Datenquelle aus. Sie können auch die Metriken und Dimensionen auswählen, die in den Bericht aufgenommen werden sollen. Wenn Sie fertig sind, wählen Sie **Bericht erstellen**. 

Die Daten aus Braze werden ab dem Zeitpunkt des nächsten geplanten Datenimports fließen. Wenden Sie sich an Ihren Clarisights-Kundenbetreuer, um die Auffüllung für längere Zeiträume zu beantragen. 

![Clarisight-Berichtseinstellungen mit Feldern für Name und Datenquelle. Für dieses Beispiel wird "Braze" als Datenquelle ausgewählt.][8]

Besuchen Sie Clarisights für weitere Informationen über verfügbare [Metriken und Dimensionen][10] oder die [Erstellung von Berichten][11].

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://clarisights.com
[3]: {{site.baseurl}}/assets/img/clarisights/overall_view.png
[4]: {{site.baseurl}}/assets/img/clarisights/unified_dashboard.png
[5]: {{site.baseurl}}/assets/img/clarisights/granular_reporting.png
[6]: {{site.baseurl}}/assets/img/clarisights/integrations.png
[7]: {{site.baseurl}}/assets/img/clarisights/braze_flow.png
[8]: {{site.baseurl}}/assets/img/clarisights/braze_report.png
[9]: {{site.baseurl}}/assets/img/clarisights/connected.png
[10]: https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions
[11]: https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights

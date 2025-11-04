---
nav_title: Clarisights
article_title: Clarisights
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Clarisights, einer Self-Service-Plattform für Performance-Marketing-Reporting, die es Ihnen erlaubt, Daten aus Kampagnen und Canvase von Braze zu importieren, um eine einheitliche Schnittstelle für Performance- und CRM/Retention-Marketing zu schaffen."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com) ist eine Self-Service-Plattform für Performance-Marketing-Berichte für datengestützte Unternehmen. Es integriert, verarbeitet und visualisiert automatisch alle Ihre Daten aus Marketing-, Analytics- und Attributionsquellen.

_Diese Integration wird von Clarisights gepflegt._

## Über die Integration

Die Integration von Braze und Clarisights lässt den Import von Daten aus Kampagnen und Canvase von Braze zu, um eine einheitliche Schnittstelle für die Berichterstattung über Performance- und CRM/Retention-Marketing zu schaffen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Clarisights-Konto | Ein Clarisights Workspace ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze Workspace Name | Der Name des Workspace, der mit dem Braze API-Schlüssel verknüpft ist. Dieser Name wird verwendet, um die Workspace Integration in Clarisights zu identifizieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Integration von Braze und Clarisights können Nutzer:innen verschiedene Visualisierungen und Tabellen erstellen, um Insights aus den von ihnen erstellten Kampagnen zu gewinnen. Beliebte Anwendungsfälle sind unter anderem:

{% tabs %}
{% tab Bessere Sichtbarkeit %}
Bessere Sichtbarkeit der gesamten Performance von Kampagnen und Canvase.

![Eine Grafik mit einem Beispiel für eine bessere Lebensfähigkeit in der Clarisights-Plattform. Diese Grafik enthält Statistiken über die Öffnungen von Kampagnen und Canvas, Klicks, gesendete Daten, Konversionen usw.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab Detaillierte Berichterstattung %}
Detaillierte Berichte für Kampagnen und Canvase.

![Eine Grafik mit granularen Berichten, wie z.B. "insgesamt gesendet nach Kanal" und "Konversionsrate".]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab Einheitliche Dashboards %}
Einheitliche Dashboards für CMOs und CXOs.

![Eine Grafik mit einem Beispiel für vereinheitlichte Dashboards.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## Integration

Um Braze-Daten mit Clarisights zu synchronisieren, müssen Sie einen Braze-Konnektor erstellen und Braze-Workspaces verbinden.

1. Navigieren Sie in Clarisights zur Seite **Integrationen**, suchen Sie den **Braze** Konnektor und wählen Sie **\+ Verbinden**.<br>![Eine Liste der verfügbaren Konnektoren aus dem Clarisights-Marktplatz für Integrationen.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. Als nächstes verbinden Sie Ihr Clarisights-Konto über den Integrationsablauf mit Braze. Dazu müssen Sie Ihren Braze REST API-Schlüssel, den Namen des Braze Workspace und den Braze REST-Endpunkt angeben.<br>![Konnektor für den Workspace von Braze in der Clarisights-Plattform. Diese Seite enthält Felder für den Namen des Braze Workspace, den REST API-Schlüssel von Braze und den REST-Endpunkt von Braze.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>Vor der erfolgreichen Integration sehen die Nutzer:innen die verbundenen Workspaces auf der gleichen Seite.<br>![Unter "Braze-Konten" finden Sie eine Liste der verbundenen Workspaces.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## Verwendung dieser Integration

Um Braze als Datenquelle in Ihre Clarisights-Berichte aufzunehmen, navigieren Sie zu **Neuer Bericht erstellen**. Benennen Sie Ihren Bericht und wählen Sie **Braze** als Datenquelle in der daraufhin angezeigten Aufforderung aus. Sie können auch die Metriken und Dimensionen auswählen, die in den Bericht aufgenommen werden sollen. Wenn Sie fertig sind, wählen Sie **Bericht erstellen**. 

Die Daten aus Braze werden ab dem Zeitpunkt des nächsten geplanten Datenimports fließen. Wenden Sie sich an Ihren Customer-Success-Manager von Clarisights, um Anfragen für längere Zeiträume zu stellen. 

![Clarisight-Berichtseinstellungen mit Feldern für Name und Datenquelle. In diesem Beispiel wird "Braze" als Datenquelle ausgewählt.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

Besuchen Sie Clarisights für weitere Informationen zu den verfügbaren [Metriken und Dimensionen](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) oder zur [Erstellung von Berichten](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights).



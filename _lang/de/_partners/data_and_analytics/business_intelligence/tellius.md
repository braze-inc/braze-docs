---
nav_title: Tellius
article_title: Tellius
alias: /partners/tellius/
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und Tellius, einer Plattform für Decision Intelligence und Augmented Analytics, die es Ihnen erlaubt, Daten zu nutzen, ohne auf BI-Ingenieure angewiesen zu sein, um Dashboards zu erstellen und Insights zu generieren, um bessere Marketing-Entscheidungen zu treffen."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), eine Plattform für Entscheidungsintelligenz und erweiterte Analytics, ermöglicht es Ihnen, Fragen zu Ihren Daten mit Hilfe der natürlichsprachlichen Suche zu beantworten und mit datengestützten Insights das "Warum" zu verstehen.

Die Integration von Braze und Tellius ermöglicht es Nutzern:innen, Daten zu nutzen, ohne auf BI-Ingenieure angewiesen zu sein, um Dashboards zu erstellen und Insights zu generieren, um bessere Marketing-Entscheidungen zu treffen. Diese Integration setzt voraus, dass Braze-Daten in Snowflake gespeichert sind. Tellius kann sich direkt mit Snowflake verbinden und Push-Abfragen mit der Integration im Live-Modus durchführen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tellius-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Tellius-Konto. Sie können Ihre Tellius Reise mit einer [kostenlosen Testversion](https://www.tellius.com/free-trial/) beginnen|
| Snowflake Datenaustauschprogramm | Wenn Sie bereits Snowflake-Kunden sind, wenden Sie sich an Ihre Braze-Vertretung, um sich über das Snowflake Data Sharing-Programm zu informieren, mit dem Sie Ihre Braze-Daten in Ihre Snowflake-Instanz übertragen können.|
| Snowflake Leser-Konto | Für Kunden, die keine Snowflake-Kunden sind, wenden Sie sich an Ihre Braze-Vertretung, um ein Snowflake Reader-Konto zu erhalten, das für Sie eingerichtet werden kann, damit Sie auf Ihre Daten bei Braze zugreifen können.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erhalten Sie Zugang zu Braze über Snowflake

Braze speichert granulare Kundendaten in Snowflake. Sie können Ihre Daten von Braze nutzen, um Insights über das Braze Snowflake Data Sharing-Programm zu generieren oder ein Snowflake-Lesekonto zu erhalten. 

Folgen Sie der [Snowflake Integration]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), um sich einzurichten. 

### Schritt 2: Verbinden Sie Tellius mit Braze-Daten in Snowflake

Verbinden Sie Tellius mit Braze-Daten in Snowflake mit einer der folgenden Methoden:

- Direkter Zugang: Um Daten in Tellius zu laden, folgen Sie den Schritten unter [Laden von Datensätzen](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- OAuth-Zugang: Für den OAuth-Zugriff auf Snowflake befolgen Sie die Schritte für die [OAuth-Authentifizierung](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Schritt 3: Business View in Tellius aus geladenen Daten erstellen

Um mit der natürlichsprachlichen Suche und automatisierten Insights zu beginnen, erstellen Sie eine [Geschäftsansicht](https://help.tellius.com/article/hy9yvh5tom-create-business-view) und wählen Datensätze aus Ihrer Snowflake-Verbindung aus.

### Schritt 4: Holen Sie den größten Nutzen aus Ihren Daten mit Tellius

In Tellius gibt es eine geführte Schnittstelle, die Sie durch die Features der Plattform führt. Weitere Fragen und Anleitungen finden Sie in der vollständigen [Wissensdatenbank](https://help.tellius.com/).
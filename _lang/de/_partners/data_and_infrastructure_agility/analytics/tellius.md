---
nav_title: Tellius
article_title: Tellius
alias: /partners/Tellius/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tellius, einer Plattform für Decision Intelligence und Augmented Analytics, die es Ihnen ermöglicht, Daten zu nutzen, ohne auf BI-Ingenieure angewiesen zu sein, um Dashboards zu erstellen und Erkenntnisse zu gewinnen, um bessere Marketingentscheidungen zu treffen."
page_type: partner
search_tag: Partner

---

# Tellius

> [Tellius](https://www.tellius.com/), eine Plattform für Entscheidungsintelligenz und erweiterte Analytik, ermöglicht es Ihnen, Fragen zu Ihren Daten mithilfe der natürlichsprachlichen Suche zu beantworten und mit KI-gesteuerten Einsichten tiefer zu gehen, um das "Warum" zu verstehen.

Die Integration von Braze und Tellius ermöglicht es Benutzern, Daten zu nutzen, ohne auf BI-Ingenieure angewiesen zu sein, um Dashboards zu erstellen und Erkenntnisse zu gewinnen, um bessere Marketingentscheidungen zu treffen. Diese Integration setzt voraus, dass Braze-Daten in Snowflake gespeichert sind, wo Tellius eine direkte Verbindung herstellen und Abfragen im Live-Modus durchführen kann.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Tellius-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Tellius-Konto. Sie können Ihre Tellius Reise mit einer [kostenlosen Testversion](https://www.tellius.com/free-trial/) beginnen|
| Snowflake Datenaustauschprogramm | Wenn Sie bereits Snowflake-Kunde sind, wenden Sie sich an Ihren Braze-Vertreter, um sich über das Snowflake Data Sharing-Programm zu informieren, mit dem Sie Ihre Braze-Daten in Ihre Snowflake-Instanz einspeisen können.|
| Snowflake Reader Konto | Wenn Sie kein Snowflake-Kunde sind, wenden Sie sich an Ihren Braze-Vertreter, um ein Snowflake Reader-Konto einzurichten, mit dem Sie auf Ihre Braze-Daten zugreifen können.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erhalten Sie Zugang zu Braze über Snowflake

Braze speichert granulare Kundendaten in Snowflake. Sie können Ihre Braze-Daten nutzen, um über das Braze Snowflake Data Sharing-Programm oder ein Snowflake-Leserkonto Erkenntnisse zu gewinnen. 

Folgen Sie der [Snowflake-Integration]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), um sich einzurichten. 

### Schritt 2: Verbinden Sie Tellius mit Braze-Daten in Snowflake

Verbinden Sie Tellius mit Braze-Daten in Snowflake mit einer der folgenden Methoden:

- Direkter Zugang: Um Daten in Tellius zu laden, folgen Sie den Schritten unter [Laden von Datensätzen](https://help.tellius.com/article/jn6o59d5gk-load-datasets).
- OAuth-Zugang: Für den OAuth-Zugriff auf Snowflake folgen Sie den Schritten für die [OAuth-Authentifizierung](https://help.tellius.com/article/11517w63b6-oauth-authentication-for-snowflake).

### Schritt 3: Business View in Tellius aus geladenen Daten erstellen

Um mit der natürlichsprachlichen Suche und automatisierten Einblicken zu beginnen, erstellen Sie eine [Geschäftsansicht](https://help.tellius.com/article/hy9yvh5tom-create-business-view) und wählen Datensätze aus Ihrer Snowflake-Verbindung aus.

### Schritt 4: Holen Sie mit Tellius den größten Nutzen aus Ihren Daten

In Tellius gibt es eine geführte Schnittstelle, die Sie durch die Funktionen der Plattform führt. Weitere Fragen und Anleitungen finden Sie in der vollständigen [Wissensdatenbank](https://help.tellius.com/).
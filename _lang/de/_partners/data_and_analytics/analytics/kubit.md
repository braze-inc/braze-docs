---
nav_title: Kubit
article_title: Kubit
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Kubit, einer no-code, self-service Analytics-Plattform, die sofortige Insights in Produkte liefert und es Ihnen erlaubt, Kohorten von Kubit-Benutzern zu importieren und sie im Messaging von Braze anzusprechen."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) ist eine No-Code, Self-Service Analytics-Plattform, die sofortige Insights in Produkte zustellt. 

Die Integration von Braze und Kubit erlaubt es Ihnen, [Nutzer:innen von Kubit zu importieren]({{site.baseurl}}/partners/data_and_analytics/cohort_import/kubit/) und sie im Messaging von Braze zu targetieren. Darüber hinaus können Sie durch den Einsatz von [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) die Rohdaten der Kampagnen und Impressionen von Braze in die Analytics von Kubit integrieren, um die Wirkung dieser Kampagnen in Echtzeit zu messen. Dieser Ansatz bietet Insights über den gesamten Lebenszyklus Ihrer Nutzer:innen, ohne dass Sie dafür einen technischen Aufwand betreiben müssen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Kubit Unternehmenskonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Kubit Unternehmenskonto. |
| Übereinstimmende Nutzer:innen IDs | Ihre Kundendaten in Kubit und Braze müssen übereinstimmende Nutzer:innen-IDs auf den beiden Plattformen haben. Dazu gehören auch anonyme UUIDs. Besuchen Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=android), um zu erfahren, wie Braze Nutzer:innen IDs festlegt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Analysieren von Braze Daten in Kubit

Nutzen Sie die Vorteile des [sicheren Datenaustauschs mit Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/), um Ihre Braze-Rohdaten zu Kampagnen und Impressionen mit Kubit auszutauschen und sie in die Self-Service Analytics von Kubit einzubinden, damit Sie ein vollständiges Bild des Nutzer:innen-Lebenszyklus erhalten.

Zum Referenzieren finden Sie hier alle [Felder von Braze]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2), die in Kubit Analytics integriert werden können. Die Details dieses Schrittes sind sehr kundenspezifisch und erfordern spezielle Konfigurationen. Sprechen Sie mit Ihrem Kubit Account Manager oder [support@kubit.ai](support@kubit.ai), um mehr zu erfahren.
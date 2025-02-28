---
nav_title: Kubit
article_title: Kubit
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Kubit, einer no-code, self-service Analyseplattform, die sofortige Produkteinblicke liefert und es Ihnen ermöglicht, Kubit-Benutzerkohorten zu importieren und sie im Braze Messaging anzusprechen."
alias: /partners/kubit/
page_type: partner
search_tag: Partner

---

# Kubit

> [Kubit](https://kubit.ai/) ist eine Selbstbedienungs-Analyseplattform ohne Code, die sofortige Produkteinblicke liefert. 

Die Integration von Braze und Kubit ermöglicht es Ihnen, [Kubit-Benutzerkohorten zu importieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/kubit/) und sie im Braze-Messaging anzusprechen. Darüber hinaus können Sie durch den Einsatz von [Snowflake Secure Data Sharing]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/) die Rohdaten der Kampagnen und Impressionen von Braze in die Kubit Produktanalyse integrieren, um die Wirkung dieser Kampagnen in Echtzeit zu messen. Dieser Ansatz bietet Einblicke in den gesamten Lebenszyklus Ihrer Benutzer, ohne dass Sie dafür einen technischen Aufwand betreiben müssen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Kubit Unternehmenskonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Kubit Unternehmenskonto. |
| Übereinstimmende Benutzer-IDs | Ihre Kundendaten in Kubit und Braze müssen in beiden Plattformen übereinstimmende Benutzer-IDs haben. Dazu gehören auch anonyme UUIDs. Besuchen Sie unsere [Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/), um zu erfahren, wie Braze Benutzer-IDs festlegt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Analysieren von Braze-Daten in Kubit

Nutzen Sie die Vorteile des [sicheren Datenaustauschs mit Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/), um Ihre Braze-Rohdaten zu Kampagnen und Impressionen mit Kubit auszutauschen und sie in die Self-Service-Analysen von Kubit einzubinden, so dass Sie ein vollständiges Bild vom Lebenszyklus der Nutzer erhalten.

Als Referenz finden Sie hier alle [Braze-Felder]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ed79384e6ac6a97fe3b3d9f76852b7c2), die in Kubit-Analysen integriert werden können. Die Details dieses Schrittes sind sehr kundenspezifisch und erfordern spezielle Konfigurationen. Sprechen Sie mit Ihrem Kubit-Kundenbetreuer oder mit [support@kubit.ai](support@kubit.ai), um mehr zu erfahren.
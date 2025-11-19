---
nav_title: Kontobasierte Segmentierung
article_title: Einrichten der kontobasierten Segmentierung
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie die verschiedenen Features von Braze nutzen können, um Ihre Anwendungsfälle für die Segmentierung von B2B-Konten zu unterstützen."
---

# Einrichten einer kontobasierten Segmentierung

> Auf dieser Seite erfahren Sie, wie Sie verschiedene Features von Braze nutzen können, um Ihre Anwendungsfälle für die Segmentierung von B2B-Konten zu unterstützen.

Sie können die B2B-kontenbasierte Segmentierung auf zwei Arten durchführen, je nachdem, wie Sie Ihr [B2B-Datenmodell]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) eingerichtet haben:

- Wenn Sie [Kataloge für Ihre Geschäftsobjekte](#option-1-when-using-catalogs-for-your-business-objects) verwenden
- Wenn Sie [verbundene Quellen für Ihre Geschäftsobjekte](#option-2-when-using-connected-sources-for-your-business-objects) verwenden

## B2B-Segmentierung auf der Grundlage von Konten einrichten

### Option 1: Wenn Sie Kataloge für Ihre Geschäftsobjekte verwenden

#### Grundlegende SQL-Vorlagensegmentierung

Um Ihnen den Einstieg zu erleichtern, haben wir grundlegende SQL-Templates für eine einfache kontenbasierte Segmentierung erstellt.

Nehmen wir an, Sie möchten Nutzer:innen eines Targeting-Unternehmenskontos segmentieren. 

1. Gehen Sie zu **Zielgruppe** > **Segmenterweiterungen** > **Neue Erweiterung erstellen** > **Mit einer Vorlage beginnen** und wählen Sie die Vorlage **Katalogsegment für Ereignisse**. <br><br> !["Wählen Sie ein Template"-Modal mit Katalogsegmentierungsoptionen für Events oder Käufe.]({% image_buster /assets/img/b2b/select_a_template.png %})<br><br>Der SQL-Editor wird automatisch mit einer Vorlage gefüllt, die Benutzer-Event-Daten mit Katalogdaten verknüpft, um Nutzer:innen zu segmentieren, die sich mit bestimmten Katalogartikeln beschäftigen. <br><br>![Ein SQL-Editor für eine neue Erweiterung mit einem geöffneten Tab "Variablen".]({% image_buster /assets/img/b2b/enter_new_name.png %})<br><br>
2. Verwenden Sie die Registerkarte **Variablen**, um die erforderlichen Felder für Ihre Vorlage bereitzustellen, bevor Sie Ihr Segment erstellen.<br><br>Damit Braze Nutzer:innen auf der Grundlage ihres Engagements für Katalogartikel identifizieren kann, müssen Sie Folgendes tun:
- Wählen Sie einen Katalog, der ein Katalogfeld enthält
- Wählen Sie ein angepasstes Event aus, das eine Event-Eigenschaft enthält
- Stimmen Sie die Werte Ihrer Katalogfelder und Ereigniseigenschaften ab

##### Leitlinien für Variablen für B2B-Anwendungsfälle

Wählen Sie die folgenden Variablen für einen Anwendungsfall der kontobasierten Segmentierung im B2B-Bereich aus:

| Variabel | Eigenschaft |
| --- | --- |
| Katalog | Konto-Katalog |
| Katalogfeld | ID |
| Angepasstes Event | account_linked |
| Angepasste Event-Eigenschaft | account_id |
| (Unter SQL-Ergebnisse filtern) Katalogfeld | Klassifizierung |
| (unter SQL-Ergebnisse filtern) Wert | Unternehmen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Ausgefeilte SQL-Segmentierung

Für eine ausgefeiltere oder komplexere Segmentierung lesen Sie bitte die [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). Um Ihnen den Einstieg zu erleichtern, finden Sie hier einige SQL-Templates, die Ihnen den Einstieg in die B2B-Kontosegmentierung erleichtern:

1. Erstellen Sie ein Segment, das zwei Filter in einem einzigen Katalog vergleicht (z.B. Nutzer:innen, die in der Gastronomie arbeiten, für ein Unternehmenskonto). Sie müssen die Katalog-ID und die ID des Artikels angeben.

```sql
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_accounts.Classification = 'Enterprise'
; 
```

{: start="2"}
2\. Erstellen Sie ein Segment, das zwei Filter in zwei separaten Katalogen vergleicht (z. B. Nutzer:innen, die mit Unternehmenszielkonten verknüpft sind, die eine offene „Phase 3“-Opportunity haben).

```sql
-- Reformat catalog data into a table with columns for each field
WITH salesforce_accounts AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Industry' THEN FIELD_VALUE END) AS Industry,
       MAX(CASE WHEN FIELD_NAME = 'Classification' THEN FIELD_VALUE END) AS Classification,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655ef5213ea0f00591816e2' -- salesforce_accounts
   GROUP BY ITEM_ID
),
salesforce_opportunities AS (
   SELECT
       ITEM_ID as id,
       MAX(CASE WHEN FIELD_NAME = 'Account_ID' THEN FIELD_VALUE END) AS Account_ID,
       MAX(CASE WHEN FIELD_NAME = 'Stage' THEN FIELD_VALUE END) AS Stage,
   FROM CATALOGS_ITEMS_SHARED
   WHERE CATALOG_ID = '6655f84a348f0f0059ad0627' -- salesforce_opportunities
   GROUP BY ITEM_ID
)
SELECT DISTINCT events.USER_ID
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED as events
JOIN salesforce_accounts
ON TRY_PARSE_JSON(events.properties):account_id::STRING = salesforce_accounts.id
JOIN salesforce_opportunities
ON salesforce_accounts.id = salesforce_opportunities.Account_ID
WHERE events.name = 'account_linked'
AND salesforce_accounts.Industry = 'Restaurants'
AND salesforce_opportunities.Stage = 'Closed Won'
;
```

### Option 2: Wenn Sie verbundene Quellen für Ihre Geschäftsobjekte verwenden

Die Grundlagen für die Verwendung verbundener Quellen bei der Segmentierung finden Sie unter [CDI Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/). Lassen Sie sich von den Vorlagen unter [Bei der Verwendung von Katalogen](#option-1-when-using-catalogs-for-your-business-objects) inspirieren, wie Sie die Quelltabellen formatieren, denn Sie können sie beliebig formatieren.

## Verwendung Ihrer kontobasierten Erweiterung in einem Segment

Nachdem Sie Ihre Segmentierung auf Kontoebene in den obigen Schritten erstellt haben, können Sie diese Segmenterweiterungen direkt in Ihre Targeting-Kriterien übernehmen. Es ist auch einfach, zusätzliche demografische Kriterien für Nutzer:innen hinzuzufügen, wie z.B. die Rolle, das Engagement bei früheren Kampagnen und mehr. Weitere Informationen finden Sie unter [Verwendung Ihrer Erweiterung in einem Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-6-use-your-extension-in-a-segment).


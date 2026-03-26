---
nav_title: Katalogdaten synchronisieren und löschen
article_title: Katalogdaten synchronisieren und löschen
page_order: 4
page_type: reference
description: "Auf dieser Seite finden Sie eine Übersicht darüber, wie Sie Katalogdaten synchronisieren können."

---

# Katalogdaten synchronisieren und löschen

> Diese Seite beschreibt, wie Sie Katalogdaten synchronisieren können.
 
## 1. Schritt: Einen neuen Katalog erstellen

Bevor Sie eine neue Cloud-Datenaufnahme-Integration (CDI) für [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/) erstellen, müssen Sie einen neuen Katalog erstellen oder einen vorhandenen Katalog identifizieren, den Sie für die Integration verwenden möchten. Es gibt mehrere Möglichkeiten, einen neuen Katalog zu erstellen. Sie alle eignen sich für die CDI-Integration:
- [CSV-Datei]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv) hochladen
- Erstellen Sie einen Katalog im [Braze-Dashboard]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) oder bei der CDI-Einrichtung.
- Erstellen Sie einen Katalog mithilfe des [Endpunkts „Katalog erstellen"]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Änderungen am Katalogschema (wie die Ergänzung neuer Felder oder Änderungen am Feldtyp) müssen stets über das Katalog-Dashboard vorgenommen werden, bevor die aktualisierten Daten über CDI synchronisiert werden. Wir empfehlen, diese Aktualisierungen vorzunehmen, wenn die Synchronisierung pausiert ist oder keine ansteht. So vermeiden Sie Konflikte zwischen den Daten aus Ihrem Data Warehouse und dem Schema in Braze.

## 2. Schritt: Integration von Cloud-Datenaufnahme mit Katalogdaten
Die Einrichtung einer Katalogsynchronisierung folgt weitgehend dem Prozess für [Nutzerdaten-CDI-Integrationen]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Richten Sie in Snowflake eine Quelltabelle ein. Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Richten Sie eine Rolle, ein Warehouse und einen Benutzer ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass Sie den Zugriff auf die Katalogquelltabelle erweitern.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Wenn Ihr Snowflake-Konto Netzwerkrichtlinien hat, setzen Sie die Braze-IPs auf die Allowlist, damit der CDI-Dienst eine Verbindung herstellen kann. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. Navigieren Sie im Braze-Dashboard zu **Technology Partners** > **Snowflake** und erstellen Sie eine neue Synchronisierung.
5. Geben Sie die Verbindungsdetails (oder vorhandene Zugangsdaten) und die Quelltabelle ein.
6. Fahren Sie mit Schritt 2 des Einrichtungsablaufs fort, wählen Sie den Synchronisierungstyp „Catalogs" und geben Sie den Integrationsnamen und den Zeitplan ein. Beachten Sie, dass der Name der Integration **exakt übereinstimmen** muss mit dem Namen des zuvor erstellten Katalogs.
7. Wählen Sie eine Synchronisierungshäufigkeit und fahren Sie mit dem nächsten Schritt fort.
8. Fügen Sie den im Dashboard angezeigten Public Key dem Benutzer hinzu, den Sie für die Verbindung von Braze mit Snowflake erstellt haben. Für diesen Schritt benötigen Sie jemanden mit `SECURITYADMIN`-Zugriff oder höher in Snowflake. 
9. Wählen Sie **Test Connection**, um sicherzustellen, dass alles wie erwartet funktioniert. 
10. Speichern Sie die Synchronisierung und nutzen Sie die synchronisierten Katalogdaten für all Ihre Personalisierungs-Anwendungsfälle. 
{% endtab %}
{% tab Redshift %}

1. Richten Sie in Redshift eine Quelltabelle ein. Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Richten Sie einen Benutzer ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass Sie den Zugriff auf die Katalogquelltabelle erweitern.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Wenn Sie eine Firewall oder andere Netzwerkrichtlinien haben, müssen Sie Braze Netzwerkzugriff auf Ihre Redshift-Instanz gewähren. Erlauben Sie den Zugriff von den unten aufgeführten IPs, die der Region Ihres Braze-Dashboards entsprechen. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Optional können Sie ein neues Projekt oder Dataset für Ihre Quelltabelle einrichten. 

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| FELDNAME | TYP | MODUS |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | ERFORDERLICH |
| PAYLOAD | JSON | ERFORDERLICH |
| ID | STRING | ERFORDERLICH |
| DELETED | BOOLEAN | OPTIONAL |

{:start="2"}

2. Richten Sie einen Benutzer ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden – stellen Sie jedoch sicher, dass Sie den Zugriff auf die Katalogquelltabelle erweitern. 
Das Dienstkonto sollte über die folgenden Berechtigungen verfügen:
- BigQuery Connection User: Ermöglicht Braze, Verbindungen herzustellen.
- BigQuery User: Ermöglicht Braze, Abfragen auszuführen, Dataset-Metadaten zu lesen und Tabellen aufzulisten.
- BigQuery Data Viewer: Ermöglicht Braze, Datasets und deren Inhalt einzusehen.
- BigQuery Job User: Ermöglicht Braze, Jobs auszuführen.<br><br>Nachdem Sie das Dienstkonto erstellt und die Berechtigungen erteilt haben, generieren Sie einen JSON-Schlüssel. Weitere Informationen finden Sie unter [Erstellen und Löschen von Schlüsseln](https://cloud.google.com/iam/docs/keys-create-delete). Diesen laden Sie später im Braze-Dashboard hoch.

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre BigQuery-Instanz gewähren. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Richten Sie eine Quelltabelle in Databricks ein. Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Katalog-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| FELDNAME | TYP | MODUS |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | ERFORDERLICH |
| PAYLOAD | STRING, STRUCT oder MAP | ERFORDERLICH |
| ID | STRING | ERFORDERLICH |
| DELETED | BOOLEAN | NULLABLE |

{:start="2"}

2. Erstellen Sie ein persönliches Zugriffstoken in Ihrem Databricks-Workspace.

- a. Wählen Sie Ihren Databricks-Benutzernamen und dann im Dropdown-Menü **User Settings**.
- b. Wählen Sie auf dem Tab **Access tokens** die Option **Generate new token**.
- c. Geben Sie einen Kommentar ein, der Ihnen hilft, dieses Token zu identifizieren, z. B. „Braze CDI". 
- d. Ändern Sie die Lifetime des Tokens auf unbegrenzt, indem Sie das Feld **Lifetime (days)** leer lassen. Wählen Sie **Generate**.
- e. Kopieren Sie das angezeigte Token und wählen Sie dann **Done**. 
- f. Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es bei der Erstellung der Zugangsdaten im Braze-Dashboard eingeben müssen.

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Eine Liste der IPs finden Sie auf der Seite [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. Richten Sie einen Dienstprinzipal ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden – stellen Sie nur sicher, dass Sie den Zugriff auf die Katalogquelltabelle erweitern. Weitere Informationen zur Erstellung eines neuen Dienstprinzipals und der Zugangsdaten finden Sie auf der Seite [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien eingerichtet haben, müssen Sie Braze Netzwerkzugriff auf Ihre Microsoft Fabric-Instanz gewähren. Eine Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Richten Sie Ihre Quelldateien in S3 ein, indem Sie JSON- oder CSV-Dateien bereitstellen. Bitte beachten Sie:

- Dateien dürfen keine Spalte `UPDATED_AT` enthalten.  
- Sie können ein optionales Feld `DELETED` hinzufügen, um Artikel zum Entfernen zu markieren. 

{% subtabs %}
{% subtab JSON %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```
{% endsubtab %}

{% subtab CSV %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% endsubtabs %}

Einzelheiten zur Einrichtung finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## So funktioniert die Integration

Bei jeder Synchronisierung ruft Braze alle Zeilen ab, deren `UPDATED_AT`-Zeitstempel nach dem zuletzt synchronisierten Wert liegt. Zeilen, die exakt auf dem Grenz-Zeitstempel liegen, können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen. Wir empfehlen, in Ihrem Data Warehouse eine Ansicht aus Ihren Katalogdaten zu erstellen, um eine Quelltabelle einzurichten, die bei jeder Synchronisierung vollständig aktualisiert wird. Mit Ansichten müssen Sie die Abfrage nicht jedes Mal neu schreiben.

Wenn Sie zum Beispiel eine Tabelle mit Produktdaten (`product_catalog_1`) mit `product_id` und drei weiteren Attributen haben, können Sie die folgende Ansicht synchronisieren:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Die von der Integration abgerufenen Daten werden verwendet, um Artikel im Zielkatalog anhand der angegebenen `id` zu erstellen oder zu aktualisieren.
- Wenn DELETED auf `true` gesetzt ist, wird der entsprechende Katalogartikel gelöscht.
- Die Synchronisierung verbraucht keine Datenpunkte, jedoch werden alle synchronisierten Daten auf Ihre gesamte Katalognutzung angerechnet. Diese Nutzung wird anhand der insgesamt gespeicherten Daten gemessen, sodass Sie sich keine Gedanken darüber machen müssen, nur geänderte Daten zu synchronisieren.
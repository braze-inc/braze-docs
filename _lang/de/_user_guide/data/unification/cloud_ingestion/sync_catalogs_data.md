---
nav_title: Katalogdaten synchronisieren und löschen
article_title: Katalogdaten synchronisieren und löschen
page_order: 4
page_type: reference
description: "Auf dieser Seite finden Sie eine Übersicht darüber, wie Sie Katalogdaten synchronisieren können."

---

# Katalogdaten synchronisieren und löschen

> Diese Seite beschreibt, wie Sie Katalogdaten synchronisieren können.
 
## Schritt 1: Einen neuen Katalog erstellen

Bevor Sie eine neue Cloud Data Ingestion (CDI)-Integration für [Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/) erstellen, müssen Sie einen neuen Katalog erstellen oder einen vorhandenen Katalog identifizieren, den Sie für die Integration verwenden möchten. Es gibt mehrere Möglichkeiten, einen neuen Katalog zu erstellen. Sie alle eignen sich für die CDI-Integration:
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv) hochladen
- Erstellen Sie einen Katalog im [Braze-Dashboard]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) oder bei der CDI-Einrichtung.
- Erstellen Sie einen Katalog mithilfe des [Endpunkts Katalog erstellen]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Änderungen am Katalogschema (wie die Ergänzung von Feldern oder Änderungen am Feldtyp) müssen stets über das Katalog-Dashboard vorgenommen werden, bevor die aktualisierten Daten über die CDI synchronisiert werden. Wir empfehlen, diese Aktualisierungen vorzunehmen, wenn die Synchronisierung unterbrochen wird oder keine ansteht. So vermeiden Sie Konflikte zwischen den Daten aus Ihrem Data Warehouse und dem Braze-Schema.

## Schritt 2: Integration von cloudbasierter Datenaufnahme und Katalogdaten
Die Einrichtung einer Katalogsynchronisation folgt weitgehend dem Prozess für [Nutzerdaten CDI Integrationen]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Richten Sie in Snowflake eine Quelltabelle ein. Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Datenbank-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.
  ```json
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
2. Set up a role, warehouse, and user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    ```json
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. If your Snowflake account has network policies, allowlist the Braze IPs so the CDI service can connect. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. In the Braze dashboard, navigate to **Technology Partners** > **Snowflake**, and create a new sync.
5. Enter connection details (or reuse existing credentials) and the source table.
6. Proceed to step 2 of the setup flow, select the “Catalogs” sync type, and input the integration name and schedule. Note that the name of the integration should **exactly match** the name of the catalog you previously created.
7. Choose a sync frequency and proceed to the next step.
8. Add the public key displayed on the dashboard to the user you created for Braze to connect to Snowflake. To complete this step, you will need someone with `SECURITYADMIN` access or higher in Snowflake. 
9. Select **Test Connection** so that everything works as expected. 
10. Save the sync, and use the synced catalog data for all your personalization use cases. 
{% endtab %}
{% tab Redshift %}

1. Set up a source table in Redshift. You can use the names in the following example or choose your own database, schema, and table names. You may also use a view or a materialized view instead of a table.
    ```json
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
2. Set up a user and grant proper permissions. If you already have credentials from an existing sync, you can reuse them, but make sure to extend access to the catalog source table.
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. If you have a firewall or other network policies, you must give Braze network access to your Redshift instance. Allow access from the below IPs corresponding to your Braze dashboard’s region. For a list of IPs, refer to the [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab BigQuery %}

1. Optionally, set up a new project or dataset to hold your source table. 

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit den folgenden Feldern:

```json
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
| UPDATED_AT | ZEITSTEMPEL | PFLICHTANGABE |
| PAYLOAD | JSON | PFLICHTANGABE |
| ID | STRING | PFLICHTANGABE |
| GELÖSCHT | BOOLESCHER WERT | OPTIONAL |

{:start="2"}

2. Richten Sie einen Nutzer:in ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden - stellen Sie jedoch sicher, dass Sie den Zugriff auf die Katalogquelltabelle erweitern.
Das Konto für den Dienst sollte über die folgenden Berechtigungen verfügen:
- BigQuery-Verbindung Benutzer: Dies erlaubt es Braze, Verbindungen herzustellen.
- BigQuery-Benutzer: So kann Braze Abfragen ausführen, Datensatz-Metadaten lesen und Tabellen auflisten.
- BigQuery Daten Betrachter: So kann Braze auf Datensätze und deren Inhalt zugreifen.
- BigQuery Job Benutzer: Dies ermöglicht Braze den Zugriff auf die Ausführung von Aufträgen<br><br>Wenn Sie das Dienstkonto erstellt und die Berechtigungen erteilt haben, erzeugen Sie einen JSON-Schlüssel. Weitere Informationen finden Sie unter [Erstellen und Löschen von Schlüsseln](https://cloud.google.com/iam/docs/keys-create-delete). Sie werden dies später auf dem Braze-Dashboard aktualisieren.

{:start="3"}
3\. Wenn Sie Netzwerkrichtlinien aufgestellt haben, müssen Sie Braze Netzwerkzugriff auf Ihre BigQuery-Instanz gewähren. Eine Liste der IPs finden Sie unter [Datenaufnahme in der Cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Richten Sie eine Quelltabelle in Databricks ein. Sie können die Namen aus dem folgenden Beispiel verwenden oder Ihre eigenen Katalog-, Schema- und Tabellennamen wählen. Sie können auch eine Ansicht oder eine materialisierte Ansicht anstelle einer Tabelle verwenden.

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```json
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
| UPDATED_AT | ZEITSTEMPEL | PFLICHTANGABE |
| PAYLOAD | STRING, STRUCT, oder MAP | PFLICHTANGABE |
| ID | STRING | PFLICHTANGABE |
| GELÖSCHT | BOOLESCHER WERT | LÖSCHBAR |

{:start="2"}

2. Erstellen Sie ein persönliches Token für den Zugriff in Ihrem Databricks Workspace.

- a. Wählen Sie Ihren Databricks-Benutzernamen und gehen Sie im Dropdown-Menü dann auf die **Benutzereinstellungen**.
- b. Auf dem Tab **Zugriffstoken** wählen Sie **Neues Token generieren**.
- c. Geben Sie einen Kommentar wie "Braze CDI" ein, um das Token leichter zu identifizieren. 
- d. Ändern Sie die Lifetime des Tokens in keine Lifetime, indem Sie das Feld **Lifetime (Tage)** leer lassen. Wählen Sie **Generieren**.
- e. Kopieren Sie das angezeigte Token, und wählen Sie dann **Fertig**. 
- f. Bewahren Sie das Token an einem sicheren Ort auf, bis Sie es bei der Erstellung der Zugangsdaten im Braze-Dashboard eingeben müssen.

{:start="3"}
3\. Wenn Sie Netzwerkrichtlinien aufgestellt haben, müssen Sie Braze Netzwerkzugriff auf Ihre Databricks-Instanz gewähren. Eine Liste der IP-Adressen finden Sie unter [cloudbasierter Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Erstellen Sie eine oder mehrere Tabellen, die Sie für Ihre CDI-Integration verwenden möchten, mit den folgenden Feldern:

```json
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

2. Richten Sie einen Dienstprinzipal ein und erteilen Sie die entsprechenden Berechtigungen. Wenn Sie bereits über Zugangsdaten aus einer bestehenden Synchronisierung verfügen, können Sie diese wiederverwenden - stellen Sie nur sicher, dass Sie den Zugriff auf die Katalogquelltabelle erweitern. Weitere Informationen über die Erstellung eines neuen Dienstes und der Zugangsdaten finden Sie auf der Seite [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3\. Wenn Sie Netzwerkrichtlinien aufgestellt haben, müssen Sie Braze Netzwerkzugriff auf Ihre Instanz von Microsoft Fabric gewähren. Eine Liste der IPs finden Sie in der [Cloud Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Richten Sie Ihre Quelldateien in S3 ein, indem Sie JSON- oder CSV-Dateien bereitstellen. Denken Sie daran:

- Dateien können keine `UPDATED_AT` Spalte enthalten  
- Sie können ein optionales `DELETED` Feld einfügen, um Artikel zum Entfernen zu markieren. 

{% subtabs %}
{% subtab JSON %}
```json
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

Einzelheiten zur Einrichtung finden Sie unter [Integration von Dateispeichern]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## So funktioniert die Integration

Bei jeder Synchronisierung zieht Braze alle Zeilen ein, bei denen `UPDATED_AT` gleich oder nach dem letzten synchronisierten Zeitstempel liegt. Wir empfehlen, in Ihrem Data Warehouse eine Ansicht aus Ihren Katalogdaten zu erstellen, um eine Quelltabelle einzurichten, die bei jeder Synchronisierung vollständig aktualisiert wird. Wenn Sie Ansichten verwenden, müssen Sie die Abfrage nicht jedes Mal neu schreiben.

Wenn Sie zum Beispiel eine Tabelle mit Produktdaten (`product_catalog_1`) mit der `product_id` und drei weiteren Attributen verwenden, können Sie folgende Ansicht synchronisieren:

{% tabs %}
{% tab Snowflake %}
```json
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
```json
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
```json
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
```json
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
```json
CREATE VIEW [braze].[user_update_example]
AS SELECT 
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- Die von der Integration abgerufenen Daten werden zur Erstellung bzw. Aktualisierung von Artikeln im Zielkatalog anhand der angegebenen `id` verwendet.
- Wenn GELÖSCHT auf `true` gesetzt ist, wird der entsprechende Katalogartikel gelöscht.
- Die Synchronisierung protokolliert keine Datenpunkte, aber alle synchronisierten Daten werden auf die Gesamtnutzung Ihres Katalogs angerechnet. Diese Nutzung wird auf der Grundlage der insgesamt gespeicherten Daten gemessen, so dass Sie sich keine Sorgen machen müssen, nur geänderte Daten zu synchronisieren.

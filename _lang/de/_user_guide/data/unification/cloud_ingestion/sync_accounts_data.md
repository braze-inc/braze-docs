---
nav_title: Synchronisieren und Löschen von Kontodaten
article_title: Kontodaten über CDI synchronisieren
page_order: 4
page_type: reference
description: "Erfahren Sie, wie Sie die Daten Ihres Braze-Kontos mithilfe von CDI synchronisieren können."

---

# Kontodaten über CDI synchronisieren

> Erfahren Sie, wie Sie die Daten Ihres Braze-Kontos mithilfe von CDI synchronisieren können.

{% alert important %}
[Kontoobjekte](https://braze.com/unlisted_docs/account_opportunity_object/) befinden sich in der Beta-Phase und sind für die Nutzung dieses Features erforderlich. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Teilnahme an der Beta interessiert sind.
{% endalert %}

## Voraussetzungen

Bevor Sie Ihre Kontodaten mit CDI synchronisieren können, müssen Sie [Ihr Kontoschema konfigurieren](https://braze.com/unlisted_docs/account_opportunity_object/).

{% alert note %}
Nehmen Sie Änderungen an Ihrem Kontoschema nur vor, wenn die Synchronisierung pausiert ist oder kein Zeitplan besteht, um Konflikte zwischen Ihren Data-Warehouse-Daten und dem Schema in Braze zu vermeiden.
{% endalert %}

## Wie die Synchronisierung funktioniert

- Bei jeder Synchronisierung werden Zeilen importiert, deren `UPDATED_AT`-Zeitstempel nach dem zuletzt synchronisierten Zeitstempel liegt. Zeilen an der exakten Grenze des Zeitstempels können erneut synchronisiert werden, wenn neue Zeilen denselben Zeitstempel aufweisen. Weitere Informationen finden Sie unter [Erneutes Synchronisieren von Zeilen mit doppelten Zeitstempeln vermeiden]({{site.baseurl}}/user_guide/data/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps).
- Die Daten aus der Integration erstellen oder aktualisieren Konten auf Grundlage der bereitgestellten `id`.
- Wenn `DELETED` den Wert `true` hat, wird das Konto gelöscht.
- Bei der Synchronisierung werden keine Datenpunkte protokolliert, jedoch werden alle synchronisierten Daten auf Ihre gesamte Kontonutzung angerechnet, gemessen an der Gesamtmenge der gespeicherten Daten – es ist nicht erforderlich, sich nur auf geänderte Daten zu beschränken.
- Felder, die nicht in Ihrem Kontoschema enthalten sind, werden verworfen. Aktualisieren Sie das Schema, bevor Sie neue Felder synchronisieren.
- Sie können eine Synchronisierung aktualisieren, fortsetzen oder pausieren, indem Sie mit der Maus über den Namen der Synchronisierung fahren und die entsprechende Aktion auswählen.

## Ihre Kontodaten synchronisieren

Sie können Ihre Kontodaten mithilfe von CDI über ein Data Warehouse oder einen Dateispeicher synchronisieren.

{% tabs local %}
{% tab Data Warehouse %}
So integrieren Sie Ihre Datenquelle mit Ihrem Data Warehouse:

{% subtabs %}
{% subtab Snowflake %}

1. Erstellen Sie eine Quelltabelle in Snowflake. Verwenden Sie die Namen aus dem Beispiel oder wählen Sie Ihre eigenen Datenbank-, Schema- und Tabellennamen. Sie können anstelle einer Tabelle auch eine View oder eine materialisierte View verwenden.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the account to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Name of the account to be created or updated
         NAME VARCHAR(16777216) NOT NULL,
         --Account fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The account associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. Erstellen Sie eine Rolle, ein Warehouse und einen Benutzer und vergeben Sie Berechtigungen. Wenn Sie bereits Zugangsdaten von einer anderen Synchronisierung haben, können Sie diese wiederverwenden – stellen Sie sicher, dass sie Zugriff auf die Kontotabelle haben.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Wenn Sie Netzwerkrichtlinien verwenden, setzen Sie die Braze-IPs auf die Allowlist, damit der CDI-Dienst eine Verbindung herstellen kann. Die Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. Gehen Sie im Braze-Dashboard zu **Data Settings** > **Cloud Data Ingestion** und erstellen Sie eine neue Synchronisierung.
5. Geben Sie die Verbindungsdetails ein (oder verwenden Sie vorhandene) und fügen Sie dann die Quelltabelle hinzu.
6. Wählen Sie den Synchronisierungstyp **Accounts** aus und geben Sie dann den Integrationsnamen und den Zeitplan ein.
7. Wählen Sie die Synchronisierungshäufigkeit.
8. Fügen Sie den Public Key aus dem Dashboard dem von Ihnen erstellten Benutzer hinzu. Dies erfordert einen Benutzer mit `SECURITYADMIN`-Zugriff oder höher in Snowflake.
9. Wählen Sie **Test Connection**, um die Einrichtung zu bestätigen.
10. Wenn Sie fertig sind, speichern Sie die Synchronisierung.

{% endsubtab %}
{% subtab Redshift %}

1. Erstellen Sie eine Quelltabelle in Redshift. Verwenden Sie die Namen aus dem Beispiel oder wählen Sie Ihre eigenen Datenbank-, Schema- und Tabellennamen. Sie können anstelle einer Tabelle auch eine View oder eine materialisierte View verwenden.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the account to be created or updated
       id varchar not null,
       --Name of the account to be created or updated
       name varchar not null,
       --Account fields and values that should be added or updated
       payload varchar(max),
       --The account associated with this ID should be deleted
       deleted boolean
    )
    ```
2. Erstellen Sie einen Benutzer und vergeben Sie Berechtigungen. Wenn Sie bereits Zugangsdaten von einer anderen Synchronisierung haben, können Sie diese wiederverwenden – stellen Sie sicher, dass sie Zugriff auf die Kontotabelle haben.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Wenn Sie eine Firewall oder Netzwerkrichtlinien verwenden, erlauben Sie Braze den Zugriff auf Ihre Redshift-Instanz. Die Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab BigQuery %}

1. (Optional) Erstellen Sie ein neues Projekt oder einen neuen Datensatz für Ihre Quelltabelle.
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Erstellen Sie die Quelltabelle für Ihre CDI-Integration:
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp,
      id STRING,
      name STRING,
      payload JSON,
      deleted BOOLEAN
    );
    ```

    Beachten Sie beim Erstellen Ihrer Quelltabelle Folgendes:

    | Feldname | Typ | Erforderlich? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Zeitstempel | Ja |
    | `PAYLOAD` | JSON | Ja |
    | `ID` | String | Ja |
    | `NAME` | String | Ja |
    | `DELETED` | Boolescher Wert | Optional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Erstellen Sie einen Benutzer und vergeben Sie Berechtigungen. Wenn Sie bereits Zugangsdaten von einer anderen Synchronisierung haben, können Sie diese wiederverwenden, solange sie Zugriff auf die Kontotabelle haben.

    | Berechtigung | Zweck |
    |------------|---------|
    | BigQuery Connection User | Ermöglicht Braze die Verbindung. |
    | BigQuery User | Ermöglicht Braze das Ausführen von Abfragen, Lesen von Metadaten und Auflisten von Tabellen. |
    | BigQuery Data Viewer | Ermöglicht Braze das Anzeigen von Datensätzen und Inhalten. |
    | BigQuery Job User | Ermöglicht Braze das Ausführen von Jobs. |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

    Generieren Sie nach der Vergabe der Berechtigungen einen JSON-Schlüssel. Anweisungen finden Sie unter [Schlüssel erstellen und löschen](https://cloud.google.com/iam/docs/keys-create-delete). Sie laden ihn später im Braze-Dashboard hoch.

{:start="4"}
4. Wenn Sie Netzwerkrichtlinien verwenden, erlauben Sie Braze-IPs den Zugriff auf Ihre BigQuery-Instanz. Die Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Databricks %}

1. Erstellen Sie einen Katalog oder ein Schema für Ihre Quelltabelle.
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Erstellen Sie die Quelltabelle für Ihre CDI-Integration:
    ```sql
    CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.ACCOUNTS_SYNC`
    (
      updated_at TIMESTAMP DEFAULT current_timestamp(),
      id STRING,
      name STRING,
      payload STRING, STRUCT, or MAP,
      deleted BOOLEAN
    );
    ```

    Beachten Sie beim Erstellen Ihrer Quelltabelle Folgendes:

    | Feldname | Typ | Erforderlich? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Zeitstempel | Ja |
    | `PAYLOAD` | String, Struct oder Map | Ja |
    | `ID` | String | Ja |
    | `NAME` | String | Ja |
    | `DELETED` | Boolescher Wert | Optional |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Erstellen Sie ein persönliches Zugriffstoken in Databricks:
    1. Wählen Sie Ihren Benutzernamen und dann **User Settings** aus.
    2. Wählen Sie auf dem Tab **Access tokens** die Option **Generate new token** aus.
    3. Fügen Sie einen Kommentar zur Identifizierung des Tokens hinzu, z. B. „Braze CDI".
    4. Lassen Sie **Lifetime (days)** leer, damit das Token nicht abläuft, und wählen Sie dann **Generate** aus.
    5. Kopieren und speichern Sie das Token sicher für die Verwendung im Braze-Dashboard.

{:start="4"}
4. Wenn Sie Netzwerkrichtlinien verwenden, erlauben Sie Braze-IPs den Zugriff auf Ihre Databricks-Instanz. Die Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. Erstellen Sie eine oder mehrere Tabellen für Ihre CDI-Integration mit diesen Feldern:
    ```sql
    CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
    (
      UPDATED_AT DATETIME2(6) NOT NULL,
      PAYLOAD VARCHAR NOT NULL,
      ID VARCHAR NOT NULL,
      NAME VARCHAR NOT NULL,
      DELETED BIT
    )
    GO
    ```

{:start="2"}
2. Erstellen Sie einen Dienstprinzipal und vergeben Sie Berechtigungen. Wenn Sie bereits Zugangsdaten von einer anderen Synchronisierung haben, können Sie diese wiederverwenden – stellen Sie sicher, dass sie Zugriff auf die Kontotabelle haben.

{:start="3"}
3. Wenn Sie Netzwerkrichtlinien verwenden, erlauben Sie Braze-IPs den Zugriff auf Ihre Microsoft Fabric-Instanz. Die Liste der IPs finden Sie unter [Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab File Storage %}
Um Kontodaten aus einem Dateispeicher zu synchronisieren, erstellen Sie eine Quelldatei mit den folgenden Feldern.

| Feld | Erforderlich? | Beschreibung |  
| --- | --- | --- |  
| `ID` | Ja | ID des Kontos, das aktualisiert oder erstellt werden soll |  
| `NAME` | Ja | Name des Kontos |  
| `PAYLOAD` | Ja | JSON-String der Felder, die mit dem Konto in Braze synchronisiert werden sollen |  
| `DELETED` | Optional | Boolescher Wert, der angibt, dass das Konto aus Braze gelöscht werden soll |  
| `UPDATED_AT` | _*Nicht unterstützt_ | Dateispeicher unterstützen keine `UPDATED_AT`-Spalten |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Dateinamen müssen den AWS-Regeln entsprechen und eindeutig sein. Hängen Sie Zeitstempel an, um die Eindeutigkeit sicherzustellen. Weitere Informationen zur Amazon S3-Synchronisierung finden Sie unter [Dateispeicher-Integrationen]({{site.baseurl}}/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

Die folgenden Beispiele zeigen gültige JSON- und CSV-Formate für die Synchronisierung von Kontodaten aus einem Dateispeicher.

{% subtabs %}
{% subtab JSON Accounts %}
```jsonl  
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```  

{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, andernfalls wird die Datei übersprungen.
{% endalert %}
{% endsubtab %}
{% subtab CSV Accounts with Delete %}
```plaintext  
ID,NAME,PAYLOAD,DELETED
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}",TRUE 
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}",FALSE
```
{% endsubtab %}
{% subtab CSV Accounts without Delete %}
```plaintext  
ID,NAME,PAYLOAD
85,"ACCOUNT_1","{""region"": ""APAC"", ""employees"": 850}"
1,"ACCOUNT_2","{""region"": ""EMEA"", ""employees"": 10000}"
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Synchronisierungsansicht erstellen

Durch das Erstellen einer Synchronisierungsansicht in Ihrem Data Warehouse kann die Quelle automatisch aktualisiert werden, ohne dass zusätzliche Abfragen neu geschrieben werden müssen.

Wenn Sie beispielsweise eine Tabelle mit Kontodaten namens `account_details_1` mit `account_id`, `account_name` und drei zusätzlichen Attributen haben, könnten Sie eine Synchronisierungsansicht wie die folgende erstellen:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS 
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    account_id as id,
    account_name as name,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "account_details_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.ACCOUNTS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    account_id as ID,
    account_name as NAME,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD 
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.account_details_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [BRAZE_CLOUD_PRODUCTION].[INGESTION].[ACCOUNTS_SYNC]
AS SELECT 
    account_id as ID,
    account_name as NAME,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[account_details_1] ;
```
{% endtab %}
{% endtabs %}
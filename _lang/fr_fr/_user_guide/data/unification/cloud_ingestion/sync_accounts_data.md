---
nav_title: Synchroniser et supprimer les données du compte
article_title: Synchroniser les données de compte à l'aide de CDI
page_order: 4
page_type: reference
description: "Découvrez comment synchroniser les données de votre compte Braze à l'aide de CDI."

---

# Synchroniser les données de compte à l'aide de CDI

> Découvrez comment synchroniser les données de votre compte Braze à l'aide de CDI.

{% alert important %}
Les [objets de compte](https://braze.com/unlisted_docs/account_opportunity_object/) sont en version bêta et sont nécessaires pour utiliser cette fonctionnalité. Contactez votre Account Manager Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Conditions préalables

Avant de pouvoir synchroniser les données de votre compte à l'aide de CDI, vous devez [configurer le schéma de vos comptes](https://braze.com/unlisted_docs/account_opportunity_object/).

{% alert note %}
Effectuez les mises à jour de votre schéma de compte uniquement lorsque la synchronisation est suspendue ou non planifiée, afin d'éviter tout conflit entre les données de votre entrepôt de données et le schéma dans Braze.
{% endalert %}

## Fonctionnement de la synchronisation

- Chaque synchronisation importe les lignes dont la valeur `UPDATED_AT` est postérieure à l'horodatage de la dernière synchronisation. Les lignes situées exactement à l'horodatage limite peuvent être resynchronisées si de nouvelles lignes partagent ce même horodatage. Pour en savoir plus, consultez [Éviter la resynchronisation de lignes avec des horodatages en double]({{site.baseurl}}/user_guide/data/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps).
- Les données issues de l'intégration créent ou mettent à jour des comptes en fonction de l'`id` fourni.
- Si `DELETED` est `true`, le compte est supprimé.
- La synchronisation ne consomme pas de points de donnée, mais toutes les données synchronisées sont comptabilisées dans l'utilisation totale de vos comptes, mesurée par le volume total de données stockées — il n'est pas nécessaire de se limiter aux seules données modifiées.
- Les champs absents de votre schéma de comptes sont ignorés ; mettez à jour le schéma avant de synchroniser de nouveaux champs.
- Vous pouvez actualiser, reprendre ou suspendre une synchronisation en survolant le nom de la synchronisation et en sélectionnant l'action correspondante.

## Synchroniser les données de votre compte

Vous pouvez synchroniser les données de votre compte à l'aide de CDI via un entrepôt de données ou un stockage de fichiers.

{% tabs local %}
{% tab Data Warehouse %}
Pour intégrer votre source de données à votre entrepôt de données :

{% subtabs %}
{% subtab Snowflake %}

1. Créez une table source dans Snowflake. Utilisez les noms fournis dans l'exemple ou choisissez vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée à la place d'une table.
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
2. Créez un rôle, un entrepôt et un utilisateur, puis accordez les autorisations. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser — assurez-vous simplement qu'ils ont accès à la table des comptes.
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
3. Si vous utilisez des politiques réseau, ajoutez les adresses IP de Braze à la liste autorisée afin que le service CDI puisse se connecter. Pour la liste des adresses IP, consultez [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).
4. Dans le tableau de bord de Braze, accédez à **Data Settings** > **Cloud Data Ingestion** et créez une nouvelle synchronisation.
5. Saisissez les détails de connexion (ou réutilisez des identifiants existants), puis ajoutez la table source.
6. Sélectionnez le type de synchronisation **Accounts**, puis saisissez le nom de l'intégration et la planification. 
7. Choisissez la fréquence de synchronisation.
8. Ajoutez la clé publique du tableau de bord à l'utilisateur que vous avez créé. Cela nécessite un utilisateur disposant d'un accès `SECURITYADMIN` ou supérieur dans Snowflake. 
9. Sélectionnez **Test Connection** pour confirmer la configuration. 
10. Une fois terminé, enregistrez la synchronisation.

{% endsubtab %}
{% subtab Redshift %}

1. Créez une table source dans Redshift. Utilisez les noms fournis dans l'exemple ou choisissez vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée à la place d'une table.
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
2. Créez un utilisateur et accordez les autorisations. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser — assurez-vous simplement qu'ils ont accès à la table des comptes.
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE ACCOUNTS_SYNC TO braze_user;
    ```
    {% endraw %}
3. Si vous disposez d'un pare-feu ou de politiques réseau, autorisez Braze à accéder à votre instance Redshift. Pour la liste des adresses IP, consultez [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab BigQuery %}

1. (Facultatif) Créez un nouveau projet ou jeu de données pour votre table source.  
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Créez la table source pour votre intégration CDI :  
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

    Référez-vous aux informations suivantes lors de la création de votre table source :

    | Nom du champ | Type | Requis ? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Oui |
    | `PAYLOAD` | JSON | Oui |
    | `ID` | String | Oui |
    | `NAME` | String | Oui |
    | `DELETED` | Boolean | Facultatif |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Créez un utilisateur et accordez les autorisations. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser à condition qu'ils aient accès à la table des comptes.

    | Autorisation | Objectif |
    |------------|---------|
    | BigQuery Connection User | Permet à Braze de se connecter. |
    | BigQuery User | Permet à Braze d'exécuter des requêtes, de lire les métadonnées et de lister les tables. |
    | BigQuery Data Viewer | Permet à Braze de consulter les jeux de données et leur contenu. |
    | BigQuery Job User | Permet à Braze d'exécuter des tâches. |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

    Après avoir accordé les autorisations, générez une clé JSON. Consultez [Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) pour les instructions. Vous la téléverserez ultérieurement dans le tableau de bord de Braze.

{:start="4"}
4. Si vous utilisez des politiques réseau, autorisez les adresses IP de Braze à accéder à votre instance BigQuery. Pour la liste des adresses IP, consultez [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Databricks %}

1. Créez un catalogue ou un schéma pour votre table source.  
    ```sql
    CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
    ```

2. Créez la table source pour votre intégration CDI :  
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

    Référez-vous aux informations suivantes lors de la création de votre table source :

    | Nom du champ | Type | Requis ? |
    | ---------- | ---- | --------- |
    | `UPDATED_AT` | Timestamp | Oui |
    | `PAYLOAD` | String, Struct, or Map | Oui |
    | `ID` | String | Oui |
    | `NAME` | String | Oui |
    | `DELETED` | Boolean | Facultatif |
    {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{:start="3"}
3. Créez un jeton d'accès personnel dans Databricks :
    1. Sélectionnez votre nom d'utilisateur, puis sélectionnez **User Settings**.  
    2. Dans l'onglet **Access tokens**, sélectionnez **Generate new token**.  
    3. Ajoutez un commentaire pour identifier le jeton, par exemple « Braze CDI ».  
    4. Laissez le champ **Lifetime (days)** vide pour ne pas définir d'expiration, puis sélectionnez **Generate**.  
    5. Copiez et enregistrez le jeton en lieu sûr pour l'utiliser dans le tableau de bord de Braze.

{:start="4"}
4. Si vous utilisez des politiques réseau, autorisez les adresses IP de Braze à accéder à votre instance Databricks. Pour la liste des adresses IP, consultez [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% subtab Microsoft Fabric %}

1. Créez une ou plusieurs tables pour votre intégration CDI avec les champs suivants :
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
2. Créez un principal de service et accordez les autorisations. Si vous disposez déjà d'identifiants provenant d'une autre synchronisation, vous pouvez les réutiliser — assurez-vous simplement qu'ils ont accès à la table des comptes.

{:start="3"}
3. Si vous utilisez des politiques réseau, autorisez les adresses IP de Braze à accéder à votre instance Microsoft Fabric. Pour la liste des adresses IP, consultez [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab File Storage %}
Pour synchroniser les données de compte depuis un stockage de fichiers, créez un fichier source avec les champs suivants.

| Champ | Requis ? | Description |  
| --- | --- | --- |  
| `ID` | Oui | ID du compte à mettre à jour ou à créer |  
| `NAME` | Oui | Nom du compte |  
| `PAYLOAD` | Oui | Chaîne de caractères JSON des champs à synchroniser vers le compte dans Braze |  
| `DELETED` | Facultatif | Valeur booléenne indiquant la suppression du compte dans Braze |  
| `UPDATED_AT` | _*Non pris en charge_ | Le stockage de fichiers ne prend pas en charge les colonnes `UPDATED_AT` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Les noms de fichiers doivent respecter les règles AWS et être uniques. Ajoutez des horodatages pour garantir l'unicité. Pour en savoir plus sur la synchronisation Amazon S3, consultez [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/cloud_ingestion/file_storage_integrations).
{% endalert %}

Les exemples suivants montrent des formats JSON et CSV valides pour synchroniser les données de compte depuis un stockage de fichiers.

{% subtabs %}
{% subtab JSON Accounts %}
```jsonl  
{"id":"s3-qa-0","name":"account0","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"id":"s3-qa-1","name":"account1","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":true}
{"id":"s3-qa-2","name":"account2","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}","deleted":false}
{"id":"s3-qa-3","name":"account3","payload":"{\"attribute_0\": \"GT896\", \"attribute_1\": 74, \"attribute_2\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
```  

{% alert important %}
Chaque ligne de votre fichier source doit contenir du JSON valide, sinon le fichier sera ignoré.
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

## Créer une vue de synchronisation

La création d'une vue de synchronisation dans votre entrepôt de données permet à la source de s'actualiser automatiquement sans avoir à réécrire de requêtes supplémentaires.

Par exemple, si vous disposez d'une table de données de compte appelée `account_details_1` avec `account_id`, `account_name` et trois attributs supplémentaires, vous pouvez créer une vue de synchronisation comme suit :

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
---
nav_title: Synchronisation et suppression des données du catalogue
article_title: Synchronisation et suppression des données du catalogue
page_order: 4
page_type: reference
description: "Cette page donne un aperçu de la manière de synchroniser les données du catalogue."

---

# Synchronisation et suppression des données du catalogue

> Cette page explique comment synchroniser les données du catalogue.
 
## Étape 1 : Créer un nouveau catalogue

Avant de créer une nouvelle intégration CDI (Cloud Data Ingestion) pour les [catalogues]({{site.baseurl}}/user_guide/data/activation/catalogs/), vous devez créer un nouveau catalogue ou identifier un catalogue existant que vous souhaitez utiliser pour l'intégration. Il existe plusieurs façons de créer un nouveau catalogue et chacune d'entre elles fonctionnera pour l'intégration CDI :
- Télécharger un [fichier CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv)
- Créez un catalogue dans le [tableau de bord de Braze]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser) ou lors de la configuration du CDI.
- Créez un catalogue à l'aide de l'[endpoint Créer un catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)

Toute modification du schéma du catalogue (par exemple, l'ajout de nouveaux champs ou la modification du type de champ) doit être effectuée via le tableau de bord du catalogue avant que les données mises à jour ne soient synchronisées via CDI. Nous vous recommandons d'effectuer ces mises à jour lorsque la synchronisation est en pause ou n'est pas planifiée afin d'éviter les conflits entre les données de votre entrepôt de données et le schéma dans Braze.

## Étape 2 : Intégration de l'ingestion de données dans le nuage avec les données du catalogue
La configuration d'une synchronisation de catalogue suit de près le processus des [intégrations CDI de données utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup). 

{% tabs %}
{% tab Snowflake %}

1. Créez un tableau des sources dans Snowflake. Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos propres noms de base de données, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée au lieu d'une table.
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

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| NOM DU CHAMP | TYPE | MODE |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | OBLIGATOIRE |
| CHARGE D'ACCOMPAGNEMENT | JSON | OBLIGATOIRE |
| ID | CHAÎNE DE CARACTÈRES | OBLIGATOIRE |
| SUPPRIMÉ | BOOLEAN | OPTIONNEL |

{:start="2"}

2. Créez un utilisateur et accordez-lui les autorisations nécessaires. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais veillez à étendre l'accès à la table source du catalogue.
Le compte de service doit disposer des autorisations suivantes :
- Utilisateur de connexion BigQuery : Cela permettra à Braze d'établir des connexions.
- Utilisateur BigQuery : Cela permettra à Braze d'accéder à l'exécution des requêtes, à la lecture des métadonnées des ensembles de données et à la liste des tableaux.
- BigQuery Data Viewer : Cela permettra à Braze d'accéder à la visualisation des ensembles de données et de leur contenu.
- BigQuery Job User : Cela permettra à Braze d'accéder à l'exécution des travaux.<br><br>Après avoir créé le compte de service et accordé les autorisations, générez une clé JSON. Pour plus d'informations, reportez-vous à la section [Création et suppression de clés](https://cloud.google.com/iam/docs/keys-create-delete). Vous le mettrez à jour dans le tableau de bord de Braze ultérieurement.

{:start="3"}
3\. Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance BigQuery. Pour obtenir la liste des IP, reportez-vous à l'[ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Databricks %}

1. Créez une table source dans Databricks. Vous pouvez utiliser les noms de l'exemple suivant ou choisir vos noms de catalogue, de schéma et de table. Vous pouvez également utiliser une vue ou une vue matérialisée au lieu d'une table.

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

| NOM DU CHAMP | TYPE | MODE |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | OBLIGATOIRE |
| CHARGE D'ACCOMPAGNEMENT | Chaîne de caractères, STRUCT ou mappage | OBLIGATOIRE |
| ID | CHAÎNE DE CARACTÈRES | OBLIGATOIRE |
| SUPPRIMÉ | BOOLEAN | NULLABLE |

{:start="2"}

2. Créez un jeton d'accès personnel dans votre espace de travail Databricks.

- a. Sélectionnez votre nom d'utilisateur Databricks, puis sélectionnez **User Settings** dans le menu déroulant.
- b. Dans l'onglet **Jetons d'accès**, sélectionnez **Générer un nouveau jeton**.
- c. Saisissez un commentaire qui vous aide à identifier ce jeton, par exemple "Braze CDI". 
- d. Remplacez la durée de vie du jeton par aucune durée de vie en laissant vide la case **Durée de vie (jours)**. Sélectionnez **Générer**.
- e. Copiez le jeton affiché, puis sélectionnez **Terminé**. 
- f. Conservez le jeton en lieu sûr jusqu'à ce que vous ayez besoin de le saisir lors de l'étape de création de justificatifs d'identité dans le tableau de bord de Braze.

{:start="3"}
3\. Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance Databricks. Pour obtenir la liste des IP, consultez la page relative à l'[ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab Microsoft Fabric %}

Créez une ou plusieurs tables à utiliser pour votre intégration CDI avec les champs suivants :

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

2. Mettez en place un principal de service et accordez les autorisations appropriées. Si vous disposez déjà d'informations d'identification provenant d'une synchronisation existante, vous pouvez les réutiliser, mais veillez à étendre l'accès à la table source du catalogue. Pour en savoir plus sur la création d'un nouveau principal de service et d'informations d'identification, consultez la page sur l'[ingestion de données dans le cloud]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views). 

{:start="3"}
3\. Si vous avez mis en place des politiques de réseau, vous devez donner à Braze un accès réseau à votre instance Microsoft Fabric. Pour obtenir une liste d'adresses IP, consultez l'[ingestion de données dans le nuage]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views).

{% endtab %}
{% tab S3 %}
Configurez vos fichiers sources dans S3 en fournissant des fichiers JSON ou CSV. N'oubliez pas :

- Les fichiers ne peuvent pas inclure une colonne `UPDATED_AT`   
- Vous pouvez inclure un champ facultatif `DELETED` pour marquer les éléments à supprimer. 

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

Pour plus de détails sur la configuration, voir [Intégrations de stockage de fichiers]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/).

{% endtab %}
{% endtabs %}

## Comment fonctionne l'intégration

Chaque fois que la synchronisation est exécutée, Braze récupère toutes les lignes pour lesquelles `UPDATED_AT` est égal ou postérieur au dernier horodatage synchronisé. Nous vous recommandons de créer une vue dans votre entrepôt de données à partir de vos données de catalogue afin de mettre en place une table source qui sera entièrement actualisée à chaque fois qu'une synchronisation sera exécutée. Avec les vues, vous n'aurez pas besoin de réécrire la requête à chaque fois.

Par exemple, si vous avez une table de données produit (`product_catalog_1`) avec `product_id` et trois attributs supplémentaires, vous pouvez synchroniser la vue ci-dessous :

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

- Les données extraites de l'intégration seront utilisées pour créer ou mettre à jour des articles dans le catalogue cible en fonction de l'adresse `id` fournie.
- Si DELETED est défini sur `true`, l'article de catalogue correspondant sera supprimé.
- La synchronisation n'enregistre pas de points de données, mais toutes les données synchronisées sont prises en compte dans l'utilisation totale de votre catalogue. Cette utilisation est mesurée sur la base de l'ensemble des données stockées, vous n'avez donc pas à vous soucier de synchroniser uniquement les données modifiées.

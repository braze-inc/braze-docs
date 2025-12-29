---
nav_title: カタログデータの同期と削除
article_title: カタログデータの同期と削除
page_order: 4
page_type: reference
description: "このページでは、カタログデータの同期方法の概要を説明する。"

---

# カタログデータの同期と削除

> このページでは、カタログデータの同期方法について説明する。
 
## ステップ1:新規カタログの作成

[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)用の新しいクラウドデータ取り込み (CDI) の連携を作成する前に、連携に使用する新規カタログを作成するか、既存のカタログを指定する必要があります。新規カタログを作成する方法はいくつかあり、いずれも CDI 連携に使用できます。
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv) をアップロードする。
- [Brazeダッシュボード]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser)またはCDIセットアップ中にカタログを作成する。
- [カタログ作成エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)を使用してカタログを作成する。

カタログスキーマへの変更（例えば、新しいフィールドの追加やフィールドタイプの変更）は、更新されたデータがCDIを通じて同期される前に、カタログダッシュボードを通じて行われなければならない。データウェアハウスのデータと Braze のスキーマとの競合を避けるために、同期が一時停止されているとき、または実行がスケジュールされていないときにこれらの更新を行うことをお勧めします。

## ステップ2:クラウドデータ取り込みとカタログデータの連携
カタログ同期の設定は、[ユーザーデータ CDI 連携]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup)のプロセスに厳密に従います。 

{% tabs %}
{% tab Snowflake %}

1. Snowflake でソーステーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。
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

次のフィールドを持ち、CDI 連携に使用するテーブルを 1 つ以上作成します。

```json
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED_AT | タイムスタンプ | 必須 |
| PAYLOAD | JSON | 必須 |
| ID | STRING | 必須 |
| 削除された | BOOLEAN | オプション |

{:start="2"}

2. ユーザーを設定し、適切な権限を付与します。既存の同期からの認証情報をすでに持っている場合はそれらを再利用できますが、必ずアクセスをカタログソーステーブルに拡張してください。
サービスアカウントには次の権限が必要です。
- BigQuery 接続ユーザー:Braze に接続を許可します。
- BigQuery ユーザー:クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- BigQuery データビューアー:データセットとその内容を表示するためのアクセスを Braze に提供します。
- BigQuery ジョブユーザー:ジョブを実行するためのアクセスを Braze に提供します。<br><br>サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳細については、[キーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。後でBrazeのダッシュボードに更新する。

{:start="3"}
3\.ネットワークポリシーを設定している場合は、Braze に Big Query インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、「[クラウド データの取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)」を参照してください。

{% endtab %}
{% tab Databricks %}

1. Databricks でソース テーブルを設定します。以下の例の名前を使うこともできるし、カタログ名、スキーマ名、テーブル名を選ぶこともできる。テーブルの代わりにビューやマテリアライズド・ビューを使うこともできる。

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

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED_AT | タイムスタンプ | 必須 |
| PAYLOAD | STRING、STRUCT、またはMAP。 | 必須 |
| ID | STRING | 必須 |
| 削除された | BOOLEAN | NULLABLE |

{:start="2"}

2. Databricks ワークスペースでパーソナルアクセストークンを作成します。

- a. Databricks ユーザー名を選択し、ドロップダウンメニューから [**ユーザー設定**] を選択します。
- b. [**アクセストークン**] タブで、[**新しいトークンの生成**] を選択します。
- c. 「Braze CDI」など、このトークンの識別に役立つコメントを入力します。 
- d. [**有効期間 (日)**] ボックスを空白のままにして、トークンの有効期間を有効期間なしに変更します。[**生成**] を選択します。
- e. 表示されたトークンをコピーして、[**完了**] を選択します。 
- f. 認証情報の作成ステップで Braze ダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

{:start="3"}
3\.ネットワークポリシーを設定している場合は、Brazeに Databricks インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、「[クラウド データの取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)」を参照してください。

{% endtab %}
{% tab Microsoft Fabric %}

次のフィールドを持ち、CDI 連携に使用するテーブルを 1 つ以上作成します。

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

2. サービスプリンシパルを設定し、適切な権限を与える。既存の同期からの認証情報をすでに持っている場合はそれらを再利用できますが、必ずアクセスをカタログソーステーブルに拡張してください。新しいサービスプリンシパルと認証情報を作成する方法については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)のページを参照のこと。 

{:start="3"}
3\.ネットワークポリシーを設定している場合は、BrazeにMicrosoft Fabricインスタンスへのネットワークアクセスを許可する必要がある。IP のリストについては、[「クラウド データの取り込み」]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab S3 %}
JSONまたはCSVファイルを提供して、S3にソースファイルを設定する。心に留めておいてほしい：

- ファイルに`UPDATED_AT` 列を含めることはできない。  
- 削除する項目をマークするために、オプションで`DELETED` フィールドを含めることができる。 

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

セットアップの詳細については、[ファイル・ストレージ統合を]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/)参照のこと。

{% endtab %}
{% endtabs %}

## 連携の仕組み

同期が実行されるたびに、Brazeは、`UPDATED_AT` が最後に同期されたタイムスタンプと同じかそれ以降のすべての行を取り込む。カタログデータからデータウェアハウスにビューを作成し、同期が実行されるたびに完全にリフレッシュされるソーステーブルを設定することをお勧めする。ビューを使えば、クエリーを毎回書き直す必要はない。

例えば、`product_id` と 3 つの追加属性を含む製品データテーブル (`product_catalog_1`) がある場合、以下のビューを同期できます。

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

- 連携からフェッチされたデータは、指定した `id` に基づいて、ターゲットカタログ内のアイテムの作成または更新に使用されます。
- DELETED が `true` に設定されている場合、対応するカタログアイテムが削除されます。
- 同期によってデータポイントは記録されないが、同期されたデータはすべてカタログの総使用量にカウントされる。この使用量は、保存されているデータの合計に基づいて計測されるため、変更されたデータだけを同期することを心配する必要はない。

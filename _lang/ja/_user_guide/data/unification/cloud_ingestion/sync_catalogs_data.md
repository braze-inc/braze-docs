---
nav_title: カタログデータの同期と削除
article_title: カタログデータの同期と削除
page_order: 4
page_type: reference
description: "このページでは、カタログデータの同期方法の概要を説明します。"

---

# カタログデータの同期と削除

> このページでは、カタログデータの同期方法について説明します。
 
## ステップ 1: 新規カタログの作成

[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/)用の新しいクラウドデータ取り込み (CDI) 連携を作成する前に、新規カタログを作成するか、連携に使用する既存のカタログを指定する必要があります。新規カタログを作成する方法はいくつかあり、いずれも CDI 連携に使用できます。
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-1-upload-csv) をアップロードする
- [Braze ダッシュボード]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#method-2-create-in-browser)または CDI セットアップ中にカタログを作成する
- [カタログ作成エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)を使用してカタログを作成する

カタログスキーマへの変更（例えば、新しいフィールドの追加やフィールドタイプの変更）は、更新されたデータが CDI を通じて同期される前に、カタログダッシュボードで行う必要があります。データウェアハウスのデータと Braze のスキーマとの競合を避けるために、同期が一時停止されているとき、または実行がスケジュールされていないときにこれらの更新を行うことをお勧めします。

## ステップ 2: クラウドデータ取り込みとカタログデータの連携
カタログ同期の設定は、[ユーザーデータ CDI 連携]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations#product-setup)のプロセスとほぼ同じです。 

{% tabs %}
{% tab Snowflake %}

1. Snowflake でソーステーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。
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
2. ロール、ウェアハウス、ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。
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
3. Snowflake アカウントにネットワークポリシーがある場合は、CDI サービスが接続できるように Braze の IP を許可リストに追加してください。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)を参照してください。
4. Braze ダッシュボードで、[**テクノロジーパートナー**] > [**Snowflake**] に移動し、新しい同期を作成します。
5. 接続の詳細（または既存の認証情報を再利用）とソーステーブルを入力します。
6. セットアップフローのステップ 2 に進み、「Catalogs」同期タイプを選択し、連携名とスケジュールを入力します。連携名は、以前に作成したカタログの名前と**完全に一致する**必要があることに注意してください。
7. 同期頻度を選択し、次のステップに進みます。
8. ダッシュボードに表示された公開キーを、Braze が Snowflake に接続するために作成したユーザーに追加します。このステップを完了するには、Snowflake で `SECURITYADMIN` 以上のアクセス権を持つ担当者が必要です。 
9. [**接続テスト**] を選択して、すべてが期待どおりに動作することを確認します。 
10. 同期を保存し、同期されたカタログデータをすべてのパーソナライゼーションのユースケースに活用します。 
{% endtab %}
{% tab Redshift %}

1. Redshift でソーステーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。
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
2. ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。
    {% raw %}
    ```sql 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. ファイアウォールやその他のネットワークポリシーがある場合は、Braze に Redshift インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab BigQuery %}

1. 必要に応じて、ソーステーブルを格納する新しいプロジェクトまたはデータセットを設定します。 

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI 連携に使用するテーブルを 1 つ以上作成します。

```sql
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
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | JSON | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | OPTIONAL |

{:start="2"}

2. ユーザーを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。 
サービスアカウントには次の権限が必要です。
- BigQuery 接続ユーザー: Braze に接続を許可します。
- BigQuery ユーザー: クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- BigQuery データビューアー: データセットとその内容を表示するためのアクセスを Braze に提供します。
- BigQuery ジョブユーザー: ジョブを実行するためのアクセスを Braze に提供します。<br><br>サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳細については、[Keys create and delete](https://cloud.google.com/iam/docs/keys-create-delete) を参照してください。後で Braze ダッシュボードにアップロードします。

{:start="3"}
3. ネットワークポリシーを設定している場合は、Braze に BigQuery インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab Databricks %}

1. Databricks でソーステーブルを設定します。以下の例の名前を使用することも、独自のカタログ名、スキーマ名、テーブル名を選択することもできます。テーブルの代わりにビューやマテリアライズドビューを使用することもできます。

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

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | STRING、STRUCT、または MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |

{:start="2"}

2. Databricks ワークスペースでパーソナルアクセストークンを作成します。

- a. Databricks ユーザー名を選択し、ドロップダウンメニューから [**ユーザー設定**] を選択します。
- b. [**アクセストークン**] タブで、[**新しいトークンの生成**] を選択します。
- c.「Braze CDI」など、このトークンの識別に役立つコメントを入力します。 
- d. [**有効期間 (日)**] ボックスを空白のままにして、トークンの有効期間を無期限に変更します。[**生成**] を選択します。
- e. 表示されたトークンをコピーして、[**完了**] を選択します。 
- f. Braze ダッシュボードの認証情報作成ステップで入力が必要になるまで、トークンを安全な場所に保管してください。

{:start="3"}
3. ネットワークポリシーを設定している場合は、Braze に Databricks インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)のページを参照してください。

{% endtab %}
{% tab Microsoft Fabric %}

次のフィールドを持つ、CDI 連携に使用するテーブルを 1 つ以上作成します。

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

2. サービスプリンシパルを設定し、適切な権限を付与します。既存の同期の認証情報をすでに持っている場合はそれらを再利用できますが、必ずカタログソーステーブルへのアクセスを拡張してください。新しいサービスプリンシパルと認証情報の作成方法については、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)のページを参照してください。 

{:start="3"}
3. ネットワークポリシーを設定している場合は、Braze に Microsoft Fabric インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab S3 %}
JSON ファイルまたは CSV ファイルを提供して、S3 にソースファイルを設定します。以下の点に注意してください。

- ファイルには `UPDATED_AT` 列を含めることはできません  
- 削除対象のアイテムをマークするためのオプションの `DELETED` フィールドを含めることができます 

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

設定の詳細については、[ファイルストレージの統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/)を参照してください。

{% endtab %}
{% endtabs %}

## 連携の仕組み

同期が実行されるたびに、Braze は `UPDATED_AT` が最後に同期された値より後のすべての行を取り込みます。境界のタイムスタンプと同じ値を持つ新しい行がある場合、そのタイムスタンプの行が再同期されることがあります。カタログデータからデータウェアハウスにビューを作成し、同期が実行されるたびに完全にリフレッシュされるソーステーブルを設定することをお勧めします。ビューを使用すれば、クエリを毎回書き直す必要はありません。

例えば、`product_id` と 3 つの追加属性を含む製品データテーブル (`product_catalog_1`) がある場合、以下のビューを同期できます。

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

- 連携からフェッチされたデータは、指定された `id` に基づいて、ターゲットカタログ内のアイテムの作成または更新に使用されます。
- DELETED が `true` に設定されている場合、対応するカタログアイテムが削除されます。
- 同期ではデータポイントは記録されませんが、同期されたすべてのデータはカタログ使用量の合計にカウントされます。この使用量は保存されたデータの総量に基づいて計測されるため、変更されたデータのみを同期することを心配する必要はありません。
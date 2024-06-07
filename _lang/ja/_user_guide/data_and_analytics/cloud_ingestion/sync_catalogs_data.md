---
nav_title: カタログデータの同期と削除
article_title: カタログデータの同期と削除
page_order: 4
page_type: reference
description: "このリファレンス記事では、カタログデータを同期する方法の概要を説明します。"

---

# カタログデータの同期と削除

 
## ステップ 1: 新規カタログの作成

[カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/)用の新しいクラウドデータ取り込み (CDI) の連携を作成する前に、連携に使用する新規カタログを作成するか、既存のカタログを指定する必要があります。新規カタログを作成する方法はいくつかあり、いずれも CDI 連携に使用できます。
- [CSV]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-1-upload-csv) をアップロードする
- [Braze ダッシュボード]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#method-2-create-in-browser)でカタログを作成する
- [カタログ作成エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)を使用してカタログを作成する

カタログスキーマへの変更 (新しいフィールドの追加、フィールドタイプの変更など) は、更新されたデータが CDI を通じて同期される前に、カタログダッシュボードから行う必要があります。データウェアハウスのデータと Braze のスキーマとの競合を避けるために、同期が一時停止されているとき、または実行がスケジュールされていないときにこれらの更新を行うことをお勧めします。

## ステップ 2: クラウドデータ取り込みとカタログデータの連携
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
2. ロール、ウェアハウス、およびユーザーを設定し、適切な権限を付与します。既存の同期からの認証情報をすでに持っている場合はそれらを再利用できますが、必ずアクセスをカタログソーステーブルに拡張してください。
    \`\`\`json
    CREATE ROLE BRAZE\_INGESTION\_ROLE;

    GRANT USAGE ON DATABASE BRAZE\_CLOUD\_PRODUCTION TO ROLE BRAZE\_INGESTION\_ROLE;
    GRANT USAGE ON SCHEMA BRAZE\_CLOUD\_PRODUCTION.INGESTION TO ROLE BRAZE\_INGESTION\_ROLE;
    GRANT SELECT ON TABLE BRAZE\_CLOUD\_PRODUCTION.INGESTION.CATALOGS\_SYNC TO ROLE BRAZE\_INGESTION\_ROLE;

    CREATE WAREHOUSE BRAZE\_INGESTION\_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE\_INGESTION\_WAREHOUSE TO ROLE BRAZE\_INGESTION\_ROLE;

    CREATE USER BRAZE\_INGESTION\_USER;
    GRANT ROLE BRAZE\_INGESTION\_ROLE TO USER BRAZE\_INGESTION\_USER;
    \`\`\`
3. Snowflake アカウントにネットワークポリシーがある場合は、CDI サービスが接続できるように Braze IP を許可リストに登録します。IP のリストについては、「[クラウド データの取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)」を参照してください。
4. Braze ダッシュボードで **[テクノロジーパートナー] > [Snowflake]** に移動し、新規の同期を作成します。
5. 接続の詳細を入力し (または既存の認証情報報を再利用する)、ソーステーブルを入力します。
6. 設定フローのステップ 2 に進み、[カタログ] 同期タイプを選択し、連携名とスケジュールを入力します。連携名は、以前に作成したカタログの名前と**正確に一致する**必要があることに注意してください。
7. 同期頻度を選択し、次のステップに進みます。
8. ダッシュボードに表示されている公開キーを、Snowflake に Braze を接続するために作成したユーザーに追加します。このステップを完了するには、Snowflake で `SECURITYADMIN` 以上のアクセスを持つ人が必要です。 
9. [**テスト接続**] をクリックして、すべてが意図どおりに動作することを確認します。 
10. 同期を保存し、同期されたカタログデータをすべてのパーソナライゼーションのユースケースに使用します。
{% endtab %}
{% tab Redshift %}

1. Redshift でソーステーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。
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
2. ユーザーを設定し、適切な権限を付与します。既存の同期からの認証情報をすでに持っている場合はそれらを再利用できますが、必ずアクセスをカタログソーステーブルに拡張してください。
    {% raw %}
    ```json 
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスに Braze ネットワークへのアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。IP のリストについては、「[クラウド データの取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)」を参照してください。

{% endtab %}
{% tab BigQuery %}

1. オプションで、ソーステーブルを保持する新規のプロジェクトまたはデータセットを設定します。次のフィールドを持ち、CDI 連携に使用するテーブルを 1 つ以上作成します。

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED\_AT | タイムスタンプ | 必須 |
| PAYLOAD | JSON | 必須 |
| ID | 文字列 |必須 |
| DELETED | ブール値 | 任意 |

{:start="2"}

2. ユーザーを設定し、適切な権限を付与します。既存の同期からの認証情報をすでに持っている場合はそれらを再利用できますが、必ずアクセスをカタログソーステーブルに拡張してください。
サービスアカウントには次の権限が必要です。
- BigQuery 接続ユーザー: Braze に接続を許可します。
- BigQuery ユーザー: クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- BigQuery データビューアー: データセットとその内容を表示するためのアクセスを Braze に提供します。
- BigQuery ジョブユーザー: ジョブを実行するためのアクセスを Braze に提供します。<br><br>サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳細については、[キーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これは後で Braze ダッシュボードに更新します。

{:start="3"}
3. ネットワークポリシーを設定している場合は、Braze に Big Query インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、[「クラウド データの取り込み」]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)を参照してください。

{% endtab %}
{% tab Databricks %}

1. Databricks でソース テーブルを設定します。次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。

| フィールド名 | タイプ | モード |
| --- | --- | --- |
| UPDATED\_AT | タイムスタンプ | 必須 |
| PAYLOAD | JSON | 必須 |
| ID | 文字列 |必須 |
| DELETED | ブール値 | 省略 (NULL) 可 |

{:start="2"}

2. Databricks ワークスペースでパーソナルアクセストークンを作成します。

- a. Databricks ユーザー名を選択し、ドロップダウンメニューから [**ユーザー設定**] を選択します。

- b. [**アクセストークン**] タブで、[**新しいトークンの生成**] を選択します。

- c. 「Braze CDI」など、このトークンの識別に役立つコメントを入力します。 

- d. [**有効期間 (日)**] ボックスを空白のままにして、トークンの有効期間を有効期間なしに変更します。[**生成**] を選択します。

- e. 表示されたトークンをコピーして、[**完了**] を選択します。 

- f. 認証情報の作成ステップで Braze ダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

{:start="3"}
3. ネットワークポリシーを設定している場合は、Brazeに Databricks インスタンスへのネットワークアクセスを許可する必要があります。IP のリストについては、「{:start="3"}クラウド データの取り込み{:start="3"}」を参照してください。

{% endtab %}
{% endtabs %}

## 連携の仕組み
同期が実行されるたびに、Braze は、`UPDATED_AT` が最後に同期されたタイムスタンプ以降にあるすべての行を取得します。同期が実行されるたびに完全に更新されるソーステーブルを設定するには、カタログデータからビューを作成することをお勧めします。例えば、`product_id`、`price` を含む製品データ (`product_catalog_1`) のテーブルと 3 つの追加属性がある場合、以下のビューを同期できます。

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
{% endtabs %}

- 連携からフェッチされたデータは、指定した `id` に基づいて、ターゲットカタログ内のアイテムの作成または更新に使用されます。
- DELETED が `true` に設定されている場合、対応するカタログアイテムが削除されます。
- 同期でデータポイントは消費されませんが、同期されたすべてのデータはカタログの合計使用量にカウントされます。この使用量は保存されている合計データに基づいて測定されるため、変更されたデータのみの同期について心配する必要はありません。

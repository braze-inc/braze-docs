---
nav_title: ゼロコピーパーソナライゼーション
article_title: CDIを用いたゼロコピーパーソナライゼーション
page_order: 4
page_type: reference
description: "このページでは、CDIを使用してBrazeキャンバスをトリガーする方法の概要を説明する。"
---

# CDIを用いたゼロコピーパーソナライゼーション

> CDIを使ってキャンバストリガーを同期する方法を学び、ゼロコピーパーソナライゼーションを実現する。この機能は、データストレージソリューションからユーザー固有の情報にアクセスし、それを送信先のキャンバスに渡す。Canvasステップには、Brazeユーザープロファイルに永続化されないパーソナライゼーションフィールドを任意で含めることができる。

{% multi_lang_include early_access_beta_alert.md feature='CDI Canvas triggers' %}

## キャンバスの同期がトリガーされる

### クイックスタートのステップ

Braze CDIに既に慣れている場合、キャンバストリガーの同期設定は[ユーザーデータCDI統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)のプロセスとほぼ同様だが、以下の注意点がある：

- 外部IDまたはユーザーエイリアス識別子のみがサポートされている。メールと電話番号はサポートされていない識別子だ。  
- 既存のBrazeユーザーのみ同期できる。新規ユーザーは作成できない。  
- `properties` 列`payload`を置き換える。これは、パーソナライゼーション用のキャンバスエントリプロパティとして使用したいフィールドのJSON文字列だ。

始めるには、新しい同期を作成する際に**「Canvas Triggers**」データタイプを選択する。

### キャンバスのトリガーを使用する 

#### ステップ 1: Canvasトリガー用のデータソースを設定する

{% tabs %}
{% tab Snowflake %}

##### ステップ1.1：Snowflakeでソーステーブルを設定する

次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。  

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

データベース、スキーマ、テーブルの名前は自由に付けられるが、列名は前述の定義と一致させる必要がある。

* `UPDATED_AT`:この行が更新されたか、テーブルに追加された時刻。前回の同期以降に追加または更新された行のみが同期される。  
* ユーザー識別子列として、いずれか一方`external_id``alias_label`、あるいは`alias_name`両方を使用する。これらは、Canvasメッセージングをトリガーしたいユーザーを識別するものである。  
  * `EXTERNAL_ID`:ユーザーを識別し、キャンバスにログインさせる。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` そして`ALIAS_LABEL`：これらの列はユーザーエイリアスオブジェクトを作成する。`alias_name`は一意の識別子であるべきであり、 はエイリアスの種類を指定する`alias_label`。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name を1つしか持つことができません。  
* `PROPERTIES`:キャンバス内でパーソナライゼーションプロパティとして利用可能なフィールドのJSON文字列。これはユーザー固有の情報を含んでいるべきだ。

{% alert note %}
プロパティは全ての行やユーザーに対して必須ではない。ただし、プロパティの値は有効なJSON文字列でなければならない。行にプロパティがない場合は空の`{}`文字列を入力せよ。
{% endalert %}

##### ステップ1.2：認証情報を設定する

役割、倉庫、ユーザーを設定し、適切な権限を付与する。既存の同期から認証情報を既に持っている場合、それを再利用できる。ただし、キャンバストリガーのソーステーブルへのアクセス権限を必ず拡張すること。  

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### ステップ1.3：ネットワークポリシーを設定する

アカウントにネットワークポリシーが設定されている場合、CDIサービス接続のイネーブルメントを行うためにBrazeのIPアドレスを許可リストに追加せよ。IPアドレスの一覧については、[クラウドデータ取り込みを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional)参照せよ。  

{% endtab %}
{% tab Redshift %}

##### ステップ1.1：Redshiftでソーステーブルを設定する

次の例の名前を使用することも、独自のデータベース、スキーマ、およびテーブルの名前を選択することもできます。テーブルの代わりに、ビューまたはマテリアライズドビューを使用することもできます。

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

データベース、スキーマ、テーブルの名前は自由に付けられるが、列名は前述の定義と一致させる必要がある。

* `UPDATED_AT`:この行が更新されたか、テーブルに追加された時刻。前回の同期以降に追加または更新された行のみが同期される。  
* ユーザー識別子列として、いずれか一方`external_id``alias_label`、あるいは`alias_name`両方を使用する。これらは、Canvasメッセージングをトリガーしたいユーザーを識別するものである。  
  * `EXTERNAL_ID`:ユーザーを識別し、キャンバスにログインさせる。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` そして`ALIAS_LABEL`：これらの列はユーザーエイリアスオブジェクトを作成する。`alias_name`は一意の識別子であるべきであり、 はエイリアスの種類を指定するalias_label。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。  
* `PROPERTIES`:キャンバス内でパーソナライゼーションプロパティとして利用可能なフィールドのJSON文字列。これはユーザー固有の情報を含んでいるべきだ。

{% alert note %}
プロパティは全ての行やユーザーに対して必須ではない。ただし、プロパティの値は有効なJSON文字列でなければならない。行にプロパティがない場合は空の`{}`文字列を入力せよ。
{% endalert %}

##### ステップ1.2：認証情報を設定する

ロール、ウェアハウス、およびユーザーを設定し、適切な権限を付与します。既存の同期から認証情報を既に持っている場合、それを再利用できる。ただし、キャンバストリガーのソーステーブルへのアクセス権限を必ず拡張すること。

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### ステップ1.3：ネットワークポリシーを設定する 

アカウントにネットワークポリシーが設定されている場合、CDIサービス接続のイネーブルメントを行うためにBrazeのIPアドレスを許可リストに追加せよ。IPアドレスの一覧については、[クラウドデータ取り込みを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips)参照せよ。

{% endtab %}
{% tab BigQuery %}

##### ステップ1.1：ソーステーブル用の新しいプロジェクトまたはデータセットを作成する（任意）

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### ステップ1.2：BigQueryでソーステーブルを設定する
ソーステーブルを作成する際は、以下の内容を参照すること。  

| フィールド名 | タイプ | 必須かどうか | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | タイムスタンプ | はい | 
| **`PROPERTIES`** | JSON | はい | 
| **`EXTERNAL_ID`** | 文字列 | NULL 許容 | 
| **`ALIAS_NAME`** | 文字列 | NULL 許容 | 
| **`ALIAS_LABEL`** | 文字列 | NULL 許容 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
プロパティは全ての行やユーザーに対して必須ではない。ただし、プロパティの値は有効なJSON文字列でなければならない。行にプロパティがない場合は空の`{}`文字列を入力せよ。
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### ステップ1.3：認証情報を設定する

ユーザーを作成し、権限を付与する。別の同期から既に認証情報を持っている場合、キャンバストリガーテーブルへのアクセス権がある限り、それらを再利用できる。

| 権限 | 目的 |
| :---- | :---- |
| BigQuery接続ユーザー | Brazeが接続することを許可する。 |
| BigQueryユーザー | Brazeがクエリを実行し、メタデータを読み取り、テーブルを一覧表示することを許可する。 |
| BigQuery データビューア | Brazeがデータセットとコンテンツを閲覧することを許可する。 |
| BigQueryジョブユーザー | Brazeがジョブを実行することを許可する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

権限を許可した後、JSONキーを生成する。[キーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)については、該当する手順を参照せよ。後でBrazeのダッシュボードにアップロードするんだ。

##### ステップ1.4:ネットワークポリシーを設定する 
アカウントにネットワークポリシーが設定されている場合、CDIサービス接続のイネーブルメントを行うためにBrazeのIPアドレスを許可リストに追加せよ。IPアドレスの一覧については、[クラウドデータ取り込みを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips)参照せよ。

{% endtab %}
{% tab Databricks %}

##### ステップ1.1：ソーステーブルのカタログまたはスキーマを作成する。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### ステップ1.2：Databricksでソーステーブルを設定する

ソーステーブルを作成する際は、以下の内容を参照すること。

| フィールド名 | タイプ | 必須かどうか |
| :---- | :---- | :---- |
| `UPDATED_AT` | タイムスタンプ | はい |
| `PROPERTIES` | JSON | はい |
| `EXTERNAL_ID` | 文字列 |  NULL 許容 |
| `ALIAS_NAME` | 文字列 | NULL 許容 |
| `ALIAS_LABEL` | 文字列 | NULL 許容 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

スキーマとテーブルの名前は自由に付けられるが、列名は前の定義と一致させる必要がある。

* `UPDATED_AT`:この行が更新されたか、テーブルに追加された時刻。前回の同期以降に追加または更新された行のみが同期される。  
* ユーザー識別子列として、いずれか一方`external_id``alias_label`、あるいは`alias_name`両方を使用する。これらは、Canvasメッセージングをトリガーしたいユーザーを識別するものである。  
  * `EXTERNAL_ID`:ユーザーを識別し、キャンバスにログインさせる。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` そして`ALIAS_LABEL`：これらの列はユーザーエイリアスオブジェクトを作成する。`alias_name`は一意の識別子であるべきであり、 はエイリアスの種類を指定する`alias_label`。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name を1つしか持つことができません。  
* `PROPERTIES`:キャンバス内でパーソナライゼーションプロパティとして利用可能にするフィールドの文字列または構造体。これはユーザー固有の情報を含んでいるべきだ。

{% alert note %}
プロパティは全ての行やユーザーに対して必須ではない。ただし、プロパティの値は有効なJSON文字列でなければならない。行にプロパティがない場合は空の`{}`文字列を入力せよ。
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### ステップ1.3：認証情報を設定する 

Databricksで個人用トークンを作成する：

1. ユーザー名を選択し、次に**ユーザー設定**を選択する**。**  
2. アクセストークンのタブで、**新しいトークンを生成する**を選択する**。**  
3. トークンを識別するための識別子を追加する。例えば「Braze CDI」など。  
4. 有効期限を無期限にするには**「有効期限（日数）**」を空白のままにし、「**生成」**を選択する。  
5. トークンをコピーして安全に保存し、Brazeダッシュボードで使用する。

##### ステップ1.4:ネットワークポリシーを設定する 

アカウントにネットワークポリシーが設定されている場合、CDIサービス接続のイネーブルメントを行うためにBrazeのIPアドレスを許可リストに追加せよ。IPアドレスの一覧については、[クラウドデータ取り込みを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips)参照せよ。

{% endtab %}
{% tab Fabric %}

##### ステップ1.1：Fabricでソーステーブルを設定する

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### ステップ1.2：認証情報を設定する 

サービスプリンシパルを作成し、権限を付与する。別の同期から既に認証情報を持っているなら、それを再利用できる。ただし、アカウントテーブルへのアクセス権があることを確認すること。

##### ステップ1.3：ネットワークポリシーを設定する 

アカウントにネットワークポリシーが設定されている場合、CDIサービス接続のイネーブルメントを行うためにBrazeのIPアドレスを許可リストに追加せよ。IPアドレスの一覧については、[クラウドデータ取り込みを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional)参照せよ。

{% endtab %}
{% tab File Storage %}

ファイルストレージからキャンバストリガーを同期するには、以下のフィールドを含むソースファイルを作成する。

| フィールド | 必須 | 説明 |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | そうだ、一つか、`external_id`あるいは`alias_name`、そして `alias_label` | これは更新したいユーザーの識別子である。これは Braze で使用されている `external_id` 値と一致しなければなりません。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | そうだ、一つか、`external_id`あるいは`alias_name`、そして `alias_label` | これら2つの列は、ユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。 |
| `PROPERTIES` | はい | キャンバス内でパーソナライゼーションプロパティとして利用可能なフィールドのJSON文字列。これはユーザー固有の情報を含んでいるべきだ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
ファイル名はAWSの規則に従い、一意でなければならない。一意性を確保するためにタイムスタンプを追加する。Amazon S3の同期に関する詳細は、[ファイルストレージの統合を](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations)参照せよ。
{% endalert %}

{% endtab %}
{% endtabs %}

#### ステップ 2:送信先のキャンバスを設定する

1. Canvasトリガー用の送信先のキャンバスを設定する。新しいAPIトリガー付きキャンバスを作成するか、既存のものを選択する。APIトリガーによる配信スケジュールタイプでキャンバスを作成する方法については[、エントリスケジュールタイプ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types)を参照せよ。
2. APIトリガーによる配信スケジュールタイプを選択した後、Canvasの設定を続けてCanvasを構築する。キャンバスは、単純な単一メッセージ送信から、複数のステップを含む複雑な顧客ワークフローまで様々だ。
3. キャンバスステップ内で、ソーステーブルから同期する予定の属性フィールドを用いて、[キャンバスエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)でメッセージをパーソナライズする。
  * 例えば、ステップ1でプロパティフィールドを計測した場合`account_balance`、メッセージをパーソナライズするには以下のLiquidテンプレートを使用する：`\{\{canvas_entry_properties.\$\{account_balance\}\}\}`
5. キャンバスを作成したら、それを起動して[ステップ3](#step-3-create-your-zero-copy-sync)に進め。

#### ステップ 3:ゼロコピー同期を作成する

ソースの設定が完了し、送信先のキャンバスが起動したら、新しいデータ同期を作成する：

1. Brazeで、**データ設定**＞**クラウドデータ取り込み**に移動する。
1. 接続の詳細を入力して接続を設定する（または既存の認証情報を再利用する）。そして[ステップ1](#step-1-set-up-data-source-for-canvas-triggers)で指定したソーステーブルを指定する。
2. 統合に名前を付ける。
3. **キャンバストリガーの**データ型を選択する。
4. [ステップ2](#step-2-configure-your-destination-canvas)から送信先のキャンバスを選ぶ。
5. 同期頻度を選べ。
6. 通知設定を有効にする。
7. **接続テスト**を選択して、すべてが期待通りに動作することを確認する。Snowflakeに接続する場合、まずダッシュボードに表示されている公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加する。このステップを完了するには、Snowflakeで**SECURITYADMIN**以上のアクセス権限が必要だ。 
8. 同期を保存して、キャンバストリガーの同期を開始する。

同期が実行されると、ソーステーブルのユーザーがキャンバスに入力し始める。Canvasの分析機能とクラウドデータ取り込みの同期ログページを使って、パフォーマンスを監視する。

{% alert tip %}  
予期しない送信を避けるため、設定全体（同期動作からキャンバスの設定まで）を見直せ。レート制限、フリークエンシーキャップ、セグメンテーションフィルターなどのキャンバス設定により、メッセージ配信をさらに精緻化できる。<br><br>本番環境でのユースケースを実装する前に、小規模なテストオーディエンスやテストオーディエンスで試運転を行うことを推奨する。
{% endalert %}

### 考慮事項

CDI Canvasのトリガーは、REST APIのレート制限を利用する`/canvas/trigger/send`。このエンドポイントをCDI CanvasトリガーとREST API統合と同時に使用する場合、その合計使用量がレート制限にカウントされることを想定せよ。

CDIキャンバスにおけるトリガーは現在早期アクセス中であるため、以下の詳細を考慮すること。

* ワークスペースごとに最大5つのアクティブなキャンバストリガー同期  
* 各同期実行では、最大で1時間あたり約375万人のユーザーを、それぞれの送信先に追加する。  
  * 以下の場合には、ソースからキャンバスへのエントリ時間が長くなることを覚悟しておけ：  
    * 1回の同期実行で375万人以上のユーザーを同期する。  
    * REST APIの[レート制限が]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)既に飽和状態にある場合[、]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)CDI [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)キャンバストリガーを使用する。
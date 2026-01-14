---
nav_title: ゼロコピー・パーソナライゼーション
article_title: CDIを使用したゼロコピーパーソナライゼーション
page_order: 4
page_type: reference
description: "このページでは、CDIを使ってBraze Canvasesをトリガーする方法の概要を説明する。"
---

# CDIを使用したゼロコピーパーソナライゼーション

> CDIを使用してキャンバスのトリガーを同期させ、ゼロコピーパーソナライゼーションを実現する方法を学習する。この機能は、データストレージソリューションからユーザー固有の情報にアクセスし、送信先のキャンバスに渡す。キャンバスステップには、Brazeユーザープロファイルに永続化されないパーソナライゼーションフィールドをオプションで含めることができる。

{% alert important %}
CDIキャンバスのトリガーは現在早期アクセス中である。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## キャンバスのトリガーを同期する

### クイックスタートのステップ

すでにBraze CDIに慣れ親しんでいる場合、キャンバストリガー同期のセットアップは、以下の注意点を除き、[ユーザーデータCDI統合の]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)プロセスに忠実に従うことに注意されたい：

- 外部IDまたはユーザーエイリアス識別子のみがサポートされる。メールや電話番号は識別子としてサポートされていない。  
- 同期できるのは既存のBrazeユーザーだけである。新しいユーザーを作成することはできない。  
- `properties` `payload` 。これは、パーソナライゼーションのためのキャンバスエントリープロパティとして使用したいフィールドのJSON文字列である。

はじめに、新しいシンクを作成するときに、**キャンバストリガーの**データタイプを選択する。

### キャンバストリガーを使う 

#### ステップ 1: キャンバストリガーのデータソースを設定する

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

データベース、スキーマ、テーブルには好きな名前をつけることができるが、カラム名は前述の定義と一致させる必要がある。

* `UPDATED_AT`:この行が更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期される。  
* `external_id` 、または`alias_name` 、`alias_label` のいずれかをユーザー識別子列とする。これらは、キャンバスのメッセージングをトリガーしたいユーザーを識別する。  
  * `EXTERNAL_ID`:キャンバスに入るユーザーを識別子で指定する。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` と`ALIAS_LABEL` ：これらのカラムはユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name を1つしか持つことができません。  
* `PROPERTIES`:キャンバスでパーソナライゼーションのプロパティとして利用できるようにするフィールドのJSON文字列。これにはユーザー固有の情報が含まれているはずだ。

{% alert note %}
プロパティは、すべての行やユーザーに必要なわけではない。ただし、プロパティ値は有効なJSON文字列でなければならない。行のプロパティがない場合は、空の`{}` 文字列を入力する。
{% endalert %}

##### ステップ1.2：認証情報を設定する

ロール、ウェアハウス、ユーザーを設定し、適切な権限を与える。既存のシンクの認証情報をすでに持っている場合は、それを再利用することができるが、キャンバストリガーのソーステーブルへのアクセスを拡張することを確認する。  

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

アカウントにネットワークポリシーがある場合は、CDIサービス接続をイネーブルメントにするためにBraze IPを許可する。IPのリストについては、[Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional)参照のこと。  

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

データベース、スキーマ、テーブルには好きな名前をつけることができるが、カラム名は前述の定義と一致させる必要がある。

* `UPDATED_AT`:この行が更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期される。  
* `external_id` 、または`alias_name` 、`alias_label` のいずれかをユーザー識別子列とする。これらは、キャンバスのメッセージングをトリガーしたいユーザーを識別する。  
  * `EXTERNAL_ID`:キャンバスに入るユーザーを識別子で指定する。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` と`ALIAS_LABEL` ：これらのカラムはユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、alias_label はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。  
* `PROPERTIES`:キャンバスでパーソナライゼーションのプロパティとして利用できるようにするフィールドのJSON文字列。これにはユーザー固有の情報が含まれているはずだ。

{% alert note %}
プロパティは、すべての行やユーザーに必要なわけではない。ただし、プロパティ値は有効なJSON文字列でなければならない。行のプロパティがない場合は、空の`{}` 文字列を入力する。
{% endalert %}

##### ステップ1.2：認証情報を設定する

ロール、ウェアハウス、およびユーザーを設定し、適切な権限を付与します。既存のシンクの認証情報をすでに持っている場合は、それを再利用することができるが、キャンバストリガーのソーステーブルへのアクセスを拡張することを確認する。

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### ステップ1.3：ネットワークポリシーを設定する 

アカウントにネットワークポリシーがある場合は、CDIサービス接続をイネーブルメントにするためにBraze IPを許可する。IPのリストについては、[Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips)参照のこと。

{% endtab %}
{% tab BigQuery %}

##### ステップ1.1：ソース・テーブル用に新しいプロジェクトまたはデータセットを作成する（オプション）

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### ステップ1.2：BigQueryでソーステーブルを設定する
ソース・テーブルを作成する際には、以下を参照のこと：  

| フィールド名 | タイプ | 必須かどうか | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | タイムスタンプ | はい | 
| **`PROPERTIES`** | JSON | はい | 
| **`EXTERNAL_ID`** | 文字列 | NULL 許容 | 
| **`ALIAS_NAME`** | 文字列 | NULL 許容 | 
| **`ALIAS_LABEL`** | 文字列 | NULL 許容 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
プロパティは、すべての行やユーザーに必要なわけではない。ただし、プロパティ値は有効なJSON文字列でなければならない。行のプロパティがない場合は、空の`{}` 文字列を入力する。
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

ユーザーを作成し、権限を与える。すでに別のシンクの認証情報を持っている場合は、キャンバストリガー・テーブルへのアクセス権を持っている限り、その認証情報を再利用することができる。

| 権限 | 目的 |
| :---- | :---- |
| BigQuery接続ユーザー | Brazeの接続を許可する。 |
| BigQueryユーザー | Brazeがクエリーを実行し、メタデータを読み、テーブルを一覧できるようにする。 |
| BigQueryデータビューアー | Brazeがデータセットとコンテンツを閲覧できるようにする。 |
| BigQueryジョブユーザー | Brazeがジョブを実行できるようにする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

権限を付与したら、JSONキーを生成する。手順については、[キーの作成と削除を](https://cloud.google.com/iam/docs/keys-create-delete)参照のこと。後でダッシュボードにアップロードする。

##### ステップ1.4:ネットワークポリシーを設定する 
アカウントにネットワークポリシーがある場合は、CDIサービス接続をイネーブルメントにするためにBraze IPを許可する。IPのリストについては、[Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips)参照のこと。

{% endtab %}
{% tab Databricks %}

##### ステップ1.1：ソース・テーブルのカタログまたはスキーマを作成する。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### ステップ1.2：Databricksでソーステーブルを設定する

ソース・テーブルを作成する際には、以下を参照のこと：

| フィールド名 | タイプ | required |
| :---- | :---- | :---- |
| `UPDATED_AT` | タイムスタンプ | はい |
| `PROPERTIES` | JSON | はい |
| `EXTERNAL_ID` | 文字列 |  NULL 許容 |
| `ALIAS_NAME` | 文字列 | NULL 許容 |
| `ALIAS_LABEL` | 文字列 | NULL 許容 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

スキーマとテーブルには好きな名前をつけることができるが、カラム名は前述の定義と一致させる必要がある。

* `UPDATED_AT`:この行が更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期される。  
* `external_id` 、または`alias_name` 、`alias_label` のいずれかをユーザー識別子列とする。これらは、キャンバスのメッセージングをトリガーしたいユーザーを識別する。  
  * `EXTERNAL_ID`:キャンバスに入るユーザーを識別子で指定する。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` と`ALIAS_LABEL` ：これらのカラムはユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name を1つしか持つことができません。  
* `PROPERTIES`:キャンバスでパーソナライゼーションプロパティとして利用できるようにするフィールドの文字列または構造体。これにはユーザー固有の情報が含まれているはずだ。

{% alert note %}
プロパティは、すべての行やユーザーに必要なわけではない。ただし、プロパティ値は有効なJSON文字列でなければならない。行のプロパティがない場合は、空の`{}` 文字列を入力する。
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

Databricksでパーソナアクセストークンを作成する：

1. ユーザー名を選択し、**ユーザー設定を**選択する**。**  
2. **アクセストークンタブで**、**Generate new tokenを**選択する。  
3. Braze CDI」のように、トークンを識別するためのコメントを追加する。  
4. **Lifetime(日数)を**空白のままにして、有効期限なしとし、**Generateを**選択する。  
5. トークンをコピーし、Brazeダッシュボードで使用できるように安全に保存する。

##### ステップ1.4:ネットワークポリシーを設定する 

アカウントにネットワークポリシーがある場合は、CDIサービス接続をイネーブルメントにするためにBraze IPを許可する。IPのリストについては、[Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips)参照のこと。

{% endtab %}
{% tab Fabric %}

##### ステップ1.1：ファブリックでソーステーブルを設定する

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

サービスプリンシパルを作成し、権限を付与する。すでに別のシンクの認証情報を持っている場合は、それを再利用することができる。

##### ステップ1.3：ネットワークポリシーを設定する 

アカウントにネットワークポリシーがある場合は、CDIサービス接続をイネーブルメントにするためにBraze IPを許可する。IPのリストについては、[Cloud Data Ingestionを]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional)参照のこと。

{% endtab %}
{% tab File Storage %}

ファイルストレージからキャンバストリガーを同期するには、以下のフィールドを持つソースファイルを作成する。

| フィールド | 必須 | 説明 |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | はい、`external_id` または`alias_name` のどちらかである。 `alias_label` | これは更新したいユーザーの識別子である。これは Braze で使用されている `external_id` 値と一致しなければなりません。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | はい、`external_id` または`alias_name` のどちらか1つである。 `alias_label` | これら2つの列は、ユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。 |
| `PROPERTIES` | はい | キャンバスのパーソナライゼーションプロパティとして利用可能なフィールドのJSON文字列。これにはユーザー固有の情報が含まれているはずだ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
ファイル名はAWSのルールに従い、一意でなければならない。タイムスタンプを付加することで、一意性を確保する。Amazon S3の同期については、[ファイル・ストレージの統合を](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations)参照のこと。
{% endalert %}

{% endtab %}
{% endtabs %}

#### ステップ 2:送信先キャンバスを設定する

1. 送信先のキャンバスをキャンバスのトリガーに設定する。新しいキャンバスを作成するか、既存のAPIトリガーキャンバスを選択する。APIトリガー配信スケジュールタイプでキャンバスを作成する方法については、[エントリースケジュールタイプを]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types)参照のこと。
2. APIトリガー配信スケジュールタイプを選択した後、キャンバスのセットアップを続行し、キャンバスを構築する。キャンバスは、単純なシングルメッセージの送信から、複数のステップを持つ複雑な顧客ワークフローまで、幅広く対応できる。
3. キャンバス・ステップの中で、[キャンバス・エントリー・プロパティを使って]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)、ソース・テーブルから同期する予定のプロパティ・フィールドでメッセージをパーソナライズさせる。
  * 例えば、ステップ1で、`account_balance` のプロパティフィールドをインストルメント化した場合、メッセージをパーソナライズするために、次のようなLiquidテンプレートを使うことになる：`\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. キャンバスを構築したら、それを起動し、[ステップ](#step-3-create-your-zero-copy-sync)3に進む。

#### ステップ 3:ゼロコピー・シンクを作成する

データソースのセットアップが完了し、送信先キャンバスが起動したら、新しいデータシンクを作成する：

1. Brazeで、**Data Settings**>**Cloud Data Ingestion**に進む。
1. 接続の詳細（または既存の認証情報を再利用）と[ステップ](#step-1-set-up-data-source-for-canvas-triggers)1のソース・テーブルを入力して接続を設定する。
2. 統合名を記入する。
3. **キャンバストリガーの**データタイプを選択する。
4. [ステップ](#step-2-configure-your-destination-canvas)2で）送信先のキャンバスを選択する。
5. 同期周波数を選択する。
6. 通知の設定をする。
7. **Test Connection（接続のテスト）**」を選択し、すべてが期待通りに動作することを確認する。Snowflakeに接続する場合は、まずダッシュボードに表示される公開キーを、Braze用に作成したユーザーに追加してSnowflakeに接続する。このステップを完了するには、**SnowflakeのSECURITYADMIN**アクセス以上が必要である。 
8. 同期を保存してキャンバストリガーの同期を開始する。

同期が実行されると、ソーステーブルのユーザーがキャンバスに入り始める。パフォーマンスを監視するには、キャンバス分析とCloud Data Ingestion sync logsページを使用する。

{% alert tip %}  
予期せぬ送信を避けるために、設定全体（同期の動作からキャンバスの設定まで）を見直す。レート制限、フリークエンシーキャップ、セグメンテーションフィルターなどのキャンバス設定は、メッセージ配信をさらに洗練させることができる。<br><br>本番のユースケースを実装する前に、少人数またはテストオーディエンスで試運転を行うことをお勧めする。
{% endalert %}

### 考慮事項

CDI キャンバスのトリガーは`/canvas/trigger/send` の REST API のレート制限を利用する。このエンドポイントをCDIキャンバストリガーとREST API統合と同時に使用している場合、合計使用量はレート制限にカウントされる。

CDIキャンバスのトリガーは早期アクセスであるが、以下の詳細を考慮されたい：

* ワークスペースごとに最大5つのアクティブなキャンバス・トリガー・シンクが可能。  
* 各同期の実行は、1時間あたり最大約375万人のユーザーをそれぞれの送信先キャンバスに入力する。  
  * 次のような場合、ソースからキャンバスへのエントリ時間が長くなる：  
    * 1回のシンクで375万人以上のユーザーをシンクする。  
    * [ `/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) REST APIのレート制限に達している場合、CDIキャンバストリガーを使用する。
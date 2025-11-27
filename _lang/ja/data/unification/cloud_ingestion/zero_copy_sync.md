---
nav_title: ゼロコピーのカスタマイズ
article_title: CDIによるゼロコピーパーソナライゼーション
page_order: 4
page_type: reference
description: "ここでは、CDI を使用してキャンバスをトリガー Brazeする方法について説明します。"
---

# CDIによるゼロコピーパーソナライゼーション

> CDI を使用してゼロコピーパーソナライゼーションでキャンバストリガーを同期する方法について説明します。この機能は、データストレージソリューションからユーザー固有の情報にアクセスし、それを送信先キャンバスに渡します。キャンバスステップs には、オプションで、Braze ユーザープロファイルs に保持されていないパーソナライゼーション フィールドs を含めることができます。

{% alert important %}
CDI Canvas トリガーは、現在、初期段階にあります。早期アクセスへの参加に興味がある方は、Brazeのアカウントマネージャーに連絡を。
{% endalert %}

## キャンバストリガーの同期

### クイックスタートステップs

Braze CDI にすでに精通している場合は、キャンバストリガーシンクの設定が[ユーザー-data CDI 統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) の処理に厳密に従うことに注意してください。

- 外部ID またはユーザー別名識別子のみがサポートされます。メールおよび電話番号は、サポートされていない識別子sです。  
- 同期できるのは、すでに存在するBraze ユーザーs のみです。新しいユーザーsは作成できません。  
- `properties` `payload` 列を置き換えます。これは、パーソナライゼーションのキャンバスエントリプロパティーとして使用するフィールドのJSON ストリングです。

開始するには、新しい同期の作成時に**Canvas Triggers**データ型を選択します。

### カンバストリガーの使用 

#### ステップ 1: キャンバストリガーのデータソースを設定する

{% tabs %}
{% tab Snowflake %}

##### ステップ1.1：Snowflake でのソーステーブルの設定

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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

* `UPDATED_AT`:この行が更新dであったか、テーブルに追加された時刻。最後の同期以降に追加または更新された行のみが同期されます。  
* ユーザー 識別子列として`external_id` または`alias_name` と`alias_label` のいずれかを指定します。これらは、キャンバスメッセージングをトリガーするユーザーを識別します。  
  * `EXTERNAL_ID`:キャンバスに入力するユーザーを指定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` と `ALIAS_LABEL`これらの列はユーザー別名オブジェクトを作成します。`alias_name` は一意の識別子で、`alias_label` は別名の種類を指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name を1つしか持つことができません。  
* `PROPERTIES`:キャンバスでパーソナライゼーションプロパティーとして使用できるようにするフィールドs のJSON ストリング。これには、ユーザー固有の情報が含まれます。

{% alert note %}
プロパティーは、すべての行またはユーザーに必要なわけではありません。ただし、プロパティ値は有効なJSON 文字列である必要があります。行のプロパティがない場合は、空の`{}` 文字列を入力します。
{% endalert %}

##### ステップ1.2：認証情報の設定

ロール、ウェアハウス、およびユーザーを設定し、適切な権限を付与します。既存の同期からすでに認証情報s がある場合は、それらを再利用できますが、必ずキャンバストリガーs のソーステーブルへのアクセスを拡張してください。  

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

##### ステップ1.3：ネットワークポリシーの設定

アカウントにネットワークポリシーがある場合は、BrazeIP を許可してCDI サービスコネクションを有効にします。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional)を参照してください。  

{% endtab %}
{% tab Redshift %}

##### ステップ1.1：Redshift でソーステーブルを設定する

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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

* `UPDATED_AT`:この行が更新dであったか、テーブルに追加された時刻。最後の同期以降に追加または更新された行のみが同期されます。  
* ユーザー 識別子列として`external_id` または`alias_name` と`alias_label` のいずれかを指定します。これらは、キャンバスメッセージングをトリガーするユーザーを識別します。  
  * `EXTERNAL_ID`:キャンバスに入力するユーザーを指定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` と `ALIAS_LABEL`これらの列はユーザー別名オブジェクトを作成します。`alias_name` は一意の識別子で、alias_label は別名の種類を指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。  
* `PROPERTIES`:キャンバスでパーソナライゼーションプロパティーとして使用できるようにするフィールドs のJSON ストリング。これには、ユーザー固有の情報が含まれます。

{% alert note %}
プロパティーは、すべての行またはユーザーに必要なわけではありません。ただし、プロパティ値は有効なJSON 文字列です。行のプロパティがない場合は、空の`{}` 文字列を入力します。
{% endalert %}

##### ステップ1.2：認証情報の設定

ロール、ウェアハウス、およびユーザーを設定し、適切な権限を付与します。既存の同期からすでに認証情報s がある場合は、それらを再利用できますが、必ずキャンバストリガーs のソーステーブルへのアクセスを拡張してください。

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### ステップ1.3：ネットワークポリシーの設定 

アカウントにネットワークポリシーがある場合は、BrazeIP を許可してCDI サービスコネクションを有効にします。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips)を参照してください。

{% endtab %}
{% tab BigQuery %}

##### ステップ1.1：ソーステーブルの新しいプロジェクトまたはデータセットを作成する(オプション)

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### ステップ1.2：BigQuery でのソーステーブルの設定
ソーステーブルを作成する場合は、次を参照してください。  

| フィールド名 | タイプ | 必須かどうか | 
| :---- | :---- | :---- | 
| **`UPDATED_AT`** | タイムスタンプ | はい | 
| **`PROPERTIES`** | JSON | はい | 
| **`EXTERNAL_ID`** | 文字列 | NULL 許容 | 
| **`ALIAS_NAME`** | 文字列 | NULL 許容 | 
| **`ALIAS_LABEL`** | 文字列 | NULL 許容 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
プロパティーは、すべての行またはユーザーに必要なわけではありません。ただし、プロパティ値は有効なJSON 文字列です。行のプロパティがない場合は、空の`{}` 文字列を入力します。
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

##### ステップ1.3：認証情報の設定

ユーザーを作成し、権限を付与します。すでに別の同期の認証情報がある場合は、キャンバス トリガー s テーブルにアクセスできる限り、それらを再利用できます。

| 権限 | 目的 |
| :---- | :---- |
| BigQuery 接続ユーザー: | Brazeの接続を許可します。 |
| BigQuery ユーザー: | クエリーの実行、メタデータの読み取り、およびテーブルの一覧表示をBrazeに許可します。 |
| BigQuery データビューアー: | Brazeがデータセットとコンテンツを表示できるようにします。 |
| BigQuery ジョブユーザー: | Brazeがジョブを実行できるようにします。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

権限を付与した後、JSON キーを生成します。手順については、[キーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。後でBraze ダッシュボードにアップロードします。

##### ステップ1.4:ネットワークポリシーの設定 
アカウントにネットワークポリシーがある場合は、BrazeIP を許可してCDI サービスコネクションを有効にします。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips)を参照してください。

{% endtab %}
{% tab Databricks %}

##### ステップ1.1：ソーステーブルのカタログまたはスキーマを登録します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### ステップ1.2：Databricks でのソーステーブルの設定

ソーステーブルを作成する場合は、次を参照してください。

| フィールド名 | タイプ | required |
| :---- | :---- | :---- |
| `UPDATED_AT` | タイムスタンプ | はい |
| `PROPERTIES` | JSON | はい |
| `EXTERNAL_ID` | 文字列 |  NULL 許容 |
| `ALIAS_NAME` | 文字列 | NULL 許容 |
| `ALIAS_LABEL` | 文字列 | NULL 許容 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

スキーマとテーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

* `UPDATED_AT`:この行が更新dであったか、テーブルに追加された時刻。最後の同期以降に追加または更新された行のみが同期されます。  
* ユーザー 識別子列として`external_id` または`alias_name` と`alias_label` のいずれかを指定します。これらは、キャンバスメッセージングをトリガーするユーザーを識別します。  
  * `EXTERNAL_ID`:キャンバスに入力するユーザーを指定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。  
  * `ALIAS_NAME` と `ALIAS_LABEL`これらの列はユーザー別名オブジェクトを作成します。`alias_name` は一意の識別子で、`alias_label` は別名の種類を指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに alias_name を1つしか持つことができません。  
* `PROPERTIES`:フィールドs のストリングまたは構造体で、キャンバスのパーソナライゼーションプロパティーとして使用できるようにします。これには、ユーザー固有の情報が含まれます。

{% alert note %}
プロパティーは、すべての行またはユーザーに必要なわけではありません。ただし、プロパティ値は有効なJSON 文字列である必要があります。行のプロパティがない場合は、空の`{}` 文字列を入力します。
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

##### ステップ1.3：認証情報の設定 

データブロックで個人用のアクセストークンを作成します。

1. ユーザーの名前を選択し、**ユーザー設定を選択します。**  
2. [**アクセストークン**] タブで、[**新しいトークンの生成**] を選択します。  
3. 「Braze CDI」など、トークンを識別するための注釈を追加します。  
4. **Lifetime (days)**を空白のままにして、有効期限なしの状態で**Generate**を選択します。  
5. Braze ダッシュボードで使用するために、トークンを安全にコピーして保存します。

##### ステップ1.4:ネットワークポリシーの設定 

アカウントにネットワークポリシーがある場合は、BrazeIP を許可してCDI サービスコネクションを有効にします。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips)を参照してください。

{% endtab %}
{% tab Fabric %}

##### ステップ1.1：ファブリックでのソーステーブルの設定

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

##### ステップ1.2：認証情報の設定 

サービスプリンシパルを作成し、権限を付与します。別の同期からすでに認証情報を取得している場合は、それらを再利用できます。つまり、アカウントテーブルにアクセスできることを確認します。

##### ステップ1.3：ネットワークポリシーの設定 

アカウントにネットワークポリシーがある場合は、BrazeIP を許可してCDI サービスコネクションを有効にします。IP のリストについては、[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional)を参照してください。

{% endtab %}
{% tab File Storage %}

ファイルストレージからキャンバストリガーを同期するには、次のフィールドs を使用してソースファイルを作成します。

| フィールド | 必須 | 説明 |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | はい、`external_id` または`alias_name` のいずれか `alias_label` | これは更新したいユーザーの識別子である。これは Braze で使用されている `external_id` 値と一致しなければなりません。 |
| `ALIAS_NAME` と `ALIAS_LABEL` | はい、`external_id` または`alias_name` のいずれか `alias_label` | これら2つの列は、ユーザーエイリアスオブジェクトを作成する。`alias_name` は一意の識別子でなければならず、`alias_label` はエイリアスのタイプを指定する。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を1つしか持つことができません。 |
| `PROPERTIES` | はい | キャンバスでパーソナライゼーションプロパティーとして使用できるようにするフィールドのJSON ストリング。これには、ユーザー固有の情報が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
ファイル名はAWS規則に従い、一意である必要があります。固有性を確保するためにタイムスタンプを追加します。Amazon S3 の同期の詳細については、[File Storage Integrations](https://www.braze.com/docs/user_guide/data/cloud_ingestion/file_storage_integrations)を参照してください。
{% endalert %}

{% endtab %}
{% endtabs %}

#### ステップ 2: 送信先キャンバスの設定

1. キャンバストリガーの送信先キャンバスを設定します。新規に作成するか、既存のAPI-トリガーのキャンバスを選択します。配信スケジュール型がAPI-トリガーのキャンバスを作成する方法については、[入力スケジュール型]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas#entry-schedule-types)を参照してください。
2. API-トリガー 配信スケジュールの種類を選択した後、キャンバスの設定を続行してキャンバスを構築します。キャンバスには、シンプルな単一メッセージ送信から、複数のステップを持つ複雑な顧客ワークフローまで、さまざまな種類があります。
3. キャンバスステップs 内で、[Canvas エントリプロパティー]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) を使用して、ソーステーブルから同期する予定のプロパティーフィールドs を使用してメッセージをカスタマイズします。
  * たとえば、ステップ1 で`account_balance` のプロパティーフィールドをインストゥルメントした場合、次のリキッドテンプレートを使用してメッセージをパーソナライズします: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`。
5. キャンバスを構築したら、それを起動し、[ステップ3](#step-3-create-your-zero-copy-sync)に進みます。

#### ステップ 3: ゼロコピー同期の作成

ソース設定が完了し、送信先キャンバスが起動したら、新しいデータシンクを作成します。

1. Brazeで、**データ設定**> **クラウドデータ取り込み**に移動します。
1. 接続の詳細(または既存の認証情報s を再利用)を入力し、ソーステーブルを[ステップ1](#step-1-set-up-data-source-for-canvas-triggers) から設定します。
2. 統合の名前を指定します。
3. **キャンバストリガーs**データタイプを選択します。
4. 送信先のキャンバスを選択します([ステップ2](#step-2-configure-your-destination-canvas))。
5. 同期周波数を選択します。
6. 通知設定を指定
7. **Test Connection**を選択して、すべてが期待どおりに動作することを確認します。Snowflakeに接続する場合は、最初にダッシュボードに表示される公開キーを、Snowflakeに接続するためにBraze用に作成されたユーザーに追加します。このステップを完了するには、Snowflakeで**SECURITYADMIN**アクセス以上が必要です。 
8. 同期を保存して、キャンバストリガーの同期を開始します。

同期が実行されると、ソーステーブルのユーザーがキャンバスに入ります。キャンバス分析とクラウドデータインジェションの同期ログページを使用して、パフォーマンスを監視します。

{% alert tip %}  
設定全体(同期動作からキャンバス設定まで)を確認して、予期しない送信を避けます。キャンバス設定s (レート制限 ing、フリークエンシーキャップ、およびセグメンテーション フィルター s など) は、メッセージ配信をさらに絞り込むことができます。<br><br>本番ユースケースs を実装する前に、小規模またはテストオーディエンスで試運転を行うことをお勧めします。
{% endalert %}

### 考慮事項

CDI Canvas トリガー は、`/canvas/trigger/send` のREST API レート制限を使用します。このエンドポイントをCDI Canvas トリガー s およびREST API インテグレーションと同時に使用している場合は、組み合わせ使用量がレート制限にカウントされることを想定してください。

CDI Canvas トリガーは初期アクセスですが、次の点を考慮してください。

* ワークスペースごとに最大5 つの有効なキャンバストリガーシンク  
* 1 回の同期実行で、1 時間あたり最大375万 ユーザー 秒のアプリ速度で、それぞれの送信先 キャンバスにユーザーs が入力されます。  
  * 以下の場合、ソースからキャンバスへのエントリ時間が長くなるように準備してください。  
    * 同期実行ごとに3.75M 以上のユーザーを同期する。  
    * REST API の[ レート制限が`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit) ですでに飽和しているときにCDI Canvas トリガーを使用する。
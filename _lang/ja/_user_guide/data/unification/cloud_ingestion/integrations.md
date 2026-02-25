The file appears to be truncated — it ends mid-sentence after "![Braze ダッシュボードの". The build error is likely caused by this incomplete file. I need to provide the complete file with proper closing tags and structure.

---
nav_title: データウェアハウスの連携
article_title: データウェアハウスの連携
alias: /partners/databricks/
description: "このページでは、Braze のクラウドデータ取り込みを使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# データウェアハウスストレージの連携

> このページでは、Braze のクラウドデータ取り込み (CDI) を使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。

## データウェアハウス連携の設定

クラウドデータ取り込みの連携では、Braze 側とデータウェアハウスインスタンス側でいくつかの設定が必要です。次のステップに従って連携を設定します。

{% tabs %}
{% tab Snowflake %}
1. Snowflake インスタンスで、Braze と同期するテーブルまたはビューを設定します。
2. Braze ダッシュボードで新しい連携を作成します。
3. Braze ダッシュボードに表示された公開キーを取得し、[認証用として Snowflake ユーザーに追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. 連携のテストを行い、同期を開始します。

{% alert tip %}
[Snowflake クイックスタートガイド](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)では、サンプルコードを提供し、Snowflake Streams と CDI を使用して Braze にデータを同期する自動パイプラインの作成に必要なステップを説明しています。
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 同期する Redshift テーブルへの Braze のアクセスが許可されていることを確認します。Braze はインターネット経由で Redshift に接続します。
2. Redshift インスタンスで、Braze と同期するテーブルまたはビューを設定します。
3. Braze ダッシュボードで新しい連携を作成します。
4. 連携のテストを行い、同期を開始します。
{% endtab %}
{% tab BigQuery %}
1. サービスアカウントを作成し、同期するデータを含む BigQuery のプロジェクトとデータセットへのアクセスを許可します。  
2. BigQuery アカウントで、Braze と同期するテーブルまたはビューを設定します。   
3. Braze ダッシュボードで新しい連携を作成します。  
4. 連携のテストを行い、同期を開始します。  
{% endtab %}
{% tab Databricks %}
1. サービスアカウントを作成し、同期するデータを含む Databricks のプロジェクトとデータセットへのアクセスを許可します。  
2. Databricks アカウントで、Braze と同期するテーブルまたはビューを設定します。   
3. Braze ダッシュボードで新しい連携を作成します。  
4. 連携のテストを行い、同期を開始します。

{% alert important %}
Braze が Classic および Pro の SQL インスタンスに接続する際、2〜5 分のウォームアップ時間が発生する場合があり、接続の設定やテスト中、およびスケジュールされた同期の開始時に遅延が生じます。サーバーレス SQL インスタンスを使用するとウォームアップ時間を最小限に抑え、クエリのスループットを向上できますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、連携に使用する Fabric ワークスペースへのアクセスを許可します。   
2. Fabric ワークスペースで、Braze と同期するテーブルまたはビューを設定します。   
3. Braze ダッシュボードで新しい連携を作成します。  
4. 連携のテストを行い、同期を開始します。
{% endtab %}
{% endtabs %}

### ステップ 1: テーブルまたはビューの設定

{% tabs %}
{% tab Snowflake %}

#### ステップ 1.1: テーブルの設定

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

データベース、スキーマ、テーブルには任意の名前を付けることができますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルで更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期されます。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id` 単独、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone` のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。
    - `BRAZE_ID` - Braze のユーザー識別子。Braze SDK によって生成されるもので、クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。メールと電話の両方を含む場合は、メールが主要識別子として使用されます。
    - `PHONE` - ユーザーの電話番号。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。
- `PAYLOAD` - Braze のユーザーに同期するフィールドの JSON 文字列。

#### ステップ 1.2: ロールとデータベース権限の設定

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を変更できますが、権限は上記の例と一致させる必要があります。

#### ステップ 1.3: ウェアハウスの設定と Braze ロールへのアクセス権の付与

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスの**自動再開**フラグをオンにしておく必要があります。オンにしない場合は、クエリの実行時に Braze がウェアハウスをオンにできるよう、追加の `OPERATE` 権限を付与する必要があります。
{% endalert %}

#### ステップ 1.4: ユーザーの設定

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、Braze と接続情報を共有し、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じ Snowflake アカウントに接続する場合は、連携を作成する Braze ワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では複数の連携で同じユーザーを再利用できますが、同じ Snowflake アカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ 1.5: Snowflake ネットワークポリシーで Braze IP を許可する（オプション）

Snowflake アカウントの設定によっては、Snowflake のネットワークポリシーで以下の IP アドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関する Snowflake のドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを格納する新しいデータベースとスキーマを設定します。
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI 連携に使用するテーブル（またはビュー）を作成します。
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

データベース、スキーマ、テーブルには任意の名前を付けることができますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルで更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期されます。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id` 単独、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone` のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。
    - `BRAZE_ID` - Braze のユーザー識別子。Braze SDK によって生成されるもので、クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。メールと電話の両方を含む場合は、メールが主要識別子として使用されます。
    - `PHONE` - ユーザーの電話番号。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。
- `PAYLOAD` - Braze のユーザーに同期するフィールドの JSON 文字列。
 
#### ステップ 1.2: ユーザーの作成と権限の付与

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

これらはこのユーザーに最低限必要な権限です。CDI 連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりすることもできます。 

#### ステップ 1.3: Braze IP へのアクセスの許可

ファイアウォールやその他のネットワークポリシーがある場合は、Redshift インスタンスへの Braze ネットワークアクセスを許可する必要があります。Redshift の URL エンドポイントの例は「example-cluster.ap-northeast-2.redshift.amazonaws.com」です。

知っておくべき重要な点がいくつかあります。
- Redshift のデータに Braze がアクセスできるよう、セキュリティグループの変更が必要になる場合もあります。
- テーブル内の IP と Redshift クラスターへのクエリに使用するポート（デフォルトは 5439）のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでの Redshift TCP 接続を明示的に許可する必要があります。
- Braze がクラスターに接続するには、Redshift クラスターのエンドポイントがパブリックにアクセス可能である必要があります。
     - Redshift クラスターをパブリックにアクセス可能にしたくない場合は、VPC と EC2 インスタンスを設定して SSH トンネル経由で Redshift データにアクセスできます。詳細については、この [AWS ナレッジセンターの記事](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。
 
Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを格納する新しいプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ CDI 連携用のテーブルを1つ以上作成します。

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

プロジェクト、データセット、テーブルには任意の名前を付けることができますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルで更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期されます。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id` 単独、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone` のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。
    - `BRAZE_ID` - Braze のユーザー識別子。Braze SDK によって生成されるもので、クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。メールと電話の両方を含む場合は、メールが主要識別子として使用されます。
    - `PHONE` - ユーザーの電話番号。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。
- `PAYLOAD` - Braze のユーザーに同期するフィールドの JSON 文字列。

{% alert important %}
**BigQuery パーティショニング**

CDI は BigQuery のパーティションをサポートしています。`UPDATED_AT` の関数でパーティショニングすると（データセットのサイズに応じて日、週、時間単位の粒度など）、BigQuery はスキャンが必要なデータを刈り込むことができます。これにより、非常に大きなテーブルのパフォーマンスと効率が向上します。

他のフィールドではパーティショニングしないでください。さまざまな構成をテストして、特定のデータに最適なセットアップを見つけてください。

すべての CDI クエリは `UPDATED_AT` でフィルタリングしますが、この動作は変更される可能性があります。クエリにこの句を含めることを前提と_しない_ようにテーブルスキーマを設計してください。

詳細については、[BigQuery パーティショニングのドキュメント](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)を参照してください。
{% endalert %}

#### ステップ 1.2: サービスアカウントの作成と権限の付与 

GCP で、Braze がテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには以下の権限が必要です。 

- **BigQuery 接続ユーザー:** Braze に接続を許可します。
- **BigQuery ユーザー:** クエリの実行、データセットメタデータの読み取り、テーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:** データセットとその内容を表示するためのアクセスを Braze に提供します。
- **BigQuery ジョブユーザー:** ジョブを実行するためのアクセスを Braze に提供します。

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。その方法の詳細については、[こちら](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。後で Braze ダッシュボードにアップロードします。 

#### ステップ 1.3: Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、BigQuery インスタンスへの Braze ネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを格納する新しいカタログまたはスキーマを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ CDI 連携用のテーブルを1つ以上作成します。


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required  
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING、STRUCT、または MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |

スキーマとテーブルには任意の名前を付けることができますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルで更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期されます。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id` 単独、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone` のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。
    - `BRAZE_ID` - Braze のユーザー識別子。Braze SDK によって生成されるもので、クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。 
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。メールと電話の両方を含む場合は、メールが主要識別子として使用されます。
    - `PHONE` - ユーザーの電話番号。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。
- `PAYLOAD` - Braze のユーザーに同期するフィールドの文字列または構造体。

#### ステップ 1.2: アクセストークンの作成  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名をクリックし、ドロップダウンから [**ユーザー設定**] を選択します。
2. [アクセストークン] タブで、[**新しいトークンの生成**] を選択します。
3. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間 (日)] ボックスを空（空白）のままにしてトークンの有効期間を無期限に設定します。
4. [**生成**] を選択します。
5. 表示されたトークンをコピーして、[**完了**] を選択します。

認証情報の作成ステップで Braze ダッシュボードに入力するまで、トークンを安全な場所に保管してください。

#### ステップ 1.3: Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Databricks インスタンスへの Braze ネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 1.1: サービスプリンシパルの設定とアクセスの許可
Braze は、Entra ID 認証によるサービスプリンシパルを使用して Fabric ウェアハウスに接続します。Braze が使用する新しいサービスプリンシパルを作成し、必要に応じて Fabric リソースへのアクセスを許可します。Braze の接続には以下の情報が必要です。    

* Azure アカウントのテナント ID（ディレクトリ ID とも呼ばれる） 
* サービスプリンシパルのプリンシパル ID（アプリケーション ID とも呼ばれる） 
* Braze が認証に使用するクライアントシークレット

1. Azure portal で、Microsoft Entra 管理センターに移動し、[アプリの登録] を選択します。 
2. [**ID**] > [**アプリケーション**] > [**アプリの登録**] で [**+ 新規登録**] を選択します。
3. 名前を入力し、サポートされるアカウントの種類として `Accounts in this organizational directory only` を選択します。次に、[**登録**] を選択します。 
4. 作成したアプリケーション（サービスプリンシパル）を選択し、[**証明書とシークレット**] > [**+ 新しいクライアントシークレット**] に移動します。
5. シークレットの説明を入力し、有効期限を設定します。次に、[**追加**] を選択します。 
6. Braze のセットアップで使用するクライアントシークレットをメモしておきます。 

{% alert note %}
Azure では、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Braze へのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ 1.2: Fabric リソースへのアクセスを許可する 
Braze が Fabric インスタンスに接続するためのアクセスを提供します。Fabric の管理ポータルで、[**設定**] > [**ガバナンスとインサイト**] > [**管理ポータル**] > [**テナント設定**] に移動します。    

* [**開発者設定**] で「サービスプリンシパルが Fabric API を使用可能」を有効にして、Braze が Microsoft Entra ID を使用して接続できるようにします。
* [**OneLake の設定**] で「ユーザーが Fabric の外部アプリを使用して OneLake に保存されているデータにアクセス可能」を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。


#### ステップ 1.3: テーブルの設定
Braze は Fabric ウェアハウスのテーブルとビューの両方をサポートしています。新しいウェアハウスを作成する必要がある場合は、Fabric コンソールで [**作成**] > [**データウェアハウス**] > [**ウェアハウス**] に進みます。 

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

ウェアハウス、スキーマ、テーブルまたはビューには任意の名前を付けることができますが、カラム名は上記の定義と一致させる必要があります。

- `UPDATED_AT` - この行がテーブルで更新または追加された時刻。前回の同期以降に追加または更新された行のみが同期されます。
- **ユーザー識別子カラム** - テーブルには1つ以上のユーザー識別子カラムを含めることができます。各行には識別子を1つだけ含める必要があります（`external_id` 単独、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone` のいずれか）。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプのカラムを含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この2つのカラムでユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つだけです。
    - `BRAZE_ID` - Braze のユーザー識別子。Braze SDK によって生成されるもので、クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。メールと電話の両方を含む場合は、メールが主要識別子として使用されます。
    - `PHONE` - ユーザーの電話番号。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先的に更新されます。
- `PAYLOAD` - Braze のユーザーに同期するフィールドの JSON 文字列。


#### ステップ 1.4: ウェアハウスの接続文字列を取得する
Braze が接続するには、ウェアハウスの SQL エンドポイントが必要です。これを取得するには、Fabric で**ワークスペース**に移動し、項目の一覧でウェアハウス名にカーソルを合わせて [**SQL 接続文字列をコピー**] を選択します。

![ユーザーが SQL 接続文字列を取得する Microsoft Azure の「Fabric Console」ページ。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### ステップ 1.5: ファイアウォールで Braze IP を許可する（オプション）

Microsoft Fabric アカウントの設定によっては、Braze からのトラフィックを許可するためにファイアウォールで以下の IP アドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access) の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ 2: Braze ダッシュボードで新しい連携を作成する

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に進み、[**新しいデータ同期を作成**] を選択してから、[**Snowflake Import**] を選択します。

#### ステップ 2.1: Snowflake の接続情報とソーステーブルの追加

Snowflake データウェアハウスとソーステーブルの情報を入力して、次のステップに進みます。

![Braze ダッシュボードの Snowflake 用「新しいインポート同期の作成」ページ。ステップ1「接続設定」にサンプルデータが入力されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_1.png %})

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先メールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除された場合などの連携エラーの通知に使用されます。

連絡先メールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラー通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

![Braze ダッシュボードの Snowflake 用「新しいインポート同期の作成」ページ。ステップ2「同期の詳細を設定する」にサンプルデータが追加されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_2.png %})

データ型と同期頻度も選択します。頻度は15分間隔から月1回まで設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、および購入イベントです。同期のデータ型は作成後に変更できません。 

#### Braze ユーザーへの公開キーの追加

この時点で、Snowflake に戻って設定を完了する必要があります。ダッシュボードに表示されている公開キーを、Braze が Snowflake に接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。キーのローテーションを行う場合は、新しいキーペアを生成して新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に進み、[**新しいデータ同期を作成**] を選択してから、[**Amazon Redshift Import**] を選択します。

#### ステップ 2.1: Redshift の接続情報とソーステーブルの追加

Redshift データウェアハウスとソーステーブルの情報を入力します。プライベートネットワークトンネルを使用している場合は、スライダーを切り替えてトンネル情報を入力します。次のステップに進みます。 

{% alert note %}
Braze ダッシュボードの**データベース名**フィールドは、Amazon Redshift がデータベース識別子で追加の文字をサポートしているにもかかわらず、アルファベット（A-Z、a-z）、数字（0-9）、アンダースコア（_）のみを受け付けます。
{% endalert %}

![Braze ダッシュボードの Redshift 用「新しいインポート同期の作成」ページ。ステップ1「接続設定」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_6.png %})

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先メールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除された場合などの連携エラーの通知に使用されます。

連絡先メールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラー通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

![Braze ダッシュボードの Redshift 用「新しいインポート同期の作成」ページ。ステップ2「同期の詳細を設定する」にサンプルデータが追加されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_7.png %})

データ型と同期頻度も選択します。頻度は15分間隔から月1回まで設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、および購入イベントです。同期のデータ型は作成後に変更できません。 
{% endtab %}
{% tab BigQuery %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に進み、[**新しいデータ同期を作成**] を選択してから、[**Google BigQuery Import**] を選択します。

#### ステップ 2.1: BigQuery の接続情報とソーステーブルの追加

JSON キーをアップロードし、サービスアカウントの名前を入力してから、ソーステーブルの詳細を入力します。

![Braze ダッシュボードの BigQuery 用「新しいインポート同期の作成」ページ。ステップ1「接続設定」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_11.png %})

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先メールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除された場合などの連携エラーの通知に使用されます。

連絡先メールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラー通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

![Braze ダッシュボードの BigQuery 用「新しいインポート同期の作成」ページ。ステップ2「同期の詳細を設定する」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

データ型と同期頻度も選択します。頻度は15分間隔から月1回まで設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、購入イベント、およびユーザー削除です。同期のデータ型は作成後に変更できません。 

{% endtab %}
{% tab Databricks %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に進み、[**新しいデータ同期を作成**] を選択してから、[**Databricks Import**] を選択します。

#### ステップ 2.1: Databricks の接続情報とソーステーブルの追加

Databricks データウェアハウスとソーステーブルの情報を入力して、次のステップに進みます。

![Braze ダッシュボードの Databricks 用「新しいインポート同期の作成」ページ。ステップ1「接続設定」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_16.png %})

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先メールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除された場合などの連携エラーの通知に使用されます。

連絡先メールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラー通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

![Braze ダッシュボードの Databricks 用「新しいインポート同期の作成」ページ。ステップ2「同期の詳細を設定する」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_12.png %})

データ型と同期頻度も選択します。頻度は15分間隔から月1回まで設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、購入イベント、およびユーザー削除です。同期のデータ型は作成後に変更できません。 

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 2.1: クラウドデータ取り込みの同期を設定する

Microsoft Fabric 用の新しいデータ同期を作成します。Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に進み、[**新しいデータ同期を作成**] を選択してから、[**Microsoft Fabric Import**] を選択します。

#### ステップ 2.2: Microsoft Fabric の接続情報とソーステーブルの追加

Microsoft Fabric ウェアハウスの認証情報とソーステーブルの情報を入力して、次のステップに進みます。

- 認証情報名は Braze におけるこれらの認証情報のラベルです。わかりやすい値を設定してください。
- テナント ID、プリンシパル ID、クライアントシークレット、および接続文字列の取得方法については、セクション1のステップを参照してください。

![Braze ダッシュボードの Microsoft 用「新しいインポート同期の作成」ページ。ステップ1「接続設定」に設定されています。]({% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %})

#### ステップ 2.3: 同期の詳細の設定

次に、同期の以下の詳細を設定します。 

- 同期名 
- データ型 - サポートされるデータ型は、カスタム属性、カスタムイベント、購入イベント、カタログ、およびユーザー削除です。同期のデータ型は作成後に変更できません。 
- 同期頻度 - 頻度は15分間隔から月1回まで設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して定期的な同期がスケジュールされます。 
  - 定期的でない同期は、手動または [API]({{site.baseurl}}/api/endpoints/cdi) 経由でトリガーできます。 

![Braze ダッシュボードの Microsoft Fabric 用「新しいインポート同期の作成」ページ。ステップ2「同期の詳細を設定する」に設定されています。]({% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %})


#### ステップ 2.4: 通知設定の構成

次に、連絡先メールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除された場合などの連携エラーの通知や、特定の行の更新に失敗した場合のアラートに使用されます。

デフォルトでは、連絡先メールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラー通知のみが送信されます。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には以下が含まれます。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

行レベルの問題に対するアラートを設定したり、同期が正常に実行されるたびにアラートを受け取るように設定したりすることもできます。 

![Braze ダッシュボードの Microsoft Fabric 用「新しいインポート同期の作成」ページ。ステップ3「通知の設定をする」に設定されています。]({% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %})


{% endtab %}

{% endtabs %}

### ステップ 3: 接続テスト

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードに戻り、[**テスト接続**] を選択します。成功するとデータのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Snowflake 用「新しいインポート同期の作成」ページ。ステップ3「テスト接続」で RSA 公開キーが表示されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Braze ダッシュボードに戻り、[**テスト接続**] を選択します。成功するとデータのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Redshift 用「新しいインポート同期の作成」ページ。ステップ3「テスト接続」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_8.png %})
{% endsubtab %}

{% subtab Private Network %}
Braze ダッシュボードに戻り、[**テスト接続**] を選択します。成功するとデータのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Redshift プライベートネットワーク用「新しいインポート同期の作成」ページ。ステップ4「テスト接続」で RSA 公開キーが表示されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

同期の設定詳細をすべて入力したら、[**テスト接続**] を選択します。成功するとデータのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの BigQuery 用「新しいインポート同期の作成」ページ。ステップ3「テスト接続」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}

{% tab Databricks %}

同期の設定詳細をすべて入力したら、[**テスト接続**] を選択します。成功するとデータのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Databricks 用「新しいインポート同期の作成」ページ。ステップ3「テスト接続」に設定されています。]({% image_buster /assets/img/cloud_ingestion/ingestion_13.png %})

{% endtab %}
{% tab Microsoft Fabric %}

同期の設定詳細をすべて入力したら、[**テスト接続**] を選択します。成功するとデータのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Microsoft Fabric 用「新しいインポート同期の作成」ページ。ステップ4「テスト接続」に設定されています。]({% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、テスト接続に成功する必要があります。作成ページを閉じる必要がある場合でも、連携は保存されるため、詳細ページに戻って変更やテストを行うことができます。  
{% endalert %}

## 追加の連携またはユーザーの設定（オプション）

{% tabs %}
{% tab Snowflake %}
Braze で複数の連携を設定できますが、各連携は異なるテーブルを同期するように構成する必要があります。追加
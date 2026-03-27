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

このページでは、現在早期アクセス (EA) 段階にある同期とソースのステップを示しています。一般提供版のステップと画像については、以下の「**一般提供版のエクスペリエンス**」を展開してください。

## データウェアハウス統合の設定

クラウドデータ取り込みの連携では、Braze 側とデータウェアハウスインスタンス側でいくつかの設定が必要です。次のステップに従って、連携を設定します。

{% tabs %}
{% tab Snowflake %}
1. Snowflake インスタンスで、Braze と同期するテーブルまたはビューを設定します。
2. Braze ダッシュボードで新しい Snowflake ソースを作成します。
3. Braze ダッシュボードに表示された公開キーを取得し、[認証用として Snowflake ユーザーに追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. Braze ダッシュボードで同期を作成し、連携のテストを行い、同期を開始します。

{% alert tip %}
[Snowflake クイックスタートガイド](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)では、サンプルコードを提供し、Snowflake Streams と CDI を使用して自動パイプラインを作成し、Braze にデータを同期するために必要なステップを説明しています。
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 同期する Redshift テーブルへの Braze のアクセスが許可されていることを確認します。Braze はインターネット経由で Redshift に接続します。
2. Redshift インスタンスで、Braze と同期するテーブルまたはビューを設定します。
3. Braze ダッシュボードで新しいソースと同期を作成します。
4. 連携のテストを行い、同期を開始します。
{% endtab %}
{% tab BigQuery %}
1. サービスアカウントを作成し、同期するデータを含む BigQuery のプロジェクトとデータセットへのアクセスを許可します。  
2. BigQuery アカウントで、Braze と同期するテーブルまたはビューを設定します。   
3. Braze ダッシュボードで新しいソースと同期を作成します。  
4. 連携のテストを行い、同期を開始します。 
{% endtab %}
{% tab Databricks %}
1. サービスアカウントを作成し、同期するデータを含む Databricks のプロジェクトとデータセットへのアクセスを許可します。  
2. Databricks アカウントで、Braze と同期するテーブルまたはビューを設定します。   
3. Braze ダッシュボードで新しいソースと同期を作成します。
4. 連携のテストを行い、同期を開始します。

{% alert important %}
Braze が Classic および Pro の SQL インスタンスに接続する際、2〜5 分のウォームアップ時間が発生することがあり、接続の設定やテスト中、およびスケジュールされた同期の開始時に遅延が生じる可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、Fabric API へのアクセスを許可します。
2. 共有ワークスペースを設定し、サービスプリンシパルにアクセスを許可します。
3. 共有 Fabric ワークスペースで、Braze と同期するテーブルまたはビューを設定します。   
4. Braze ダッシュボードで新しいソースと同期を作成します。  
5. 連携のテストを行い、同期を開始します。
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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。

#### ステップ 1.2: ロールとデータベース権限の設定

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を更新してください。ただし、権限は上記の例と一致する必要があります。

#### ステップ 1.3: ウェアハウスの設定と Braze ロールへのアクセス権の付与

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスは**自動再開**フラグをオンにしておく必要があります。オンにしない場合は、Braze がクエリの実行時にウェアハウスをオンにできるように、追加の `OPERATE` 権限を付与する必要があります。
{% endalert %}

#### ステップ 1.4: ユーザーの設定

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、Braze と接続情報を共有し、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じ Snowflake アカウントに接続する場合は、連携を作成する Braze ワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では、複数の連携にわたって同じユーザーを再利用できますが、同じ Snowflake アカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ 1.5: Snowflake ネットワークポリシーで Braze IP を許可する（オプション）

Snowflake アカウントの設定によっては、Snowflake のネットワークポリシーで以下の IP アドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関する Snowflake の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを保持する新規データベースとスキーマを設定します。
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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。
 
#### ステップ 1.2: ユーザーの作成と権限の付与

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

これらは、このユーザーに最低限必要な権限です。CDI 連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりすることもできます。 

#### ステップ 1.3: Braze IP へのアクセスの許可

ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスへの Braze ネットワークアクセスを許可する必要があります。Redshift の URL エンドポイントの例は「example-cluster.ap-northeast-2.redshift.amazonaws.com」です。

知っておくべき重要な点がいくつかあります。
- Redshift のデータへの Braze のアクセスを許可するために、セキュリティグループの変更が必要になる場合もあります。
- テーブル内の IP と Redshift クラスターへのクエリに使用するポート（デフォルトは 5439）のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでの Redshift の TCP 接続を明示的に許可する必要があります。
- Braze がクラスターに接続するには、Redshift クラスターのエンドポイントがパブリックにアクセス可能である必要があります。
     - Redshift クラスターにパブリックアクセスを許可しない場合は、SSH トンネルを使用して Redshift データにアクセスするように VPC と EC2 インスタンスを設定できます。詳細については、[AWS ナレッジセンターの投稿](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。
 
Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを保持する新規のプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI 連携に使用するテーブルを 1 つ以上作成します。

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

プロジェクト、データセット、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。

{% alert important %}
**BigQuery のパーティショニング**

CDI は BigQuery のパーティションをサポートしています。`UPDATED_AT` の関数によるパーティション分割（例えば、データセットのサイズに応じて日単位、週単位、時間単位の粒度で）を行うと、BigQuery はスキャンする必要のあるデータを絞り込めます。これにより、非常に大きなテーブルのパフォーマンスと効率が向上します。

他のフィールドでパーティション分割しないでください。さまざまな設定をテストして、ご自身のデータに最適な構成を見つけてください。

すべての CDI クエリは `UPDATED_AT` でフィルターしますが、この動作は変更される可能性があります。テーブルスキーマを設計する際は、クエリにこの句を含めることを前提と_しない_ようにしてください。

詳細については、[BigQuery のパーティショニングに関するドキュメント](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)を参照してください。
{% endalert %}

#### ステップ 1.2: サービスアカウントの作成と権限の付与 

GCP で、Braze がテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。 

- **BigQuery 接続ユーザー:** Braze に接続を許可します。
- **BigQuery ユーザー:** クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:** データセットとその内容を表示するためのアクセスを Braze に提供します。
- **BigQuery ジョブユーザー:** ジョブを実行するためのアクセスを Braze に提供します。

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳細については、[サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。このキーは後のステップで Braze ダッシュボードにアップロードします。 

#### ステップ 1.3: Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、BigQuery インスタンスへの Braze ネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを保持する新しいカタログまたはスキーマを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI 連携に使用するテーブルを 1 つ以上作成します。


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

スキーマとテーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。 
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze でユーザーと同期するフィールドの文字列または構造体です。

#### ステップ 1.2: アクセストークンの作成  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名を選択し、ドロップダウンから [**ユーザー設定**] を選択します。
2. [アクセストークン] タブで、[**新しいトークンの生成**] を選択します。
3. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間（日）] ボックスを空（空白）のままにして、トークンの有効期間を無期限に変更します。
4. [**生成**] を選択します。
5. 表示されたトークンをコピーして、[**完了**] を選択します。

認証情報の作成ステップで Braze ダッシュボードに入力する必要があるまで、トークンを安全な場所に保管してください。

#### ステップ 1.3: Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Databricks インスタンスへの Braze ネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 1.1: サービスプリンシパルの設定とアクセスの許可
Braze は、Entra ID 認証でサービスプリンシパルを使用して Fabric ウェアハウスに接続します。Braze が使用する新しいサービスプリンシパルを作成し、必要に応じて Fabric リソースへのアクセスを許可します。Braze の接続には以下の情報が必要です。    

* Azure アカウントのテナント ID（ディレクトリとも呼ばれます） 
* サービスプリンシパルのプリンシパル ID（アプリケーション ID とも呼ばれます） 
* Braze が認証するためのクライアントシークレット

1. Azure portal で、[Microsoft Entra 管理センター]、[アプリの登録] の順に移動します。 
2. [**ID**] > [**アプリケーション**] > [**アプリの登録**] で [**+ 新規登録**] を選択します。
3. 名前を入力し、サポートされているアカウントの種類として `Accounts in this organizational directory only` を選択します。次に、[**登録**] を選択します。 
4. 作成したアプリケーション（サービスプリンシパル）を選択し、[**証明書とシークレット**] > [**+ 新しいクライアントシークレット**] に移動します。
5. シークレットの説明を入力し、有効期限を設定します。次に、[**追加**] を選択します。 
6. Braze のセットアップで使用するために、作成したクライアントシークレットをメモしてください。 

{% alert note %}
Azure では、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Braze へのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ 1.2: Fabric リソースへのアクセスの許可 
Braze が Fabric インスタンスに接続するためのアクセスを提供します。Fabric の管理ポータルで、[**設定**] > [**ガバナンスとインサイト**] > [**管理ポータル**] > [**テナント設定**] の順に移動します。    

* [**開発者設定**] で、[**サービスプリンシパルが Fabric API を使用可能**] を有効にして、Braze が Microsoft Entra ID を使用して接続できるようにします。
* [**OneLake の設定**] で、[**ユーザーが Fabric の外部アプリを使用して OneLake に保存されているデータにアクセス可能**] を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。

#### ステップ 1.3: 共有ワークスペースの設定とアクセスの許可

Braze に接続する Fabric リソースは、共有ワークスペースに配置する必要があります。デフォルトの **My Workspace** のみを使用している場合は、新しい共有ワークスペースを作成してください。

1. ナビゲーションメニューで [**ワークスペース**] を選択し、[**+ 新しいワークスペース**] を選択します。
2. ワークスペースの**名前**を入力し、[**適用**] を選択します。

共有ワークスペースを作成したら、サービスプリンシパルにアクセスを許可します。

1. ワークスペースを選択し、[**アクセスの管理**] を選択します。
2. [**+ ユーザーまたはグループの追加**] を選択します。
3. ステップ 1.1 で作成したサービスプリンシパルの名前を検索して選択します。表示されない場合は、ステップ 1.2 で [**サービスプリンシパルが Fabric API を使用可能**] の設定が有効になっていることを確認してください。
4. ロールのドロップダウンで [**共同作成者**] を選択します。

これで、サービスプリンシパルは SQL エンドポイントを通じてこのワークスペース内の Fabric ウェアハウスリソース（Braze で使用するウェアハウスを含む）にアクセスできるようになります。

#### ステップ 1.4: テーブルの設定
Braze は Fabric ウェアハウスのテーブルとビューの両方をサポートしています。新しいウェアハウスを作成する必要がある場合は、ステップ 1.3 の共有ワークスペース内に作成してください。Fabric コンソールで [**作成**] > [**データウェアハウス**] > [**ウェアハウス**] と進みます。

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

ウェアハウス、スキーマ、テーブルまたはビューには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。


#### ステップ 1.5: ウェアハウスの接続文字列を取得する
ウェアハウスの SQL エンドポイントを取得するには、Fabric で**ワークスペース**に移動し、項目の一覧でウェアハウスの名前にカーソルを合わせ、[**SQL 接続文字列をコピー**] を選択します。

![Microsoft Azure の「Fabric コンソール」ページ。ユーザーはここで SQL 接続文字列を取得します。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### ステップ 1.6: ファイアウォールで Braze IP を許可する（オプション）

Microsoft Fabric アカウントの設定によっては、Braze からのトラフィックを許可するために、ファイアウォールで以下の IP アドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access) の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ 2: Braze ダッシュボードで新しいソースを作成する

{% alert important %}
2026 年 2 月以降にオンボーディングされたお客様は、ソースと同期が分離された CDI UI に早期アクセスできる場合があります。この UI では、同期を作成する前にソースを作成してください。複数の同期で同じソースを使用できます。
{% endalert %}

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] > [**ソース**] に移動し、[**データソースの追加**] を選択して、[**Snowflake**] を選択します。

#### ステップ 2.1: Snowflake の接続情報の追加

ソースの名前を選択し、Snowflake の認証情報と設定を入力して、次のステップに進みます。

{% alert note %}
[**Snowflake アカウントロケーター**] フィールドには、Snowflake の[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。通常、`xy12345.us-east-1.aws` のような形式です。これはデータベース名やウェアハウス名とは異なります。
{% endalert %} 

#### ステップ 2.2: Braze ユーザーへの公開キーの追加

認証情報と設定を入力したら、[**認証情報を保存**] をクリックして RSA キーを生成し、Snowflake に戻って設定を完了します。ダッシュボードに表示されている公開キーを、Braze が Snowflake に接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でキーをローテーションする場合は、Braze が新しいキーペアを生成して新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] > [**ソース**] に移動し、[**データソースの追加**] を選択して、[**Amazon Redshift**] を選択します。

#### ステップ 2.1: Redshift の接続情報とソーステーブルの追加

ソースの名前を選択し、Redshift の認証情報と設定を入力します。プライベートネットワークトンネルを使用している場合は、スライダーを切り替えてトンネル情報を入力します。次のステップに進みます。 

{% alert note %}
Braze ダッシュボードの [**データベース名**] フィールドは、Amazon Redshift がデータベース識別子で追加の文字をサポートしているにもかかわらず、英字（A–Z、a–z）、数字（0–9）、アンダースコア（_）のみを受け付けます。
{% endalert %}

#### ステップ 2.2: 接続のテストとソースへの接続

次に、[**テスト接続**] を選択します。成功したら、残りの設定を確定し、[**ソースに接続**] をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。
{% endtab %}
{% tab BigQuery %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] > [**ソース**] に移動し、[**データソースの追加**] を選択して、[**Google BigQuery**] を選択します。

#### ステップ 2.1: BigQuery の接続情報とソーステーブルの追加

ソースの名前を選択します。次に、JSON キーをアップロードし、サービスアカウントの名前を入力して、残りの設定フィールドを入力します。

#### ステップ 2.2: 接続のテストとソースへの接続

次に、[**テスト接続**] を選択します。成功したら、残りの設定を確定し、[**ソースに接続**] をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}
{% tab Databricks %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] > [**ソース**] に移動し、[**データソースの追加**] を選択して、[**Databricks**] を選択します。

#### ステップ 2.1: Databricks の接続情報とソーステーブルの追加

ソースの名前を選択し、Databricks の認証情報と設定を入力します。次のステップに進みます。

#### ステップ 2.2: 接続のテストとソースへの接続

次に、[**テスト接続**] を選択します。成功したら、残りの設定を確定し、[**ソースに接続**] をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成するには、テスト接続に成功する必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Braze ダッシュボードで、[データ設定] > [クラウドデータ取り込み] > [ソース] に移動し、[**データソースの追加**] を選択して、[**Microsoft Fabric**] を選択します。

#### ステップ 2.1: クラウドデータ取り込みの同期を設定する

ソースの名前を選択し、Microsoft Fabric の認証情報と設定を入力します。
- **認証情報名**は、Braze におけるこれらの認証情報のラベルです。わかりやすい値を設定してください。
- テナント ID、プリンシパル ID、クライアントシークレット、および接続文字列の取得方法については、セクション 1 のステップを参照してください。

#### ステップ 2.2: 接続のテストとソースへの接続

次に、[**テスト接続**] を選択します。成功したら、残りの設定を確定し、[**ソースに接続**] をクリックします。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
ソースを作成するには、テスト接続に成功する必要があります。作成ページを閉じると、ソースは保存されません。
{% endalert %}

{% endtab %}

{% endtabs %}

### ステップ 3: Braze ダッシュボードで新しい同期を作成する
[**データ設定**] > [**クラウドデータ取り込み**] > [**同期**] に移動し、[**データ同期の作成**] を選択します。

{% tabs %}
{% tab Snowflake %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、[**テスト接続**] をクリックします。

成功すると、データのプレビューが表示されます。[**次へ: 通知**] を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、[**下書きとして保存**] をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Braze はこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。 

このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動または API 経由でトリガーできます。

定期的な同期は、15 分間隔から 1 か月に 1 回までの頻度で設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}

{% tab Redshift %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、[**テスト接続**] をクリックします。

成功すると、データのプレビューが表示されます。[**次へ: 通知**] を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、[**下書きとして保存**] をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Braze はこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。 

このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動または API 経由でトリガーできます。

定期的な同期は、15 分間隔から 1 か月に 1 回までの頻度で設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}

{% tab BigQuery %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、[**テスト接続**] をクリックします。

成功すると、データのプレビューが表示されます。[**次へ: 通知**] を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、[**下書きとして保存**] をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Braze はこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動または API 経由でトリガーできます。

定期的な同期は、15 分間隔から 1 か月に 1 回までの頻度で設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}

{% tab Databricks %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト
同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、[**テスト接続**] をクリックします。

成功すると、データのプレビューが表示されます。[**次へ: 通知**] を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、[**下書きとして保存**] をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Braze はこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。 

このような問題には、次のようなものがあります。
- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動または API 経由でトリガーできます。

定期的な同期は、15 分間隔から 1 か月に 1 回までの頻度で設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 3.1: 同期の詳細の設定と接続のテスト

同期の名前を選択します。次に、アクティブなソースから選択し、同期のソーステーブルを入力します。データタイプを選択し、[**テスト接続**] をクリックします。

成功すると、データのプレビューが表示されます。[**次へ: 通知**] を選択して続行します。接続に失敗した場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% alert note %}
次のステップに進むには、テスト接続に成功する必要があります。同期の作成ページを閉じる必要がある場合は、[**下書きとして保存**] をクリックして作業中の内容を保持してください。
{% endalert %}

#### ステップ 3.2: 通知設定の追加
同期エラー通知用の連絡先メールアドレスを入力します。Braze はこの連絡先情報を使用して、テーブルへのアクセスが予期せず失われたなどの連携エラーの通知を送信します。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。 

このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題

（カタログ同期のみ）カタログ層の容量不足

#### ステップ 3.3: スケジューリング
最後に、同期を非定期または定期として設定します。

非定期の同期は、手動または API 経由でトリガーできます。

定期的な同期は、15 分間隔から 1 か月に 1 回までの頻度で設定できます。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。

{% endtab %}
{% endtabs %}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、テスト接続に成功する必要があります。作成ページを閉じた場合でも、連携は保存されるため、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## 追加の連携またはユーザーの設定（オプション）

{% tabs %}
{% tab Snowflake %}
Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Snowflake アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーとロールを再利用する場合、公開キーを追加するステップを再度行う必要はありません。
{% endtab %}
{% tab Redshift %}
Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Snowflake または Redshift アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。
{% endtab %}
{% tab BigQuery %}

Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ BigQuery アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Databricks %}

Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Databricks アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Microsoft Fabric %}

Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Fabric アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% endtabs %}

## 同期の実行

{% tabs %}
{% tab Snowflake %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Redshift %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab BigQuery %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Databricks %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Microsoft Fabric %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}

{% endtabs %}

{% details 一般提供版のエクスペリエンス %}

## データウェアハウス統合の設定

クラウドデータ取り込みの連携では、Braze 側とデータウェアハウスインスタンス側でいくつかの設定が必要です。次のステップに従って、連携を設定します。

{% tabs %}
{% tab Snowflake %}
1. Snowflake インスタンスで、Braze と同期するテーブルまたはビューを設定します。
2. Braze ダッシュボードで新しい連携を作成します。
3. Braze ダッシュボードに表示された公開キーを取得し、[認証用として Snowflake ユーザーに追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. 連携のテストを行い、同期を開始します。

{% alert tip %}
[Snowflake クイックスタートガイド](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)では、サンプルコードを提供し、Snowflake Streams と CDI を使用して自動パイプラインを作成し、Braze にデータを同期するために必要なステップを説明しています。
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
Braze が Classic および Pro の SQL インスタンスに接続する際、2〜5 分のウォームアップ時間が発生することがあり、接続の設定やテスト中、およびスケジュールされた同期の開始時に遅延が生じます。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、Fabric API へのアクセスを許可します。
2. 共有ワークスペースを設定し、サービスプリンシパルにアクセスを許可します。
3. ステップ 2 で作成した共有 Fabric ワークスペースで、Braze と同期するテーブルまたはビューを設定します。   
4. Braze ダッシュボードで新しい連携を作成します。  
5. 連携のテストを行い、同期を開始します。
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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。

#### ステップ 1.2: ロールとデータベース権限の設定

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を更新してください。ただし、権限は上記の例と一致する必要があります。

#### ステップ 1.3: ウェアハウスの設定と Braze ロールへのアクセス権の付与

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスは**自動再開**フラグをオンにしておく必要があります。オンにしない場合は、Braze がクエリの実行時にウェアハウスをオンにできるように、追加の `OPERATE` 権限を付与する必要があります。
{% endalert %}

#### ステップ 1.4: ユーザーの設定

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、Braze と接続情報を共有し、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じ Snowflake アカウントに接続する場合は、連携を作成する Braze ワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では、複数の連携にわたって同じユーザーを再利用できますが、同じ Snowflake アカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ 1.5: Snowflake ネットワークポリシーで Braze IP を許可する（オプション）

Snowflake アカウントの設定によっては、Snowflake のネットワークポリシーで以下の IP アドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関する Snowflake の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを保持する新規データベースとスキーマを設定します。
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

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。
 
#### ステップ 1.2: ユーザーの作成と権限の付与

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

これらは、このユーザーに最低限必要な権限です。CDI 連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりすることもできます。 

#### ステップ 1.3: Braze IP へのアクセスの許可

ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスへの Braze ネットワークアクセスを許可する必要があります。Redshift の URL エンドポイントの例は「example-cluster.ap-northeast-2.redshift.amazonaws.com」です。

知っておくべき重要な点がいくつかあります。
- Redshift のデータへの Braze のアクセスを許可するために、セキュリティグループの変更が必要になる場合もあります。
- テーブル内の IP と Redshift クラスターへのクエリに使用するポート（デフォルトは 5439）のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートでの Redshift の TCP 接続を明示的に許可する必要があります。
- Braze がクラスターに接続するには、Redshift クラスターのエンドポイントがパブリックにアクセス可能である必要があります。
     - Redshift クラスターにパブリックアクセスを許可しない場合は、SSH トンネルを使用して Redshift データにアクセスするように VPC と EC2 インスタンスを設定できます。詳細については、[AWS ナレッジセンターの投稿](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。
 
Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを保持する新規のプロジェクトまたはデータセットを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI 連携に使用するテーブルを 1 つ以上作成します。

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

プロジェクト、データセット、テーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。

{% alert important %}
**BigQuery のパーティショニング**

CDI は BigQuery のパーティションをサポートしています。`UPDATED_AT` の関数によるパーティション分割（例えば、データセットのサイズに応じて日単位、週単位、時間単位の粒度で）を行うと、BigQuery はスキャンする必要のあるデータを絞り込めます。これにより、非常に大きなテーブルのパフォーマンスと効率が向上します。

他のフィールドでパーティション分割しないでください。さまざまな設定をテストして、ご自身のデータに最適な構成を見つけてください。

すべての CDI クエリは `UPDATED_AT` でフィルターしますが、この動作は変更される可能性があります。テーブルスキーマを設計する際は、クエリにこの句を含めることを前提と_しない_ようにしてください。

詳細については、[BigQuery のパーティショニングに関するドキュメント](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)を参照してください。
{% endalert %}

#### ステップ 1.2: サービスアカウントの作成と権限の付与 

GCP で、Braze がテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。 

- **BigQuery 接続ユーザー:** Braze に接続を許可します。
- **BigQuery ユーザー:** クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:** データセットとその内容を表示するためのアクセスを Braze に提供します。
- **BigQuery ジョブユーザー:** ジョブを実行するためのアクセスを Braze に提供します。

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。その方法の詳細については、[こちら](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これは後で Braze ダッシュボードにアップロードします。 

#### ステップ 1.3: Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、BigQuery インスタンスへの Braze ネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ 1.1: テーブルの設定 

オプションで、ソーステーブルを保持する新しいカタログまたはスキーマを設定します。

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持つ、CDI 連携に使用するテーブルを 1 つ以上作成します。


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

スキーマとテーブルには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。 
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze でユーザーと同期するフィールドの文字列または構造体です。

#### ステップ 1.2: アクセストークンの作成  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名を選択し、ドロップダウンから [**ユーザー設定**] を選択します。
2. [アクセストークン] タブで、[**新しいトークンの生成**] を選択します。
3. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間（日）] ボックスを空（空白）のままにして、トークンの有効期間を無期限に変更します。
4. [**生成**] を選択します。
5. 表示されたトークンをコピーして、[**完了**] を選択します。

認証情報の作成ステップで Braze ダッシュボードに入力する必要があるまで、トークンを安全な場所に保管してください。

#### ステップ 1.3: Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Databricks インスタンスへの Braze ネットワークアクセスを許可する必要があります。Braze ダッシュボードのリージョンに対応する以下の IP からのアクセスを許可してください。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 1.1: サービスプリンシパルの設定とアクセスの許可
Braze は、Entra ID 認証でサービスプリンシパルを使用して Fabric ウェアハウスに接続します。Braze が使用する新しいサービスプリンシパルを作成し、必要に応じて Fabric リソースへのアクセスを許可します。Braze の接続には以下の情報が必要です。    

* Azure アカウントのテナント ID（ディレクトリとも呼ばれます） 
* サービスプリンシパルのプリンシパル ID（アプリケーション ID とも呼ばれます） 
* Braze が認証するためのクライアントシークレット

1. Azure portal で、[Microsoft Entra 管理センター]、[アプリの登録] の順に移動します。 
2. [**ID**] > [**アプリケーション**] > [**アプリの登録**] で [**+ 新規登録**] を選択します。
3. 名前を入力し、サポートされているアカウントの種類として `Accounts in this organizational directory only` を選択します。次に、[**登録**] を選択します。 
4. 作成したアプリケーション（サービスプリンシパル）を選択し、[**証明書とシークレット**] > [**+ 新しいクライアントシークレット**] に移動します。
5. シークレットの説明を入力し、有効期限を設定します。次に、[**追加**] を選択します。 
6. Braze のセットアップで使用するために、作成したクライアントシークレットをメモしてください。 

{% alert note %}
Azure では、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Braze へのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ 1.2: Fabric リソースへのアクセスの許可 
Braze が Fabric インスタンスに接続するためのアクセスを提供します。Fabric の管理ポータルで、[**設定**] > [**ガバナンスとインサイト**] > [**管理ポータル**] > [**テナント設定**] の順に移動します。    

* [**開発者設定**] で、[**サービスプリンシパルが Fabric API を使用可能**] を有効にして、Braze が Microsoft Entra ID を使用して接続できるようにします。
* [**OneLake の設定**] で、[**ユーザーが Fabric の外部アプリを使用して OneLake に保存されているデータにアクセス可能**] を有効にして、サービスプリンシパルが外部アプリからデータにアクセスできるようにします。

#### ステップ 1.3: 共有ワークスペースの設定とアクセスの許可

Braze に接続する Fabric リソースは、共有ワークスペースに配置する必要があります。デフォルトの **My Workspace** のみを使用している場合は、新しい共有ワークスペースを作成してください。

1. ナビゲーションメニューで [**ワークスペース**] を選択し、[**+ 新しいワークスペース**] を選択します。
2. ワークスペースの**名前**を入力し、[**適用**] を選択します。

共有ワークスペースを作成したら、サービスプリンシパルにアクセスを許可します。

1. ワークスペースを選択し、[**アクセスの管理**] を選択します。
2. [**+ ユーザーまたはグループの追加**] を選択します。
3. ステップ 1.1 で作成したサービスプリンシパルの名前を検索して選択します。表示されない場合は、ステップ 1.2 で [**サービスプリンシパルが Fabric API を使用可能**] の設定が有効になっていることを確認してください。
4. ロールのドロップダウンで [**共同作成者**] を選択します。

これで、サービスプリンシパルは SQL エンドポイントを通じてこのワークスペース内の Fabric ウェアハウスリソース（Braze で使用するウェアハウスを含む）にアクセスできるようになります。

#### ステップ 1.4: テーブルの設定
Braze は Fabric ウェアハウスのテーブルとビューの両方をサポートしています。新しいウェアハウスを作成する必要がある場合は、ステップ 1.3 の共有ワークスペース内に作成してください。Fabric コンソールで [**作成**] > [**データウェアハウス**] > [**ウェアハウス**] と進みます。

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

ウェアハウス、スキーマ、テーブルまたはビューには任意の名前を付けることができますが、列名は上記の定義と一致する必要があります。

- `UPDATED_AT` - テーブルでこの行が更新された時刻、または追加された時刻です。Braze は `UPDATED_AT` が前回の同期値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界タイムスタンプの行は再同期される可能性があります。
- **ユーザー識別子カラム** - テーブルには、1 つ以上のユーザー識別子カラムを含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、`braze_id`、`email`、または `phone`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、3 つ、4 つ、または 5 つすべての識別子タイプの列を含めることができます。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
    - `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
    - `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。
    - `EMAIL` - ユーザーのメールアドレスです。同じメールアドレスを持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。メールと電話番号の両方を含める場合、メールが主要な識別子として使用されます。
    - `PHONE` - ユーザーの電話番号です。同じ電話番号を持つ複数のプロファイルが存在する場合、最も最近更新されたプロファイルが優先されます。
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列です。


#### ステップ 1.5: ウェアハウスの接続文字列を取得する
Braze を接続するには、ウェアハウスの SQL エンドポイントが必要です。これを取得するには、Fabric で**ワークスペース**に移動し、項目の一覧でウェアハウスの名前にカーソルを合わせ、[**SQL 接続文字列をコピー**] を選択します。

![Microsoft Azure の「Fabric コンソール」ページ。ユーザーはここで SQL 接続文字列を取得します。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### ステップ 1.6: ファイアウォールで Braze IP を許可する（オプション）

Microsoft Fabric アカウントの設定によっては、Braze からのトラフィックを許可するために、ファイアウォールで以下の IP アドレスを許可する必要がある場合があります。これを有効にする方法の詳細については、[Entra Conditional Access](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access) の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ 2: Braze ダッシュボードで新規連携を作成する

{% alert important %}
2026 年 2 月以降にオンボーディングされたお客様は、ソースと同期が分離された CDI UI に早期アクセスできる場合があります。この UI では、同期を作成する前にソースを作成してください。複数の同期で同じソースを使用できます。
{% endalert %}

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に移動し、[**新規データ同期の作成**] を選択して、[**Snowflake インポート**] を選択します。

#### ステップ 2.1: Snowflake の接続情報とソーステーブルの追加

Snowflake データウェアハウスとソーステーブルの情報を入力して、次のステップに進みます。

{% alert note %}
[**Snowflake アカウントロケーター**] フィールドには、Snowflake の[アカウント識別子](https://docs.snowflake.com/en/user-guide/admin-account-identifier)を入力します。通常、`xy12345.us-east-1.aws` のような形式です。これはデータベース名やウェアハウス名とは異なります。
{% endalert %}

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなどの連携エラーの通知に使用されます。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

データタイプと同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータタイプは、カスタム属性、カスタムイベント、および購入イベントです。同期のデータタイプは、作成後に変更できません。 

#### Braze ユーザーへの公開キーの追加

この時点で、Snowflake に戻って設定を完了する必要があります。ダッシュボードに表示されている公開キーを、Braze が Snowflake に接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でキーをローテーションする場合は、新しいキーペアを生成して新しい公開キーを提供できます。

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に移動し、[**新規データ同期の作成**] を選択して、[**Amazon Redshift インポート**] を選択します。

#### ステップ 2.1: Redshift の接続情報とソーステーブルの追加

Redshift データウェアハウスとソーステーブルの情報を入力します。プライベートネットワークトンネルを使用している場合は、スライダーを切り替えてトンネル情報を入力します。次のステップに進みます。 

{% alert note %}
Braze ダッシュボードの [**データベース名**] フィールドは、Amazon Redshift がデータベース識別子で追加の文字をサポートしているにもかかわらず、英字（A–Z、a–z）、数字（0–9）、アンダースコア（_）のみを受け付けます。
{% endalert %}

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなどの連携エラーの通知に使用されます。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

データタイプと同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータタイプは、カスタム属性、カスタムイベント、および購入イベントです。同期のデータタイプは、作成後に変更できません。 
{% endtab %}
{% tab BigQuery %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に移動し、[**新規データ同期の作成**] を選択して、[**Google BigQuery インポート**] を選択します。

#### ステップ 2.1: BigQuery の接続情報とソーステーブルの追加

JSON キーをアップロードし、サービスアカウントの名前を入力して、ソーステーブルの詳細を入力します。

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなどの連携エラーの通知に使用されます。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

データタイプと同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータタイプは、カスタム属性、カスタムイベント、購入イベント、およびユーザー削除です。同期のデータタイプは、作成後に変更できません。 

{% endtab %}
{% tab Databricks %}

Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に移動し、[**新規データ同期の作成**] を選択して、[**Databricks インポート**] を選択します。

#### ステップ 2.1: Databricks の接続情報とソーステーブルの追加

Databricks データウェアハウスとソーステーブルの情報を入力して、次のステップに進みます。

#### ステップ 2.2: 同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなどの連携エラーの通知に使用されます。

連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。行レベルの問題は通知されません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

データタイプと同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータタイプは、カスタム属性、カスタムイベント、購入イベント、およびユーザー削除です。同期のデータタイプは、作成後に変更できません。 

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 2.1: クラウドデータ取り込みの同期を設定する

Microsoft Fabric 用の新しいデータ同期を作成します。Braze ダッシュボードで、[**データ設定**] > [**クラウドデータ取り込み**] に移動し、[**新規データ同期の作成**] を選択して、[**Microsoft Fabric インポート**] を選択します。

#### ステップ 2.2: Microsoft Fabric の接続情報とソーステーブルの追加

Microsoft Fabric ウェアハウスの認証情報とソーステーブルの情報を入力して、次のステップに進みます。

- 認証情報名は、Braze におけるこれらの認証情報のラベルです。わかりやすい値を設定してください。
- テナント ID、プリンシパル ID、クライアントシークレット、および接続文字列の取得方法については、セクション 1 のステップを参照してください。

#### ステップ 2.3: 同期の詳細の設定

次に、同期のために以下の詳細を設定します。 

- 同期名 
- データタイプ - サポートされるデータタイプは、カスタム属性、カスタムイベント、購入イベント、カタログ、およびユーザー削除です。同期のデータタイプは、作成後に変更できません。 
- 同期頻度 - 頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。 
  - 非定期の同期は、手動または [API]({{site.baseurl}}/api/endpoints/cdi) 経由でトリガーできます。 

#### ステップ 2.4: 通知設定の構成

次に、連絡先のメールアドレスを入力します。この連絡先情報を使用して、テーブルへのアクセスが予期せず削除された場合などの連携エラーの通知や、特定の行の更新に失敗した場合のアラートを送信します。

デフォルトでは、連絡先のメールアドレスには、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみが送信されます。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題には、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- （カタログ同期のみ）カタログ層の容量不足

行レベルの問題に対するアラートを設定したり、同期が正常に実行されるたびにアラートを受け取るように設定したりすることもできます。 

{% endtab %}

{% endtabs %}

### ステップ 3: 接続のテスト

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードに戻り、[**テスト接続**] を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Braze ダッシュボードに戻り、[**テスト接続**] を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。
{% endsubtab %}

{% subtab Private Network %}
Braze ダッシュボードに戻り、[**テスト接続**] を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

同期の設定詳細をすべて入力したら、[**テスト接続**] を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}

{% tab Databricks %}

同期の設定詳細をすべて入力したら、[**テスト接続**] を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}
{% tab Microsoft Fabric %}

同期の設定詳細をすべて入力したら、[**テスト接続**] を選択します。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合は、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

{% endtab %}
{% endtabs %}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、テスト接続に成功する必要があります。作成ページを閉じる必要がある場合でも、連携は保存されるため、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## 追加の連携またはユーザーの設定（オプション）

{% tabs %}
{% tab Snowflake %}
Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Snowflake アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーとロールを再利用する場合、公開キーを追加するステップを再度行う必要は**ありません**。
{% endtab %}
{% tab Redshift %}
Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Snowflake または Redshift アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。
{% endtab %}
{% tab BigQuery %}

Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ BigQuery アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Databricks %}

Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Databricks アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Microsoft Fabric %}

Braze との連携を複数設定できますが、各連携は異なるテーブルを同期するように設定する必要があります。追加の同期を作成する際に同じ Fabric アカウントに接続する場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% endtabs %}

## 同期の実行

{% tabs %}
{% tab Snowflake %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Redshift %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab BigQuery %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Databricks %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}
{% tab Microsoft Fabric %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行されます。通常のスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、[**今すぐ同期**] を選択します。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}

{% endtabs %}

{% enddetails %}
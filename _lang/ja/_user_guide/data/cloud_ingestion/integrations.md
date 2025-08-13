---
nav_title: データウェアハウスの連携
article_title: データウェアハウスの連携
description: "このページでは、Braze のクラウドデータ取り込みを使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# データウェアハウスストレージの連携

> このページでは、Braze のクラウドデータ取り込み (CDI) を使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。

## データウェアハウス統合の設定

クラウドデータ取り込みの連携では、Braze 側とデータウェアハウスインスタンス側で設定がいくつか必要です。次のステップに従って、連携を設定します。

{% tabs %}
{% tab Snowflake %}
1. Snowflake インスタンスで、Braze と同期するテーブルまたはビューを設定します。
2. Braze ダッシュボードで新しい連携を作成します。
3. Braze ダッシュボードに表示された公開キーを取得し、[認証用として Snowflake ユーザーに公開キーを追加](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)します。
4. 連携のテストを行い、同期を開始します。

{% alert tip %}
[Snowflakeクイックスタートガイドでは](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)、サンプルコードを提供し、Snowflake StreamsとCDIを使用して自動パイプラインを作成し、Brazeにデータを同期するために必要なステップを説明する。
{% endalert %}
{% endtab %}
{% tab レッドシフト %}
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
Braze が Classic および Pro の SQL インスタンスに接続するときにウォームアップ時間が 2 〜 5 分かかることがあるため、接続の設定中やテスト中、およびスケジュールされた同期の開始時に遅延が発生します。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、統合に使用する Fabric ワークスペースへのアクセスを許可します。   
2. Fabric ワークスペースで、Braze と同期するテーブルまたはビューを設定します。   
3. Braze ダッシュボードで新しい連携を作成します。  
4. 連携のテストを行い、同期を開始します。
{% endtab %}
{% endtabs %}

### ステップ 1: テーブルまたはビューの設定

{% tabs %}
{% tab Snowflake %}

#### ステップ1.1：テーブルの設定

```json
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
     --If you include both email and phone, we will use the email as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

- `UPDATED_AT` - テーブルで、この行が更新された時刻、または追加された時刻。最後の同期以降に追加されたか、更新された行のみを同期します。
- **ユーザー識別子カラム**\- テーブルには、1つ以上のユーザー識別子カラムを含めることができる。各行は、識別子 (`external_id` 単独か、`alias_name` と `alias_label`、`braze_id`、`email` または `phone` の組み合わせ) を 1 つのみ含まなければなりません。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列が含まれる場合があります。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。 
    - `ALIAS_NAME` および `ALIAS_LABEL` \- この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を 1 つしか持つことができません。
    - `BRAZE_ID` - Braze のユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。
    - `PHONE` - ユーザの電話番号。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列。

#### ステップ1.2：ロールとデータベース権限の設定

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

必要に応じて名前を更新します。ただし、権限は前述の例と一致する必要があります。

#### ステップ1.3：ウェアハウスの設定と、Braze ロールへのアクセス権の付与

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
倉庫は**自動再開**フラグをオンにしておく必要がある。オンにしない場合は、Braze がクエリの実行時にオンにできるように、Braze に追加の `OPERATE` 権限を付与する必要があります。
{% endalert %}

#### ステップ1.4:ユーザーの設定

```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

このステップの後、Braze と接続情報を共有し、ユーザーに追加する公開キーを受け取ります。

{% alert note %}
異なるワークスペースを同じ Snowflake アカウントに接続する場合は、連携を作成する Braze ワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では、複数の連携にわたって同じユーザーを再利用できますが、同じ Snowflake アカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ1.5:Snowflake ネットワークポリシー内で Braze IP を許可 (任意)

Snowflake アカウントの設定によっては、Snowflake のネットワークポリシー内で以下の IP アドレスを許可する必要があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関する Snowflake の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### ステップ1.1：テーブルの設定 

オプションで、ソーステーブルを保持する新規データベースとスキーマを設定します。
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI 連携に使用するテーブル (またはビュー) を作成します。
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, we will use the email as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

データベース、スキーマ、テーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

- `UPDATED_AT` - テーブルで、この行が更新された時刻、または追加された時刻。最後の同期以降に追加されたか、更新された行のみを同期します。
- **ユーザー識別子カラム**\- テーブルには、1つ以上のユーザー識別子カラムを含めることができる。各行は、識別子 (`external_id` 単独か、`alias_name` と `alias_label`、`braze_id`、`email` または `phone` の組み合わせ) を 1 つのみ含まなければなりません。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列が含まれる場合があります。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。 
    - `ALIAS_NAME` および `ALIAS_LABEL` \- この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を 1 つしか持つことができません。
    - `BRAZE_ID` - Braze のユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。
    - `PHONE` - ユーザの電話番号。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列。
 
#### ステップ1.2：ユーザーの作成と権限の付与 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

これらは、このユーザーに最低限必要な権限です。CDI 連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりできます。 

#### ステップ1.3：Braze IP へのアクセスの許可

ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスに Braze ネットワークへのアクセスを許可する必要があります。RedshiftのURLエンドポイントの例は "example-cluster.ap-northeast-2.redshift.amazonaws.com".

知っておくべき重要なことがいくつかある：
- また、Redshift のデータへのアクセスを Braze に許可するように、セキュリティグループを変更しなければならないこともあります。
- テーブル内のIPとRedshiftクラスタへのクエリに使用するポート（デフォルトは5439）のインバウンド・トラフィックを明示的に許可していることを確認する。インバウンドルールが "すべて許可 "に設定されている場合でも、このポートでのRedshiftのTCP接続を明示的に許可する必要がある。
- Braze がクラスターに接続するには、Redshift クラスターのエンドポイントがパブリックにアクセス可能でなければなりません。
     - Redshift クラスターにパブリックアクセスを許可しない場合は、ssh トンネルを使用して Redshift データにアクセスするように VPC と EC2 インスタンスを設定できます。詳細については、この [AWS ナレッジセンターの投稿](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)を参照してください。
 
Brazeダッシュボードの地域に対応する以下のIPからのアクセスを許可する。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### ステップ1.1：テーブルの設定 

オプションで、ソーステーブルを保持する新規のプロジェクトまたはデータセットを設定します。

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持ち、CDI 連携に使用するテーブルを 1 つ以上作成します。

```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| タイムスタンプ | 必須 |
| `PAYLOAD`| JSON | 必須 |
| `EXTERNAL_ID`| 文字列 | NULL 許容 |
| `ALIAS_NAME`| 文字列 | NULL 許容 |
| `ALIAS_LABEL`| 文字列 | NULL 許容 |
| `BRAZE_ID`| 文字列 | NULL 許容 |
| `EMAIL`| 文字列 | NULL 許容 |
| `PHONE`| 文字列 | NULL 許容 |

プロジェクト、データセット、テーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

- `UPDATED_AT` - テーブルで、この行が更新された時刻、または追加された時刻。最後の同期以降に追加されたか、更新された行のみを同期します。
- **ユーザー識別子カラム**\- テーブルには、1つ以上のユーザー識別子カラムを含めることができる。各行は、識別子 (`external_id` 単独か、`alias_name` と `alias_label`、`braze_id`、`email` または `phone` の組み合わせ) を 1 つのみ含まなければなりません。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列が含まれる場合があります。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。 
    - `ALIAS_NAME` および `ALIAS_LABEL` \- この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を 1 つしか持つことができません。
    - `BRAZE_ID` - Braze のユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。
    - `PHONE` - ユーザの電話番号。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。
   email varchar,
   phone_number varchar,
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列。

#### ステップ1.2：サービスアカウントの作成と権限の付与 

GCP で、Braze がテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。 

- **BigQuery 接続ユーザー:**Braze に接続を許可します。
- **BigQuery ユーザー:**クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:**データセットとその内容を表示するためのアクセスを Braze に提供します。
- **BigQuery ジョブユーザー:**ジョブを実行するためのアクセスを Braze に提供します。

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。その方法の詳細については、[こちら](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これは後で Braze ダッシュボードに更新します。 

#### ステップ1.3：Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Braze に Big Query インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### ステップ1.1：テーブルの設定 

オプションとして、ソース・テーブルを保持する新しいカタログまたはスキーマをセットアップする。

```json
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

次のフィールドを持ち、CDI 連携に使用するテーブルを 1 つ以上作成します。


```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| タイムスタンプ | 必須 |
| `PAYLOAD`| STRING、STRUCT、またはMAP。 | 必須 |
| `EXTERNAL_ID`| 文字列 | NULL 許容 |
| `ALIAS_NAME`| 文字列 | NULL 許容 |
| `ALIAS_LABEL`| 文字列 | NULL 許容 |
| `BRAZE_ID`| 文字列 | NULL 許容 |
| `EMAIL`| 文字列 | NULL 許容 |
| `PHONE`| 文字列 | NULL 許容 |

スキーマとテーブルには任意の名前を付けることができますが、列名は先行する定義と一致する必要があります。

- `UPDATED_AT` - テーブルで、この行が更新された時刻、または追加された時刻。最後の同期以降に追加されたか、更新された行のみを同期します。
- **ユーザー識別子カラム**\- テーブルには、1つ以上のユーザー識別子カラムを含めることができる。各行は、識別子 (`external_id` 単独か、`alias_name` と `alias_label`、`braze_id`、`email` または `phone` の組み合わせ) を 1 つのみ含まなければなりません。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列が含まれる場合があります。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。 
    - `ALIAS_NAME` および `ALIAS_LABEL` \- この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を 1 つしか持つことができません。
    - `BRAZE_ID` - Braze のユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。 
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。
    - `PHONE` - ユーザの電話番号。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 
- `PAYLOAD` - Braze でユーザーと同期するフィールドの文字列または構造体。

#### ステップ1.2：アクセストークンを作成する  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名をクリックし、ドロップダウンから [**ユーザー設定**] を選択します。
2. [アクセストークン] タブで、[**新しいトークンの生成**] を選択します。
3. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間 (日)] ボックスを空 (空白) のままにして、トークンの有効期間を有効期間なしに変更します。
4. [**生成**] を選択します。
5. 表示されたトークンをコピーして、[**完了**] を選択します。

認証情報の作成ステップで Braze ダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

#### ステップ1.3：Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Brazeに Databricks インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ1.1：サービスプリンシパルを設定し、アクセスを許可する。
Braze は、Entra ID 認証でサービスプリンシパルを使用して Fabric ウェアハウスに接続します。Braze が使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを許可する。Braze の接続には以下の詳細が必要となります。    

* Azure アカウントのテナント ID (ディレクトリとも呼ばれる) 
* サービスプリンシパルのプリンシパル ID (アプリケーション ID とも呼ばれる) 
* Braze が認証するためのクライアントシークレット

1. Azure portal で、[Microsoft Entra 管理センター]、[アプリの登録] の順に移動します。 
2. [**ID**] > [**アプリケーション**] > [**アプリの登録**] で [**+新規登録**] を選択します。
3. 名前を入力し、サポートされているアカウントの種類として`Accounts in this organizational directory only` を選択します。次に、[**登録**] を選択します。 
4. 作成したアプリケーション（サービスプリンシパル）を選択し、[**Certificates & secrets**] >**[+ New client secret**]の順に移動する。
5. シークレットの説明を入力し、有効期限を設定します。そして、[**追加**] を選択します。 
6. Brazeのセットアップで使用するために作成したクライアントシークレットに注意すること。 

{% alert note %}
Azure では、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Braze へのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ1.2：Fabric リソースへのアクセスを許可する 
BrazeがFabricインスタンスに接続するためのアクセスを提供する。Fabricの管理ポータルで、**「設定」**>「**ガバナンスとインサイト**」>「**管理ポータル**」>「**テナント設定**」の順に移動する。    

* **開発者設定**で、[サービスプリンシパルが Fabric API を使用可能] を有効にして、Braze が Microsoft Entra ID を使用して接続できるようにします。
* **OneLake の設定**で、サービスプリンシパルが外部アプリからデータにアクセスできるように、[ユーザーが Fabric の外部アプリを使用して OneLake に保存されているデータにアクセス可能] を有効にします。


#### ステップ1.3：テーブルの設定
Braze は Fabric ウェアハウスのテーブルとビューの両方をサポートしています。新しいウェアハウスを作成する必要がある場合は、Fabric コンソールで **[作成] > [データウェアハウス] > [ウェアハウス] **と進みます。 

```json
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
  --If you include both email and phone, we will use the email as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

ウェアハウス、スキーマ、テーブルまたはビューには好きな名前をつけることができますが、カラム名は前述の定義と一致させる必要があります。

- `UPDATED_AT` - テーブルで、この行が更新された時刻、または追加された時刻。最後の同期以降に追加されたか、更新された行のみを同期します。
- **ユーザー識別子カラム**\- テーブルには、1つ以上のユーザー識別子カラムを含めることができる。各行は、識別子 (`external_id` 単独か、`alias_name` と `alias_label`、`braze_id`、`email` または `phone` の組み合わせ) を 1 つのみ含まなければなりません。ソーステーブルには、1つ、2つ、3つ、4つ、または5つすべての識別子タイプの列が含まれる場合があります。
    - `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。 
    - `ALIAS_NAME` および `ALIAS_LABEL` \- この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を 1 つしか持つことができません。
    - `BRAZE_ID` - Braze のユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。
    - `EMAIL` - ユーザーのメールアドレス。同じメールアドレスを持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。メールと電話の両方が指定された場合は、メールをプライマリ識別子として使用します。
    - `PHONE` - ユーザの電話番号。同じ電話番号を持つプロファイルが複数存在する場合、最後に更新されたプロファイルが優先されて更新されます。 
- `PAYLOAD` - Braze 内のユーザーと同期するフィールドの JSON 文字列。


#### ステップ1.4:ウェアハウスの接続文字列を取得する 
Brazeを接続するには、倉庫のSQLエンドポイントが必要である。これを取得するには、Fabric で**ワークスペース**に移動し、項目の一覧でウェアハウスの名前にカーソルを合わせ、 [**SQL 接続文字列をコピー**] を選択します。

![ユーザーが SQL 接続文字列を取得する必要がある Microsoft Azure の [Fabric Console] ページ。]{% image_buster /assets/img/cloud_ingestion/fabric_1.png %}


#### ステップ1.5:ファイアウォールで Braze IP を許可する（オプション）

Microsoft Fabric アカウントの設定によっては、Braze からのトラフィックを許可するように、ファイアウォールで以下の IP アドレスを許可する必要があります。これを有効にする方法の詳細については、[Entra Conditional Access ](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### ステップ 2: Braze ダッシュボードでの新規連携の作成

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードで [**データ設定**] > [**クラウドデータ取り込み**] > の順に移動し、［**新しいデータ同期を作成**] を選択し ［**Snowflake のインポート**] を選択します。

#### ステップ 2.1:Snowflake の接続情報とソーステーブルの追加

Snowflake データウェアハウスとソーステーブルの情報を入力して、次のステップに進みます。

![Braze ダッシュボードの Snowflake の [新しいインポート同期の作成] ページには、ステップ1で入力したデータの例が表示されます。「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_1.png %}

#### ステップ 2.2:同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなど、連携エラーの通知に使用されます。

連絡先のメールアドレスは、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみを受け取ります。行レベルの問題を受け取ることはありません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題として、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- (カタログ同期のみ) カタログ層の容量不足

![Braze ダッシュボードの Snowflake の [新しいインポート同期の作成] ページには、ステップ2に追加されたデータの例が表示されます。同期の詳細を設定]{% image_buster /assets/img/cloud_ingestion/ingestion_2.png %}

データ型と同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、および購入イベントです。同期のデータ型は、作成後に変更できません。 

#### Braze ユーザーへの公開キーの追加

この時点で、Snowflake に戻って設定を完了する必要があります。ダッシュボードに表示されている公開キーを、Snowflake に Braze を接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でのキーのローテーションを行う場合、新規のキーペアを生成して、新規の公開キーを提供できます。

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```
{% endtab %}
{% tab Redshift %}

Braze ダッシュボードで [**データ設定**] > [**クラウドデータ取り込み**] > の順に移動し、［**新しいデータ同期を作成**] を選択し ［**Amazon Redshift のインポート**] を選択します。

#### ステップ 2.1:Redshift の接続情報とソーステーブルの追加

Redshift データウェアハウスとソーステーブルの情報を入力します。プライベート・ネットワーク・トンネルを使用している場合は、スライダーを切り替えてトンネル情報を入力する。その後、次のステップに進みます。

![Braze ダッシュボードの Redshift 用 [新しいインポート同期を作成] ページ、ステップ1に設定「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_6.png %}

#### ステップ 2.2:同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなど、連携エラーの通知に使用されます。

連絡先のメールアドレスは、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみを受け取ります。行レベルの問題を受け取ることはありません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題として、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- (カタログ同期のみ) カタログ層の容量不足

![Braze ダッシュボードの Redshift 用の [新しいインポート同期の作成] ページには、ステップ2に追加されたデータのいくつかの例が表示されます。同期の詳細を設定]{% image_buster /assets/img/cloud_ingestion/ingestion_7.png %}

データ型と同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、および購入イベントです。同期のデータ型は、作成後に変更できません。
{% endtab %}
{% tab BigQuery %}

Braze ダッシュボードで [**データ設定**] > [**クラウドデータ取り込み**] > の順に移動し、［**新しいデータ同期を作成**] を選択し ［**Google BigQuery のインポート**] を選択します。

#### ステップ 2.1:BigQuery の接続情報とソーステーブルの追加

JSON キーをアップロードし、サービスアカウントの名前を入力して、ソーステーブルの詳細を入力します。

![Braze ダッシュボードの BigQuery 用 [新しいインポート同期を作成] ページ、ステップ1に設定「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_11.png %}

#### ステップ 2.2:同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなど、連携エラーの通知に使用されます。

連絡先のメールアドレスは、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみを受け取ります。行レベルの問題を受け取ることはありません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題として、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- (カタログ同期のみ) カタログ層の容量不足

![Braze ダッシュボードの BigQuery 用 [新しいインポート同期を作成] ページ、ステップ2に設定同期の詳細を設定]{% image_buster /assets/img/cloud_ingestion/ingestion_12.png %}

データ型と同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、購入イベント、およびユーザー削除です。同期のデータ型は、作成後に変更できません。 

{% endtab %}
{% tab Databricks %}

Braze ダッシュボードで [**データ設定**] > [**クラウドデータ取り込み**] > の順に移動し、［**新しいデータ同期を作成**] を選択し ［**Databricks のインポート**] を選択します。

#### ステップ 2.1:Databricks の接続情報とソーステーブルの追加

Databricks データウェアハウスとソーステーブルの情報を入力して、次のステップに進みます。

![Braze ダッシュボードの Databricks 用 [新しいインポート同期を作成] ページ、ステップ1に設定「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_16.png %}

#### ステップ 2.2:同期の詳細の設定

次に、同期の名前を選択し、連絡先のメールアドレスを入力します。この連絡先情報は、テーブルへのアクセスが予期せず削除されたなど、連携エラーの通知に使用されます。

連絡先のメールアドレスは、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみを受け取ります。行レベルの問題を受け取ることはありません。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題として、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- (カタログ同期のみ) カタログ層の容量不足

![Braze ダッシュボードの Databricks 用 [新しいインポート同期を作成] ページ、ステップ2に設定同期の詳細を設定]{% image_buster /assets/img/cloud_ingestion/ingestion_12.png %}

データ型と同期頻度も選択します。頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。サポートされているデータ型は、カスタム属性、カスタムイベント、購入イベント、およびユーザー削除です。同期のデータ型は、作成後に変更できません。 

{% endtab %}
{% tab Microsoft Fabric %}

#### ステップ 2.1:クラウドデータ取り込みの同期を設定する

Microsoft Fabric 用の新しいデータ同期を作成します。Braze ダッシュボードで [**データ設定**] > [**クラウドデータ取り込み**] > の順に移動し、［**新しいデータ同期を作成**] を選択し ［**Microsoft Fabricks のインポート**] を選択します。

#### ステップ 2.2:Microsoft Fabricの接続情報とソーステーブルを追加する

Microsoft Fabric ウェアハウスの認証情報とソーステーブルの情報を入力して、次のステップに進みます。

- 認証情報名は、Braze におけるこれらの認証情報のラベルであり、ここでわかりやすい値を設定することができます。
- テナント ID、プリンシパル ID、クライアントシークレット、および接続文字列を取得する方法の詳細については、セクション1のステップを参照してください。

![Braze ダッシュボードの iMicrosoft 用 [新しいインポート同期を作成] ページ、ステップ1に設定「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/fabric_setup_1.png %}

#### ステップ 2.3:同期の詳細の設定

次に、同期のために以下の詳細を設定する： 

- 同期名 
- データタイプ - サポートされるデータタイプは、カスタム属性、カスタムイベント、購入イベント、カタログ、およびユーザー削除である。同期のデータ型は、作成後に変更できません。 
- 同期の頻度 - 頻度の範囲は 15 分間隔から 1 か月に 1 回までです。Braze ダッシュボードで設定したタイムゾーンを使用して、定期的な同期がスケジュールされます。 
  - 定期的でない同期は、手動または [API]({{site.baseurl}}/api/endpoints/cdi) 経由でトリガーできます。 

![Braze ダッシュボードの Microsoft Fabric 用 [新しいインポート同期を作成] ページ、ステップ2に設定同期の詳細を設定]{% image_buster /assets/img/cloud_ingestion/fabric_setup_2.png %}


#### ステップ 2.4:通知設定を行う

次に、コンタクトメールを入力します。この連絡先情報を使用して、テーブルへのアクセスが予期せず削除された場合などの統合エラーを通知したり、特定の行の更新に失敗した場合に警告を発したりする。

デフォルトでは、連絡先のメールアドレスは、テーブルや権限の欠落など、グローバルまたは同期レベルのエラーの通知のみを受け取ります。グローバルエラーは、同期の実行を妨げる接続の重大な問題を示します。このような問題として、次のようなものがあります。

- 接続の問題
- リソース不足
- 権限の問題
- (カタログ同期のみ) カタログ層の容量不足

行レベルの問題に対するアラートを設定することもできるし、同期が正常に実行されるたびにアラートを受け取るようにすることもできる。 

![Braze ダッシュボードの Microsoft Fabric 用 [新しいインポート同期を作成] ページ、ステップ3に設定通知設定を指定]{% image_buster /assets/img/cloud_ingestion/fabric_setup_3.png %}


{% endtab %}

{% endtabs %}

### ステップ 3: テスト接続

{% tabs %}
{% tab Snowflake %}

Braze ダッシュボードに戻って、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Snowflake の [新しいインポート同期の作成] ページのステップ3。RSA公開キーを表示する "テスト接続"]({% image_buster /assets/img/cloud_ingestion/ingestion_3.png %})
{% endtab %}

{% tab Redshift %}
{% subtabs local %}
{% subtab Public Network %}
Braze ダッシュボードに戻って、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Redshift 用 [新しいインポート同期を作成] ページ、ステップ3に設定テスト接続]{% image_buster /assets/img/cloud_ingestion/ingestion_8.png %}
{% endsubtab %}

{% subtab Private Network %}
Braze ダッシュボードに戻って、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Redshift プライベートネットワークの [新しいインポート同期の作成] ページのステップ4。RSA公開キーを表示する "テスト接続"]({% image_buster /assets/img/cloud_ingestion/ingestion_19.png %})
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}

同期の設定の詳細をすべて入力したら、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの BigQuery 用 [新しいインポート同期を作成] ページ、ステップ3に設定テスト接続]{% image_buster /assets/img/cloud_ingestion/ingestion_13.png %}

{% endtab %}

{% tab Databricks %}

同期の設定の詳細をすべて入力したら、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Databricks 用 [新しいインポート同期を作成] ページ、ステップ3に設定テスト接続]{% image_buster /assets/img/cloud_ingestion/ingestion_13.png %}

{% endtab %}
{% tab Microsoft Fabric %}

同期の設定の詳細をすべて入力したら、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続できない場合、問題のトラブルシューティングに役立つエラーメッセージが表示されます。

![Braze ダッシュボードの Microsoft Fabric 用 [新しいインポート同期を作成] ページ、ステップ4に設定テスト接続]{% image_buster /assets/img/cloud_ingestion/fabric_setup_4.png %}

{% endtab %}
{% endtabs %}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、連携のテストに成功する必要があります。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## 追加の連携またはユーザーの設定 (オプション)

{% tabs %}
{% tab Snowflake %}
Braze との連携を複数設定することもできますが、各連携で異なるテーブルを同期するように設定する必要があります。追加の同期を作成するときに Snowflake アカウントに接続している場合は、既存の認証情報を再利用できます。

![Braze ダッシュボードの Snowflake の [新しいインポート同期の作成] ページ、ステップ1で [認証情報を選択] ドロップダウンが開いている。「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_4.png %}

複数の連携にわたって同じユーザーとロールを再利用する場合、公開キーを追加するステップを再び行う必要は**ありません**。
{% endtab %}
{% tab レッドシフト %}
Braze との連携を複数設定することもできますが、各連携で異なるテーブルを同期するように設定する必要があります。追加の同期を作成するときに同じ Snowflake または Redshift のアカウントに接続している場合は、既存の認証情報を再利用できます。

![Braze ダッシュボード の Redshift 用 [新しいインポート同期を作成] ページ、ステップ1で [認証情報を選択] ドロップダウンが開いている「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_9.png %}

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。
{% endtab %}
{% tab BigQuery %}

Braze との連携を複数設定することもできますが、各連携で異なるテーブルを同期するように設定する必要があります。追加の同期を作成するときに同じ BigQuery アカウントに接続している場合は、既存の認証情報を再利用できます。

![Braze ダッシュボード の BigQuery 用 [新しいインポート同期を作成] ページ、ステップ1で [認証情報を選択] ドロップダウンが開いている「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_14.png %}

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Databricks %}

Braze との連携を複数設定することもできますが、各連携で異なるテーブルを同期するように設定する必要があります。追加の同期を作成するときに同じ Databricks アカウントに接続している場合は、既存の認証情報を再利用できます。

![Braze ダッシュボードの Databricks の [新しいインポート同期の作成] ページ、ステップ1で [認証情報を選択] ドロップダウンが開いている。「接続を設定します」]{% image_buster /assets/img/cloud_ingestion/ingestion_17.png %}

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% tab Microsoft Fabric %}

Braze との連携を複数設定することもできますが、各連携で異なるテーブルを同期するように設定する必要があります。追加の同期を作成するときに同じ Fabric アカウントに接続している場合は、既存の認証情報を再利用できます。

複数の連携にわたって同じユーザーを再利用している場合、すべてのアクティブな同期から削除されるまで、Braze ダッシュボードでそのユーザーを削除することはできません。

{% endtab %}
{% endtabs %}

## 同期の実行

{% tabs %}
{% tab Snowflake %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行される。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、「**今すぐ同期**」を選択する。この実行は、定期的にスケジュールされている将来の同期には影響しません。

![Braze ダッシュボードの Snowflake 用 [データインポート] ページで、縦の省略記号メニューから [今すぐ同期] オプションが表示されている状態]({% image_buster /assets/img/cloud_ingestion/ingestion_5.png %})

{% endtab %}
{% tab Redshift %}
有効にすると、セットアップ時に設定したスケジュールで同期が実行される。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、「**今すぐ同期**」を選択する。この実行は、定期的にスケジュールされている将来の同期には影響しません。

![「Braze ダッシュボードの Redshift 用 [データインポート] ページで、縦の省略記号メニューから [今すぐ同期] オプションが表示されている状態]({% image_buster /assets/img/cloud_ingestion/ingestion_10.png %})

{% endtab %}
{% tab BigQuery %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行される。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、「**今すぐ同期**」を選択する。この実行は、定期的にスケジュールされている将来の同期には影響しません。

![Braze ダッシュボードの BigQuery 用 [データインポート] ページで、縦の省略記号メニューから [今すぐ同期] オプションが表示されている状態]({% image_buster /assets/img/cloud_ingestion/ingestion_15.png %})

{% endtab %}
{% tab Databricks %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行される。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、「**今すぐ同期**」を選択する。この実行は、定期的にスケジュールされている将来の同期には影響しません。

![Braze ダッシュボードの Databricks 用 [データインポート] ページで、縦の省略記号メニューから [今すぐ同期] オプションが表示されている状態]({% image_buster /assets/img/cloud_ingestion/ingestion_18.png %})

{% endtab %}
{% tab Microsoft Fabric %}

有効にすると、セットアップ時に設定したスケジュールで同期が実行される。通常のテストスケジュール以外で同期を実行したい場合や、最新のデータを取得したい場合は、「**今すぐ同期**」を選択する。この実行は、定期的にスケジュールされている将来の同期には影響しません。

{% endtab %}

{% endtabs %}


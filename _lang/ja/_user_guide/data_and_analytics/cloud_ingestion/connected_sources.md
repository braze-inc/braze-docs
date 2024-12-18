---
nav_title: 接続されたソース
article_title: 接続されたソース
description: "このリファレンス記事では、Braze のクラウドデータ取り込みを使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# 接続されたソース

> 接続されたソースは、Braze の CDI (クラウドデータ取り込み) 機能を使ってデータを直接同期するのではなく、ゼロコピーの代替手段です。接続ソースでは、データウェアハウスに直接クエリを行い、基盤となるデータを Braze に一切コピーせずに新しいセグメントを作成します。 

接続ソースを Braze ワークスペースに追加すると、セグメントエクステンション内に CDI セグメントを作成できます。CDI セグメントを使用すると、(CDI の接続ソース経由で利用可能なデータを使用して) データウェアハウスに直接クエリを行う SQL を記述し、Braze 内でターゲットに設定できるユーザーグループを作成して管理することができます。 

このソースでセグメントを作成する方法の詳細については、「[CDI セグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)」を参照してください。

{% alert warning %}
接続されたソースはデータウェアハウス上で直接実行されるため、データウェアハウスでこれらのクエリの実行に関連するすべてのコストが発生します。接続されたソースはデータポイントを消費せず、CDIセグメントはSQLセグメント・クレジットを消費しない。
{% endalert %}

## 接続されたソースの統合

### ステップ 1:リソースをつなぐ

クラウドデータ取り込みの接続されたソースは、Braze 側とインスタンス側での設定を必要とします。統合を設定するには、次の手順に従います。この一部はデータウェアハウスで実行され、一部はBraze ダッシュボードで実行されます。

{% tabs %}
{% tab Snowflake %}
**データウェアハウスで次を行います。**
1. ロールを作成し、スキーマ内のテーブルのクエリと作成の権限を付与する。
2. 倉庫を設定し、そのロールにアクセス権を与える。
3. そのロールのユーザーを作成する。
4. 設定によっては、Snowflake ネットワークポリシーで Braze IP を許可する必要があります。

**Braze ダッシュボードで次を行います。**

{: start="5"}
5. Braze ダッシュボードで接続されたソースを新規作成する。
6. 接続されたソースの同期の詳細を設定する。
7. Braze ダッシュボードで提供された公開鍵を取得する。

**データウェアハウスで次を行います。**

{: start="8"}
8. Braze ダッシュボードの公開鍵を[認証用の Snowflake ユーザー](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)に追加する。完了したら、接続されたソースを使用して1つ以上のCDIセグメントを作成できる。
{% endtab %}

{% tab Redshift %}
1. Redshift環境にソースデータと必要なリソースをセットアップする。
2. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1 つ以上の CDI セグメントを作成する。
{% endtab %}

{% tab BigQuery %}
1. BigQuery環境でソースデータと必要なリソースをセットアップする。
2. サービスアカウントを作成し、同期するデータを含む BigQuery のプロジェクトとデータセットへのアクセスを許可します。  
3. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1 つ以上の CDI セグメントを作成する。
{% endtab %}

{% tab Databricks %}
1. Databricks 環境でソースデータと必要なリソースをセットアップする。
2. サービスアカウントを作成し、同期するデータを含む Databricks のプロジェクトとデータセットへのアクセスを許可します。  
3. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1 つ以上の CDI セグメントを作成する。

{% alert important %}
Braze が Classic および Pro の SQL インスタンスに接続するときウォームアップに 2 ～ 5 分かかる場合があり、接続の設定中やテスト中、および CDI セグメントの作成と更新中に遅延が発生します。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ 2:データウェアハウスをセットアップする

データウェアハウス環境でソースデータと必要なリソースを設定します。接続ソースは1つまたは複数のテーブルを参照する可能性があるため、Brazeユーザーが接続ソース内の必要なすべてのテーブルにアクセスできる権限を持っていることを確認する。

{% tabs %}
{% tab Snowflake %}
#### ステップ 2.1:ロールを作成し、権限を付与する

接続ソースが使用するロールを作成する。このロールは、CDI セグメントで使用可能なテーブルのリストを生成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Braze ロールがアクセスできるテーブルは、CDI セグメントでクエリすることができます。

Braze でセグメントを更新する前に、Braze が CDI セグメントのクエリ結果を使用してテーブルを作成できるようにするには、`create table` 権限が必要です。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。

```json
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### ステップ 2.2:ウェアハウスの設定と、Braze ロールへのアクセス権の付与

```json
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
ウェアハウスの**自動再開**フラグをオンにする必要があります。そうでない場合は、Braze がクエリの実行時にオンにできるように、Braze に追加の `OPERATE` 権限を付与する必要があります。
{% endalert %}

#### ステップ 2.3:ユーザーの設定
```json
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Brazeと接続情報を共有し、後のステップでユーザーに付加する公開鍵を受け取る。

{% alert note %}
異なるワークスペースを同じ Snowflake アカウントに接続する場合は、連携を作成する Braze ワークスペースごとに一意のユーザーを作成する必要があります。ワークスペース内では、複数の連携にわたって同じユーザーを再利用できますが、同じ Snowflake アカウントのユーザーが複数のワークスペースで重複すると、連携の作成に失敗します。
{% endalert %}

#### ステップ 2.4:Snowflake ネットワークポリシー内で Braze IP を許可する (省略可)

Snowflake アカウントの設定によっては、Snowflake のネットワークポリシー内で以下の IP アドレスを許可する必要があります。この方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関する Snowflake の関連ドキュメントを参照してください。

{% subtabs %}
{% subtab United States (US) %}
インスタンス `US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、`US-07` の場合、関連する IP アドレスは次のとおりです。
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
インスタンス `EU-01` と `EU-02` の場合、関連する IP アドレスは次のとおりです。
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Redshift %}
#### ステップ 2.1:ユーザーの作成と権限の付与 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

接続ソースが使用するユーザーを作成する。このユーザは、CDI セグメントで使用可能なテーブルのリストを作成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。CDI 連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりできます。 

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Braze ロールがアクセスできるテーブルは、CDI セグメントでクエリすることができます。新しいテーブルを作成する際には、必ずそのユーザーにアクセス権を与えるか、そのユーザーにデフォルトのアクセス権を設定する。 

Braze でセグメントを更新する前に、Braze が CDI セグメントのクエリ結果を使用してテーブルを作成できるようにするには、`create table` 権限が必要です。Brazeはセグメントごとにテンポラリテーブルを作成し、Brazeがセグメンテーションを更新している間だけ持続する。


#### ステップ 2.2:Braze IP へのアクセスの許可    

ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスに Braze ネットワークへのアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。 

また、Redshift のデータへのアクセスを Braze に許可するように、セキュリティグループを変更しなければならないこともあります。以下の IP と Redshift クラスターのクエリに使用するポート (デフォルトは 5439) のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートで Redshift TCP 接続を明示的に許可する必要があります。さらに、Braze がクラスターに接続するために、Redshift クラスターのエンドポイントがパブリックにアクセス可能であることが重要です。

Redshift クラスターにパブリックアクセスを許可しない場合は、ssh トンネルを使用して Redshift データにアクセスするように VPC と EC2 インスタンスを設定できます。詳しくは、[AWSを参照のこと：ローカルマシンからAmazon Redshiftのプライベートクラスタにアクセスするには？](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% subtabs %}
{% subtab United States (US) %}
インスタンス `US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、`US-07` の場合、関連する IP アドレスは次のとおりです。
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
インスタンス `EU-01` と `EU-02` の場合、関連する IP アドレスは次のとおりです。
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab BigQuery %}
#### ステップ 2.1:サービスアカウントの作成と権限の付与 

GCP で、Braze がテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。 

- **BigQuery 接続ユーザー:**Braze に接続を許可します。
- **BigQuery ユーザー:**クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:**データセットとその内容を閲覧するためのBrazeアクセスを提供する。
- **BigQuery ジョブユーザー:**ジョブを実行するためのBrazeアクセスを提供する。
- **bigquery.tables.create** セグメント更新時に一時テーブルを作成するためのアクセスを Braze に提供します。

接続するソースが使用するサービスアカウントを作成する。このユーザは、CDI セグメントで使用可能なテーブルのリストを作成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。 

データセット内のすべてのテーブルにアクセス権を与えるか、特定のテーブルだけに権限を与えるかを選択できる。Braze ロールがアクセスできるテーブルは、CDI セグメントでクエリすることができます。 

Braze でセグメントを更新する前に、Braze が CDI セグメントのクエリ結果を使用してテーブルを作成できるようにするには、`create table` 権限が必要です。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。 

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳細は、[Google Cloudを参照のこと：サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これを後でBrazeのダッシュボードにアップロードする。

#### ステップ 2.2:Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Braze に Big Query インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% subtabs %}
{% subtab United States (US) %}
インスタンス `US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、`US-07` の場合、関連する IP アドレスは次のとおりです。
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
インスタンス `EU-01` と `EU-02` の場合、関連する IP アドレスは次のとおりです。
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Databricks %}
#### ステップ 2.1:アクセストークンを作成する  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名をクリックし、ドロップダウンから [**ユーザー設定**] を選択します。
2. サービスアカウントに、接続されたソースに使用されているスキーマに対する `CREATE TABLE` 権限があることを確認します。 
3. [**アクセストークン**] タブで、[**新しいトークンの生成**] を選択します。
4. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間 (日)] ボックスを空 (空白) のままにして、トークンの有効期間を有効期間なしに変更します。
5. [**生成**] を選択します。
6. 表示されたトークンをコピーして、[**完了**] を選択します。

このトークンは、CDI セグメントで使用可能なテーブルの一覧を生成したり、 新しいセグメントを作成するためにソーステーブルをクエリしたりする際に使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。 

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Braze ロールがアクセスできるテーブルは、CDI セグメントでクエリすることができます。

Braze でセグメントを更新する前に、Braze が CDI セグメントのクエリ結果を使用してテーブルを作成できるようにするには、`create table` 権限が必要です。Brazeはセグメントごとにテンポラリテーブルを作成し、Brazeがセグメンテーションを更新している間だけ持続する。 

認証情報の作成ステップで Braze ダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

#### ステップ 2.2:Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Brazeに Databricks インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% subtabs %}
{% subtab United States (US) %}
インスタンス `US-01`、`US-02`、`US-03`、`US-04`、`US-05`、`US-06`、`US-07` の場合、関連する IP アドレスは次のとおりです。
- `23.21.118.191`
- `34.206.23.173`
- `50.16.249.9`
- `52.4.160.214`
- `54.87.8.34`
- `54.156.35.251`
- `52.54.89.238`
- `18.205.178.15`
{% endsubtab %}

{% subtab European Union (EU) %}
インスタンス `EU-01` と `EU-02` の場合、関連する IP アドレスは次のとおりです。
- `52.58.142.242`
- `52.29.193.121`
- `35.158.29.228`
- `18.157.135.97`
- `3.123.166.46`
- `3.64.27.36`
- `3.65.88.25`
- `3.68.144.188`
- `3.70.107.88`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 3:Brazeダッシュボードで接続ソースを作成する。

{% tabs %}
{% tab Snowflake %}
#### ステップ 3.1:Snowflake の接続情報とソーステーブルの追加

Brazeダッシュボードで接続ソースを作成する。[**データ設定**] > [**クラウドデータ取り込み**] > ［**接続されたソース**] の順に移動し、［**新しいデータ同期を作成**] > ［**Snowflake のインポート**] を選択します。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Snowflakeデータウェアハウスとソーススキーマの情報を入力し、次のステップに進む。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### ステップ 3.2:同期の詳細の設定

接続するソースの名前を選択する。この名前は、新しい CDI セグメントの作成時に使用可能なソースのリストで使用されます。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は 60 分です。実行時間を短くすると、Snowflake アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### ステップ3.3：公開鍵を書き留める  

[**テスト接続**] ステップに表示されている RSA 公開鍵をメモします。Snowflakeでの統合を完了させるために必要だ。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% tab Redshift %}
#### ステップ 3.1:Redshift の接続情報とソーステーブルの追加

Brazeダッシュボードで接続ソースを作成する。[**データ設定**] > [**クラウドデータ取り込み**] > ［**接続されたソース**] の順に移動し、［**新しいデータ同期を作成**] > ［**Amazon Redshift のインポート**] を選択します。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Redshiftデータウェアハウスとソーススキーマの情報を入力し、次のステップに進む。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_1.png %})

#### ステップ 3.2:同期の詳細の設定

接続するソースの名前を選択する。この名前は、新しい CDI セグメントの作成時に使用可能なソースのリストで使用されます。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は60分です。実行時間を短くすると、Redshift アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_2.png %})

#### ステップ3.3：公開鍵を書き留める (省略可能)

認証情報で [**SSH トンネルで接続**] が選択されている場合は、[**テスト接続**] ステップに表示されている RSA 公開鍵をメモします。Redshiftでの統合を完了するために必要だ。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rd_3.png %})

{% endtab %}
{% tab BigQuery %}
#### ステップ 3.1:BigQuery の接続情報とソーステーブルの追加

Brazeダッシュボードで接続ソースを作成する。[**データ設定**] > [**クラウドデータ取り込み**] > ［**接続されたソース**] の順に移動し、［**新しいデータ同期を作成**] > ［**Google BigQuery のインポート**] を選択します。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

BigQueryプロジェクトとデータセットの情報を入力し、次のステップに進む。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_1.png %})

#### ステップ 3.2:同期の詳細の設定

接続するソースの名前を選択する。この名前は、新しい CDI セグメントの作成時に使用可能なソースのリストで使用されます。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は60分です。実行時間を短くすると、BigQuery アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### ステップ3.3：接続をテストする

[**テスト接続**] を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### ステップ 3.1:Databricks の接続情報とソーステーブルの追加

Brazeダッシュボードで接続ソースを作成する。[**データ設定**] > [**クラウドデータ取り込み**] > ［**接続されたソース**] の順に移動し、［**新しいデータ同期を作成**] > ［**Databricks のインポート**] を選択します。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Databricks 認証情報、オプションのカタログとソーススキーマの情報を入力してから、次のステップに進みます。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### ステップ 3.2:同期の詳細の設定

接続するソースの名前を選択する。この名前は、新しい CDI セグメントの作成時に使用可能なソースのリストで使用されます。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は60分です。実行時間を短くすると、Databricks アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### ステップ3.3：接続をテストする

[**テスト接続**] を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:データウェアハウスの構成を確定する

{% tabs %}
{% tab Snowflake %}
最後の手順で書き留めた公開鍵を Snowflake のユーザーに追加します。これで Braze は、Snowflake に接続できるようになります。この方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。 

任意の時点で鍵のローテーションを行う場合は、新しい公開鍵を作成できます。このためには、［**クラウドデータ取り込み**] の ［**データアクセス管理**] に移動し、該当するアカウントの ［**新しいキーを生成**] を選択します。

![「新しいキーを生成」ボタンが表示されている「データアクセス管理」の「Snowflake データアクセス認証情報」。]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflake でユーザーに鍵を追加したら、Braze で [**テスト接続**] を選択し、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。
{% endtab %}

{% tab Redshift %}
SSHトンネルで接続する場合は、最後のステップで記した公開キーをSSHトンネル・ユーザーに追加する。 

ユーザーに鍵を追加したら、Braze で [**テスト接続**] を選択し、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。

{% endtab %}
{% tab BigQuery %}
これはBigQueryには当てはまらない。

{% endtab %}
{% tab Databricks %}
これは Databricks には適用されません。

{% endtab %}
{% endtabs %}

{% alert note %}
「下書き」状態から「アクティブ」状態に移行する前に、ソースのテストに成功する必要があります。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## 追加の統合またはユーザーを設定する（オプション）

{% tabs %}
{% tab Snowflake %}
Brazeと複数の統合を設定することができるが、各統合は異なるスキーマを接続するように設定する必要がある。追加の接続を作成する際、同じ Snowflake アカウントに接続する場合は既存の認証情報を再利用できます。

同じユーザーとロールを統合間で再利用する場合、公開キーを再度追加する必要はありません。
{% endtab %}

{% tab Redshift %}
Braze で複数のソースを設定できますが、各ソースは異なるスキーマを接続するように設定する必要があります。追加ソースを作成する際、同じ Redshift アカウントに接続する場合は、既存の認証情報を再利用できる。
{% endtab %}

{% tab BigQuery %}
Brazeで複数のソースを設定することもできるが、各ソースは異なるデータセットを接続するように設定する必要がある。追加のソースを作成する際、同じ BigQuery アカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}

{% tab Databricks %}
Braze で複数のソースを設定できますが、各ソースは異なるスキーマを接続するように設定する必要があります。追加ソースを作成する際、同じ Databricks アカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}
{% endtabs %}

## 接続されたソースの使用

ソースが作成されると、それを使用して1つまたは複数の CDI セグメントを作成できます。このソースでセグメントを作成する方法の詳細については、[CDI セグメントのドキュメント]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)を参照してください。

{% alert note %}
クエリが一貫してタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、より多くの計算リソース (より大きなウェアハウスなど) を Braze ユーザーに割り当てることを検討してください。
{% endalert %}

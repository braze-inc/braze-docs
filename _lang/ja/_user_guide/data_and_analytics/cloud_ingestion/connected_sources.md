---
nav_title: コネクテッド・ソース
article_title: コネクテッド・ソース
description: "このリファレンス記事では、Braze のクラウドデータ取り込みを使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# コネクテッド・ソース

> 接続されたソースは、BrazeのCDI（Cloud Data Ingestion）機能を使ってデータを直接同期するゼロコピーの代替手段である。接続されたソースがあれば、データウェアハウスに直接クエリを発行して新しいセグメントを作成できる。 

接続ソースをBrazeワークスペースに追加したら、Segment ExtensionsでCDIセグメントを作成できる。CDIセグメントを使用すると、（CDIコネクテッドソース経由で利用可能なデータを使用して）独自のデータウェアハウスに直接クエリを実行するSQLを記述し、Braze内でターゲットとなるユーザーグループを作成して管理できる。 

このソースでセグメントを作成する詳細については、[CDI Segmentsのドキュメントを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)参照のこと。

{% alert warning %}
接続されたソースはデータウェアハウス上で直接実行されるため、データウェアハウスでこれらのクエリを実行することに関連するすべてのコストが発生する。接続されたソースはデータ・ポイントを消費せず、CDI セグメントは SQL セグメント・クレジットを消費しない。
{% endalert %}

## 接続されたソースを統合する

### ステップ 1:リソースをつなぐ

Cloud Data Ingestionの接続ソースは、Braze側とインスタンス側でいくつかのセットアップを必要とする。いくつかのステップはデータウェアハウスで行い、いくつかのステップはBrazeダッシュボードで行う。

{% tabs %}
{% tab Snowflake %}
**データウェアハウス**
1. ロールを作成し、スキーマ内のテーブルのクエリと作成の権限を付与する。
2. 倉庫を設定し、そのロールにアクセス権を与える。
3. そのロールのユーザーを作成する。
4. 構成によっては、SnowflakeネットワークポリシーでBraze IPを許可する必要がある。

**ブレイズのダッシュボード**

{: start="5"}
5. Brazeダッシュボードで新しい接続ソースを作成する。
6. 接続されているソースのシンク詳細を設定する。
7. Brazeダッシュボードで提供された公開鍵を取得する。

**データウェアハウス**

{: start="8"}
8. Brazeダッシュボードの公開鍵を[認証用のSnowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)ユーザーに追加する。完了したら、接続されたソースを使用して1つ以上のCDIセグメントを作成できる。
{% endtab %}

{% tab Redshift %}
1. Redshift環境にソースデータと必要なリソースをセットアップする。
2. Brazeダッシュボードで新しい接続ソースを作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントを作成する。
{% endtab %}

{% tab BigQuery %}
1. BigQuery環境でソースデータと必要なリソースをセットアップする。
2. サービスアカウントを作成し、同期するデータを含む BigQuery のプロジェクトとデータセットへのアクセスを許可します。  
3. Brazeダッシュボードで新しい接続ソースを作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントを作成する。
{% endtab %}

{% tab Databricks %}
1. Databricks 環境でソースデータと必要なリソースをセットアップする。
2. サービスアカウントを作成し、同期するデータを含む Databricks のプロジェクトとデータセットへのアクセスを許可します。  
3. Brazeダッシュボードで新しい接続ソースを作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントを作成する。

{% alert important %}
BrazeがClassicおよびPro SQLインスタンスに接続する際、ウォームアップ時間が2～5分かかる場合があり、接続のセットアップとテスト中、およびCDIセグメントの作成と更新中に遅延が発生する。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}
{% endtabs %}

### ステップ2:データウェアハウスをセットアップする

まず、データウェアハウス環境にソースデータと必要なリソースをセットアップする。接続ソースは1つまたは複数のテーブルを参照する可能性があるため、Brazeユーザーが接続ソースで使用したいすべてのテーブルの権限を持っていることを確認する。

{% tabs %}
{% tab Snowflake %}
#### ステップ 2.1:ロールを作成し、権限を付与する

接続ソースが使用するロールを作成する。このロールは、CDI セグメントで使用可能なテーブルのリストを生成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントでクエリーできる。

Brazeでセグメントを更新する前に、BrazeがCDIセグメントのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。

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
ウェアハウスの**自動再開**フラグをオンにする必要があります。そうでない場合は、Brazeがクエリを実行するときにオンにできるように、Brazeに追加の`OPERATE` 権限を付与する必要がある。
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

#### ステップ 2.4:Snowflake ネットワークポリシー内で Braze IP を許可 (任意)

Snowflake アカウントの設定によっては、Snowflake のネットワークポリシー内で以下の IP アドレスを許可する必要があります。これを有効にする方法の詳細については、[ネットワークポリシーの変更](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)に関する Snowflake の関連ドキュメントを参照してください。

{% subtabs %}
{% subtab United States (US) %}
インスタンス`US-01` 、`US-02` 、`US-03` 、`US-04` 、`US-05` 、`US-06` 、`US-07` 、これらは関連するIPアドレスである：
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
インスタンス`EU-01` と`EU-02` 、これらは関連するIPアドレスである：
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

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントでクエリーできる。新しいテーブルを作成する際には、必ずそのユーザーにアクセス権を与えるか、そのユーザーにデフォルトのアクセス権を設定する。 

 Brazeでセグメントを更新する前に、BrazeがCDIセグメントのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。


#### ステップ 2.2:Braze IP へのアクセスの許可    

ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスに Braze ネットワークへのアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。 

また、BrazeがRedshiftのデータにアクセスできるように、セキュリティグループを変更する必要があるかもしれない。以下の IP と Redshift クラスターのクエリに使用するポート (デフォルトは 5439) のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートで Redshift TCP 接続を明示的に許可する必要があります。さらに、Braze がクラスターに接続するために、Redshift クラスターのエンドポイントがパブリックにアクセス可能であることが重要です。

Redshiftクラスターを一般公開したくない場合は、VPCとEC2インスタンスをセットアップし、sshトンネルを使用してRedshiftデータにアクセスすることができる。詳しくは、[AWSを参照のこと：ローカルマシンからプライベートなAamazon Redshiftクラスタにアクセスするには？](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% subtabs %}
{% subtab United States (US) %}
インスタンス`US-01` 、`US-02` 、`US-03` 、`US-04` 、`US-05` 、`US-06` 、`US-07` 、これらは関連するIPアドレスである：
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
インスタンス`EU-01` と`EU-02` 、これらは関連するIPアドレスである：
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

- **BigQuery 接続ユーザー:**これでブレイズはコネクションを作ることができる。
- **BigQuery ユーザー:**クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:**データセットとその内容を表示するためのアクセスを Braze に提供します。
- **BigQuery ジョブユーザー:**これにより、ジョブを実行するためのBrazeへのアクセスが可能になる。
- **bigquery.tables.create** これによりBrazeは、セグメント更新時に一時テーブルを作成するためのアクセスを提供する。

接続するソースが使用するサービスアカウントを作成する。このユーザは、CDI セグメントで使用可能なテーブルのリストを作成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。 

データセット内のすべてのテーブルにアクセス権を与えるか、特定のテーブルだけに権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントでクエリーできる。 

Brazeでセグメントを更新する前に、BrazeがCDIセグメントのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。 

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳しくは、[Google Cloudを参照のこと：サービス・アカウント・キーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete).これを後でBrazeのダッシュボードにアップロードする。

#### ステップ 2.2:Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Braze に Big Query インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% subtabs %}
{% subtab United States (US) %}
インスタンス`US-01` 、`US-02` 、`US-03` 、`US-04` 、`US-05` 、`US-06` 、`US-07` 、これらは関連するIPアドレスである：
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
インスタンス`EU-01` と`EU-02` 、これらは関連するIPアドレスである：
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
#### ステップ 2.1:アクセストークンの作成  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名をクリックし、ドロップダウンから \[**ユーザー設定**] を選択します。
2. サービス・アカウントが、接続されたソースに使用されているスキーマで`CREATE TABLE` 権限を持っていることを確認する。 
3. \[アクセストークン] タブで、\[**新しいトークンの生成**] をクリックします。
4. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、\[有効期間 (日)] ボックスを空 (空白) のままにして、トークンの有効期間を有効期間なしに変更します。
5. \[**生成**] をクリックします。
6. 表示されたトークンをコピーして、\[**完了**] をクリックします。

このトークンは、CDI セグメントで使用可能なテーブルの一覧を生成したり、 新しいセグメントを作成するためにソーステーブルをクエリしたりする際に使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。 

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントでクエリーできる。

 Brazeでセグメントを更新する前に、BrazeがCDIセグメントのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。 

認証情報の作成ステップで Braze ダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

#### ステップ 2.2:Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Brazeに Databricks インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% subtabs %}
{% subtab United States (US) %}
インスタンス`US-01` 、`US-02` 、`US-03` 、`US-04` 、`US-05` 、`US-06` 、`US-07` 、これらは関連するIPアドレスである：
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
インスタンス`EU-01` と`EU-02` 、これらは関連するIPアドレスである：
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

{% tabs local %}
{% tab Snowflake %}
#### ステップ 3.1:Snowflake の接続情報とソーステーブルの追加

次に、Brazeダッシュボードで接続ソースを作成する。**Data Settings**>**Cloud Data Ingestionに**進む。**Connected Sources」**タブに移動し、「**Create data connection**」をクリックする。

Snowflakeデータウェアハウスとソーススキーマの情報を入力し、次のステップに進む。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_1.png %})

#### ステップ 3.2:同期の詳細の設定

次に、接続するソースの名前を選ぶ。この名前は、新しいCDIセグメントを作成する際に、利用可能なソースのリストで使用される。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。最大実行時間は60分である。実行時間を短くすれば、Snowflakeアカウントに発生するコストを削減できる。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### ステップ3.3：公開鍵に注意  

**Test connection**ページで、RSA公開鍵が表示される。これをメモしておこう。Snowflakeで統合を完了させる必要がある。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_3.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:データウェアハウスの構成を確定する

{% tabs %}
{% tab Snowflake %}
最後のステップで記した公開鍵をSnowflakeのユーザーに追加する。これでBrazeはSnowflakeに接続できるようになる。この方法の詳細については、[Snowflakeのドキュメントを](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)参照のこと。 

鍵をローテーションしたい場合は、Brazeが新しい鍵ペアを生成し、新しい公開鍵を提供する。

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflakeでユーザーにキーを追加したら、Brazeで**Test Connectionを**選択し、**Doneを**選択する。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。
{% endtab %}

{% tab Redshift %}
#### ステップ4.1：Redshift の接続情報とソーステーブルの追加

**Data Settings**>**Cloud Data Ingestionに**進む。**Connected Sources」**タブに移動し、「**Create data connection**」をクリックする。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**Data**」の下にある**「Cloud Data Ingestion**」に進む。
{% endalert %}

Redshiftアカウントとソース・スキーマの情報を入力し、次のステップに進む。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_rs_1.png %})

#### ステップ4.2：同期の詳細の設定

次に、接続するソースの名前を選ぶ。この名前は、新しいCDIセグメントを作成する際に、利用可能なソースのリストで使用される。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。最大実行時間は60分である。実行時間を短くすれば、Snowflakeアカウントに発生するコストを削減できる。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化することを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### ステップ4.3：テスト接続

Brazeの**Test Connectionを**選択し、ユーザーに見えるテーブルのリストが期待通りであることを確認し、**Doneを**選択する。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_3.png %})
{% endtab %}

{% tab BigQuery %}
#### ステップ4.1：BigQueryの接続情報とソースデータセットを追加する

JSONキーをアップロードし、サービスアカウント名を指定し、ソースデータセットの詳細を入力する。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bq_1.png %})

#### ステップ4.2：同期の詳細の設定

次に、接続するソースの名前を選ぶ。この名前は、新しいCDIセグメントを作成する際に、利用可能なソースのリストで使用される。

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。最大実行時間は60分である。実行時間を短くすれば、Snowflakeアカウントに発生するコストを削減できる。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化することを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### ステップ4.3：テスト接続

Brazeの**Test Connectionを**選択し、ユーザーに見えるテーブルのリストが期待通りであることを確認し、**Doneを**選択する。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_3.png %})
{% endtab %}

{% tab Databricks %}
#### ステップ4.1：Databricksの接続情報とソースデータセットを追加する

Databricksデータウェアハウスとソースデータの情報を入力し、次のステップに進む。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_1.png %})

#### ステップ4.2：同期の詳細の設定

次に、接続するソースの名前を選ぶ。この名前は、新しいCDIセグメントを作成する際に、利用可能なソースのリストで使用される。

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。最大実行時間は60分である。実行時間を短くすれば、Snowflakeアカウントに発生するコストを削減できる。

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化することを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_2.png %})

#### ステップ4.3：テスト接続

Brazeの**Test Connectionを**選択し、ユーザーに見えるテーブルのリストが期待通りであることを確認し、**Doneを**選択する。これで接続ソースが作成され、CDIセグメントで使用する準備が整った。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_3.png %})
{% endtab %}
{% endtabs %}

{% alert note %}
ドラフト状態からアクティブ状態に移行する前に、ソースのテストに成功する必要がある。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## 追加の統合またはユーザーを設定する（オプション）

{% tabs %}
{% tab Snowflake %}
Brazeと複数の統合を設定することができるが、各統合は異なるスキーマを接続するように設定する必要がある。追加接続を作成する際、同じSnowflakeアカウントに接続する場合は、既存の認証情報を再利用することができる。

同じユーザーとロールを統合間で再利用する場合、公開鍵を再度追加する必要はない。
{% endtab %}

{% tab Redshift %}
Brazeで複数のソースを設定することができるが、各ソースは異なるスキーマを接続するように設定する必要がある。追加ソースを作成する際、同じ Redshift アカウントに接続する場合は、既存の認証情報を再利用できる。
{% endtab %}

{% tab BigQuery %}
Brazeで複数のソースを設定することもできるが、各ソースは異なるデータセットを接続するように設定する必要がある。追加のソースを作成する際、同じ BigQuery アカウントに接続する場合は、既存の認証情報を再利用できる。
{% endtab %}

{% tab Databricks %}
Brazeで複数のソースを設定することができるが、各ソースは異なるスキーマを接続するように設定する必要がある。追加ソースを作成する際、同じ Databricks アカウントに接続する場合は既存の認証情報を再利用できる。
{% endtab %}
{% endtabs %}

## 接続されたソースを使用する

ソースが作成されると、それを使用して1つまたは複数のCDIセグメントを作成することができる。このソースでセグメントを作成する詳細については、[CDI Segmentsのドキュメントを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)参照のこと。

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより多くの計算リソース（e.g... より大きな倉庫）を割り当てることを検討する。
{% endalert %}

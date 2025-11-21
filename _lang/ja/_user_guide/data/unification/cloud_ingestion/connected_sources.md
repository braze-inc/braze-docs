---
nav_title: 接続されたソース
article_title: 接続されたソース
description: "このページでは、Braze のクラウドデータ取り込みを使用して、関連するデータを Snowflake、Redshift、BigQuery、および Databricks の連携と同期する方法について説明します。"
page_order: 2
page_type: reference

---

# 接続されたソース

> 接続されたソースは、Braze の CDI (クラウドデータ取り込み) 機能を使ってデータを直接同期するのではなく、ゼロコピーの代替手段です。接続ソースでは、データウェアハウスに直接クエリを行い、基盤となるデータを Braze に一切コピーせずに新しいセグメントを作成します。 

接続ソースを Braze ワークスペースに追加すると、セグメントエクステンション内に CDI セグメントを作成できます。CDIセグメントエクステンションは、データウェアハウスに直接クエリするSQLを記述し（CDIコネクテッドソースを通じて利用可能になったデータを使用）、Braze内でターゲットとなるユーザーグループを作成、管理することができる。 

このソースでセグメントを作成する詳細については、[CDIセグメントエクステンションを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)参照のこと。

{% alert warning %}
接続されたソースはデータウェアハウス上で直接実行されるため、データウェアハウスでこれらのクエリの実行に関連するすべてのコストが発生します。接続されたソースはデータポイントを記録せず、CDIセグメントエクステンションはSQLセグメントクレジットを消費しない。
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
8. Braze ダッシュボードの公開鍵を[認証用の Snowflake ユーザー](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)に追加する。完了したら、接続されたソースを使用して1つ以上のCDIセグメントエクステンションを作成できる。
{% endtab %}

{% tab Redshift %}
1. Redshift環境にソースデータと必要なリソースをセットアップする。
2. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成する。
{% endtab %}

{% tab BigQuery %}
1. BigQuery環境でソースデータと必要なリソースをセットアップする。
2. サービスアカウントを作成し、同期するデータを含む BigQuery のプロジェクトとデータセットへのアクセスを許可します。  
3. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成する。
{% endtab %}

{% tab Databricks %}
1. Databricks 環境でソースデータと必要なリソースをセットアップする。
2. サービスアカウントを作成し、同期するデータを含む Databricks のプロジェクトとデータセットへのアクセスを許可します。  
3. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成する。

{% alert important %}
BrazeがClassicおよびPro SQLインスタンスに接続する際、ウォームアップ時間が2～5分かかる場合があり、接続のセットアップやテスト時、CDIセグメントエクステンションの作成やリフレッシュ時に遅延が発生する。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. サービスプリンシパルを作成し、統合に使用する Fabric ワークスペースへのアクセスを許可します。   
2. Fabricワークスペースで、ソースデータを設定し、サービスプリンシパルに権限を付与する。 
3. Braze ダッシュボードで接続されたソースを新規作成する。
4. 統合をテストする。
5. 接続されたソースを使用して、1つ以上のCDIセグメントエクステンションを作成する。
{% endtab %}

{% endtabs %}

### ステップ 2:データウェアハウスをセットアップする

データウェアハウス環境でソースデータと必要なリソースを設定します。接続ソースは1つまたは複数のテーブルを参照する可能性があるため、Brazeユーザーが接続ソース内の必要なすべてのテーブルにアクセスできる権限を持っていることを確認する。

{% tabs %}
{% tab Snowflake %}
#### ステップ 2.1: ロールを作成し、権限を付与する

接続ソースが使用するロールを作成する。このロールは、CDI セグメントエクステンションで使用可能なテーブルのリストを生成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントエクステンションでクエリーできる。

Brazeでセグメントを更新する前に、BrazeがCDIセグメントエクステンションのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。

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

{% multi_lang_include data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### ステップ 2.1: ユーザーの作成と権限の付与 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

接続ソースが使用するユーザーを作成する。このユーザーは、CDI セグメントエクステンションで使用可能なテーブルのリストを作成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。CDI 連携を複数作成する場合は、スキーマに権限を付与したり、グループを使用して権限を管理したりできます。 

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントエクステンションでクエリーできる。新しいテーブルを作成する際には、必ずそのユーザーにアクセス権を与えるか、そのユーザーにデフォルトのアクセス権を設定する。 

Brazeでセグメントを更新する前に、BrazeがCDIセグメントエクステンションのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとにテンポラリテーブルを作成し、Brazeがセグメンテーションを更新している間だけ持続する。


#### ステップ 2.2:Braze IP へのアクセスの許可    

ファイアウォールや他のネットワークポリシーがある場合は、Redshift インスタンスに Braze ネットワークへのアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。 

また、Redshift のデータへのアクセスを Braze に許可するように、セキュリティグループを変更しなければならないこともあります。以下の IP と Redshift クラスターのクエリに使用するポート (デフォルトは 5439) のインバウンドトラフィックを明示的に許可してください。インバウンドルールが「すべて許可」に設定されている場合でも、このポートで Redshift TCP 接続を明示的に許可する必要があります。さらに、Braze がクラスターに接続するために、Redshift クラスターのエンドポイントがパブリックにアクセス可能であることが重要です。

Redshift クラスターにパブリックアクセスを許可しない場合は、ssh トンネルを使用して Redshift データにアクセスするように VPC と EC2 インスタンスを設定できます。詳しくは、[AWSを参照のこと：ローカルマシンからAmazon Redshiftのプライベートクラスタにアクセスするには？](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### ステップ 2.1: サービスアカウントの作成と権限の付与 

GCP で、Braze がテーブルに接続してデータを読み取るために使用するサービスアカウントを作成します。サービスアカウントには次の権限が必要です。 

- **BigQuery 接続ユーザー:**Braze に接続を許可します。
- **BigQuery ユーザー:**クエリの実行、データセットメタデータの読み取り、およびテーブルの一覧表示を行うためのアクセスを Braze に提供します。
- **BigQuery データビューアー:**データセットとその内容を閲覧するためのBrazeアクセスを提供する。
- **BigQuery ジョブユーザー:**ジョブを実行するためのBrazeアクセスを提供する。
- **bigquery.tables.create** セグメント更新時に一時テーブルを作成するためのアクセスを Braze に提供します。

接続するソースが使用するサービスアカウントを作成する。このユーザーは、CDI セグメントエクステンションで使用可能なテーブルのリストを作成したり、新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。 

データセット内のすべてのテーブルにアクセス権を与えるか、特定のテーブルだけに権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントエクステンションでクエリーできる。 

Brazeでセグメントを更新する前に、BrazeがCDIセグメントエクステンションのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとに一時テーブルを作成し、そのテーブルはBrazeがセグメントを更新している間だけ持続する。 

サービスアカウントを作成して権限を付与したら、JSON キーを生成します。詳しくは、[Google Cloudを参照：サービスアカウントキーの作成と削除](https://cloud.google.com/iam/docs/keys-create-delete)を参照してください。これを後でBrazeのダッシュボードにアップロードする。

#### ステップ 2.2:Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Braze に Big Query インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### ステップ 2.1: アクセストークンを作成する  

Braze が Databricks にアクセスするには、パーソナルアクセストークンを作成する必要があります。

1. Databricks ワークスペースで、上部バーにある Databricks ユーザー名をクリックし、ドロップダウンから [**ユーザー設定**] を選択します。
2. サービスアカウントに、接続されたソースに使用されているスキーマに対する `CREATE TABLE` 権限があることを確認します。 
3. [**アクセストークン**] タブで、[**新しいトークンの生成**] を選択します。
4. 「Braze CDI」など、このトークンの識別に役立つコメントを入力し、[有効期間 (日)] ボックスを空 (空白) のままにして、トークンの有効期間を有効期間なしに変更します。
5. [**生成**] を選択します。
6. 表示されたトークンをコピーして、[**完了**] を選択します。

このトークンは、CDI セグメントエクステンションで使用可能なテーブルの一覧を生成したり、 新しいセグメントを作成するためにソーステーブルをクエリしたりするために使用される。接続ソースが作成されると、Brazeはソーススキーマ内のユーザーが利用可能なすべてのテーブルの名前と説明を検出する。 

スキーマ内のすべてのテーブルにアクセス権を与えるか、特定のテーブルにのみ権限を与えるかを選択できる。Brazeロールがアクセスできるテーブルは、CDIセグメントエクステンションでクエリーできる。

Brazeでセグメントを更新する前に、BrazeがCDIセグメントエクステンションのクエリ結果でテーブルを作成できるように、`create table` 権限が必要である。Brazeはセグメントごとにテンポラリテーブルを作成し、Brazeがセグメンテーションを更新している間だけ持続する。 

認証情報の作成ステップで Braze ダッシュボードへの入力が必要になるまで、トークンを安全な場所に保管してください。

#### ステップ 2.2:Braze IP へのアクセスの許可    

ネットワークポリシーを設定している場合は、Brazeに Databricks インスタンスへのネットワークアクセスを許可する必要があります。Braze ダッシュボードの地域に対応する以下の IP からのアクセスを許可します。  

{% multi_lang_include data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### ステップ 2.1: Fabric リソースへのアクセスを許可する 
Braze は、Entra ID 認証でサービスプリンシパルを使用して Fabric ウェアハウスに接続します。Braze が使用する新しいサービスプリンシパルを作成し、必要に応じてFabricリソースへのアクセスを許可する。Braze の接続には以下の詳細が必要となります。    

* Azure アカウントのテナント ID (ディレクトリとも呼ばれる) 
* サービスプリンシパルのプリンシパル ID (アプリケーション ID とも呼ばれる) 
* Braze が認証するためのクライアントシークレット

1. Azure portal で、[Microsoft Entra 管理センター]、[**アプリの登録**] の順に移動します。
2. **[ID] > [アプリケーション] > [アプリの登録]** で [**+新規登録**] を選択します。 
3. 名前を入力し、サポートされているアカウントの種類として`Accounts in this organizational directory only` を選択します。次に、[**登録**] を選択します。 
4. 先ほど作成したアプリケーション（サービスプリンシパル）を選択し、**証明書& secret > + New client secretに**移動する。
5. シークレットの説明を入力し、有効期限を設定します。そして、[**追加**] を選択します。 
6. Brazeのセットアップで使用するために作成したクライアントシークレットに注意すること。 

{% alert note %}
Azure では、サービスプリンシパルシークレットの有効期限を無制限に設定することはできません。Braze へのデータフローを維持するために、認証情報が失効する前に忘れずに更新してください。
{% endalert %}

#### ステップ 2.2:Fabric リソースへのアクセスを許可する 
BrazeがFabricインスタンスに接続するためのアクセスを提供する。Fabricの管理ポータルで、**「設定」**>「**ガバナンスとインサイト**」>「**管理ポータル**」>「**テナント設定**」の順に移動する。    

* **開発者設定**で、[サービスプリンシパルが Fabric API を使用可能] を有効にして、Braze が Microsoft Entra ID を使用して接続できるようにします。
* **OneLake の設定**で、サービスプリンシパルが外部アプリからデータにアクセスできるように、[ユーザーが Fabric の外部アプリを使用して OneLake に保存されているデータにアクセス可能] を有効にします。

#### ステップ 2.3:ウェアハウスの接続文字列を取得する 

Brazeを接続するには、倉庫のSQLエンドポイントが必要である。SQL エンドポイントを取得するには、Fabric で**ワークスペース**に移動し、項目の一覧でウェアハウスの名前にカーソルを合わせ、 [**SQL 接続文字列をコピー**] を選択します。

![ユーザーがSQL接続文字列を取得する必要がある。]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})

#### ステップ 2.4:ファイアウォールで Braze IP を許可する（オプション）

Microsoft Fabric アカウントの設定によっては、Braze からのトラフィックを許可するように、ファイアウォールで以下の IP アドレスを許可する必要があります。これを有効にする方法の詳細については、[Entra Conditional Access ](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)の関連ドキュメントを参照してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

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

接続するソースの名前を選択する。この名前は、新しいCDIセグメントエクステンションを作成するときに、利用可能なソースのリストで使用される。 

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

接続するソースの名前を選択する。この名前は、新しいCDIセグメントエクステンションを作成するときに、利用可能なソースのリストで使用される。 

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

接続するソースの名前を選択する。この名前は、新しいCDIセグメントエクステンションを作成するときに、利用可能なソースのリストで使用される。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は60分です。実行時間を短くすると、BigQuery アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_bg_2.png %})

#### ステップ3.3：接続をテストする

[**テスト接続**] を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントエクステンションで使用できるようになった。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Databricks %}
#### ステップ 3.1:Databricks の接続情報とソーステーブルの追加

Brazeダッシュボードで接続ソースを作成する。[**データ設定**] > [**クラウドデータ取り込み**] > ［**接続されたソース**] の順に移動し、［**新しいデータ同期を作成**] > ［**Databricks のインポート**] を選択します。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Databricks 認証情報、オプションのカタログとソーススキーマの情報を入力してから、次のステップに進みます。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_databricks_1.png %})

#### ステップ 3.2:同期の詳細の設定

接続するソースの名前を選択する。この名前は、新しいCDIセグメントエクステンションを作成するときに、利用可能なソースのリストで使用される。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は60分です。実行時間を短くすると、Databricks アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、Brazeユーザーにより大きな倉庫を割り当てることを検討すること。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_db_2.png %})

#### ステップ3.3：接続をテストする

[**テスト接続**] を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントエクステンションで使用できるようになった。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% tab Microsoft Fabric %}
#### ステップ 3.1:Microsoft Fabricの接続情報とソーステーブルを追加する

Brazeダッシュボードで接続ソースを作成する。[**データ設定**] > [**クラウドデータ取り込み**] > ［**接続されたソース**] の順に移動し、［**新しいデータ同期を作成**] > ［**Microsoft Fabric のインポート**] を選択します。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_tab.png %}){: style="max-width:80%;"}

Microsoft Fabric の認証情報およびソースウェアハウス、スキーマの情報を入力し、次のステップに進みます。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_1.png %})

#### ステップ 3.2:同期の詳細の設定

接続するソースの名前を選択する。この名前は、新しいCDIセグメントエクステンションを作成するときに、利用可能なソースのリストで使用される。 

このソースの最大ランタイムを設定する。Brazeは、セグメントを作成または更新する際に、最大実行時間を超えるクエリは自動的に中止する。許容される最大実行時間は60分です。実行時間を短くすると、Microsoft Fabric アカウントに課金されるコストが削減されます。 

{% alert note %}
クエリーが常にタイムアウトしており、最大実行時間を60分に設定している場合は、クエリーの実行時間を最適化するか、ファブリック容量を拡張することを検討してください。
{% endalert %}

![]({% image_buster /assets/img/cloud_ingestion/connected_source_mf_2.png %})

#### ステップ3.3：接続をテストする

[**テスト接続**] を選択し、ユーザーに表示されるテーブルのリストが期待どおりであることを確認してから、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントエクステンションで使用できるようになった。

![]({% image_buster /assets/img/cloud_ingestion/connected_source_test_connection.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:データウェアハウスの構成を確定する

{% tabs %}
{% tab Snowflake %}
最後の手順で書き留めた公開鍵を Snowflake のユーザーに追加します。これで Braze は、Snowflake に接続できるようになります。この方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。 

任意の時点で鍵のローテーションを行う場合は、新しい公開鍵を作成できます。このためには、［**クラウドデータ取り込み**] の ［**データアクセス管理**] に移動し、該当するアカウントの ［**新しいキーを生成**] を選択します。

![Snowflakeデータアクセス認証情報のデータアクセス管理、新しいキーを生成するボタンがある。]({% image_buster /assets/img/cloud_ingestion/connected_source_sf_4.png %})

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflake でユーザーに鍵を追加したら、Braze で [**テスト接続**] を選択し、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントエクステンションで使用できるようになった。
{% endtab %}

{% tab Redshift %}
SSHトンネルで接続する場合は、最後のステップで記した公開キーをSSHトンネル・ユーザーに追加する。 

ユーザーに鍵を追加したら、Braze で [**テスト接続**] を選択し、[**完了**] を選択します。これで接続ソースが作成され、CDIセグメントエクステンションで使用できるようになった。

{% endtab %}
{% tab BigQuery %}
これはBigQueryには当てはまらない。

{% endtab %}
{% tab Databricks %}
これは Databricks には適用されません。

{% endtab %}
{% tab Microsoft Fabric %}
これは Microsoft Fabric には当てはまりません。

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

{% tab Microsoft Fabric %}
Braze で複数のソースを設定できますが、各ソースは異なるスキーマを接続するように設定する必要があります。追加のソースを作成する際、同じ Azure アカウントに接続する場合は既存の認証情報を再利用できます。
{% endtab %}
{% endtabs %}

## 接続されたソースの使用

ソースが作成されたら、それを使って1つ以上のCDIセグメントエクステンションを作成できる。このソースでセグメントを作成する方法の詳細については、[CDI セグメントエクステンションのドキュメントを]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/)参照のこと。

{% alert note %}
クエリが一貫してタイムアウトしており、最大実行時間を60分に設定している場合は、クエリの実行時間を最適化するか、より多くの計算リソース (より大きなウェアハウスなど) を Braze ユーザーに割り当てることを検討してください。
{% endalert %}

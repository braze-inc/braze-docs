---
nav_title: 国勢調査
article_title: 国勢調査
description: "この参考記事では、Brazeとデータ統合プラットフォームであるCensusのパートナーシップについて概説している。Censusは、クラウドウェアハウスのデータを使って、ターゲットを絞ったユーザーセグメントを動的に作成することを可能にする。"
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# 国勢調査

> [Census][1] は、Snowflake や BigQuery のようなクラウドデータウェアハウスを Braze に接続するデータアクティベーションプラットフォームです。マーケティングチームは、ファーストパーティデータの力を解き放ち、ダイナミックなオーディエンスセグメントを構築し、顧客属性を同期してキャンペーンをパーソナライズし、Braze内のすべてのデータを最新の状態に保つことができる。信頼できる実用的なデータで、これまで以上に簡単に行動を起こすことができます。CSV のアップロードやエンジニアの助力は必要ありません。

Braze と Census の統合により、オーディエンスや製品データを Braze にダイナミックにインポートし、パーソナライズされたキャンペーンを送信できます。例えば、Brazeで「CLV > 1000のニュースレター購読者」のコホートを作成し、価値の高い顧客をターゲットにしたり、「過去30日間にアクティブだったユーザー」のコホートを作成し、次期ベータ機能をテストする特定のユーザーをターゲットにすることができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| Census アカウント | このパートナーシップを活用するには、[Census アカウント][1]が必要です。 |
| Braze REST API キー | すべてのユーザーデータ権限 (`users.delete` を除く) と `segments.list` 権限を持つ Braze REST API キー。Census でサポートされる Braze オブジェクトの増加に伴い、権限セットが変わる可能性があります。このため、この時点でより多くの権限を付与するか、これらの権限を今後更新する計画を立てることができます。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントは、[BrazeインスタンスのURL][2]によって異なります。 |
| データウェアハウスとデータモデル | 統合を開始する前に、Censusでデータウェアハウスをセットアップし、Brazeと同期させたいデータのサブセットのモデルを定義しておく必要がある。利用可能なデータソースのリストとモデル作成に関するガイダンスについては、[Census のドキュメント](https://docs.getcensus.com/destinations/braze)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 統合

### ステップ1:Brazeサービス接続を作成する

Census プラットフォームで Census を統合するには、[**Connections**] タブに移動し、[**New Destination**] を選択して新しい Braze サービス接続を作成します。

表示されるプロンプトで、この接続に名前を付け、Braze エンドポイント URL と Braze REST API キー (オプションで、コホートを同期するためのデータインポートキー) を入力します。

![][8]{: style="max-width:60%;"}

### ステップ2:国勢調査の同期を作成する

顧客を Braze に同期するには、同期を作成する必要があります。ここで、データを同期する場所と、2つのプラットフォーム間でどのようにフィールドをマッピングするかを定義する。

1. [**Syncs**] タブに移動し、[**New Sync**] を選択します。<br><br> 
2. コンポーザーで、データウェアハウスからソースデータモデルを選択します。<br><br>
3. モデルの同期先を設定する。宛先として [**Braze**] を選択し、同期する[サポートされているオブジェクトタイプ](#supported-objects)を選択します。<br>![[Select a Destination] プロンプトで接続として「Braze」が選択されており、さまざまなオプションが一覧表示されている。][10]{: style="max-width:80%;"}<br><br>
4. 適用する同期ルールを選択します ([**Update or Create**] が最も一般的な選択肢ですが、データの削除を処理するためのより詳細なルールを選択することもできます)。<br><br>
5. 次に、レコードマッチングのために、Brazeオブジェクトをモデルフィールドに[マッピング](#supported-objects)するシンクキーを選択する。<br>![「Select a Sync Key」プロンプトで Braze の「External User ID」がソースの「user_id」に一致している。][9]{: style="max-width:80%;"}<br><br>
6. 最後に、Census データフィールドを対応する Braze フィールドにマッピングします。<br>![Census でのマッピング][11]{: style="max-width:80%;"}<br><br>
7. 詳細を確認し、シンクを作成する。 

同期が実行されると、Brazeにユーザーデータが表示される。今後のBrazeキャンペーンやCanvasにBrazeセグメントを作成・追加して、これらのユーザーをターゲットにできるようになった。 

{% alert note %}
Census と Braze の統合を使用する場合、Census は Braze との同期のたびに差分 (変更データ) のみを送信します。
{% endalert %}

## サポートされるオブジェクト

Censusは現在、以下のBrazeオブジェクトの同期をサポートしている：

| オブジェクト名 | 同期の動作 |
| --- | --- |
| ユーザー | 更新、作成、ミラー、削除 |
| コホート | 更新、作成、ミラー | 
| カタログ | 更新、作成、ミラー |
| サブスクリプション・グループ・メンバーシップ | 鏡 |
| イベント | 追加する |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

さらに、CensusはBrazeへの[構造化データの](https://docs.getcensus.com/destinations/braze#supported-objects)送信もサポートしている： 
- ユーザープッシュトークン:プッシュトークンを送信するには、データを2-3の値を持つオブジェクトの配列として構造化する必要がある：`app_id` `token` 、そしてオプションで`device_id` 。
- 階層化カスタム属性:オブジェクトと配列の両方がサポートされている。2022年4月現在、この機能はまだ早期アクセス段階です。アクセスするには、Brazeのアカウントマネージャーに連絡する必要があるかもしれない。

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}
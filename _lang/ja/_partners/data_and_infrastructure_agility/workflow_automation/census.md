---
nav_title: 国勢調査
article_title: 国勢調査
description: "この参考記事では、Brazeとデータ統合プラットフォームであるCensusのパートナーシップについて概説している。Censusは、クラウドウェアハウスのデータを使って、ターゲットを絞ったユーザーセグメントを動的に作成することを可能にする。"
alias: /partners/census/
page_type: partner
search_tag: Partner

---

# 国勢調査

> [Censusは][1]、SnowflakeやBigQueryのようなクラウドデータウェアハウスをBrazeに接続するデータ活性化プラットフォームである。マーケティングチームは、ファーストパーティデータの力を解き放ち、ダイナミックなオーディエンスセグメントを構築し、顧客属性を同期してキャンペーンをパーソナライズし、Braze内のすべてのデータを最新の状態に保つことができる。CSVのアップロードやエンジニアの好意は必要ない。

BrazeとCensusの統合により、オーディエンスや製品データをBrazeに動的にインポートし、パーソナライズされたキャンペーンを送ることができる。例えば、Brazeで「CLV > 1000のニュースレター購読者」のコホートを作成し、価値の高い顧客をターゲットにしたり、「過去30日間にアクティブだったユーザー」のコホートを作成し、次期ベータ機能をテストする特定のユーザーをターゲットにすることができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| 国勢調査アカウント | このパートナーシップを利用するには、[国勢調査のアカウントが][1]必要である。 |
| Braze REST API キー | すべてのユーザーデータ権限（`users.delete` を除く）と`segments.list` 権限を持つ Braze REST API キー。Censusがより多くのBrazeオブジェクトのサポートを追加するにつれて、パーミッションのセットは変更される可能性がある。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに][2]依存する。 |
| データウェアハウスとデータモデル | 統合を開始する前に、Censusでデータウェアハウスをセットアップし、Brazeと同期させたいデータのサブセットのモデルを定義しておく必要がある。利用可能なデータソースのリストとモデル作成に関するガイダンスについては、[国勢調査のドキュメントを](https://docs.getcensus.com/destinations/braze)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 統合

### ステップ1:Brazeサービス接続を作成する

CensusプラットフォームでCensusを統合するには、**Connections**タブに移動し、**New Destinationを**選択して新しいBrazeサービス接続を作成する。

表示されるプロンプトで、この接続に名前を付け、BrazeエンドポイントURLとBraze REST APIキー（オプションで、コホートを同期するためのデータインポートキー）を入力する。

![][8]{: style="max-width:60%;"}

### ステップ2:国勢調査の同期を作成する

顧客をBrazeに同期させるには、同期を構築する必要がある。ここで、データを同期する場所と、2つのプラットフォーム間でどのようにフィールドをマッピングするかを定義する。

1. **Syncs**タブに移動し、**New Syncを**選択する。<br><br> 
2. コンポーザーで、データウェアハウスからソース・データモデルを選択する。<br><br>
3. モデルの同期先を設定する。同期先として**Brazeを**選択し、[サポートするオブジェクトタイプを](#supported-objects)選択する。<br>![Select a Destination "プロンプトでは、接続先として "Braze "が選択され、様々なオブジェクトがリストアップされる。][10]{: style="max-width:80%;"}<br><br>
4. 適用したい同期ルールを選択する**（UpdateまたはCreateが**最も一般的な選択だが、データの削除など、より高度なルールを選択することもできる）。<br><br>
5. 次に、レコードマッチングのために、Brazeオブジェクトをモデルフィールドに[マッピング](#supported-objects)するシンクキーを選択する。<br>![Select a Sync Key "プロンプトで、Brazeの "External User ID "がソースの "user_id "に一致する。][9]{: style="max-width:80%;"}<br><br>
6. 最後に、国勢調査のデータフィールドを同等のBrazeフィールドにマッピングする。<br>![国勢調査マッピング][11]{: style="max-width:80%;"}<br><br>
7. 詳細を確認し、シンクを作成する。 

同期が実行されると、Brazeにユーザーデータが表示される。今後のBrazeキャンペーンやCanvasにBrazeセグメントを作成・追加して、これらのユーザーをターゲットにできるようになった。 

{% alert note %}
CensusとBrazeの統合を使用する場合、Censusは、各同期のデルタ（変更データ）のみをBrazeに送信する。
{% endalert %}

## サポート対象

Censusは現在、以下のBrazeオブジェクトの同期をサポートしている：

| オブジェクト名 | シンクの動作 |
| --- | --- |
| ユーザー | 更新、作成、ミラー、削除 |
| コホート | 更新、作成、ミラー | 
| カタログ | 更新、作成、ミラー |
| サブスクリプション・グループ・メンバーシップ | 鏡 |
| イベント | 追加する |
{: .reset-td-br-1 .reset-td-br-2}

さらに、CensusはBrazeへの[構造化データの](https://docs.getcensus.com/destinations/braze#supported-objects)送信もサポートしている： 
- ユーザーがトークンをプッシュする：プッシュトークンを送信するには、データを2-3の値を持つオブジェクトの配列として構造化する必要がある：`app_id` `token` 、そしてオプションで`device_id` 。
- カスタム属性を入れ子にする：オブジェクトと配列の両方がサポートされている。2022年4月現在、この機能はまだ早期アクセスである。アクセスするには、Brazeのアカウントマネージャーに連絡する必要があるかもしれない。

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}
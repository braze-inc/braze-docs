---
nav_title: Census
article_title:Census
description:"この参考記事では、Brazeと、クラウドウェアハウスのデータを使ってダイナミックなターゲットユーザーセグメントの作成を可能にするデータ統合プラットフォームCensusのパートナーシップについて概説している。"
alias: /partners/census/
page_type: partner
search_tag:Partner

---

# Census

> [Censusは][1]、SnowflakeやBigQueryのようなクラウドデータウェアハウスをBrazeに接続するデータ活性化プラットフォームである。マーケティングチームは、ダイナミックなオーディエンスセグメントを構築し、キャンペーンをパーソナライズするために顧客属性を同期し、Braze内のすべてのデータを最新の状態に保つために、ファーストパーティデータの力を引き出すことができる。信頼できるアクション可能なデータで、これまで以上に簡単にアクションを起こすことができる。CSVのアップロードや開発者の好意は必要ない。

BrazeとCensusの統合により、オーディエンスや商品データをダイナミックな形でBrazeにインポートし、パーソナライズされたキャンペーンを送ることができる。例えば、Brazeで「CLV > 1000のニュースレター購読者」のコホートを作成し、価値の高い顧客をターゲットにしたり、「過去30日間にアクティブだったユーザー」のコホートを作成し、特定のユーザーをターゲットにして、今後のベータ機能をテストしたりすることができる。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| センサス・アカウント | このパートナーシップを利用するには、[Censusアカウントが][1]必要である。 |
| Braze REST API キー | すべてのユーザーデータ権限（`users.delete` を除く）と`segments.list` 権限を持つ Braze REST API キー。Censusがより多くのBrazeオブジェクトをサポートするようになると、権限設定は変更される可能性がある。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは[インスタンスのBraze URLに][2]依存する。 |
| データウェアハウスとデータモデル | 統合を開始する前に、Censusでデータウェアハウスを設定し、Brazeと同期させたいデータのサブセットのモデルを定義しておく必要がある。利用可能なデータソースのリストとモデル作成に関するガイダンスについては、[Censusのドキュメントを](https://docs.getcensus.com/destinations/braze)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## 統合

### ステップ1:Brazeサービス接続を作成する

CensusプラットフォームでCensusを統合するには、**Connections**タブに移動し、**New Destinationを**選択して新しいBrazeサービス接続を作成する。

表示されるプロンプトで、この接続に名前を付け、BrazeエンドポイントURLとBraze REST APIキー（オプションで、コホートを同期するためのデータインポートキー）を入力する。

![][8]{: style="max-width:60%;"}

### ステップ2:国勢調査の同期を作成する

顧客をBrazeに同期させるには、同期を構築する必要がある。ここで、データを同期する場所と、2つのプラットフォーム間でどのようにフィールドをマッピングするかを定義する。

1. **Syncs**タブに移動し、**New Syncを**選択する。<br><br> 
2. コンポーザーで、データウェアハウスからソース・データ・モデルを選択する。<br><br>
3. モデルの同期先を設定する。送信先として**Brazeを**選択し、同期する[対応オブジェクトタイプを](#supported-objects)選択する。<br>![送信先の選択」プロンプトでは、接続先として「Braze」が選択され、さまざまなオブジェクトがリストアップされる。][10]{: style="max-width:80%;"}<br><br>
4. 適用したい同期ルールを選択する**（更新または作成が**最も一般的な選択だが、データの削除など、より高度なルールを選択することもできる）。<br><br>
5. 次に、レコードマッチングのために、Brazeオブジェクトをモデルフィールドに[マッピング](#supported-objects)するためのシンクキーを選択する。<br>![Select a Sync Key "プロンプトで、Brazeの "External User ID "がソースの "user_id "と一致する。][9]{: style="max-width:80%;"}<br><br>
6. 最後に、Censusのデータフィールドを同等のBrazeフィールドにマッピングする。<br>![国勢調査マッピング][11]{: style="max-width:80%;"}<br><br>
7. 詳細を確認し、シンクを作成する。 

同期が実行されると、Brazeにユーザーデータが表示される。Brazeセグメントを作成し、今後のBrazeキャンペーンやCanvasに追加することで、これらのユーザーをターゲットにすることができる。 

{% alert note %}
CensusとBrazeの統合を使用する場合、Censusは、各同期のデルタ（変更データ）のみをBrazeに送信する。
{% endalert %}

## サポート対象

Currentsは現在、以下のBrazeオブジェクトの同期をサポートしている：

| オブジェクト名 | シンクの動作 |
| --- | --- |
| ユーザー | 更新、作成、ミラー、削除 |
| コホート | 更新、作成、ミラー | 
| カタログ | 更新、作成、ミラー |
| サブスクリプショングループメンバーシップ | 鏡 |
| イベント | 追加する |
{: .reset-td-br-1 .reset-td-br-2}

さらにCensusは、Brazeへの[構造化データの](https://docs.getcensus.com/destinations/braze#supported-objects)送信をサポートしている： 
- ユーザーのプッシュトークン：プッシュトークンを送信するには、データを2～3の値を持つオブジェクトの配列として構造化する必要がある：`app_id` `token` 、そしてオプションの`device_id` 。
- 階層化されたカスタム属性：オブジェクトと配列の両方がサポートされている。2022年4月現在、この機能はまだ早期アクセスである。アクセスするには、Brazeアカウントマネージャーに連絡する必要があるかもしれない。

[1]: https://www.getcensus.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {% image_buster /assets/img/census/add_service.png %}
[9]: {% image_buster /assets/img/census/census_1.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}
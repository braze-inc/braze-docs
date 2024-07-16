---
nav_title: MetaRouter
article_title:メタルーター
description:MetaRouterでBrazeの顧客データ管理を向上させましょう。 この高性能なサーバーサイドタグ管理ソリューションは、MetaRouterがホストするプライベートクラウドや独自のインフラストラクチャ上でのシームレスな展開オプションにより、最大限のコンプライアンスと制御を提供します。
alias: /partners/MetaRouter/
page_type: partner
search_tag:Partner
---

# メタルーター

> [MetaRouter](https://www.metarouter.io/) は、強力なサーバーサイドタグ管理プラットフォームとしてシームレスに統合することで、Brazeの体験を向上させます。それは、信頼性の高い完全なファーストパーティデータ収集から、最大30％の強化されたデータ、リアルタイムのイベントストリームのアクティベーションによるパーソナライズされたジャーニーまで、Braze内で完全な顧客データジャーニーを編成する力を与えます。さらに、MetaRouterはBrazeタグや他のサードパーティタグを必要としないことで実装を簡素化し、Brazeに流入するデータをパラメータごとに詳細に制御できるようにします。

## サポートされている機能

- リトライを組み込むことができます。
- リクエストはバッチ処理されます。
- レート制限の問題は再試行で処理されます。
- 外部IDとPIIがサポートされています。MetaRouterは、クライアントが望む匿名IDおよび任意のPII（メールアドレス、電話番号、名前）を渡します。
- Brazeの購入とカスタムイベントデータを送信できます。
  - イベントプロパティがサポートされています。
  - ネストされたイベントプロパティはサポートされていません。

## 前提条件

始める前に、次のものが必要です:

| 要件           | 説明                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MetaRouterアカウント  | [MetaRouter Enterprise アカウント](https://enterprise.metarouter.io/)。                                                                                |
| Braze REST API キー    | `users.track` の権限を持つBraze REST APIキー。作成するには、**設定** > **APIキー**に移動します。                                                |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、インスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
古いナビゲーションを使用している場合は、**開発者コンソール** > **API設定**でAPIキーを作成できます。
{% endalert %}

## MetaRouterの設定

Braze統合のためにMetaRouterを設定するには:

1. MetaRouterに移動して新しいクラスターを作成します。
2. 追跡したいイベントを選択してください。
3. MetaRouter SDKをインストールし、イベントをウェブサイトに統合します。
4. ウェブサイトのUIにクラスターを接続します。
5. 新しいパイプラインを作成します。
6. あなたのウェブサイトがMetaRouterにイベントを送信していることを確認してください。

## Braze を統合する

### ステップ1:Brazeの統合を追加

エンタープライズMetaRouterで、**統合** > **新しい統合** > **Braze**を選択し、統合に名前を付けます。次に、インスタンスURLとAPIキーを入力し、**変更を適用**を選択します。

![Adding Braze as an integration in MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### ステップ2:イベントマッピングを追加

各アイデンティティ出力に対してイベントマッピングを追加し、Brazeに送信したいイベントを構成します。完了したら、**新しいリビジョンとして保存**を選択します。

![Add event mapping for each of the identity outputs.]({% image_buster /assets/img/metarouter/img2.png %})

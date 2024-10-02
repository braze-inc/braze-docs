---
nav_title: メタ・ルーター
article_title: メタ・ルーター
description: "MetaRouterでBrazeの顧客データ管理を向上させよう。この高性能なサーバーサイド・タグ管理ソリューションは、MetaRouterがホストするプライベートクラウド上でも、独自のインフラ上でも、シームレスな展開オプションで最大限のコンプライアンスとコントロールを提供する。"
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
---

# メタ・ルーター

> [MetaRouterは](https://www.metarouter.io/)、強力なサーバーサイドのタグ管理プラットフォームとしてシームレスに統合することで、Brazeの体験を向上させる。Brazeは、最大30%までエンリッチされた信頼性の高いファーストパーティデータの収集から、パーソナライズされたジャーニーのためのリアルタイムのイベントストリームの活性化まで、Braze内で完全なカスタマーデータジャーニーをオーケストレーションすることを可能にする。さらに、MetaRouterは、Brazeタグやその他のサードパーティタグを不要にすることで実装を合理化し、Brazeに流入するデータをパラメータごとに細かく制御できるようにする。

## サポートされている機能

- リトライを組み込むこともできる。
- リクエストはバッチされる。
- レート制限の問題はリトライで処理される。
- 外部IDとPIIに対応している。MetaRouterは、匿名IDと、クライアントが望むあらゆる個人情報（電子メール、電話番号、名前）を渡す。
- Brazeの購入データやカスタムイベントデータを送信できる。
  - イベント・プロパティがサポートされている。
  - ネストされたイベント・プロパティはサポートされていない。

## 前提条件

始める前に、以下のものが必要だ：

| 必要条件           | 説明                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MetaRouterアカウント  | [MetaRouter Enterpriseアカウント](https://enterprise.metarouter.io/)。                                                                                |
| Braze REST API キー    | `users.track` 権限を持つ Braze REST API キー。作成するには、**「設定」**>「**APIキー**」を選択する。                                                |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**Developer Console**>**API Settingsで**APIキーを作成できる。
{% endalert %}

## MetaRouterをセットアップする

Brazeとの統合用にMetaRouterをセットアップする：

1. MetaRouterに行き、新しいクラスタを作成する。
2. 追跡したいイベントを選択する。
3. MetaRouter SDKをインストールし、イベントをウェブサイトに統合する。
4. クラスターをウェブサイトのUIに接続する。
5. 新しいパイプラインを作る。
6. ウェブサイトがMetaRouterにイベントを送信していることを確認する。

## Braze を統合する

### ステップ1:Brazeとの統合を追加する

Enterprise MetaRouterで、**Integrations**>**New Integration**>**Brazeの**順に選択し、統合名を付ける。次にインスタンスURLとAPIキーを入力し、**Apply Changesを**選択する。

![]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### ステップ2:イベントマッピングを追加する

各ID出力にイベントマッピングを追加し、Brazeに送信したいイベントを設定する。終了したら、**Save as New Revisionを**選択する。

![]({% image_buster /assets/img/metarouter/img2.png %}) 各アイデンティティ出力のイベントマッピングを追加する。

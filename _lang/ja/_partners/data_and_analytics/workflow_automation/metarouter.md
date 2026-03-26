---
nav_title: MetaRouter
article_title: MetaRouter
description: "MetaRouter を使用して、Braze で顧客データ管理を強化します。この高性能なサーバーサイドタグ管理ソリューションは、MetaRouter がホストするプライベートクラウドでもお客様のインフラストラクチャでも、シームレスな導入オプションによって最大限のコンプライアンスと制御を提供します。"
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> [MetaRouter](https://www.metarouter.io/) は、強力なサーバーサイドタグ管理プラットフォームとしてシームレスに統合して、Braze エクスペリエンスを向上させます。これにより、最大30 %強化される信頼性の高いファーストパーティデータ収集から、パーソナライズされたジャーニーのリアルタイムのイベントストリームアクティベーションまで、Braze 内で完全な顧客データジャーニーをオーケストレーションできます。さらに ＭetaRouter は、Braze タグやその他のサードパーティタグの必要性を解消することで実装を合理化し、Braze へのデータ流入をより細かくパラメーター単位で制御できるようにします。

_この統合は Metarouter によって管理されます。_

## サポートされている機能

- リトライを組み込むこともできる。
- リクエストはバッチ処理されます。
- レート制限の問題はリトライで処理される。
- 外部IDとPIIに対応している。MetaRouter は、クライアントが必要とする匿名 ID と PII (メール、電話番号、名前) を渡します。
- Brazeの購入データやカスタムイベントデータを送信できる。
  - イベント・プロパティがサポートされている。
  - ネストされたイベント・プロパティはサポートされていない。

## 前提条件

開始する前に、次のものが必要になります。

| 要件           | 説明                                                                                                                                          |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MetaRouterアカウント  | [MetaRouter Enterpriseアカウント](https://enterprise.metarouter.io/)。                                                                                |
| Braze REST API キー    | `users.track` 権限を持つ Braze REST API キー。作成するには、**「設定」**>「**APIキー**」を選択する。                                                |
| Braze RESTエンドポイント | [RESTエンドポイントのURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## MetaRouterをセットアップする

Brazeとの統合用にMetaRouterをセットアップする：

1. MetaRouterに行き、新しいクラスタを作成する。
2. 追跡したいイベントを選択する。
3. MetaRouter SDK をインストールし、Web サイトにイベントを統合します。
4. クラスターをウェブサイトのUIに接続する。
5. 新しいパイプラインを作る。
6. ウェブサイトがMetaRouterにイベントを送信していることを確認する。

## Braze を統合する

### ステップ1:Brazeとの統合を追加する

Enterprise MetaRouter で [**Integrations**] > [**New Integration**] > [**Braze**] を選択し、統合に名前を付けます。次に、インスタンスの URL と API キーを入力し、[**Apply Changes**] を選択します。

![MetaRouter での統合としてのBrazeの追加]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### ステップ 2:イベントマッピングを追加する

各ID出力にイベントマッピングを追加し、Brazeに送信したいイベントを設定する。終了したら、[**Save as New Revision**] を選択します。

![ID アウトプットごとにイベントm アプリを追加します。]({% image_buster /assets/img/metarouter/img2.png %})


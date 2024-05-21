---
nav_title: メタルーター
article_title: メタルーター
description: "MetaRouter を使用して、Braze での顧客データ管理を強化します。 この高性能なサーバー側タグ管理ソリューションは、MetaRouter がホストするプライベート クラウドでも、独自のインフラストラクチャでも、シームレスな導入オプションにより最大限のコンプライアンスと制御を実現します。"
alias: /partners/MetaRouter/
page_type: partner
search_tag: Partner
---

# メタルーター

> [MetaRouter は](https://www.metarouter.io/) 、強力なサーバー側タグ管理プラットフォームとしてシームレスに統合することで、Braze エクスペリエンスを向上させます。これにより、最大 30% 強化された信頼性の高い完全なファーストパーティ データ収集から、パーソナライズされたジャーニーのためのリアルタイム イベント ストリームのアクティブ化まで、Braze 内で完全な顧客データ ジャーニーを調整できるようになります。さらに、MetaRouter は Braze タグやその他のサードパーティ タグの必要性を排除することで実装を合理化し、Braze に流入するデータをパラメータごとに細かく制御できるようにします。

## サポートされている機能

- 再試行を組み込むことができます。
- リクエストはバッチ処理されます。
- レート制限の問題は再試行によって処理されます。
- 外部 ID と PII がサポートされています。MetaRouter は、クライアントが希望する匿名 ID と PII (電子メール、電話番号、名前) を渡します。
- Braze の購入とカスタム イベントのデータを送信できます。
  - イベント プロパティがサポートされています。
  - ネストされたイベント プロパティはサポートされていません。

## 前提条件

始める前に、次のものが必要です。

| 要件 | 説明 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| MetaRouter アカウント |[MetaRouter Enterprise アカウント](https://enterprise.metarouter.io/)|
| Braze REST APIキー | Braze REST APIキー `users.track` 権限。作成するには、**[設定]**>**[API キー]**に移動します。 |
| Braze REST エンドポイント |[REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスの Braze URL によって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、 **開発者コンソール** >**API 設定**で API キーを作成できます。
{% endalert %}

## MetaRouterの設定

Braze 統合用に MetaRouter を設定するには:

1. MetaRouter に移動して、新しいクラスターを作成します。
2. 追跡したいイベントを選択します。
3. MetaRouter SDK をインストールし、イベントを Web サイトに統合します。
4. クラスターを Web サイトの UI に接続します。
5. 新しいパイプラインを作成します。
6. ウェブサイトが MetaRouter にイベントを送信していることを確認します。

## Braze を統合する

### ステップ 1: Braze統合を追加する

Enterprise MetaRouter で、**「統合」**>**「新しい統合」**>**「Braze」**を選択し、統合に名前を付けます。次に、インスタンス URL と API キーを入力し、**「変更を適用」**を選択します。

![Adding Braze as an integration in MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### ステップ 2: イベントマッピングを追加する

各 ID 出力にイベント マッピングを追加し、Braze に送信するイベントを構成します。完了したら、**「新しいリビジョンとして保存」**を選択します。

![Add event mapping for each of the identity outputs.]({% image_buster /assets/img/metarouter/img2.png %})

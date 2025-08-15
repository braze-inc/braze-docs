---
nav_title: Judo
article_title: Judo
description: "この参考記事では、BrazeとJudoのパートナーシップについて概説している。Judoは、iOSおよびAndroidアプリに位置情報コンテキストとトラッキングを追加できる、コード不要のサーバー駆動型UIプラットフォームである。"
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) はサーバー駆動型 UI プラットフォームであり、パブリッシャーがアプリを更新せずに、リッチで魅力的なアプリ内ユーザーエクスペリエンスを効率的に提供できるようにします。

_この統合は Judo によって管理されます。_

## 統合について

Braze と Judo の統合により、キャンペーンとキャンバスで特別にカスタマイズされたエクスペリエンスが実現します。Braze キャンペーンには、シンプルなテンプレート化されたランディングページエクスペリエンスの代わりに、複数の画面、モーダル、動画、カスタムフォント、サポート設定 (コードを使わず作成され、アプリ更新なしでデプロイされるアクセシビリティ機能やダークモードなど) からなるコンテンツを組み込むことができます。Judo エクスペリエンスでパーソナライズされたコンテンツをサポートするために、Braze のデータを使用することもできます。ユーザーイベントとエクスペリエンスからのデータは、アトリビューションとターゲティングのためにBrazeにフィードバックできる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 柔道アカウント | このパートナーシップを活用するには、[Judo](https://www.judo.app/) アカウントが必要です。 |
| 柔道SDK | Judo SDK は、[iOS](https://github.com/judoapp/judo-ios/) アプリおよび/または[Android](https://github.com/judoapp/judo-android) アプリに統合する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

**オンボーディング**:Judo を使用するアプリパブリッシャーは、リッチでネイティブなオンボーディングエクスペリエンスを構築、デプロイします。これらのエクスペリエンスを、Braze により調整されるパーソナライズされたクロスチャネルオンボーディングの要素として利用できます。さまざまなアプリフローの有効性をテストするために、エクスペリエンスをパーソナライズし、アプリの更新を使用せずに迅速に更新できます。

**コンバージョン**:アプリパブリッシャーは Braze のデータを使用して、パーソナライズされたリッチなアプリ内エクスペリエンスを作成し、Judo の統合フックを使用して、アプリ内購入、有料サブスクリプション、またはコンテキストに基づくマーチャンダイジングを促進することができます。これらのエクスペリエンスへのアクセスは、Braze で作成されたエンゲージメントマーケティングキャンペーンによってトリガーできます。

**イベント駆動型コンテンツ**：スポーツやエンターテインメント分野では、Judo は主として、イベントのプレビュー、プロモーション、要約のためのリッチなエクスペリエンスを構築する目的で使用されています。この機能は、他の業種でも季節的なコンテンツやニュースに基づくコンテンツに幅広く応用できます。イベントをタイムリーに宣伝またはハイライトするメッセージングをリッチなアプリ内エクスペリエンスにリンクできるため、パブリッシャーは状況に即して対応することで、エンゲージメントを促進できます。

## サイドバイサイドの SDK 統合

Judoは、モバイルアプリにJudoとBraze SDKを並べて統合するために必要な作業の一部を自動化する追加ライブラリを提供している。 

### ステップ1:Judo Braze 統合ライブラリをインストールする

アプリにJudo-Braze統合ライブラリをインストールしてセットアップする。これにより、イベント追跡が自動的に有効になります。

- [iOSのインストール
手順](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android のインストール
手順](https://github.com/judoapp/judo-braze-android/wiki#installation)。

### ステップ2:アプリ内メッセージングを設定する

このステップでは、iOS および Android 用のカスタム `ABKInAppMessageControllerDelegate` および`IInAppMessageManagerListener` 実装を作成します。

各統合ライブラリに同梱されているアプリ内メッセージ設定ドキュメントを参照のこと：

- [iOSアプリ内メッセージ
セットアップ](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Androidアプリ内メッセージ
の設定](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup)。.

## この統合を使う

アプリ側の統合が完了したら、Judo エクスペリエンスの Braze アプリ内メッセージキャンペーンを実行してこの統合をテストし、期待どおりに実行されていることを確認できます。

### ステップ1:カスタムコードのアプリ内メッセージキャンペーンを作成する

Brazeプラットフォームから、**カスタムコードの**メッセージタイプでBrazeアプリ内メッセージキャンペーンを作成する。次に、カスタムタイプとして [**HTML Upload**] を選択します。メッセージのコンテンツに、ベースのアプリ内メッセージングのフィールドが取り込まれていることを確認してください。このコンテンツはユーザーには表示されません。

![「カスタムコード」メッセージタイプを選択したときのダッシュボードの画像。]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

次に、以下の最小限のHTMLスニペットを使って、フォームのバリデーションを満たす： 
```
<a href="appboy://close">X</a>
```

JudoがこれをJudoエクスペリエンスに書き換えて置き換えるので、これはあなたのデバイスの本番では表示されないことに注意してほしい。

![キャンペーンの作成ステップに追加されたフォーム検証コードを示す画像。]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### ステップ2: 柔道のキーと値のペアを設定する
![この統合に必要な１つのキー値ペアを示す画像。「キー」は「judo-experience」、「値」は Judo リンクです。.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

キャンペーンに[カスタムキーバリューペアを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)設定する。キーは`judo-experience` 。ここに表示したい柔道体験のURLを記入する。その後、Judo-Braze 統合ライブラリはハンドラーでこのキー値ペアを検出し、このペアを使用して Judo エクスペリエンスを標準 Braze アプリ内メッセージ UI の代わりに挿入します。
<br><br>
### ステップ3:キャンペーンを終える

最後に、キャンペーンを完了し、キャンペーンのトリガーを設定し、[**配信**] セクションと [**ターゲットユーザー**] セクションで Segments からユーザーを選択します。Brazeアプリ内メッセージのさまざまな構成要素については、アプリ内メッセージの[記事を]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)参照。



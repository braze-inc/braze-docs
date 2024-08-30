---
nav_title: Judo
article_title: Judo
description: "この参考記事では、BrazeとJudoのパートナーシップについて概説している。Judoは、iOSおよびAndroidアプリに位置情報コンテキストとトラッキングを追加できる、コード不要のサーバー駆動型UIプラットフォームである。"
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judoは](https://judo.app)サーバー駆動型のUIプラットフォームで、パブリッシャーがアプリを更新することなく、リッチで魅力的なアプリ内ユーザー体験を効率的に提供できるようにする。

BrazeとJudoの統合は、キャンペーンやCanvasにオーダーメイドの体験を提供する。Brazeのキャンペーンでは、シンプルなテンプレート化されたランディングページ体験の代わりに、複数のスクリーン、モーダル、動画、カスタムフォント、ダークモードやアクセシビリティなどのサポート設定からなるコンテンツを組み込むことができる。Brazeのデータは、柔道エクスペリエンスでパーソナライズされたコンテンツをサポートするためにも使用されることがある。ユーザーイベントとエクスペリエンスからのデータは、アトリビューションとターゲティングのためにBrazeにフィードバックできる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 柔道アカウント | このパートナーシップを利用するには、[柔道](https://www.judo.app/)アカウントが必要である。 |
| 柔道SDK | 柔道SDKは、[iOS](https://github.com/judoapp/judo-ios/)および/または[Android](https://github.com/judoapp/judo-android)アプリに統合されなければならない。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

**オンボーディングで**ある：Judoを使用するアプリパブリッシャーは、リッチでネイティブなオンボーディング体験を構築し、展開する。これらの体験は、Brazeを介して調整されたパーソナライズされたクロスチャネル・オンボーディング・ジャーニーの1つの要素となる。様々なアプリ内フローの有効性をテストするために、アプリを更新することなく、パーソナライズされたエクスペリエンスを素早く更新することができる。

**コンバージョンだ**：アプリパブリッシャーは、Brazeのデータを使用して、パーソナライズされたリッチなアプリ内体験を作成し、Judoの統合フックを使用して、アプリ内購入、有料購読、またはコンテキスト・マーチャンダイジングを促進することができる。これらのエクスペリエンスへのアクセスは、Brazeで作成されたエンゲージメント・マーケティング・キャンペーンがトリガーとなる。

**イベント駆動型コンテンツ**：スポーツやエンターテインメントにおける柔道の主な用途は、イベントのプレビュー、プロモーション、総括のためのリッチな体験の構築である。この能力は、季節的なコンテンツやニュース主導のコンテンツなど、他の業種にも幅広く応用できる。イベントをタイムリーに宣伝したり強調したりするメッセージングをリッチなアプリ内体験にリンクさせることで、パブリッシャーは文脈に即したエンゲージメントを促進することができる。

## サイド・バイ・サイドのSDK統合

Judoは、モバイルアプリにJudoとBraze SDKを並べて統合するために必要な作業の一部を自動化する追加ライブラリを提供している。 

### ステップ1:柔道整復師の統合ライブラリをインストールする

アプリにJudo-Braze統合ライブラリをインストールしてセットアップする。これで自動的にイベント・トラッキングが有効になる。

- [iOSのインストール
指示](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [アンドロイドのインストール
instructions](https://github.com/judoapp/judo-braze-android/wiki#installation).

### ステップ2:アプリ内メッセージを設定する

このステップでは、iOSとAndroid用のカスタム`ABKInAppMessageControllerDelegate` 、`IInAppMessageManagerListener` 。

各統合ライブラリに同梱されているアプリ内メッセージ設定ドキュメントを参照のこと：

- [iOSアプリ内メッセージ
セットアップ](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Androidアプリ内メッセージ
セットアップ](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## この統合を使う

アプリ側の統合が完了したら、Judo Experience向けにテストBrazeアプリ内メッセージキャンペーンを実行してテストし、期待通りに実行されることを確認することができる。

### ステップ1:カスタムコードのアプリ内メッセージキャンペーンを作成する

Brazeプラットフォームから、**カスタムコードの**メッセージタイプでBrazeアプリ内メッセージキャンペーンを作成する。次に、カスタムタイプとして**HTMLアップロードを**選択する。このコンテンツはユーザーには表示されない。

![カスタムコード」メッセージタイプを選択したときのダッシュボードのイメージ。][2]

次に、以下の最小限のHTMLスニペットを使って、フォームのバリデーションを満たす： 
```
<a href="appboy://close">X</a>
```

JudoがこれをJudoエクスペリエンスに書き換えて置き換えるので、これはあなたのデバイスの本番では表示されないことに注意してほしい。

![キャンペーンの作成ステップに追加されたフォーム検証コードを示す画像。][3]

### ステップ2:柔道のキーと値のペアを設定する
![この画像は、この統合に必要な1つのキーと値のペアを示している。「キー」は「柔道経験」で、「値」はあなたの柔道リンクである。][4]{: style="float:right;max-width:50%;margin-left:15px;"}

キャンペーンに[カスタムキーバリューペアを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)設定する。キーは`judo-experience` 。ここに表示したい柔道体験のURLを記入する。Judo-Braze統合ライブラリーは、ハンドラーでこのキーと値のペアを検出し、標準のBrazeアプリ内メッセージUIの代わりにJudo Experienceを注入するために使用する。
<br><br>
### ステップ3:キャンペーンを終える

最後に、キャンペーンのトリガーを設定し、**配信と** **ターゲットユーザーの**セクションでセグメントを介してユーザーを選択し、キャンペーンを完了する。Brazeアプリ内メッセージのさまざまな構成要素については、アプリ内メッセージの[記事を]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/)参照。


[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}

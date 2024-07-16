---
nav_title: Judo
article_title:Judo
description:「この参考記事では、BrazeとJudoのパートナーシップについて概説しています。Judoはコード不要のサーバー駆動型UIプラットフォームで、iOSアプリとAndroidアプリにロケーションコンテキストとトラッキング, 追跡を追加することができます。「
alias: /partners/judo/
page_type: partner
search_tag:Partner

---

# Judo

> [Judoはサーバー駆動型のUIプラットフォームで](https://judo.app)、パブリッシャーはアプリを更新しなくても、リッチで魅力的なアプリ内ユーザーエクスペリエンスを効率的に提供できます。

BrazeとJudoのインテグレーションにより、キャンペーンやキャンバスにオーダーメイドのエクスペリエンスを提供できます。シンプルなテンプレート形式のランディングページエクスペリエンスの代わりに、Brazeキャンペーンには、複数の画面、モーダル、動画、カスタムフォント、およびサポート設定（ダークモードやアクセシビリティなど）を含むコンテンツや、コードなしで構築され、アプリを更新せずにデプロイされるダークモードやアクセシビリティなどのサポート設定が含まれる場合があります。Brazeのデータは、Judo 体験のパーソナライズされたコンテンツをサポートするためにも使用できます。ユーザーイベントやエクスペリエンスからのデータを Braze にフィードバックして、アトリビューションやターゲティングに役立てることができます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Judo アカウント | このパートナーシップを利用するには、[Judo](https://www.judo.app/) アカウントが必要です。 |
| Judo SDK | Judo SDK は [iOS](https://github.com/judoapp/judo-ios/) アプリや [Android](https://github.com/judoapp/judo-android) アプリに統合されている必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

**オンボーディング**:Judo を使用するアプリパブリッシャーは、豊富なネイティブオンボーディングエクスペリエンスを構築してデプロイします。こうした体験は、Brazeを通じてパーソナライズされたクロスチャネルのオンボーディングジャーニーの1つの要素として活用できるようになりました。さまざまなアプリ内フローの効果をテストするために、アプリを更新せずにエクスペリエンスをパーソナライズされたしてすばやく更新できます。

**変換**:アプリパブリッシャーは、Brazeのデータを利用してパーソナライズされたリッチなアプリ内体験を構築し、Judoのインテグレーションフックを使用してアプリ内購入、有料購読、文脈に応じた or 状況に即したマーチャンダイジングを促進できます。これらのエクスペリエンスへのアクセスは、Braze で作成されたエンゲージメントマーケティングキャンペーンを通じてトリガーされる場合があります。

**イベント駆動型コンテンツ**:スポーツやエンターテイメントにおけるJudo の主な用途は、イベントのプレビュー、宣伝、まとめのための豊富な体験を構築することです。この機能は、季節限定のコンテンツやニュース主導型のコンテンツなど、他の業種でも幅広く使用されています。イベントをタイムリーに宣伝したり強調したりするためのメッセージングを、豊富なアプリ内エクスペリエンスとリンクさせることで、パブリッシャーはコンテキストに関連性を持たせることでエンゲージメントを促進できます。

## サイドバイサイド SDK 統合

Judo には、Judo SDK と Braze SDK をモバイルアプリに並べて統合するのに必要な作業の一部を自動化する追加ライブラリが用意されています。 

### ステップ1:Judo-Braze インテグレーションライブラリーをインストールする

Judo-Braze 統合ライブラリーをアプリにインストールして設定します。これにより、イベントトラッキング, 追跡が自動的に有効になります。

- [iOS インストール
指示](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Android インストール
指示](https://github.com/judoapp/judo-braze-android/wiki#installation)。

### ステップ2:アプリ内メッセージングの設定

このステップには、`ABKInAppMessageControllerDelegate` `IInAppMessageManagerListener` iOSとAndroid用のカスタムと実装の作成が含まれます。

各統合ライブラリに同梱されているアプリ内メッセージ設定ドキュメントを参照してください。

- [iOS アプリ内メッセージング
セットアップ](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Android アプリ内メッセージング
セットアップ](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup)。

## このインテグレーションを使用する

アプリ側の統合が完了したら、Judo ExperienceのテストBrazeアプリ内メッセージキャンペーンを実行してテストし、期待どおりに動作することを確認できます。

### ステップ1:カスタムコードアプリ内メッセージキャンペーンを作成する

Braze プラットフォームから、**カスタムコードメッセージタイプの** Braze アプリ内メッセージキャンペーンを作成します。次に、カスタムタイプとして \[**HTML アップロード**] を選択します。メッセージの内容には、必ず基本的なアプリ内メッセージングフィールドを入力してください。この内容はユーザーには表示されません。

![「カスタムコード」メッセージタイプを選択したときのダッシュボードの外観の画像, 写真。][2]

次に、以下の最小限の HTML スニペットを使用してフォームの検証を行います。 
```
<a href="appboy://close">X</a>
```

Judoはこれを書き換えてJudo Experienceに置き換えるため、本番環境ではデバイスに表示されないことに注意してください。

![キャンペーン作成ステップに追加されたフォーム検証コードを示す画像, 写真。][3]

### ステップ2:Judo 道のキーと値のペアを設定する
![この画像, 写真は、この統合に必要な1つのキーと値のペアを示しています。「キー」は「Judo 経験」で、「値」は柔道リンクです。][4]{: style="float:right;max-width:50%;margin-left:15px;"}

[というキーを使用してキャンペーンにカスタムのキーと値のペアを設定します]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)。`judo-experience`見せたいJudo 体験のURLをここに入力してください。Judo-Braze統合ライブラリーは、ハンドラーでこのキーと値のペアを検出し、それを使用して標準のBrazeアプリ内メッセージUIの代わりにJudoエクスペリエンスを注入します。
<br><br>
### ステップ3:キャンペーン終了

最後に、キャンペーントリガー設定、****配信セクションとターゲットユーザーセクションのセグメントでユーザーを選択してキャンペーン****を完了します。[Brazeアプリ内メッセージのさまざまなコンポーネントに関するアプリ内メッセージ記事をご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/)。


[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}

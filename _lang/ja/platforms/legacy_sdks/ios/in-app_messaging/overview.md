---
nav_title: 概要
article_title: iOS 向けアプリ内メッセージの概要
platform: iOS
page_order: 0
description: "この参考記事では、iOS のアプリ内メッセージングの種類、期待される動作、いくつかのユースケースについて説明します。"
channel:
  - in-app messages
search_rank: 4
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージ

[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。様々なレイアウトやカスタマイズツールから選べるので、アプリ内メッセージはこれまで以上にユーザーを惹きつけます。

アプリ内メッセージの[事例については、ケーススタディを](https://www.braze.com/customers)ご覧いただきたい。

## アプリ内メッセージのタイプ

Braze は現在、以下のアプリ内メッセージタイプをデフォルトで提供しています。 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信に渡って高度にカスタマイズできます。

すべてのアプリ内メッセージは、`ABKInAppMessage` のサブクラスであり、すべてのアプリ内メッセージの基本動作と特徴を定義しています。アプリ内メッセージのクラス構造は以下の通りです。

![ABKInAppMessageクラスがABKInAppMessageSlideup、ABKInAppMessageImmersive、ABKInAppMessageHTMLのルートクラスであることを示す図。ABKInAppMessage には、メッセージ、エクストラ、持続時間、クリックアクション、URI、閉じるアクション、アイコンの向き、テキストの配置などのカスタマイズ可能なプロパティが含まれています。ABKInAppMessageSlideup には、シェブロンやスライドアップアンカーなどのカスタマイズ可能なプロパティが含まれています。ABKInAppMessageImmersive には、ヘッダー、[閉じる] ボタン、フレーム、アプリ内メッセージボタンなどのカスタマイズ可能なプロパティが含まれています。ABKInAppMessageHTMLを使うと、HTMLアプリ内メッセージボタンクリックを手動で記録できる。]({% image_buster /assets/img_archive/ABKInAppMessage-models.png %})

{% alert important %}
デフォルトでは、アプリ内メッセージは、GIF サポートを含む標準 SDK インテグレーションを完了した後に有効になります。
<br><br>
iOS アプリ内メッセージまたはコンテンツカード内の画像を表示するために Braze UI を使用しようとしている場合は、`SDWebImage` の統合が必要です。
{% endalert %}

### メッセージタイプ別に予想される動作

ユーザーが既定のアプリ内メッセージタイプの1つを開くと、次のようになります。

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![携帯電話の画面の下部からスライドして表示されるアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの下端に表示されています。(]({% image_buster /assets/img/slideup-behavior.gif %})){: style="border:0px;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) アプリ内のメッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに有用で、最大2つのクリックアクションと分析対応ボタンを装備できます。

![携帯電話の画面中央のモーダルアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの中央に表示されています。(]({% image_buster /assets/img/modal-behavior.gif %})){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

[`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大 2 つのクリックアクションと分析対応ボタンが表示されます。

![携帯電話の画面全体に表示されるアプリ内メッセージには、「人間は複雑だ。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの中央に大きく表示されています。(]({% image_buster /assets/img/full-screen-behavior.gif %})){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のフルメッセージコンテンツは、`WKWebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。<br><br>iOS アプリ内メッセージは、HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェイスをサポートしています。詳細については、[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)を参照してください。

次の例は、ページ分割された HTML の完全アプリ内メッセージを示しています。

![コンテンツのカルーセルとインタラクティブなボタンを備えたHTMLのアプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})()

完全なアプリ内メッセージコンテンツは、`WKWebView` に表示され、オプションで画像やフォントなどの他のリッチコンテンツを含めることができ、メッセージの外観や機能を完全に制御できます。現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。

{% alert note %}
iOS SDK バージョン 3.19.0 から、以下の JavaScript メソッドは HTML のアプリ内メッセージではノーオペレーションとなりました: `alert`、`confirm`、`prompt`。
{% endalert %}

{% endtab %}
{% endtabs %}


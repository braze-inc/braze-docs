---
nav_title: 統合
article_title: Web 用アプリ内メッセージの統合
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "この記事には、アプリ内メッセージタイプと Web アプリケーションのメッセージ動作に関するリソースが含まれています。"
search_rank: 2
---

# アプリ内メッセージ統合

> この記事では、ウェブアプリケーションのアプリ内メッセージの設定方法について説明する。

[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。アプリ内メッセージでは、さまざまなレイアウトとカスタマイズツールを選択できるため、これまで以上にユーザーの関心を引き付けることができます。

アプリ内メッセージの[事例については、ケーススタディを](https://www.braze.com/customers)ご覧いただきたい。

## アプリ内メッセージのタイプ

Braze は現在、以下のアプリ内メッセージタイプをデフォルトで提供しています。 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信にわたってカスタマイズできます。

すべてのアプリ内メッセージは、そのプロトタイプを [[`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)] から継承します。このプロトタイプは、すべてのアプリ内メッセージの基本動作と特徴を定義しています。プロトタイプのサブクラスは以下の通りである。 [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)および [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

## メッセージタイプ別に予想される動作

ユーザーがデフォルトのアプリ内メッセージタイプの 1 つを開くと、次のようになります。

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) アプリ内メッセージは、伝統的にモバイルプラットフォームでは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられている。Braze Web SDK では、これらのメッセージは、Web の主流のパラダイムに合わせて Growl または Toast スタイルの通知として表示されます。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![携帯電話の画面の下部からスライドして表示されるアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの下端に表示されています。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに有用で、最大2つのクリックアクションと分析対応ボタンを装備できます。

![携帯電話の画面中央のモーダルアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの中央に表示されています。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab フルスクリーン %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。狭いブラウザウィンドウ (例えばモバイル Web) では、`full` アプリ内メッセージがブラウザウィンドウ全体を占めます。大きなブラウザウィンドウでは、`full` アプリ内メッセージは、`modal` アプリ内メッセージと同様に表示されます。`full` アプリ内メッセージの上半分には画像が含まれ、下半分には最大8行のテキストと最大2つのクリックアクション、アナリティクス対応ボタンが表示される。

![携帯電話の画面全体に表示されるアプリ内メッセージには、「人間は複雑だ。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの中央に大きく表示されています。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab カスタムHTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML は、iFrame に表示され、画像やフォント、動画、インタラクティブ要素などのリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全にコントロールできます。これらは、HTML 内から Braze Web SDK のメソッドを呼び出すためのJavaScript `brazeBridge` インターフェイスをサポートしています。詳しくは、[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)を参照してください。

{% alert important %}

Web SDK を介して HTML アプリ内メッセージを有効にするには、`allowUserSuppliedJavascript` 初期化オプションを Braze に指定する**必要があります**。例: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由からだ。HTML のアプリ内メッセージは JavaScript を実行できるため、サイト管理者が有効にする必要があります。

{% endalert %}

次の例は、ページ分割されたHTMLアプリ内メッセージを示している：

![コンテンツのカルーセルとインタラクティブボタンを含む HTML アプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## 統合

デフォルトでは、アプリ内メッセージは、推奨される [統合手順]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).追加のカスタマイズは、このガイドの手順に従って行うことができます。


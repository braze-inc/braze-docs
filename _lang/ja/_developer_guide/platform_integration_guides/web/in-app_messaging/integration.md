---
nav_title: 統合
article_title: ウェブ用アプリ内メッセージ統合
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "この記事には、アプリ内メッセージ・タイプとウェブ・アプリケーションのメッセージ動作に関するリソースが含まれている。"
search_rank: 2
---

# アプリ内メッセージ統合

> この記事では、ウェブアプリケーションのアプリ内メッセージの設定方法について説明する。

[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。アプリ内メッセージでは、さまざまなレイアウトとカスタマイズツールを選択できるため、これまで以上にユーザーの関心を引き付けることができます。

アプリ内メッセージの事例を見るには、\[ケーススタディ][53] ] をチェックしよう。

## アプリ内メッセージのタイプ

Braze は現在、以下のアプリ内メッセージタイプをデフォルトで提供しています。 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、アナリティクス、表示、配信をカスタマイズできる。

すべてのアプリ内メッセージは、そのプロトタイプを \[`InAppMessage`][2]] から継承する。このプロトタイプは、すべてのアプリ内メッセージの基本動作と特徴を定義している。プロトタイプのサブクラスは \[`SlideUpMessage`][3]] 、 \[`ModalMessage`][6]] 、 \[`FullScreenMessage`][7]] 、 \[`HtmlMessage`][12]] である。

## メッセージタイプ別に予想される動作

ユーザーがデフォルトのアプリ内メッセージタイプの 1 つを開くと、次のようになります。

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) アプリ内メッセージは、伝統的にモバイルプラットフォームでは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられている。Braze Web SDKでは、これらのメッセージは、Webの支配的なパラダイムに合わせるために、よりGrowlまたはToastスタイルの通知として表示される。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![携帯電話の画面下部からスライドするアプリ内メッセージには「人間は複雑だ」と表示されている。カスタム・エンゲージメントはそうあるべきでない。背景には、ウェブページの下隅に表示されているのと同じアプリ内メッセージがある。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに有用で、最大2つのクリックアクションと分析対応ボタンを装備できます。

![携帯電話の画面中央にモーダルなアプリ内メッセージが表示され、「人間は複雑だ」と表示される。カスタム・エンゲージメントはそうあるべきでない。背景には、ウェブページの中央に表示されているのと同じアプリ内メッセージがある。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab フルスクリーン %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。狭いブラウザウィンドウ（例えばモバイルウェブ）では、`full` アプリ内メッセージがブラウザウィンドウ全体を占める。より大きなブラウザウィンドウでは、`full` アプリ内メッセージは、`modal` アプリ内メッセージと同様に表示される。`full` アプリ内メッセージの上半分には画像が含まれ、下半分には最大8行のテキストと最大2つのクリックアクション、アナリティクス対応ボタンが表示される。

![携帯電話の画面全体に表示されるアプリ内メッセージには、「人間は複雑だ。カスタム・エンゲージメントはそうあるべきでない。背景には、同じアプリ内メッセージがウェブページの中央に大きく表示されている。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab カスタムHTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義のHTMLはiFrame内に表示され、画像、フォント、ビデオ、インタラクティブ要素などのリッチコンテンツを含むことができる。これらは、HTML内からBraze Web SDKのメソッドを呼び出すためのJavaScript`brazeBridge` インターフェイスをサポートしている。

{% alert important %}

Web SDKを通じてHTMLアプリ内メッセージを有効に**するには**、Brazeに`allowUserSuppliedJavascript` の初期化オプションを与える**必要がある**。例えば、`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})` 。これはセキュリティ上の理由からだ。HTMLのアプリ内メッセージはJavaScriptを実行できるため、サイト管理者が有効にする必要がある。

{% endalert %}

次の例は、ページ分割されたHTMLアプリ内メッセージを示している：

![] （{% image_buster /assets/img_archive/ios-html-full-iam.gif %} ）。

{% endtab %}
{% endtabs %}

## 統合

][1]デフォルトでは、アプリ内メッセージは自動的に表示される。このガイドのステップに従うことで、さらなるカスタマイズが可能だ。

[1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html
[6]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html
[12]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[53]: https://www.braze.com/customers

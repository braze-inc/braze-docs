---
nav_title: 統合
article_title: Web用アプリ内メッセージ統合
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "この記事には、ウェブアプリケーションのアプリ内メッセージタイプとメッセージ動作に関するリソースが含まれています。"
search_rank: 2
---

# アプリ内メッセージ統合

> この記事では、ウェブアプリケーションのアプリ内メッセージを設定する方法について説明します。

[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。アプリ内メッセージでは、さまざまなレイアウトとカスタマイズツールを選択できるため、これまで以上にユーザーの関心を引き付けることができます。

[ケーススタディ][6] でアプリ内メッセージの例をチェックしましょう。

## アプリ内メッセージのタイプ

Braze は現在、以下のアプリ内メッセージタイプをデフォルトで提供しています。 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信に渡って高度にカスタマイズできます。

すべてのアプリ内メッセージは、すべてのアプリ内メッセージの基本的な動作と特性を定義する [\`InAppMessage\`] [2] のプロトタイプを継承します。プロトタイプのサブクラスは [\`SlideUpMessage\`] [3]、[\`ModalMessage\`] [6]、[\`フルスクリーンメッセージ\`] [7]、[\`\`HTMLメッセージ\`] [12] です。

## メッセージタイプ別に予想される動作

ユーザーがデフォルトのアプリ内メッセージタイプの 1 つを開くと、次のようになります。

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) アプリ内メッセージは、従来のモバイルプラットフォームでは、画面の上部または下部から「上」または「下にスライド」していたため、このように呼ばれています。Braze Web SDKでは、これらのメッセージは、ウェブの支配的なパラダイムに合わせて、どちらかというとGrowlまたはToastスタイルの通知として表示されます。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![An in-app message sliding from the bottom of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the bottom corner of a web page.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) アプリ内のメッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに有用で、最大2つのクリックアクションと分析対応ボタンを装備できます。

![A modal in-app message in the center of a phone screen displaying "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed in the center of a web page.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。狭いブラウザウィンドウ（モバイルウェブなど）では、`full`アプリ内メッセージがブラウザウィンドウ全体に表示されます。大きなブラウザウィンドウでは、`full``modal`アプリ内メッセージはアプリ内メッセージと同様に表示されます。`full`アプリ内メッセージの上半分には画像が含まれ、下半分には最大8行のテキスト、最大2回のクリックアクション、分析対応ボタンが表示されます。

![A full screen in-app message shown across an entire phone screen displaying, "Humans are complicated. Custom engagement shouldn't be." In the background is the same in-app message displayed largely in the center of a web page.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義のHTMLはiFrameに表示され、画像、フォント、ビデオ、インタラクティブ要素などの豊富なコンテンツを含む場合があり、メッセージの外観と機能を完全に制御できます。これらは HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェースをサポートしています。詳細については、[ベストプラクティスをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)。

{% alert important %}

Web SDK を使用して HTML アプリ内メッセージを有効にするには、Braze `allowUserSuppliedJavascript` に初期化オプション (例:) **を指定する必要があります**。`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`これはセキュリティ上の理由からです。HTML アプリ内メッセージは JavaScript を実行できるため、サイト管理者に有効にしてもらう必要があります。

{% endalert %}

次の例は、ページ分割された HTML アプリ内メッセージを示しています。

![An HTML in-app message with the a carousel of content and interactive buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## 統合

デフォルトでは、アプリ内メッセージは推奨される [統合手順] [1] の一部として自動的に表示されます。このガイドの手順に従うと、さらにカスタマイズできます。

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

---
nav_title: 統合
article_title: iOS 向けアプリ内メッセージの概要
platform: Swift
page_order: 0
description: "この記事では、Swift SDK のiOS アプリ内メッセージングタイプ、期待される動作、およびいくつかのユースケースについて説明します。"
channel:
  - in-app messages

---

# アプリ内メッセージ統合

> [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。様々なレイアウトやカスタマイズツールから選べるので、アプリ内メッセージはこれまで以上にユーザーを惹きつけます。

アプリ内メッセージの例については、[ケーススタディ][31]を参照してください。

## アプリ内メッセージのタイプ

Braze は現在、以下のアプリ内メッセージタイプをデフォルトで提供しています。 

- スライドアップ
- \- モーダル
- モーダルイメージ
- フル
- フルイメージ
- カスタム HTML
- コントロール

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信に渡って高度にカスタマイズできます。

アプリ内メッセージのプロパティと使用法の完全なリストについては、[`InAppMessage` クラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) を参照してください。

すべてのアプリ内メッセージは、`Braze.InAppMessage` の列挙型で、すべてのアプリ内メッセージの基本的な動作と特性を定義します。アプリ内メッセージの各タイプと対応する詳細は、以下のタブにリストされています。

### メッセージタイプ別に予想される動作

ユーザーが既定のアプリ内メッセージタイプの1つを開くと、次のようになります。

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![A slideup in-app message at the bottom and the top of a phone screen.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに役立つ、最大2 つのアナリティクス対応ボタンを装備できます。

![A modal in-app message in the center of a phone screen.]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。これらのメッセージは、`Modal` タイプに似ていますが、ヘッダーまたはメッセージテキストがないことが異なります。より重要なメッセージングに役立つ、最大2 つのアナリティクス対応ボタンを装備できます。

![A modal image in-app message in the center of a phone screen.]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大2 つの分析が有効なボタンが表示されます。

![A fullscreen in-app message shown across an entire phone screen.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) アプリ内メッセージは、`Full` アプリ内メッセージに似ていますが、ヘッダーまたはメッセージテキストは含まれません。このメッセージタイプは、ユーザー通信のコンテンツと影響を最大化するのに役立ちます。`Full Image` アプリ内メッセージには、画面全体にまたがるイメージが含まれ、最大2 つの分析が有効なボタンを表示するオプションがあります。

![A fullscreen image in-app message shown across an entire phone screen.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のフルメッセージコンテンツは、`WKWebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。<br><br>iOS アプリ内メッセージは、HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェイスをサポートしています。詳細については、[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)を参照してください。

次の例は、ページ分割された HTML の完全アプリ内メッセージを示しています。

![An HTML in-app message with a carousel of content and interactive buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。

{% endtab %}
{% tab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) アプリ内メッセージにはUI コンポーネントが含まれず、主に分析目的で使用されます。このタイプは、コントロールグループに送信されたアプリ内メッセージの受信を確認するために使用されます。

インテリジェントセレクションとコントロールグループの詳細については、[インテリジェントセレクション]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/)を参照してください。

{% endtab %}
{% endtabs %}


{% alert important %}
標準のSDK 統合には、GIF サポートを含むアプリ内メッセージを有効化する手順が含まれています。GIF サポートの詳細については、こちらの[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)を参照してください。
{% endalert %}


[30]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[31]: https://www.braze.com/customers

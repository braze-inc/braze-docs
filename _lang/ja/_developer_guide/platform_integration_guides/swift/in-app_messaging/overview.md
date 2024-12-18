---
nav_title: 統合
article_title: iOS 向けアプリ内メッセージの概要
platform: Swift
page_order: 0
description: "この記事では、Swift SDK に関する、iOS のアプリ内メッセージングの種類、期待される動作、いくつかのユースケースについて説明します。"
channel:
  - in-app messages

---

# アプリ内メッセージ統合

> [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)を使用すると、プッシュ通知でユーザーの日常を邪魔することなく、コンテンツをユーザーに届けることができます。カスタマイズされ調整されたアプリ内メッセージは、ユーザーエクスペリエンスが向上し、オーディエンスがアプリから最大限の価値を得るのに役立ちます。様々なレイアウトやカスタマイズツールから選べるので、アプリ内メッセージはこれまで以上にユーザーを惹きつけます。

アプリ内メッセージの[事例については、ケーススタディを](https://www.braze.com/customers)ご覧いただきたい。

## アプリ内メッセージのタイプ

Braze は現在、以下のアプリ内メッセージタイプをデフォルトで提供しています。 

- スライドアップ
- モーダル
- モーダルイメージ
- フル
- フル画像
- カスタムHTML
- コントロール

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信に渡って高度にカスタマイズできます。

アプリ内メッセージのプロパティと使用法の完全なリストについては、[`InAppMessage` クラスのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage)を参照してください。

すべてのアプリ内メッセージは、`Braze.InAppMessage` の列挙型であり、これによりすべてのアプリ内メッセージの基本動作と特徴が定義されます。アプリ内メッセージの各種類と対応する詳細が以下のタブに示されています。

### メッセージタイプ別に予想される動作

ユーザーが既定のアプリ内メッセージタイプの1つを開くと、次のようになります。

{% tabs %}
{% tab スライドアップ %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![電話機の画面の上部と下部にスライド式で表示されたアプリ内メッセージ。]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。よりクリティカルなメッセージングに有用で、最大2つのアナリティクス対応ボタンを装備できる。

![電話機の画面の中央に表示されたモーダルアプリ内メッセージ。]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab モーダル画像 %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。これらのメッセージは、ヘッダーやメッセージテキストがないことを除けば、`Modal` タイプに似ている。よりクリティカルなメッセージングに有用で、最大2つのアナリティクス対応ボタンを装備できる。

![電話機の画面の中央に表示されたモーダル画面のアプリ内メッセージ。]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab フルスクリーン %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大2つの分析対応ボタンが表示されます。

![携帯電話の画面全体に表示されるフルスクリーンのアプリ内メッセージ。]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab フルスクリーン画像 %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) アプリ内メッセージは、ヘッダーやメッセージテキストがないことを除けば、`Full` アプリ内メッセージと似ている。このメッセージタイプは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full Image` アプリ内メッセージには画面全体に広がる画像が含まれ、オプションで最大2つの分析対応ボタンが表示されます。

![携帯電話の画面全体に表示されるフルスクリーン画像のアプリ内メッセージ。]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab カスタムHTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のフルメッセージコンテンツは、`WKWebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。<br><br>iOS アプリ内メッセージは、HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェイスをサポートしています。詳細については、[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)を参照してください。

次の例は、ページ分割された HTML の完全アプリ内メッセージを示しています。

![コンテンツのカルーセルとインタラクティブなボタンを備えたHTMLのアプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。

{% endtab %}
{% tab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) アプリ内メッセージには UI コンポーネントは含まれず、主に分析用に使用されます。このタイプは、コントロールグループに送信されたアプリ内メッセージの受信を確認するために使用される。

インテリジェントセレクションとコントロールグループについては、[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)を参照してください。

{% endtab %}
{% endtabs %}


{% alert important %}
標準のSDK統合には、GIFサポートを含むアプリ内メッセージを有効にするステップが含まれている。GIF サポートの詳細については、こちらの[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support)を参照してください。
{% endalert %}



{% multi_lang_include developer_guide/prerequisites/web.md %} しかし、追加の設定は必要ない。

## メッセージの種類

すべてのアプリ内メッセージは、そのプロトタイプを [[`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)] から継承します。このプロトタイプは、すべてのアプリ内メッセージの基本動作と特徴を定義しています。プロトタイプのサブクラスは以下の通りである。 [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html)および [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信にわたってカスタマイズできます。

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) アプリ内メッセージは、伝統的にモバイルプラットフォームでは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられている。Braze Web SDK では、これらのメッセージは、Web の主流のパラダイムに合わせて Growl または Toast スタイルの通知として表示されます。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![携帯電話の画面の下部からスライドして表示されるアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、Webページの下隅に表示されるのと同じアプリ内メッセージがある。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) アプリ内のメッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに有用で、最大2つのクリックアクションと分析対応ボタンを装備できます。

![携帯電話の画面中央のモーダルアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、Webページの中央に表示されているのと同じアプリ内メッセージがある。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}

[`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。狭いブラウザウィンドウ (例えばモバイル Web) では、`full` アプリ内メッセージがブラウザウィンドウ全体を占めます。大きなブラウザウィンドウでは、`full` アプリ内メッセージは、`modal` アプリ内メッセージと同様に表示されます。`full` アプリ内メッセージの上半分には画像が含まれ、下半分には最大8行のテキストと最大2つのクリックアクション、アナリティクス対応ボタンが表示される。

![携帯電話の画面全体に表示されるアプリ内メッセージには、「人間は複雑だ。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージがWebページの中央に大きく表示されている。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Custom HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML は、iFrame に表示され、画像やフォント、動画、インタラクティブ要素などのリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全にコントロールできます。これらは、HTML 内から Braze Web SDK のメソッドを呼び出すためのJavaScript `brazeBridge` インターフェイスをサポートしています。詳しくは、[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)を参照してください。

{% alert important %}
Web SDK を介して HTML アプリ内メッセージを有効にするには、`allowUserSuppliedJavascript` 初期化オプションを Braze に指定する**必要があります**。例: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`。これはセキュリティ上の理由からだ。HTML のアプリ内メッセージは JavaScript を実行できるため、サイト管理者が有効にする必要があります。
{% endalert %}

次の例は、ページ分割されたHTMLアプリ内メッセージを示している：

![コンテンツのカルーセルとインタラクティブなボタンを備えたHTMLアプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

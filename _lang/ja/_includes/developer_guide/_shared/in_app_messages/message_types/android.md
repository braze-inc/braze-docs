
{% tab android %}
Brazeは複数のデフォルトアプリ内メッセージタイプを提供している。それぞれメッセージ、画像、[Font Awesome](https://fontawesome.com/icons?d=gallery&p=2)アイコン、クリックアクション、分析、カラースキームなどでカスタマイズ可能だ。

それらの基本的な動作と特性は、サブクラスと呼ばれる[`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html)インターフェイスによって定義される。`IInAppMessage`また、[`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)サブインターフェースも含まれており、これにより[`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html)アプリに閉じるボタン、クリックアクションボタン、分析[ボタンを](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html)追加できる。

{% alert important %}
覚えておいてほしいが、ボタンを含むアプリ内メッセージは、ボタンテキストを追加する前にクリックアクションを追加した場合、その`clickAction`メッセージが最終的なペイロードに含まれる。
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

`slideup` アプリ内メッセージオブジェクトは [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) を拡張します。

![携帯電話の画面の下部からスライドして表示されるアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、ウェブページの右下隅に表示されるのと同じアプリ内メッセージがある。]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングの場合に有用で、2 つのクリックアクションと分析対応ボタンを装備できます。

このメッセージタイプは[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)、抽象クラスであるのサブクラスだ。この抽象クラスはを実装しており`IInAppMessageImmersive`、ローカルで生成されるアプリ内メッセージにカスタム機能を追加する選択肢を提供する。

![携帯電話の画面中央のモーダルアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、ウェブページの中央に表示されるのと同じアプリ内メッセージがある。]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大 2 つのクリックアクションと分析対応ボタンが表示されます。

このメッセージタイプは を拡張しており[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)、ローカルで生成されるアプリ内メッセージにカスタム機能を追加する選択肢を提供する。

![携帯電話の画面全体に表示されるアプリ内メッセージには、「人間は複雑だ。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、ウェブページの中央付近に大きく表示された、同じアプリ内メッセージがある。]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のメッセージコンテンツは、`WebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。

このメッセージタイプは、のサブクラス[`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html)であるを実装している[`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)。

{% alert note %}
Androidでは、カスタムHTMLアプリ内メッセージ`target="_blank"`で設定されたリンクは、デバイスのデフォルトのウェブブラウザで開く。
{% endalert %}

Androidアプリ内メッセージは、HTML内からBraze Android SDKのメソッドを呼び出すためのJavaScript`brazeBridge`インターフェイスをサポートしている。詳細は<a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">JavaScriptブリッジ</a>のページを参照のこと。

![アプリ内メッセージのHTMLで、コンテンツのカルーセルとインタラクティブなボタンを備えている。]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
アプリ用にカスタムのアプリ内メッセージ表示を定義することもできる。完全な手順については、[「カスタムファクトリの設定」]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories)を参照せよ。
{% endalert %}
{% endtab %}
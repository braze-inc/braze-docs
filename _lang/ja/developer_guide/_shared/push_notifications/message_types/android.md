{% tab android %}
Braze には、メッセージ、"画像 s、[フォントアウェゾーム](https://fontawesome.com/icons?d=gallery&p=2)アイコン、アクションs、分析、カラースキームなど、カスタマイズ可能な複数のデフォルト アプリ内メッセージタイプが用意されています。

これらの基本的な動作と特性は、[`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) インターフェイスによって定義されます。[`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) と呼ばれるサブクラスで定義されます。`IInAppMessage` には、サブインターフェイス、[`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html) も含まれます。これにより、アプリにclose、click-アクション、および分析 [ボタン](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html)

{% alert important %}
ボタンを含むアプリ内メッセージs は、ボタンテキストを追加する前にクリックアクションが追加されている場合、最終的な支払い読み込むに`clickAction` メッセージを含めます。
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

`slideup` アプリ内メッセージオブジェクトは [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) を拡張します。

![携帯電話の画面の下部からスライドして表示されるアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの下端に表示されています。(]({% image_buster /assets/img/slideup-behavior.gif %})){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングの場合に有用で、2 つのクリックアクションと分析対応ボタンを装備できます。

このメッセージタイプは、[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html) のサブクラスです。これは、`IInAppMessageImmersive` を実装する抽象クラスで、ローカルに生成されたアプリ内メッセージs にカスタム機能を追加するオプションを提供します。

![携帯電話の画面中央のモーダルアプリ内メッセージに「人間は複雑だ」と表示されています。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの中央に表示されています。(]({% image_buster /assets/img/modal-behavior.gif %})){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大 2 つのクリックアクションと分析対応ボタンが表示されます。

このメッセージタイプは、[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html) を拡張し、ローカルで生成されたアプリ内メッセージs にカスタム機能を追加するオプションを提供します。

![携帯電話の画面全体に表示されるアプリ内メッセージには、「人間は複雑だ。カスタム・エンゲージメントはそうあるべきでない。バックグラウンドには、同じアプリ内メッセージが Web ページの中央に大きく表示されています。(]({% image_buster /assets/img_archive/In-App_Full.png %}))

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のメッセージコンテンツは、`WebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。

これらのメッセージ・インスタンス[`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)は、`IInAppMessage`サブクラス[`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html)を実装します。

Android アプリ内メッセージは、HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェイスをサポートしています。詳細については、<a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">ベストプラクティス</a>を参照してください。

![コンテンツのカルーセルとインタラクティブボタンを含む HTML アプリ内メッセージ。]({% image_buster /assets/img/full-screen-behavior.gif %})({: style="border:0px;"})

{% alert important %}
現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
また、アプリのカスタムアプリ内メッセージビューを定義することもできます。詳細については、[カスタムファクトリーの設定]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories)を参照してください。
{% endalert %}
{% endtab %}
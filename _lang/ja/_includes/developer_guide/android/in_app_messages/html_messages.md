{% multi_lang_include developer_guide/prerequisites/android.md %}

## HTMLメッセージについて

BrazeのJavaScriptインターフェイスを使えば、アプリ内のカスタムWebView内でBrazeを活用することができる。以下はその責任である。 [`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html)がレスポンシブである：

1. [ユーザーガイドに記載されているように、Braze JavaScriptブリッジをWebViewに注入する：HTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. WebViewから受け取ったブリッジメソッドを[Braze Android SDKに](https://github.com/braze-inc/braze-android-sdk)渡す。

## WebView へのインターフェースの追加

アプリの WebView から Braze 機能を使用するには、WebView に Braze JavaScript インターフェイスを追加します。インターフェイスが追加された後、[ユーザーガイドと同じAPIが利用できる：HTMLアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) はカスタムWebView内で利用できるようになる。

{% tabs %}
{% tab JAVA %}

```java
String javascriptString = BrazeFileUtils.getAssetFileStringContents(context.getAssets(), "braze-html-bridge.js");
myWebView.loadUrl("javascript:" + javascriptString);

final InAppMessageJavascriptInterface javascriptInterface = new InAppMessageJavascriptInterface(context, inAppMessage);
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val javascriptString = context.assets.getAssetFileStringContents("braze-html-bridge.js")
myWebView.loadUrl("javascript:" + javascriptString!!)

val javascriptInterface = InAppMessageJavascriptInterface(context, inAppMessage)
myWebView.addJavascriptInterface(javascriptInterface, "brazeInternalBridge")
```

{% endtab %}
{% endtabs %}

## YouTubeのコンテンツを埋め込む

YouTube やその他の HTML5コンテンツは、HTML アプリ内メッセージで再生できます。これには、アプリ内メッセージが表示されるアクティビティでハードウェアアクセラレーションが有効になっている必要があります。詳細については、[Android 開発者ガイド](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling)を参照してください。ハードウェアアクセラレーションは、Android API バージョン11以降でのみ利用できます。

以下は、HTML スニペットに YouTube 動画を埋め込んだ例です。

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```

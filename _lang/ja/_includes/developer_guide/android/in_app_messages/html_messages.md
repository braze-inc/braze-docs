{% multi_lang_include developer_guide/prerequisites/android.md %}

## HTMLについて

Braze JavaScript インターフェイスを使用すると、Brazeをアプリ内のカスタムWebView 内で活用できます。[`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html) は、以下の原因となります。

1. [ ユーザガイドに記載されているように、Braze JavaScript ブリッジをWebView に挿入します。HTML アプリ内メッセージs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages).
2. WebViewから受信したブリッジメソッドを[Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)に渡す。

## WebView へのインターフェースの追加

アプリの WebView から Braze 機能を使用するには、WebView に Braze JavaScript インターフェイスを追加します。インターフェイスが追加された後、[ ユーザガイドで使用できる同じAPI が使用可能になります。HTML アプリ内メッセージs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) は、ユーザ定義のWebView で使用できます。

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

## YouTubeコンテンツの埋め込み

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

## ディープリンクの使用

Android HTML アプリ内メッセージs でディープリンクまたは外部リンクを使用する場合、**do not** はJavaScript で`brazeBridge.closeMessage()` を呼び出します。SDKの内部ロジックは、リンクにリダイレクトすると、自動的にアプリ内メッセージを閉じます。`brazeBridge.closeMessage()` を呼び出すと、この処理が妨げられ、ユーザーがアプリに戻ったときにメッセージがレスポンシブでなくなることがあります。 

以下は、コード スニペットのディープリンクの例です。

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}
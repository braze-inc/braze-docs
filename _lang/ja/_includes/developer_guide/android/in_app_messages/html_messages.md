{% multi_lang_include developer_guide/prerequisites/android.md %}

## HTMLメッセージについて

BrazeのJavaScriptインターフェイスを使えば、アプリ内のカスタムWebView内でBrazeを活用できる。の責任[`InAppMessageJavascriptInterface`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.jsinterface/-in-app-message-javascript-interface/index.html)は次の通りである：

1. ユーザー[ガイドに記載されているように、WebViewにBraze JavaScriptブリッジを注入する。アプリ内HTMLメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)。
2. WebViewから受け取ったブリッジメソッドを[Braze Android SDK](https://github.com/braze-inc/braze-android-sdk)に渡す。

## WebView へのインターフェースの追加

アプリの WebView から Braze 機能を使用するには、WebView に Braze JavaScript インターフェイスを追加します。インターフェイスが追加された後、ユーザー[ガイドで利用可能な同じAPIが利用可能となる。HTML形式のアプリ内メッセージは、カスタムWebView]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages)内で利用可能となる。

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

## ディープリンクを使う

AndroidのHTMLアプリ内メッセージでディープリンクや外部リンクを使用する場合、JavaScript内で\``brazeBridge.closeMessage()``を呼び出して**はならない**。SDKの内部ロジックは、リンクにリダイレクトする際にアプリ内メッセージを自動的に閉じる。呼び出しはこの`brazeBridge.closeMessage()`プロセスを妨げ、ユーザーがアプリに戻った際にメッセージが応答しなくなる可能性がある。 

以下はコードスニペットにおけるディープリンクの例だ：

{% raw %}
```javascript
<script>
document.querySelectorAll('[data-button-id]').forEach(function (node)
Unknown macro: { node.addEventListener('click', function () { brazeBridge.logClick(node.dataset.buttonId); brazeBridge.closeMessage(); }); }
);
</script>
```
{% endraw %}
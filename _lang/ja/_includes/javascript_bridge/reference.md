カスタムHTMLアプリ内メッセージとバナーは、Braze SDKと連携するためのJavaScript「ブリッジ」をサポートしている。これにより、ユーザーがリンク付き要素をクリックしたり、コンテンツと何らかの形でエンゲージメントを行った際に、カスタムBrazeアクションをトリガーできる。これらの方法は、グローバル変数 `brazeBridge` または`appboyBridge` とともに存在します。

{% alert important %}
Brazeでは、グローバル変数`brazeBridge` の使用を推奨している。グローバル変数 `appboyBridge` は非推奨ですが、既存のユーザー向けに引き続き機能しています。`appboyBridge` を使用している場合は、`brazeBridge` に移行することをお勧めします。<br><br> `appboyBridge` は以下のSDKバージョンで非推奨となった：<br><br>
- Web:[3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android :[14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS:[4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

例えば、カスタム属性とカスタムイベントをログに記録し、メッセージを閉じるには、カスタムHTML内で以下のJavaScriptを使用できる：

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close the message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScriptブリッジ・メソッド {#bridge}

アプリ内メッセージとバナーのカスタムHTMLでは、以下のJavaScriptメソッドがサポートされている：

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Liquid を参照して、 <code>customAttributes</code> をJavaScript Bridge のメソッドに挿入することはできません。
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

### ボタンクリックのトラッキング

カスタムHTML内のクリックのトラッキングを行うには、メソッド`brazeBridge.logClick(button_id)`を使用する。

{% alert note %}
**バナー:**引数なしの only`brazeBridge.logClick()` のみがサポートされている。ボタンIDとカスタムボタントラッキングは、アプリ内メッセージでのみサポートされている。
{% endalert %}

アプリ内メッセージについては、プログラムで「ボタン1」「ボタン2」「本文クリック」をそれぞれ、`brazeBridge.logClick('1')` 、 `brazeBridge.logClick()`、 `brazeBridge.logClick('0')`を使ってトラッキングできる。

| クリック数     | 方法                       | サポート |
| ---------- | ---------------------------- | --------- |
| 本文クリック | `brazeBridge.logClick()`    | アプリ内メッセージとバナー |
| ボタン1   | `brazeBridge.logClick('0')` | アプリ内メッセージのみ |
| ボタン2   | `brazeBridge.logClick('1')` | アプリ内メッセージのみ |
| カスタムボタンのトラッキング |`brazeBridge.logClick('your custom name here')`| アプリ内メッセージのみ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

アプリ内メッセージについては、1回のインプレッションごとに複数のボタンクリックイベントをトラッキングできる。例えば、メッセージを閉じ、ボタン2のクリックを記録するには：

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
```

また、新しいカスタムボタンの名前 (キャンペーンあたり一意の名前を最大 100 個) も追跡できます。`brazeBridge.logClick('blue button')`、`brazeBridge.logClick('viewed carousel page 3')` などがあります。

{% alert tip %}
属性`onclick`内でJavaScriptメソッドを使用する場合、文字列値はシングルクォートで囲むこと。そうしないと、ダブルクォートで囲まれたHTML属性との衝突を避けるためだ。
{% endalert %}

#### 制限事項（アプリ内メッセージのみ）

- キャンペーンあたり最大 100 個の一意のボタン ID を設定できます。
- ボタン ID はそれぞれ最大 255文字です。
- ボタン ID には、英字、数字、スペース、ダッシュ、およびアンダースコアのみを使用できます。

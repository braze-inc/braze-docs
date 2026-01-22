{% multi_lang_include developer_guide/prerequisites/web.md %}

## 顧客スタイル

BrazeのUI要素はデフォルトの外観と操作感を備えており、ニュートラルなアプリ内メッセージ体験を提供し、他のBrazeモバイルプラットフォームとの一貫性を目指しています。デフォルトのBrazeスタイルは、Braze SDK内のCSSで定義されている。 

### デフォルトスタイルの設定

アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準アプリ内メッセージタイプをカスタマイズできます。 

たとえば、次の例はアプリ内メッセージのヘッダーをイタリックで表示する上書きを示しています。

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

詳細については[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)を参照してください。

### z-indexをカスタマイズする

デフォルトでは、アプリ内メッセージは `z-index: 9001` を使用して表示されます。これは、`inAppMessageZIndex ` [初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を使用して構成可能であり、あなたのWeb サイトがそれよりも高い値で要素をスタイルするシナリオで使用されます。

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
この機能は、Web Braze SDK v3.3.0以降でのみ使用できる。
{% endalert %}

## メッセージの破棄をカスタマイズする

デフォルトでは、アプリ内メッセージが表示されている場合、エスケープボタンを押すか、ページのグレーアウトした背景をクリックすると、メッセージが表示されなくなる。`requireExplicitInAppMessageDismissal` [初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を`true`に設定して、この動作を防ぎ、メッセージを消去するために明示的なボタンをクリックする必要があります。 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## リンクを新しいタブで開封する

新しいタブでアプリ内メッセージのリンクが開くように設定するには、`openInAppMessagesInNewTab` オプションを `true` に設定して、アプリ内メッセージでのクリックによるすべてのリンク先が新しいタブまたはウィンドウで開くように強制します。

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```

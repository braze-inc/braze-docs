---
nav_title: カスタムスタイリング
article_title: Web向けアプリ内メッセージのカスタムスタイリング
platform: Web
channel: in-app messages
page_order: 1
page_type: reference
description: "この記事では、Webアプリケーションのアプリ内メッセージングのカスタムスタイリングについて説明します。"

---

# カスタムスタイリング

> BrazeのUI要素はデフォルトの外観と操作感を備えており、ニュートラルなアプリ内メッセージ体験を提供し、他のBrazeモバイルプラットフォームとの一貫性を目指しています。Brazeのデフォルトスタイルは、Braze SDK内のCSSで定義されています。 

アプリケーションで選択したスタイルを上書きすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して標準アプリ内メッセージタイプをカスタマイズできます。 

たとえば、次の例はアプリ内メッセージのヘッダーをイタリックで表示する上書きを示しています。

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

詳細については[JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html)を参照してください。

## アプリ内メッセージ デフォルト z-index

デフォルトでは、アプリ内メッセージは `z-index: 9001` を使用して表示されます。これは、`inAppMessageZIndex ` [初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)を使用して構成可能であり、あなたのWeb サイトがそれよりも高い値で要素をスタイルするシナリオで使用されます。

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
このオプションはWeb SDK v3.3.0で導入されました。このオプションを使用するには、従来の SDK をアップグレードする必要があります。
{% endalert %}


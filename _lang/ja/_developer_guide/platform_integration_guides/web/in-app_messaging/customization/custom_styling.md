---
nav_title: カスタムスタイル
article_title: Web 用アプリ内メッセージカスタムスタイリング
platform: Web
channel: in-app messages
page_order: 1
page_type: reference
description: "この記事では、ウェブアプリケーションのアプリ内メッセージングのカスタムスタイルについて説明します。"

---

# カスタムスタイル

> Braze UI要素には、ニュートラルなアプリ内メッセージエクスペリエンスを実現し、他のBrazeモバイルプラットフォームとの一貫性を保つことを目的としたデフォルトのルックアンドフィールが付属しています。Braze のデフォルトスタイルは、Braze SDK 内の CSS で定義されます。 

アプリケーションで選択したスタイルをオーバーライドすることで、独自の背景画像、フォントファミリ、スタイル、サイズ、アニメーションなどを使用して、標準のアプリ内メッセージタイプをカスタマイズできます。 

たとえば、以下はアプリ内メッセージのヘッダーを斜体で表示するオーバーライドの例です。

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

詳細については、[JSDocs][2] を参照してください。

## アプリ内メッセージのデフォルト Z インデックス

デフォルトでは、`z-index: 9001`アプリ内メッセージはを使用して表示されます。これは、ウェブサイトがそれよりも高い値を持つ要素のスタイルを設定するシナリオでは、`inAppMessageZIndex `[初期化オプションを使用して設定できます][41]。

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
このオプションは Web SDK v3.3.0 で導入されました。このオプションを使用するには、古い SDK をアップグレードする必要があります。
{% endalert %}

[2]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html
[15]: https://fontawesome.com/?from=io
[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions

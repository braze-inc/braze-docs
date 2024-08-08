---
nav_title: インプレッション数とクリック数を記録する
article_title: インプレッション数とクリック数を記録する
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "この記事では、ウェブアプリケーションのアプリ内メッセージのインプレッションとクリックのロギングについて説明します。"

---

# インプレッション数とクリック数を記録する

> この記事では、ウェブアプリケーションのアプリ内メッセージのインプレッションとクリックを記録する方法について説明します。

[[アプリ内メッセージのインプレッションとクリックの記録は](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick)](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression)、`showInAppMessage``automaticallyShowInAppMessage`またはメソッドを使用すると自動的に実行されます。

どちらの方法も使用せず、独自のUIコードを使用してメッセージを手動で表示することを選択した場合は、次の方法を使用して分析を記録してください。

```javascript
// Registers that a user has viewed an in-app message with the Braze server.
braze.logInAppMessageImpression(inAppMessage);
// Registers that a user has clicked on the specified in-app message with the Braze server.
braze.logInAppMessageClick(inAppMessage);
// Registers that a user has clicked a specified in-app message button with the Braze server.
braze.logInAppMessageButtonClick(button, inAppMessage);
// Registers that a user has clicked on a link in an HTML in-app message with the Braze server.
braze.logInAppMessageHtmlClick(inAppMessage, buttonId?, url?)
```



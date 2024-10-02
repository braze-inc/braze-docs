---
nav_title: インプレッション数とクリック数を記録する
article_title: インプレッション数とクリック数を記録する
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "この記事では、Web アプリライケーションのアプリ内メッセージのインプレッションとクリックの記録について説明します。"

---

# インプレッション数とクリック数を記録する

> この記事では、Web アプリケーションのアプリ内メッセージのインプレッションとクリックを記録する方法について説明します。

アプリ内メッセージの[インプレッション](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression)と[クリック](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick)の記録は、`showInAppMessage` または `automaticallyShowInAppMessage` メソッドを使用すると自動的に実行されます。

どちらのメソッドも使用せず、独自のUI コードを使用して手動でメッセージを表示することを選択した場合は、次の方法を使用して分析を記録します。

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



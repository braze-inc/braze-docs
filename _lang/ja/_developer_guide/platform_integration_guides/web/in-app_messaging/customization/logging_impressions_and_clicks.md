---
nav_title: 印象とクリックの記録
article_title: 印象とクリックの記録
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "この記事では、ウェブアプリライケーションのログアプリ内メッセージ インプレッションとクリックについて説明します。"

---

# インプレッション数とクリック数を記録する

> ここでは、ウェブアプリライケーションのアプリ内メッセージ インプレッションとクリックを記録する方法について説明します。

`showInAppMessage`または`automaticallyShowInAppMessage`メソッドを使用すると、ログアプリ内メッセージ[インプレッションs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression)および[clicks](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick)が自動的に実行されます。

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



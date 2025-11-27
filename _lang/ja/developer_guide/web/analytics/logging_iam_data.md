{% multi_lang_include developer_guide/prerequisites/web.md %}

## メッセージデータのロギング

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

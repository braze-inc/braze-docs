{% multi_lang_include developer_guide/prerequisites/web.md %}

## Protokollierung von Nachrichten-Daten

Die Protokollierung der [Impressionen](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) und [Klicks](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) von In-App-Nachrichten erfolgt automatisch, wenn Sie die Methode `showInAppMessage` oder `automaticallyShowInAppMessage` verwenden.

Wenn Sie keine der beiden Methoden verwenden und sich dafür entscheiden, die Nachricht manuell über Ihren eigenen UI Code anzuzeigen, verwenden Sie die folgenden Methoden zur Protokollierung von Analytics:

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

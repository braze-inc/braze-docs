{% multi_lang_include developer_guide/prerequisites/web.md %}

## Logging message data

Logging in-app message [impressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) and [clicks](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) is performed automatically when you use the `showInAppMessage` or `automaticallyShowInAppMessage` method.

If you do not use either method and opt to manually display the message using your own UI code, use the following methods to log analytics:

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

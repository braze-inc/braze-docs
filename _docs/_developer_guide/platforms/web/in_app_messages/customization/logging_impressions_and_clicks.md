---
nav_title: Impressions and Clicks
article_title: Logging Impressions and Clicks
platform: Web
channel: in-app messages
page_type: reference
description: "This article covers logging in-app message impressions and clicks for your web application."

---

# Logging impressions and clicks

> This article covers how to log in-app message impressions and clicks for your web application.

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



---
nav_title: Logging Impressions and Clicks
article_title: Logging Impressions and Clicks
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "This article covers logging in-app message impressions and clicks for your web application."

---

# Logging impressions and clicks

Logging in-app message [impressions](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessageimpression) and [clicks](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#loginappmessagebuttonclick) is performed automatically when you use the `automaticallyDisplayInAppMessages` or `showInAppMessage`.

If you do not use either method and manually display the message using your own UI code then use the following methods to log analytics:

```javascript
// Registers that a user has viewed an in-app message with the Braze server.
braze.logInAppMessageImpression(message);
// Registers that a user has clicked on an in-app message with the Braze server.
braze.logInAppMessageButtonClick(button, message);
```



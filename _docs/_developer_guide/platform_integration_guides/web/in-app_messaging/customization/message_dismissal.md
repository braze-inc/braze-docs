---
nav_title: Message Dismissal
article_title: In-App Message Dismissal for Web
platform: Web
channel: in-app messages
page_order: 2
page_type: reference
description: "This article covers in-app message dismissal for your web application."

---

# Message dismissal

> This article covers how to handle in-app message dismissal for your web application.

By default, when an in-app message is showing, pressing the escape button or a click on the grayed-out background of the page will dismiss the message. Configure the `requireExplicitInAppMessageDismissal` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) to `true` to prevent this behavior and require an explicit button click to dismiss messages. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions

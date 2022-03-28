---
nav_title: Message Dismissal
article_title: In-App Message Dismissal for Web
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "This article covers customization of in-app messaging via the Braze SDK."

---

# In-app message dismissal

By default, when an in-app message is showing, pressing the escape button or a click on the greyed-out background of the page will dismiss the message. Configure the `requireExplicitInAppMessageDismissal` [initialization option][41] to `true` to prevent this behavior and require an explicit button click to dismiss messages. 

```javascript
import braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions

---
nav_title: Key-Value Pairs
article_title: In-App Message Key-Value Pairs for Web
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "This article covers customization of in-app messaging via the Braze SDK."

---

# Key-value pairs

In-app message objects may carry key-value pairs as their `extras` property. These are specified on the dashboard under **Settings** when creating an in-app message campaign. These can be used to send data with an in-app message for further handling by your site. For example:

```javascript
import braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  if (inAppMessage instanceof braze.InAppMessage) {
    var extras = inAppMessage.extras;
    if (extras) {
      for (var key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.display.showInAppMessage(inAppMessage);
});
```

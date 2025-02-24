---
nav_title: Key-Value Pairs
article_title: In-App Message Key-Value Pairs for Web
platform: Web
channel: in-app messages
page_type: reference
description: "This article covers how to leverage in-app messaging key-value pairs to display information for your web application."

---

# Key-value pairs

> This article covers how to leverage in-app messaging key-value pairs to display information for your web application.

In-app message objects may carry key-value pairs as their `extras` property. These are specified on the dashboard under **Settings** when creating an in-app message campaign. These can be used to send data with an in-app message for further handling by your site. For example:

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```

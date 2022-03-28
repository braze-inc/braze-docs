---
nav_title: Custom Styling
article_title: In-App Message Customization for Web
platform: Web
channel: in-app messages
page_order: 3
page_type: reference
description: "This article covers customization of in-app messaging via the Braze SDK."

---

# Custom styling

Braze UI elements come with a default look and feel that create a neutral in-app message experience and aim for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, you can customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause an in-app message's headers to appear italicized:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

See the [JSDocs][2] for more information.

## In-app message default z-index

By default, in-app messages are displayed using `z-index: 1050`. This is configurable using the `inAppMessageZIndex ` [initialization option][41] in the scenario that your website styles elements with higher values than that.

```javascript
import braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 9001
});
```

{% alert important %}
This option was introduced in Web SDK v3.3.0. Older SDKs must be upgraded to use this option.
{% endalert %}

[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[15]: https://fontawesome.com/?from=io
[41]: https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions


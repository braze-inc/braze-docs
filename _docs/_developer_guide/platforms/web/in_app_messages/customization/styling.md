---
nav_title: Styling
article_title: In-App Message Custom Styling for Web
platform: Web
channel: in-app messages
page_type: reference
description: "This article covers in-app messaging custom styling for your web application."

---

# Custom in-app message styling

> Braze UI elements come with a default look and feel that create a neutral in-app message experience and aim for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. 

## Example

By overriding selected styles in your application, you can customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more. 

For instance, the following is an example override that will cause an in-app message's headers to appear italicized:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) for more information.

## In-app message default z-index

By default, in-app messages are displayed using `z-index: 9001`. This is configurable using the `inAppMessageZIndex ` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) in the scenario that your website styles elements with higher values than that.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
This option was introduced in Web SDK v3.3.0. Older SDKs must be upgraded to use this option.
{% endalert %}

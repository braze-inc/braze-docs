{% multi_lang_include developer_guide/prerequisites/web.md %}

## Custom styles

Braze UI elements come with a default look and feel that create a neutral in-app message experience and aim for consistency with other Braze mobile platforms. The default Braze styles are defined in CSS within the Braze SDK. 

### Setting a default style

By overriding selected styles in your application, you can customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more. 

For instance, the following is an example override that will cause an in-app message's headers to appear italicized:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

See the [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html) for more information.

### Customizing the z-index

By default, in-app messages are displayed using `z-index: 9001`. This is configurable using the `inAppMessageZIndex ` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) in the scenario that your website styles elements with higher values than that.

```javascript
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    inAppMessageZIndex: 12000
});
```

{% alert important %}
This feature is only available for Web Braze SDK v3.3.0 and later.
{% endalert %}

## Customizing message dismissals

By default, when an in-app message is showing, pressing the escape button or a click on the grayed-out background of the page will dismiss the message. Configure the `requireExplicitInAppMessageDismissal` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) to `true` to prevent this behavior and require an explicit button click to dismiss messages. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Opening links in a new tab

To set your in-app message links to open in a new tab, set the `openInAppMessagesInNewTab` option to `true` to force all links from in-app message clicks open in a new tab or window.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```

## Setting key-value pairs

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

## Logging impressions and clicks

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

## Customizing message dismissals

By default, when an in-app message is showing, pressing the escape button or a click on the grayed-out background of the page will dismiss the message. Configure the `requireExplicitInAppMessageDismissal` [initialization option](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) to `true` to prevent this behavior and require an explicit button click to dismiss messages. 

```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY", {
    baseUrl: "YOUR-API-ENDPOINT",
    requireExplicitInAppMessageDismissal: true
});
```

## Configuring links to open in a new tab

To set your in-app message links to open in a new tab, set the `openInAppMessagesInNewTab` option to `true` to force all links from in-app message clicks open in a new tab or window.

```javascript
braze.initialize('api-key', { openInAppMessagesInNewTab: true} );
```

## Message styling

Braze UI elements come with a default look and feel that create a neutral in-app message experience and aim for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. 

### Customizing the styling

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
This option was introduced in Web SDK v3.3.0. Older SDKs must be upgraded to use this option.
{% endalert %}

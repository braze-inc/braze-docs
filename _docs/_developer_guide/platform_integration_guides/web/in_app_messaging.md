---
nav_title: In-App Messaging
platform: Web
page_order: 2
search_rank: 5
---
# In-App Messaging

In-App Messages are great for creating unobtrusive calls to action, notifying people of new content in the News Feed and driving them toward it, or communicating with users who have push turned off. They are also effective for other content that isn't time-sensitive enough to warrant a push notification, or permanent enough to warrant a News Feed item. You can find a detailed explanation of in-app message behavior on [Braze Academy][4].

## Integration

By default, in-app messages are automatically displayed as part of our [recommended integration instructions][1]. Additional customization can be done by following the steps in this guide.

## In-App Message Types

Braze currently offers the following default in-app message types: [`Slideup`][13], [`Modal`][17], and [`Full`][41] and [`HTML`][42].  Each in-app message type is customizable across content, images, icons, click actions, analytics, display, and delivery.

All in-app messages inherit their prototype from [`appboy.ab.InAppMessage`][2], which defines basic behavior and traits for all in-app messages. The protypical subclasses are [appboy.ab.SlideUpMessage][3], [appboy.ab.ModalMessage][6], [appboy.ab.FullScreenMessage][7], and [appboy.ab.HtmlMessage][12].

### Slideup In-App Messages

[`SlideUp`][3] in-app messages are so-named because traditionally on mobile platforms they "slide up" or "slide down" from the top or bottom of the screen. In the Braze Web SDK, these messages are actually displayed as more of a Growl or Toast style notification, to align with the web's dominant paradigm. They cover a small portion of the screen and provide an effective and non-intrusive messaging capability.

![Slideup Example][49]

### Modal In-App Messages

[`Modal`][6] in-app messages appear in the center of the screen and are framed by a translucent panel. Useful for more critical messaging, they can be equipped with up to two click action and analytics enabled buttons.

![Modal Example][48]

### Full In-App Messages

[`Full`][7] in-app messages are useful for maximizing the content and impact of your user communication. On narrow browser windows (e.g. the mobile web), `full` in-app messages take up the entire browser window. On larger browser windows, `full` in-app messages appear similarly to `modal` in-app messages. The upper half of a `full` in-app message contains an image and the lower half allows up to eight lines of text as well as up to two click action and analytics enabled buttons

![Full Example][47]

### HTML In-App Messages

[`HTML`][12] in-app messages are useful for creating fully customized user content. User-defined HTML is displayed in an iframe and may contain rich content, such as images, fonts, videos, and interactive elements, allowing for full control over message appearance and functionality. These support a Javascript `appboyBridge` interface to call methods on the Braze Web SDK from within your HTML, see [Best Practices][52] for more details.

>  To enable HTML in-app messages, your SDK integration must supply the `enableHtmlInAppMessages` initialization option to Braze, e.g. `appboy.initialize('YOUR-API_KEY', {enableHtmlInAppMessages: true})`. This is for security reasons - HTML in-app messages can execute javascript so we require a site maintainer to enable them.

The following example shows a paginated HTML in-app message:

![HTML5 Example][51]

## In-App Message Delivery

### In-App Messages (Triggered)

The following documentation refers to Braze's `In-App Messaging` product, aka "triggered in-app messages," which are branded as highlighted below in the "Create Campaign" drop-down:

![In-App Messaging Composer][30]

You may also refer to the documentation for our deprecated [`Original In-App Messaging`][33] product.

#### Trigger Types

Our in-app message product allows you to trigger in-app message display as a result of several different event types: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Furthermore, `Specific Purchase` and `Custom Event` triggers can contain robust property filters.

#### Delivery Semantics
All in-app messages that a user is eligible for are automatically delivered to the user upon a session start event. For more information about the SDK's session start semantics, see our [session lifecycle documentation][10].

#### Minimum Time Interval Between Triggers
By default we rate limit in-app messages to once every 30 seconds to ensure a quality user experience. To override this value, you can pass the `minimumIntervalBetweenTriggerActionsInSeconds` configuration option to your [`initialize`][9] function.

```js
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
appboy.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```

### Manual In-App Message Display

If you don't want your site to immediately display new in-app messages when they're received, you can disable automatic display and register your own display subscribers. First, find and remove the call to `appboy.display.automaticallyShowNewInAppMessages()` from within your loading snippet.  Then, create your own subscriber:

```javascript
appboy.subscribeToNewInAppMessages(function(inAppMessages) {
  // Display the first in-app message. You could defer display here by pushing this message to code within in your own application.
  // If you don't want to use Braze's built-in display capabilities, you could alternatively pass the in-app message to your own display code here.
  appboy.display.showInAppMessage(inAppMessages[0]);

  // Return an array with any remaining, unhandled messages to Braze's internal queue.
  // These will be part of the inAppMessages param the next time this subscriber is invoked.
  return inAppMessages.slice(1);
});
```

The `inAppMessages` parameter will be an array of [`appboy.ab.InAppMessage`][2] subclass or [`appboy.ab.ControlMessage`][8] objects, each of which has various lifecycle event subscription methods. See the [JSDocs][2] for full documentation.

>  Only one [`Modal`][17] or [`Full`][41] in-app message can be displayed at a given time. If you attempt to show a second Modal or Full message while one is already showing, `appboy.display.showInAppMessage` will return false, and the message will automatically be returned to Braze's internal queue, where it will part of the `inAppMessages` array parameter the next time your subscriber is invoked.

#### Local In-App Messages

In-app messages can also be created within your site and displayed locally in real-time.  All customization options available on the dashboard are also available locally.  This is particularly useful for displaying messages that you wish to trigger within the app in real-time. However, analytics on these locally-created messages will not be available within the Braze dashboard.

```javascript
  // Displays a slideup type in-app message.
  var message = new appboy.ab.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = appboy.ab.InAppMessage.SlideFrom.TOP;
  appboy.display.showInAppMessage(message);
```

### Exit-Intent Messages

Exit-intent in-app messages appear when visitors are about to navigate away from your site. They provide another opportunity to communicate important information to users, while not interrupting their experience on your site. To be able to send these messages, first reference the [open-source library][50] with the code below, which will log 'exit intent' as a custom event. In-app message campaigns can then be created in the dashboard using 'exit intent' as the trigger custom event.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { appboy.logCustomEvent('exit intent'); }
  });
```

## Customization {#in-app-message-customization}

### Key-Value Pair Extras

In-app message objects may carry key-value pairs as their `extras` property. These are specified on the dashboard under "Additional Message Settings" when creating an in-app message campaign. These can be used to send data down along with an in-app message for further handling by your site. For example:

```javascript
appboy.subscribeToNewInAppMessages(function(inAppMessages) {
  if (inAppMessages[0] instanceof appboy.ab.InAppMessage) {
    var extras = inAppMessages[0].extras;
    for (var key in extras) {
      if (data.hasOwnProperty(key)) {
         console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }

  appboy.display.showInAppMessage(inAppMessages[0]);
  return inAppMessages.slice(1);
});
```

### Custom Styling

Braze UI elements come with a default look and feel that matches the composers within the Braze Dashboard and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause a in-app messages' headers to appear italicized:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

See the [JSDocs][2] for more information.

{% include archive/troubleshooting_iams.md platform="Web" %}

[1]: https://github.com/Appboy/appboy-web-sdk#getting-started
[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/ab.SlideUpMessage.html
[4]: {{ site.baseurl }}//help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
[5]: #display-in-app
[6]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ModalMessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/ab.FullScreenMessage.html
[8]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ControlMessage.html
[9]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize
[10]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle
[11]: #inapp-customization
[12]: https://js.appboycdn.com/web-sdk/latest/doc/ab.HtmlMessage.html
[13]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[14]: #key-value
[15]: http://fortawesome.github.io/Font-Awesome/
[17]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[30]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[32]: #in-app-messages-triggered
[33]: #original-in-app-messages-deprecated
[35]: #styling
[40]: #message-types
[41]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[46]: #inapp-control
[47]: {% image_buster /assets/img_archive/In-App_Full.png %}
[48]: {% image_buster /assets/img_archive/In-App_Modal.png %}
[49]: {% image_buster /assets/img_archive/Web_Slideup.png %}
[50]: https://github.com/carlsednaoui/ouibounce
[51]: {% image_buster /assets/img_archive/ios-html-full-iam.gif %}
[52]: {{ site.baseurl }}/help/best_practices/in-app_messages/web_browsers_only/#web-html-messages
